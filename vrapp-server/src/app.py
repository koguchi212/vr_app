import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client
from dotenv import load_dotenv
import openai
import sqlite3
from trans_file import generate_new_glb_file

app = Flask(__name__)
CORS(app)

# .envファイルをロード
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

openai.api_key = os.getenv("CHATGPT_API_KEY")

def answer_chat_gpt(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "次の文章を画像生成用プロンプト(英語)に変換してください：" + question,
        }]
    )
    response = completion.choices[0].message['content']
    return response


@app.route('/', methods=['POST'])
def index():
    # データベースに接続
    database_path = os.path.join('..', 'database.db')
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    prompt = request.json.get('prompt')  # フロントエンドから受信したデータ

    # 新しいpromptをDBに保存
    c.execute("INSERT INTO prompts (prompt) VALUES (?)", (prompt,))
    conn.commit()

    response = answer_chat_gpt(prompt)  # promptをChatGPTに通して、回答を取得

    # データベースを検索して該当のpromptが存在するか確認
    c.execute("SELECT file_path FROM glb_files WHERE prompt=?", (prompt,))
    result = c.fetchone()

    if result:
        # promptが存在する場合は、該当のglbファイルパスを取得
        file_path = result[0]

    
    else:
        # Gradio APIを使用して3Dテキスト変換を行う
        client = Client("https://hysts-shap-e.hf.space/")
        result = client.predict(
            response,
            0,
            15,
            64,
            api_name="/text-to-3d"
        )
        
        print(result)

        # 新たなglbファイルを生成し、ファイルパスを取得
        file_path = generate_new_glb_file(result)

        # データベースにpromptとglbファイルパスを保存
        c.execute("INSERT INTO glb_files (prompt, file_path) VALUES (?, ?)", (prompt, file_path))
        conn.commit()

    # データベース接続を閉じる
    conn.close()

    print(response)  # responseを出力

    return jsonify({"response": response})
if __name__ == '__main__':
    app.run()

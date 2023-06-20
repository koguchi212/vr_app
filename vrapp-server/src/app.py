import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client
from dotenv import load_dotenv
import openai

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
    prompt = request.json.get('prompt')  # フロントエンドから受信したデータ

    # GPTによる回答
    response = answer_chat_gpt(prompt)

    # Gradio APIを使用して3Dテキスト変換を行う
    client = Client("https://hysts-shap-e.hf.space/")
    result = client.predict(
        response,
        0,
        15,
        64,
        api_name="/text-to-3d"
    )
    print(response)  # responseを出力
    print(result)

    glb_file_path = result
    file_path = os.getenv("FILE_PATH")  # 保存先のディレクトリとファイル名を指定

    with open(file_path, "w") as f:
        f.write(glb_file_path)

    return jsonify({"glb_file_path": glb_file_path})

if __name__ == '__main__':
    app.run()

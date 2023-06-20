import os
from flask import Flask, request
from flask_cors import CORS
from gradio_client import Client
from dotenv import load_dotenv

# .envファイルをロード
load_dotenv()


app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def index():
    prompt = request.json.get('prompt') # フロントエンドから受信したデータ

    client = Client("https://hysts-shap-e.hf.space/")
    result = client.predict(
        prompt,
        0,
        15,
        64,
        api_name="/text-to-3d"
    )
    print(prompt)
    print(result)
    glb_file_path = result
    file_path = os.getenv("FILE_PATH") # 保存先のディレクトリとファイル名を指定

    with open(file_path, "w") as f:
        f.write(glb_file_path)

    return {"glb_file_path": glb_file_path}

if __name__ == '__main__':
    app.run()

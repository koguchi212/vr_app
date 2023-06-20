import bpy
import os
from gradio_client import Client
from dotenv import load_dotenv
# .envファイルのパスを取得
dotenv_path = os.path.join(os.path.dirname(__file__))
load_dotenv(dotenv_path)
prompt = input("Enter a prompt: ")


client = Client("https://hysts-shap-e.hf.space/")
result = client.predict(
    prompt,
    0,
    15,
    64,
    api_name="/text-to-3d"
)
print(result)
glb_file_path = result

# 新しいシーンを作成
# bpy.ops.scene.new(type='NEW')

# オブジェクトをインポート
bpy.ops.import_scene.gltf(filepath=glb_file_path)

# インポートされたオブジェクトを選択
imported_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

# インポートされたオブジェクトをアクティブにする
if imported_objects:
    bpy.context.view_layer.objects.active = imported_objects[0]

# オブジェクトを選択状態にする
for obj in imported_objects:
    obj.select_set(True)

# カメラを設定
bpy.ops.object.camera_add(location=(0, -5, 2))
camera = bpy.context.object
bpy.context.scene.camera = camera

# レンダリング設定
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = os.getenv("RENDER_FILEPATH") # 保存先のディレクトリとファイル名を指定

# レンダリング実行
bpy.ops.render.render(write_still=True)



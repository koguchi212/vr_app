import os
import bpy
from dotenv import load_dotenv
# .envファイルのパスを取得
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


file_path = os.getenv("FILE_PATH") 




# オブジェクトをインポート
bpy.ops.import_scene.gltf(filepath=file_path)

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
bpy.context.scene.render.filepath =  os.getenv("RENDER_FILEPATH") 

# レンダリング実行
bpy.ops.render.render(write_still=True)

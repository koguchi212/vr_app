import os
import bpy
from dotenv import load_dotenv
import sqlite3

# .envファイルのパスを取得
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# データベースに接続
db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()


# 最新のpromptを取得
c.execute("SELECT prompt FROM prompts ORDER BY rowid DESC LIMIT 1")
latest_prompt = c.fetchone()


if latest_prompt:
    prompt = latest_prompt[0]

    # promptと一致するglbファイルパスのレコードを取得
    c.execute("SELECT file_path FROM glb_files WHERE prompt = ?", (prompt,))
    result = c.fetchone()

    if result:
        file_path = result[0]

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

    else:
            print("指定されたpromptに関連するglbファイルパスが見つかりません。")
else:
    print("promptが見つかりません。")
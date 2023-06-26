import os
import shutil

def generate_new_glb_file(result):
    # 新しいglbファイルを生成する処理を記述
    # 生成されたglbファイルのパスを返す

    if os.path.isfile(result):  # resultが存在するかチェック
        # glbファイルの保存先ディレクトリ
        glb_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'glb_file')

        # glbファイルのファイル名
        glb_filename = os.path.basename(result)

        # 新しいglbファイルのパス
        glb_file_path = os.path.join(glb_dir, glb_filename)

        # glbファイルを移動
        shutil.move(result, glb_file_path)

        return glb_file_path
    else:
        raise FileNotFoundError("指定されたパスが見つかりません。")

import os
import sqlite3

# SQLiteデータベース接続の設定
db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

# promptとfile_pathを追加する関数
def add_glb_file(prompt, file_path):
    c.execute("INSERT INTO glb_files (prompt, file_path) VALUES (?, ?)", (prompt, file_path))
    conn.commit()

# promptに一致するレコードを削除する関数
def delete_glb_file_by_prompt(prompt):
    c.execute("DELETE FROM glb_files WHERE prompt=?", (prompt,))
    conn.commit()

# # 使用例
# prompt = "example prompt"
# file_path = "example_file.glb"

# # レコードの追加
# add_glb_file(prompt, file_path)

# # レコードの削除
# delete_glb_file_by_prompt(prompt)

# データベース接続を閉じる
conn.close()

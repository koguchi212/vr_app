import os
import sqlite3

# データベースのパスを取得
database_path = os.path.join('..', 'database.db')

# データベースに接続
conn = sqlite3.connect(database_path)
c = conn.cursor()

# テーブルの作成
c.execute("CREATE TABLE IF NOT EXISTS prompts (prompt TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS glb_files (prompt TEXT, file_path TEXT)")

# 変更をコミット
conn.commit()

# データベース接続を閉じる
conn.close()

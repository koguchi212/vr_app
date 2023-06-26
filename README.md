# VR_APP:なりきり創造主


## プロトタイプ
- `vr_rpa.py`で標準入力でshap-eを試せます

## 事前準備
- `vrapp-server`下に`.env`を作成する
- blenderのアドオン設定をする
  
## データベース作成
- `vrapp-server/src`ディレクトリに移動して以下のコマンドを実行
  ```bash
    python database.py
  ```  

## サーバー起動
- `vrapp-front`ディレクトリに移動して以下のコマンドを実行
  ```bash
    yarn start
  ```  
- `vrapp-server/src`ディレクトリに移動して以下のコマンドを実行
  ```bash
    python app.py
  ```    
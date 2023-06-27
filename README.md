# VR_APP:なりきり創造主


## プロトタイプ
- `vr_rpa.py`で標準入力でshap-eを試せます

## 事前準備
- `vrapp-server`下に`.env`を作成する
- vscodeでblenderのアドオン設定をする
- `vrapp-front`をクローンする
  
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

## blenderで画像生成
- ブラウザから音声入力してpromptが返ってきたら、`vrapp-server/blender/blender.py`を開く
- `Ctrl`+`shift`+`P`で`Blender:start`を選び、blenderのパスを選択する
- blenderが起動したら、`Ctrl`+`shift`+`P`で`Blender:Run Script`を選択する

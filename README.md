# poms

Python Only で作る MicroServices

## クイックスタート

### 仮想環境の構築

事前に導入しておくもの

- Python3.10
- pipenv (`pip install pipenv`) ※Python3.10に入れてください

```shell
$ pipenv install
# 開発する場合
$ pipenv install --dev
```

### サーバの起動

両方起動してください。

```shell
#フロントエンド
$ pipenv run start-frontend
# バックエンド
$ pipenv run start-backend
```

- Webアプリ: <http://localhost:8501/>
- バックエンドドキュメント: <http://localhost:8000/docs>

アプリ画面
![](docs/images/app-page.png)
# Puchineko
Twitterクライアントっぽいものです。

## セッティング
1. /services/app/puchineko/keys.pyにTwitterのAPIキーを記述する
2. /で`docker-compose up -d --build`
3. localhost:1337で動作の確認ができる

## 開発するにあたってよく使うコマンド
以下のコマンドはdocker-compose.ymlのあるディレクトリでやってね。


dockerのコンテナ(アプリケーション＋webサーバー)の更新＆起動
```
$ docker-compose up -d --build
```

コンテナの状態を確認する。
```
$ docker-compose ps
```

コンテナの吐き出したログを見る。
```
$ docker-compose logs
```

コンテナに入る。コンテナにはpython3のモジュールがインストールされているので、コンテナに入ってpython3のインタープリターを起動すると書いたコードの動作を確認できて便利。
```
$ docker-compose exec web /bin/sh
```

webコンテナのpythonを起動。
```
$ docker-compose run web python3
```
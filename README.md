# Redis の教科書 — サンプルコード

書籍『Redis の教科書 — キャッシュ・キュー・運用とマネージドRedis』（森川 陽介 著）の companion code です。

各章の redis-cli スクリプト、`redis.conf` 設定例、Lua スクリプト、クライアント接続例（Go / Node.js / Python / Ruby）を章ごとのディレクトリにまとめています。

## 動作環境

- Redis 8.x（8.8 系で検証）
- Docker / Docker Compose（コンテナで Redis を起動する場合）
- redis-cli

## ディレクトリ構成

章ごとに `chNN-<topic>/` ディレクトリを用意します。各ディレクトリの `README.md` に起動方法と実行手順を記載します。

```
ch02-setup/        セットアップと疎通確認
ch03-data-types/   基本データ型と主要コマンド
ch04-cache/        キャッシュ設計
...
```

## 起動の基本

多くの章は Docker Compose で Redis 8 を起動します。

```bash
cd chNN-<topic>
docker compose up -d
redis-cli -h 127.0.0.1 -p 6379 PING
```

各章の詳細は、その章のディレクトリの `README.md` を参照してください。

## ライセンス

サンプルコードは書籍の読者が学習目的で自由に利用できます。

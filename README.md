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
ch02-setup/             セットアップと疎通確認
ch03-data-types/        基本データ型と主要コマンド
ch04-cache/             キャッシュ設計（cache-aside の Python 例つき）
ch05-session-lock/      セッション・レート制限・分散ロック（Lua つき）
ch06-ranking-pubsub/    ランキング・カウンタ・Pub/Sub
ch07-streams/           キューと Streams
ch08-persistence/       永続化とメモリ管理
ch09-ha-scale/          高可用性とスケール（replication / sentinel / cluster）
ch10-monitoring/        監視・障害対応・セキュリティ（exporter + Prometheus）
ch11-vector-sets/       Redis 8 の新機能と Vector Sets
ch12-managed/           マネージド Redis（移行スクリプト）
appendix-a-commands/    主要コマンド早見表（リファレンス）
appendix-b-comparison/  Redis / Valkey / Dragonfly / Memcached 比較
```

第1章（判断章）は実行するコードがないためディレクトリはありません。

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

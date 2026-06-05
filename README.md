# redis-textbook-examples

「**Redis の教科書 — キャッシュ・キュー・運用とマネージドRedis**」（森川 陽介 著）のサンプルコード集です。

本書の各章で使う redis-cli コマンド・`redis.conf` 設定例・Lua スクリプト・クライアント接続例（Go / Python）を、そのまま動かせる形で収録しています。すべて **Redis 8.8**（`redis:8-alpine`）で動作を確認しています。本書の `127.0.0.1:6379>` の出力は、ここの構成を実機で起動して取得した値です。

## 構成（全 12 章 + 付録 2）

各章のディレクトリ（`chNN-<topic>/`）に、その章のコマンド・設定・コードと実行手順（`README.md`）が入っています。

- [ch02-setup](ch02-setup/README.md) — セットアップと疎通確認（Docker / `redis.conf` / Go・Python クライアント）
- [ch03-data-types](ch03-data-types/README.md) — 基本データ型と主要コマンド
- [ch04-cache](ch04-cache/README.md) — キャッシュ設計（cache-aside の Python 例つき）
- [ch05-session-lock](ch05-session-lock/README.md) — セッション・レート制限・分散ロック（Lua スクリプトつき）
- [ch06-ranking-pubsub](ch06-ranking-pubsub/README.md) — ランキング・カウンタ・Pub/Sub
- [ch07-streams](ch07-streams/README.md) — キューと Streams
- [ch08-persistence](ch08-persistence/README.md) — 永続化とメモリ管理
- [ch09-ha-scale](ch09-ha-scale/README.md) — 高可用性とスケール（replication / sentinel / cluster の 3 構成）
- [ch10-monitoring](ch10-monitoring/README.md) — 監視・障害対応・セキュリティ（redis_exporter + Prometheus）
- [ch11-vector-sets](ch11-vector-sets/README.md) — Redis 8 の新機能と Vector Sets（VADD / VSIM）
- [ch12-managed](ch12-managed/README.md) — マネージド Redis（セルフホストからの移行スクリプト）
- [appendix-a-commands](appendix-a-commands/README.md) — 主要コマンド早見表（リファレンス）
- [appendix-b-comparison](appendix-b-comparison/README.md) — Redis / Valkey / Dragonfly / Memcached 比較

> 第1章（Redis をいつ使うかの判断章）は実行するコードがないため、ディレクトリはありません。

各章ディレクトリには、おおむね次が含まれます。

- `docker-compose.yml` — その章で使う Redis を起動する（`redis:8-alpine` = Redis 8.8.0）
- `examples/*.redis` — 本書の redis-cli コマンドの抜粋（`redis-cli < examples/xxx.redis` で実行）
- `examples/*.lua` / `app/*.py` — Lua スクリプトやアプリ側のコード例（該当章のみ）
- `*.conf` — `redis.conf` の設定例（該当章のみ）
- `README.md` — その章の起動方法と実行手順

## はじめかた

```bash
# 1. リポジトリを取得
git clone https://github.com/forest6511/redis-textbook-examples.git
cd redis-textbook-examples

# 2. 読みたい章のディレクトリへ移動して Redis を起動
cd ch03-data-types
docker compose up -d
redis-cli -h 127.0.0.1 -p 6379 PING        # => PONG

# 3. その章のコマンドをまとめて実行
redis-cli < examples/data-types.redis

# 4. 後片付け
docker compose down
```

各章の詳しい手順は、その章の `README.md` を参照してください。`ch09`（HA）と `ch10`（監視）は複数コンテナ構成のため、章 README に専用の手順があります。

## 動作環境

- Redis 8.8（`redis:8-alpine` で検証）
- Docker / Docker Compose
- `redis-cli`（ローカルにある場合。なければ `docker exec` 経由でも可）

## ライセンス

サンプルコードは、本書の読者が学習目的で自由に利用できます。

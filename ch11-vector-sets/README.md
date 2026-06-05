# ch11-vector-sets — Redis 8の新機能とVector Sets

『Redis の教科書』第章のサンプルです。本書の redis-cli コマンドを抜粋しています。

## 実行

```bash
docker compose up -d        # Redis 8.8 (redis:8-alpine) を起動
redis-cli < examples/vector-sets.redis
docker compose down         # 後片付け
```

`examples/*.redis` は本書の `127.0.0.1:6379>` プロンプトのコマンド列を抜き出したものです。出力は本書本文に掲載しています。

> Redis バージョン: 8.8.0（`redis:8-alpine`）

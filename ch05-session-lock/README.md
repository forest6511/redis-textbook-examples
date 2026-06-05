# ch05-session-lock — セッション・レート制限・分散ロック

『Redis の教科書』第5章のサンプルです。本書の redis-cli コマンドを抜粋しています。

## 実行

```bash
docker compose up -d        # Redis 8.8 (redis:8-alpine) を起動
redis-cli < examples/session-lock.redis
# Lua: redis-cli --eval examples/session-lock_1.lua lock:key , token
docker compose down         # 後片付け
```

`examples/*.redis` は本書の `127.0.0.1:6379>` プロンプトのコマンド列を抜き出したものです。出力は本書本文に掲載しています。

> Redis バージョン: 8.8.0（`redis:8-alpine`）

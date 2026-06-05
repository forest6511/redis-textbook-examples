# ch10-monitoring — 監視・障害対応・セキュリティ

『Redis の教科書』第10章のサンプルです。Redis 8.8（`redis:8-alpine`）。

## 監視スタック（Redis + redis_exporter + Prometheus）

```bash
docker compose up -d
# Prometheus: http://localhost:9090 で redis ターゲットを確認
redis-cli < examples/monitoring.redis   # INFO / SLOWLOG / LATENCY / ACL 等
docker compose down
```

`docker-compose.yml` は Redis 本体・`redis_exporter`（9121 でメトリクス公開）・Prometheus（9090）の 3 サービスです。`prometheus.yml` で exporter をスクレイプします。

## 設定例

- `redis-1.conf` — `bind` でインターフェースを限定し `protected-mode yes`（本番のネットワーク防御）
- `redis-2.conf` — 平文ポートを無効化し TLS のみにする例

## 注意

`examples/monitoring.redis` は本書の redis-cli コマンド抜粋です。本文の出力（`INFO` のメトリクス値、`SLOWLOG` エントリ、`ACL` の応答）は Redis 8.8 を実機で動かして取得しています。本書では「Docker 既定の `bind * -::*` + `protected-mode no` は本番と異なる」点も解説しています。

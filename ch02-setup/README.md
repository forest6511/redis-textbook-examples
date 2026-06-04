# 第2章 セットアップと最初の一歩

## 起動

```bash
docker compose up -d
redis-cli -h 127.0.0.1 -p 6379 PING   # => PONG
```

## redis-cli の例を流す

```bash
redis-cli -h 127.0.0.1 -p 6379 < examples/ping.redis
redis-cli -h 127.0.0.1 -p 6379 --scan --pattern "user:*:name"
```

## クライアント接続例

- `clients/connect.py` — redis-py(`pip install redis` 後に `python3 connect.py`)
- `clients/connect.go` — go-redis(`cd clients && go mod tidy && go run connect.go`)

## 後片付け

```bash
docker compose down -v
```

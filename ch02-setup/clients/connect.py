"""redis-py で Redis に接続する最小例。

decode_responses=True を付けると、バイト列ではなく
Python の文字列で値を受け取れる。
"""
import redis

# 単一の接続
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

print(r.set("user:1:name", "alice"))  # >>> True
print(r.get("user:1:name"))           # >>> alice


# コネクションプール(本番ではこちらを使い、接続の確立コストを抑える)
pool = redis.ConnectionPool().from_url("redis://localhost")
r1 = redis.Redis(decode_responses=True).from_pool(pool)
print(r1.get("user:1:name"))          # >>> alice
pool.close()

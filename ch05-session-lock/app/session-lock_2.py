import time
import redis

r = redis.Redis(decode_responses=True)

def allow(user_id, limit=100, window=60):
    key = f"rate:{user_id}"
    now = time.time()
    pipe = r.pipeline()
    pipe.zremrangebyscore(key, 0, now - window)  # 窓の外を削除
    pipe.zadd(key, {f"{now}": now})              # 今回のリクエスト
    pipe.zcard(key)                              # 窓内の件数
    pipe.expire(key, window)
    count = pipe.execute()[2]
    return count <= limit

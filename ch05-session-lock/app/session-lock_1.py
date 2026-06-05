import json
import redis

r = redis.Redis(decode_responses=True)

def save_session(session_id, data):
    key = f"session:{session_id}"
    # JSON 文字列にして 30 分の TTL を付ける
    r.set(key, json.dumps(data), ex=1800)

def load_session(session_id):
    key = f"session:{session_id}"
    raw = r.get(key)
    if raw is None:  # 失効済み or 未ログイン
        return None
    r.expire(key, 1800)  # アクセスのたびに期限を延長する
    return json.loads(raw)

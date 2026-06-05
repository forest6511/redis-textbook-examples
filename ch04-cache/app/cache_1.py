import redis

r = redis.Redis(decode_responses=True)

def get_product(product_id):
    key = f"cache:product:{product_id}"
    cached = r.get(key)
    if cached is not None:  # キャッシュヒット
        return cached
    # キャッシュミス: DB から取得し、TTL 付きで保存する
    value = fetch_from_db(product_id)
    r.set(key, value, ex=600)  # 600 秒で自動失効させ、古い写しを残さない
    return value

import random

# 基準 600 秒に 0-60 秒のばらつきを足し、同時失効を避ける
ttl = 600 + random.randint(0, 60)
r.set(key, value, ex=ttl)

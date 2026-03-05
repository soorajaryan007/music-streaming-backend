import redis
from config import Config

'''
redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    decode_responses=True
)

'''

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get(key):
    try:
        return redis_client.get(key)
    except Exception:
        print("Redis unavailable")
        return None


def set(key, value, ttl=3600):
    try:
        redis_client.set(key, value, ex=ttl)
    except Exception:
        print("Redis unavailable, cannot cache")
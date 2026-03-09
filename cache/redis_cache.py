import redis
from config import Config


class RedisCache:
    '''i got used'''
    def __init__(self):
        self.redis_client = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            decode_responses=True
        )

    def get(self, key):
        try:
            return self.redis_client.get(key)
        except Exception:
            print("Redis unavailable")
            return None

    def set(self, key, value, ttl=3600):
        try:
            self.redis_client.set(key, value, ex=ttl)
        except Exception:
            print("Redis unavailable, cannot cache")



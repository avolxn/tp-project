import json
import logging

import redis.asyncio as redis

from tp_project.core.config import get_settings

logger = logging.getLogger(__name__)


class CacheService:
    def __init__(self):
        self._redis: redis.Redis | None = None

    async def get_redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.from_url(get_settings().REDIS_URL, decode_responses=True)
        return self._redis

    async def get(self, key: str) -> dict | None:
        """Получает значение из кэша"""
        try:
            r = await self.get_redis()
            data = await r.get(key)
            if data:
                logger.debug(f"Cache hit: {key}")
                return json.loads(data)
            logger.debug(f"Cache miss: {key}")
            return None
        except Exception as e:
            logger.warning(f"Redis get error: {e}")
            return None

    async def set(self, key: str, value: dict, ttl: int | None = None) -> bool:
        """Сохраняет значение в кэш"""
        try:
            r = await self.get_redis()
            ttl = ttl or get_settings().CACHE_TTL
            await r.set(key, json.dumps(value), ex=ttl)
            logger.debug(f"Cache set: {key}, ttl={ttl}")
            return True
        except Exception as e:
            logger.warning(f"Redis set error: {e}")
            return False

    async def close(self):
        """Закрывает соединение с Redis"""
        if self._redis:
            await self._redis.close()
            self._redis = None


_cache_service: CacheService | None = None


def get_cache_service() -> CacheService:
    global _cache_service
    if _cache_service is None:
        _cache_service = CacheService()
    return _cache_service

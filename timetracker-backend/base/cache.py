import datetime
import os
import threading
import uuid
from abc import abstractmethod
from typing import Dict, Callable
from base.base_objects import base_object, ThreadBase, CacheManagerBase, objects
import logging
from logging import config
from functools import lru_cache

CACHE_MODE_TTL: int = 1
CACHE_MODE_KEEP_FOREVER: int = 2
CACHE_MODE_REFRESH: int = 3


# wrapper for threads used in services
class CacheItem:
    mode: int  # 1 - TTL, 2 - KEEP_FOREVER, 3 - CACHE_MODE_REFRESH
    key: str
    obj: any
    ttl_seconds: int  # number of seconds to keep object in cache
    acquire_time: int  # acquire time in seconds to get object from original source again
    created_date: datetime.datetime  # cache item created date and time
    method: Callable
    used_count: int = 0  # how many times object in cache was used
    def __init__(self, key: str, obj: any, ttl_seconds: int, method: Callable):
        self.mode = CACHE_MODE_TTL
        self.created_date = datetime.datetime.now()
        self.key = key
        self.obj = obj
        self.ttl_seconds = ttl_seconds
        self.method = method
        self.acquire_time = 1
        self.used_count = 0
    def get_info(self) -> dict[str, any]:
        return {
            "mode": self.mode,
            "key": self.key,
            "ttl_seconds": self.ttl_seconds,
            "acquire_time": self.acquire_time,
            "created_date": self.created_date,
            "used_count": self.used_count
        }
    # if cache item is fresh
    def is_old(self):
        return not self.is_fresh()
    def is_fresh(self):
        match self.mode:
            case 2:
                return True
            case 1:
                return (datetime.datetime.now()-self.created_date).total_seconds() < self.ttl_seconds
            case _:
                return False


class LocalCache(CacheManagerBase):
    cache_items: dict[str, CacheItem]
    def __init__(self):
        super().__init__()
        objects.register_cache(self)
        self.created_date = datetime.datetime.now()
        logging.info("Creating CacheManager, creation time: " + str(self.created_date))
        self.cache_items = {}
    def get_infos(self) -> list[dict]:
        return list(map(lambda x: x.get_info(), self.cache_items.values()))
    def get_base_object_type(self) -> str:
        return "LocalCache"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "LocalCache"
    def initialize(self):
        logging.info("Initializing LocalCache, object_id: " + self.object_id)
        self.initialize_thread()
    # put cache item into cache storage
    def put(self, key: str, obj: any, method: any, ttl_seconds: int = 60):
        item = CacheItem(key, obj, ttl_seconds, method)
        self.cache_items[key] = item
    def get(self, key: str) -> CacheItem | None:
        if self.cache_items.__contains__(key):
            return self.cache_items[key]
        else:
            return None

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        # TODO: check inactive cache items
        return True


# Manager of all cache items
class CacheManager(CacheManagerBase):
    created_date: datetime.datetime  # creation date of this manager with cache items
    local_cache: CacheManagerBase
    redis_cache: CacheManagerBase
    chain_caches: list[CacheManagerBase]

    def __init__(self):
        super().__init__()
        objects.register_cache(self)
        self.created_date = datetime.datetime.now()
        logging.info("Creating CacheManager, creation time: " + str(self.created_date))
    def get_infos(self) -> list[dict]:
        return [
            {"local_cache": "local_cache"},
            {"redis_cache": "redis_cache"}
        ]
    def get_base_object_type(self) -> str:
        return "CacheManager"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "CacheManager"
    def initialize(self):
        logging.info("Initializing CacheManager, object_id: " + self.object_id)
        self.initialize_thread()
    # put cache item into cache storage
    def put(self, key: str, obj: any, method: any, ttl_seconds: int = 60):
        self.local_cache.put(key, obj, method, ttl_seconds)

    def get(self, key: str) -> CacheItem | None:
        return self.local_cache.get(key)

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        # TODO: check inactive cache items
        return True

    def with_cache(self, key: str, method: Callable[[str], any], mode: int = 1, ttl: int = 60) -> any:
        item: CacheItem | None = self.get(key)
        if item is None or item.is_old():
            obj = method(key)
            self.put(key, obj, method, ttl)
            return obj
        else:
            return item.obj


cache = CacheManager()

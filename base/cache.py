import datetime
import os
import threading
import uuid
from abc import abstractmethod
from typing import Dict, Callable
from base.base_objects import base_object, thread_base

CACHE_MODE_TTL: int = 1
CACHE_MODE_KEEP_FOREVER: int = 2
CACHE_MODE_REFRESH: int = 3

# wrapper for threads used in services
class CacheItem:
    mode: int  # 1 - TTL, 2 - KEEP_FOREVER, 3 - CACHE_MODE_REFRESH
    key: any
    obj: any
    ttl_seconds: int
    acquire_time: int
    created_date: datetime.datetime
    method: Callable
    used_count: int = 0
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

# Manager of all cache items
class CacheManager(thread_base):
    created_date: datetime.datetime  # creation date of this manager with cache items
    cache_items: dict[str, CacheItem]
    def __init__(self):
        super().__init__()
        self.created_date = datetime.datetime.now()
        print("Creating object manager, creation time: " + str(self.created_date))
        self.cache_items = {}
    def get_infos(self) -> list[dict]:
        return list(map(lambda x: x.get_info(), self.cache_items.values()))
    def get_base_object_type(self) -> str:
        return "CacheManager"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "CacheManager"
    def initialize(self):
        print("Initializing CacheManager")
        self.initialize_thread()
    # put cache item into cache storage
    def put(self, key: str, obj: any, method: any, ttl_seconds: int = 60):
        item = CacheItem(key, obj, ttl_seconds, method)
        self.cache_items[key] = item
    def get(self, key: str) -> CacheItem | None:
        item = self.cache_items[key]
        if item is None:
            return None
        else:
            return item
    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        # check inactive cache items
        return True
    def with_cache(self, key: str, method: Callable, ttl: int = 60) -> any:
        item: CacheItem | None = self.get(key)
        if item is None or item.is_old():
            obj = method()
            self.put(key, obj, method, ttl)
            return obj
        else:
            return item.obj


cache = CacheManager()

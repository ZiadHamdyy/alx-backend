#!/usr/bin/env python3
""" 3-lru_cache.py """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initializes the LIFO cache """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.lru.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            else:
                if key in self.lru:
                    self.lru.remove(key)
            self.lru.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache_data[key]
        return None

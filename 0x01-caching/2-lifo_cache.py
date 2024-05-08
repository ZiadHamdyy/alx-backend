#!/usr/bin/env python3
""" 2-lifo_cache.py """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initializes the LIFO cache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.stack.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None

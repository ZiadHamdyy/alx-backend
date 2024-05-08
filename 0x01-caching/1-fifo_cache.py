#!/usr/bin/env python3
""" 0-basic_cache.py """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initializes the FIFO cache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None

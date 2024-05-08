#!/usr/bin/env python3
""" 100-lfu_cache.py """
from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initializes the LIFO cache """
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if len(self.cache_data) == 0:
                    return
                freq = Counter(self.lfu)
                min_value = float("inf")
                least_freq = None
                for k, v in freq.items():
                    if v  < min_value:
                        min_value = v
                        least_freq = k
                discarded_key = self.cache_data[least_freq]
                del self.cache_data[least_freq]
                print("DISCARD:", discarded_key)
                self.lfu.remove(least_freq)
            else:
                if key in self.lfu:
                    self.lfu.remove(key)
            self.lfu.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            return self.cache_data[key]
        return None


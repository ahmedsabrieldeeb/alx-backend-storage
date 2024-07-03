#!/usr/bin/env python3
""" Exercise Redis """
import redis
import uuid
from typing import Union


class Cache():
    """ Cache Class """
    def __init__(self):
        """ Constructor to setup the cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in cache and return a key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

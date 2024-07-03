#!/usr/bin/env python3
""" Exercise Redis """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ Cache Class """
    def __init__(self):
        """ Constructor to setup the cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in cache and return a key

        Args:
            data: Data to store

        Returns:
            key: Key to access the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> \
            Union[str, bytes, int, float]:
        """
        Get data from cache

        Args:
            key: Key to get its value
            fn (=None): Function to convert the data

        Returns:
            data: Converted data
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get data from cache as string

        Args:
            key: Key to get its value

        Returns:
            data: Data as string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get data from cache as integer

        Args:
            key: Key to get its value

        Returns:
            data: Data as integer
        """
        return self.get(key, fn=int)

#!/usr/bin/env python3
"""
Cache class with method call counting using Redis INCR command.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increment the count in Redis and call the original method.
        """
        # Use the method's qualified name as the key
        key = method.__qualname__
        # Increment the count in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    
    return wrapper

class Cache:
    """
    Cache class that interacts with Redis to store and retrieve data, with method call counting.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    @count_calls
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    @count_calls
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.
        """
        return self.get(key, lambda d: int(d))

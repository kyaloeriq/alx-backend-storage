#!/usr/bin/env python3
"""
Cache class implementation using Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """Cache class that interacts with Redis to store data."""

    def __init__(self) -> None:
        """Initialize the Cache instance and flush the Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.
        
        Args:
            data: Data to be stored (str, bytes, int, float).
        
        Returns:
            str: The randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

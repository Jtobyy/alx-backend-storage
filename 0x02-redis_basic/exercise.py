#!/usr/bin/env python3
'''Writing strings to Redis'''
from uuid import uuid4
from typing import Union
import redis


class Cache:
    '''Stores an instance of the redis client'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key

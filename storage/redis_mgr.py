# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

import redis


class RedisManager(object):
    def __init__(self, url, db):
        # self.redis_client = redis.StrictRedis(host=host, port=port, db=db)
        # pool = redis.ConnectionPool(host=host, port=port, db=db)
        pool = redis.ConnectionPool.from_url(url=url, db=db)
        self.redis_client = redis.Redis(connection_pool=pool)

    def pop_msg(self, redis_key):
        fetch_data = self.redis_client.lpop(redis_key)
        return fetch_data

    def push_msg(self, redis_key, msg):
        p_res = self.redis_client.rpush(redis_key, msg)
        return p_res

    def push_msgs(self, redis_key, msgs: list):
        try:
            with self.redis_client.pipeline(transaction=False) as pipe:
                for msg in msgs:
                    pipe.rpush(redis_key, msg)
                pipe.execute()
        except Exception as exec:
            print(exec)
        else:
            print('success')
    pass


REDIS_CLS = None


def redis_cls():
    global REDIS_CLS
    if REDIS_CLS is None:
        REDIS_CLS = RedisManager('redis://@localhost:6379', 0)
    return REDIS_CLS


if __name__ == "__main__":
    key = 'tbk_api_cats'
    # print(redis_cls().redis_client.info())
    # print(redis_cls().push_msg(key, '3367117'))
    # print(redis_cls().redis_client.keys())
    # print(redis_cls().pop_msg(key))
    # print(redis_cls().redis_client.delete(key))
    print(redis_cls().redis_client.llen(key))

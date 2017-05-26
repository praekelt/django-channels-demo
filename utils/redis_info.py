#!/usr/bin/env python
from pprint import pprint
import time
import redis

GROUP_NAMES = ["subscribers"]


def get_redis_connection():
    return redis.StrictRedis(host='localhost', port=6379, db=0)

def get_channel_message_counts(r=None, mask="*:message_count"):
    r = r or get_redis_connection()

    result = {}
    for key in r.keys("*:messages_count"):
        result[key] = r.get(key)

    return result

def get_subscriber_group_sizes(r=None, groups=GROUP_NAMES):
    r = r or get_redis_connection()

    result = {}
    for name in groups:
        result[name] = r.zcard("asgi::group:" + name)

    return result

def get_key_ttls(r=None, mask="*"):
    r = r or get_redis_connection()

    result = {}
    for key in r.keys(mask):
        result[key] = r.ttl(key)

    return result


if __name__ == "__main__":
    r = get_redis_connection()
    while True:
        print("Message counts:")
        pprint(get_channel_message_counts())
        print("Subscriber groups sizes:")
        pprint(get_subscriber_group_sizes())
        print("Time to live:")
        pprint(get_key_ttls())
        time.sleep(1)





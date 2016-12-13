#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

from test_0001 import *
import redis

genes = gene_activation_code(20)
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
# r.flushdb()
count = r.dbsize()

for i in range(count, count + len(genes)):
    r.set(i, genes[i - count])

print(r.dbsize())

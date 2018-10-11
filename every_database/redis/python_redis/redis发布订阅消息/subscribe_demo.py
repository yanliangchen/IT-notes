#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''订阅方'''
import  sys

reload(sys)

sys.setdefaultencoding('utf-8')
from  redishelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe(channel='liyanliang')

while True:
    msg = redis_sub.parse_response()
    print('接收：'.decode(),msg)
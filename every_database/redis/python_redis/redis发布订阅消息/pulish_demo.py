#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
发布者
'''
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
from  redishelper import RedisHelper

obj = RedisHelper()
#订阅了100次
n = 1
while True :
    if  n <=100:
        obj.public(chanel='liyanliang',msg='no usr  moren')
    else:
        obj.unsubscribe(chanel='liyanliang')
        print('取消订阅')
        break
    n+=1
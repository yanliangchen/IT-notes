#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import  sys
reload(sys)

sys.setdefaultencoding('utf-8')
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='163.53.91.47', password='123456', port=6379)
        # self.chan_sub = 'test'
        # self.chan_pub = 'test'

#发送消息
    def public(self,chanel='moren',msg='1'):
        self.__conn.publish(chanel,msg)
        return True
#订阅
    def subscribe(self,channel='moren'):
        #打开收音机
        pub = self.__conn.pubsub()
        #调频道
        pub.subscribe(channel)
        #准备接收
        pub.parse_response()
        return pub

    def  unsubscribe(self,chanel='moren'):
        pub = self.__conn.pubsub()
        pub.unsubscribe(chanel)
        return  pub

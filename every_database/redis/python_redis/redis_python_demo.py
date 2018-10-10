#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
安装见centos7安装redis.md
python安装redis :  pip  install  redis
'''

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

import  redis

pool = redis.ConnectionPool(host='163.53.91.47', password='123456', port=6379)
r = redis.Redis(connection_pool=pool)
def demo_one():
    '''
    redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，
    StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
    :return:
    '''
    r = redis.Redis(host='163.53.91.47',password='123456',port=6379)
    r.set('foo', 'Bar')
    print (r.get('foo'))
# demo_one()


def demo_second():
    '''
    redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，
    每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，
    这样就可以实现多个Redis实例共享一个连接池。
    :return:
    '''
    pool = redis.ConnectionPool(host='163.53.91.47',password='123456',port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('fooaaaa', 'Baraaaa')
    print r.get('fooaaaa')

# demo_second()

def demo_three():
    '''
    在Redis中设置值，默认，不存在则创建，存在则修改
    参数：
         ex，过期时间（秒）
         px，过期时间（毫秒）
         nx，如果设置为True，则只有name不存在时，当前set操作才执行
         xx，如果设置为True，则只有name存在时，岗前set操作才执行
    :return:
    '''
    pool = redis.ConnectionPool(host='163.53.91.47', password='123456', port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set("name", "hehe", ex=5)  # 保留时长 5秒
    print(r.get("name"))  # 获取字段
    r.mset({'k1': 'v1', 'k2': 'v2'}) # 支持字典格式
    print(r.get("k2"))


# demo_three()


def demo_mset():
    # 批量设置
    r.mset(name="liyanliang",age=18,abc='a',ddd='aaa')
    print(r.get('name'))
    print(r.get('age'))
# demo_mset()

def demo_mget():
    #批量获取
    print(r.mget("name","age")) # ['xixi', '18']
    r.set("name","koka")
    print(r.get("name"))# koka
# demo_mget()

def demo_getset():
    #设置新值并获取原来的值
    print(r.getset("name","def"))

# demo_getset()

def demo_getrange():
    # 获取子序列（根据字节获取，非字符）
    # 参数：
    # name，Redis 的 name
    # start，起始位置（字节）
    # end，结束位置（字节）
    # 如： "武沛齐" ，0-2表示 "武"
    r.set("parter",u"柴少")
    print(r.getrange("parter",0,-1).decode())

# demo_getrange()

def demo_setrange():
    # 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
    # 参数：
    # offset，字符串的索引，字节（一个汉字三个字节）
    # value，要设置的值

    # r.set("name", 'oko123456')
    # 修改字符串内容，从指定字符串索引开始向后替换
    r.setrange("name",3,"koaaaaaaaaaaa")
    # r.get("name")

# demo_setrange()

def  demo_incr():
    # 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

    # 参数：
    # name,Redis的name
    # amount,自增数（必须是整数）

    # 注：同incrby
    r.set("n", 1)
    r.incr("n",'3')  # 4

    # 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

    # 参数：
    # name,Redis的name
    # amount,自增数（浮点型)

    r.incrbyfloat('n', 1) # 3.0
# demo_incr()


def demo_decr():
    # 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。

    # 参数：
    # name,Redis的name
    # amount,自减数（整数）

    r.set('n', '2')
    r.decr('n', 1) #1

# demo_decr()

def demo_append():
    # 在redis name对应的值后面追加内容
    # 参数：
        #key, redis的name
        #value, 要追加的字符串
    r.append('n', 'a') # 2
    r.get("n")

# demo_append()


####################哈希操作#################
def demo_hset():
    # name对应的hash名里设置一个键值对（不存在，则创建；否则，修改） 返回 1 和 0
    #  参数：
    # name，redis的name
    # key，name对应的hash中的key
    # value，name对应的hash中的value

    # 注：
    # hsetnx(name, key, value),当name对应的hash中不存在当前key时则创建（相当于添加）

    print(r.hset("h1", "age", "koka")) #1
    print(r.hget("h1", "age"))
# demo_hset()

def demo_hmset():
    # 在name对应的hash中批量设置键值对

    # 参数：
    # name，redis的name
    # mapping，字典，如：{'k1':'v1', 'k2': 'v2'}

    # 如：
    # r.hmset('xx', {'k1':'v1', 'k2': 'v2'})

    r.hmset('n1', {'k1': 'v1', 'k2': 'v2'})
    print(r.hmget("n1", "k1", "k2")) # ['v1', 'v2']

    # 获取name对应hash的所有键值
    print(r.hgetall("n1")) # {b'k2': b'v2', b'k1': b'v1'}


    # 获取name对应的hash中键值对的个数
    print(r.hlen("n1")) # 2

    # 获取name对应的hash中所有的key的值
    r.hkeys("n1") # [b'k2', b'k1']

    # 获取name对应的hash中所有的value的值
    r.hvals("n1")  # [b'v2', b'v1']

    # 检查name对应的hash是否存在当前传入的key
    print(r.hexists("n1", "k1"))

    # 将name对应的hash中指定key的键值对删除
    r.hdel("n1", "k1") # 1
# demo_hmset()


#############  list操作   #################
def demo_lpush():
    # 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
    # 如：
    # r.lpush('oo', 11,22,33)
    # 保存顺序为: 33,22,11
    # 扩展：
    # rpush(name, values) 表示从右向左操作
    r.lpush("l1", [11, 22, 33, 44]) # 1
    r.lpush("l1", [11, 22, 33, 44]) # 2
    # 索引  包括3  和python里的不一样
    # print(r.lrange("l1", '0', '3')) # [b'[11, 22, 33, 44]', b'[11, 22, 33, 44]']，[b'[11, 22, 33, 44]'
    r.lpush("l3", "AA", "BB", "CC", "DD") # 1
    r.lrange("l3", 0, 2) # [b'CC', b'BB', b'AA']


    # lpushx(name,value)
    # 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
    # rpushx(name, value) 表示从右向左操作
    r.lpushx("l2", "33")
    # 0
    print(r.lrange("l2", 0, 1))

    # llen(name)
    # name对应的list元素的个数
    r.llen("l1") # 2




# demo_lpush()

def demo_linsert():
    # 在name对应的列表的某一个值前或后插入一个新值
    # 参数：
    # name，redis的name
    # where: BEFORE或AFTER
    # refvalue，标杆值，即：在它前后插入数据
    # value，要插入的数据

    # r.lpush("l3", "AA", "BB", "CC", "DD")
    # print(r.lrange("l3", 0, 3))
    # ['DD', 'CC', 'BB', 'AA']

    # r.linsert("l3", "AFTER", "CC", "cc")
    # print(r.lrange("l3", 0, 3))
    # [b'CC', b'cc', b'BB', b'AA']
    pass
# demo_linsert()

def demo_lset():
    # 对name对应的list中的某一个索引位置重新赋值

    # 参数：
    # name，redis的name
    # index，list的索引位置
    # value，要设置的值

    r.lset("l3", '2', 'Cc')
    r.lrange("l3", '0', '5') # [b'DD', b'CC', b'Cc', b'BB', b'AA']
# demo_lset()

def demo_lpop():
    # 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
    # 更多：
    # rpop(name) 表示从右向左操作
    r.lpop("l3")
    b'DD'
    r.lrange("l3", '0', '2')#[b'CC', b'BB', b'AA']

# demo_lpop()

def demo_lindex():
    # 在name对应的列表中根据索引获取列表元素
    r.lrange("l3", 0, 3) #[b'CC', b'cc', b'BB', b'AA']
    r.lindex("l3", "0") #b'CC'
# demo_lindex()



'''
自定义增量迭代
# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
# 参数：
# src，要取数据的列表的name
# dst，要添加数据的列表的name

#测试元素
r.lpush("l3", '11', '22', '33')
def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

# 使用
for item in list_iter('l3'):
    print(item)
'''

'''
##############集合###############
参见: https://www.cnblogs.com/koka24/p/5841826.html
'''


'''
###################其他常用操作#####################
delete(*names)

# 根据删除redis中的任意数据类型
r.set("test","123")
r.get('test')
b'123'
r.delete("test")
1
r.get("test")
None

exists(name)

# 根据删除redis中的任意数据类型
r.set("test","123")
r.get('test')
b'123'
r.delete("test")
1
r.exists("test")
False

keys(pattern='*')

# 根据模型获取redis的name
 
# 更多：
    # KEYS * 匹配数据库中所有 key 。
    # KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
    # KEYS h*llo 匹配 hllo 和 heeeeello 等。
    # KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo 

r.keys(pattern="*")
[b'l5', b'parter', b'name', b'l3', b'l4', b'foo']

expire(name ,time)
# 为某个redis的某个name设置超时时间
r.set("t","ok")
r.expire("t",3)
r.get("t")  # 隔3秒后取值
None
rename(src, dst)
# 对redis的name重命名为
r.set('rn','123')
r.rename('rn','rename')
r.get('rename')
b'123'
move(name, db))
# 将redis的某个值移动到指定的db下
randomkey()
# 随机获取一个redis的name（不删除）
type(name)
# 获取name对应值的类型
r.get("name")
b'jn'
r.type("name")
b'string'
'''



'''
###############管道##################

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，
则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import redis
 
pool = redis.ConnectionPool(host='163.53.91.47', password='123456,port=6379)
 
r = redis.Redis(connection_pool=pool)
 
# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)
 
r.set('username', 'koka')
r.set('passwd', '123')
 
pipe.execute()
'''






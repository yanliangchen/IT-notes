import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
# cur = conn.cursor()
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    #创建cursor的时候，指定其返回的cursor类型为dict

#1 . 查询
sql = "select * from info"
reCount = cur.execute(sql)  # 返回受影响的行数
print(reCount)
data = cur.fetchall()  # 返回数据,返回的是tuple类型
print(data)

cur.close()
conn.close()

"""
[{'address': 'tokyo', 'name': 'mj', 'id': 1}, {'address': 'newyork', 'name': 'alex', 'id': 2}, {'address': 'beijing', 'name': 'tommy', 'id': 3}]
"""


# 2 . 插入数据
sql = "insert into info(NAME,address ) VALUES(%s,%s)"
params = ('eric', '/usr/bin/a.txt')
reCount = cur.execute(sql, params)
conn.commit()

new_id = cur.lastrowid  #获取自增id，提交完之后才能取到值
print(new_id)


# 3 . cursor定位
#使用fechone来逐条获取数据
data = cur.fetchone()
print(data)

data = cur.fetchone()
print(data)

data = cur.fetchone()
print(data)

"""
(1, 'mj', 'tokyo')
(2, 'alex', 'newyork')
(3, 'tommy', 'beijing')
"""

# 3.1.绝对定位
cur.scroll(0,mode='absolute')
data = cur.fetchone()
print(data)

cur.scroll(0,mode='absolute')

data = cur.fetchone()
print(data)

data = cur.fetchone()
print(data)
"""
(1, 'mj', 'tokyo')
(1, 'mj', 'tokyo')
(2, 'alex', 'newyork')
"""

# 3.2.相对定位
cur.scroll(-1,mode='relative')
data = cur.fetchone()
print(data)

data = cur.fetchone()
print(data)

cur.scroll(-1,mode='relative')

data = cur.fetchone()
print(data)
"""
(1, 'mj', 'tokyo')
(2, 'alex', 'newyork')
(2, 'alex', 'newyork')
"""


# encoding: utf-8
import  pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='renyisi886', db='mysql')
cur = conn.cursor()
#插入数据
sql_two = "insert into info(NAME,address ) VALUES(%s,%s)" # sql语句，%s是占位符（%s是唯一的，不论什么数据类型都使用%s）
# 用来防止sql注入
params = ('eric', 'wuhan') #参数
reCount = cur.execute(sql_two, params)
#批量插入
li = [('a1', 'b1'), ('a2', 'b2')]
sql_three = 'insert into info(NAME ,address) VALUES (%s,%s)'
reCount = cur.executemany(sql_three,li)
conn.commit()
cur.close()
conn.close()
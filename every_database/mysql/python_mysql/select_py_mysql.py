# encoding: utf-8
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='renyisi886', db='mysql')
#建立游标对象
cur = conn.cursor()
sql = "select * from db"
reCount = cur.execute(sql)# 返回受影响的行数
print(reCount)
data = cur.fetchall() # 返回数据，返回的是tuple类型
print(data)
cur.close()
conn.close()
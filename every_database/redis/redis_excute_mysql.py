import redis, json, time
from pymysql import connect

#redis数据库连接
redis_client = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
# mysql数据库连接
mysql_client = connect(host="127.0.0.1", user="root", password="mysql",
                 database="sina", port=3306, charset='utf8')
cursor = mysql_client.cursor()

i = 1
while True:
    print(i)
    time.sleep(1)
    source, data = redis_client.blpop(["sinainfospider_redis:items"])
    item = json.loads(data.decode())
    print("source===========", source)
    print("item===========", item)
    sql = "insert into sina_items(parent_url,parent_title,sub_title,sub_url,sub_file_name,son_url,head,content,crawled,spider) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    params = [item["parent_url"], item["parent_title"], item["sub_title"], item["sub_url"], item["sub_file_name"],
              item["son_url"], item["head"], item["content"], item["crawled"], item["spider"], ]
    cursor.execute(sql, params)
    mysql_client.commit()
    i += 1

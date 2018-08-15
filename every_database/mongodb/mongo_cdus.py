#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

settings = {
    "ip":'192.168.0.113',   #ip
    "port":27017,           #端口
    "db_name" : "mydb",    #数据库名字
    "set_name" : "test_set"   #集合名字
}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self,dic):
        print("inser...")
        self.my_set.insert(dic)

    def update(self,dic,newdic):
        print("update...")
        self.my_set.update(dic,newdic)

    def delete(self,dic):
        print("delete...")
        self.my_set.remove(dic)

    def dbfind(self,dic):
        print("find...")
        data = self.my_set.find(dic)
        for result in data:
            print(result["name"],result["age"])

def main():
    dic={"name":"zhangsan","age":18}
    mongo = MyMongoDB()
    mongo.insert(dic)
    mongo.dbfind({"name":"zhangsan"})

    mongo.update({"name":"zhangsan"},{"$set":{"age":"25"}})
    mongo.dbfind({"name":"zhangsan"})

    mongo.delete({"name":"zhangsan"})
    mongo.dbfind({"name":"zhangsan"})



if __name__ == "__main__":
    main()

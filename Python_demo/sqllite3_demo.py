# encoding: utf-8
__author__ = 'yanliangchen'
'''
sqllite 和 mysql 区别:
简单来说，SQLITE功能简约，小型化，追求最大磁盘效率；MYSQL功能全面，综合化，追求最大并发效率。如果只是单机上用的，数据量不是很大
，需要方便移植或者需要频繁读/写磁盘文件的话，就用SQLite比较合适；如果是要满足多用户同时访问，或者是网站访问量比较大是使用MYSQL比较合适。 

摘自: https://blog.csdn.net/zbw1185/article/details/47975965
'''


import sqlite3

class SqLite(object):
    def __init__(self, db_name):

        self.conn = sqlite3.connect(db_name)

    def close(self):
        """
        关闭Connection
        """
        self.conn.close()

    def create(self):
        """
        创建数据表
        """
        # 创建一个Cursor:
        cursor = self.conn.cursor()
        # 执行一条SQL语句，创建user表:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        # 继续执行一条SQL语句，插入一条记录:
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
        # 通过rowcount获得插入的行数:
        print cursor.rowcount
        # 关闭Cursor:
        cursor.close()
        # 提交事务:
        self.conn.commit()

    def show_tables(self):
        """
        显示数据库表名
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = cursor.fetchall()
        cursor.close()
        print result
        return result

    def get_row(self):
        """
        获取多行数据
        :return:
        """
        cursor = self.conn.cursor()
        # 执行查询语句:
        cursor.execute('select * from user where id=?', '1')
        # 获得查询结果集:
        values = cursor.fetchall()
        cursor.close()
        print values
        return values

def test():
    """
    测试
    """
    db = SqLite('test.db')
    db.create()
    db.show_tables()
    db.get_row()
    db.close()

if __name__ == '__main__':
    test()
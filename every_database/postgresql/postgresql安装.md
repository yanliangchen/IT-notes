## 1. centos7 安装最新版postgresql10

摘自 ：https://blog.csdn.net/rudy5348/article/details/79299162

### 1.1补充添加其他用户操作登陆：

**摘自： https://www.cnblogs.com/xxfcz/p/6483892.html**

```
二、创建新用户来访问PostgreSQL

1、如上所述，先切换到Linux用户postgres，并执行psql：

$ su - postgres

-bash-4.2$ psql

postgres=#

现在位于数据库提示符下。

2、创建数据库新用户，如 dbuser：

postgres=# CREATEUSER dbuser WITH PASSWORD '*****';
注意：

语句要以分号结尾。
密码要用单引号括起来。
3、创建用户数据库，如exampledb：

postgres=# CREATE DATABASE exampledb OWNER dbuser;
4、将exampledb数据库的所有权限都赋予dbuser：

postgres=# GRANT ALL PRIVILEGES ON DATABASE exampledb TO dbuser;
5、使用命令 \q 退出psql：

postgres=# \q
6、创建Linux普通用户，与刚才新建的数据库用户同名，如 dbuser：

$ sudo adduser dbuser

$ sudo passwd dbuser

7、以dbuser的身份连接数据库exampledb：

$ su - dbuser

Password: 
Last login: Wed Mar 1 11:52:07 CST 2017 on pts/

[dbuser@master ~]$ psql -d exampledb
```

## 2. postgresql命令

### 2.1.连接数据库

```
	# 默认的用户和数据库是postgres
	$ psql -U  postgres -d postgres 
```

### 2.2.创建数据库

```
 $ CREATE  DATABASE  data_li ;
```

### 2.3.切换数据库

```
$ \c data_li 
```

#### 2.3.1 查看数据库表

```
$ \d 
```



### 2.4 其他命令和mysql（差不多，现用现查）

pass

## 3. UI创建操作数据库（postgresql）

**连接不上去**

## 4. python服务器操作数据库

**pycharm连接不上去**

**首要解决问题**

```
用jdbc连接Postgresql数据库时经常出现这个错误，然而用pgAdmin III是可以正确连接的，表明用户名和密码都是正确的。
这主要是由于用户密码认证方式引起的，Postgresql数据库安装好后默认采用md5密码加密认证方式。
解决方法：
打开Postgresql安装目录下的data文件夹，找到pg_hba.conf文件并打开。
修改认证方式，将md5改为trust，然后保存。
# TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD

# IPv4 local connections:
host    all         all         127.0.0.1/32          trust
```

### 4.1 **连接到数据库**

```
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")

print "Opened database successfully"  
```

在这里，也可以提供数据库testdb的名称，如果数据库成功打开，那么它会给下面的消息：

```
Open database successfully
```

### 4.2 创建表

以下Python程序将使用以前创建的数据库中创建一个表：

```
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="data_li", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print ("Opened database successfully")


cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully"）

conn.commit()
conn.close()  
```

上述程序执行时，它会创建表COMPANY 在数据库test.db中，它会显示以下消息：

```
Opened database successfully
Table created successfully
```

### 4.2 insert操作 

```
import psycopg2

conn = psycopg2.connect(database="data_li", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");
conn.close()
```

### 4.3 select操作

```
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="data_li", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()  


#输出如下
Opened database successfully
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  20000.0

ID =  2
NAME =  Allen
ADDRESS =  Texas
SALARY =  15000.0

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond
SALARY =  65000.0

Operation done successfully
  
```



### 4.5 update操作

```
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit
print "Total number of rows updated :", cur.rowcount

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()  



#结果
Opened database successfully
Total number of rows updated : 1
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  25000.0

ID =  2
NAME =  Allen
ADDRESS =  Texas
SALARY =  15000.0

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond
SALARY =  65000.0

Operation done successfully
  
```



### 4.6 delete操作

```
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("DELETE from COMPANY where ID=2;")
conn.commit
print "Total number of rows deleted :", cur.rowcount

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()  




#结果
Opened database successfully
Total number of rows deleted : 1
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  20000.0

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond
SALARY =  65000.0

Operation done successfully www.yi

```


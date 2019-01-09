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


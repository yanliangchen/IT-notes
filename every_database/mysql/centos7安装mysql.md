### 1 下载并安装MySQL官方的Yum Repository

 

ps参考:https://www.cnblogs.com/bigbrotherer/p/7241845.html

```
[root@localhost ~]# wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
```

 

  使用上面的命令就直接下载了安装用的Yum Repository，大概25KB的样子，然后就可以直接yum安装了。

 

```
[root@localhost ~]# yum -y install mysql57-community-release-el7-10.noarch.rpm
```

 

  之后就开始安装MySQL服务器。

 

```
[root@localhost ~]# yum -y install mysql-community-server
```

 

  这步可能会花些时间，安装完成后就会覆盖掉之前的mariadb。

 

![img](https://images2017.cnblogs.com/blog/1079354/201707/1079354-20170726201927328-459165254.png)

 

至此MySQL就安装完成了，然后是对MySQL的一些设置。

 

### 2 MySQL数据库设置

 

  首先启动MySQL

 

```
[root@localhost ~]# systemctl start  mysqld.service
```

 

  查看MySQL运行状态，运行状态如图：

 

```
[root@localhost ~]# systemctl status mysqld.service
```

 

![img](https://images2017.cnblogs.com/blog/1079354/201707/1079354-20170726202441687-1168874203.png)

 

  此时MySQL已经开始正常运行，不过要想进入MySQL还得先找出此时root用户的密码，通过如下命令可以在日志文件中找出密码：

 

```
[root@localhost ~]# grep "password" /var/log/mysqld.log
```

 

![img](https://images2017.cnblogs.com/blog/1079354/201707/1079354-20170726202722796-1932560887.png)

 

  如下命令进入数据库：

 

```
[root@localhost ~]# mysql -uroot -p
```

 

  输入初始密码，此时不能做任何事情，因为MySQL默认必须修改密码之后才能操作数据库：

 

```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
```

 

  这里有个问题，新密码设置的时候如果设置的过于简单会报错：

 

![img](https://images2017.cnblogs.com/blog/1079354/201707/1079354-20170726203136000-1398594667.png)

 

  原因是因为MySQL有密码设置的规范，具体是与validate_password_policy的值有关：

 

 ![img](https://images2017.cnblogs.com/blog/1079354/201707/1079354-20170726203904812-1008115240.png)

 

  MySQL完整的初始密码规则可以通过如下命令查看：

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password_check_user_name    | OFF   |
| validate_password_dictionary_file    |       |
| validate_password_length             | 4     |
| validate_password_mixed_case_count   | 1     |
| validate_password_number_count       | 1     |
| validate_password_policy             | LOW   |
| validate_password_special_char_count | 1     |
+--------------------------------------+-------+
7 rows in set (0.01 sec)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

  密码的长度是由validate_password_length决定的，而validate_password_length的计算公式是：

 

```
validate_password_length = validate_password_number_count + validate_password_special_char_count + (2 * validate_password_mixed_case_count)
```

 

 

 

我的是已经修改过的，初始情况下第一个的值是ON，validate_password_length是8。可以通过如下命令修改：

 

```
mysql> set global validate_password_policy=0;
mysql> set global validate_password_length=1;
```

 

  设置之后就是我上面查出来的那几个值了，此时密码就可以设置的很简单，例如1234之类的。到此数据库的密码设置就完成了。

 

  但此时还有一个问题，就是因为安装了Yum Repository，以后每次yum操作都会自动更新，需要把这个卸载掉：

 

```
[root@localhost ~]# yum -y remove mysql57-community-release-el7-10.noarch
```

 

  此时才算真的完成了。





### 3. 客户端连接mysql 

//如果是像navicat这种连接mysql ,那么则需要保证云主机上的mysql跑在ipv4上 

```
//vi my.cnf
bind-address = 0.0.0.0
```



//云主机端口放行 



//这里顺便复习一下端口的相关操作 

```
一、查看端口开启状态
[zhujiang@localhost n2]$ sudo firewall-cmd --query-port=9998/udp
[sudo] password for zhujiang: 
no

二、开启端口

[zhujiang@localhost n2]$ sudo firewall-cmd --add-port=9998/udp --permanent
success

--permanent表示永久生效，重启不会丢失配置。

三、关闭端口
[zhujiang@localhost n2]$ sudo firewall-cmd --remove-port=9998/udp --permanent
Warning: NOT_ENABLED: 9998:udp
success

重新加载配置
[zhujiang@localhost n2]$ sudo firewall-cmd --reload
success
```



//防火墙关闭

```
systemctl stop firewalld.service
systemctl disable firewalld.service 
firewall-cmd --state #查看默认防火墙状态
```





//重启mysql 

```
service  mysqld stop 
service mysqld start 
service mysqld restart
```



//之后本地就可以连接了 ，还需要通过指定ip来进行授予客户端访问权限一个设置 进入mysql来敲命令

```
grant all privileges on *.* to 'root'@'192.168.1.1' identified by '密码';
//删除权限
DELETE FROM user WHERE User='root' and Host='%';
```


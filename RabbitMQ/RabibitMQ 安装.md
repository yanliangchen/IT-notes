**RabbitMQ个人博客文章 (https://blog.csdn.net/super_rd/article/category/6869439)**



# 三.  安装RabbitMQ

文章链接(来自博客https://blog.csdn.net/super_rd): 

​                 //先安装RabbitMQ  之后生产环境配置 可能少一些选项  之后把需要的安装上结合文章2.再重新配置一下

​		 **1.RabbitMQ消息队列-Centos7下安装RabbitMQ3.6.1** 

​		**https://blog.csdn.net/super_rd/article/details/70241007?utm_source=itdadao&utm_medium=referral**

​		**2.第一个链接 报错出现问题 接着 CentOS安装ErlangOTP**

​         	https://blog.csdn.net/tojohnonly/article/details/76790713



## 用什么系统

本文使用的是Centos7，为了保证对linux不太熟悉的伙伴也能轻松上手（避免折在安装的路上），下面是我的系统镜像地址：<https://pan.baidu.com/s/1gfl6Y9l> 
养成良好的习惯，安装好系统运行更新：

```
yum update -y

reboot  //一般情况不用重启，个人习惯。123
```

有人问如果我是初学者使用ubuntu可以吗？我的答案是如果你是为了在以后的生产应用中使用，请使用Centos，如果只是学着玩玩那就无所谓。在我在的公司（某世界500强，就不点名了）大部分的生产系统都使用了Centos。

## 安装依赖文件：

```
yum -y install gcc glibc-devel make ncurses-devel openssl-devel xmlto perl wget1

yum install -y wget
```

## 安装erlang 语言环境：

- 下载安装：

```
wget http://www.erlang.org/download/otp_src_18.3.tar.gz  //下载erlang包
tar -xzvf otp_src_18.3.tar.gz  //解压
cd otp_src_18.3/ //切换到安装路径
./configure --prefix=/usr/local/erlang  //生产安装配置
make && make install  //编译安装12345
```

- 配置erlang环境变量：

```
vi /etc/profile  //在底部添加以下内容
    #set erlang environment
    ERL_HOME=/usr/local/erlang
    PATH=$ERL_HOME/bin:$PATH
    export ERL_HOME PATH

source /etc/profile  //生效1234567
```

测试一下是否安装成功,在控制台输入命令erl

```
erl  //如果进入erlang的shell则证明安装成功，退出即可。1
```

## 下载安装RabbitMQ：

- 下载安装

```
cd /usr/local  //切换到计划安装RabbitMQ的目录，我这里放在/usr/local
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-generic-unix-3.6.1.tar.xz  //下载RabbitMQ安装包
xz -d rabbitmq-server-generic-unix-3.6.1.tar.xz
tar -xvf rabbitmq-server-generic-unix-3.6.1.tar
```

解压后多了个文件夹rabbitmq-server-3.6.1 ，重命名为rabbitmq以便记忆。

```
mv rabbitmq_server-3.6.1/ rabbitmq1
```

- 配置rabbitmq环境变量：

```
vi /etc/profile
    #set rabbitmq environment
    export PATH=$PATH:/usr/local/rabbitmq/sbin
source /etc/profile
```

- 启动服务：

```
rabbitmq-server -detached //启动rabbitmq，-detached代表后台守护进程方式启动。
12
```

查看状态，如果显示如下截图说明安装成功：

```
rabbitmqctl status1
```

![RabbitMQ状态](https://img-blog.csdn.net/20170419145307562?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvU3VwZXJfUkQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

其他相关命令

```
启动服务：rabbitmq-server -detached【 /usr/local/rabbitmq/sbin/rabbitmq-server  -detached 】
查看状态：rabbitmqctl status【 /usr/local/rabbitmq/sbin/rabbitmqctl status  】
关闭服务：rabbitmqctl stop【 /usr/local/rabbitmq/sbin/rabbitmqctl stop  】
列出角色：rabbitmqctl list_users
```



## 配置网页插件：

首先创建目录，否则可能报错：

```
mkdir /etc/rabbitmq
```

然后启用插件：

```
rabbitmq-plugins enable rabbitmq_management
```

## 配置防火墙：

//安装防火墙

 yum install firewalld systemd -y

配置linux 端口 15672 网页管理 5672 AMQP端口：

```
firewall-cmd --permanent --add-port=15672/tcp
firewall-cmd --permanent --add-port=5672/tcp
systemctl restart firewalld.service
```

现在你在浏览器中输入服务器IP:15672 就可以看到RabbitMQ的WEB管理页面了，是不是很兴奋，可是你没有账号密码，别急。 
![RabbitMQ WEB网页管理](https://img-blog.csdn.net/20170419145800478?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvU3VwZXJfUkQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



## 配置访问账号密码和权限：

默认网页是不允许访问的，需要增加一个用户修改一下权限，代码如下：

```
rabbitmqctl add_user superrd superrd  //添加用户，后面两个参数分别是用户名和密码，我这都用superrd了。
rabbitmqctl set_permissions -p / superrd ".*" ".*" ".*"  //添加权限
rabbitmqctl set_user_tags superrd administrator  //修改用户角色
```












**摘自 : https://blog.csdn.net/zhaogangyyxf/article/details/79614464**

# centos7环境下RabbitMQ安装与配置

2018年03月19日 17:56:40 [过客幽影星风](https://me.csdn.net/zhaogangyyxf) 阅读数：3373

RabbitMQ是流行的开源消息队列系统，是AMQP（Advanced Message Queuing Protocol高级消息队列协议）的标准实现，用erlang语言开发。RabbitMQ据说具有良好的性能和时效性，同时还能够非常好的支持集群和负载部署，非常适合在较大规模的分布式系统中使用，具体使用场景请参考https://www.cnblogs.com/stopfalling/p/5375492.html。由于项目需要，我就安装并配置了RabbitMQ，[服务器](https://www.baidu.com/s?wd=%E6%9C%8D%E5%8A%A1%E5%99%A8&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)操作系统是[CentOS](https://www.linuxidc.com/topicnews.aspx?tid=14)7。下面就自测的安装步骤介绍下：

1.首安装rabbitMQ所需依赖，安装erlang，

yum install gcc glibc-devel make ncurses-devel openssl-devel xmlto   一路y下去就行

![img](https://img-blog.csdn.net/20180319171804658?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

在官网上下载 epel-release   网址http://rpm.pbone.net/index.php3/stat/4/idpl/29069710/dir/centos_7/com/epel-release-7-5.noarch.rpm.html

然后用ftp上传至系统中，这部就不在操作，网上多的是，我这里下载的是epel-release-7-5.noarch.rpm

执行安装命令：

rpm -Uvh epel-release-7-5.noarch.rpm

安装 erlang:yum install -y erlang

安装完成后，进入正式的rabbitMQ安装阶段

下载：

wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.6/rabbitmq-server-3.6.6-1.el7.noarch.rpm

![img](https://img-blog.csdn.net/20180319172746937?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

下载完成后安装：yum install -y rabbitmq-server-3.6.6-1.el7.noarch.rpm

![img](https://img-blog.csdn.net/20180319173103163?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

完成后启动服务：

```
service rabbitmq-server start(如果启动失败，可将服务器重新启动后再执行该命令)
```

![img](https://img-blog.csdn.net/20180319173125956?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

可以查看服务状态：

```
service rabbitmq-server status
```

![img](https://img-blog.csdn.net/2018031917323988?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

看到log文件的位置，转到文件位置，打开文件：

![img](https://img-blog.csdn.net/20180319173344666?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

not found 没有找到，我们可以从其他文件夹复制

cp /usr/share/doc/rabbitmq-server-3.6.6/rabbitmq.config.example /etc/rabbitmq/rabbitmq.config

进入rabbit文件夹下：cd /etc/rabbitmq

修改rabbitmq.config文件，使外部可以访问;vim rabbitmq.config

![img](https://img-blog.csdn.net/20180319174248554?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

进入文件，找到第64行，

![img](https://img-blog.csdn.net/20180319174351108?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

将%% 和后面的，删除

![img](https://img-blog.csdn.net/20180319174438724?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 接下来安装插件，执行命令：/sbin/rabbitmq-plugins enable rabbitmq_management 

![img](https://img-blog.csdn.net/20180319174816178?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

此时重启服务就行了，重启rabbitmq服务

service rabbitmq-server restart  （系统重启后再重启该服务，（原因未找到））

关闭防火墙：systemctl stop firewalld.service 端口是15672，账号和密码默认都是guest

![img](https://img-blog.csdn.net/20180319175132445?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

登录，就可以使用了 。

![img](https://img-blog.csdn.net/20180319175214240?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3poYW9nYW5neXl4Zg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 
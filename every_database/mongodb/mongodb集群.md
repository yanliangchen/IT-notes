# mongodb集群搭建



mongodb集群有三种方式

​    1，主从模式，类似mysql master slave方式。

​    2，副本集模式，其实是一主多从，如果主节点挂掉，会重新在从节点选取一台为主节点。

​    3，分片模式，针对大数据量，高负载情况。

[![wKioL1UsvwCgUF0jAAG8apv8TOY057.jpg](http://s3.51cto.com/wyfs02/M02/6B/65/wKioL1UsvwCgUF0jAAG8apv8TOY057.jpg)](http://s3.51cto.com/wyfs02/M02/6B/65/wKioL1UsvwCgUF0jAAG8apv8TOY057.jpg)

从图中可以看到有四个组件：mongos、config server、shard、replica set。

**mongos**，数据库集群请求的入口，所有的请求都通过mongos进行协调，不需要在应用程序添加一个路由选择器，mongos自己就是一个请求分发中心，它负责把对应的数据请求请求转发到对应的shard服务器上。在生产环境通常有多mongos作为请求的入口，防止其中一个挂掉所有的mongodb请求都没有办法操作。

**config server**，顾名思义为配置服务器，存储所有数据库元信息（路由、分片）的配置。mongos本身没有物理存储分片服务器和数据路由信息，只是缓存在内存里，配置服务器则实际存储这些数据。mongos第一次启动或者关掉重启就会从 config server 加载配置信息，以后如果配置服务器信息变化会通知到所有的 mongos 更新自己的状态，这样 mongos 就能继续准确路由。在生产环境通常有多个 config server 配置服务器，因为它存储了分片路由的元数据，这个可不能丢失！就算挂掉其中一台，只要还有存货， mongodb集群就不会挂掉。

**shard**，这就是传说中的分片了。上面提到一个机器就算能力再大也有天花板，就像军队打仗一样，一个人再厉害喝血瓶也拼不过对方的一个师。俗话说三个臭皮匠顶个诸葛亮，这个时候团队的力量就凸显出来了。在互联网也是这样，一台普通的机器做不了的多台机器来做，如下图：

[![wKiom1UsviPDW-8HAAGzUzKmy3A693.jpg](http://s3.51cto.com/wyfs02/M00/6B/69/wKiom1UsviPDW-8HAAGzUzKmy3A693.jpg)](http://s3.51cto.com/wyfs02/M00/6B/69/wKiom1UsviPDW-8HAAGzUzKmy3A693.jpg)

一台机器的一个数据表 Collection1 存储了 1T 数据，压力太大了！在分给4个机器后，每个机器都是256G，则分摊了集中在一台机器的压力。也许有人问一台机器硬盘加大一点不就可以了，为什么要分给四台机器呢？不要光想到存储空间，实际运行的数据库还有硬盘的读写、网络的IO、CPU和内存的瓶颈。在mongodb集群只要设置好了分片规则，通过mongos操作数据库就能自动把对应的数据操作请求转发到对应的分片机器上。在生产环境中分片的片键可要好好设置，这个影响到了怎么把数据均匀分到多个分片机器上，不要出现其中一台机器分了1T，其他机器没有分到的情况，这样还不如不分片！

**replica set**，上两节已经详细讲过了这个东东，怎么这里又来凑热闹！其实上图4个分片如果没有 replica set 是个不完整架构，假设其中的一个分片挂掉那四分之一的数据就丢失了，所以在高可用性的分片架构还需要对于每一个分片构建 replica set 副本集保证分片的可靠性。生产环境通常是 2个副本 + 1个仲裁。

说了这么多，还是来实战一下如何搭建高可用的mongodb集群：

首先确定各个组件的数量，mongos 3个， config server 3个，数据分3片 shard server 3个，每个shard 有一个副本一个仲裁也就是 3 * 2 = 6 个，总共需要部署15个实例。这些实例可以部署在独立机器也可以部署在一台机器，我们这里测试资源有限，只准备了 3台机器，在同一台机器只要端口不同就可以，看一下物理部署图：

[![wKioL1UswCjgmYTwAAUnOHDR7OI538.jpg](http://s3.51cto.com/wyfs02/M02/6B/65/wKioL1UswCjgmYTwAAUnOHDR7OI538.jpg)](http://s3.51cto.com/wyfs02/M02/6B/65/wKioL1UswCjgmYTwAAUnOHDR7OI538.jpg)

下面是安装配置

1，准备三台机器

ip:10.19.21.241

   10.19.21.242

   10.19.21.243

2,分别在每台机器上建立mongodb数据目录

 我使用ansible工具来创建目录

创建存放mongodb数据文件

```
ansible mongodb -m shell -a "mkdir /data/mongodb -p"
```

3,安装mongodb，这里使用yum来安装

配置yum repo

```
vim /etc/yum.repos.d/mongodb-org.repo
[mongodb-org-2.6]
name=MongoDB 2.6 Repository
baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
gpgcheck=0
enabled=1
```

拷贝过去

```
ansible mongodb -m copy -a "src=mongodb/mongodb-org.repo dest=/etc/yum.repos.d/"

错误如下：
10.19.21.243 | FAILED >> {
"checksum": "d79d6075271e933b3811455e74eaa9ef47f593e6",
"failed": true,
"msg": "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"
}
解决方法：
ansible mongodb -m yum -a "name=libselinux-python state=latest"
```

安装mongodb

```
ansible mongodb -m yum -a "name=mongodb-org state=latest"
```

4,每台上创建mongos config shard1 shard2 shard3五个目录，因为mongos不存储数据，只需建立日志文件目录

建立mongos目录和日志目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/mongos/log"
```

建立config server数据目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/config/data"
```

建立config server日志目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/config/log"
```

建立shard1数据目录和日志目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/shard1/data /data/mongodb/shard1/log"
```

建立shard2数据目录和日志目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/shard2/data /data/mongodb/shard2/log"
```

建立shard3数据目录和日志目录

```
ansible mongodb -m shell -a "mkdir -p /data/mongodb/shard3/data /data/mongodb/shard3/log"
```

5,规划5个组件对应的端口号，由于一个机器需要同时部署mongos, config server, shard1, shard2, shard3,所以需要用端口号进行区分

这个端口号可以自己定义，mongos:20000,config server:21000, shard1:22001, shard2:22002, shard3:22003

6,配置每台服务器的配置文件

由于我们的mongodb是yum安装，会有一个默认的配置文件，需要先备份

```
ansible mongodb -m shell -a "mv /etc/mongod.conf /etc/mongod.conf.bak"
```

配置每台服配置服务器

```
cat mongod-configsvr.conf
dbpath=/data/mongodb/config/data
port=21000
logpath=/data/mongodb/config/log/config.log
fork=true
configsvr=true
logappend=true
```

配置每台mongos服务器

```
cat mongod-mongos.conf
configdb=10.19.21.241:21000,10.19.21.242:21000,10.19.21.243:21000
port=20000
logpath=/data/mongodb/mongos/log/mongos.log
logappend=true
fork=true
```

配置各个分片的副本集

```
cat mongod-shardsvr1.conf
shardsvr=true
replSet=shard1
port=22001
dbpath=/data/mongodb/shard1/data
logpath=/data/mongodb/shard1/log/shard1.log
fork=true
logappend=true

cat mongod-shardsvr2.conf
shardsvr=true
replSet=shard2
port=22002
dbpath=/data/mongodb/shard2/data
logpath=/data/mongodb/shard2/log/shard2.log
fork=true
logappend=true

cat mongod-shardsvr3.conf
shardsvr=true
replSet=shard3
port=22003
dbpath=/data/mongodb/shard3/data
logpath=/data/mongodb/shard3/log/shard3.log
fork=true
logappend=true
```

创建配置文件目录

```
ansible mongodb -m shell -a "mkdir /etc/mongodb"
```

拷贝配置文件到目录

```
ansible mongodb -m copy -a "src=mongodb/mongod-configsvr.conf dest=/etc/mongodb/"
ansible mongodb -m copy -a "src=mongodb/mongod-mongos.conf dest=/etc/mongodb/"
ansible mongodb -m copy -a "src=mongodb/mongod-shardsvr1.conf dest=/etc/mongodb/"
ansible mongodb -m copy -a "src=mongodb/mongod-shardsvr2.conf dest=/etc/mongodb/"
ansible mongodb -m copy -a "src=mongodb/mongod-shardsvr3.conf dest=/etc/mongodb/"
```

启动服务

```
ansible mongodb -m shell -a "mongod -f /etc/mongodb/mongod-configsvr.conf"
ansible mongodb -m shell -a "mongos -f /etc/mongodb/mongod-mongos.conf"

启动这个报错了
2015-04-10T20:42:37.340+0800 [mongosMain] MongoS version 2.6.9 starting: pid=19701 port=20000 64-bit host=VM-241 (--help for usage)
2015-04-10T20:42:37.340+0800 [mongosMain] db version v2.6.9
2015-04-10T20:42:37.340+0800 [mongosMain] git version: df313bc75aa94d192330cb92756fc486ea604e64
2015-04-10T20:42:37.340+0800 [mongosMain] build info: Linux build20.nj1.10gen.cc 2.6.32-431.3.1.el6.x86_64 #1 SMP Fri Jan 3 21:39:27 UTC 2014 x86_64 BOOST_LIB_VERSION=1_49
2015-04-10T20:42:37.340+0800 [mongosMain] allocator: tcmalloc
2015-04-10T20:42:37.341+0800 [mongosMain] options: { config: "/etc/mongodb/mongod-mongos.conf", net: { port: 20000 }, processManagement: { fork: true }, sharding: { configDB: "10.19.21.241:21000,10.19.21.242:21000,10.19.21.243:21000" }, systemLog: { destination: "file", path: "/data/mongodb/mongos/log/mongos.log" } }
2015-04-10T20:42:37.345+0800 [mongosMain] SyncClusterConnection connecting to [10.19.21.241:21000]
2015-04-10T20:42:37.346+0800 [mongosMain] SyncClusterConnection connecting to [10.19.21.242:21000]
2015-04-10T20:42:37.349+0800 [mongosMain] SyncClusterConnection connecting to [10.19.21.243:21000]
2015-04-10T20:42:37.414+0800 [mongosMain] scoped connection to 10.19.21.241:21000,10.19.21.242:21000,10.19.21.243:21000 not being returned to the pool
2015-04-10T20:42:48.522+0800 [mongosMain] waited 11s for distributed lock configUpgrade for upgrading config database to new format v5
2015-04-10T20:42:59.622+0800 [mongosMain] waited 22s for distributed lock configUpgrade for upgrading config database to new format v5
2015-04-10T20:43:10.720+0800 [mongosMain] waited 33s for distributed lock configUpgrade for upgrading config database to new format v5
```

然后网上找了下原因，由于每台服务器时间不同步导致

这个坑爹问题都出现，看来是不够仔细

```
ansible mongodb -m shell -a "date"
10.19.21.243 | success | rc=0 >>
Thu Apr  9 22:11:05 CST 2015
10.19.21.241 | success | rc=0 >>
Fri Apr 10 20:45:27 CST 2015
10.19.21.242 | success | rc=0 >>
Thu Apr  9 22:09:13 CST 2015
一看果然有问题
```

执行命令同步时间服务器

```
ansible mongodb -m shell -a "/usr/sbin/ntpdate cn.pool.ntp.org"
10.19.21.242 | FAILED | rc=127 >>
/bin/sh: /usr/sbin/ntpdate: No such file or directory
10.19.21.243 | FAILED | rc=127 >>
/bin/sh: /usr/sbin/ntpdate: No such file or directory
10.19.21.241 | success | rc=0 >>
13 Apr 17:11:59 ntpdate[19842]: adjust time server 202.112.29.82 offset 0.000138 sec
```

尼玛只有一台能正常同步，估计没有安装ntpdate命令

```
ansible mongodb -m shell -a "yum install ntpdate -y"
ansible mongodb -m shell -a "/usr/sbin/ntpdate cn.pool.ntp.org"
10.19.21.243 | success | rc=0 >>
13 Apr 17:14:03 ntpdate[2661]: step time server 202.112.31.197 offset 327602.420329 sec
10.19.21.241 | success | rc=0 >>
13 Apr 17:14:03 ntpdate[19888]: adjust time server 202.112.29.82 offset 0.004004 sec
10.19.21.242 | success | rc=0 >>
13 Apr 17:14:03 ntpdate[2681]: step time server 202.112.31.197 offset 327714.079649 sec
ansible mongodb -m shell -a "date"
10.19.21.242 | success | rc=0 >>
Mon Apr 13 17:14:08 CST 2015
10.19.21.243 | success | rc=0 >>
Mon Apr 13 17:14:08 CST 2015
10.19.21.241 | success | rc=0 >>
Mon Apr 13 17:14:08 CST 2015
```

```
顺便把硬件时间也同步下
```

```
ansible mongodb -m shell -a "hwclock --systohc"
10.19.21.241 | success | rc=0 >>
10.19.21.243 | success | rc=0 >>
10.19.21.242 | success | rc=0 >>
```

```
继续启动mongos
```

```
ansible mongodb -m shell -a "mongos -f /etc/mongodb/mongod-mongos.conf"
10.19.21.243 | success | rc=0 >>
about to fork child process, waiting until server is ready for connections.
forked process: 2708
child process started successfully, parent exiting
10.19.21.241 | success | rc=0 >>
about to fork child process, waiting until server is ready for connections.
forked process: 19968
child process started successfully, parent exiting
10.19.21.242 | success | rc=0 >>
about to fork child process, waiting until server is ready for connections.
forked process: 2728
child process started successfully, parent exiting
```

启动各个分片的副本集

```
ansible mongodb -m shell -a "mongod -f /etc/mongodb/mongod-shardsvr1.conf"
ansible mongodb -m shell -a "mongod -f /etc/mongodb/mongod-shardsvr2.conf"
ansible mongodb -m shell -a "mongod -f /etc/mongodb/mongod-shardsvr3.conf"
```

顺便关闭开机自动启动mongod

```
ansible mongodb -m shell -a "chkconfig mongod off"
10.19.21.243 | success | rc=0 >>
10.19.21.242 | success | rc=0 >>
10.19.21.241 | success | rc=0 >>
```

6,登陆任意一台，连接mongodb

设置第一个分片副本集

```
[root@VM-241 ~]# mongo 127.0.0.1:22001
MongoDB shell version: 2.6.9
connecting to: 127.0.0.1:22001/test
```

使用admin数据库

```
mongos> use admin
switched to db admin
```

定义副本集配置

```
mongos> config={_id:"shard1",members:[{_id:0,host:"10.19.21.241:22001"},{_id:1,host:"10.19.21.242:22001"},{_id:2,host:"10.19.21.243:22001",arbiterOnly:true}]}
{
"_id" : "shard1",
"members" : [
{
"_id" : 0,
"host" : "10.19.21.241:22001"
},
{
"_id" : 1,
"host" : "10.19.21.242:22001"
},
{
"_id" : 2,
"host" : "10.19.21.243:22001",
"arbiterOnly" : true
}
]
}
```

初始化副本集配置

```
> rs.initiate(config);
{
"info" : "Config now saved locally.  Should come online in about a minute.",
"ok" : 1
}
```

设置第二个分片副本集

```
[root@VM-241 ~]# mongo 127.0.0.1:22002
MongoDB shell version: 2.6.9
connecting to: 127.0.0.1:22002/test
> use admin
switched to db admin
> config={_id:"shard2",members:[{_id:0,host:"10.19.21.241:22002"},{_id:1,host:"10.19.21.242:22002"},{_id:2,host:"10.19.21.243:22002",arbiterOnly:true}]}
{
"_id" : "shard2",
"members" : [
{
"_id" : 0,
"host" : "10.19.21.241:22002"
},
{
"_id" : 1,
"host" : "10.19.21.242:22002"
},
{
"_id" : 2,
"host" : "10.19.21.243:22002",
"arbiterOnly" : true
}
]
}
> rs.initiate(config);
{
"info" : "Config now saved locally.  Should come online in about a minute.",
"ok" : 1
}
```

设置第三个分片副本集

```
[root@VM-241 ~]# mongo 127.0.0.1:22003
MongoDB shell version: 2.6.9
connecting to: 127.0.0.1:22003/test
> use admin
switched to db admin
> config={_id:"shard3",members:[{_id:0,host:"10.19.21.241:22003"},{_id:1,host:"10.19.21.242:22003"},{_id:2,host:"10.19.21.243:22003",arbiterOnly:true}]}
{
"_id" : "shard3",
"members" : [
{
"_id" : 0,
"host" : "10.19.21.241:22003"
},
{
"_id" : 1,
"host" : "10.19.21.242:22003"
},
{
"_id" : 2,
"host" : "10.19.21.243:22003",
"arbiterOnly" : true
}
]
}
> rs.initiate(config);
{
"info" : "Config now saved locally.  Should come online in about a minute.",
"ok" : 1
}
```

7,配置分片

目前搭建的mongodb配置服务器，路由服务器，各个分片服务器，不过应用程序连接到mongs路由服务器并不能使用分片机制，还需要在程序里设置分片配置，让分片生效。

连接mongos

```
[root@VM-241 ~]# mongo 127.0.0.1:20000
MongoDB shell version: 2.6.9
connecting to: 127.0.0.1:20000/test
```

使用admin数据库

```
mongos> use admin
switched to db admin
```

串联路由服务器与分配副本集1

```
mongos> db.runCommand({addshard:"shard1/10.19.21.241:22001,10.19.21.242:22001,10.19.21.243:22001"});
{ "shardAdded" : "shard1", "ok" : 1 }
```

串联路由服务器与分配副本集2

```
mongos> db.runCommand({addshard:"shard2/10.19.21.241:22002,10.19.21.242:22002,10.19.21.243:22002"});
{ "shardAdded" : "shard2", "ok" : 1 }
```

串联路由服务器与分配副本集3

```
mongos> db.runCommand({addshard:"shard3/10.19.21.241:22003,10.19.21.242:22003,10.19.21.243:22003"});
{ "shardAdded" : "shard3", "ok" : 1 }
```

查看分片服务器配置

```
mongos> db.runCommand({listshards:1})
{
"shards" : [
{
"_id" : "shard1",
"host" : "shard1/10.19.21.241:22001,10.19.21.242:22001"
},
{
"_id" : "shard2",
"host" : "shard2/10.19.21.241:22002,10.19.21.242:22002"
},
{
"_id" : "shard3",
"host" : "shard3/10.19.21.241:22003,10.19.21.242:22003"
}
],
"ok" : 1
}
```

由于10.19.21.243是每个分片副本集的仲裁节点，所以上面没有列出

8,目前配置服务、路由服务、分片服务、副本集服务都已经串联起来了，但我们的目的是希望插入数据，数据能够自动分片，连接在mongos上，准备让指定的数据库、指定的集合分片生效

指定数据库testdb使分片生效

```
mongos> db.runCommand({enablesharding:"testdb"});
{ "ok" : 1 }
```

指定数据库里需要分片的集合和片键

```
mongos> db.runCommand({shardcollection:"testdb.table1",key:{id:1}})
{ "collectionsharded" : "testdb.table1", "ok" : 1 }
```

我们设置testdb的 table1 表需要分片，根据 id 自动分片到 shard1 ，shard2，shard3 上面去。要这样设置是因为不是所有mongodb 的数据库和表 都需要分片！

```
mongos> use testdb
switched to db testdb
```

插入测试数据

```
 for (var i=1;i<=100000;i++)db.table1.save({id:i,"test1":"testvar1"});
WriteResult({ "nInserted" : 1 })
```

查看分片情况如下：

```
mongos> db.table1.stats();
{
"sharded" : true,
"systemFlags" : 1,
"userFlags" : 1,
"ns" : "testdb.table1",
"count" : 100000,
"numExtents" : 12,
"size" : 11200000,
"storageSize" : 23212032,
"totalIndexSize" : 6091120,
"indexSizes" : {
"_id_" : 3278576,
"id_1" : 2812544
},
"avgObjSize" : 112,
"nindexes" : 2,
"nchunks" : 3,
"shards" : {
"shard1" : {
"ns" : "testdb.table1",
"count" : 5097,
"size" : 570864,
"avgObjSize" : 112,
"storageSize" : 696320,
"numExtents" : 4,
"nindexes" : 2,
"lastExtentSize" : 524288,
"paddingFactor" : 1,
"systemFlags" : 1,
"userFlags" : 1,
"totalIndexSize" : 335216,
"indexSizes" : {
"_id_" : 179872,
"id_1" : 155344
},
"ok" : 1
},
"shard2" : {
"ns" : "testdb.table1",
"count" : 0,
"size" : 0,
"storageSize" : 8192,
"numExtents" : 1,
"nindexes" : 2,
"lastExtentSize" : 8192,
"paddingFactor" : 1,
"systemFlags" : 0,
"userFlags" : 1,
"totalIndexSize" : 16352,
"indexSizes" : {
"_id_" : 8176,
"id_1" : 8176
},
"ok" : 1
},
"shard3" : {
"ns" : "testdb.table1",
"count" : 94903,
"size" : 10629136,
"avgObjSize" : 112,
"storageSize" : 22507520,
"numExtents" : 7,
"nindexes" : 2,
"lastExtentSize" : 11325440,
"paddingFactor" : 1,
"systemFlags" : 0,
"userFlags" : 1,
"totalIndexSize" : 5739552,
"indexSizes" : {
"_id_" : 3090528,
"id_1" : 2649024
},
"ok" : 1
}
},
"ok" : 1
}
```

可以看到数据分到3个分片，shard1:5097 shard2:0 shard3:94903

从结果看出，效果不是很理想，因为shard2里没有分配到。还要调试。





ps:这篇文章不错，算是自己的一个入门小集群，用ansible批量部署的时候由于云主机机器配置不是很高，

出现了一些小问题

转自：http://blog.51cto.com/charlie928/1632314
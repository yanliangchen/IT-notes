[redis持久化存储](https://www.cnblogs.com/meitian/p/5209877.html)

redis持久化存储支持两种方式：RDB和AOF。RDB一定时间取存储文件，AOF默认每秒去存储历史命令，官方建议两种方式同时使用

没有持久化的redis和memcache一样，相当于一个纯内存的数据库

 

**一、RDB（Redis DataBase）**

RDB是将数据写入一个临时文件，持久化结束后，用这个临时文件替换上次持久化的文件，达到数据恢复。

优点：使用单独子进程来进行持久化，主进程不会进行任何IO操作，保证了redis的高性能

缺点：RDB是间隔一段时间进行持久化，如果持久化之间redis发生故障，会发生数据丢失。所以这种方式更适合数据要求不严谨的时候

 

RDB默认开启，redis.conf中的**具体配置参数如下**；

\#dbfilename：持久化数据存储在本地的文件

dbfilename dump.rdb

\#dir：持久化数据存储在本地的路径，如果是在/redis/redis-3.0.6/src下启动的redis-cli，则数据会存储在当前src目录下

dir ./

\#save时间，以下分别表示更改了1个key时间隔900s进行持久化存储；更改了10个key300s进行存储；更改10000个key60s进行存储。

save 900 1

save 300 10

save 60 10000

 

持久化过程：

当满足save的条件时，比如更改了1个key，900s后会将数据写入临时文件，持久化完成后将临时文件替换旧的dump.rdb。（存储数据的节点是到触发时间时的的节点）

 

使用RDB恢复数据：

自动的持久化数据存储到dump.rdb后。实际只要重启redis服务即可完成（启动redis的server时会从dump.rdb中先同步数据）

 

使用命令进行持久化save存储：

./redis-cli -h ip -p port save

./redis-cli -h ip -p port bgsave

一个是在前台进行存储，一个是在后台进行存储。我的client就在server这台服务器上，所以不需要连其他机器，直接./redis-cli bgsave

 

**二、AOF（AppendOnly File）**

AOF是将执行过的指令记录下来，数据恢复时按照从前到后的顺序再将指令执行一遍，实现数据恢复

优点：可以保持更高的数据完整性，如果设置追加file的时间是1s，如果redis发生故障，最多会丢失1s的数据；且如果日志写入不完整支持redis-check-aof来进行日志修复；AOF文件没被rewrite之前（文件过大时会对命令进行合并重写），可以删除其中的某些命令（比如误操作的flushall）。

缺点：AOF文件比RDB文件大，且恢复速度慢。

 

AOF默认关闭，开启方法，修改配置文件reds.conf：appendonly yes

其他相关配置项：

\#AOF保存的文件名

appendfilename ""

 

**以下为同步方式相关的配置：**

\#一旦插入命令，立即同步到磁盘，保证了完全的持久化，但是速度慢，不推荐

appendfsync always

 

\#AOF每秒进行同步

appendfsync everysec

 

\#不自动同步，性能最好，但是持久化没有保证

appendfsync no

 

存储过程：将快照内容以命令的形式追加到AOF文件中，所以随着追加AOF文件会越来越大

保存的AOF文件存储了执行的所有命令，所以可以进行修改文件来撤销输错的命令（在重写之前，如果重写了就没有办法了）

 

针对AOF文件越来越大的问题，可以对AOF文件进行**重写**，命令如下：

redis-cli -h ip -p port bgrewriteaof

重写命令的操作过程：在当前的快照保存工作结束后，开启一个子进程，将AOF文件进行重写，合并set命令等操作到一个临时文件，达到缩小文件大小的目的。重写结束后后将临时文件替换为新的AOF文件（重写过程中如果有新的redis操作命令，会提交到缓存中，重写结束后追加到AOF文件内）

 

说明：redis2.4以上版本，重写机制自动触发。触发的相关redis.conf配置如下：

auto-aof-rewrite-percentage 100（当目前的AOF文件大小超过上一次重写文件大小的百分之几时进行重写，如果没有重启过，则以启动时的AOF文件大小为依据）；

auto-aof-rewrite-min-size 64mb（允许重写的最小AOF文件大小）；

数据恢复：

重启redis服务，前提是配置文件必须设置了appendonly yes，然后会从appendfile的文件加载文件。反之是从RDB中加载数据的。

 

下面的博客是具体讲redis启动过程中的操作的，比较好，大家可以看一下：

<http://www.jb51.net/article/63671.htm>

引自上面这个博客的加载数据的过程：



**加载数据：**

根据配置的不同，Redis加载数据的源也不一样，如果在配置文件里设置了appendonly yes（默认是no），那么就从appendfile加载数据，反之则从RedisDb加载数据

 

·从appendfile加载数据：我们先来看一下appendfile的内容是什么。下面的一条记录摘取自appendfile：SET $9 olylakers $3 oly。很显，appendfile保存的就是redis server接收到的各种命令，那么从appendfile加载数据就是redis server从appenfile里面读取这些命令的记录，然后重新把这些命令执行一遍即可。需要注意的是，如果开启了VM，那么在从appendfile加载数据的时候可能要涉及swap操作。
·从redisdb加载数据：如果没有开启appendonly，那么则需要从db file加载数据到内存，其过程是：
1.通过处理select命令，选择DB
2.然后从db file读取key和value
3.检查key是否过期，如果过期则跳过这个key，如果不过期，则把数据Add到对应的db的dict中

4.如果开启了VM，则从db file中load数据，也可能涉及到swap操作
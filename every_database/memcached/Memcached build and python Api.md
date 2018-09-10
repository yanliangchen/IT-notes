# Memcached  (ubuntu16.04)

## 1. 服务的部署，和启动。

**简介：**Memcached 是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提高动态、数据库驱动网站的速度。Memcached基于一个存储键/值对的[hashmap](http://baike.baidu.com/view/1487140.htm)。其[守护进程](http://baike.baidu.com/view/53123.htm)（daemon ）是用[C](http://baike.baidu.com/subview/10075/6770152.htm)写的，但是客户端可以用任何语言来编写，并通过memcached协议与守护进程通信。



**操作系统** ：ubuntu 16.04

​	**1 .安装memcached：  **sudo apt-get install memcached

​	**2.由于memcached依赖于libevent；因此，还需要安装libevent,命令如下：**

​			sudo apt-get install libevent-dev

​	**3.找到memcached的安装目录:** 

​			which  memcached 

​	**4.之后运行memcached   /usr/bin下**

​			./memcached -m 512 -p 11211 -vv

​		![img](http://7xknzt.com1.z0.glb.clouddn.com/memcache_4.JPG)

​	**5、使用telnet测试Memcached**

使用如下的命令连接上面刚启动的Memcached。

```
telnet localhost 112111
```

在控制台会看到如下的信息：

```
Trying 127.0.0.1...  
Connected to localhost.  
Escape character is '^]'. 
1234
```

保存数据的命令格式如下

```
    set foo 0 0 3
    bar12
```

如果保存成功，控制台会输出：STORED

获取数据的命令格式如下：

```
get foo1
```

在控制台的输出信息为：

```
VALUE foo 0 3
bar
END
```



输入 status 之后会出现一些参数

```
pid	MemCache服务器的进程id 
uptime	服务器已经运行的秒数
time	服务器当前的UNIX时间戳 
version	MemCache版本 
pointer_size	当前操作系统指针大小，反映了操作系统的位数，64意味着MemCache服务器是64位的 
rusage_user	进程的累计用户时间 
rusage_system 	进程的累计系统时间 
curr_connections 	 当前打开着的连接数
total_connections 	 当服务器启动以后曾经打开过的连接数
connection_structures 	服务器分配的连接构造数 
cmd_get 	get命令总请求次数 
cmd_set	set命令总请求次数 
cmd_flush 	flush_all命令总请求次数 
get_hits 	总命中次数，重要，缓存最重要的参数就是缓存命中率，以get_hits / (get_hits + get_misses)表示，比如这个缓存命中率就是99.2% 
get_misses 	总未命中次数 
auth_cmds 	认证命令的处理次数 
auth_errors 	认证失败的处理次数 
bytes_read 	总读取的字节数
bytes_written 	总发送的字节数 
 limit_maxbytes	分配给MemCache的内存大小（单位为字节） 
accepting_conns 	是否已经达到连接的最大值，1表示达到，0表示未达到
listen_disabled_num 	统计当前服务器连接数曾经达到最大连接的次数，这个次数应该为0或者接近于0，如果这个数字不断增长， 就要小心我们的服务了
threads 	当前MemCache总线程数，由于MemCache的线程是基于事件驱动机制的，因此不会一个线程对应一个用户请求 
bytes 	当前服务器存储的items总字节数
current_items 	当前服务器存储的items总数量 
total_items 	自服务器启动以后存储的items总数量 
```



## 2. Python操作Memcached 

###  **2. 1 首先安装python环境在ubuntu下**

​	//安装 Python 发布版本，dev包必须安装 ，很多用pip安装包都需要编译

​	**sudo  apt-get install python2.7  python2.7-dev **

​	//安装build依赖包

​	//很多pip安装的包都需要libssl和libevent编译环境	

​	**sudo apt-get install build-essential libssl-dev libevent-dev libjpeg-dev libxml2-dev libxslt-dev**

​	//安装pip

​	 **sudo apt-get install python-pip**

​	//安装 virtualenv

​	**sudo pip install virtualenv**

​	//配置个人用virtualenv

​	 **virtualenv --no-site-packages -p /usr/bin/python3.2 ~/.venv/python3.2**

​	//然后将下面的代码增加到~/.bashrc的最后面，缺省使用 virtualenv 来代替系统 Python 环境：

```
1 # 缺省激活python2.7环境
2 if [ -f ~/.venv/python2.7/bin/activate ]; then
3     . ~/.venv/python2.7/bin/activate
4 fi
```

​	

### 2.2 安装python 中的memcache （memcache提供了python的API）

​	**pip  install  python-Python-memcached**



### 2.3 使用  ：Python-memcached模块的用法

**在写下面的代码用memcach的时候，先把memcach服务搭起来**

**启动服务的命令 :  1  ./memcached -m 512 -p 12000 -vv**

​				**netstat -lnp :看服务起来没起来，里面有进程id和启动的服务还有端口**

​				**也可以telnet ip port : 检测主机端口有没有链接上，如果没有连接上，就需要把主机和端口进行放行**				

​			       **2.  之后全同了就可以写python代码了**

​				**3. 重启进程之后里面的数据就没了 (这里重启进程用kill -9  pid进程id)**

​				**4.这里记几个端口号：**

​						**端口总共是 ：0~65535**

​						**HTTPS :443**

​						**HTTP :80**

​						**telnet :23 **

​						**ssh ：22**



​	

**demo1**

```
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> #!/usr/bin/env python3
... #coding:utf8
... import memcache
>>> mc = memcache.Client(['10.130.1.122:12000'],debug=True)
>>> mc.set('name','python')
True
>>> ret=mc.get('name')
>>> print(ret)
python
>>> ret=mc.get('name')
>>> print(ret)
python

```



#### 



**demo2**

**set:设置一个键值对，如果key不存在，则创建，如果key存在，则修改**

**set_multi:设置多个键值对，如果key不存在，则创建，如果 key存在，则修改**

```
import  memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
res=mc.get('name1')

//设置多个键值对
dic  = {'name':'to','age':'19','job':'1T'}
mc.set_multi(dic)
mcname = mc.get('name')
mcage = mc.get('age')
mcjob = mc.get('job')

```



**demo3**

**add 添加一条键值对，如果已经存在的key,重复执行add会出现异常**

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import   memcache 
mc = mamcache.Client(['0.0.0.0:12000'])
mc.add('k1','v1')
//报错，对已存在的key重复添加，失败!!
mc.add('k2','v2')
ret1 =  mc.add('name','tom')
ret2 = mc.add（'name','jack')
结果:
False  #当已存在key  那么返回false  
True # 如果不存在key  那么返回true 
```



**demo4 **

**replace  :replace修改某个key的值 ，如果key不存在，则异常**

```
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
mc = memache.Cliet(['0.0.0.0:12000'])
mc.set('name','tom')
re =mc.replace('name','jack')
//如果key 存在 那么修改成功  返回True 
//如果key  不存在，修改失败，返回空值
```



**demo5**

**delete : 在Memcached 中删除指定的一个键值对**

**delete_multi : 在Memcached中删除指定多个键值对**

```
import  memcache 
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
res  =   mc.get('name')
mc.delete('name')
re = mc.get('name')

```



**demo6 **

**get:获取一个键值对  get_multi ：获取多个键值对**

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
re = mc.get('name')
print('get',re)     #获取一个键值对
dic = {'name':'to,','age':'19','job':'IT'}
mc.set_multi(dic)
regetmu=mc.get_multi(['name','age','job'])
print('get_multi',re) #获取多个键值对的值
```



**demo7**

**append : 修改指定key的值，在该值后面追加内容。**

**prepend : 修改指定key的值，在该值前面插入内容。**

```
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('num','第一|')
re = mc.get('num')
print(re)
mc.append('num','追加第二个') #在第一后面追加
re = mc.get('num')
print(re)
mc.prepend('num','我是零个')  #在第一前面追加
re = mc.get('num')
print(re)
结果：
第一|
第一|追加第二个
我是零个第一|追加第二个
```

**demo8**

**decr :自减，将Memcached中的一个值增加N(N默认为1)**

**incr :自减, 将Memcached中的一个值减少N(N默认为1)**



```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('num','1')
re = mc.get('num')
print('我是没加过的值',re)
mc.incr('num','9')
re = mc.get('num')
print('我是加上新增后的值',re)
mc.decr('num','5')
re = mc.get('num')
print('我是减去的值',re)
# 结果：
我是没加过的值 1
我是加上新增后的值 10
是减去的值 5
```



**demo9**

**俩人同时提交数据库，并发的数据混乱问题**

```
gets 和 cas
使用缓存系统共享数据资源就必然绕不开数据争夺和脏数据（数据混乱）的问题。

假设商城某件商品的剩余个数保存在memcache中，product_count = 900

A用户刷新页面从memecache中读取到product_count = 900

B用户刷新页面从memecache中读取到product_count = 900

A,B用户均购买商品，并修改product_count的值

A修改后，product_count = 899

B修改后，product_count = 899

然而正确数字应该是898，数据就混乱了。

如果想要避免这种情况的发生，则可以使用  gets　和　cas

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'],cache_cas=True)
mc.set('count','10')
reget = mc.get('count')
print('件数',reget)
regets = mc.gets('count')
print(regets)
# 如果有人在gets之后和cas之前修改了product_count，那么，
下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
recas = mc.cas('count','11')
print(recas)
regets = mc.gets('count')
print('修改',regets)
本质上每次执行gets时，会从memcache中获取一个自增的数字，通过cas去修改gets的值时，会携带之前获取的自增和memcache中的自增值进行比较，如果相等，则可以提交，如果不相等，那么表示在gets和cas执行之间，又有其他人执行了gets，则不允许修改。
```



## 3.Memcached访问模型

特别澄清一个问题，**MemCache虽然被称为"分布式缓存"，但是MemCache本身完全不具备分布式的功能**，MemCache集群之间不会相互通信（与之形成对比的，比如JBoss Cache，某台服务器有缓存数据更新时，会通知集群中其他机器更新缓存或清除缓存数据），所谓的"分布式"，完全依赖于客户端程序的实现，就像上面这张图的流程一样。



**分布式读写，和去缓存的原理，这里指定哪一台是关键**

```
1、应用程序输入需要写缓存的数据

2、API将Key输入路由算法模块，路由算法根据Key和MemCache集群服务器列表得到一台服务器编号

3、由服务器编号得到MemCache及其的ip地址和端口号

4、API调用通信模块和指定编号的服务器通信，将数据写入该服务器，完成一次分布式缓存的写操作

读缓存和写缓存一样，只要使用相同的路由算法和服务器列表，只要应用程序查询的是相同的Key，MemCache客户端总是访问相同的客户端去读取数据，只要服务器中还缓存着该数据，就能保证缓存命中。

这种MemCache集群的方式也是从分区容错性的方面考虑的，假如Node2宕机了，那么Node2上面存储的数据都不可用了，此时由于集群中Node0和Node1还存在，下一次请求Node2中存储的Key值的时候，肯定是没有命中的，这时先从数据库中拿到要缓存的数据，然后路由算法模块根据Key值在Node0和Node1中选取一个节点，把对应的数据放进去，这样下一次就又可以走缓存了，这种集群的做法很好，但是缺点是成本比较大。

```





## 4.MemCache实现原理

```
首先要说明一点，MemCache的数据存放在内存中，存放在内存中个人认为意味着几点：

1、访问数据的速度比传统的关系型数据库要快，因为Oracle、MySQL这些传统的关系型数据库为了保持数据的持久性，数据存放在硬盘中，IO操作速度慢

2、MemCache的数据存放在内存中同时意味着只要MemCache重启了，数据就会消失

3、既然MemCache的数据存放在内存中，那么势必受到机器位数的限制，这个之前的文章写过很多次了，32位机器最多只能使用2GB的内存空间，64位机器可以认为没有上限

然后我们来看一下MemCache的原理，MemCache最重要的莫不是内存分配的内容了，MemCache采用的内存分配方式是固定空间分配


//图片可以看http://www.cnblogs.com/xrq730/p/4948707.html
这张图片里面涉及了slab_class、slab、page、chunk四个概念，它们之间的关系是：

1、MemCache将内存空间分为一组slab

2、每个slab下又有若干个page，每个page默认是1M，如果一个slab占用100M内存的话，那么这个slab下应该有100个page

3、每个page里面包含一组chunk，chunk是真正存放数据的地方，同一个slab里面的chunk的大小是固定的

4、有相同大小chunk的slab被组织在一起，称为slab_class

MemCache内存分配的方式称为allocator，slab的数量是有限的，几个、十几个或者几十个，这个和启动参数的配置相关。

MemCache中的value过来存放的地方是由value的大小决定的，value总是会被存放到与chunk大小最接近的一个slab中，比如slab[1]的chunk大小为80字节、slab[2]的chunk大小为100字节、slab[3]的chunk大小为128字节（相邻slab内的chunk基本以1.25为比例进行增长，MemCache启动时可以用-f指定这个比例），那么过来一个88字节的value，这个value将被放到2号slab中。放slab的时候，首先slab要申请内存，申请内存是以page为单位的，所以在放入第一个数据的时候，无论大小为多少，都会有1M大小的page被分配给该slab。申请到page后，slab会将这个page的内存按chunk的大小进行切分，这样就变成了一个chunk数组，最后从这个chunk数组中选择一个用于存储数据。

如果这个slab中没有chunk可以分配了怎么办，如果MemCache启动没有追加-M（禁止LRU，这种情况下内存不够会报Out Of Memory错误），那么MemCache会把这个slab中最近最少使用的chunk中的数据清理掉，然后放上最新的数据。针对MemCache的内存分配及回收算法，总结三点：
```



## 5. MemCache的特性和限制 

```
1、MemCache中可以保存的item数据量是没有限制的，只要内存足够

2、MemCache单进程在32位机中最大使用内存为2G，这个之前的文章提了多次了，64位机则没有限制

3、Key最大为250个字节，超过该长度无法存储

4、单个item最大数据是1MB，超过1MB的数据不予存储

5、MemCache服务端是不安全的，比如已知某个MemCache节点，可以直接telnet过去，并通过flush_all让已经存在的键值对立即失效

6、不能够遍历MemCache中所有的item，因为这个操作的速度相对缓慢且会阻塞其他的操作

7、MemCache的高性能源自于两阶段哈希结构：第一阶段在客户端，通过Hash算法根据Key值算出一个节点；第二阶段在服务端，通过一个内部的Hash算法，查找真正的item并返回给客户端。从实现的角度看，MemCache是一个非阻塞的、基于事件的服务器程序

8、MemCache设置添加某一个Key值的时候，传入expiry为0表示这个Key值永久有效，这个Key值也会在30天之后失效
```



## 6.MemCache指令汇总

上面说过，已知MemCache的某个节点，直接telnet过去，就可以使用各种命令操作MemCache了，下面看下MemCache有哪几种命令：

| get         | 返回Key对应的Value值                           |
| ----------- | ---------------------------------------- |
| add         | 添加一个Key值，没有则添加成功并提示STORED，有则失败并提示NOT_STORED |
| set         | 无条件地设置一个Key值，没有就增加，有就覆盖，操作成功提示STORED     |
| replace     | 按照相应的Key值替换数据，如果Key值不存在则会操作失败            |
| stats       | 返回MemCache通用统计信息（下面有详细解读）                |
| stats items | 返回各个slab中item的数目和最老的item的年龄（最后一次访问距离现在的秒数） |
| stats slabs | 返回MemCache运行期间创建的每个slab的信息（下面有详细解读）      |
| version     | 返回当前MemCache版本号                          |
| flush_all   | 清空所有键值，但不会删除items，所以此时MemCache依旧占用内存     |
| quit        | 关闭连接                                     |



## 7.stats指令解读

stats是一个比较重要的指令，用于列出当前MemCache服务器的状态，拿一组数据举个例子：

```
STAT pid 1023
STAT uptime 21069937
STAT time 1447235954
STAT version 1.4.5
STAT pointer_size 64
STAT rusage_user 1167.020934
STAT rusage_system 3346.933170
STAT curr_connections 29
STAT total_connections 21
STAT connection_structures 49
STAT cmd_get 49
STAT cmd_set 7458
STAT cmd_flush 0
STAT get_hits 7401
STAT get_misses 57
..（delete、incr、decr、cas的hits和misses数，cas还多一个badval）
STAT auth_cmds 0
STAT auth_errors 0
STAT bytes_read 22026555
STAT bytes_written 8930466
STAT limit_maxbytes 4134304000
STAT accepting_conns 1
STAT listen_disabled_num 0
STAT threads 4
STAT bytes 151255336
STAT current_items 57146
STAT total_items 580656
STAT evicitions 0
```

这些参数反映着MemCache服务器的基本信息，它们的意思是：

| **参  数  名**           | **作      用**                             |
| --------------------- | ---------------------------------------- |
| pid                   | MemCache服务器的进程id                         |
| uptime                | 服务器已经运行的秒数                               |
| time                  | 服务器当前的UNIX时间戳                            |
| version               | MemCache版本                               |
| pointer_size          | 当前操作系统指针大小，反映了操作系统的位数，64意味着MemCache服务器是64位的 |
| rusage_user           | 进程的累计用户时间                                |
| rusage_system         | 进程的累计系统时间                                |
| curr_connections      | 当前打开着的连接数                                |
| total_connections     | 当服务器启动以后曾经打开过的连接数                        |
| connection_structures | 服务器分配的连接构造数                              |
| cmd_get               | get命令总请求次数                               |
| cmd_set               | set命令总请求次数                               |
| cmd_flush             | flush_all命令总请求次数                         |
| get_hits              | 总命中次数，重要，缓存最重要的参数就是缓存命中率，以get_hits / (get_hits + get_misses)表示，比如这个缓存命中率就是99.2% |
| get_misses            | 总未命中次数                                   |
| auth_cmds             | 认证命令的处理次数                                |
| auth_errors           | 认证失败的处理次数                                |
| bytes_read            | 总读取的字节数                                  |
| bytes_written         | 总发送的字节数                                  |
| limit_maxbytes        | 分配给MemCache的内存大小（单位为字节）                  |
| accepting_conns       | 是否已经达到连接的最大值，1表示达到，0表示未达到                |
| listen_disabled_num   | 统计当前服务器连接数曾经达到最大连接的次数，这个次数应该为0或者接近于0，如果这个数字不断增长， 就要小心我们的服务了 |
| threads               | 当前MemCache总线程数，由于MemCache的线程是基于事件驱动机制的，因此不会一个线程对应一个用户请求 |
| bytes                 | 当前服务器存储的items总字节数                        |
| current_items         | 当前服务器存储的items总数量                         |
| total_items           | 自服务器启动以后存储的items总数量                      |



## 8.stats slab指令解读

如果对上面的MemCache存储机制比较理解了，那么我们来看一下各个slab中的信息，还是拿一组数据举个例子：



```
 1 STAT1:chunk_size 96
 2 ...
 3 STAT 2:chunk_size 144
 4 STAT 2:chunks_per_page 7281
 5 STAT 2:total_pages 7
 6 STAT 2:total_chunks 50967
 7 STAT 2:used_chunks 45197
 8 STAT 2:free_chunks 1
 9 STAT 2:free_chunks_end 5769
10 STAT 2:mem_requested 6084638
11 STAT 2:get_hits 48084
12 STAT 2:cmd_set 59588271
13 STAT 2:delete_hits 0
14 STAT 2:incr_hits 0
15 STAT 2:decr_hits 0
16 STAT 2:cas_hits 0
17 STAT 2:cas_badval 0
18 ...
19 STAT 3:chunk_size 216
20 ...
```

首先看到，第二个slab的chunk_size（144）/第一个slab的chunk_size（96）=1.5，第三个slab的chunk_size（216）/第二个slab的chunk_size（144）=1.5，可以确定这个MemCache的增长因子是1.5，chunk_size以1.5倍增长。然后解释下字段的含义：

| **参  数  名**     | **作      用**                             |
| --------------- | ---------------------------------------- |
| chunk_size      | 当前slab每个chunk的大小，单位为字节                   |
| chunks_per_page | 每个page可以存放的chunk数目，由于每个page固定为1M即1024*1024字节，所以这个值就是（1024*1024/chunk_size） |
| total_pages     | 分配给当前slab的page总数                         |
| total_chunks    | 当前slab最多能够存放的chunk数，这个值是total_pages*chunks_per_page |
| used_chunks     | 已经被分配给存储对象的chunks数目                      |
| free_chunks     | 曾经被使用过但是因为过期而被回收的chunk数                  |
| free_chunks_end | 新分配但还没有被使用的chunk数，这个值不为0则说明当前slab从来没有出现过容量不够的时候 |
| mem_requested   | 当前slab中被请求用来存储数据的内存空间字节总数，（total_chunks*chunk_size）-mem_requested表示有多少内存在当前slab中是被闲置的，这包括未用的slab+使用的slab中浪费的内存 |
| get_hits        | 当前slab中命中的get请求数                         |
| cmd_set         | 当前slab中接收的所有set命令请求数                     |
| delete_hits     | 当前slab中命中的delete请求数                      |
| incr_hits       | 当前slab中命中的incr请求数                        |
| decr_hits       | 当前slab中命中的decr请求数                        |
| cas_hits        | 当前slab中命中的cas请求数                         |
| cas_badval      | 当前slab中命中但是更新失败的cas请求数                   |

看到这个命令的输出量很大，所有信息都很有作用。举个例子吧，比如第一个slab中使用的chunks很少，第二个slab中使用的chunks很多，这时就可以考虑适当增大MemCache的增长因子了，让一部分数据落到第一个slab中去，适当平衡两个slab中的内存，避免空间浪费。
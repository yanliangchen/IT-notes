

### **redis原理**

**介绍**

redis是一个开源的使用ANSI [**C语言**]编写，可基于内存亦可持久化的日志型、Key-Value[数据库](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93/103728)，



**定义 **

redis是一个key-value[存储系统](https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E7%B3%BB%E7%BB%9F)。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list([链表](https://baike.baidu.com/item/%E9%93%BE%E8%A1%A8))、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。这些[数据类型](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。

 

Redis 是一个高性能的key-value数据库。 redis的出现，很大程度补偿了[memcached](https://baike.baidu.com/item/memcached)这类key/value存储的不足，在部 分场合可以对关系数据库起到很好的补充作用。它提供了Java，C/C++，C#，PHP，JavaScript，Perl，Object-C，Python，Ruby，Erlang等客户端，使用很方便。 [1]  

 

Redis支持主从同步。数据可以从主服务器向任意数量的从服务器上同步，从服务器可以是关联其他从服务器的主服务器。这使得Redis可执行单层树复制。存盘可以有意无意的对数据进行写操作。由于完全实现了发布/订阅机制，使得从数据库在任何地方同步树时，可订阅一个频道并接收主服务器完整的消息发布记录。同步对读取操作的可扩展性和数据冗余很有帮助。

 

redis的官网地址，非常好记，是redis.io。（特意查了一下，域名后缀io属于国家域名，是british Indian Ocean territory，即英属印度洋领地）



**redis性能**

下面是官方的bench-mark数据： [1]  

 

测试完成了50个并发执行100000个请求。

 

设置和获取的值是一个256字节字符串。

 

Linux box是运行Linux 2.6,这是X3320 Xeon 2.5 ghz。

 

文本执行使用loopback接口(127.0.0.1)。

 

结果:读的速度是110000次/s,写的速度是81000次/s 。



**特点和memacache**

当接收到SAVE指令的时候，Redis就会dump数据到一个文件里面。

 

值得一说的是它的独家功能：存储列表和集合，这是它与mc之流相比更有竞争力的地方。

 

不介绍mc里面已经有的东东，只列出特殊的：

 

TYPE key — 用来获取某key的类型

 

KEYS pattern — 匹配所有符合模式的key，比如KEYS * 就列出所有的key了，当然，复杂度O(n)

```
复杂度：算法复杂度分为时间复杂度和空间复杂度。其作用： 时间复杂度是指执行算法所需要的计算工作量；而空间复杂度是指执行这个算法所需要的内存空间。（算法的复杂性体现在运行该算法时的计算机所需资源的多少上，计算机资源最重要的是时间和空间（即寄存器）资源，因此复杂度分为时间和空间复杂度。）
```

 

RANDOMKEY - 返回随机的一个key

 

RENAME oldkey[newkey](https://baike.baidu.com/item/newkey)— key也可以改名




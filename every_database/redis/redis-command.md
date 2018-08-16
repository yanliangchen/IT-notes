



**访问**

$ redis-cli -h 127.0.0.1

**密码验证** 

$ auto  123456



### key

**查看所有的数据**

$keys *

**创建库,默认在0**

$select 1 

**移动数据，将当前的数据库key移动到某个数据库,目标库有，则不能移动 **

$move mystring 1  

**删除数据库**

$flush db 

**随机出key**

$randomkey

**查看key的类型**

$type key

**设置key **

$set key1 value1 

**批量设置key**

$mset  key1 value1  key2 value2 key3 value3 

**批量获取key**

$mget  key1  key2 key3 

**删除key**

$del key1 

**判断是否存在key**

$exits key 

**设置过期时间给键**

$expire key 10 

**删除过期时间**

$persist key 







### string

$ set name  cxx 

$ get  name 

$ getrange  name 0 -1  字符串分段

$ mset key1 key2            批量设置 

$ mget key1 key2            批量获取 

$   setnx key value           不存在就插入（not exists）

$ setex key time value      过期时间（expire）

$ setrange key index value  从index开始替换value 

$incr   age  递增  //初始没有这个键 给这个值赋值成1  之后依次递增

$incrby age 10 递增

$ decr age        递减 

$decrby age 10   递减

$incrbyfloat     增减浮点数

$append          追加   往键的值里面进行追加

$strlen      长度





### hash

```
  hset myhash name cxx
    hget myhash name
    hmset myhash name cxx age 25 note "i am notes"
    hmget myhash name age note   
    hgetall myhash               获取所有的
    hexists myhash name          是否存在
    hsetnx myhash score 100      设置不存在的
    hincrby myhash id 1          递增
    hdel myhash name             删除
    hkeys myhash                 只取key
    hvals myhash                 只取value
    hlen myhash                  长度
```





### **list**

```
   lpush mylist a b c  左插入
    rpush mylist x y z  右插入
    lrange mylist 0 -1  数据集合
    lpop mylist  弹出元素
    rpop mylist  弹出元素
    llen mylist  长度
    lrem mylist count value  删除
    lindex mylist 2          指定索引的值
    lset mylist 2 n          索引设值
    ltrim mylist 0 4         删除key
    linsert mylist before a  插入
    linsert mylist after a   插入
    rpoplpush list list2     转移列表的数据
```





### set

set是一个集合，它是string类型的无序集合，set是通过hash table实现的，添加，删除，查找的时间复杂度都是O(1)，对于集合我们可以取并集，交集，差集。通过这些操作我们可以实现SNS中好友推荐和Blog的tag

```
set
    sadd myset redis 
    smembers myset       数据集合
    srem myset set1         删除
    sismember myset set1 判断元素是否在集合中
    scard key_name       个数
    sdiff | sinter | sunion 操作：集合间运算：差集 | 交集 | 并集
    srandmember          随机获取集合中的元素
    spop                 从集合中弹出一个元素
```





### zset

zset是在set的基础上增加了顺序，形成一个有序的集合。

每次指定后,zset会自动重新按新的值调整顺序,可以理解为由两列的mysql,一列存value,一列存顺序。

 

其中key理解为zset的名字.

 

zadd  添加元素 

 

zadd  myzset 1 "one" 

 

zadd  myzset 2 "two" 

 

zadd  myzset 3 "three" 

 

zrange myzset 0 -1 withscores 

 

这里的0和-1代表的是索引  withscores 输出顺序号

 

 

zrem  删除名称为key的zset中的元素 

 

zrem  myzset two

 

 

zincrby  以指定值来增加(减少)顺序 对数序号进行加减 

 

如果在名称为key的zset中,已经存在元素member，则该元素的sroce增加increment，

 

否则向该集合添加元素,其score的值为incrnment

 

zincrby myzset 2 one 

 

 

再比如 four这个元素是不存在的

 

 

zrank 返回名称为key的zset中的member元素的排名 (按score从小到大排序) 即下标 

 

zrank myzset two

 

 

zrevrank  反转 按照score从大到小排名 zrevrank myzset two

 

 

zrevrange  逆序 降序排序 

 

zrevrange  myzset 0 -1 withscores



 

zrangebyscore 返回下标在给定区间的元素 

 

zrangebyscore  myzset 2 3 withscore

 

 

zcount 返回集合中score在给定区间中的数量 

 

zcount  myzset 2 3

 

 

zcard  返回集合中所有元素的个数 

 

zcard  myzset

 

 

zremrangebyrank删除集合中在给定区间的元素 按照下标删除 

 

zremrangebyrank  myzset 1 2

 

zremrangebyscore删除集合中给定区间的元素 按照顺序删除 

 

zremrangebyscore  myzset 1 2

```
   zadd zset 1 one
    zadd zset 2 two
    zadd zset 3 three
    zincrby zset 1 one              增长分数
    zscore zset two                 获取分数
    zrange zset 0 -1 withscores     范围值
    zrangebyscore zset 10 25 withscores 指定范围的值
    zrangebyscore zset 10 25 withscores limit 1 2 分页
    Zrevrangebyscore zset 10 25 withscores  指定范围的值
    zcard zset  元素数量
    Zcount zset 获得指定分数范围内的元素个数
    Zrem zset one two        删除一个或多个元素
    Zremrangebyrank zset 0 1  按照排名范围删除元素
    Zremrangebyscore zset 0 1 按照分数范围删除元素
    Zrank zset 0 -1    分数最小的元素排名为0
    Zrevrank zset 0 -1  分数最大的元素排名为0
    Zinterstore
    zunionstore rank:last_week 7 rank:20150323 rank:20150324 rank:20150325  weights 1 1 1 1 1 1 1
```



### 排序

```
  sort mylist  排序
    sort mylist alpha desc limit 0 2 字母排序
    sort list by it:* desc           by命令
    sort list by it:* desc get it:*  get参数
    sort list by it:* desc get it:* store sorc:result  sort命令之store参数：表示把sort查询的结果集保存起来
```



### 订阅与发布

```
  订阅频道：subscribe chat1
    发布消息：publish chat1 "hell0 ni hao"
    查看频道：pubsub channels
    查看某个频道的订阅者数量: pubsub numsub chat1
    退订指定频道： unsubscrible chat1   , punsubscribe java.*
    订阅一组频道： psubscribe java.*
    
    
    
    取消息：  ？？？/ 没看到命令
```


# Python操作rabbitmq 实践笔记

摘自：https://www.cnblogs.com/wt11/p/5970297.html?from=timeline&isappinstalled=0

**发布/订阅  系统**

1.基本用法

生产者

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 chan = s_conn.channel()  #在连接上创建一个频道
 9 
10 chan.queue_declare(queue='hello') #声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
11 chan.basic_publish(exchange='',  #交换机
12                    routing_key='hello',#路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
13                    body='hello world')#生产者要发送的消息
14 print("[生产者] send 'hello world")
15 
16 s_conn.close()#当生产者发送完消息后，可选择关闭连接
17 
18 
19 输出：
20 [生产者] send 'hello world
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

消费者

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import pika

username = 'wt'#指定远程rabbitmq的用户名密码
pwd = '111111'
user_pwd = pika.PlainCredentials(username, pwd)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
chan = s_conn.channel()#在连接上创建一个频道

chan.queue_declare(queue='hello')#声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行


def callback(ch,method,properties,body): #定义一个回调函数，用来接收生产者发送的消息
    print("[消费者] recv %s" % body)

chan.basic_consume(callback,  #调用回调函数，从队列里取消息
                   queue='hello',#指定取消息的队列名
                   no_ack=True) #取完一条消息后，不给生产者发送确认消息，默认是False的，即  默认给rabbitmq发送一个收到消息的确认，一般默认即可
print('[消费者] waiting for msg .')
chan.start_consuming()#开始循环取消息

输出：
[消费者] waiting for msg .
[消费者] recv b'hello world'
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

2.  实现功能：（1）rabbitmq循环调度，将消息循环发送给不同的消费者，如：消息1,3,5发送给消费者1；消息2,4,6发送给消费者2。
                   （2）消息确认机制，为了确保一个消息不会丢失，RabbitMQ支持消息的确认 , 一个 ack(acknowlegement) 是从消费者端发送一个确认去告诉RabbitMQ 消息已经接收了、处理了，RabbitMQ可以释放并删除掉了。如果一个消费者死掉了（channel关闭、connection关闭、或者TCP连接断开了）而没有发送ack，RabbitMQ 就会认为这个消息没有被消费者处理，并会重新发送到生产者的队列里，如果同时有另外一个消费者在线，rabbitmq将会将消息很快转发到另外一个消费者中。 那样的话你就能确保虽然一个消费者死掉，但消息不会丢失。

​        这个是没有超时的，当消费方（consumer）死掉后RabbitMQ会重新转发消息，即使处理这个消息需要很长很长时间也没有问题。消息的 acknowlegments 默认是打开的，在前面的例子中关闭了： no_ack = True . 现在删除这个标识 然后 发送一个 acknowledgment。

​                   （3）消息持久化，将消息写入硬盘中。  RabbitMQ不允许你重新定义一个已经存在、但属性不同的queue。需要标记消息为持久化的 - 要通过设置 delivery_mode 属性为 2来实现。

　　　　　　　　消息持久化的注意点：

　　　　　　　　标记消息为持久化并不能完全保证消息不会丢失，尽管已经告诉RabbitMQ将消息保存到磁盘，但RabbitMQ接收到的消息在还没有保存的时候，仍然有一个短暂的时间窗口。RabbitMQ不会对每个消息都执行同步 --- 可能只是保存到缓存cache还没有写入到磁盘中。因此这个持久化保证并不是很强，但这比我们简单的任务queue要好很多，如果想要很强的持久化保证，可以使用 publisher confirms。

​                    （4）公平调度。在一个消费者未处理完一个消息之前不要分发新的消息给它，而是将这个新消息分发给另一个不是很忙的消费者进行处理。为了解决这个问题我们可以在消费者代码中使用 channel.basic.qos ( prefetch_count = 1 )，将消费者设置为公平调度。

生产者

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()  #在连接上创建一个频道
 9 
10 channel.queue_declare(queue='task_queue', durable=True) #创建一个新队列task_queue，设置队列持久化，注意不要跟已存在的队列重名，否则有报错
11 
12 message = "Hello World"
13 channel.basic_publish(exchange='',
14                       routing_key='worker',#写明将消息发送给队列worker
15                       body=message,    #要发送的消息
16                       properties=pika.BasicProperties(delivery_mode=2,)#设置消息持久化，将要发送的消息的属性标记为2，表示该消息要持久化
17                       )
18 print(" [生产者] Send %r " % message)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

消费者

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import time
 3 
 4 username = 'wt'#指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()#在连接上创建一个频道
 9 
10 channel.queue_declare(queue='task_queue', durable=True) #创建一个新队列task_queue，设置队列持久化，注意不要跟已存在的队列重名，否则有报错
11 
12 
13 def callback(ch, method, properties, body):
14     print(" [消费者] Received %r" % body)
15     time.sleep(1)
16     print(" [消费者] Done")
17     ch.basic_ack(delivery_tag=method.delivery_tag)#  接收到消息后会给rabbitmq发送一个确认
18 
19 channel.basic_qos(prefetch_count=1)   # 消费者给rabbitmq发送一个信息：在消费者处理完消息之前不要再给消费者发送消息
20 
21 channel.basic_consume(callback,
22                       queue='worker',
23                                       #这里就不用再写no_ack=False了
24                       )
25 channel.start_consuming()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 3.交换机

exchange：交换机。生产者不是将消息发送给队列，而是将消息发送给交换机，由交换机决定将消息发送给哪个队列。所以exchange必须准确知道消息是要送到哪个队列，还是要被丢弃。因此要在exchange中给exchange定义规则，所有的规则都是在exchange的类型中定义的。

exchange有4个类型：direct, topic, headers ,fanout

​    之前，我们并没有讲过exchange，但是我们仍然可以将消息发送到队列中。这是因为我们用的是默认exchange.也就是说之前写的：exchange=''，空字符串表示默认的exchange。

之前的代码结构：

```
1 channel.basic_publish(exchange='',
2                       routing_key='hello',
3                       body=message)
```

exchange = '参数'  

参数表示exchange 的名字，空字符串是默认或者没有exchange。消息被路由到某队列的根据是：routing_key.。如果routing_key的值存在的话。

现在，我们可以用我们自己命名的exchange来代替默认的exchange。

```
1 channel.basic_publish(exchange='logs',#自己命名exchange为logs
2                       routing_key='',
3                       body=message)
```

 （1）fanout：广播类型，生产者将消息发送给所有消费者，如果某个消费者没有收到当前消息，就再也收不到了（消费者就像收音机）

生产者：（可以用作日志收集系统）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1   import pika
 2   import sys
 3   username = 'wt'   #指定远程rabbitmq的用户名密码
 4   pwd = '111111'
 5   user_pwd = pika.PlainCredentials(username, pwd)
 6   s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 7   channel = s_conn.channel()  #在连接上创建一个频道
 8   channel.exchange_declare(exchange='logs',
 9                            type='fanout')#创建一个fanout(广播)类型的交换机exchange，名字为logs。
10  
11  message =  "info: Hello World!"
12  channel.basic_publish(exchange='logs',#指定交换机exchange为logs，这里只需要指定将消息发给交换机logs就可以了，不需要指定队列，因为生产者消息是发送给交换机的。
13                        routing_key='',#在fanout类型中，绑定关键字routing_key必须忽略，写空即可
14                        body=message)
15  print(" [x] Sent %r" % message)
16  connection.close()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

消费者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()  #在连接上创建一个频道
 9 
10  channel.exchange_declare(exchange='logs',
11                            type='fanout')#消费者需再次声明一个exchange 以及类型。
12  
13  result = channel.queue_declare(exclusive=True)#创建一个队列，exclusive=True（唯一性）表示在消费者与rabbitmq断开连接时，该队列会自动删除掉。
14  queue_name = result.method.queue#因为rabbitmq要求新队列名必须是与现存队列名不同，所以为保证队列的名字是唯一的，method.queue方法会随机创建一个队列名字，如：‘amq.gen-JzTY20BRgKO-HjmUJj0wLg‘。
15  
16  channel.queue_bind(exchange='logs',
17                     queue=queue_name)#将交换机logs与接收消息的队列绑定。表示生产者将消息发给交换机logs，logs将消息发给随机队列queue，消费者在随机队列queue中取消息
18  
19  print(' [消费者] Waiting for logs. To exit press CTRL+C')
20  
21  def callback(ch, method, properties, body):
22      print(" [消费者] %r" % body)
23  
24  channel.basic_consume(callback,#调用回调函数从queue中取消息
25                        queue=queue_name,
26                        no_ack=True)#设置为消费者不给rabbitmq回复确认。
27  
28  channel.start_consuming()#循环等待接收消息。
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

这样，开启多个消费者后，会同时从生产者接收相同的消息。

（2）direct：关键字类型。功能：交换机根据生产者消息中含有的不同的关键字将消息发送给不同的队列，消费者根据不同的关键字从不同的队列取消息

生产者：不用创建对列

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()  #在连接上创建一个频道
 9 
10 channel.exchange_declare(exchange='direct_logs',
11                          type='direct')#创建一个交换机并声明exchange的类型为：关键字类型，表示该交换机会根据消息中不同的关键字将消息发送给不同的队列
12 
13 severity =  'info'#severity这里只能为一个字符串，这里为‘info’表明本生产者只将下面的message发送到info队列中，消费者也只能从info队列中接收info消息
14 message = 'Hello World!'
15 channel.basic_publish(exchange='direct_logs',#指明用于发布消息的交换机、关键字
16                       routing_key=severity,#绑定关键字，即将message与关键字info绑定，明确将消息发送到哪个关键字的队列中。
17                       body=message)
18 print(" [生产者] Sent %r:%r" % (severity, message))
19 connection.close()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

消费者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()  #在连接上创建一个频道
 9 
10 channel.exchange_declare(exchange='direct_logs',
11                          type='direct')#创建交换机，命名为‘direct_logs’并声明exchange类型为关键字类型。
12 
13 result = channel.queue_declare(exclusive=True)#创建随机队列，当消费者与rabbitmq断开连接时，这个队列将自动删除。
14 queue_name = result.method.queue#分配随机队列的名字。
15 
16 severities = ['info','err']#可以接收绑定关键字info或err的消息，列表中也可以只有一个
17 if not severities:#判断如果输入有误，输出用法
18     sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
19     sys.exit(1)
20 
21 for severity in severities:
22     channel.queue_bind(exchange='direct_logs',#将交换机、队列、关键字绑定在一起，使消费者只能根据关键字从不同队列中取消息
23                        queue=queue_name,
24                        routing_key=severity)#该消费者绑定的关键字。
25 
26 print(' [消费者] Waiting for logs. To exit press CTRL+C')
27 
28 def callback(ch, method, properties, body):#定义回调函数，接收消息
29     print(" [消费者] %r:%r" % (method.routing_key, body))
30 
31 channel.basic_consume(callback,
32                       queue=queue_name,
33                       no_ack=True)#消费者接收消息后，不给rabbimq回执确认。
34 
35 channel.start_consuming()#循环等待消息接收。
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 （3）topics：模糊匹配类型。**比较常用**

发送到一个 topics交换机的消息，它的 routing_key不能是任意的 -- 它的routing_key必须是一个用小数点分割的单词列表。 这个字符可以是任何单词，但是通常是一些指定意义的字符。比如：“stock.usd.nyse","nyse.vmw","quick.orange.rabbit".  这里可以是你想要路由键的任意字符。最高限制为255字节。

 生产者与消费者的routing_key必须在同一个表单中。 Topic交换的背后的逻辑类似直接交换（direct） -- 包含特定关键字的消息将会分发到所有匹配的关键字队列中。然后有两个重要的特殊情况：

绑定键值：

\> * (星)  可代替一个单词

\> # (井) 可代替0个或多个单词

生产者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'   #指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()  #在连接上创建一个频道
 9 
10 channel.exchange_declare(exchange='topic_logs',
11                          type='topic')  # 创建模糊匹配类型的exchange。。
12 
13 routing_key = '[warn].kern'##这里关键字必须为点号隔开的单词，以便于消费者进行匹配。引申：这里可以做一个判断，判断产生的日志是什么级别，然后产生对应的routing_key，使程序可以发送多种级别的日志
14 message =  'Hello World!'
15 channel.basic_publish(exchange='topic_logs',#将交换机、关键字、消息进行绑定
16                       routing_key=routing_key,  # 绑定关键字，将队列变成[warn]日志的专属队列
17                       body=message)
18 print(" [x] Sent %r:%r" % (routing_key, message))
19 s_conn.close()
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

消费者：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 import pika
 2 import sys
 3 
 4 username = 'wt'#指定远程rabbitmq的用户名密码
 5 pwd = '111111'
 6 user_pwd = pika.PlainCredentials(username, pwd)
 7 s_conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.240', credentials=user_pwd))#创建连接
 8 channel = s_conn.channel()#在连接上创建一个频道
 9 
10 channel.exchange_declare(exchange='topic_logs',
11                          type='topic')  # 声明exchange的类型为模糊匹配。
12 
13 result = channel.queue_declare(exclusive=True)  # 创建随机一个队列当消费者退出的时候，该队列被删除。
14 queue_name = result.method.queue  # 创建一个随机队列名字。
15 
16 binding_keys = ['[warn]', 'info.*']#绑定键。‘#’匹配所有字符，‘*’匹配一个单词。这里列表中可以为一个或多个条件，能通过列表中字符匹配到的消息，消费者都可以取到
17 if not binding_keys:
18     sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
19     sys.exit(1)
20 
21 for binding_key in binding_keys:#通过循环绑定多个“交换机-队列-关键字”，只要消费者在rabbitmq中能匹配到与关键字相应的队列，就从那个队列里取消息
22     channel.queue_bind(exchange='topic_logs',
23                        queue=queue_name,
24                        routing_key=binding_key)
25 
26 print(' [*] Waiting for logs. To exit press CTRL+C')
27 
28 
29 def callback(ch, method, properties, body):
30     print(" [x] %r:%r" % (method.routing_key, body))
31 
32 
33 channel.basic_consume(callback,
34                       queue=queue_name,
35                       no_ack=True)#不给rabbitmq发送确认
36 
37 channel.start_consuming()#循环接收消息
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

4.远程过程调用（RPC）Remote procedure call

消息属性

AMQP协议在一个消息中预先定义了一个包含14个属性的集合。大部分属性很少用到，以下几种除外：

\> delivery_mode: 标记一个消息为持久的（值为2）或者 瞬时的（其它值）， 你需要记住这个属性（在第二课时用到过）

\> content_type : 用来描述 MIME 类型的编码 ,比如我们经常使用的 JSON 编码，设置这个属性就非常好实现： application/json

\> reply_to：reply_to没有特别的意义，只是一个普通的变量名，只是它通常用来命名一个 callback 队列

\> correlation_id ： 用来关联RPC的请求与应答。关联id的作用：当在一个队列中接收了一个返回，我们并不清楚这个结果时属于哪个请求的，这样当correlation_id属性使用后，我们为每个请求设置一个唯一值，这个值就是关联id。这样，请求会有一个关联id，该请求的返回结果也有一个相同的关联id。然后当我们从callback队列中接收到一个消息后，我们查看一下这个关联，基于这个我们就能将请求和返回进行匹配。如果我们看到一个未知的correlation_id值，我们可以直接丢弃这个消息 -- 它是不属于我们的请求。

 

RPC执行过程：

![img](http://img.blog.csdn.net/20160321235322526?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

​                                                                                                                                                                      callback队列

 

我们的RPC将会这样执行：

\>  当客户端启动后，它创建一个匿名的唯一的回调队列

\> 对一个RPC请求, 客户端发送一个消息包含两个属性： reply_to （用来设置回调队列）和 correlation_id（用来为每个请求设置一个唯一标识）

\> 请求发送到 rpc_queue队列

\> RPC worker( 服务端) 在那个队列中等待请求，当一个请求出现后，服务端就执行一个job并将结果消息发送给客户端，使用reply_to字段中的队列

\> 客户端在callback 队列中等待数据, 当一个消息出现后，检查这个correlation_id属性,如果和请求中的值匹配将返回给应用

 

 

代码：

rpc_server.py代码

```


1. #!/usr/bin/env python  
2. import pika  
3.   
4. connection = pika.BlockingConnection(pika.ConnectionParameters(  
5.         host='localhost'))  
6.   
7. channel = connection.channel()  
8.   
9. channel.queue_declare(queue='rpc_queue')  
10.   
11. def fib(n):  
12.     if n == 0:  
13.         return 0  
14.     elif n == 1:  
15.         return 1  
16.     else:  
17.         return fib(n-1) + fib(n-2)  
18.   
19. def on_request(ch, method, props, body):  
20.     n = int(body)  
21.   
22.     print(" [.] fib(%s)" % n)  
23.     response = fib(n)  
24.   
25.     ch.basic_publish(exchange='',  
26.                      routing_key=props.reply_to,  
27.                      properties=pika.BasicProperties(correlation_id = props.correlation_id),  
28.                      body=str(response))  
29.     ch.basic_ack(delivery_tag = method.delivery_tag)  
30.   
31. channel.basic_qos(prefetch_count=1)  
32. channel.basic_consume(on_request, queue='rpc_queue')  
33.   
34. print(" [x] Awaiting RPC requests")  
35. channel.start_consuming()  

```

 

服务端代码详单简单：

\> (4) 和往常一样我们建立一个连接并定义一个队列

\> (11) 我们定义了  斐波纳契 函数，假定输入的都是合法正数

\> (19) 我们定义了一个回调的 basic_consume, RPC服务的核心。 当收到请求后执行这个函数并返回结果

\> (32) 我们可能会执行多个服务端，为了在多个服务端上均匀的分布负荷，我们需要这是 prefetch_count。

 

rpc_client.py 代码：

 

[python]

 [view plain](http://blog.csdn.net/songfreeman/article/details/50951065#) [copy](http://blog.csdn.net/songfreeman/article/details/50951065#)

 [print](http://blog.csdn.net/songfreeman/article/details/50951065#)[?](http://blog.csdn.net/songfreeman/article/details/50951065#)

1. \#!/usr/bin/env python  
2. import pika  
3. import uuid  
4.   
5. class FibonacciRpcClient(object):  
6. ​    def __init__(self):  
7. ​        self.connection = pika.BlockingConnection(pika.ConnectionParameters(  
8. ​                host='localhost'))  
9.   
10. ​        self.channel = self.connection.channel()  
11.   
12. ​        result = self.channel.queue_declare(exclusive=True)  
13. ​        self.callback_queue = result.method.queue  
14.   
15. ​        self.channel.basic_consume(self.on_response, no_ack=True,  
16. ​                                   queue=self.callback_queue)  
17.   
18. ​    def on_response(self, ch, method, props, body):  
19. ​        if self.corr_id == props.correlation_id:  
20. ​            self.response = body  
21.   
22. ​    def call(self, n):  
23. ​        self.response = None  
24. ​        self.corr_id = str(uuid.uuid4())  
25. ​        self.channel.basic_publish(exchange='',  
26. ​                                   routing_key='rpc_queue',  
27. ​                                   properties=pika.BasicProperties(  
28. ​                                         reply_to = self.callback_queue,  
29. ​                                         correlation_id = self.corr_id,  
30. ​                                         ),  
31. ​                                   body=str(n))  
32. ​        while self.response is None:  
33. ​            self.connection.process_data_events()  
34. ​        return int(self.response)  
35.   
36. fibonacci_rpc = FibonacciRpcClient()  
37.   
38. print(" [x] Requesting fib(30)")  
39. response = fibonacci_rpc.call(30)  
40. print(" [.] Got %r" % response)  

 

客户端代码稍微复杂些：

\> (7) 我们建立一个连接，通道并定义一个专门的’callback‘队列用来接收回复

\> (16) 我们订阅了“callback”队列，因此我们能够接收 RPC 的返回结果

\> (18) ’on_response'  在每个返回中执行的回调是一个简单的job， 对每个返回消息将检查是否correlation_id使我们需要查找的那个ID，如果是，将保存结果到 self.response 并终端consuming循环

\> (23) 下一步，我们定义我们的main方法 - 执行实际的RPC请求

\> (24) 在这方法中，首先我们生产一个唯一的 correlatin_id 号并保存 -- 'on_response"回调函数将用着号码来匹配发送和接收的消息值

\> (25) 下一步，发布请求信息，使用两个属性： reply_to 和 correlation_id

\> (32) 这一步我们可以坐等结果的返回

\>(33) 最后我们返回结果给用户

 

**或者  看下边一篇好理解一点**

 

前面的例子都有个共同点，就是发送端发送消息出去后没有结果返回。如果只是单纯发送消息，当然没有问题了，但是在实际中，常常会需要接收端将收到的消息进行处理之后，返回给发送端。

 

**处理方法描述**：发送端在发送信息前，产生一个接收消息的临时队列，该队列用来接收返回的结果。其实在这里接收端、发送端的概念已经比较模糊了，因为发送端也同样要接收消息，接收端同样也要发送消息，所以这里笔者使用另外的示例来演示这一过程。

 

**示例内容**：假设有一个控制中心和一个计算节点，控制中心会将一个自然数N发送给计算节点，计算节点将N值加1后，返回给控制中心。这里用center.py模拟控制中心，compute.py模拟计算节点。

 

**compute.py代码分析**

 

```

#!/usr/bin/env python
#coding=utf8
import pika
 
#连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
 
#定义队列
channel.queue_declare(queue='compute_queue')
print ' [*] Waiting for n'
 
#将n值加1
def increase(n):
    return n + 1
 
#定义接收到消息的处理方法
def request(ch, method, properties, body):
    print " [.] increase(%s)"  % (body,)
 
    response = increase(int(body))
 
    #将计算结果发送回控制中心
    ch.basic_publish(exchange='',
                    routing_key=properties.reply_to,
                    body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)
 
channel.basic_qos(prefetch_count=1)
channel.basic_consume(request, queue='compute_queue')
 
channel.start_consuming()
```

 

计算节点的代码比较简单，值得一提的是，原来的接收方法都是直接将消息打印出来，这边进行了加一的计算，并将结果发送回控制中心。

 

**center.py代码分析**

 

```
#!/usr/bin/env python
#coding=utf8
import pika
 
class Center(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
 
        self.channel = self.connection.channel()
         
        #定义接收返回消息的队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
 
        self.channel.basic_consume(self.on_response,
                                  no_ack=True,
                                  queue=self.callback_queue)
 
    #定义接收到返回消息的处理方法
    def on_response(self, ch, method, props, body):
        self.response = body
     
     
    def request(self, n):
        self.response = None
        #发送计算请求，并声明返回队列
        self.channel.basic_publish(exchange='',
                                  routing_key='compute_queue',
                                  properties=pika.BasicProperties(
                                        reply_to = self.callback_queue,
                                         ),
                                  body=str(n))
        #接收返回的数据
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)
 
center = Center()
 
print " [x] Requesting increase(30)"
response = center.request(30)
print " [.] Got %r" % (response,)
```

 

上例代码定义了接收返回数据的队列和处理方法，并且在发送请求的时候将该队列赋值给reply_to，在计算节点代码中就是通过这个参数来获取返回队列的。

 

打开两个终端，一个运行代码python compute.py，另外一个终端运行center.py，如果执行成功，应该就能看到效果了。

 

笔者在测试的时候，出了些小问题，就是在center.py发送消息时没有指明返回队列，结果compute.py那边在计算完结果要发回数据时报错，提示routing_key不存在，再次运行也报错。用rabbitmqctl list_queues查看队列，发现compute_queue队列有1条数据，每次重新运行compute.py的时候，都会重新处理这条数据。后来使用/etc/init.d/rabbitmq-server restart重新启动下rabbitmq就ok了。

 

参考文章：<http://www.rabbitmq.com/tutorials/tutorial-six-python.html>
# Nginx(http服务器)



## 1.什么是Nginx

Nginx 是俄罗斯人编写的十分轻量级的 HTTP 服务器,Nginx，它的发音为“engine X”，是一个高性能的HTTP和反向代理服务器，同时也是一个 IMAP/POP3/SMTP 代理服务器。Nginx 是由俄罗斯人 Igor Sysoev 为俄罗斯访问量第二的 Rambler.ru 站点开发的，它已经在该站点运行超过两年半了。Igor Sysoev 在建立的项目时,使用基于 BSD 许可。

英文主页：[http://nginx.net](http://nginx.net/) 。

到 2013 年，目前有很多国内网站采用 Nginx 作为 Web 服务器，如国内知名的新浪、163、腾讯、Discuz、豆瓣等。据 netcraft 统计，Nginx 排名第 3，约占 15% 的份额(参见：<http://news.netcraft.com/archives/category/web-server-survey/> )

Nginx 以事件驱动的方式编写，所以有非常好的性能，同时也是一个非常高效的反向代理、负载平衡。其拥有匹配 Lighttpd 的性能，同时还没有 Lighttpd 的内存泄漏问题，而且 Lighttpd 的 mod_proxy 也有一些问题并且很久没有更新。





SSL(Secure Sockets Layer [安全套接层](https://baike.baidu.com/item/%E5%AE%89%E5%85%A8%E5%A5%97%E6%8E%A5%E5%B1%82)),及其继任者[传输层安全](https://baike.baidu.com/item/%E4%BC%A0%E8%BE%93%E5%B1%82%E5%AE%89%E5%85%A8)（Transport Layer Security，TLS）是为[网络通信](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1)提供安全及[数据完整性](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%AE%8C%E6%95%B4%E6%80%A7)的一种安全协议。TLS与SSL在[传输层](https://baike.baidu.com/item/%E4%BC%A0%E8%BE%93%E5%B1%82)对网络连接进行加密。



## 2.Nginx的特点

Nginx 做为 HTTP 服务器，有以下几项基本特性：

- 处理静态文件，索引文件以及自动索引；打开文件描述符缓冲．
- 无缓存的反向代理加速，简单的负载均衡和容错．
- FastCGI，简单的负载均衡和容错．
- 支持 SSL 和 TLSSNI．

Nginx 具有很高的稳定性。其它 HTTP 服务器，当遇到访问的峰值，或者有人恶意发起慢速连接时，也很可能会导致服务器物理内存耗尽频繁交换，失去响应，只能重启服务器。例如当前 apache 一旦上到 200 个以上进程，web响应速度就明显非常缓慢了。而 Nginx 采取了分阶段资源分配技术，使得它的 CPU 与内存占用率非常低。Nginx 官方表示保持 10,000 个没有活动的连接，它只占 2.5M 内存，所以类似 DOS 这样的攻击对 Nginx 来说基本上是毫无用处的。就稳定性而言,Nginx 比 lighthttpd 更胜一筹。

Nginx 支持热部署。它的启动特别容易, 并且几乎可以做到 7*24 不间断运行，即使运行数个月也不需要重新启动。你还能够在不间断服务的情况下，对软件版本进行进行升级。



Nginx 代码质量非常高，代码很规范，手法成熟，模块扩展也很容易。特别值得一提的是强大的 Upstream 与 Filter 链。Upstream 为诸如 reverse proxy,与其他服务器通信模块的编写奠定了很好的基础。而 Filter 链最酷的部分就是各个 filter 不必等待前一个 filter 执行完毕。它可以把前一个 filter 的输出做为当前 filter 的输入，这有点像 Unix 的管线。这意味着，一个模块可以开始压缩从后端服务器发送过来的请求，且可以在模块接收完后端服务器的整个请求之前把压缩流转向客户端。





## 3.Nigix的架构

1.Nigix在启动后，在unix系统中会以daemon的方式在后台运行，后台进程包含一个master进程和多个worker进程。

2.我们可以手动关掉后台，让nigix在前台运行，并且通过ngnix取消master进程（生产环境下，不会这么做，调试情况下，可以这么做）

3.Nginx 是以多进程的方式来工作的,Nginx 也是支持多线程的方式的



**进程**

```
考虑一个场景：浏览器，网易云音乐以及notepad++ 三个软件只能顺序执行是怎样一种场景呢？另外，假如有两个程序A和B，程序A在执行到一半的过程中，需要读取大量的数据输入（I/O操作），而此时CPU只能静静地等待任务A读取完数据才能继续执行，这样就白白浪费了CPU资源。你是不是已经想到在程序A读取数据的过程中，让程序B去执行，当程序A读取完数据之后，让程序B暂停。聪明，这当然没问题，但这里有一个关键词：切换。

既然是切换，那么这就涉及到了状态的保存，状态的恢复，加上程序A与程序B所需要的系统资源（内存，硬盘，键盘等等）是不一样的。自然而然的就需要有一个东西去记录程序A和程序B分别需要什么资源，怎样去识别程序A和程序B等等(比如读书)。

进程定义：

进程就是一个程序在一个数据集上的一次动态执行过程。进程一般由程序、数据集、进程控制块三部分组成。我们编写的程序用来描述进程要完成哪些功能以及如何完成；数据集则是程序在执行过程中所需要使用的资源；进程控制块用来记录进程的外部特征，描述进程的执行变化过程，系统可以利用它来控制和管理进程，它是系统感知进程存在的唯一标志。

举一例说明进程：
想象一位有一手好厨艺的计算机科学家正在为他的女儿烘制生日蛋糕。他有做生日蛋糕的食谱，厨房里有所需的原料:面粉、鸡蛋、糖、香草汁等。在这个比喻中，做蛋糕的食谱就是程序(即用适当形式描述的算法)计算机科学家就是处理器(cpu)，而做蛋糕的各种原料就是输入数据。进程就是厨师阅读食谱、取来各种原料以及烘制蛋糕等一系列动作的总和。现在假设计算机科学家的儿子哭着跑了进来，说他的头被一只蜜蜂蛰了。计算机科学家就记录下他照着食谱做到哪儿了(保存进程的当前状态)，然后拿出一本急救手册，按照其中的指示处理蛰伤。这里，我们看到处理机从一个进程(做蛋糕)切换到另一个高优先级的进程(实施医疗救治)，每个进程拥有各自的程序(食谱和急救手册)。当蜜蜂蛰伤处理完之后，这位计算机科学家又回来做蛋糕，从他离开时的那一步继续做下去。
```

**线程**

```
线程的出现是为了降低上下文切换的消耗，提高系统的并发性，并突破一个进程只能干一样事的缺陷，使到进程内并发成为可能。

假设，一个文本程序，需要接受键盘输入，将内容显示在屏幕上，还需要保存信息到硬盘中。若只有一个进程，势必造成同一时间只能干一样事的尴尬（当保存时，就不能通过键盘输入内容）。若有多个进程，每个进程负责一个任务，进程A负责接收键盘输入的任务，进程B负责将内容显示在屏幕上的任务，进程C负责保存内容到硬盘中的任务。这里进程A，B，C间的协作涉及到了进程通信问题，而且有共同都需要拥有的东西——-文本内容，不停的切换造成性能上的损失。若有一种机制，可以使任务A，B，C共享资源，这样上下文切换所需要保存和恢复的内容就少了，同时又可以减少通信所带来的性能损耗，那就好了。是的，这种机制就是线程。
线程也叫轻量级进程，它是一个基本的CPU执行单元，也是程序执行过程中的最小单元，由线程ID、程序计数器、寄存器集合和堆栈共同组成。线程的引入减小了程序并发执行时的开销，提高了操作系统的并发性能。线程没有自己的系统资源。
```

**进程和线程的关系**

```
进程是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。或者说进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。
线程则是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位。
```



**并行和并发**

```
并行处理（Parallel Processing）是计算机系统中能同时执行两个或更多个处理的一种计算方法。并行处理可同时工作于同一程序的不同方面。并行处理的主要目的是节省大型和复杂问题的解决时间。并发处理(concurrency Processing)：指一个时间段中有几个程序都处于已启动运行到运行完毕之间，且这几个程序都是在同一个处理机(CPU)上运行，但任一个时刻点上只有一个程序在处理机(CPU)上运行

并发的关键是你有处理多个任务的能力，不一定要同时。并行的关键是你有同时处理多个任务的能力。所以说，并行是并发的子集
```

**同步和异步**

```
在计算机领域，同步就是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到收到返回信息才继续执行下去；异步是指进程不需要一直等下去，而是继续执行下面的操作，不管其他进程的状态。当有消息返回时系统会通知进程进行处理，这样可以提高执行的效率。举个例子，打电话时就是同步通信，发短息时就是异步通信。
```

**Nginx启动后操作Nginx**

4.在 Nginx 启动后，如果我们要操作 Nginx，要怎么做呢？master 来管理 worker 进程，所以我们只需要与 master 进程通信就行了。master 进程会接收来自外界发来的信号，再根据信号做不同的事情。所以我们要控制 Nginx，只需要通过 kill 向 master 进程发送信号就行了。比如`kill -HUP pid`，则是告诉 Nginx，从容地重启 Nginx，我们一般用这个信号来重启 Nginx，或重新加载配置，因为是从容地重启，因此服务是不中断的。master 进程在接收到 HUP 信号后是怎么做的呢？首先 master 进程在接到信号后，会先重新加载配置文件，然后再启动新的 worker 进程，并向所有老的 worker 进程发送信号，告诉他们可以光荣退休了。新的 worker 在启动后，就开始接收新的请求，而老的 worker 在收到来自 master 的信号后，就不再接收新的请求，并且在当前进程中的所有未处理完的请求处理完成后，再退出。当然，直接给 master 进程发送信号，这是比较老的操作方式，Nginx 在 0.8 版本之后，引入了一系列命令行参数，来方便我们管理。比如，`./nginx -s reload`，就是来重启 Nginx，`./nginx -s stop`，就是来停止 Nginx 的运行。如何做到的呢？我们还是拿 reload 来说，我们看到，执行命令时，我们是启动一个新的 Nginx 进程，而新的 Nginx 进程在解析到 reload 参数后，就知道我们的目的是控制 Nginx 来重新加载配置文件了，它会向 master 进程发送信号，然后接下来的动作，就和我们直接向 master 进程发送信号一样了。



**Nginx 是如何来处理事件的**

5.有人可能要问了，Nginx 采用多 worker 的方式来处理请求，每个 worker 里面只有一个主线程，那能够处理的并发数很有限啊，多少个 worker 就能处理多少个并发，何来高并发呢？非也，这就是 Nginx 的高明之处，Nginx 采用了异步非阻塞的方式来处理请求，也就是说，Nginx 是可以同时处理成千上万个请求的。

为什么 Nginx 可以采用异步非阻塞的方式来处理呢，或者异步非阻塞到底是怎么回事呢？我们先回到原点，看看一个请求的完整过程。首先，请求过来，要建立连接，然后再接收数据，接收数据后，再发送数据。具体到系统底层，就是读写事件，而当读写事件没有准备好时，必然不可操作，



它们提供了一种机制，让你可以同时监控多个事件，调用他们是阻塞的，但可以设置超时时间，在超时时间之内，如果有事件准备好了，就返回。这种机制正好解决了我们上面的两个问题，拿 epoll 为例(在后面的例子中，我们多以 epoll 为例子，以代表这一类函数)，当事件没准备好时，放到 epoll 里面，事件准备好了，我们就去读写，当读写返回 EAGAIN 时，我们将它再次加入到 epoll 里面。这样，只要有事件准备好了，我们就去处理它，只有当所有事件都没准备好时，才在 epoll 里面等着。这样，我们就可以并发处理大量的并发了，当然，这里的并发请求，是指未处理完的请求，线程只有一个，所以同时能处理的请求当然只有一个了，只是在请求间进行不断地切换而已，切换也是因为异步事件未准备好，而主动让出的。这里的切换是没有任何代价，你可以理解为循环处理多个准备好的事件，事实上就是这样的。与多线程相比，这种事件处理方式是有很大的优势的，不需要创建线程，每个请求占用的内存也很少，没有上下文切换，事件处理非常的轻量级。并发数再多也不会导致无谓的资源浪费（上下文切换）。更多的并发数，只是会占用更多的内存而已。 我之前有对连接数进行过测试，在 24G 内存的机器上，处理的并发请求数达到过 200 万。现在的网络服务器基本都采用这种方式，这也是nginx性能高效的主要原因。



## 4.Nigix 基础概念

1. 在 Nginx 中 connection 就是对 tcp 连接的封装，其中包括连接的 socket，读事件，写事件。利用 Nginx 封装的 connection，我们可以很方便的使用 Nginx 来处理与连接相关的事情，比如，建立连接，发送与接受数据等。而 Nginx 中的 http 请求的处理就是建立在 connection之上的，所以 Nginx 不仅可以作为一个web服务器，也可以作为邮件服务器。当然，利用 Nginx 提供的 connection，我们可以与任何后端服务打交道。
2. 结合一个 tcp 连接的生命周期，我们看看 Nginx 是如何处理一个连接的。首先，Nginx 在启动时，会解析配置文件，得到需要监听的端口与 ip 地址，然后在 Nginx 的 master 进程里面，先初始化好这个监控的 socket(创建 socket，设置 addrreuse 等选项，绑定到指定的 ip 地址端口，再 listen)，然后再 fork 出多个子进程出来，然后子进程会竞争 accept 新的连接。此时，客户端就可以向 Nginx 发起连接了。当客户端与服务端通过三次握手建立好一个连接后，Nginx 的某一个子进程会 accept 成功，得到这个建立好的连接的 socket，然后创建 Nginx 对连接的封装，即 ngx_connection_t 结构体。接着，设置读写事件处理函数并添加读写事件来与客户端进行数据的交换。最后，Nginx 或客户端来主动关掉连接，到此，一个连接就寿终正寝了。



## 5.Nginx是什么，有什么优点(博客)

摘自:https://zhidao.baidu.com/question/716711650194437965.html

```
Nginx是一个高性能的 HTTP 和 反向代理 服务器，也是一个 IMAP/POP3/SMTP 代理服务器。因它的稳定性、丰富的功能集、示例配置文件和低系统资源的消耗而闻名。2011年6月1日，nginx 1.0.4发布。
优点：
（1）更快
这表现在两个方面：一方面，在正常情况下，单次请求会得到更快的响应；另一方面，在高峰期（如有数以万计的并发请求），Nginx可以比其他Web服务器更快地响应请求。
（2）高扩展性，跨平台
Nginx的设计极具扩展性，它完全是由多个不同功能、不同层次、不同类型且耦合度极低的模块组成。因此，当对某一个模块修复Bug或进行升级时，可以专
注于模块自身，无须在意其他。而且在HTTP模块中，还设计了HTTP过滤器模块：一个正常的HTTP模块在处理完请求后，会有一串HTTP过滤器模块对
请求的结果进行再处理。这样，当我们开发一个新的HTTP模块时，不但可以使用诸如HTTP核心模块、events模块、log模块等不同层次或者不同类
型的模块，还可以原封不动地复用大量已有的HTTP过滤器模块。这种低耦合度的优秀设计，造就了Nginx庞大的第三方模块，当然，公开的第三方模块也如
官方发布的模块一样容易使用。
Nginx的模块都是嵌入到二进制文件中执行的，无论官方发布的模块还是第三方模块都是如此。这使得第三方模块一样具备极其优秀的性能，充分利用Nginx的高并发特性，因此，许多高流量的网站都倾向于开发符合自己业务特性的定制模块。
（3）高可靠性：用于反向代理，宕机的概率微乎其微
高可靠性是我们选择Nginx的最基本条件，因为Nginx的可靠性是大家有目共睹的，很多家高流量网站都在核心服务器上大规模使用Nginx。
Nginx的高可靠性来自于其核心框架代码的优秀设计、模块设计的简单性；另外，官方提供的常用模块都非常稳定，每个worker进程相对独
立，master进程在1个worker进程出错时可以快速“拉起”新的worker子进程提供服务。
（4）低内存消耗
一般情况下，10 000个非活跃的HTTP Keep-Alive连接在Nginx中仅消耗2.5MB的内存，这是Nginx支持高并发连接的基础。
（5）单机支持10万以上的并发连接
这是一个非常重要的特性！随着互联网的迅猛发展和互联网用户数量的成倍增长，各大公司、网站都需要应付海量并发请求，一个能够在峰值期顶住10万以上并发
请求的Server，无疑会得到大家的青睐。理论上，Nginx支持的并发连接上限取决于内存，10万远未封顶。当然，能够及时地处理更多的并发请求，是
与业务特点紧密相关的。
（6）热部署
master管理进程与worker工作进程的分离设计，使得Nginx能够提供热部署功能，即可以在7×24小时不间断服务的前提下，升级Nginx的可执行文件。当然，它也支持不停止服务就更新配置项、更换日志文件等功能。
（7）最自由的BSD许可协议
这是Nginx可以快速发展的强大动力。BSD许可协议不只是允许用户免费使用Nginx，它还允许用户在自己的项目中直接使用或修改Nginx源码，然后发布。这吸引了无数开发者继续为Nginx贡献自己的智慧。
以上7个特点当然不是Nginx的全部，拥有无数个官方功能模块、第三方功能模块使得Nginx能够满足绝大部分应用场景，这些功能模块间可以叠加以实现
更加强大、复杂的功能，有些模块还支持Nginx与Perl、Lua等脚本语言集成工作，大大提高了开发效率。这些特点促使用户在寻找一个Web服务器时
更多考虑Nginx。
选择Nginx的核心理由还是它能在支持高并发请求的同时保持高效的服务。
```

 



## 6. Nigix的一些基本功能

摘自：https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887

1、静态HTTP服务器

首先，Nginx是一个HTTP服务器，可以将服务器上的静态文件（如HTML、图片）通过HTTP协议展现给客户端。

配置：

**[plain]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. server {  
2. ​    listen80; # 端口号  
3. ​    location / {  
4. ​        root /usr/share/nginx/html; # 静态文件路径  
5. ​    }  
6. }  

 

2、反向代理服务器

什么是反向代理？

客户端本来可以直接通过HTTP协议访问某网站应用服务器，网站管理员可以在中间加上一个Nginx，客户端请求Nginx，Nginx请求应用服务器，然后将结果返回给客户端，此时Nginx就是反向代理服务器。

配置：

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. server {  
2. ​    listen80;  
3. ​    location / {  
4. ​        proxy_pass http://192.168.20.1:8080; # 应用服务器HTTP地址  
5. ​    }  
6. }  

既然服务器可以直接HTTP访问，为什么要在中间加上一个反向代理，不是多此一举吗？反向代理有什么作用？继续往下看，下面的负载均衡、虚拟主机等，都基于反向代理实现，当然反向代理的功能也不仅仅是这些。

3、负载均衡

当网站访问量非常大，网站[站长](http://zz.2cto.com/)开心赚钱的同时，也摊上事儿了。因为网站越来越慢，一台服务器已经不够用了。于是将同一个应用部署在多台服务器上，将大量用户的请求分配给多台机器处理。同时带来的好处是，其中一台服务器万一挂了，只要还有其他服务器正常运行，就不会影响用户使用。

Nginx可以通过反向代理来实现负载均衡。

配置 

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. upstream myapp {  
2. ​    server192.168.20.1:8080; # 应用服务器1  
3. ​    server192.168.20.2:8080; # 应用服务器2  
4. }  
5. server {  
6. ​    listen80;  
7. ​    location / {  
8. ​        proxy_pass http://myapp;  
9. ​    }  
10. }  

以上配置会将请求轮询分配到应用服务器，也就是一个客户端的多次请求，有可能会由多台不同的服务器处理。可以通过ip-hash的方式，根据客户端ip地址的hash值将请求分配给固定的某一个服务器处理。

配置：

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. upstream myapp {  
2. ​    ip_hash; # 根据客户端IP地址Hash值将请求分配给固定的一个服务器处理  
3. ​    server192.168.20.1:8080;  
4. ​    server192.168.20.2:8080;  
5. }  
6. server {  
7. ​    listen80;  
8. ​    location / {  
9. ​        proxy_pass http://myapp;  
10. ​    }  
11. }  

另外，服务器的硬件配置可能有好有差，想把大部分请求分配给好的服务器，把少量请求分配给差的服务器，可以通过weight来控制。

 

配置：

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. upstream myapp {  
2. ​    server192.168.20.1:8080weight=3; # 该服务器处理3/4请求  
3. ​    server192.168.20.2:8080; # weight默认为1，该服务器处理1/4请求  
4. }  
5. server {  
6. ​    listen80;  
7. ​    location / {  
8. ​        proxy_pass http://myapp;  
9. ​    }  
10. }  

4、虚拟主机

有的网站访问量大，需要负载均衡。然而并不是所有网站都如此出色，有的网站，由于访问量太小，需要节省成本，将多个网站部署在同一台服务器上。

例如将www.aaa.com和www.bbb.com两个网站部署在同一台服务器上，两个域名解析到同一个IP地址，但是用户通过两个域名却可以打开两个完全不同的网站，互相不影响，就像访问两个服务器一样，所以叫两个虚拟主机。

配置：

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. server {  
2. ​    listen80default_server;  
3. ​    server_name _;  
4. ​    return444; # 过滤其他域名的请求，返回444状态码  
5. }  
6. server {  
7. ​    listen80;  
8. ​    server_name www.aaa.com; # www.aaa.com域名  
9. ​    location / {  
10. ​        proxy_pass http://localhost:8080; # 对应端口号8080  
11. ​    }  
12. }  
13. server {  
14. ​    listen80;  
15. ​    server_name www.bbb.com; # www.bbb.com域名  
16. ​    location / {  
17. ​        proxy_pass http://localhost:8081; # 对应端口号8081  
18. ​    }  
19. }  

在服务器8080和8081分别开了一个应用，客户端通过不同的域名访问，根据server_name可以反向代理到对应的应用服务器。

虚拟主机的原理是通过HTTP请求头中的Host是否匹配server_name来实现的，有兴趣的同学可以研究一下HTTP协议。

另外，server_name配置还可以过滤有人恶意将某些域名指向你的主机服务器。

5、FastCGI

Nginx本身不支持[PHP](http://www.2cto.com/kf/web/php/)等语言，但是它可以通过FastCGI来将请求扔给某些语言或框架处理（例如PHP、[Python](http://www.2cto.com/kf/web/Python/)、Perl）。

**[html]** [view plain](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#) [copy](https://blog.csdn.net/ZhongGuoZhiChuang/article/details/52816887#)

1. server {  
2. ​    listen80;  
3. ​    location ~ \.php$ {  
4. ​        include fastcgi_params;  
5. ​        fastcgi_param SCRIPT_FILENAME /PHP文件路径$fastcgi_script_name; # PHP文件路径  
6. ​        fastcgi_pass127.0.0.1:9000; # PHP-FPM地址和端口号  
7. ​        # 另一种方式：fastcgi_pass unix:/var/run/php5-fpm.sock;  
8. ​    }  
9. }  

 

配置中将.php结尾的请求通过FashCGI交给PHP-FPM处理，PHP-FPM是PHP的一个FastCGI管理器。有

# 案例1 .：Flask+uwsgi+Nginx+Ubuntu部署



 学了一段时间flask，可是一直没有做过部署， 于是想着怎么部署呢， 想想，先吧服务给搞通吧，于是呢 就先想着去吧服务给搞起来，这里选择的是Flask+uwsgi+Nginx+Ubuntu， Python选择的是2.7.2这个是Ubuntu系统自带的学起来感觉还是简单的 不用去软连，目前自己的flask是python3写的 ，慢慢去过渡，先吧这个给搞通了，那么在优化也是很顺手的。其实对于很多的原理自己也是一知半解，先吧这个给搭起来，慢慢去了解里面的逻辑什么的。

**Nginx**

Nginx 是高效的 Web 服务器和反向代理服务器，可以用作负载均衡（当有 n 个用户访问服务器时，可以实现分流，分担服务器的压力），与 Apache 相比，Nginx 支持高并发，可以支持百万级的 TCP 连接，十万级别的并发连接，部署简单，内存消耗少，成本低，但 Nginx 的模块没有 Apache 丰富。Nginx 支持 uWSGI 的 uwsgi 协议，因此我们可以将 Nginx 与 uWSGI 结合起来，Nginx 通过 `uwsgi_pass` 将动态内容交给 uWSGI 处理。

官方文档在[这](https://www.nginx.com/resources/wiki/)

最好的 Nginx 教程在[这](http://openresty.org/download/agentzh-nginx-tutorials-zhcn.html)

**uwsgi**

uWSGI是一个[Web服务器](http://baike.baidu.com/item/Web%E6%9C%8D%E5%8A%A1%E5%99%A8)，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。

要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

- WSGI看过前面小节的同学很清楚了，是一种通信协议。
- uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
- 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，它与WSGI相比是两样东西。

 

  准备工作，首先呢，我们先去安装我们需要的包，首先呢  我这里是我新装的系统，所以没有pip，所以我先来去安装pip

```
sudo apt-get install python-pip
```

使用 下面命令去安装flask

```
pip install flask
```

安装后呢，我们可以去测试下，

import flask

没有报错证明我们的flask 是安装成功的。那么接下来我们要做的就是安装ngnix和uwsgi。

```
sudo apt-get install nginx
```

安装好以后，我们可以先启动下， nginx start 直接命令行启动，简单粗暴

![img](https://images2015.cnblogs.com/blog/920110/201707/920110-20170708162915378-2128117815.jpg)

这样我们的nginx就启动成功了，接下来，我们就是利用pip 去安装uwsgi

我们安装好后，那么接下来就开始开干吧，

首先我在hellowflak下创建一个app的python的包，

```
#app/__init__.py
from flask import Flask
app = Flask(__name__)
from app import view
```

接下来我们去创建view.py

```
from app import app
@app.route('/')
def index():
    return 'hellow'
```

那么我们去在app同级目录创建hello.py

```
from app import app
if __name__ == "__main__":
    app.run()
```

，那么我们可以在本地利用Python去调试我们的程序，

![img](https://images2015.cnblogs.com/blog/920110/201707/920110-20170708163558206-2078332090.jpg)

那么我们可以在浏览器去看看，输入地址，可以得到这个，这么来看我们flask程序是没有问题的。

![img](https://images2015.cnblogs.com/blog/920110/201707/920110-20170708163651440-244771023.jpg)

那么我们接下来要做的就是让nginx去承担web服务。

我这里做的是简单粗暴直接删除nginx的配置文件

```
$ sudo rm /etc/nginx/sites-enabled/default
```

接下来，我在hellowflask下创建的一个配置文件

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

server {
listen 3389;
server_name 60.205.187.178 www.lileilei.online;
charset utf-8;
client_max_body_size 75M;
location / {
include uwsgi_params;
uwsgi_pass 127.0.0.1:9160;
uwsgi_param UWSGI_PYTHON /usr/bin/python;
uwsgi_param UWSGI_CHDIR /home/flask_blog-python3;
uwsgi_param UWSGI_SCRIPT hello:application;
} 
}

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

稍作解释：server_name 可以是域名，也可以写 ip 地址，uwsgi_pass 是表明 Nginx 与 uwsgi 的交流方式。我这里选择的是制定的端口号。

那么我们接下来去软连我们的这个配置到nginx中去。

```
sudo ln -s /home/liwanlei/Desktop/hellowflask/helloflask_nginx.conf /etc/nginx/conf.d/
这样我们再去启动我们的nginx，
```

```
sudo /etc/init.d/nginx restart
```

这里的不是welcome了，而是502错误呢，因为我们现在的uwsgi文件还没有配置，也没有去启动uwsgi，那么我们接下来就是要去出来这个uwsgi，下面的例子是我的配置。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[uwsgi]
base = /home/flask_blog-python3
pidfile = /var/run/uwsgi.pid
master = true
wsgi-file = hello.py
chdir = /home/flask_blog-python3
socket = 127.0.0.1:9160
callable = application
logto = %n.log
processes = 10
master = true 
workers=10
enable-threads = true

py-autoreload = 1

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

这时候我们的uwsgi已经配置号，那么我们去启动，

```
sudo /usr/bin/uwsgi --ini/home/liwanlei/Desktop/hellowflask/helloflask_uwsgi.ini
```

我们去重新启动我们的nginx，

```
sudo nginx reload
平滑重启可以用用，重新加载配置文件，用新的工作进程代替旧的工作进程。

```

```
sudo nginx -s reload
```

```
启动后，我这里修改了地址，这里就可以直接访问了，那么我们的部署这样就算可以了，简单的。

```

```
 
```

完工之后，感觉还是很简单的 有问题那么就去看log，只要log配置得当，那么排除错误是很快的。

**我已经成功的把我写的部署到了阿里云上面。 **

**增加supervisor管理，当chrash了，可以自动重启**

**安装后/etc/supervisor/conf.d/ 配置一个文件，如下 简单配置**

command=uwsgi /home/flask/flask_blog-python3/helloflask_uwsgi.ini
autostart=ture
autorestart=true
stdout_logfile=/home/flask/flask_blog-python3/uwsgi_supervisor.log
user=root
配置后启动

service supervisor start

终止服务

service supervisor stop




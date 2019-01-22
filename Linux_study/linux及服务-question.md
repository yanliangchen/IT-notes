### 1.DNS解析过程是怎样的？有几种解析方式？各自的区别是什么？

**转自:http://blog.51cto.com/369369/812889**

**DNS原理及其解析过程**
 **精彩剖析**

​     网络通讯大部分是基于TCP/IP的，而TCP/IP是基于IP地址的，所以计算机在网络上进行通讯时只能识别如“202.96.134.133”之类的IP地址，而不能认识域名。我们无法记住10个以上IP地址的网站，所以我们访问网站时，更多的是在浏览器地址栏中输入域名，就能看到所需要的页面，这是因为有一个叫“DNS服务器”的计算机自动把我们的域名“翻译”成了相应的IP地址，然后调出IP地址所对应的网页。

 

什么是DNS？
     DNS( Domain Name System)是“域名系统”的英文缩写，是一种组织成域层次结构的计算机和网络服务命名系统，它用于TCP/IP网络，它所提供的服务是用来将主机名和域名转换为IP地址的工作。DNS就是这样的一位“翻译官”，它的基本工作原理可用下图来表示。
 [![img](http://blog.51cto.com/attachment/201203/171327624.jpg)](http://blog.51cto.com/attachment/201203/171327624.jpg)

 

DNS域名称
     域名系统作为一个层次结构和分布式数据库，包含各种类型的数据，包括主机名和域名。DNS数据库中的名称形成一个分层树状结构称为域命名空间。域名包含单个标签分隔点，例如：im.qq.com。
 完全限定的域名 (FQDN) 唯一地标识在 DNS 分层树中的主机的位置，通过指定的路径中点分隔从根引用的主机的名称列表。 下图显示与主机称为 im 内 qq.com DNS 树的示例。  主机的 FQDN 是 im.qq.com。
 DNS 域的名称层次结构
 [![img](http://blog.51cto.com/attachment/201203/171354709.jpg)](http://blog.51cto.com/attachment/201203/171354709.jpg)

 

DNS域名称空间的组织方式
     按其功能命名空间中用来描述 DNS 域名称的五个类别的介绍详见下表中，以及与每个名称类型的示例。
 [![img](http://blog.51cto.com/attachment/201203/171409287.jpg)](http://blog.51cto.com/attachment/201203/171409287.jpg)

 

DNS 和 Internet 域
     互联网域名系统由名称注册机构负责维护分配由组织和国家/地区的顶级域在 Internet 上进行管理。 这些域名按照国际标准 3166。 一些很多现有缩写，保留以供组织中，以及两个字母和三个字母的国家/地区使用的缩写使用下表所示。一些常见的DNS域名称如下图：
 [![img](http://blog.51cto.com/attachment/201203/171425985.jpg)](http://blog.51cto.com/attachment/201203/171425985.jpg)

 

资源记录
     DNS 数据库中包含的资源记录 (RR)。 每个 RR 标识数据库中的特定资源。我们在建立DNS服务器时，经常会用到SOA,NS,A之类的记录，在维护DNS服务器时，会用到MX，CNAME记录。 
 常见的RR见下图：
 [![img](http://blog.51cto.com/attachment/201203/171440482.jpg)](http://blog.51cto.com/attachment/201203/171440482.jpg)

 

Dns服务的工作过程
 当 DNS 客户机需要查询程序中使用的名称时，它会查询本地DNS 服务器来解析该名称。客户机发送的每条查询消息都包括3条信息，以指定服务器应回答的问题。
 ● 指定的 DNS 域名，表示为完全合格的域名 (FQDN) 。
 ● 指定的查询类型，它可根据类型指定资源记录，或作为查询操作的专门类型。
 ● DNS域名的指定类别。
     对于DNS 服务器，它始终应指定为 Internet 类别。例如，指定的名称可以是计算机的完全合格的域名，如im.qq.com，并且指定的查询类型用于通过该名称搜索地址资源记录。
     DNS 查询以各种不同的方式进行解析。客户机有时也可通过使用从以前查询获得的缓存信息就地应答查询。DNS 服务器可使用其自身的资源记录信息缓存来应答查询，也可代表请求客户机来查询或联系其他 DNS 服务器，以完全解析该名称，并随后将应答返回至客户机。这个过程称为递归。
     另外，客户机自己也可尝试联系其他的 DNS 服务器来解析名称。如果客户机这么做，它会使用基于服务器应答的独立和附加的查询，该过程称作迭代，即DNS服务器之间的交互查询就是迭代查询。
 DNS 查询的过程如下图所示。
 [![img](http://blog.51cto.com/attachment/201203/175333937.jpg)](http://blog.51cto.com/attachment/201203/175333937.jpg)

 

1、在浏览器中输入www.qq.com域名，操作系统会先检查自己本地的hosts文件是否有这个网址映射关系，如果有，就先调用这个IP地址映射，完成域名解析。 

 

2、如果hosts里没有这个域名的映射，则查找本地DNS解析器缓存，是否有这个网址映射关系，如果有，直接返回，完成域名解析。 

 

3、如果hosts与本地DNS解析器缓存都没有相应的网址映射关系，首先会找TCP/ip参数中设置的首选DNS服务器，在此我们叫它本地DNS服务器，此服务器收到查询时，如果要查询的域名，包含在本地配置区域资源中，则返回解析结果给客户机，完成域名解析，此解析具有权威性。 

 

4、如果要查询的域名，不由本地DNS服务器区域解析，但该服务器已缓存了此网址映射关系，则调用这个IP地址映射，完成域名解析，此解析不具有权威性。 

 

5、如果本地DNS服务器本地区域文件与缓存解析都失效，则根据本地DNS服务器的设置（是否设置转发器）进行查询，如果未用转发模式，本地DNS就把请求发至13台根DNS，根DNS服务器收到请求后会判断这个域名(.com)是谁来授权管理，并会返回一个负责该顶级域名服务器的一个IP。本地DNS服务器收到IP信息后，将会联系负责.com域的这台服务器。这台负责.com域的服务器收到请求后，如果自己无法解析，它就会找一个管理.com域的下一级DNS服务器地址(qq.com)给本地DNS服务器。当本地DNS服务器收到这个地址后，就会找qq.com域服务器，重复上面的动作，进行查询，直至找到www.qq.com主机。 

 

6、如果用的是转发模式，此DNS服务器就会把请求转发至上一级DNS服务器，由上一级服务器进行解析，上一级服务器如果不能解析，或找根DNS或把转请求转至上上级，以此循环。不管是本地DNS服务器用是是转发，还是根提示，最后都是把结果返回给本地DNS服务器，由此DNS服务器再返回给客户机。 
     从客户端到本地DNS服务器是属于递归查询，而DNS服务器之间就是的交互查询就是迭代查询。

 

附录：
 本地DNS配置转发与未配置转发数据包分析
     新建一DNS，具体怎么建我这里就不再描述了，见我的上一篇博文[《在Win2003中安装bind【部署智能DNS】》](http://369369.blog.51cto.com/319630/811179)
 1、DNS服务器不设转发
     在192.168.145.228服务器上安装上wireshark软件，并打开它，设置数据包为UDP过滤，在192.168.145.12客户机上用nslookup命令查询一下www.sohu.com，马上可以看到本地DNS服务器直接查全球13台根域中的某几台，然后一步步解析，通过递代的方式，直到找到www.sohu.com对应的IP为220.181.118.87。
     本地DNS服务器得到www.sohu.com的IP后，它把这个IP返回给192.168.145.12客户机，完成解析。
 [![img](http://blog.51cto.com/attachment/201203/171529219.jpg)](http://blog.51cto.com/attachment/201203/171529219.jpg)

 

2、DNS服务器设置转发
 [![img](http://blog.51cto.com/attachment/201203/171552607.jpg)](http://blog.51cto.com/attachment/201203/171552607.jpg)

 

​    因www.sohu.com域名在第一步的验证中使用过，有缓存，为了不受上步实验干扰，我们在客户机上192.168.145.12上nslookup www.baidu.com。从图上看，本地DNS把请求转发至192.168.133.10服务器，133.10服务器把得到的IP返回给本地DNS，然后本地DNS再把IP告诉DNS客户机，完成解析。
 [![img](http://blog.51cto.com/attachment/201203/171606724.jpg)](http://blog.51cto.com/attachment/201203/171606724.jpg)



### 2.mysql5和mysql6 有什么区别

```
mysql-server-5.5：默认引擎改为Innodb，提高了性能和扩展性，提高实用性（中继日志自动恢复）
mysql-server-5.6：InnoDB性能加强，InnoDB死锁信息可以记录到 error 日志，方便分析，MySQL5.6支持延时复制，可以让slave跟master之间控制一个时间间隔，方便特殊情况下的数据恢复。

```

### 3. nginx用于md5加密的模块是什么

```
nginx_file_md5
```

### 4. lvs通常和什么结合到一起使用

```
LVS只是做一个负载均衡，通过访问VIP来访问后端的网站程序，一旦LVS宕机，整个网站就访问不了，这就出现了单点。所以要结合keepalive这种高可用软件来保证整个网站的高可用
```

### 5. lvs的三种工作模式

```
 LVS只是做一个负载均衡，通过访问VIP来访问后端的网站程序，一旦LVS宕机，整个网站就访问不了，这就出现了单点。所以要结合keepalive这种高可用软件来保证整个网站的高可用
```

### 6.lvs的八种调度算法

```
* 轮叫调度（Round-Robin Scheduling）
* 加权轮叫调度（Weighted Round-Robin Scheduling）
* 最小连接调度（Least-Connection Scheduling）
* 加权最小连接调度（Weighted Least-Connection Scheduling）
* 基于局部性的最少链接（Locality-Based Least Connections Scheduling）
* 带复制的基于局部性最少链接（Locality-Based Least Connections with Replication Scheduling）
* 目标地址散列调度（Destination Hashing Scheduling）
* 源地址散列调度（Source Hashing Scheduling）
* 最短预期延时调度（Shortest Expected Delay Scheduling）
* 不排队调度（Never Queue Scheduling）

在一般的网络服务（如HTTP和Mail Service等）调度中，我会使用加权最小连接调度wlc或者加权轮叫调度wrr算法。
```

### 7.nginx和lvs的区别

**LVS特点：**

​    1.抗负载能力强，使用IP负载均衡技术，只做分发，所以LVS本身并没有多少流量产生；

​    2.稳定性、可靠性好，自身有完美的热备方案；（如：LVS+Keepalived）

​    3.应用范围比较广，可以对所有应用做负载均衡；

​    4.不支持正则处理，不能做动静分离。

**常用四种算法：**

​    1.rr：轮叫，轮流分配到后端服务器；

​    2.wrr：权重轮叫，根据后端服务器负载情况来分配；

​    3.lc：最小连接，分配已建立连接最少的服务器上；

​    4.wlc：权重最小连接，根据后端服务器处理能力来分配。

**Nginx特点：**

​    1.工作在7层，可以对做正则规则处理；（如：针对域名、目录进行分流）

​    2.配置简单，能ping通就能进行负载功能，可以通过端口检测后端服务器状态，不支持url检测；

​    3.抗高并发，采用epoll网络模型处理客户请求；

​    4.只支持HTTP和EMail，应用范围比较少；

​    5.nginx主要是HTTP和反向代理服务器，低系统资源消耗。

**常用四种算法：**

​    1.RR：（默认）轮询，轮流分配到后端服务器；

​    2.weight：根据后端服务器性能分配；

​    3.ip_hash：每个请求按访问ip的hash结果进行分配，并发小时合适，解决session问题；

​    4.fair：（扩展策略），默认不被编译nginx内核，根据后端服务器响应时间判断负载情况，选择最轻的进行处理。

 

lvs优点：

   是三个集群软件中性能和稳定性最高的（但是配置管理却是最复杂的）

   工作在4层传输层，只用来做分发工作，并无流量的产生

   几乎支持所有的应用，如：http，mysql，email等等

   对网络要求很高，若是采用DR方式，最好用同一网段进行通信（LB与后端web）

nginx：

   工作在7层应用层，可以对http应用层实现分流策略（如：根据域名，根据目录结构）

   只支持http和email

   对网络要求不是很高，理论上只要ping的通，就可以正常工作（nginx与后端web）

我建议：

   如果公司的网站比较小，访问人数不是很多，可以采用nginx来做负载均衡

   但是若公司网站规模较大，达到门户级别，建议采用lvs



### 8. http服务器

```
与提供http服务相关的一些配置参数。例如：是否使用keepalive啊，是否使用gzip进行压缩等。

sendfile on
开启高效文件传输模式，sendfile指令指定nginx是否调用sendfile函数来输出文件，减少用户空间到内核空间的上下文切换。对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。

keepalive_timeout 65 : 长连接超时时间，单位是秒，这个参数很敏感，涉及浏览器的种类、后端服务器的超时设置、操作系统的设置，可以另外起一片文章了。长连接请求大量小文件的时候，可以减少重建连接的开销，但假如有大文件上传，65s内没上传完成会导致失败。如果设置时间过长，用户又多，长时间保持连接会占用大量资源。

send_timeout : 用于指定响应客户端的超时时间。这个超时仅限于两个连接活动之间的时间，如果超过这个时间，客户端没有任何活动，Nginx将会关闭连接。

client_max_body_size 10m
允许客户端请求的最大单文件字节数。如果有上传较大文件，请设置它的限制值

client_body_buffer_size 128k
缓冲区代理缓冲用户端请求的最大字节数
模块http_proxy：
这个模块实现的是nginx作为反向代理服务器的功能，包括缓存功能（另见文章）

proxy_connect_timeout 60
nginx跟后端服务器连接超时时间(代理连接超时)
proxy_read_timeout 60
连接成功后，与后端服务器两个成功的响应操作之间超时时间(代理接收超时)

proxy_buffer_size 4k
设置代理服务器（nginx）从后端realserver读取并保存用户头信息的缓冲区大小，默认与proxy_buffers大小相同，其实可以将这个指令值设的小一点

proxy_buffers 4 32k
proxy_buffers缓冲区，nginx针对单个连接缓存来自后端realserver的响应，网页平均在32k以下的话，这样设置

proxy_busy_buffers_size 64k
高负荷下缓冲大小（proxy_buffers*2）

proxy_max_temp_file_size
当 proxy_buffers 放不下后端服务器的响应内容时，会将一部分保存到硬盘的临时文件中，这个值用来设置最大临时文件大小，默认1024M，它与 proxy_cache 没有关系。大于这个值，将从upstream服务器传回。设置为0禁用。

proxy_temp_file_write_size 64k
当缓存被代理的服务器响应到临时文件时，这个选项限制每次写临时文件的大小。proxy_temp_path（可以在编译的时候）指定写到哪那个目录。

proxy_pass，proxy_redirect见 location 部分。

模块http_gzip：

gzip on : 开启gzip压缩输出，减少网络传输。
gzip_min_length 1k ： 设置允许压缩的页面最小字节数，页面字节数从header头得content-length中进行获取。默认值是20。建议设置成大于1k的字节数，小于1k可能会越压越大。
gzip_buffers 4 16k ： 设置系统获取几个单位的缓存用于存储gzip的压缩结果数据流。4 16k代表以16k为单位，安装原始数据大小以16k为单位的4倍申请内存。
gzip_http_version 1.0 ： 用于识别 http 协议的版本，早期的浏览器不支持 Gzip 压缩，用户就会看到乱码，所以为了支持前期版本加上了这个选项，如果你用了 Nginx 的反向代理并期望也启用 Gzip 压缩的话，由于末端通信是 http/1.0，故请设置为 1.0。
gzip_comp_level 6 ： gzip压缩比，1压缩比最小处理速度最快，9压缩比最大但处理速度最慢(传输快但比较消耗cpu)
gzip_types ：匹配mime类型进行压缩，无论是否指定,”text/html”类型总是会被压缩的。
gzip_proxied any ： Nginx作为反向代理的时候启用，决定开启或者关闭后端服务器返回的结果是否压缩，匹配的前提是后端服务器必须要返回包含”Via”的 header头。
gzip_vary on ： 和http头有关系，会在响应头加个 Vary: Accept-Encoding ，可以让前端的缓存服务器缓存经过gzip压缩的页面，例如，用Squid缓存经过Nginx压缩的数据。

```

### 9.apache select 和 nginx epoll模型区别

http://blog.51cto.com/oldboy/1855201
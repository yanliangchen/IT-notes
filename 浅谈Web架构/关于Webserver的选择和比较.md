### Webserver有哪些



常用web服务器有Apache、Nginx、Lighttpd、Tomcat、IBM Websphere等，其中应用最广泛的是Apache。而Windows NT/2000/2003平台下最常用的服务器则是IIS。 
 Apache服务器 
 Apache仍然是世界上用的最多的Web服务器，市场占有率达60%左右；它的优势在开源代码开放，可以运行在几乎所有的Unix、Linux、Windows系统平台上；缺点在于消耗的内存也比其他的web服务器要高。

  

Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行。由俄罗斯的程序设计师Igor Sysoev所开发，供俄国大型的入口网站及搜索引擎Rambler（俄文：Рамблер）使用。其特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：京东、新浪、网易、腾讯、淘宝等。

  

Lighttpd服务器 
 Lighttpd服务器其目标是提供一个专门针对高性能网站，安全、快速、兼容性好并且灵活的Web Server环境。它具有内存开销低、CPU占用率低、效能好，以及模块丰富等特点。 Tomcat服务器

  

Tomcat服务器是一个开放源代码、运行servlet和JSP Web应用软件的基于java的Web应用软件容器。 
 IIS(iis php mysql环境搭建教程)

  

IIS是一种web服务组件，其中包括Web服务器、FTp服务器、NNTP服务器和SMTP服务器，分别用于网页浏览、文件传输、新闻服务和邮件发送等方面，它使得在网络上发送信息成为一件很容易的事。但IIS只能运行在Windows平台、Linux/Unix平台上。

  

------

  

Apache与Nginx的优缺点比较  
 1、nginx相对于apache的优点： 

  

轻量级，同样起web 服务，比apache 占用更少的内存及资源  
 抗并发，nginx 处理请求是异步非阻塞的，而apache 则是阻塞型的，在高并发下nginx 能保持低资源低消耗高性能  
 高度模块化的设计，编写模块相对简单  
 社区活跃，各种高性能模块出品迅速啊  
 apache 相对于nginx 的优点：

  

rewrite ，比nginx 的rewrite 强大 
 模块超多，基本想到的都可以找到  
 少bug ，nginx 的bug 相对较多  
 超稳定  
 存在就是理由，一般来说，需要性能的web 服务，用nginx 。如果不需要性能只求稳定，那就apache 吧。后者的各种功能模块实现得比前者，例如ssl 的模块就比前者好，可配置项多。这里要注意一点，epoll(freebsd 上是 kqueue )网络IO 模型是nginx 处理性能高的根本理由，但并不是所有的情况下都是epoll 大获全胜的，如果本身提供静态服务的就只有寥寥几个文件，apache 的select 模型或许比epoll 更高性能。当然，这只是根据网络IO 模型的原理作的一个假设，真正的应用还是需要实测了再说的。

  

2、作为 Web 服务器：相比 Apache，Nginx 使用更少的资源，支持更多的并发连接，体现更高的效率，这点使 Nginx 尤其受到虚拟主机提供商的欢迎。在高连接并发的情况下，Nginx是Apache服务器不错的替代品: Nginx在美国是做虚拟主机生意的老板们经常选择的软件平台之一. 能够支持高达 50,000 个并发连接数的响应, 感谢Nginx为我们选择了 epoll and kqueue 作为开发模型. 

  

Nginx作为负载均衡服务器: Nginx 既可以在内部直接支持 Rails 和 PHP 程序对外进行服务, 也可以支持作为 HTTP代理 服务器对外进行服务. Nginx采用C进行编写, 不论是系统资源开销还是CPU使用效率都比 Perlbal 要好很多. 

  

作为邮件代理服务器: Nginx 同时也是一个非常优秀的邮件代理服务器（最早开发这个产品的目的之一也是作为邮件代理服务器）, Last.fm 描述了成功并且美妙的使用经验. Nginx 是一个安装非常的简单 , 配置文件非常简洁（还能够支持perl语法）, Bugs 非常少的服务器: Nginx 启动特别容易, 并且几乎可以做到7*24不间断运行，即使运行数个月也不需要重新启动. 你还能够不间断服务的情况下进行软件版本的升级 . 

  

3、Nginx 配置简洁, Apache 复杂 

  

Nginx 静态处理性能比 Apache 高 3倍以上  
 Apache 对 PHP 支持比较简单，Nginx 需要配合其他后端用  
 Apache 的组件比 Nginx 多  
 现在 Nginx 才是 Web 服务器的首选  
 4、最核心的区别在于apache是同步多进程模型，一个连接对应一个进程；nginx是异步的，多个连接（万级别）可以对应一个进程 

  

5、nginx处理静态文件好,耗费内存少.但无疑apache仍然是目前的主流,有很多丰富的特性.所以还需要搭配着来.当然如果能确定nginx就适合需求,那么使用nginx会是更经济的方式.

  

6、从个人过往的使用情况来看，nginx的负载能力比apache高很多。最新的服务器也改用nginx了。而且nginx改完配置能-t测试一下配置有没有问题，apache重启的时候发现配置出错了，会很崩溃，改的时候都会非常小心翼翼现在看有好多集群站，前端nginx抗并发，后端apache集群，配合的也不错。 

  

7、nginx处理动态请求是鸡肋，一般动态请求要apache去做，nginx只适合静态和反向。

  

8、從我個人的經驗來看，nginx是很不錯的前端服務器，負載性能很好，在老奔上開nginx，用webbench模擬10000個靜態文件請求毫不吃力。apache對php等語言的支持很好，此外apache有強大的支持網路，發展時間相對nginx更久，bug少但是apache有先天不支持多核心處理負載雞肋的缺點，建議使用nginx做前端，後端用apache。大型網站建議用nginx自代的集群功能 

  

9、Nginx优于apache的主要两点：1.Nginx本身就是一个反向代理服务器 2.Nginx支持7层负载均衡；其他的当然，Nginx可能会比apache支持更高的并发，但是根据NetCraft的统计，2011年4月的统计数据，Apache依然占有62.71%，而Nginx是7.35%，因此总得来说，Aapche依然是大部分公司的首先，因为其成熟的技术和开发社区已经也是非常不错的性能。

  

10、你对web server的需求决定你的选择。大部分情况下nginx都优于APACHE，比如说静态文件处理、PHP-CGI的支持、反向代理功能、前端Cache、维持连接等等。在Apache+PHP（prefork）模式下，如果PHP处理慢或者前端压力很大的情况下，很容易出现Apache进程数飙升，从而拒绝服务的现象。 

  

11、可以看一下nginx lua模块：[https://github.com/chaoslaw…apache](https://github.com/chaoslaw...apache)比nginx多的模块，可直接用lua实现apache是最流行的，why？大多数人懒得更新到nginx或者学新事物 

  

12、对于nginx，我喜欢它配置文件写的很简洁，正则配置让很多事情变得简单运行效率高，占用资源少，代理功能强大，很适合做前端响应服务器 

  

13、Apache在处理动态有优势，Nginx并发性比较好，CPU内存占用低，如果rewrite频繁，那还是Apache吧

  

------

  

Nginx与lvs的对比优势  
 1，nginx工作在网络的7层，所以它可以针对http应用本身来做分流策略，比如针对域名、目录结构等 ，相比之下lvs并不具备这样的功能 
 2，nginx对网络的依赖较小,理论上只要ping得通，网页访问正常，nginx就能连得通 ，lvs就比较依赖于网络环境

  

3，nginx安装和配置比较简单，测试起来也很方便，因为它基本能把错误用日志打印出来 ，lvs的安装和配置、测试就要花比较长的时间了，lvs对网络依赖比较大，很多时候不能配置成功都是因为网络问题而不是配置问题，出了问题要解决也相应的会麻烦得多 
 4，nginx可以检测到服务器内部的故障 ，比如根据服务器处理网页返回的状态码、超时等等，并且会把返回错误的请求重新提交到另一个节点。目前lvs中ldirectd也能支持针对服务器内部的情况来监控，但lvs的原理使其不能重发请求。重发请求这点，譬如用户正在上传一个文件，而处理该上传的节点刚好在上传过程中出现故障，nginx会把上传切到另一台服务器重新处理 

  

------

  

nginx版本如何选择？  
 注意各版本的区别：Nginx官网提供了三个类型的版本 
 1、Mainline version：Mainline 是 Nginx 目前主力在做的版本，可以说是开发版 
 2、Stable version：最新稳定版，生产环境上建议使用的版本 
 3、Legacy versions：遗留的老版本的稳定版 
 生产环境使用Stable version：最新稳定版，现在最新的版本是nginx-1.9.11开发版本 
# 【Nginx安装】CentOS7安装Nginx及配置



```
   Nginx是一款轻量级的网页服务器、反向代理服务器。相较于Apache、lighttpd具有占有内存少，稳定性高等优势。**它最常的用途是提供反向代理服务。**
```

### 安装

------

```
   在Centos下，yum源不提供nginx的安装，可以通过切换yum源的方法获取安装。也可以通过直接下载安装包的方法，**以下命令均需root权限执行**：
   首先安装必要的库（nginx 中gzip模块需要 zlib 库，rewrite模块需要 pcre 库，ssl 功能需要openssl库）。选定**/usr/local**为安装目录，以下具体版本号根据实际改变。
```

1.安装gcc gcc-c++(如新环境,未安装请先安装)

```
$ yum install -y gcc gcc-c++
```

2.安装PCRE库

```
$ cd /usr/local/
$ wget http://jaist.dl.sourceforge.net/project/pcre/pcre/8.33/pcre-8.33.tar.gz
$ tar -zxvf pcre-8.36.tar.gz
$ cd pcre-8.36
$ ./configure
$ make && make install

如报错:configure: error: You need a C++ compiler for C++ support
解决:yum install -y gcc gcc-c++
```

3.安装SSL库

```
$ cd /usr/local/
$ wget http://www.openssl.org/source/openssl-1.0.1j.tar.gz
$ tar -zxvf openssl-1.0.1j.tar.gz
$ cd openssl-1.0.1j
$ ./config
$ make && make install

4.安装zlib库存
```

$ cd /usr/local/
$ wget [http://zlib.net/zlib-1.2.11.tar.gz](https://link.jianshu.com/?t=http://zlib.net/zlib-1.2.11.tar.gz)
$ tar -zxvf zlib-1.2.11.tar.gz
$ ./configure
$ make && make install

```

```

4.安装nginx

```
$ cd /usr/local/
$ wget http://nginx.org/download/nginx-1.8.0.tar.gz
$ tar -zxvf nginx-1.8.0.tar.gz
$ cd nginx-1.8.0 
$ ./configure --user=nobody --group=nobody --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_gzip_static_module --with-http_realip_module --with-http_sub_module --with-http_ssl_module
(注: --with-http_ssl_module:这个不加后面在nginx.conf配置ssl:on后,启动会报nginx: [emerg] unknown directive "ssl" in /opt/nginx/conf/nginx.conf 异常)
$ make && make install

报错:./configure: error: the HTTP gzip module requires the zlib library
```

在–prefix后面接以下命令:

```
--with-pcre=/usr/local/pcre-8.36 指的是pcre-8.36 的源码路径。--with-zlib=/usr/local/zlib-1.2.8 指的是zlib-1.2.8 的源码路径。
```

[点击此处下载安装脚本](https://link.jianshu.com/?t=http%3A%2F%2F172.16.82.126%2Fnfc%2Fnginx%2Fnginx_install.sh)

5.启动

```
$ /usr/local/nginx/sbin/nginx
```

检查是否启动成功：

打开浏览器访问此机器的 IP，如果浏览器出现 Welcome to nginx! 则表示 Nginx 已经安装并运行成功。

部分命令如下：
重启：

```
$ /usr/local/nginx/sbin/nginx –s reload
```

停止：

```
$ /usr/local/nginx/sbin/nginx –s stop
```

测试配置文件是否正常：

```
 $ /usr/local/nginx/sbin/nginx –t
```

强制关闭：

```
$ pkill nginx
```

### 配置

------

以上安装方法nginx的配置文件位于

> /usr/local/nginx/conf/nginx.conf
> Nginx配置文件常见结构的从外到内依次是「http」「server」「location」等等，缺省的继承关系是从外到内，也就是说内层块会自动获取外层块的值作为缺省值。

# Server

接收请求的服务器需要将不同的请求按规则转发到不同的后端服务器上，在 nginx 中我们可以通过构建虚拟主机（server）的概念来将这些不同的服务配置隔离。

> server {
> listen 80;
> server_name localhost;
> root html;
> index index.html index.htm;
> }

例如我们笔戈玩下的两个子项目 passport 和 wan 就可以通过在 nginx 的配置文件中配置两个 server，servername 分别为 passport.bigertech.com 和 wan.bigertech.com。这样的话不同的 url 请求就会对应到 nginx 相应的设置，转发到不同的后端服务器上。
这里的 **listen** 指监听端口，**server_name** 用来指定IP或域名，多个域名对应统一规则可以空格分开，**index** 用于设定访问的默认首页地址，**root** 指令用于指定虚拟主机的网页跟目录，这个地方可以是相对地址也可以是绝对地址。
通常情况下我们可以在 nginx.conf 中配置多个server，对不同的请求进行设置。就像这样：

> server {
> listen 80;
> server_name host1;
> root html;
> index index.html
> index.htm;
> }
> server {
> listen 80;
> server_name host2;
> root /data/www/html;
> index index.html index.htm;
> }

但是当 server 超过2个时，建议将不同对虚拟主机的配置放在另一个文件中，然后通过在主配置文件 nginx.conf 加上 include 指令包含进来。更便于管理。

> include vhosts/*.conf;

就可以把vhosts的文件都包含进去啦。

Localtion
每个 url 请求都会对应的一个服务，nginx 进行处理转发或者是本地的一个文件路径，或者是其他服务器的一个服务路径。而这个路径的匹配是通过 location 来进行的。我们可以将 server 当做对应一个域名进行的配置，而 location 是在一个域名下对更精细的路径进行配置。

以上面的例子，可以将root和index指令放到一个location中，那么只有在匹配到这个location时才会访问root后的内容：

> location / {

```
   root /data/www/host2; 
   index index.html index.htm; 
```

}

location 匹配规则

> ~ 波浪线表示执行一个正则匹配，区分大小写
> ~* 表示执行一个正则匹配，不区分大小写
> ^~ ^~表示普通字符匹配，如果该选项匹配，只匹配该选项，不匹配别的选项，一般用来匹配目录
> = 进行普通字符精确匹配

匹配例子：

静态文件映射
访问文件的配置主要有 **root 和 alias**p’s 两个指令。这两个指令的区别容易弄混：
alias
alias后跟的指定目录是准确的，并且末尾必须加 /。

> location /c/ {
> alias /a/;
> }

root
root后跟的指定目录是上级目录，并且该上级目录下要含有和location后指定名称的同名目录才行。

> location /c/ {
> root /a/;
> }

如果你需要将这个目录展开，在这个location的末尾加上「autoindex on; 」就可以了

转发
配置起来很简单比如我要将所有的请求到转移到真正提供服务的一台机器的 8001 端口，只要这样：

> location / {
> proxy_pass 172.16.1.1:8001;
> }

这样访问host时，就都被转发到 172.16.1.1的8001端口去了。

负载均衡

> upstream myserver; {
> ip_hash;
> server 172.16.1.1:8001;
> server 172.16.1.2:8002;
> server 172.16.1.3;
> server 172.16.1.4;
> }
> location / {
> proxy_pass [http://myserver](https://link.jianshu.com/?t=http%3A%2F%2Fmyserver);
> }

我们在 upstream 中指定了一组机器，并将这个组命名为 myserver，这样在 proxypass 中只要将请求转移到 myserver 这个 upstream 中我们就实现了在四台机器的反向代理加负载均衡。其中的 ip_hash 指明了我们均衡的方式是按照用户的 ip 地址进行分配。另外还有轮询、指定权重轮询、fair、url_hash几种调度算法。

#### 总结

以上是最简单的通过 nginx 实现静态文件转发、反向代理和负载均衡的配置。在 nginx 中所有的功能都是通过模块来实现的，比如当我们配置 upstream 时是用 upstream 模块，而 server 和 location 是在 http core 模块，其他的还有流控的 limt 模块，邮件的 mail 模块，https 的 ssl 模块。他们的配置都是类似的可以再 nginx 的[模块文档](https://link.jianshu.com/?t=http%3A%2F%2Fwiki.nginx.org%2FModules)中找到详细的配置说明。

 
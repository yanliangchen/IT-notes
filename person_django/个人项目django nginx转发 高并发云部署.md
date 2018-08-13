# Centos + nginx + Django + uwsgi 部署Web服务解决高并发 

### 1. 这么搭建的作用  

### uwsgi

  

与WSGI一样，是uWSGI服务器的独占通信协议，用于定义传输信息的类型(type of information)。每一个uwsgi packet前4byte为传输信息类型的描述，与WSGI协议是两种东西，据说该协议是fcgi协议的10倍快。

​    

### Nginx

  

Nginx是一个Web服务器其中的HTTP服务器功能和uWSGI功能很类似，但是Nginx还可以用作更多用途，比如最常用的反向代理功能。

​    

### Django

  

Django是一个Web框架，框架的作用在于处理request和 reponse，其他的不是框架所关心的内容。所以如何部署Django不是Django所需要关心的。 

  

Django所提供的是一个开发服务器，这个开发服务器，没有经过安全测试，而且使用的是Python自带的simple HTTPServer 创建的，在安全性和效率上都是不行的。 



ps :为了解决高并发，因为django自带的web服务器效率上不行。

### 2. 前期环境准备

#### 2.1 centos（云主机7.2）

```
$ cat /etc/redhat-release
CentOS Linux release 7.2.1511 (Core) 
```



#### 2.2 nginx 安装



##### 安装所需环境

Nginx 是 C语言 开发，建议在 Linux 上运行，当然，也可以安装 Windows 版本，本篇则使用 [CentOS](https://www.linuxidc.com/topicnews.aspx?tid=14) 7 作为安装环境。

###### **一. gcc 安装**

安装 nginx 需要先将官网下载的源码进行编译，编译依赖 gcc 环境，如果没有 gcc 环境，则需要安装：

```
yum install gcc-c++
```

###### **二. PCRE pcre-devel 安装**

PCRE(Perl Compatible Regular Expressions) 是一个Perl库，包括 perl 兼容的正则表达式库。nginx 的 http 模块使用 pcre 来解析正则表达式，所以需要在 linux 上安装 pcre 库，pcre-devel 是使用 pcre 开发的一个二次开发库。nginx也需要此库。命令：

```
yum install -y pcre pcre-devel
```

###### **三. zlib 安装**

zlib 库提供了很多种压缩和解压缩的方式， nginx 使用 zlib 对 http 包的内容进行 gzip ，所以需要在 Centos 上安装 zlib 库。

```
yum install -y zlib zlib-devel
```

###### **四. OpenSSL 安装**

OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及 SSL 协议，并提供丰富的应用程序供测试或其它目的使用。
nginx 不仅支持 http 协议，还支持 https（即在ssl协议上传输http），所以需要在 Centos 安装 OpenSSL 库。

```
yum install -y openssl openssl-devel
```

##### 官网下载

1.直接下载`.tar.gz`安装包，地址：<https://nginx.org/en/download.html>

![nginx.png](https://www.linuxidc.com/upload/2016_09/160905180451092.png)

2.使用`wget`命令下载（推荐）。

```
wget -c https://nginx.org/download/nginx-1.10.1.tar.gz
```

![nginx-wget.png](https://www.linuxidc.com/upload/2016_09/160905180451091.png)

我下载的是1.10.1版本，这个是目前的稳定版。

##### 解压

依然是直接命令：

```
tar -zxvf nginx-1.10.1.tar.gz
cd nginx-1.10.1
```

##### 配置

其实在 nginx-1.10.1 版本中你就不需要去配置相关东西，默认就可以了。当然，如果你要自己配置目录也是可以的。
1.使用默认配置

```
./configure
```

2.自定义配置（不推荐）

```
./configure \
--prefix=/usr/local/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--pid-path=/usr/local/nginx/conf/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--http-client-body-temp-path=/var/temp/nginx/client \
--http-proxy-temp-path=/var/temp/nginx/proxy \
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \
--http-scgi-temp-path=/var/temp/nginx/scgi
```

> 注：将临时文件目录指定为/var/temp/nginx，需要在/var下创建temp及nginx目录

##### 编译安装

```
make
make install
```

查找安装路径：

```
whereis nginx
```

![nginx-whereis.png](https://www.linuxidc.com/upload/2016_09/160905180451094.png)

##### 启动、停止nginx

```
cd /usr/local/nginx/sbin/
./nginx 
./nginx -s stop
./nginx -s quit
./nginx -s reload
```

> `./nginx -s quit`:此方式停止步骤是待nginx进程处理任务完毕进行停止。
> `./nginx -s stop`:此方式相当于先查出nginx进程id再使用kill命令强制杀掉进程。

查询nginx进程：

```
ps aux|grep nginx
```

##### 重启 nginx

1.先停止再启动（推荐）：
对 nginx 进行重启相当于先停止再启动，即先执行停止命令再执行启动命令。如下：

```
./nginx -s quit
./nginx
```

2.重新加载配置文件：
当 ngin x的配置文件 nginx.conf 修改后，要想让配置生效需要重启 nginx，使用`-s reload`不用先停止 ngin x再启动 nginx 即可将配置信息在 nginx 中生效，如下：
./nginx -s reload

启动成功后，在浏览器可以看到这样的页面：

![nginx-welcome.png](https://www.linuxidc.com/upload/2016_09/160905180451093.png)

##### 开机自启动

即在`rc.local`增加启动代码就可以了。

```
vi /etc/rc.local
```

增加一行 `/usr/local/nginx/sbin/nginx`
设置执行权限：

```
chmod 755 rc.local
```

![nginx-rclocal.png](https://www.linuxidc.com/upload/2016_09/160905180451095.png)

到这里，nginx就安装完毕了，启动、停止、重启操作也都完成了，当然，你也可以添加为系统服务，我这里就不在演示了。







#### 2.3 Python3.5安装

```
安装Python3.5 
不要删除自带的python2.7，否则会出问题，因为centos许多软件需要依赖系统自带python
安装依赖工具 yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
下载 wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
解压 tar -zxvf Python-3.5.1.tgz
移动至规范的放软件的目录下 mv Python-3.5.1 /usr/local
安装：
cd /usr/local/Python-3.5.1/
make & make install
更新python的软连接：
rm -rf /usr/bin/python
ln -s /usr/local/bin/python3.5 /usr/bin/python
验证
python -V

这里需要注意的是安装完python3  会发现yum不好用了  是因为版本升级的原因
yum里面指明python环境用python2来解析  
vim /usr/bin/yum
试一下 结果发现还报错 给改成 python
vim /usr/libexec/urlgrabber-ext-down 

```



```
#上面安装python 我记得这里有个坑 编译的时候  也记录了下来 到时候看吧
make: *** No targets specified and no makefile found. Stop.解决方法
2015年09月24日 14:34:03
阅读数：33445 
转载请注明出处:http://blog.csdn.net/l1028386804/article/details/48710993
1、wget http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.6.tar.gz
2.、tar zxvf ncurses-5.6.tar.gz
3、 ./configure -prefix=/usr/local -with-shared-without-debug
4、make
5、make install
```



#### 2.4 Django2.1安装

```3
#检查是否有pip 先给pip做一个软链  
$ ln -s /usr/local/bin/python3.5 /usr/bin/python
#之后 升级pip (18版本)
$ pip install --upgrade  pip 
#之后安装django （这里是2.1版本的django）
$ pip install  django 
```



##### 2.4.1 Django代码部署

```
1. 先把测试环境的windows 代码项目打包成zip压缩包
2. 之后上传到服务器 用rz 或者 sz 
3. 解压到 django的目录下 之后测试  看能否run起来
4. 此时因为数据库的原因，需要再centos上安装mysql，github上我参考别人记录了下来 直接按操作来就好了
5. 配置django的setting了就是
```



#### 2.5 安装uwsgi

```
安装 pip install uwsgi 
验证 test.py 文件随便放
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello Django"]
uwsgi --http :8001 --wsgi-file test.py
```



### 2.3 环境准备好,开始配置

#### 2.3.1 nginx的配置文件

//nginx的配置文件

```
 //加一个server 它自带的server你不用动  再底下加一个就好了
 //需要注意的是这下面的server_name是ifconfig内网里的ip
 server {
    listen 80; #暴露给外部访问的端口
    server_name www.yanliangchen.top 172.33.0.6;
    charset utf-8;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:9000; #外部访问8996就转发到内部8997
    }
    location /static/ {
        alias /usr/local/lib/python3.5/site-packages/django/bin/yun1/static; #项目静态路径设置
    }
}

```

//重新加载nginx 

```
../sbin/nginx -s reload	
```



#### 2.3.2 uwsgi的配置

```
[root@i-a907f513 yun1]# ls
manage.py  myadmin  myhome  nohup.out  static  templates  ueditor  uwsgi.log  yun1  yun1.xml
[root@i-a907f513 yun1]# cat yun1.xml 
<uwsgi>
    <socket>127.0.0.1:9000</socket><!-- 内部端口，自定义 -->
        <chdir>/usr/local/lib/python3.5/site-packages/django/bin/yun1</chdir><!-- 项目路径 -->
            <module>yun1.wsgi</module>
                <processes>4</processes> <!-- 进程数 --> 
    <daemonize>uwsgi.log</daemonize><!-- 日志文件 -->
</uwsgi>

```

//配置django uwsgi 给这个文件载入进去 

```
$ uwsgi -x yun1.xml
```

//执行 service nginx restart 或者 start 

```
重启nginx 
然后访问你的nginx对外服务的 域名：80 就到了你看到了你的django项目了！！！
```


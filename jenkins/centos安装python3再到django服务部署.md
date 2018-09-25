参考:https://www.cnblogs.com/FZfangzheng/p/7588944.html

### **1. Centos7.2安装Python3,pip等的方法**		

由于centos7原本就安装了Python2，而且这个Python2不能被删除，因为有很多系统命令，比如yum都要用到。

```
[root@VM_105_217_centos Python-3.6.2]# python
Python 2.7.5 (default, Aug  4 2017, 00:39:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
```

输入Python命令，查看可以得知是Python2.7.5版本

输入

```
which python
```

可以查看位置，一般是位于/usr/bin/python目录下。

下面介绍安装Python3的方法

首先安装依赖包

```
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

然后根据自己需求下载不同版本的Python3，我下载的是Python3.6.2

```
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
```

如果速度不够快，可以直接去官网下载，利用WinSCP等软件传到服务器上指定位置，我的存放目录是/usr/local/python3，使用命令：

```
mkdir /usr/local/python3 
```

建立一个空文件夹

然后解压压缩包，进入该目录，安装Python3

```
tar -xvJf  Python-3.6.2.tar.xz
cd Python-3.6.2
./configure --prefix=/usr/local/python3
make && make install
```

最后创建软链接

#这里需要注入的是如果出现报错软连接存在的话 

#则需要把之前的python软连接进行移除

```
 mv /usr/bin/python /usr/bin/python_old
```

```
ln -s /usr/local/python3/bin/python3 /usr/bin/python
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

在命令行中输入python3测试:

成功！

#之后因为升级了python所以yum安装报错

- 新版的python安装好后要修改python的系统默认指向问题
- 升级到最新版python后yum报错的问题

http://www.mamicode.com/info-detail-1454043.html

```
$vim /usr/bin/yum
$vim  /usr/libexec/urlgrabber-ext-down
改成2.7 也就是说大的系统环境是3 yum用的2.7的python环境
#!/usr/bin/python2.7
```



**之后升级下pip再安装服务**

```
#系统python3下的环境 来升级pip 
$python -m pip install --upgrade pip   （因为这个是之前安装的pip3）

#之后改变一下pip3给它做个pip的软连接  就可以直接输入pip了
```



### **2.安装django服务**

https://www.cnblogs.com/freeweb/p/5210167.html

**遇到的问题:**

.服务起在本地了直接python manage.py  runserver的话 默认起在了本地8000端口

```
$ python  manage.py  runserver  
```

2 .解决这个问题的方法是给它改成0.0.0.0段，之后任何网段都能访问到你的服务

```
$ python  manage.py  runserver  0.0.0.0:8000
```

3. 外网访问公网ip 之后（出现页面)
4. 检查端口是否放行，防火墙是否被关掉

```
#中间那个需要改成disable（关闭防火墙) 
$vim /etc/selinux/config
```

5. 写django 测试代码

   参考：https://blog.csdn.net/GitChat/article/details/78271099

### 3. yum安装过程中出现问题

**yum去安装net-tools的时候yum报错的时候需要指定yum的python的老版本**

**参考 http://www.bigtspace.com/227.html 解决的**

```
$cd /usr/bin
$ls -ll python* 
lrwxrwxrwx  1 root root   16 Jul 17 04:07 python -> /usr/bin/python3
lrwxrwxrwx. 1 root root    9 May 10 12:32 python2 -> python2.7
-rwxr-xr-x. 1 root root 7136 Nov 20  2015 python2.7
lrwxrwxrwx  1 root root   30 Jul 17 04:05 python3 -> /usr/local/python3/bin/python3
lrwxrwxrwx. 1 root root    7 May 10 12:32 python_old -> python2

之后来修改yum配置文件,给yum文件指向python的老版本 python_old
$vim /usr/bin/yum
#!/usr/bin/python_old
```





### 4. 之后回到jenkins服务页面配置git等

https://blog.csdn.net/a877415861/article/details/74544086



### 5.之后通过之前openssh配置执行execshell

1.去把代码推到git上

2.用jenkins 去执行 execshell脚本(克隆下来代码命令等cd位置的目录的命令运行服务的命令)


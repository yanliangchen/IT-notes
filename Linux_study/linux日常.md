**1.  windows 下查看python环境安装位置 : where python**

**2.  python 指定环境下安装工具包 C:\Users\liyanliang\AppData\Local\Programs\Python\Python35\python.exe -m pip install fabric3**

linux下			      		             源文件路径        待修改的文件路径

**3. 命令修改配置文件路径  sed -i 's/\/var\/www\/html/\/root\/test/g' /etc/httpd/conf/httpd.conf  **

**4. 起一个http服务 ：  **

​		yum list | grep httpd

​		yum -y install httpd

​		启动服务 没写暂时

**5. 编写一个html  echo  "hello" > /root/test/abc.html**

**vim 编辑器  vim  文件之后 :q退出  ，:q! 强制退出  :wq保存并退出 :wq!保存强制退出**

 **6 .ssh链接远程主机 ： ssh  用户名@主机地址**

​     **如果修改了远程端口： ssh -p 10888 root@域名/ip **

**7. 系统境变量 : etc下profile(系统用户环境变量，往这里加) **

**8.家环境变量: vim ~/.profile **

**9.命令干掉死掉的程序: sudo killall filebox ** 

**10.远程上传下载文件: 先安装 apt-get install  lrzsz**

​			**上传: rz **

​			**下载: sz 根路径**

**11. http://www.bih.cn  www为二级域名 bih为主域名 **

**12 .netstat -lnp :看服务起来没起来，里面有进程id和启动的服务还有端口**

**13. 也可以telnet ip port : 检测主机端口有没有链接上，如果没有连接上，就需要把主机和端口进行放行**				

**14 .重启进程之后里面的数据就没了 (这里重启进程用kill -9  pid进程id)**

**15 .这里记几个端口号：**

​	**端口总共是 ：0~65535**

​			       **HTTPS :443**

​				**HTTP :80**

​				**telnet :23 **

​				**ssh ：22**

**16.关于环境变量**

**只对当前的shell 起作用的环境变量**

**1、**控制台中设置，不赞成这种方式，因为他只对当前的shell 起作用，换一个shell设置就无效了：

直接控制台中输入 ： $PATH="$PATH":/NEW_PATH  (关闭shell Path会还原为原来的path)

**对所有的用户的都起作用的环境变量**

**2、**修改 /etc/profile 文件，如果你的计算机仅仅作为开发使用时推存使用这种方法，因为所有用户的shell都有权使用这个环境变量，可能会给系统带来安全性问题。这里是针对所有的用户的，所有的shell

vi /etc/profile

在/etc/profile的最下面添加：  export  PATH="$PATH:/NEW_PATH"

**针对当前特定的用户起作用的环境变量**

**3、**修改bashrc文件，这种方法更为安全，它可以把使用这些环境变量的权限控制到用户级别，这里是针对某一特定的用户，如果你需要给某个用户权限使用这些环境变量，你只需要修改其个人用户主目录下的 .bashrc文件就可以了。

vi ~/.bashrc

在下面添加：

Export  PATH="$PATH:/NEW_PATH"



**17. 软连接和硬链接的作用**

**硬链接和软链接的区别和作用**

****来源网络 发布时间：2017-11-02 11:23:36 此页面信息为商业广告

1.原理上：

硬链接(hard link)：文件A是文件B的硬链接，则A的目录项中的inode节点号与B的目录项中的inode节点号相同，即一个inode节点对应两个不同的文件名，两个文件名指向同一个文件，A和B对文件系统来说是完全平等的。如果删除了其中一个，对另外一个没有影响。每增加一个文件名，inode节点上的链接数增加一，每删除一个对应的文件名，inode节点上的链接数减一，直到为0，inode节点和对应的数据块被回收。注：文件和文件名是不同的东西，rm A删除的只是A这个文件名，而A对应的数据块（文件）只有在inode节点链接数减少为0的时候才会被系统回收。

软链接(soft link)：A是B的软链接（A和B都是文件名），A的目录项中的inode节点号与B的目录项中的inode节点号不相同，A和B指向的是两个不同的inode，继而指向两块不同的数据块。但是A的数据块中存放的只是B的路径名（可以根据这个找到B的目录项）。A和B之间是“主从”关系，如果B被删除了，A仍然存在（因为两个是不同的文件），但指向的是一个无效的链接。

2.使用限制上：

```
硬链接：
```

a：不能对目录创建硬链接，原因有几种，*重要的是：文件系统不能存在链接环（目录创建时的”..”除外，这个系统可以识别出来）,存在环的后果会导致例如文件遍历等操作的混乱(du，pwd等命令的运作原理就是基于文件硬链接，顺便一提，ls -l结果的第二列也是文件的硬链接数，即inode节点的链接数)

b：不能对不同的文件系统创建硬链接,即两个文件名要在相同的文件系统下。

c：不能对不存在的文件创建硬链接，由原理即可知原因。

```
软链接：
```

a.可以对目录创建软链接，遍历操作会忽略目录的软链接。

b:可以跨文件系统

c:可以对不存在的文件创建软链接，因为放的只是一个字符串，至于这个字符串是不是对于一个实际的文件，就是另外一回事了

3.命令

```
硬链接：ln 源文件名 链接名
```

```
软链接：ln -s 源文件名 链接名
```

**硬链接作用**

```
硬链接：
```

硬连接的作用是允许一个文件拥有多个有效路径名，这样用户就可以建立硬连接到重要文件，以防止“误删”的功能。只删除一个连接并不影响节点本身和其它的连接，只有当*一个连接被删除后，文件的数据块及目录的连接才会被释放。也就是说，文件真正删除的条件是与之相关的所有硬连接文件均被删除。



**18 ./configure --prefix 命令的意思**

```
源码的安装一般由3个步骤组成：配置(configure)、编译(make)、安装(make install)。

Configure是一个可执行脚本，它有很多选项，在待安装的源码路径下使用命令./configure –help输出详细的选项列表。

其中--prefix选项是配置安装的路径，如果不配置该选项，安装后可执行文件默认放在/usr /local/bin，库文件默认放在/usr/local/lib，配置文件默认放在/usr/local/etc，其它的资源文件放在/usr /local/share，比较凌乱。

如果配置--prefix，如：


./configure --prefix=/usr/local/test
可以把所有资源文件放在/usr/local/test的路径中，不会杂乱。
用了—prefix选项的另一个好处是卸载软件或移植软件。当某个安装的软件不再需要时，只须简单的删除该安装目录，就可以把软件卸载得干干净净；移植软件只需拷贝整个目录到另外一个机器即可（相同的操作系统）。

当然要卸载程序，也可以在原来的make目录下用一次make uninstall，但前提是make文件指定过uninstall。
```



**19. yum update -y  更新系统**



**20. yum  install  -y python2-pip  安装pip（新系统） **



**21 .连接完xshell 连接完xftp 直接按Ctrl+Alt+F  进行远程上传  **



**22.环境变量相关 **

```
/etc/profile:此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.
并从/etc/profile.d目录的配置文件中搜集shell的设置.
/etc/bashrc:为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.
~/.bash_profile:每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该
文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.
```



 **23 .linux下登录日志在下面的目录里 ：**

  cd /var/log  查看ssh用户的登录日志：  less secure  linux日志管理： 



**24. Linux下的常用性能查询命令top、vmstat、gprof、pidstat之对比**

（1）查看各个CPU核的使用情况
sudo top -d 1
进入之后，按1，会出现下面的CPU使用情况，其中us列反映了各个CPU核的使用情况，百分比大说明该核在进行紧张的任务。


（2）查看哪个进程在哪个CPU核上运行
sudo top -d 1
进入之后，依次按f、j和空格，会出现如下（其中P列指示的是该进程最近使用的CPU核，如进程mencoder的P列为7，则表示mencoder最近在核7上运行，对于多线程甚至单线程的进程，在不同时刻会使用不同的CPU Core）：

（3）vmstat查看整体的CPU使用情况
sudo vmstat 2 3
参数2表示每个2秒显示一下结果，3表示显示结果的数目。

cs列表示每秒上下文切换次数，us表示用户CPU时间。

（4）Intel工具powertop
sudo powertop
会显示各个CPU核的使用百分比。

（5）gprof分析一个程序
假设程序源文件为speedup-example.cpp
gcc speedup-example.cpp -o speedup-example -pg（注意-pg）
执行程序./speedup-example，会在当前目录生成gmon.out，这个文件是我们查看程序运行情况的来源，接下来用gprof命令查看它：
gprof -b speedup-example gmon.out > Results.txt
这样这个程序的运行信息就在Results.txt中了。


（6）pidstat实时查看一个进程的CPU使用情况及上下文切换情况
首先安装
sudo apt-get install sysstat
接下来使用pidstat（下面的-p是与进程号连用，用于显示特定进程的性能信息，之后还可以指定每隔几秒显示，一共显示几条）：

pidstat 5 -p 15488（你要追踪的进程的pid）
这样就能实时显示15488进程的CPU使用情况：



pidstat -w —— 显示每个进程的上下文切换情况pidstat -w -p 15488 2 —— 每隔2秒显示15488进程的上下文切换情况：


cswch/s —— 每秒该进程产生的voluntary context switches总数。voluntary context switches出现在访问一个已经被占用的资源，从而不得不挂起（即我们通常说的Synchronization Context Switches）

nvcswch/s —— 每秒该进程产生的involuntary context switches总数。involuntary  context switches发生在自己的时间片用完或被更高的优先级抢占（包含Preemption Context Switches）




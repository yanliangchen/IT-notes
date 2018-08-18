### 1.编程脚本目录习惯



```

README (1)目录说明

    --bin/
        bin存放项目的一些可执行文件，
        当然你可以起名script/之类的也行，但bin/更直观。易懂
       --bin/start.py
            写启动程序
    
    --core/
        存放项目的所有源代码(核心代码）。
        (1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。
        (2) 其子目录tests/存放单元测试代码；
        (3) 程序的入口最好命名为main.py。
       --core/test_main.py
         存放核心逻辑

    --conf/
        配置文件
       --setting.py
            写上相关配置
    
    --db/
        数据库文件
        --db.json
            写数据文件
    
    --docs/
        存放一些文档

    --lib/
        库文件,放自定义模块和包
        --common.py
            放常用的功能
    
    --log/
        日志文件
        --access.log
            写上日志

    (2)项目说明

注:运行程序时,在bin目录下执行start.py代码,不可以直接执行core下的模块.

```



### 2. linux下的目录及含义

- **/bin**：
  bin是Binary的缩写, 这个目录存放着最经常使用的命令。

- **/boot：**
  这里存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。

- **/dev ：**
  dev是Device(设备)的缩写, 该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。

- **/etc：**
  这个目录用来存放所有的系统管理所需要的配置文件和子目录。

- **/home**：
  用户的主目录，在Linux中，每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。

- **/lib**：
  这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。

- **/lost+found**：
  这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。

- **/media**：
  linux系统会自动识别一些设备，例如U盘、光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。

- **/mnt**：
  系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

- **/opt**：
   这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。

- **/proc**：
  这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息。
  这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件，比如可以通过下面的命令来屏蔽主机的ping命令，使别人无法ping你的机器：

  ```
  echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
  ```

- **/root**：
  该目录为系统管理员，也称作超级权限者的用户主目录。

- **/sbin**：
  s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。

- **/selinux**：
   这个目录是Redhat/CentOS所特有的目录，Selinux是一个安全机制，类似于windows的防火墙，但是这套机制比较复杂，这个目录就是存放selinux相关的文件的。

- **/srv**：
   该目录存放一些服务启动之后需要提取的数据。

- **/sys**：
   这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。

  sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。

  ​

  该文件系统是内核设备树的一个直观反映。

  当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。

- **/tmp**：
  这个目录是用来存放一些临时文件的。

- **/usr**：
   这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。

- **/usr/bin：**
  系统用户使用的应用程序。

- **/usr/sbin：**
  超级用户使用的比较高级的管理程序和系统守护程序。

- **/usr/src：**内核源代码默认的放置目录。

- **/var**：
  这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

在linux系统中，有几个目录是比较重要的，平时需要注意不要误删除或者随意更改内部文件。

/etc： 上边也提到了，这个是系统中的配置文件，如果你更改了该目录下的某个文件可能会导致系统不能启动。

/bin, /sbin, /usr/bin, /usr/sbin: 这是系统预设的执行文件的放置目录，比如 ls 就是在/bin/ls 目录下的。

值得提出的是，/bin, /usr/bin 是给系统用户使用的指令（除root外的通用户），而/sbin, /usr/sbin 则是给root使用的指令。

/var： 这是一个非常重要的目录，系统上跑了很多程序，那么每个程序都会有相应的日志产生，而这些日志就被记录到这个目录下，具体在/var/log 目录下，另外mail的预设放置也是在这里。





###  3. linux 相关操作

 **1 .ls -l**

​	[ r ]代表可读(read)、[ w ]代表可写(write)、[ x ]代表可执行(execute)



**2 .touch test1**

​	创建 test1 文件 



3 .o 就是owner所属主  ,g就是group所属组, others就是其他的用户

​	第一种: **chmod  u=rwx,g=rx,o=r  test1**    也可以写成  **chmod   u+r ,g+r,o+r**

​	第二种: rwx = 4+2+1 = 7

​			**chomod   777  ./basrc**

​	 	 修改test1 的权限

**4.ls -al test1 **

​	查看test1 文件的权限



**5. cd ~**

​	表示回到自己的家目录 

**6.创建一个带权限的文件或者文件夹**

​	**mkdir  -m  711  test2**



**7. linux下压缩和解压缩**

```
压缩

tar -cvf jpg.tar *.jpg //将目录里所有jpg文件打包成tar.jpg 

tar -czf jpg.tar.gz *.jpg   //将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz

 tar -cjf jpg.tar.bz2 *.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用bzip2压缩，生成一个bzip2压缩过的包，命名为jpg.tar.bz2

tar -cZf jpg.tar.Z *.jpg   //将目录里所有jpg文件打包成jpg.tar后，并且将其用compress压缩，生成一个umcompress压缩过的包，命名为jpg.tar.Z

rar a jpg.rar *.jpg //rar格式的压缩，需要先下载rar for linux

zip jpg.zip *.jpg //zip格式的压缩，需要先下载zip for linux

解压

tar -xvf file.tar //解压 tar包

tar -xzvf file.tar.gz //解压tar.gz

tar -xjvf file.tar.bz2   //解压 tar.bz2

tar -xZvf file.tar.Z   //解压tar.Z

unrar e file.rar //解压rar

unzip file.zip //解压zip


```



**8. ln -s   源文件目录  新命名目录  ** 其实根创建一个快捷方式一样

### 4. Linux 文件内容查看

Linux系统中使用以下命令来查看文件的内容：

- cat  由第一行开始显示文件内容
- tac  从最后一行开始显示，可以看出 tac 是 cat 的倒著写！
- nl   显示的时候，顺道输出行号！  **nl 文件名**
- more 一页一页的显示文件内容  **more  文件名    之后空格翻页**
- less 与 more 类似，但是比 more 更好的是，他可以往前翻页！
- head 只看头几行   **head -n  文件名**
- tail 只看尾巴几行   **tail -n 文件名**







### 5.添加个用户  删除用户等操作

1、建用户：

adduser phpq                             //新建phpq用户
passwd phpq                               //给phpq用户设置密码

 

2、建工作组
groupadd test                          //新建test工作组

 

3、新建用户同时增加工作组
useradd -g test phpq                      //新建phpq用户并增加到test工作组

 

注：：-g 所属组 -d 家目录 -s 所用的SHELL



4、给已有的用户增加工作组
usermod -G groupname username

 

或者：gpasswd -a user group



6、永久性删除用户账号 userdel peter




### 6. yum 常用命令

- 1.列出所有可更新的软件清单命令：yum check-update
- 2.更新所有软件命令：yum update
- 3.仅安装指定的软件命令：yum install <package_name>
- 4.仅更新指定的软件命令：yum update <package_name>
- 5.列出所有可安裝的软件清单命令：yum list
- 6.删除软件包命令：yum remove <package_name>
- 7.查找软件包 命令：yum search <keyword>
- 8.清除缓存命令:
  - yum clean packages: 清除缓存目录下的软件包
  - yum clean headers: 清除缓存目录下的 headers
  - yum clean oldheaders: 清除缓存目录下旧的 headers
  - yum clean, yum clean all (= yum clean packages; yum clean oldheaders) :清除缓存目录下的软件包及旧的headers




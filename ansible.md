# Ansible

ansible官方文档 **http://docs.ansible.com/ansible/latest/index.html**

## 关于Ansible

Ansible是一款IT自动化工具。它可以配置系统，部署软件并编排更高级的IT任务，例如连续部署或零停机滚动更新。

Ansible的主要目标是简单易用。它还非常注重安全性和可靠性，具有最少的移动部件，使用OpenSSH进行传输（其他传输和拉模式作为替代方案），以及围绕人类可审计性设计的语言，即使那些不熟悉该程序。

我们相信简单性与各种规模的环境相关，因此我们为各种类型的繁忙用户进行设计：开发人员，系统管理员，发布工程师，IT经理以及其他人员。Ansible适用于管理所有环境，从少数几个实例的小型设置到数千个实例的企业环境。

Ansible以无代理方式管理机器。永远不会有如何升级远程守护进程或由于守护进程被卸载而无法管理系统的问题。由于OpenSSH是同行评审最多的开源组件之一，安全风险大大降低。Ansible是分散的，它依赖于您现有的操作系统凭据来控制对远程机器的访问。如果需要，Ansible可以轻松连接Kerberos，LDAP和其他集中式身份验证管理系统。

本文档涵盖了Ansible（2.5）的当前发行版本以及一些开发版本功能。对于最近的功能，我们在每个部分中注意添加功能的Ansible版本。

Ansible大约每两个月发布一个新的主要版本。核心应用程序的演变有点保守，重视语言设计和设置的简单性。然而，围绕新模块和插件开发和提供的社区发展非常迅速，每个版本都增加了许多新模块。





## ansible 原理及详解



**简介**

 ansible是个什么东西呢？官方的title是“Ansible is Simple IT Automation”——简单的自动化IT工具。这个工具的目标有这么几项：

- 自动化部署APP；
- 自动化管理配置项；
- 自动化的持续交互；
- 自动化的（AWS）云服务管理；

 

  所有的这几个目标从本质上来说都是在一个台或者几台服务器上，执行一系列的命令而已。通俗的说就是批量的在远程服务器上执行命令。当然，最主要的是它是基于 paramiko 开发的。这个paramiko是什么呢？它是一个纯Python实现的ssh协议库。因此fabric和ansible还有一个共同点就是不需要在远程主机上安装client/agents，因为它们是基于ssh来和远程主机通讯的。简单归纳一下：

 

Ansible

—基于 Python paramiko 开发，分布式，无需客户端，轻量级，配置语法使用 YMAL 及 Jinja2模板语言，更强的远程命令执行操作

 

类似的自动化运维工具有很多常用的还有：

Puppet

—基于 Ruby 开发，采用 C/S 架构，扩展性强，基于 SSL，远程命令执行相对较弱

 

SaltStack

—基于 Python 开发，采用 C/S 架构，相对 puppet 更轻量级，配置语法使用 YMAL，使得配置脚本更简单

 

## **Ansible 工作机制**

 

Ansible 在管理节点将 Ansible 模块通过 SSH 协议（或者 Kerberos、LDAP）推送到被管理端执行，执行完之后自动删除，可以使用 SVN 等来管理自定义模块及编排

[![wKiom1aSQHHjJRZTAAEBRfKpi_E196.png](http://s2.51cto.com/wyfs02/M02/79/79/wKiom1aSQHHjJRZTAAEBRfKpi_E196.png)](http://s2.51cto.com/wyfs02/M02/79/79/wKiom1aSQHHjJRZTAAEBRfKpi_E196.png)

 

[![wKioL1aSQMaAKaEaAAG9obSmtq8836.png](http://s3.51cto.com/wyfs02/M02/79/78/wKioL1aSQMaAKaEaAAG9obSmtq8836.png)](http://s3.51cto.com/wyfs02/M02/79/78/wKioL1aSQMaAKaEaAAG9obSmtq8836.png)

 

由上面的图可以看到 Ansible 的组成由 5 个部分组成：

 

- Ansible ：     核心
- Modules ：    包括 Ansible 自带的核心模块及自定义模块
- Plugins ：      完成模块功能的补充，包括连接插件、邮件插件等
- Playbooks ：   剧本；定义 Ansible 多任务配置文件，由Ansible 自动执行
- Inventory ：    定义 Ansible 管理主机的清单



### 1. 先决条件

   0.ansible的安装

​	**yum install  ansible**

 1. 两台云主机配置openssh做一下互相通信

 2. 之后把要被管理的ip节点给加入到ansible机器里的 /etc/ansible/hosts

      格式:   

    ​	  [test] 

    ​	   127.0.0.1#要被执行的机器

	3. 之后执行命令测试  出现sueccess则成功

    		 ansible all -m  command -a "who" (all可以改成test，这个test就是你在ansible的节点配置ip的)





### 2.Playbook

 命令: ansible  test -m  file  -a "path=/testdir/test state=directory"

解释: 表示使用ping模块去ping主机test ,然后再用file模块在test主机上创建目录，那么如果把上述命令转换为 **playbook**的表现形式：



#### **2.1 控制单台机器**

```
---
- hosts: test
  remote_user: root
  tasks:
  - name: Ping the host
    ping:
  - name: make directory test
    file:
      path: /testdir/test
      state: directory

```

看这个文档总结来的 ： 没办法复制 http://www.zsythink.net/archives/2602



#### 2.2 控制2台机器

```
---
- hosts: test
  remote_user: root
  tasks:
  - name: Ping the host
    ping:
  - name: make directory test
    file:
      path: /testdir/test
      state: directory
- hosts: shanghai,test
  remote_user: root
  tasks:
  - name: touch tfile
    file:
      path: /tfile
      state: touch
- hosts:
    test 
    shanghai
  remote_user: root
  tasks:
  - name: create user zsythink
    user:
      name: zsythink

```



#### 2.3 控制一台机器去安装ntpd服务(时间服务器)

```
---    #ymal语法标示
- hosts: gz    #配置hosts文件中的所有主机
  tasks: #需要执行的任务
   - name: Ensure NTP (for time synchronization) is installed.    # 名字运行ansible-playbook的时候显示，可以没有
     yum: name=ntp state=installed     #使用yum模块安装ntp，state表示保持安装完成的状态
   - name: Ensure NTP is running.    # 标示
     service: name=ntpd state=started enabled=yes    #ntpd服务要保持启动的状态，并且开机启动

```





### 3. 构建测试环境	

#### 3.0先决条件

​	4台云主机，其中1台本机节点 ，3台其他节点

参考:http://blog.51cto.com/jwh5566/1843477

```
一：
构建测试环境,如下
安装上一篇博客的方法配置3台服务器
我的地址分别是：
10.0.0.130（app1）
10.0.0.131（app2）
10.0.0.141（db）


配置资源文件
#可以把自己节点加入进来，也可以不加
[example]
10.0.0.132
 
[app]
10.0.0.130
10.0.0.131
 
[db]
10.0.0.141
 
[multi:children]
app
db
example
```



#### 3.1 AD-HOC命令使用

查看每个服务器的主机名

​	$ ansible multi -a 'hostname'

使用一个线程执行命令，相当于顺序在每个服务器上运行（默认5个线程执行）

​	$ ansible multi -a 'hostname' -f 1 

查看你的环境情况:

查看磁盘使用情况

​	$ ansible multi -a 'df  -h'

查看内存使用情况

​	$ ansible multi -a  'free -m'

查看时间是否准确

​	$ ansible multi -a 'date'

如果时间不一致，可以使用ntpdate 同步一下

​	$ ansoble multi -a "ntpdate cn.pool.ntp.org"



#### 3.2 安装epel源

```
EPEL是企业版 Linux 附加软件包的简称，EPEL是一个由Fedora特别兴趣小组创建、维护并管理的，针对 红帽企业版 Linux(RHEL)及其衍生发行版(比如 CentOS、Scientific Linux、Oracle Enterprise Linux)的一个高质量附加软件包项目。
EPEL 的软件包通常不会与企业版 Linux 官方源中的软件包发生冲突，或者互相替换文件。EPEL 项目与 Fedora 基本一致，包含完整的构建系统、升级管理器、镜像管理器等等。
```

//安装的阿里云的epel源

**yum -y install epel-release**

//查看一下是否安装成功

**yum repolist**





#### 3.2.0 执行安装django命令

```
前提是安装好epel源和centos base源（可以使用阿里云的镜像源）
$ ansible app -m yum -a "name=MySQL-python state=present"

//present',installed', 是指安裝套件，而 `latest' 則是指安裝最新的套件，也就是會使用 yum mirror 上最新的版本。
$ ansible app -m yum -a "name=python-setuptools state=present"
//参见3.3这里报错了
$ ansible app -m easy_install -a "name=django"

//第三个命令报错，改一个套路，改一个套路
	//先安装pip 
	$easy_install  pip 
	//升级pip
	$python -m pip install --upgrade pip
	//升级python的安装工具
     $python -m pip install --upgrade setuptools



//之后拿pip来安装django 成功
	$ansible  app -m  command -a ' pip install  django'
	
	
    114.67.22.221 | SUCCESS | rc=0 >>
    1.11.14

    114.67.22.213 | SUCCESS | rc=0 >>
    1.11.14

```



#### 3.3 中间涉及的知识点 pip和easyinstall的区别

参考：https://blog.csdn.net/u013709332/article/details/44451341

```
pip (pip installs packages) 的安裝與使用
安装 east_install : 
https://pypi.python.org/pypi/setuptools/5.4.2  
下载ez_setup.py 脚本后执行，就完成了安装
安装pip 可以通过 east_install  pip 安装

区别：

 pip 官網的說法，pip 改善了不少 easy_install 的缺點，如此說來 pip 應該是略勝一籌，不過它還不能夠完全取代對方，因為目前有很多套件還是得用 easy_install 安裝


详细：

安裝套件：
easy_install PackageName
更新套件：
easy_install -U PackageName
移除套件：
easy_install -m PackageName
顯示說明：
easy_install --showhelp
pip (pip installs packages) 的安裝與使用
pip 的安裝方法：
easy_install pip
有趣的是，pip 可以透過 easy_install 安裝，而且也會裝到 Scripts 資料夾下。
安裝套件：
pip install PackageName
更新套件：
pip install -U PackageName
移除套件：
pip uninstall PackageName
搜尋套件：
pip search PackageName
顯示說明：
pip help
```



#### **3.4配置数据库服务器**



```
//出现问题！
$ansible db -m  yum -a "name=mysql-server state=present"
//敲这两个（如果必须要安装MySQL，首先必须添加mysql社区repo通过输入命令：）
// ansible  db -m  command -a ' sudo rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm'
// ansible  db -m  command -a ' yum install mysql mysql-server mysql-libs mysql-server'
$ sudo rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
$  yum install mysql mysql-server mysql-libs mysql-server

//之后敲这个
$ansible db -m service -a "name=mysqld state=started enabled=yes"

```



#### 3.5配置数据库用户django,并且赋予权限

```
$ ansible db  -m yum -a "name=MySQL-python state=present"
$ ansible db  -m mysql_user -a "name=django host=% password=12345 \
priv=*.*:ALL state=present
```



#### 3.6限制命令只在一个服务武器上生效(前提app这个组里要有这个被限制的ip)

```
//先安装下这个ntp服务
$ ansible app -a "yum  install -y  ntp"

$ ansible app -a "service ntpd restart" --limit "114.67.22.213"
$ ansible app  -a "service ntpd restart" --limit "*.4"
$ ansible app  -a "service ntpd restart" --limit ~".*\.4"
```





#### 3.7管理系统用户和组

//系统添加admin组

```
$ ansible app -m group -a "name=admin state=present"
```

//系统添加jwh5566用户

```
$ ansible app -m  user -a "name=jwh5566 group=admin createhome=yes"
```

//删除系统用户

```
$ ansible app -m user -a "name=jwh5566 state=absent"
```



#### 3.8管理文件和目录

//获取文件的信息，权限，所有者等

```
$ ansible multi -m stat -a "path=/etc/environment"
```

//复制文件到服务器

```
$ ansible multi -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

//从服务器接收文件(接收到控制机)

```
$ ansible multi -m fetch -a "src=/etc/hosts dest=/tmp"
```

//创建目录

```
$ ansible multi -m file -a "dest=/tmp/test mode=644 state=directory"
```

//创建符号连接

```
$ ansible multi -m file -a "src=/src/symlink dest=/dest/symlink \ owner=root group=root state=link"
```

//删除目录和文件

```
$ ansible multi -m file  -a "dest=/tmp/test state=absent"
```



#### 3.9运行后台任务

-B <seconds> 指定运行任务的最大时间

-P <seconds> 指定多久时间去一次服务器查看任务执行的状态



**异步**更新服务器(根据系统情况，可能需要很长时间)



**复习异步**

```
同步：
同步的思想是：所有的操作都做完，才返回给用户。这样用户在线等待的时间太长，给用户一种卡死了的感觉（就是系统迁移中，点击了迁移，界面就不动了，但是程序还在执行，卡死了的感觉）。这种情况下，用户不能关闭界面，如果关闭了，即迁移程序就中断了。

异步：
将用户请求放入消息队列，并反馈给用户，系统迁移程序已经启动，你可以关闭浏览器了。然后程序再慢慢地去写入数据库去。这就是异步。但是用户没有卡死的感觉，会告诉你，你的请求系统已经响应了。你可以关闭界面了。

同步，是所有的操作都做完，才返回给用户结果。即写完数据库之后，在相应用户，用户体验不好。
异步，不用等所有操作等做完，就相应用户请求。即先相应用户请求，然后慢慢去写数据库，用户体验较好。

异步操作例子：

为了避免短时间大量的数据库操作，就使用缓存机制，也就是消息队列。先将数据放入消息队列，然后再慢慢写入数据库。
引入消息队列机制，虽然可以保证用户请求的快速响应，但是并没有使得我数据迁移的时间变短（即80万条数据写入mysql需要1个小时，用了redis之后，还是需要1个小时，只是保证用户的请求的快速响应。用户输入完http url请求之后，就可以把浏览器关闭了，干别的去了。如果不用redis，浏览器不能关闭）。

同步就没有任何价值了吗？
银行的转账功能。
```



```
ansible multi  -B 3600 -a "yum -y update"
    background launch...
     
    10.0.0.132 | success >> {
    "ansible_job_id": "763350539037",
    "results_file": "/root/.ansible_async/763350539037",
    "started": 1
```



如果说后台任务还在运行，使用下面的命令查看运行状态

```
$ ansible multi -m async_status -a "jid=763350539037"
```



#### 4.0 检查日志文件

```
$ ansible  multi -a "tail /var/log/messages"
```



如果需要grep,需要使用shell模块

```
ansible multi  -m shell -a "tail /var/log/messages | \
 grep ansible-command | wc -l"
10.0.0.131 | success | rc=0 >>
2
 
10.0.0.130 | success | rc=0 >>
2
 
10.0.0.141 | success | rc=0 >>
6
这个命令显示每台服务器分别执行了几次ansible命令

```





#### 4.1 管理crontab 任务

```
$ ansible multi -m  cron -a "name='daily-cron-all-servers\
hour=4 job='/path/to/daily-script.sh'"
```

可以使用这个配置ntp任务



删除crontab任务

```
$ ansible multi  -m  cron -a "name='daily-cron-all-servers' state=absent"
```







### 4.Playbook追加

https://blog.csdn.net/hxpjava1/article/details/79513812
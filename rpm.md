# 一、什么是RPM

**RPM**的全名是**Red Hat Package Manager**，本意是Red Hat 软件包管理，顾名思义是Red Hat 贡献出来的软件包管理；在Fedora 、Redhat、Mandriva、SuSE、YellowDog等主流发行版本，以及在这些版本基础上二次开发出来的发行版采用。

简单来说，RPM是以一种数据库记录的方式将所需要的软件安装到Linux主机的一套管理程序，最大的特点是将要安装的软件先编译并打包，通过包装好的软件中默认的数据库记录，记录这个软件在安装的时候需要的依赖属性模块，在用户的Linux主机安装时，RPM会先根据软件里的记录数据，查询Linux主机的依赖属性软件是否满足，若满足则予以安装，不满足则不安装。安装的时候将该软件的信息全部写入RPM的数据库中以便将来的查询、验证与卸载。

软件安装流程如下：

[![o_packageinstalllinuxsir_org0000](https://images2018.cnblogs.com/blog/741682/201803/741682-20180328173046939-485069859.jpg)](https://images2018.cnblogs.com/blog/741682/201803/741682-20180328173046239-1118653317.jpg)

总结一下，RPM的**用途**有以下几点：

1、安装、删除、升级和管理软件；当然也支持在线安装和升级软件；

2、通过RPM包管理能知道软件包包含哪些文件，也能知道系统中的某个文件属于哪个软件包；

3、可以在查询系统中的软件包是否安装以及其版本；

4、作为开发者可以把自己的程序打包为RPM 包发布；

5、软件包签名GPG和MD5的导入、验证和签名发布

6、依赖性的检查，查看是否有软件包由于不兼容而扰乱了系统；

 

# 二、RPM的优点和缺点

## 1. 优点

- 由于已经编译完成并且打包，所以安装很方便
- 由于套件信息已经记录在Linux主机的数据库中，方便查询、升级与卸载

## 2. 缺点

- 安装环境必须与打包时的环境一致
- 需要满足软件的依赖属性需求
- 卸载时需要特别小心，最底层的软件不可以先删除，否则可能造成整个系统出问题

 



# 三、RPM的使用权限

RPM软件的安装、删除、更新只有root权限才能使用；对于查询功能任何用户都可以操作；如果普通用户拥有安装目录的权限，也可以进行安装。

 



# 四、RPM包的命名规则

## 1. 命名格式

-  name-version-arch.rpm
- name-version-arch.src.rpm

## 2. 说明

- name：软件包名称。
- version：带有主、次和修订的软件包版本。
- arch：硬件平台。硬件平台包括了：i386、i486、i586、i686、x86_64、ppc、sparc、alpha
- src.rpm：源代码包。

## 3.  范例

以“openssl-1.0.1c-1.fc18.i686.rpm”为例：

- openssl：是软件名称。
- 1.0.1c-1：是软件版本。
- i686：是适用的硬件平台。

## 4. 特殊名称

1）fcXX，elXX：表示这个软件包的发行商版本，就像这里的fc18，说明这个软件包是在Fedora 18下使用的。而openssl-1.0.0-20.el6.x86_64.rpm表示这个软件包是在RHEL 6.x(Red Hat Enterprise Linux)/CentOS 6.x下使用。

2）devel：表示这个RPM包是软件的开发包，例如mysql-devel-5.1.52-1.el6_0.1.i686.rpm。

3）noarch：说明这样的软件包可以在任何平台上安装，不需要特定的硬件平台。在任何硬件平台上都可以运行。

 



# 五、基本用法

## 一）RPM的软件包查询功能

RPM在查询的时候，查询的地方是在/var/lib/rpm目录下的数据库文件。

命令格式：

```
rpm -qa
rpm -q[licdR] 已经安装的软件名称
rpm -qf 存在于系统中的某个文件名称
rpm -qp[licdR] 未安装的某个文件名称
```

从上面的命令看来，根据后面所带的参数来区分可以分为四种：

\1. 后面不接名称的

-  **-qa：**查询所有已经安装的软件名称

\2. 后面接已经安装的软件名称的：

-  **-q：**查询后面接的软件是否安装，已安装有信息输出，否则没有
- **-qi：**列出该软件的详细信息（information），包含开发商、版本与说明等
- **-ql：**列出该软件所有的文件与目录（list）
- **-qc：**列出该软件的所有配置文件
- **-qd：**列出该软件的所有帮助文件（与man有关的文件）
- -**qR：**列出与该软件有关的依赖软件所含的文件（Required）

\3. 后面接一个存在于系统的文件名称

- **-qf：**找出该文件属于哪个已安装的软件

\4. 后面接一个.rpm文件

- **-qp[licdR]：-**qp后面接的所有参数以上面的说明为准，目的在于找出某个rpm文件内的信息，而非已安装的软件信息

 

## 二）软件包的安装和升级

\1. 安装

1）命令格式

```
rpm -ivh package_name.rpm
参数：
-i：install的意思
-v：查看更详细的安装信息页面
-h：以安装信息列显示安装进度
```

2）范例

```
rpm –ivh rp-ppppoe-3.1-5.i386.rpm # 安装一个软件
rpm –ivh a.i386.rpm b.i386.rpm *.rpm # 安装多个软件
rpm –ivh http://website.name/path/pkgname.rpm # 通过网络直接安装软件
```

如果在安装过程中发现问题，或者已经知道会发生的问题，还执意安装，可以使用“**强制**”安装参数：

[![installforce](https://images2018.cnblogs.com/blog/741682/201803/741682-20180328173053500-1888728370.jpg)](https://images2018.cnblogs.com/blog/741682/201803/741682-20180328173051087-1236257758.jpg)

2.升级

1）命令格式

```
rpm –Uvh package_name.rpm # 如果该软件没安装过，则直接安装，若没安装则升级至最新版
rpm –Fvh package_name.rpm # 如果该软件没有安装，则不会安装
```

 

## 三）RPM卸载与重建数据库

\1. 命令格式

```
rpm -e logrotate  # 卸载logrotate
rpm –-rebuilddb   # 重建数据库
```

注意，卸载过程要自上而下，否则会出现结构问题。由于一直在修改文件内容，有时候会导致数据库有点乱，这个时候就可以使用命令重建rpm的数据库。

 

## 四）RPM验证与数字签名

验证功能主要是向系统管理员提供一种有用的管理机制，方式是用数据库内容，来比较当前Linux系统环境的所有软件文件，当有数据丢失或者误删/修改某个软件的文件时，就用这种方法来验证原理的文件系统，以了解改动的地方。

\1. 命令格式

[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
rpm -Va
rpm -V 已安装的软件名称
rpm -Vp 某个rpm文件的文件名
rpm -Vf 系统上的某个文件

参数：
-Va：列出当前系统上所有可能改动过的文件
-V：跟软件名称，如果所含文件被更改过，才会列出来
-Vp：跟文件名称，列出该软件内可能更改过的文件
-Vf：列出某个文件是否被更改过
```

[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

\2. 从范例看**修改因素**

查询/etc/crontab是否被更改过

​    rpm –Vf /etc/crontab

​    S.5…..T c /etc/crontab

上面的信息从左到右分别表示已改变的因素：

- S：（file Size differs）文件的容量大小
- M：（Mode differs）文件的类型或属性，以及可执行参数
- 5：（MD5 sum differs）MD5这一加密防被黑的属性
- D：（Device major/minor number mis-match）设备名称
- L：（readLink（2）path mis-match）Link属性
- U：（User ownership differs）文件的拥有者
- G：（Group ownership differs）文件所属用户组
- T：（mTime differs）文件的建立时间

如果一个文件全部信息都改过，显示会是：

​    SM5DLUGT c filename

其中c表示“Config file”，也就是文件类型，文件类型有几类：

- c：配置文件，config file
- d：文档文件，documentation
- g：ghost文件，通常该文件不包含在某个软件中，较少发生，ghost file
- l：授权文件，license file
- r：自述文件，read me

经过验证就知道哪个文件被改过，是否符合预期。

\3. 数字签名

rpm可以使用数字签名来判断待安装的软件是否有问题，对数字签名不熟悉的，可以看看阮一峰的两篇文章：

- [密码学笔记](http://www.ruanyifeng.com/blog/2006/12/notes_on_cryptography.html)
- [数字签名是什么](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)

一般我们使用的是GPG的公钥，方法很简单，如果想要使用某个软件，就要将该发布商的GPG公钥先安装到自己的系统上，然后，安装软件时，就会坚持两个密钥是否相同，如果相同就直接安装，不同则在显示信息，之初未安装发布商的GPG公钥。

安装公钥方法很简单，如red hat系统自带有公钥，安装方法：

```
rpm --import /usr/share/rhn/RPM-GPG-KEY
```

一般来说，Linux系统都会发布自己的GPG密钥，可以使用以下命令来搜索文件：

```
locate GPG-KEY
```

已经安装的公钥可以用下面命令查询

```
rpm -qa | grep gpg
```

然后选取gpg-pubkey-…文件来查看信息

```
rpm -qi gpg-pubkey-c105b9de-4e0fd3a3
```

 

## 六、小结

本文开头介绍了RPM的由来和用途，然后分析了RPM的优缺点和使用权限，最后重点将了包的命名规则和RPM的基本用法。

虽然RPM很好用，但是实际上现在已经出现了基于RPM包管理的，更强大的工具，如yum。所以建议在安装软件的时候，还是使用yum来安装。
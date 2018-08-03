1.首先在服务器上生成公私钥

2.如果想从A链接B ，那么则需要把A的公钥放到B的  home下/用户下/.ssh/authorized_keys 认证的文件下

(你是想通过命令还是复制无所谓)

3.（之后改一下权限)

4.这里你要明确，你必须有私钥，之后去访问，服务器才会把公钥给你 让你保存 确保传送





​    **eggs:我有两台笔记本电脑上分别装有两个centos的虚拟机，一个IP为172.16.1.10(slave),一个IP为172.16.1.9(master)。**

在slave上用root用户 vi /etc/hosts ,在里面增加 172.16.1.9   master。

**1 在slave上执行：s**

复制代码

ssh-keygen -t rsa或者ssh-keygen -t rsa -P ''

-P表示密码，-P '' 就表示空密码，也可以不用-P参数，这样就要三车回车，用-P就一次回车。
它在~目录下生成.ssh目录，.ssh下有id_rsa和id_rsa.pub。

**2 在slave上执行scp远程拷贝命令：**

//复制代码

scp ~/.ssh/id_rsa.pub <a href="mailto:hadoop@master:~/id_rsa.pub">hadoop@master:~/id_rsa.pub</a> 

由于此时还没有设置免密码登陆，所以此时远程拷贝需要输入密码。

（scp 命令格式如下：

//复制代码

//sc p     本地文件目录        目标地址  目标路径 

**scp   /home/adminstor/news.txt    root@163.163.163:/etc/hosts**   

 

**3 在master上执行:** 

//复制代码

**cat ~/id_rsa.pub >> ~/.ssh/authorized_keys** 



**4.将公钥追加到授权KEY里面。 执行下面的命令**

//复制代码

**chmod 600 ~/.ssh/authorized_keys**

authorized_keys的权限要是600。

此时 slave机就可以 ssh master 了。
小结：登录的机子可有私钥，被登录的机子要有登录机子的公钥。这个公钥/私钥对一般在私钥宿主机产生。上面是用rsa算法的公钥/私钥对，当然也可以用dsa(对应的文件是id_dsa，id_dsa.pub)

想让A，B机无密码互登录，那B机以上面同样的方式配置即可。







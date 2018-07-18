### 1.安装jenkins (参照jenkins.pdf)

1.安装java(参考文档)
2.安装tomcat (参考文档)
3.上传war包(参考文档)
4.端口云主机开启80 或者8080 （不备案，是不好使的,自动屏蔽掉)
5.hostname (查看主机名称之后把名称加163.53.91.49 i-b5b36fed 进去)

  5.1修改config/server.xml ?(在8080端口后加入 并修改端口80 address="0.0.0.0") 

  5.2重启tomcat

?	再看看netstat -lnpt 在不在ipv6上 

?	**https://blog.csdn.net/weiwangchao_/article/details/49820101  解决让tomcat只抛在ipv4上**

   5.3.访问http://ip/war包名

6.中间学习的命令:
	$netstat -lnpt  查看服务所占用的端口
	$tail -300 catalina.out 打印日志（首先cd tomcat/logs）
	ps -ef | grep java 过滤出服务的进程 （1. 可以去可以kill -9 进程号  2.也可以通过bin目录下去执行启动文件，和停止文件）

7.中间出现隐藏文件问题
	ls -lta 查看隐藏文件
	rm -rf  .server.xml.swp  删除隐藏文件



### 2.jenkins控制台配置

1.管理员密码 :

?	$ cat /root/.jenkins/secrets/initialAdminPassword

2.出现离线安装的解决办法:

?	$ vim root/.jenkins/hudson.model.UpdateCenter.xml 将下面一行

?	(<url>https://updates.jenkins.io/update-center.json</url>)	

?	换成下面所示就行

 <url>https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json</url>

2. 修改密码 

3. 之后配置ssh 在jenkins上 实现两个云主机是通的

   ```
   1.两台机器相同操作
   ssh-keygen -trsa
   然后，不断的按回车键。
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   2、将公钥复制到其他从机
   #注意如果有多的话则最好公钥手动粘贴呼唤下
   scp ~/.ssh/authorized_keys root@slave1:~/.ssh/
   scp ~/.ssh/authorized_keys root@slave2:~/.ssh/ 
   ```

4. 更新之后页面出现问题改下/root/.jenkins/config文件里的配置

   ```
    <authorizationStrategy class="hudson.security.LegacyAuthorizationStrategy"/>
     <securityRealm class="hudson.security.HudsonPrivateSecurityRealm">
       <disableSignup>false</disableSignup>
       <enableCaptcha>false</enableCaptcha>
     </securityRealm>
   ```

   

   

### 3.被部署的节点 

####  3.1django环境搭建 

 https://blog.csdn.net/GitChat/article/details/78271099

```
1.由于jdnago 1.7之后的版本就不支持python 2.6了，所以我们需要升级python 2.6-2.7。
[root@vagrant-centos65 ~]# yum -y install  zlib zlib-devel openssl openssl-devel  sqlite-devel
[root@vagrant-centos65 ~]# wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2

#坑，需要安装bzip2安装工具：$yum -y install  bzip2
[root@vagrant-centos65 ~]# tar -jxvf Python-2.7.3.tar.bz2

[root@vagrant-centos65 ~]# cd Python-2.7.3

#坑, 原因是: 缺少gcc编译环境:
     配置yum，可以用yum install -y  gcc 
     没有配置yum   : 可以安装gcc的安装包
[root@vagrant-centos65 Python-2.7.3]# ./configure    --prefix=/usr/local/python2.7
[root@vagrant-centos65 Python-2.7.3]# make && make install
[root@vagrant-centos65 Python-2.7.3]# cd /usr/bin/
[root@vagrant-centos65 bin]# ll | grep python
-rwxr-xr-x.   2 root root      4864 Nov 22  2013 python
lrwxrwxrwx.   1 root root         6 Jan 16  2014 python2 -> python
-rwxr-xr-x.   2 root root      4864 Nov 22  2013 python2.6
[root@vagrant-centos65 bin]# mv python python2.6.bak
[root@vagrant-centos65 bin]# ln -s /usr/local/python2.7/bin/python /usr/bin/python
[root@vagrant-centos65 bin]# vi /usr/bin/yum
#!/usr/bin/python2.6


2.安装setuptools：pip的安装需要依赖setuptools。其实是pip的安装setup.py有这样一条代码from setuptools import setup：
[root@vagrant-centos65 bin]# cd /opt/
[root@vagrant-centos65 opt]# wget https://pypi.python.org/packages/61/3c/8d680267eda244ad6391fb8b211bd39d8b527f3b66207976ef9f2f106230/setuptools-1.4.2.tar.gz
[root@vagrant-centos65 opt]# tar zxvf setuptools-1.4.2.tar.gz
[root@vagrant-centos65 opt]# cd setuptools-1.4.2
[root@vagrant-centos65 setuptools-1.4.2]# python setup.py install


3.安装pip：
[root@vagrant-centos65 ~]# cd /opt/
[root@vagrant-centos65 opt]# wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate
[root@vagrant-centos65 opt]# tar zxvf pip-1.5.4.tar.gz
[root@vagrant-centos65 opt]# cd pip-1.5.4
[root@vagrant-centos65 pip-1.5.4]# python setup.py install
[root@vagrant-centos65 pip-1.5.4]# pip
-bash: pip: command not found
[root@vagrant-centos65 pip-1.5.4]# find / -name pip
/usr/local/python2.7/bin/pip
[root@vagrant-centos65 pip-1.5.4]# ln -s /usr/local/python2.7/bin/pip /usr/bin/pip

4.安装django：
[root@vagrant-centos65 pip-1.5.4]# pip install django
[root@vagrant-centos65 pip-1.5.4]# pip list
Django (1.11.3)
pip (1.5.4)
pytz (2017.2)
setuptools (1.4.2)
wsgiref (0.1.2)
```



#### 3.2jenkins配置OpenSSH

**参考 ：https://blog.csdn.net/tototuzuoquan/article/details/78568655**



#### 3.3jenkins配置git

**jenkins安装git:**

centos安装git:

?		1 .yum install -y git 坑:yum安装出现问题看vim /usr/local/yum的版本 给改成和python一样的版本
		2.  centos升级git参照 : https://www.cnblogs.com/kevingrace/p/8252517.html

?		3.jenkin连接github :https://blog.csdn.net/boling_cavalry/article/details/78943061

### 4.自动化django服务

#### 4.1 在被控制的节点搭django服务

**参考：https://blog.csdn.net/nunchakushuang/article/details/77118621**




    本文旨在使用一个全新安装好的Linux系统从0开始进行Hadoop伪分布式环境的搭建，以达到快速搭建的目的，从而体验Hadoop的魅力所在，为后面的继续学习提供基础环境。
    对使用的系统环境作如下说明：


操作系统：CentOS 6.5 64位


主机IP地址：10.0.0.131/24


主机名：leaf


用户名：root


hadoop版本：2.6.5


jdk版本：1.7


    可以看到，这里直接使用root用户，而不是按照大多数的教程创建一个hadoop用户来进行操作，就是为了达到快速搭建Hadoop环境以进行体验的目的。
    为了保证后面的操作能够正常完成，请先确认本机是否可以解析到主机名leaf，如果不能，请手动添加解析到/etc/hosts目录中：



[root@leaf ~]# echo "127.0.0.1  leaf" >> /etc/hosts 
[root@leaf ~]# ping leaf 
PING leaf (127.0.0.1) 56(84) bytes of data. 
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.043 ms 
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.048 ms 
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.046 ms




1.rsync软件安装
    使用下面命令安装：


[root@leaf ~]# yum install -y rsync



2.ssh安装与免密码登陆配置
（1）ssh安装
    使用下面命令安装


[root@leaf ~]# yum install -y openssh-server openssh-clients


（2）ssh免密码登陆配置
    因为Hadoop使用ssh协议来管理远程守护进程，所以需要配置免密码登陆。


关闭防火墙和selinux


    为了确保能够成功配置，在配置前，先把防火墙和selinux关闭：

**关闭防火墙**

[root@leaf ~]# /etc/init.d/iptables stop 
[root@leaf ~]# chkconfig --level 3 iptables off 

**关闭selinux**

[root@leaf ~]# setenforce 0 
[root@leaf ~]# sed -i s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config  
[root@leaf ~]# cat /etc/selinux/config | grep disabled 

disabled - No SELinux policy is loaded.

SELINUX=disabled





生成密钥对





[root@leaf ~]# mkdir .ssh 
[root@leaf ~]# ssh-keygen -t dsa -P '' -f .ssh/id_dsa 
Generating public/private dsa key pair. 
Your identification has been saved in .ssh/id_dsa. 
Your public key has been saved in .ssh/id_dsa.pub. 
The key fingerprint is: 
5b:af:7c:45:f3:ff:dc:50:f5:81:4b:1e:5c:c1:86:90 root@leaf 
The key's randomart image is: 
+--[ DSA 1024]----+ 
|           .o oo.| 
|           E..oo | 
|             =...| 
|            o = +| 
|        S .  + oo| 
|         o .  ...| 
|        .   ... .| 
|         . ..  oo| 
|          o.    =| 
+-----------------+





将公钥添加到本地信任列表




[root@leaf ~]# cat .ssh/id_dsa.pub >> .ssh/authorized_keys




验证


    上面三步完成后就完成了免密码登陆的配置，可以使用下面的命令进行验证：



[root@leaf ~]# ssh localhost 
The authenticity of host 'localhost (::1)' can't be established. 
RSA key fingerprint is d1:0d:ed:eb:e7:d1:2f:02:23:70:ef:11:14:4e:fa:42. 
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'localhost' (RSA) to the list of known hosts. 
Last login: Wed Aug 30 04:28:01 2017 from 10.0.0.1 
[root@leaf ~]#



    在第一次登陆的时候需要输入yes，之后再登陆时就可以直接登陆了：



[root@leaf ~]# ssh localhost 
Last login: Wed Aug 30 04:44:02 2017 from localhost 
[root@leaf ~]#




3.jdk安装与配置
（1）jdk下载
    这里使用的是jdk1.7版本，可以到下面的网站进行下载：
http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html
    下载完成后，可以使用winscp上传到/root目录下，如下：



[root@leaf ~]# ls -lh jdk-7u80-linux-x64.tar.gz  
-rw-r--r--. 1 root root 147M Aug 29 12:05 jdk-7u80-linux-x64.tar.gz



（2）jdk安装
    将jdk解压到/usr/local目录下，并创建软链接：



[root@leaf ~]# cp jdk-7u80-linux-x64.tar.gz /usr/local/ 
[root@leaf ~]# cd /usr/local/ 
[root@leaf local]# tar -zxf jdk-7u80-linux-x64.tar.gz  
[root@leaf local]# ls -ld jdk1.7.0_80/ 
drwxr-xr-x. 8 uucp 143 4096 Apr 11  2015 jdk1.7.0_80/ 
[root@leaf local]# ln -s jdk1.7.0_80/ jdk 
[root@leaf local]# ls -ld jdk 
lrwxrwxrwx. 1 root root 12 Aug 30 04:56 jdk -> jdk1.7.0_80/



（3）JAVA_HOME环境变量配置
    java命令在/usr/local/jdk/bin目录下：



[root@leaf local]# cd jdk/bin/ 
[root@leaf bin]# ls -lh java 
-rwxr-xr-x. 1 uucp 143 7.6K Apr 11  2015 java



    配置java环境变量：



[root@leaf bin]# echo 'export JAVA_HOME=/usr/local/jdk/bin' >> /etc/profile 
[root@leaf bin]# echo 'export PATH=$PATH:$JAVA_HOME' >> /etc/profile 
[root@leaf bin]# source /etc/profile



    这样我们就可以在任何一个目录下使用java相关的命令：



[root@leaf ~]# java -version 
java version "1.7.0_80"
Java(TM) SE Runtime Environment (build 1.7.0_80-b15) 
Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode) 
[root@leaf ~]# javac -version 
javac 1.7.0_80




4.hadoop安装与配置
（1）hadoop下载
    这里使用hadoop 2.6.5版本，可以到下面的网站进行下载：
http://hadoop.apache.org/releases.html
    选择2.6.5的binary进入相应的页面便可以下载，然后使用winscp上传到/root目录下，如下：



[root@leaf ~]# ls -lh hadoop-2.6.5.tar.gz  
-rw-r--r--. 1 root root 191M Aug 29 19:09 hadoop-2.6.5.tar.gz



（2）hadoop安装
    将hadoop解压到/usr/local目录下，并创建软链接：



[root@leaf ~]# cp hadoop-2.6.5.tar.gz /usr/local 
[root@leaf ~]# cd /usr/local 
[root@leaf local]# tar -zxf hadoop-2.6.5.tar.gz  
[root@leaf local]# ls -ld hadoop-2.6.5 
drwxrwxr-x. 9 1000 1000 4096 Oct  3  2016 hadoop-2.6.5 
[root@leaf local]# ln -s hadoop-2.6.5 hadoop 
[root@leaf local]# ls -ld hadoop 
lrwxrwxrwx. 1 root root 12 Aug 30 05:05 hadoop -> hadoop-2.6.5



（3）hadoop环境变量配置
    hadoop相关命令在/usr/local/hadoop/bin和/usr/local/hadoop/sbin目录下，如下所示：



[root@leaf local]# cd hadoop/bin/ 
[root@leaf bin]# ls -lh hadoop 
-rwxr-xr-x. 1 1000 1000 5.4K Oct  3  2016 hadoop



    配置hadoop环境变量：








[root@leaf bin]# echo 'export HADOOP_HOME=/usr/local/hadoop/bin:/usr/local/hadoop/sbin' >> /etc/profile 
[root@leaf bin]# echo 'export PATH=$PATH:$HADOOP_HOME' >> /etc/profile







    这样我们就可以在任何一个目录下使用hadoop相关的命令：



[root@leaf ~]# hadoop 
Usage: hadoop [--config confdir] COMMAND 
       where COMMAND is one of: 
  fs                   run a generic filesystem user client 
  version              print the version 
  jar <jar>            run a jar file
  checknative [-a|-h]  check native hadoop and compression libraries availability 
  distcp <srcurl> <desturl> copy file or directories recursively 
  archive -archiveName NAME -p <parent path> <src>* <dest> create a hadoop archive 
  classpath            prints the class path needed to get the 
  credential           interact with credential providers 
                       Hadoop jar and the required libraries 
  daemonlog            get/set the log level for each daemon 
  trace                view and modify Hadoop tracing settings 
 or 
  CLASSNAME            run the class named CLASSNAME 

Most commands print help when invoked w/o parameters.



（4）hadoop配置
    hadoop的配置文件在/usr/local/hadoop/etc/hadoop目录下：



[root@leaf ~]# cd /usr/local/hadoop/etc/hadoop/ 
[root@leaf hadoop]# ls 
capacity-scheduler.xml      hadoop-policy.xml        kms-log4j.properties        ssl-client.xml.example 
configuration.xsl           hdfs-site.xml            kms-site.xml                ssl-server.xml.example 
container-executor.cfg      httpfs-env.sh            log4j.properties            yarn-env.cmd 
core-site.xml               httpfs-log4j.properties  mapred-env.cmd              yarn-env.sh 
hadoop-env.cmd              httpfs-signature.secret  mapred-env.sh               yarn-site.xml 
hadoop-env.sh               httpfs-site.xml          mapred-queues.xml.template 
hadoop-metrics2.properties  kms-acls.xml             mapred-site.xml.template 
hadoop-metrics.properties   kms-env.sh               slaves





配置core-site.xml





<configuration> 
    <property> 
        <name>fs.default.name</name> 
        <value>hdfs://localhost:9000</value> 
    </property> 
</configuration>



    fs.default.name这个字段下的值用于指定NameNode（HDFS的Master）的IP地址和端口号，如下面的value值hdfs://localhost:9000，就表示HDFS NameNode的IP地址或主机为localhost，端口号为9000.


配置hdfs-site.xml





<configuration> 
    <property> 
        <name>dfs.replication</name> 
        <value>1</value> 
    </property> 
    <property> 
        <name>dfs.name.dir</name> 
        <value>/home/nuoline/hdfs-filesystem/name</value> 
    </property> 
    <property> 
        <name>dfs.data.dir</name> 
        <value>/home/nuoline/hdfs-filesystem/data</value> 
    </property> 
</configuration>



    dfs.replication用于指定HDFS中每个Block块被复制的次数，起到数据冗余备份的作用；dfs.name.dir用于配置HDFS的NameNode的元数据，以逗号隔开，HDFS会把元数据冗余复制到这些目录下；dfs.data.dir用于配置HDFS的DataNode的数据目录，以逗号隔开，HDFS会把数据存在这些目录下。


配置mapred-site.xml





<configuration> 
    <property> 
        <name>mapred.job.tracker</name> 
        <value>localhost:9001</value> 
    </property> 
</configuration>



    mapred.job.tracker字段用于指定MapReduce Jobtracker的IP地址及端口号，如这里IP地址或主机为localhost，9001是MapReduce Jobtracker RPC的交互端口。


配置hadoop-env.sh




export JAVA_HOME=/usr/local/jdk



5.hadoop启动与测试
（1）格式化HDFS分布式文件系统
    执行如下命令：



[root@leaf ~]# hadoop namenode -format 
... 
17/08/30 08:41:29 INFO namenode.NNStorageRetentionManager: Going to retain 1 images with txid >= 0 
17/08/30 08:41:29 INFO util.ExitUtil: Exiting with status 0 
17/08/30 08:41:29 INFO namenode.NameNode: SHUTDOWN_MSG:  
/************************************************************ 
SHUTDOWN_MSG: Shutting down NameNode at leaf/127.0.0.1 
************************************************************/



    注意看输出显示是不是跟上面的类似，如果是，则说明操作成功。
（2）启动hadoop服务
    执行如下命令：



[root@leaf ~]# start-all.sh  
This script is Deprecated. Instead use start-dfs.sh and start-yarn.sh 
17/08/30 08:53:22 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable 
Starting namenodes on [localhost] 
localhost: starting namenode, logging to /usr/local/hadoop-2.6.5/logs/hadoop-root-namenode-leaf.out 
localhost: starting datanode, logging to /usr/local/hadoop-2.6.5/logs/hadoop-root-datanode-leaf.out 
Starting secondary namenodes [0.0.0.0] 
0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop-2.6.5/logs/hadoop-root-secondarynamenode-leaf.out 
17/08/30 08:53:48 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable 
starting yarn daemons 
starting resourcemanager, logging to /usr/local/hadoop-2.6.5/logs/yarn-root-resourcemanager-leaf.out 
localhost: starting nodemanager, logging to /usr/local/hadoop-2.6.5/logs/yarn-root-nodemanager-leaf.out



（3）hadoop服务测试
    启动完成后，执行jps命令，可以看到hadoop运行的守护进程，如下：



[root@leaf ~]# jps 
4167 SecondaryNameNode 
4708 Jps 
3907 NameNode 
4394 NodeManager 
4306 ResourceManager 
3993 DataNode



    也可以通过在浏览器中输入地址来访问相关页面，这里访问NameNode的页面，地址为http://10.0.0.131:50070，如下：
    访问DataNode的页面，地址为http://10.0.0.131:50075，如下

**补充**

2.如果java这种环境变量配置失败了

​	在root目录下 **vi ~/.bashrc**  仅对当前用户有效

```
export JAVA_HOME=/usr/local/jdk
export PATH=$PATH:$JAVA_HOME/bin
```

1.sudo  vim  /etc/hosts  (其实可有可无)

```
# The following lines are desirable for IPv4 capable hosts
127.0.0.1 VM_16_23_centos VM_16_23_centos
127.0.0.1 localhost.localdomain localhost
127.0.0.1 localhost4.localdomain4 localhost4

# The following lines are desirable for IPv6 capable hosts
::1 VM_16_23_centos VM_16_23_centos
::1 localhost.localdomain localhost
::1 localhost6.localdomain6 localhost6


```

2. 配置文件  

   sudo   vim  core-site.xml

   ```
   <configuration>
    <property>

           <name>fs.default.name</name>

           <value>hdfs://localhost:50090</value>

       </property>

   </configuration>

   ```

   sudo  vim  hdfs-site.xml

   ```

       http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License. See accompanying LICENSE file.
   -->

   <!-- Put site-specific property overrides in this file. -->

   <configuration>
    <property>

           <name>dfs.replication</name>

           <value>1</value>

       </property>

       <property>

           <name>dfs.name.dir</name>

           <value>/home/nuoline/hdfs-filesystem/name</value>

       </property>

       <property>

           <name>dfs.data.dir</name>

           <value>/home/nuoline/hdfs-filesystem/data</value>

       </property>


   ```

   sudo  vim  mapred-site.xml

   ```

   <?xml version="1.0"?>
   <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
   <!--
     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License. See accompanying LICENSE file.
   -->

   <!-- Put site-specific property overrides in this file. -->

   <configuration>

       <property>

           <name>mapred.job.tracker</name>

           <value>localhost:9001</value>

       </property>

   </configuration>


   ```

   ​

3. netstate  -lnp  是查看启动的服务端口  (查看网卡监听状态) 如果启动，则可以访问

   ​

4. 通过外网ip 来访问服务    
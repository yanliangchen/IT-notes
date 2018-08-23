

### **svn 安装**

```
安装服务

yum install subversion
配置服务

mkdir -p /data/wwwsvn/myrepo #创建svn仓库的目录
这里可以自定义创建的目录，注意不是网站的文件目录。

svnadmin create /data/wwwsvn/myrepo #与上面的目录相同。
这里要注意该目录不能是空目录。 成功以后会得到以下文件

# ls
conf db format hooks locks README.txt
进入conf修改配置文件
vi passwd添加在末尾

[users]
# harry = harryssecret
# sally = sallyssecret
youname = yourpassword #你的用户和密码
vi authz添加在末尾

...
[/]
yourname = rw
vi svnserve.conf关闭注释以及修改变量

anon-access = read #匿名用户可读
auth-access = write #授权用户可写
password-db = passwd #使用哪个文件作为账号文件
authz-db = authz #使用哪个文件作为权限文件
realm = /data/wwwsvn/myrepo # 认证空间名，版本库所在目录，和之前的一样
开启和关闭服务

svnserve -d -r /data/wwwroot/myrepo #开启
killall svnserve #关闭
ps aux | grep svnserve #查看是否运行
打开端口
这一步很重要，如果你都配置完了却发现连接不上，那一定是端口没有打开，默认端口是3690.

iptables -I INPUT -i eth0 -p tcp --dport 3690 -j ACCEPT #开放端口 
service iptables save #保存 iptables 规则（如不能保存请使用其他方法保存）
客户端连接
Windows
使用TortoiseSVN,url填写svn://你的服务器ip，账号密码填刚刚设置的。
```



### **svn 使用**

需要下载TortoiseSVN  



下载连接 ： https://www.visualsvn.com/visualsvn/download/tortoisesvn/



#### svn 检出操作

 

我们就可以通过这个URL在客户端对版本库进行检出操作。

  svn checkout http://svn.server.com/svn/project_repo --username=user01 以上命令将产生如下结果： 

```
root@runoob:~/svn# svn checkout svn://192.168.0.1/runoob01 --username=user01
A    runoob01/trunk
A    runoob01/branches
A    runoob01/tags
Checked out revision 1.
```

 

检出成功后在当前目录下生成runoob01副本目录。查看检出的内容

 

```
root@runoob:~/svn# ll runoob01/
total 24
drwxr-xr-x 6 root root 4096 Jul 21 19:19 ./
drwxr-xr-x 3 root root 4096 Jul 21 19:10 ../
drwxr-xr-x 2 root root 4096 Jul 21 19:19 branches/
drwxr-xr-x 4 root root 4096 Jul 21 19:19 .svn/
drwxr-xr-x 2 root root 4096 Jul 21 19:19 tags/
drwxr-xr-x 2 root root 4096 Jul 21 19:19 trunk/
```

 

你想查看更多关于版本库的信息，执行 info 命令。





#### svn  提交操作 

我们在库本版中需要增加一个readme的说明文件。

 

```
root@runoob:~/svn/runoob01/trunk# cat readme 
this is SVN tutorial.
```

 

查看工作副本中的状态。

 

```
root@runoob:~/svn/runoob01/trunk# svn status
?       readme
```

  

此时 readme的状态为？，说明它还未加到版本控制中。

  

将文件readme加到版本控制，等待提交到版本库。

 

```
root@runoob:~/svn/runoob01/trunk# svn add readme 
A         readme
```

 

查看工作副本中的状态

 

```
root@runoob:~/svn/runoob01/trunk# svn status     
A       readme
```

 

此时 readme的状态为A,它意味着这个文件已经被成功地添加到了版本控制中。

 

为了把 readme 存储到版本库中，使用 commit -m 加上注释信息来提交。 

如果你忽略了 -m 选项， SVN会打开一个可以输入多行的文本编辑器来让你输入提交信息。

 

```
root@runoob:~/svn/runoob01/trunk# svn commit -m "SVN readme."
Adding         readme
Transmitting file data .
Committed revision 8.
svn commit -m "SVN readme."
```

 

现在 readme 被成功地添加到了版本库中，并且修订版本号自动增加了1。



#### svn 查看版本 更新到指定版本 

$ svn log  

$ svn update -r6



#### svn 版本回退 

添加之后 不想添加了 可以用

$ svn revert 文件名



#### svn 分支 

通过copy 命令来创建分支 用到的时候看菜鸟教程 或者百度吧 根git有很大区别  





#### svn tags 

可以给版本进行打标签

trunk  可能是一个分支名

```
root@runoob:~/svn/runoob01# svn copy trunk/ tags/v1.0
A         tags/v1.0
```

 

上面的代码成功完成，新的目录将会被创建在 tags 目录下。

 

```
root@runoob:~/svn/runoob01# ls tags/
v1.0
root@runoob:~/svn/runoob01# ls tags/v1.0/
HelloWorld.html  readme
```

 

查看状态。

 

```
root@runoob:~/svn/runoob01# svn status
A  +    tags/v1.0
```

 

提交tag内容。

 

```
root@runoob:~/svn/runoob01# svn commit -m "tags v1.0" 
Adding         tags/v1.0
Transmitting file data ..
Committed revision 14.
```














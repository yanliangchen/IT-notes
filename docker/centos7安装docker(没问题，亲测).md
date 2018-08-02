原

# centos7 安装docker

 	

2017年11月22日 19:16:44

 				阅读数：177 											

 	

- [安装](https://blog.csdn.net/u012460749/article/details/78607128#1-安装)
- [使用Docker加速器](https://blog.csdn.net/u012460749/article/details/78607128#2-使用docker加速器)
- [开放管理端口映射](https://blog.csdn.net/u012460749/article/details/78607128#3-开放管理端口映射)
- [测试docker](https://blog.csdn.net/u012460749/article/details/78607128#4-测试docker)
- [参考资料](https://blog.csdn.net/u012460749/article/details/78607128#参考资料)

直接用yum install docker -y安装的docker版本为1.12，但是docker发展很快，现在都17.09.0了。

# 1 安装

1 卸载老版本的 docker 及其相关依赖

```
sudo yum remove docker docker-common container-selinux docker-selinux docker-engine1
```

2 安装 yum-utils，它提供了 yum-config-manager，可用来管理yum源

```
sudo yum install -y yum-utils1
```

3 添加yum源

```
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo1
```

4 更新yum索引

```
sudo yum makecache fast1
```

5 安装 docker-ce

```
sudo yum install docker-ce1
```

6 启动 docker

```
sudo systemctl start docker1
```

7 验证是否安装成功

```
sudo docker info1
```

8 设置开机启动

```
$systemctl enable docker1
```

# 2 使用Docker加速器

通过修改daemon配置文件`/etc/docker/daemon.json`来使用加速器，加速器地址可以在自己阿里云账号里面看到

```
$vi /etc/docker/daemon.json
{
  "registry-mirrors": ["https://woomhbbx.mirror.aliyuncs.com"]
}
$sudo systemctl daemon-reload
$sudo systemctl restart docker123456
```

# 3 开放管理端口映射

管理端口在 /lib/systemd/system/docker.service 文件中,将其中第11行的 ExecStart=/usr/bin/dockerd 替换为：

```
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock -H tcp://0.0.0.0:76541
```

**备注：**#此处默认2375为主管理端口，unix:///var/run/docker.sock用于本地管理，7654是备用的端口

将管理地址写入 /etc/profile   

```
$echo 'export DOCKER_HOST=tcp://0.0.0.0:2375' >> /etc/profile  
$source /etc/profile  
$systemctl daemon-reload && service docker restart  123
```

**备注：**systemctl daemon-reload  #重新载入 systemd，扫描新的或有变动的单元

# 4 测试docker

```
$sudo docker run hello-world 
#若成功，显示：
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
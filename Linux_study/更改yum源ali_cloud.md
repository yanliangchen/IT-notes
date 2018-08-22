# Centos-7修改yum源为国内的yum源	

 

国外地址yum源下载慢,下到一半就断了,就这个原因就修改它为国内yum源地址

 

国内也就是ali 与 网易

 

以centos7为例 ,以 修改为阿里的yum源

 

1.备份本地yum源

 **mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak** 

 

2.获取阿里yum源配置文件

 **wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo** 

 

3.更新cache并删除之前的cache

 **yum  clean all**

 **yum makecache** 

 

4.查看

 **yum -y update** 

 

5.最后你就可以链接国内镜像了,其实就是那个什么城XXX的 。。。

 

mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak 



wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 



yum makecache 



yum -y update 
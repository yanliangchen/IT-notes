## 关于k8s各种组建原理介绍（包括本文的单点安装，请看此连接）

参考 https://k8s.abcdocker.com/kubernetes_introduce.html



## kubernetes 安装

### kubernetes  单点安装

#### 一.环境准备

1.**不使用集群版本安装,使用单点安装。**

前面的ip是官方给的/后面的ip为本次我的演练。

|             IP             | 主机名 | 节点   |                             服务                             |
| :------------------------: | :----: | ------ | :----------------------------------------------------------: |
| 192.168.60.24/114.67.23.24 | master | master | etcd、kube-apiserver、kube-controller-manage、kube-scheduler 如果master上不安装Node可以不安装以下服务docker、kubelet、kube-proxy |
| 192.168.60.25/114.67.23.22 |  node  | node   |                 docker、kubelet、kube-proxy                  |

**Kubernetes版本 :** 本次版本采用v1.11



2.**查看系统及内核版本**

  

```
➜ cat /etc/redhat-release
CentOS Linux release 7.4.1708 (Core)

➜ uname -a
3.10.0-327.22.2.el7.x86_64 #1 SMP Thu Jun 23 17:05:11 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

#我们要升级内核版本

➜升级centos版本内核

这个包中其实并没有 xen 的工具，只是一个内核而已。安装这个包就能将 linux 内核升级到高版本。
yum install centos-release-xen
yum update

#重启reboot，然后检查一下就会发现内核版本已经到了比如 
➜uname -r 
4.9.58-29.el6.x86_64

```



**温馨提示：下面的操作需要在两台服务器上执行**



3.**设置主机名**

```
➜ hostnamectl set-hostname [master|node]
#刷新一下
➜ bash
```



4.**master 设置互信**

//或者手动

```
➜ yum install expect wget -y
➜ for i in 192.168.60.25;do
ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa
expect -c "
spawn ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.60.25
        expect {
                \"*yes/no*\" {send \"yes\r\"; exp_continue}
                \"*password*\" {send \"123456\r\"; exp_continue}
                \"*Password*\" {send \"123456\r\";}
        } "
done 
```



5.**设置时间同步**

```
 yum -y install ntp
 systemctl enable ntpd
 systemctl start ntpd
 ntpdate -u cn.pool.ntp.org
 hwclock --systohc
 timedatectl set-timezone Asia/Shanghai
```



6.**关闭swap分区**

```
➜ swapoff -a     #临时关闭swap分区
➜ vim /etc/fstab  #永久关闭swap分区
swap was on /dev/sda11 during installation
UUID=0a55fdb5-a9d8-4215-80f7-f42f75644f69 none  swap    sw      0       0
#注释掉SWAP分区项，即可
#不听我的kubelet启动报错自己百度
```



**7.关闭防火墙**

```
   //关闭防火墙
 systemctl stop firewalld
   //开机禁用防火墙
 systemctl disable firewalld
    // 执行setenforce 0 表示关闭selinux防火墙
 setenforce 0
    //关闭Linux里面的selinux
 sed -i '/SELINUX/s/enforcing/disabled/' /etc/selinux/config
```



8.**升级内核** 

```
不要问我为什么
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
yum --enablerepo=elrepo-kernel install kernel-ml -y&&
sed -i s/saved/0/g /etc/default/grub&&
grub2-mkconfig -o /boot/grub2/grub.cfg && reboot
```

  查看内核

```
➜ uname -a
Linux master 4.17.6-1.el7.elrepo.x86_64 #1 SMP Wed Jul 11 17:24:30 EDT 2018 x86_64 x86_64 x86_64 GNU/Linux
```


**9.设置内核参数**

解决办法

```
解决方法：
产生这个问题的原因是文件系统此时处于只读模式下，/etc/passwd和/etc/shadow不能被修改，运行下面的命令就可以解决这个问题
#mount -rw -o remount /
注：
  mount 是挂载命令
  -rw  是说指定的挂载文件是可读/写的
  -o remount / 是说重新挂载根
```

```
echo "* soft nofile 190000" >> /etc/security/limits.conf
echo "* hard nofile 200000" >> /etc/security/limits.conf
echo "* soft nproc 252144" >> /etc/security/limits.conf
echo "* hadr nproc 262144" >> /etc/security/limits.conf
tee /etc/sysctl.conf <<-'EOF'
# System default settings live in /usr/lib/sysctl.d/00-system.conf.
# To override those settings, enter new settings here, or in an /etc/sysctl.d/<name>.conf file
#
# For more information, see sysctl.conf(5) and sysctl.d(5).

net.ipv4.tcp_tw_recycle = 0
net.ipv4.ip_local_port_range = 10000 61000
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_fin_timeout = 30
net.ipv4.ip_forward = 1
net.core.netdev_max_backlog = 2000
net.ipv4.tcp_mem = 131072  262144  524288
net.ipv4.tcp_keepalive_intvl = 30
net.ipv4.tcp_keepalive_probes = 3
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_low_latency = 0
net.core.rmem_default = 256960
net.core.rmem_max = 513920
net.core.wmem_default = 256960
net.core.wmem_max = 513920
net.core.somaxconn = 2048
net.core.optmem_max = 81920
net.ipv4.tcp_mem = 131072  262144  524288
net.ipv4.tcp_rmem = 8760  256960  4088000
net.ipv4.tcp_wmem = 8760  256960  4088000
net.ipv4.tcp_keepalive_time = 1800
net.ipv4.tcp_sack = 1
net.ipv4.tcp_fack = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_syn_retries = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-arptables = 1
EOF
echo "options nf_conntrack hashsize=819200" >> /etc/modprobe.d/mlx4.conf 
modprobe br_netfilter
sysctl -p
```
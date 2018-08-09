## 关于k8s各种组建原理介绍（包括本文的单点安装，请看此连接）

参考 https://k8s.abcdocker.com/kubernetes_introduce.html



## kubernetes 安装

### kubernetes  单点安装

#### 一.环境准备

1.**不使用集群版本安装,使用单点安装。**

前面的ip是官方给的/后面的ip为本次我的演练改为ifconfig 机器里的innetip地址。

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



**设置host**

```
➜ echo "192.168.60.25 node" >>/etc/hosts
➜ echo "192.168.60.24 master" >>/etc/hosts
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



设置Yum源 

 

```
 curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
 wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
 yum makecache
 yum install wget vim lsof net-tools lrzsz -y
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
//中间有一个地方文件夹没找到，没关系的
sysctl -p
```


#### 二.Kubernetes Install

##### Master配置

###### 1.安装CFSSL工具

  

**工具说明：**
 **client certificate** 用于服务端认证客户端,例如etcdctl、etcd proxy、fleetctl、docker客户端
 **server certificate** 服务端使用，客户端以此验证服务端身份,例如docker服务端、kube-apiserver
 **peer certificate** 双向证书，用于etcd集群成员间通信



**安装CFSSL工具**

//遇到的问题

```
wget：无法解析主机地址。这就能看出是DNS解析的问题。 
解决办法： 
登入root（VPS）。 
进入/etc/resolv.conf。 
修改内容为下
nameserver 8.8.8.8 #google域名服务器
nameserver 8.8.4.4 #google域名服务器 
```



```
➜ wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64
chmod +x cfssl_linux-amd64
mv cfssl_linux-amd64 /usr/bin/cfssl

➜ wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64
chmod +x cfssljson_linux-amd64
mv cfssljson_linux-amd64 /usr/bin/cfssljson

➜ wget https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64
chmod +x cfssl-certinfo_linux-amd64
mv cfssl-certinfo_linux-amd64 /usr/bin/cfssl-certinfo
```



###### 2.生成ETCD证书

etcd作为Kubernetes集群的主数据库，在安装Kubernetes各服务之前需要首先安装和启动

**创建CA证书**

```
#创建etcd目录，用户生成etcd证书，请步骤和我保持一致
➜ mkdir /root/etcd_ssl && cd /root/etcd_ssl

cat > etcd-root-ca-csr.json << EOF
{
  "key": {
    "algo": "rsa",
    "size": 4096
  },
  "names": [
    {
      "O": "etcd",
      "OU": "etcd Security",
      "L": "beijing",
      "ST": "beijing",
      "C": "CN"
    }
  ],
  "CN": "etcd-root-ca"
}
EOF
```



**etcd集群证书**

```
cat >  etcd-gencert.json << EOF  
{                                 
  "signing": {                    
    "default": {                  
      "expiry": "87600h"           
    },                            
    "profiles": {                 
      "etcd": {             
        "usages": [               
            "signing",            
            "key encipherment",   
            "server auth", 
            "client auth"  
        ],  
        "expiry": "87600h"  
      }  
    }  
  }  
}  
EOF
```

```
# 过期时间设置成了 87600h
ca-config.json：可以定义多个 profiles，分别指定不同的过期时间、使用场景等参数；后续在签名证书时使用某个 profile；
signing：表示该证书可用于签名其它证书；生成的 ca.pem 证书中 CA=TRUE；
server auth：表示client可以用该 CA 对server提供的证书进行验证；
client auth：表示server可以用该CA对client提供的证书进行验证；
```



**etcd证书签名请求**

```
cat > etcd-csr.json << EOF
{
  "key": {
    "algo": "rsa",
    "size": 4096
  },
  "names": [
    {
      "O": "etcd",
      "OU": "etcd Security",
      "L": "beijing",
      "ST": "beijing",
      "C": "CN"
    }
  ],
  "CN": "etcd",
  "hosts": [
    "127.0.0.1",
    "localhost",
    "192.168.60.24"
  ]
}
EOF

//改192.168.60.24那一个  给改成ifconfig 里面的172.31.0.6
$ hosts写master地址
```



**生成证书**

```
cfssl gencert --initca=true etcd-root-ca-csr.json \
| cfssljson --bare etcd-root-ca
```



**创建根CA**

```
cfssl gencert --ca etcd-root-ca.pem \
--ca-key etcd-root-ca-key.pem \
--config etcd-gencert.json \
-profile=etcd etcd-csr.json | cfssljson --bare etcd
```



**ETCD所需证书如下**

```
➜ ll
total 36
-rw-r--r-- 1 root root 1765 Jul 12 10:48 etcd.csr
-rw-r--r-- 1 root root  282 Jul 12 10:48 etcd-csr.json
-rw-r--r-- 1 root root  471 Jul 12 10:48 etcd-gencert.json
-rw------- 1 root root 3243 Jul 12 10:48 etcd-key.pem
-rw-r--r-- 1 root root 2151 Jul 12 10:48 etcd.pem
-rw-r--r-- 1 root root 1708 Jul 12 10:48 etcd-root-ca.csr
-rw-r--r-- 1 root root  218 Jul 12 10:48 etcd-root-ca-csr.json
-rw------- 1 root root 3243 Jul 12 10:48 etcd-root-ca-key.pem
-rw-r--r-- 1 root root 2078 Jul 12 10:48 etcd-root-ca.pem
```



###### 3.安装启动ETCD

ETCD 只有apiserver和Controller Manager需要连接

`yum install etcd -y` && 上传rpm包，使用rpm -ivh 安装

```
分发etcd证书
 ➜ mkdir -p /etc/etcd/ssl && cd /root/etcd_ssl

查看etcd证书
➜ ll /root/etcd_ssl/
total 36
-rw-r--r--. 1 root root 1765 Jul 20 10:46 etcd.csr
-rw-r--r--. 1 root root  282 Jul 20 10:42 etcd-csr.json
-rw-r--r--. 1 root root  471 Jul 20 10:40 etcd-gencert.json
-rw-------. 1 root root 3243 Jul 20 10:46 etcd-key.pem
-rw-r--r--. 1 root root 2151 Jul 20 10:46 etcd.pem
-rw-r--r--. 1 root root 1708 Jul 20 10:46 etcd-root-ca.csr
-rw-r--r--. 1 root root  218 Jul 20 10:40 etcd-root-ca-csr.json
-rw-------. 1 root root 3243 Jul 20 10:46 etcd-root-ca-key.pem
-rw-r--r--. 1 root root 2078 Jul 20 10:46 etcd-root-ca.pem


复制证书到相关目录
\cp *.pem /etc/etcd/ssl/
chown -R etcd:etcd /etc/etcd/ssl
chown -R etcd:etcd /var/lib/etcd
chmod -R 644 /etc/etcd/ssl/
chmod 755 /etc/etcd/ssl/


配置修改ETCD-master配置
➜ cp /etc/etcd/etcd.conf{,.bak} && >/etc/etcd/etcd.conf

cat >/etc/etcd/etcd.conf <<EOF
# [member]
ETCD_NAME=etcd
ETCD_DATA_DIR="/var/lib/etcd/etcd.etcd"
ETCD_WAL_DIR="/var/lib/etcd/wal"
ETCD_SNAPSHOT_COUNT="100"
ETCD_HEARTBEAT_INTERVAL="100"
ETCD_ELECTION_TIMEOUT="1000"
ETCD_LISTEN_PEER_URLS="https://192.168.60.24:2380"
ETCD_LISTEN_CLIENT_URLS="https://192.168.60.24:2379,http://127.0.0.1:2379"
ETCD_MAX_SNAPSHOTS="5"
ETCD_MAX_WALS="5"
#ETCD_CORS=""

# [cluster]
ETCD_INITIAL_ADVERTISE_PEER_URLS="https://192.168.60.24:2380"
# if you use different ETCD_NAME (e.g. test), set ETCD_INITIAL_CLUSTER value for this name, i.e. "test=http://..."
ETCD_INITIAL_CLUSTER="etcd=https://192.168.60.24:2380"
ETCD_INITIAL_CLUSTER_STATE="new"
ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster"
ETCD_ADVERTISE_CLIENT_URLS="https://192.168.60.24:2379"
#ETCD_DISCOVERY=""
#ETCD_DISCOVERY_SRV=""
#ETCD_DISCOVERY_FALLBACK="proxy"
#ETCD_DISCOVERY_PROXY=""
#ETCD_STRICT_RECONFIG_CHECK="false"
#ETCD_AUTO_COMPACTION_RETENTION="0"

# [proxy]
#ETCD_PROXY="off"
#ETCD_PROXY_FAILURE_WAIT="5000"
#ETCD_PROXY_REFRESH_INTERVAL="30000"
#ETCD_PROXY_DIAL_TIMEOUT="1000"
#ETCD_PROXY_WRITE_TIMEOUT="5000"
#ETCD_PROXY_READ_TIMEOUT="0"

# [security]
ETCD_CERT_FILE="/etc/etcd/ssl/etcd.pem"
ETCD_KEY_FILE="/etc/etcd/ssl/etcd-key.pem"
ETCD_CLIENT_CERT_AUTH="true"
ETCD_TRUSTED_CA_FILE="/etc/etcd/ssl/etcd-root-ca.pem"
ETCD_AUTO_TLS="true"
ETCD_PEER_CERT_FILE="/etc/etcd/ssl/etcd.pem"
ETCD_PEER_KEY_FILE="/etc/etcd/ssl/etcd-key.pem"
ETCD_PEER_CLIENT_CERT_AUTH="true"
ETCD_PEER_TRUSTED_CA_FILE="/etc/etcd/ssl/etcd-root-ca.pem"
ETCD_PEER_AUTO_TLS="true"

# [logging]
#ETCD_DEBUG="false"
# examples for -log-package-levels etcdserver=WARNING,security=DEBUG
#ETCD_LOG_PACKAGE_LEVELS=""
EOF

###需要将192.168.60.24修改成master的地址
```



**启动etcd**

```
systemctl daemon-reload
systemctl restart etcd
systemctl enable etcd
```

测试是否可以使用 

```
[root@master ~]#export ETCDCTL_API=3
//注意这里地址别忘记来看
[root@master ~]#etcdctl --cacert=/etc/etcd/ssl/etcd-root-ca.pem --cert=/etc/etcd/ssl/etcd.pem --key=/etc/etcd/ssl/etcd-key.pem --endpoints=https://192.168.60.24:2379 endpoint health
```

可用状态如下:

```
[root@master ~]# export ETCDCTL_API=3
[root@master ~]# etcdctl --cacert=/etc/etcd/ssl/etcd-root-ca.pem --cert=/etc/etcd/ssl/etcd.pem --key=/etc/etcd/ssl/etcd-key.pem --endpoints=https://192.168.60.24:2379 endpoint health
https://192.168.60.24:2379 is healthy: successfully committed proposal: took = 643.432µs
```

查看2379 ETCD端口

```
➜ netstat -lntup
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.60.24:2379      0.0.0.0:*               LISTEN      2016/etcd           
tcp        0      0 127.0.0.1:2379          0.0.0.0:*               LISTEN      2016/etcd           
tcp        0      0 192.168.60.24:2380      0.0.0.0:*               LISTEN      2016/etcd           
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      965/sshd            
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1081/master         
tcp6       0      0 :::22                   :::*                    LISTEN      965/sshd            
tcp6       0      0 ::1:25                  :::*                    LISTEN      1081/master         
udp        0      0 127.0.0.1:323           0.0.0.0:*                           721/chronyd         
udp6       0      0 ::1:323                 :::*                                721/chronyd 
```

**#####以上ETCD安装并配置完成**





###### 4.安装Docker

下载Docker安装包

```
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-17.03.2.ce-1.el7.centos.x86_64.rpm
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch.rpm
```

由于网络经常超时，我们已经把镜像上传上去，可以直接下载我提供的安装包安装即可



**安装修改配置**

```
➜ yum install docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch.rpm -y
➜ yum install docker-ce-17.03.2.ce-1.el7.centos.x86_64.rpm -y

设置开机启动并启动docker
systemctl enable docker 
systemctl start docker 

替换docker相关配置
sed -i '/ExecStart=\/usr\/bin\/dockerd/i\ExecStartPost=\/sbin/iptables -I FORWARD -s 0.0.0.0\/0 -d 0.0.0.0\/0 -j ACCEPT' /usr/lib/systemd/system/docker.service
sed -i '/dockerd/s/$/ \-\-storage\-driver\=overlay2/g' /usr/lib/systemd/system/docker.service

重启docker
systemctl daemon-reload 
systemctl restart docker
```



###### 5.安装Kubernetes

命令行下载：

  

```
wget https://dl.k8s.io/v1.10.5/kubernetes-server-linux-amd64.tar.gz
```

  

Kubernetes配置

  

```
tar xf kubernetes-server-linux-amd64.tar.gz
for i in hyperkube kube-apiserver kube-scheduler kubelet kube-controller-manager kubectl kube-proxy;do
cp ./kubernetes/server/bin/$i /usr/bin/
chmod 755 /usr/bin/$i
done
```



###### 6.生成分发Kubernetes证书

  

设置证书目录

  

```
mkdir /root/kubernets_ssl && cd /root/kubernets_ssl 
```

  

k8s-root-ca-csr.json证书

  

```
cat > k8s-root-ca-csr.json << EOF
{
  "CN": "kubernetes",
  "key": {
    "algo": "rsa",
    "size": 4096
  },
  "names": [
    {
      "C": "CN",
      "ST": "BeiJing",
      "L": "BeiJing",
      "O": "k8s",
      "OU": "System"
    }
  ]
}
EOF
```

k8s-gencert.json证书

```
cat >  k8s-gencert.json << EOF
{
  "signing": {
    "default": {
      "expiry": "87600h"
    },
    "profiles": {
      "kubernetes": {
        "usages": [
            "signing",
            "key encipherment",
            "server auth",
            "client auth"
        ],
        "expiry": "87600h"
      }
    }
  }
}
EOF
```

kubernetes-csr.json 证书

> $ hosts字段填写上所有你要用到的节点ip(master)，创建 kubernetes 证书签名请求文件 kubernetes-csr.json：

```
cat >kubernetes-csr.json << EOF
{
    "CN": "kubernetes",
    "hosts": [
        "127.0.0.1",
        "10.254.0.1",
        "192.168.60.24",
        "localhost",
        "kubernetes",
        "kubernetes.default",
        "kubernetes.default.svc",
        "kubernetes.default.svc.cluster",
        "kubernetes.default.svc.cluster.local"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "ST": "BeiJing",
            "L": "BeiJing",
            "O": "k8s",
            "OU": "System"
        }
    ]
}
EOF
```

kube-proxy-csr.json 证书

```
cat > kube-proxy-csr.json << EOF
{
  "CN": "system:kube-proxy",
  "hosts": [],
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "ST": "BeiJing",
      "L": "BeiJing",
      "O": "k8s",
      "OU": "System"
    }
  ]
}
EOF
```

admin-csr.json证书

```
cat > admin-csr.json << EOF
{
  "CN": "admin",
  "hosts": [],
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "ST": "BeiJing",
      "L": "BeiJing",
      "O": "system:masters",
      "OU": "System"
    }
  ]
}
EOF
```

**生成Kubernetes证书**

```
➜ cfssl gencert --initca=true k8s-root-ca-csr.json | cfssljson --bare k8s-root-ca

➜ for targetName in kubernetes admin kube-proxy; do
    cfssl gencert --ca k8s-root-ca.pem --ca-key k8s-root-ca-key.pem --config k8s-gencert.json --profile kubernetes $targetName-csr.json | cfssljson --bare $targetName
done
```

**#生成boostrap配置**

```
export KUBE_APISERVER="https://127.0.0.1:6443"
export BOOTSTRAP_TOKEN=$(head -c 16 /dev/urandom | od -An -t x | tr -d ' ')
echo "Tokne: ${BOOTSTRAP_TOKEN}"
cat > token.csv <<EOF
${BOOTSTRAP_TOKEN},kubelet-bootstrap,10001,"system:kubelet-bootstrap"
EOF
```

 

 

------

**配置证书信息**

> \# Master 上该地址应为 <https://MasterIP:6443>

进入Kubernetes证书目录/root/kubernetes_ssl

```
export KUBE_APISERVER="https://127.0.0.1:6443"
```

\# 设置集群参数

```
kubectl config set-cluster kubernetes \
  --certificate-authority=k8s-root-ca.pem \
  --embed-certs=true \
  --server=${KUBE_APISERVER} \
  --kubeconfig=bootstrap.kubeconfig
```

\# 设置客户端认证参数

```
kubectl config set-credentials kubelet-bootstrap \
  --token=${BOOTSTRAP_TOKEN} \
  --kubeconfig=bootstrap.kubeconfig
```

\# 设置上下文参数

```
kubectl config set-context default \
  --cluster=kubernetes \
  --user=kubelet-bootstrap \
  --kubeconfig=bootstrap.kubeconfig
```

\# 设置默认上下文

```
kubectl config use-context default --kubeconfig=bootstrap.kubeconfig
```

\# echo "Create kube-proxy kubeconfig..."

```
kubectl config set-cluster kubernetes \
  --certificate-authority=k8s-root-ca.pem \
  --embed-certs=true \
  --server=${KUBE_APISERVER} \
  --kubeconfig=kube-proxy.kubeconfig
```

\# kube-proxy

```
kubectl config set-credentials kube-proxy \
  --client-certificate=kube-proxy.pem \
  --client-key=kube-proxy-key.pem \
  --embed-certs=true \
  --kubeconfig=kube-proxy.kubeconfig
```

\# kube-proxy_config

```
kubectl config set-context default \
  --cluster=kubernetes \
  --user=kube-proxy \
  --kubeconfig=kube-proxy.kubeconfig 
kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
```

\# 生成高级审计配置

```
cat >> audit-policy.yaml <<EOF
# Log all requests at the Metadata level.
apiVersion: audit.k8s.io/v1beta1
kind: Policy
rules:
- level: Metadata
EOF
```

\#分发kubernetes证书#####

```
cd /root/kubernets_ssl
mkdir -p /etc/kubernetes/ssl
cp *.pem /etc/kubernetes/ssl
\cp *.kubeconfig token.csv audit-policy.yaml /etc/kubernetes
useradd -s /sbin/nologin -M kube
chown -R kube:kube /etc/kubernetes/ssl
```

\# 生成kubectl的配置

```
cd /root/kubernets_ssl
kubectl config set-cluster kubernetes \
  --certificate-authority=/etc/kubernetes/ssl/k8s-root-ca.pem \
  --embed-certs=true \
  --server=https://127.0.0.1:6443

  
  
kubectl config set-credentials admin \
  --client-certificate=/etc/kubernetes/ssl/admin.pem \
  --embed-certs=true \
  --client-key=/etc/kubernetes/ssl/admin-key.pem

  
kubectl config set-context kubernetes \
  --cluster=kubernetes \
  --user=admin

  
kubectl config use-context kubernetes
```

\# 设置 log 目录权限

```
mkdir -p /var/log/kube-audit /usr/libexec/kubernetes
chown -R kube:kube /var/log/kube-audit /usr/libexec/kubernetes
chmod -R 755 /var/log/kube-audit /usr/libexec/kubernetes
```

 

 

------

###### 7.master节点配置

证书与 rpm 都安装完成后，只需要修改配置(配置位于 /etc/kubernetes 目录)后启动相关组件即可

```
cd /etc/kubernetes
```

config 通用配置

```
cat > /etc/kubernetes/config <<EOF
###
# kubernetes system config
#
# The following values are used to configure various aspects of all
# kubernetes services, including
#
#   kube-apiserver.service
#   kube-controller-manager.service
#   kube-scheduler.service
#   kubelet.service
#   kube-proxy.service
# logging to stderr means we get it in the systemd journal
KUBE_LOGTOSTDERR="--logtostderr=true"

# journal message level, 0 is debug
KUBE_LOG_LEVEL="--v=2"

# Should this cluster be allowed to run privileged docker containers
KUBE_ALLOW_PRIV="--allow-privileged=true"

# How the controller-manager, scheduler, and proxy find the apiserver
KUBE_MASTER="--master=http://127.0.0.1:8080"
EOF
```

apiserver 配置

```
cat > /etc/kubernetes/apiserver <<EOF
###
# kubernetes system config
#
# The following values are used to configure the kube-apiserver
#

# The address on the local server to listen to.
KUBE_API_ADDRESS="--advertise-address=0.0.0.0 --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0"

# The port on the local server to listen on.
KUBE_API_PORT="--insecure-port=8080 --secure-port=6443"

# Port minions listen on
# KUBELET_PORT="--kubelet-port=10250"

# Comma separated list of nodes in the etcd cluster
KUBE_ETCD_SERVERS=--etcd-servers=https://192.168.60.24:2379 ##etcd地址

# Address range to use for services
KUBE_SERVICE_ADDRESSES="--service-cluster-ip-range=10.254.0.0/16"

# default admission control policies
KUBE_ADMISSION_CONTROL="--admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,ResourceQuota,NodeRestriction"

# Add your own!
KUBE_API_ARGS="--authorization-mode=RBAC,Node \
               --endpoint-reconciler-type=lease \
               --runtime-config=batch/v2alpha1=true \
               --anonymous-auth=false \
               --kubelet-https=true \
               --enable-bootstrap-token-auth \
               --token-auth-file=/etc/kubernetes/token.csv \
               --service-node-port-range=30000-50000 \
               --tls-cert-file=/etc/kubernetes/ssl/kubernetes.pem \
               --tls-private-key-file=/etc/kubernetes/ssl/kubernetes-key.pem \
               --client-ca-file=/etc/kubernetes/ssl/k8s-root-ca.pem \
               --service-account-key-file=/etc/kubernetes/ssl/k8s-root-ca-key.pem \
               --etcd-quorum-read=true \
               --storage-backend=etcd3 \
               --etcd-cafile=/etc/etcd/ssl/etcd-root-ca.pem \
               --etcd-certfile=/etc/etcd/ssl/etcd.pem \
               --etcd-keyfile=/etc/etcd/ssl/etcd-key.pem \
               --enable-swagger-ui=true \
               --apiserver-count=3 \
               --audit-policy-file=/etc/kubernetes/audit-policy.yaml \
               --audit-log-maxage=30 \
               --audit-log-maxbackup=3 \
               --audit-log-maxsize=100 \
               --audit-log-path=/var/log/kube-audit/audit.log \
               --event-ttl=1h "
EOF

#需要修改的地址是etcd的，集群因逗号为分隔符填写
```

controller-manager 配置

```
cat > /etc/kubernetes/controller-manager <<EOF
###
# The following values are used to configure the kubernetes controller-manager

# defaults from config and apiserver should be adequate

# Add your own!
KUBE_CONTROLLER_MANAGER_ARGS="--address=0.0.0.0 \
                              --service-cluster-ip-range=10.254.0.0/16 \
                              --cluster-name=kubernetes \
                              --cluster-signing-cert-file=/etc/kubernetes/ssl/k8s-root-ca.pem \
                              --cluster-signing-key-file=/etc/kubernetes/ssl/k8s-root-ca-key.pem \
                              --service-account-private-key-file=/etc/kubernetes/ssl/k8s-root-ca-key.pem \
                              --root-ca-file=/etc/kubernetes/ssl/k8s-root-ca.pem \
                              --leader-elect=true \
                              --node-monitor-grace-period=40s \
                              --node-monitor-period=5s \
                              --pod-eviction-timeout=60s"
EOF
```

scheduler 配置

```
cat >scheduler <<EOF
###
# kubernetes scheduler config

# default config should be adequate

# Add your own!
KUBE_SCHEDULER_ARGS="--leader-elect=true --address=0.0.0.0"
EOF
```

**设置服务启动脚本**
Kubernetes服务的组件配置已经生成，接下来我们配置组件的启动脚本
\###kube-apiserver.service服务脚本###

```
vim /usr/lib/systemd/system/kube-apiserver.service

[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.target
After=etcd.service

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/apiserver
User=root
ExecStart=/usr/bin/kube-apiserver \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBE_ETCD_SERVERS \
        $KUBE_API_ADDRESS \
        $KUBE_API_PORT \
        $KUBELET_PORT \
        $KUBE_ALLOW_PRIV \
        $KUBE_SERVICE_ADDRESSES \
        $KUBE_ADMISSION_CONTROL \
        $KUBE_API_ARGS
Restart=on-failure
Type=notify
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

\###kube-controller-manager.service服务脚本###

```
vim /usr/lib/systemd/system/kube-controller-manager.service

[Unit]
Description=Kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/controller-manager
User=root
ExecStart=/usr/bin/kube-controller-manager \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBE_MASTER \
        $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

\###kube-scheduler.service服务脚本###

```
vim /usr/lib/systemd/system/kube-scheduler.service

[Unit]
Description=Kubernetes Scheduler Plugin
Documentation=https://github.com/GoogleCloudPlatform/kubernetes

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/scheduler
User=root
ExecStart=/usr/bin/kube-scheduler \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBE_MASTER \
        $KUBE_SCHEDULER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

启动kube-apiserver、kube-controller-manager、kube-schedule

```
systemctl daemon-reload
systemctl start kube-apiserver
systemctl start kube-controller-manager
systemctl start kube-scheduler


设置开机启动
systemctl enable kube-apiserver
systemctl enable kube-controller-manager
systemctl enable kube-scheduler
```

提示：kube-apiserver是主要服务，如果apiserver启动失败其他的也会失败

验证是否成功

```
[root@master system]# kubectl get cs
NAME                 STATUS    MESSAGE              ERROR
controller-manager   Healthy   ok                   
scheduler            Healthy   ok                   
etcd-0               Healthy   {"health": "true"} 
```

\#创建ClusterRoleBinding
由于 kubelet 采用了 TLS Bootstrapping，所有根绝 RBAC 控制策略，kubelet 使用的用户 kubelet-bootstrap 是不具备任何访问 API 权限的
这是需要预先在集群内创建 ClusterRoleBinding 授予其 system:node-bootstrapper Role

```
kubectl create clusterrolebinding kubelet-bootstrap \
  --clusterrole=system:node-bootstrapper \
  --user=kubelet-bootstrap
  
  
删除命令
kubectl delete  clusterrolebinding kubelet-bootstrap
```

###### 8.Master 上安装node节点

对于node节点，master也可以进行安装

master上node节点安装kube-proxy、kubelet

```
######Kuberlet配置

cat >/etc/kubernetes/kubelet <<EOF
###
# kubernetes kubelet (minion) config

# The address for the info server to serve on (set to 0.0.0.0 or "" for all interfaces)
KUBELET_ADDRESS="--address=192.168.60.24"

# The port for the info server to serve on
# KUBELET_PORT="--port=10250"

# You may leave this blank to use the actual hostname
KUBELET_HOSTNAME="--hostname-override=master"

# location of the api-server
# KUBELET_API_SERVER=""

# Add your own!
KUBELET_ARGS="--cgroup-driver=cgroupfs \
              --cluster-dns=10.254.0.2 \
              --resolv-conf=/etc/resolv.conf \
              --experimental-bootstrap-kubeconfig=/etc/kubernetes/bootstrap.kubeconfig \
              --kubeconfig=/etc/kubernetes/kubelet.kubeconfig \
              --cert-dir=/etc/kubernetes/ssl \
              --cluster-domain=cluster.local. \
              --hairpin-mode promiscuous-bridge \
              --serialize-image-pulls=false \
              --pod-infra-container-image=gcr.io/google_containers/pause-amd64:3.0"
EOF


将IP地址修改为master上的IP地址和主机名，其他不需要修改
```

创建服务脚本
\###kubelet.service服务脚本###
文件名称：kubelet.service

```
vim /usr/lib/systemd/system/kubelet.service

[Unit]
Description=Kubernetes Kubelet Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=docker.service
Requires=docker.service

[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBELET_API_SERVER \
        $KUBELET_ADDRESS \
        $KUBELET_PORT \
        $KUBELET_HOSTNAME \
        $KUBE_ALLOW_PRIV \
        $KUBELET_ARGS
Restart=on-failure
KillMode=process

[Install]
WantedBy=multi-user.target
```

创建工程目录

```
/var/lib/kubelet    这个目录如果没有需要我们手动创建
mkdir /var/lib/kubelet -p
```

\#kube-proxy配置

```
cat >/etc/kubernetes/proxy <<EOF
###
# kubernetes proxy config

# default config should be adequate

# Add your own!
KUBE_PROXY_ARGS="--bind-address=192.168.60.24 \
                 --hostname-override=master \
                 --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig \
                 --cluster-cidr=10.254.0.0/16"
EOF

#master ip && name
```

kube-proxy启动脚本
路径：/usr/lib/systemd/system/kube-proxy.service

```
[Unit]
Description=Kubernetes Kube-Proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.target

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/proxy
ExecStart=/usr/bin/kube-proxy \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBE_MASTER \
        $KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

**启动kubelet and Kube-proxy**

```
systemctl daemon-reload
systemctl restart kube-proxy
systemctl restart kubelet
```



#####  Node节点配置

###### 	1.Docker安装

```
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-17.03.2.ce-1.el7.centos.x86_64.rpm
wget https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch.rpm

yum install docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch.rpm -y
yum install docker-ce-17.03.2.ce-1.el7.centos.x86_64.rpm -y

systemctl enable docker 
systemctl start docker 

sed -i '/ExecStart=\/usr\/bin\/dockerd/i\ExecStartPost=\/sbin/iptables -I FORWARD -s 0.0.0.0\/0 -d 0.0.0.0\/0 -j ACCEPT' /usr/lib/systemd/system/docker.service
sed -i '/dockerd/s/$/ \-\-storage\-driver\=overlay2/g' /usr/lib/systemd/system/docker.service

systemctl daemon-reload 
systemctl restart docker
```

###### 2.分配证书

  

我们需要去Master上分配证书`kubernetes``etcd`给Node
 虽然 Node 节点上没有 Etcd，但是如果部署网络组件，如 calico、flannel 等时，网络组件需要联通 Etcd 就会用到 Etcd 的相关证书。

> 从Mster节点上将hyperkuber kubelet kubectl kube-proxy 拷贝至node上

  

```
for i in hyperkube kubelet kubectl kube-proxy;do
scp ./kubernetes/server/bin/$i 192.168.60.25:/usr/bin/
ssh 192.168.60.25 chmod 755 /usr/bin/$i
done

##这里的IP是node节点ip
进入到K8S二进制目录下，for循环看不懂就别玩K8s了
```



分发K8s证书
 cd K8S证书目录

```
cd /root/kubernets_ssl/
for IP in 192.168.60.25;do
    ssh $IP mkdir -p /etc/kubernetes/ssl
    scp *.pem $IP:/etc/kubernetes/ssl
    scp *.kubeconfig token.csv audit-policy.yaml $IP:/etc/kubernetes
    ssh $IP useradd -s /sbin/nologin/ kube
    ssh $IP chown -R kube:kube /etc/kubernetes/ssl
done
```



分发ETCD证书

```
for IP in 192.168.60.25;do
    cd /root/etcd_ssl
    ssh $IP mkdir -p /etc/etcd/ssl
    scp *.pem $IP:/etc/etcd/ssl
    ssh $IP chmod -R 644 /etc/etcd/ssl/*
    ssh $IP chmod 755 /etc/etcd/ssl
done
```

给Node设置文件权限

```
ssh root@192.168.60.25 mkdir -p /var/log/kube-audit /usr/libexec/kubernetes &&
ssh root@192.168.60.25 chown -R kube:kube /var/log/kube-audit /usr/libexec/kubernetes &&
ssh root@192.168.60.25 chmod -R 755 /var/log/kube-audit /usr/libexec/kubernetes
```

###### 3.Node节点配置

node 节点上配置文件同样位于 /etc/kubernetes 目录
node 节点只需要修改 `config` `kubelet` `proxy`这三个配置文件，修改如下

\#config 通用配置

注意: config 配置文件(包括下面的 kubelet、proxy)中全部未 定义 API Server 地址，因为 kubelet 和 kube-proxy 组件启动时使用了 --require-kubeconfig 选项，该选项会使其从 *.kubeconfig 中读取 API Server 地址，而忽略配置文件中设置的；
所以配置文件中设置的地址其实是无效的

```
cat > /etc/kubernetes/config <<EOF
###
# kubernetes system config
#
# The following values are used to configure various aspects of all
# kubernetes services, including
#
#   kube-apiserver.service
#   kube-controller-manager.service
#   kube-scheduler.service
#   kubelet.service
#   kube-proxy.service
# logging to stderr means we get it in the systemd journal
KUBE_LOGTOSTDERR="--logtostderr=true"

# journal message level, 0 is debug
KUBE_LOG_LEVEL="--v=2"

# Should this cluster be allowed to run privileged docker containers
KUBE_ALLOW_PRIV="--allow-privileged=true"

# How the controller-manager, scheduler, and proxy find the apiserver
# KUBE_MASTER="--master=http://127.0.0.1:8080"
EOF
```

\# kubelet 配置

```
cat >/etc/kubernetes/kubelet <<EOF
###
# kubernetes kubelet (minion) config

# The address for the info server to serve on (set to 0.0.0.0 or "" for all interfaces)
KUBELET_ADDRESS="--address=192.168.60.25"

# The port for the info server to serve on
# KUBELET_PORT="--port=10250"

# You may leave this blank to use the actual hostname
KUBELET_HOSTNAME="--hostname-override=node"

# location of the api-server
# KUBELET_API_SERVER=""

# Add your own!
KUBELET_ARGS="--cgroup-driver=cgroupfs \
              --cluster-dns=10.254.0.2 \
              --resolv-conf=/etc/resolv.conf \
              --experimental-bootstrap-kubeconfig=/etc/kubernetes/bootstrap.kubeconfig \
              --kubeconfig=/etc/kubernetes/kubelet.kubeconfig \
              --cert-dir=/etc/kubernetes/ssl \
              --cluster-domain=cluster.local. \
              --hairpin-mode promiscuous-bridge \
              --serialize-image-pulls=false \
              --pod-infra-container-image=gcr.io/google_containers/pause-amd64:3.0"
EOF

#这里的IP地址是node的IP地址和主机名
```

复制启动脚本
存放路径[/usr/lib/systemd/system/kubelet.service]

```
[Unit]
Description=Kubernetes Kubelet Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=docker.service
Requires=docker.service

[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBELET_API_SERVER \
        $KUBELET_ADDRESS \
        $KUBELET_PORT \
        $KUBELET_HOSTNAME \
        $KUBE_ALLOW_PRIV \
        $KUBELET_ARGS
Restart=on-failure
KillMode=process

[Install]
WantedBy=multi-user.target
```

`mkdir /var/lib/kubelet -p`
工程目录我们设置在/var/lib/kubele需要我们手动创建

启动kubelet

```
sed -i 's#127.0.0.1#192.168.60.24#g' /etc/kubernetes/bootstrap.kubeconfig
#这里的地址是master地址

systemctl daemon-reload
systemctl restart kubelet
systemctl enable kubelet
```

\#修改kube-proxy配置

```
cat >/etc/kubernetes/proxy <<EOF
###
# kubernetes proxy config

# default config should be adequate

# Add your own!
KUBE_PROXY_ARGS="--bind-address=192.168.60.25 \
                 --hostname-override=node \
                 --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig \
                 --cluster-cidr=10.254.0.0/16"
EOF
```

kube-proxy启动脚本
路径：/usr/lib/systemd/system/kube-proxy.service

```
[Unit]
Description=Kubernetes Kube-Proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.target

[Service]
EnvironmentFile=-/etc/kubernetes/config
EnvironmentFile=-/etc/kubernetes/proxy
ExecStart=/usr/bin/kube-proxy \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBE_MASTER \
        $KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

###### 4.创建 nginx 代理

此时所有 node 应该连接本地的 nginx 代理，然后 nginx 来负载所有 api server；以下为 nginx 代理相关配置
我们也可以不用nginx代理。需要修改 `bootstrap.kubeconfig` `kube-proxy.kubeconfig`中的 API Server 地址即可

> 注意: 对于在 master 节点启动 kubelet 来说，不需要 nginx 做负载均衡；可以跳过此步骤，并修改 kubelet.kubeconfig、kube-proxy.kubeconfig 中的 apiserver 地址为当前 master ip 6443 端口即可

\# 创建配置目录

```
mkdir -p /etc/nginx
```

\# 写入代理配置

```
cat > /etc/nginx/nginx.conf <<EOF
error_log stderr notice;

worker_processes auto;
events {
  multi_accept on;
  use epoll;
  worker_connections 1024;
}

stream {
    upstream kube_apiserver {
        least_conn;
        server 192.168.60.24:6443 weight=20 max_fails=1 fail_timeout=10s;
        #server中代理master的IP
    }

    server {
        listen        0.0.0.0:6443;
        proxy_pass    kube_apiserver;
        proxy_timeout 10m;
        proxy_connect_timeout 1s;
    }
}
EOF

##servcer 中代理的ip应该是master中的apiserver端口
```

\# 更新权限

```
chmod +r /etc/nginx/nginx.conf
```

\#启动nginx的docker容器。运行转发

```
docker run -it -d -p 127.0.0.1:6443:6443 -v /etc/nginx:/etc/nginx  --name nginx-proxy --net=host --restart=on-failure:5 --memory=512M  nginx:1.13.5-alpine
```

为了保证 nginx 的可靠性，综合便捷性考虑，node 节点上的 nginx 使用 docker 启动，同时 使用 systemd 来守护， systemd 配置如下

```
cat >/etc/systemd/system/nginx-proxy.service <<EOF 
[Unit]
Description=kubernetes apiserver docker wrapper
Wants=docker.socket
After=docker.service

[Service]
User=root
PermissionsStartOnly=true
ExecStart=/usr/bin/docker start nginx-proxy
Restart=always
RestartSec=15s
TimeoutStartSec=30s

[Install]
WantedBy=multi-user.target
EOF


➜ systemctl daemon-reload
➜ systemctl start nginx-proxy
➜ systemctl enable nginx-proxy
```

我们要确保有6443端口，才可以启动kubelet

```
sed -i 's#192.168.60.24#127.0.0.1#g' /etc/kubernetes/bootstrap.kubeconfig
```

查看6443端口

```
[root@node kubernetes]# netstat -lntup
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:10249         0.0.0.0:*               LISTEN      2042/kube-proxy     
tcp        0      0 0.0.0.0:6443            0.0.0.0:*               LISTEN      1925/nginx: master  
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      966/sshd            
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1050/master         
tcp6       0      0 :::10256                :::*                    LISTEN      2042/kube-proxy     
tcp6       0      0 :::22                   :::*                    LISTEN      966/sshd            
tcp6       0      0 ::1:25                  :::*                    LISTEN      1050/master         
udp        0      0 127.0.0.1:323           0.0.0.0:*                           717/chronyd         
udp6       0      0 ::1:323                 :::*                                717/chronyd  

[root@node kubernetes]# lsof -i:6443
lsof: no pwd entry for UID 100
lsof: no pwd entry for UID 100
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
kubelet 1765     root    3u  IPv4  27573      0t0  TCP node1:39246->master:sun-sr-https (ESTABLISHED)
nginx   1925     root    4u  IPv4  29028      0t0  TCP *:sun-sr-https (LISTEN)
lsof: no pwd entry for UID 100
nginx   1934      100    4u  IPv4  29028      0t0  TCP *:sun-sr-https (LISTEN)
lsof: no pwd entry for UID 100
nginx   1935      100    4u  IPv4  29028      0t0  TCP *:sun-sr-https (LISTEN)
```

启动kubelet-proxy
在启动kubelet之前最好将kube-proxy重启一下

```
systemctl restart kube-proxy
systemctl enable kubelet

systemctl daemon-reload
systemctl restart kubelet
systemctl enable kubelet
```

###### 5.认证

由于采用了 TLS Bootstrapping，所以 kubelet 启动后不会立即加入集群，而是进行证书申请，从日志中可以看到如下输出

```
7月 24 13:55:50 master kubelet[1671]: I0724 13:55:50.877027    1671 bootstrap.go:56] Using bootstrap kubeconfig to generate TLS client cert, key and kubeconfig file
```

此时只需要在 master 允许其证书申请即可
\# 查看 csr

```
➜  kubectl get csr
NAME        AGE       REQUESTOR           CONDITION
csr-l9d25   2m        kubelet-bootstrap   Pending
'

如果我们将2台都启动了kubelet都配置好了并且启动了，这里会显示2台，一个master一个node
```

\# 签发证书

```
➜  kubectl certificate approve csr-l9d25  或者执行kubectl get csr | grep Pending | awk '{print $1}' | xargs kubectl certificate approve
```

\# 查看 node



//到这出现了问题

签发完成证书

```
[root@master ~]# kubectl get nodes
NAME      STATUS    ROLES     AGE       VERSION
master    Ready     <none>    40m       v1.11.0
node      Ready     <none>    39m       v1.11.0
```

认证后自动生成了kubelet kubeconfig 文件和公私钥：

```
$ ls -l /etc/kubernetes/kubelet.kubeconfig
-rw------- 1 root root 2280 Nov  7 10:26 /etc/kubernetes/kubelet.kubeconfig
$ ls -l /etc/kubernetes/ssl/kubelet*
-rw-r--r-- 1 root root 1046 Nov  7 10:26 /etc/kubernetes/ssl/kubelet-client.crt
-rw------- 1 root root  227 Nov  7 10:22 /etc/kubernetes/ssl/kubelet-client.key
-rw-r--r-- 1 root root 1115 Nov  7 10:16 /etc/kubernetes/ssl/kubelet.crt
-rw------- 1 root root 1675 Nov  7 10:16 /etc/kubernetes/ssl/kubelet.key
```

> **#注意：**
> apiserver如果不启动后续没法操作
> kubelet里面配置的IP地址都是本机（master配置node）
> Node服务上先启动nginx-proxy在启动kube-proxy。kube-proxy里面地址配置本机127.0.0.1:6443实际上就是master:6443
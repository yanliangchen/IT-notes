### lsof

lsof（list open files）是一个列出当前系统打开文件的工具。在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。





1.**作用**

在终端下输入lsof即可显示系统打开的文件，因为 lsof 需要访问核心内存和各种文件，所以必须以 root 用户的身份运行它才能够充分地发挥其功能。



2.**显示示例**

```
显示示例
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
init     1   root cwd DIR 3,3   1024  2    /
init 1 root rtd DIR 3,3 1024 2 /
init 1 root txt REG 3,3 38432 1763452 /sbin/init
init 1 root mem REG 3,3 106114 1091620 /lib/libdl-2.6.so
init 1 root mem REG 3,3 7560696 1091614 /lib/libc-2.6.so
init 1 root mem REG 3,3 79460 1091669 /lib/libselinux.so.1
init 1 root mem REG 3,3 223280 1091668 /lib/libsepol.so.1
init 1 root mem REG 3,3 564136 1091607 /lib/ld-2.6.so
init 1 root 10u FIFO 0,15 1309 /dev/initctl

各列解释
每行显示一个打开的文件，若不指定条件默认将显示所有进程打开的所有文件。lsof输出各列信息的意义如下：
COMMAND：进程的名称
PID：进程标识符
USER：进程所有者
FD：文件描述符，应用程序通过文件描述符识别该文件。如cwd、txt等
TYPE：文件类型，如DIR、REG等
DEVICE：指定磁盘的名称
SIZE：文件的大小
NODE：索引节点（文件在磁盘上的标识）
NAME：打开文件的确切名称
```



**egg:**

```
查看22端口现在运行的情况
# lsof -i :22
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
sshd 1409 root 3u IPv6 5678 TCP *:ssh (LISTEN)
查看所属root用户进程所打开的文件类型为txt的文件# lsof -a -u root -d txt
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
init 1 root txt REG 3,3 38432 1763452 /sbin/init
mingetty 1632 root txt REG 3,3 14366 1763337 /sbin/mingetty
mingetty 1633 root txt REG 3,3 14366 1763337 /sbin/mingetty
mingetty 1634 root txt REG 3,3 14366 1763337 /sbin/mingetty
mingetty 1635 root txt REG 3,3 14366 1763337 /sbin/mingetty
mingetty 1636 root txt REG 3,3 14366 1763337 /sbin/mingetty
mingetty 1637 root txt REG 3,3 14366 1763337 /sbin/mingetty
kdm 1638 root txt REG 3,3 132548 1428194 /usr/bin/kdm
X 1670 root txt REG 3,3 1716396 1428336 /usr/bin/Xorg
kdm 1671 root txt REG 3,3 132548 1428194 /usr/bin/kdm
startkde 2427 root txt REG 3,3 645408 1544195 /bin/bash
```


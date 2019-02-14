## 自动化部署

### pexpect

Pexpect 是 Don Libes 的 Expect 语言的一个 Python 实现，是一个用来启动子程序，并使用正则表达式对程序输出做出特定响应，以此实现与其自动交互的 Python 模块。 Pexpect 的使用范围很广，可以用来实现与 ssh、ftp 、telnet 等程序的自动交互；可以用来自动复制软件安装包并在不同机器自动安装；还可以用来实现软件测试中与命令行交互的自动化。

```
import pexpect
import sys

child = pexpect.spawn('ssh std20@123.57.211.212')
child.logfile = sys.stdout
#fout = file('mylog.txt', 'w')
#child.logfile = fout
child.expect('password:')
child.sendline('std20')
child.expect('std20.*')
child.sendline('ls /')
child.expect('std20.*')
child.sendline('exit')
```

```
#coding=utf_8

from pexpect import pxssh
import sys

s = pxssh.pxssh()
s.logfile = sys.stdout
hostname = '123.57.211.212'
username = 'std20'
password = 'std20'
s.login(hostname, username, password)
s.sendline('ls /')
s.prompt()  #匹配系统提示符
s.sendline('whoami')
s.prompt()  
s.logout()
```

### fabric

项目发布和运维的工作相当机械，频率还蛮高，导致时间浪费在敲大量重复的命令上。

修复bug什么的，测试，提交版本库(2分钟)，ssh到测试环境pull部署（2分钟），rsync到线上机器A,B,C,D,E（1分钟），分别ssh到ABCDE五台机器，逐一重启(8-10分钟) = 13-15分钟

其中郁闷的是，每次操作都是相同的，命令一样，要命的是在多个机器上，很难在本机一个脚本搞定，主要时间都浪费在ssh，敲命令上了，写成脚本，完全可以一键执行，花两分钟看下执行结果。

#### 安装

pip install fabric

#### 入门示例

```
#fabfile.py
from fabric.api import run

def host_type():
    run('uname -s')
```

启动

```
itcast@ubuntu:~/tmp/fab$ fab -H 127.0.0.1 host_type
[127.0.0.1] Executing task 'host_type'
[127.0.0.1] run: uname -s
[127.0.0.1] Login password for 'itcast': 
[127.0.0.1] out: Linux
[127.0.0.1] out: 


Done.
Disconnecting from 127.0.0.1... done.
itcast@ubuntu:~/tmp/fab$ fab -H 127.0.0.1 host_type
[127.0.0.1] Executing task 'host_type'
[127.0.0.1] run: uname -s
[127.0.0.1] Login password for 'itcast': 
[127.0.0.1] out: Linux
[127.0.0.1] out: 
```

#### fabric常用参数

- -l : 显示定义好的任务函数名
- -f : 指定fab入口文件，默认入口文件名为fabfile.py
- -H : 指定目标主机，多台主机用","号分割

#### fabric常用API

- local : 执行本地命令，如：local('uname -s')
- lcd : 切换本地目录，如：lcd('/home')
- cd : 切换远程目录，如：cd('/etc')
- run : 执行远程命令，如：run('free -m')
- sudo : sudo方式执行远程命令，如：sudo('touch /abc')
- put : 上传本地文件到远程主机，如：put('/hello', '/home/itcast/hello')
- get : 从远程主机下载文件到本地，如：get('/home/python/world', '/home/itcast/world')
- reboot : 重启远程主机，如：reboot()
- @task : 函数装饰器，标识的函数为fab可调用的，非标记的对fab不可见，纯业务逻辑
- @runs_once : 函数装饰器，标识的函数只会执行一次，不受多台主机影响

#### fabric全局属性设定

- env.host : 定义目标主机，如：env.host=['192.168.17.192', '192.168.17.193']
- env.user : 定义用户名，如：env.user="root"
- env.port : 定义目标主机端口，默认为22，如：env.port="22"
- env.password : 定义密码，如：env.password="chuanzhi"
- env.passwords : 不同的主机不同的密码，如：env.passwords={'itcast@192.168.17.192:22':'chuanzhi', 'itcast@192.168.17.193:22':'python'}

#### 示例1：动态获取远程目录列表

```
from fabric.api import *

env.hosts=['192.168.17.192', '192.168.17.193']
#env.password='python'
env.passwords = {
    'itcast@192.168.17.192:22':'python',
    'itcast@192.168.17.193:22':'python',
}

@runs_once
def input_raw():
    return prompt("please input directory name:", default="/home")

def workask(dirname):
    run('ls -l ' + dirname)

@task
def go():
    print('start ...')
    getdirname = input_raw()
    workask(getdirname)
    print('end ...')
```

#### 示例2：上传文件并执行

```
from fabric.api import *

env.user = 'itcast'
env.hosts = ['192.168.17.192', '192.168.17.193']
env.password = 'python'

@task
@runs_once
def tar_task():
    with lcd('/home/itcast/testdemo'):
        local('tar zcvf demo.tar.gz demo.py')

@task
def put_task():
    run('mkdir -p /home/itcast/testdemo')
    with cd('/home/itcast/testdemo'):
        put('/home/itcast/testdemo/demo.tar.gz', '/home/itcast/testdemo/demo.tar.gz')

@task
def check_task():
    lmd5 = local('md5sum /home/itcast/testdemo/demo.tar.gz', capture=True).split(' ')[0]
    rmd5 = run('md5sum /home/itcast/testdemo/demo.tar.gz').split(' ')[0]
    if lmd5 == rmd5:
        print('OK ...')
    else:
        print('ERROR ...')

@task
def run_task():
    with cd('/home/itcast/testdemo'):
        run('tar zxvf demo.tar.gz')
        run('python demo.py')

@task
def go():
    tar_task()
    put_task()
    check_task()
    run_task()
```

#### 代码自动化部署

```
from fabric.api import *

env.user = 'itcast'
env.hosts = ['192.168.17.192', '192.168.17.193']
env.password = 'python'

@runs_once
@task
def local_update():
    with lcd("/home/itcast/tmp/itcasthello"):
        local("git add -A")
        local("git commit -m 'update'")
        local("git pull origin master")
        local("git push origin master")


@task
def remote_update():
    with cd("/home/itcast/tmp/itcasthello"):
        run("git checkout master")
        run("git pull origin master")

@task
def deploy():
    local_update()
    remote_update()
```
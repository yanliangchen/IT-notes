# django+celery+ RabbitMQ实现异步任务最完整教程

置顶 2018年03月25日 17:33:05 [Yrish](https://me.csdn.net/sinat_29699167) 阅读数：3136

 版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/sinat_29699167/article/details/79688464

# 一，首先安装[celery](https://www.baidu.com/s?wd=celery&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)

```
pip install django-celery1
```

# 二，安装rabbitmq

ubuntu环境下执行以下

```
sudo apt-get install rabbitmq-server1
```

添加用户,myuser为用户名，mypassword为用户密码

```
sudo rabbitmqctl add_user myuser mypassword1
```

查看用户

```
sudo rabbitmqctl list_users1
```

新增管理员用户 myuser为用户名密码，administrator为管理员标签

```
sudo rabbitmqctl set_user_tags myuser administrator1
```

添加虚拟环境

```
sudo rabbitmqctl add_vhost vhost1
```

设置用户在虚拟环境下拥有所有权限

```
sudo rabbitmqctl set_permissions -p vhost myuser ".*" ".*" ".*"1
```

可以用刚设置的账户登录管理页面

```
http://服务器ip:156721
```

在浏览器打开后可以看到登录界面 
![这里写图片描述](https://img-blog.csdn.net/20180325165323404?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzI5Njk5MTY3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 
输入刚才设置的用户名密码即可登录。

# 三，django工程配置

1，在工程settings.py中INSTALLED_APPS中加入djcelery,如下图所示 
![这里写图片描述](https://img-blog.csdn.net/20180325165653520?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzI5Njk5MTY3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 
2，在工程settings.py加入broker相关配置，默认是以本机的mq服务作为broker。如果你需要配置成远程的mq，需要填写完整的BROKER_URL = amqp://userid:password@hostname:port/virtual_host，本文以远程broker为例

```
import djcelery
djcelery.setup_loader()
#数据库调度
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
BROKER_URL= 'amqp://myuser:password@服务器ip:5672/vhost'12345
```

3在工程设置目录下加入celery.py(与settings.py同级)

```
# coding:utf8
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.

# yourprojectname代表你工程的名字，在下面替换掉
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourprojectname.settings')

app = Celery('proj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))123456789101112131415161718192021222324
```

4修改工程目录里面的*init*.py

```
from __future__ import absolute_import
from .celery import app as celery_app12
```

5在应用目录下新建tasks.py，假设加入以下两个计算任务

```
from __future__ import absolute_import
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y123456789101112
```

# 最后，运行celery worker

```
python manage.py celery worker --loglevel=info
12
```

# 补充

Celery提供了一个工具flower，将各个任务的执行情况、各个worker的健康状态进行监控并以可视化的方式展现

1. 安装flower:

```
pip install flower1
```

　　2. 启动flower（默认会启动一个webserver，端口为5555）:

```
python manage.py celery flower1
```

　　3. 进入[http://localhost:5555](http://localhost:5555/)即可查看。
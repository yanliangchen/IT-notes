# django配置连接多个数据库，自定义表名称

在项目tt下新建两个app，分别为app01、app02。配置app01使用default节点数据库；app02使用hvdb节点数据库（也可以配置app01下的model既使用default，也可以使用hvdb数据库）

**1.编辑settings.py，添加多个数据库：**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testly',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST':'192.168.1.1',
        'PORT':'3306',
    },
    'hvdb':{   #配置第二个数据库节点名称
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdjango', #第二个数据库的名称
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST':'192.168.1.1',
        'PORT':'3306',   
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

Django 要求default 数据库必须定义，但是如果不会用到，其参数字典可以保留为空。若要这样做，你必须为你的所有的应用的模型建立DATABASE_ROUTERS，包括正在使用的contrib 中的应用和第三方应用。

default留空写法：

```
'default': {},
```

**2.添加数据库路由表**

   在tt目录下新建文件db_router.py，内如如下。该文件用来对数据库进行自动路由，可以**根据每个model的app_label来指定使用某个DB**。

   注：可以定义多个Router，由于此处的app01使用default数据库，所以在此无需指定default节点的数据库路由。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# -*- coding: UTF-8 -*-
class app02Router(object): #配置app02的路由，去连接hvdb数据库
    """
    A router to control all database operations on models in the app02 application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read app02 models go to hvdb DB.
        """
        if model._meta.app_label == 'app02': #app name（如果该app不存在，则无法同步成功）
            return 'hvdb' #hvdb为settings中配置的database节点名称，并非db name。dbname为testdjango
        return None
 
    def db_for_write(self, model, **hints):
        """
        Attempts to write app02 models go to hvdb DB.
        """
        if model._meta.app_label == 'app02':
            return 'hvdb'
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app02 app is involved.
        当 obj1 和 obj2 之间允许有关系时返回 True ，不允许时返回 False ，或者没有 意见时返回 None 。
        """
        if obj1._meta.app_label == 'app02' or \
           obj2._meta.app_label == 'app02':
            return True
        return None
 
    def allow_migrate(self, db, model):
        """
        Make sure the app02 app only appears in the hvdb database.
        """
        if db == 'hvdb':
            return model._meta.app_label == 'app02'
        elif model._meta.app_label == 'app02':
            return False

 
    def allow_syncdb(self, db, model): #决定 model 是否可以和 db 为别名的数据库同步
        if db == 'hvdb' or model._meta.app_label == "app02":
            return False  # we're not using syncdb on our hvdb database
        else:  # but all other models/databases are fine
            return True
        return None
 

# class app01Router(object):
#     """
#     A router to control all database operations on models in the
#     aew application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read aew models go to aew DB.
#         """
#         if model._meta.app_label == 'app01':
#             return 'default'
#         return None
 
#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write aew models go to aew DB.
#         """
#         if model._meta.app_label == 'app01':
#             return 'default'
#         return None
 
#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the aew app is involved.
#         """
#         if obj1._meta.app_label == 'app01' or obj2._meta.app_label == 'app01':
#             return True
#         return None
 
#     def allow_migrate(self, db, model):
#         """
#         Make sure the aew app only appears in the aew database.
#         """
#         if db == 'default':
#             return model._meta.app_label == 'app01'
#         elif model._meta.app_label == 'app01':
#             return False
#         return None
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

**3.编辑settings.py，添加路由**：

   注：由于此处的app01使用default数据库，所以在此无需指定default节点的数据库路由。

```
DATABASE_ROUTERS = ['tt.db_router.app02Router'] #tt为当前项目名称，db_router为上一步编写的db_router.py文件，app02Router为Router
#DATABASE_ROUTERS = ['tt.db_router.app02Router','tt.db_router.app01Router'] #如果定义了多个Router，在此就需要分别指定。注意：这个是有顺序的（先匹配上的规则，就先生效）
```

**4.为每个app的model分别指定所需要连接的数据库**：

   通过对每个model指定好对应的app_label，使其通过Router去连接相应的数据库。

  编辑app02下的models.py，为app02下的model mtable01指定连接hvdb节点数据库，内容如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class mtable01(models.Model):
    name=models.CharField(max_length=100,primary_key=True,unique=True)
    ip=models.GenericIPAddressField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'app02' #定义该model的app_label
        ordering = ['name'] 使用migrate命令同步数据库：
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

编辑app01下的models.py:

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class tb05(models.Model): #该model使用default数据库
    name=models.CharField(max_length=100,primary_key=True,unique=True)
    ip=models.GenericIPAddressField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        #app_label = 'app01' #由于该model连接default数据库，所以在此无需指定
        ordering = ['name'] 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 也可以为app01下的model指定连接hvdb数据库，内容如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class tb2(models.Model):
    name=models.CharField(max_length=100,primary_key=True,unique=True)
    ip=models.GenericIPAddressField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'app02'
        ordering = ['name'] 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

为app01下的tb02指定使用hvdb数据库，同时**自定义表名称**为‘mytable’，不使用默认的表名称app02_tb06，不便于区分

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class tb06(models.Model):
    name=models.CharField(max_length=100,primary_key=True,unique=True,db_column='mycname') #使用db_column自定义字段名称
    ip=models.GenericIPAddressField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mytable' #自定义表名称为mytable
        verbose_name = '自定义名称' #指定在admin管理界面中显示的名称 
        app_label = 'app02'
        ordering = ['name'] 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

**5.同步数据库：**

 migrate管理命令一次操作一个数据库。默认情况下，它在`default` 数据库上操作，但是通过提供一个 -`-database` 参数，告诉migrate同步一个不同的数据库。

1）同步default节点数据库，只运行不带 --database参数的命令，不对其他数据库进行同步

python manage.pymigrate
python manage.py makemigrations
python manage.pymigrate

2）同步hvdb节点数据库：

python manage.pymigrate --database=hvdb
python manage.py makemigrations
python manage.pymigrate --database=hvdb

结果：

testdjango数据库（hvdb节点）下的app02_mtable01表对应app02下的mtable01模型

testdjango数据库（hvdb节点）下的app02_tb2表对应app01下的tb2模型

testly数据库（default节点）下的app01_tb05表对应app01下的tb05模型

![img](https://images2015.cnblogs.com/blog/235279/201605/235279-20160507210633046-785594365.jpg)

  参考：http://smilejay.com/2014/07/django-use-mult-databases/ **根据model的app label区分数据库**

   　　  http://my.oschina.net/u/572994/blog/108533  **根据应用自动区分数据库**

 　　    http://python.usyiyi.cn/django/topics/db/multi-db.html  **Django文档**
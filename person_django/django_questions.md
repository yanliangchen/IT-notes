1. Django里QuerySet的get和filter方法的区别?

get获得是一个对象，filter得到是一个对象列表，即使只有一个满足条件 

```
用get方法查询的时候，查询不到内容的时候会抛出异常，同样查询结果多余1条的时候也会抛出异常

Exp：fresh.models.DoesNotExist: Cart matching query does not exist.

filer若是查询不到数据，会返回一个空的查询集，[]  type类型是：Queryset。查询到多余一条的时候会返回一个包含多个对象的查询集。

因此可以用filter来判断数据库中是否存在某条记录：

cart = Cart.objects.filter(user=user, goods=good)
if len(cart)>0:
    cart[0].number = cart[0].number+int(amount)
    cart[0].save()
else:
    newCart = Cart()
    newCart.user=user
    newCart.goods=good
    newCart.number=int(amount)
    newCart.save()
从Cart表查询，如果不存在这条记录，则返回[ ]，所以len(cart)=0，因此如果len(cart)>0，说明记录存在


```



### 2.简述django对http请求的执行流程。

```
一个 HTTP 请求，首先被转化成一个 HttpRequest 对象，然后该对象被传递给 Request 中间件处理，如果该中间件返回了Response，则直接传递给 Response 中间件做收尾处理。否则的话 Request 中间件将访问 URL 配置，确定哪个 view 来处理，在确定了哪个 view 要执行，但是还没有执行该 view 的时候，系统会把 request 传递给 View 中间件处理器进行处理，如果该中间件返回了Response，那么该Response 直接被传递给 Response 中间件进行后续处理，否则将执行确定的 View 函数处理并返回 Response，在这个过程中如果引发了异常并抛出，会被 Exception 中间件处理器进行处理。
```



### 3.简述Django下的(内建的)缓存机制。

#### **3.1.缓存的简介**

在动态网站中,用户所有的请求,服务器都会去数据库中进行相应的增,删,查,改,渲染模板,执行业务逻辑,最后生成用户看到的页面.

当一个网站的用户访问量很大的时候,每一次的的后台操作,都会消耗很多的服务端资源,所以必须使用缓存来减轻后端服务器的压力.

缓存是将一些常用的数据保存内存或者memcache中,在一定的时间内有人来访问这些数据时,则不再去执行数据库及渲染等操作,而是直接从内存或memcache的缓存中去取得数据,然后返回给用户.

#### **3.2.Django提供了6种缓存方式**

- 开发调试缓存
- 内存缓存
- 文件缓存
- 数据库缓存
- Memcache缓存(使用python-memcached模块)
- Memcache缓存(使用pylibmc模块)

经常使用的有文件缓存和Mencache缓存

#### 3.3 各种缓存配置

1.2.1 开发调试(此模式为开发调试使用,实际上不执行任何操作)

settings.py文件配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 缓存后台使用的引擎
  'TIMEOUT': 300,            # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
  'OPTIONS':{
   'MAX_ENTRIES': 300,          # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  },
 }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

1.2.2 内存缓存(将缓存内容保存至内存区域中)

settings.py文件配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 指定缓存使用的引擎
  'LOCATION': 'unique-snowflake',         # 写在内存中的变量的唯一值 
  'TIMEOUT':300,             # 缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }  
 }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

1.2.3 文件缓存(把缓存数据存储在文件中)

settings.py文件配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #指定缓存使用的引擎
  'LOCATION': '/var/tmp/django_cache',        #指定缓存的路径
  'TIMEOUT':300,              #缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }
 }   
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

1.2.4 数据库缓存(把缓存数据存储在数据库中)

settings.py文件配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # 指定缓存使用的引擎
  'LOCATION': 'cache_table',          # 数据库表    
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }  
 }   
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

注意,创建缓存的数据库表使用的语句:

```
python manage.py createcachetable
```

1.2.5 Memcache缓存(使用python-memcached模块连接memcache)

Memcached是Django原生支持的缓存系统.要使用Memcached,需要下载Memcached的支持库python-memcached或pylibmc.

settings.py文件配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', # 指定缓存使用的引擎
  'LOCATION': '192.168.10.100:11211',         # 指定Memcache缓存服务器的IP地址和端口
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }
 }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

LOCATION也可以配置成如下:

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
'LOCATION': 'unix:/tmp/memcached.sock',   # 指定局域网内的主机名加socket套接字为Memcache缓存服务器
'LOCATION': [         # 指定一台或多台其他主机ip地址加端口为Memcache缓存服务器
 '192.168.10.100:11211',
 '192.168.10.101:11211',
 '192.168.10.102:11211',
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

1.2.6 Memcache缓存(使用pylibmc模块连接memcache)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
settings.py文件配置
 CACHES = {
  'default': {
   'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',  # 指定缓存使用的引擎
   'LOCATION':'192.168.10.100:11211',         # 指定本机的11211端口为Memcache缓存服务器
   'OPTIONS':{
    'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
    'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
   },  
  }
 }
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

LOCATION也可以配置成如下:

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
'LOCATION': '/tmp/memcached.sock',  # 指定某个路径为缓存目录
'LOCATION': [       # 分布式缓存,在多台服务器上运行Memcached进程,程序会把多台服务器当作一个单独的缓存,而不会在每台服务器上复制缓存值
 '192.168.10.100:11211',
 '192.168.10.101:11211',
 '192.168.10.102:11211',
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

Memcached是基于内存的缓存,数据存储在内存中.所以如果服务器死机的话,数据就会丢失,所以Memcached一般与其他缓存配合使用

#### **3.4 Django中的缓存应用**

Django提供了不同粒度的缓存,可以缓存某个页面,可以只缓存一个页面的某个部分,甚至可以缓存整个网站.

数据库：

```
class Book(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=1)
```

![img](https://images2017.cnblogs.com/blog/877318/201712/877318-20171213193539004-1037954462.png)

视图：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
from django.views.decorators.cache import cache_page
import time
from .models import *

@cache_page(15)          #超时时间为15秒
def index(request):

 t=time.time()      #获取当前时间
 bookList=Book.objects.all()
 return render(request,"index.html",locals())
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

模板(index.html):

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>当前时间:-----{{ t }}</h3>

<ul>
    {% for book in bookList %}
       <li>{{ book.name }}--------->{{ book.price }}$</li>
    {% endfor %}
</ul>

</body>
</html>
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

上面的例子是基于内存的缓存配置,基于文件的缓存该怎么配置呢??

更改settings.py的配置

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', # 指定缓存使用的引擎
  'LOCATION': 'E:\django_cache',          # 指定缓存的路径
  'TIMEOUT': 300,              # 缓存超时时间(默认为300秒,None表示永不过期)
  'OPTIONS': {
   'MAX_ENTRIES': 300,            # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,           # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  }
 }
}
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

然后再次刷新浏览器,可以看到在刚才配置的目录下生成的缓存文件

通过实验可以知道,Django会以自己的形式把缓存文件保存在配置文件中指定的目录中. 

**1.3.2 全站使用缓存**

既然是全站缓存,当然要使用Django中的中间件.

用户的请求通过中间件,经过一系列的认证等操作,如果请求的内容在缓存中存在,则使用FetchFromCacheMiddleware获取内容并返回给用户

当返回给用户之前,判断缓存中是否已经存在,如果不存在,则UpdateCacheMiddleware会将缓存保存至Django的缓存之中,以实现全站缓存

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
缓存整个站点，是最简单的缓存方法

在 MIDDLEWARE_CLASSES 中加入 “update” 和 “fetch” 中间件
MIDDLEWARE_CLASSES = (
    ‘django.middleware.cache.UpdateCacheMiddleware’, #第一
    'django.middleware.common.CommonMiddleware',
    ‘django.middleware.cache.FetchFromCacheMiddleware’, #最后
)
“update” 必须配置在第一个
“fetch” 必须配置在最后一个
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

修改settings.py配置文件

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',   #响应HttpResponse中设置几个headers
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',   #用来缓存通过GET和HEAD方法获取的状态码为200的响应

)


CACHE_MIDDLEWARE_SECONDS=10
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

视图函数：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
from django.views.decorators.cache import cache_page
import time
from .models import *


def index(request):

     t=time.time()      #获取当前时间
     bookList=Book.objects.all()
     return render(request,"index.html",locals())

def foo(request):
    t=time.time()      #获取当前时间
    return HttpResponse("HELLO:"+str(t))
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

模板(index.html)：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3 style="color: green">当前时间:-----{{ t }}</h3>

<ul>
    {% for book in bookList %}
       <li>{{ book.name }}--------->{{ book.price }}$</li>
    {% endfor %}
</ul>

</body>
</html>
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

其余代码不变,刷新浏览器是10秒,页面上的时间变化一次,这样就实现了全站缓存.

**1.3.3 局部视图缓存**

例子,刷新页面时,整个网页有一部分实现缓存

views视图函数

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
from django.views.decorators.cache import cache_page
import time
from .models import *


def index(request):

     t=time.time()      #获取当前时间
     bookList=Book.objects.all()

     return render(request,"index.html",locals())
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

模板(index.html):

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
{% load cache %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 <h3 style="color: green">不缓存:-----{{ t }}</h3>

{% cache 2 'name' %}
 <h3>缓存:-----:{{ t }}</h3>
{% endcache %}

</body>
</html> 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

### 4.Django中Model的slugFied类型字段有什么用途（温故其他字段类型）？

转自：https://blog.csdn.net/gavinking0110/article/details/54412590

```
Django中的页面管理后台
Djano中自带admin后台管理模块,可以通过web页面去管理,有点想php-admin,使用步骤:

在项目中models.py 中创建数据库表

class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    memo = models.TextField()
    img = models.ImageField()
    usertype=models.ForeignKey("usertype",null=True,blank=True)
class usertype(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
在terminal中执行

python manage.py makemigrations
   python manage.py migrate
 
#创建超级用户,设置管理员密码,密码至少8位
   python manage.py createsuperuser
在项目中的admin.py中设置,注册已经设置的数据库

from django.contrib import admin
 
# Register your models here.
 
from app01 import models
admin.site.register(models.userinfo)
admin.site.register(models.usertype)
在页面中访问/admin,即可访问后台管理以及对数据增删改查

model详解
Django中遵循 Code Frist 的原则，即：根据代码中定义的类来自动生成数据库表。

创建表
基本结构
from django.db import models
 
# Create your models here.
 
class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    memo = models.TextField()
    img = models.ImageField()
    usertype=models.ForeignKey("usertype",null=True,blank=True)
class usertype(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
更多字段:

1、models.AutoField　　自增列 = int(11)
　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、models.CharField　　字符串字段
　　必须 max_length 参数
3、models.BooleanField　　布尔类型=tinyint(1)
　　不能为空，Blank=True
4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
　　继承CharField，所以必须 max_lenght 参数
5、models.DateField　　日期类型 date
　　对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、models.DateTimeField　　日期类型 datetime
　　同DateField的参数
7、models.Decimal　　十进制小数类型 = decimal
　　必须指定整数位max_digits和小数位decimal_places
8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
　　对字符串进行正则表达式
9、models.FloatField　　浮点类型 = double
10、models.IntegerField　　整形
11、models.BigIntegerField　　长整形
　　integer_field_ranges = {
　　　　'SmallIntegerField': (-32768, 32767),
　　　　'IntegerField': (-2147483648, 2147483647),
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
　　　　'PositiveSmallIntegerField': (0, 32767),
　　　　'PositiveIntegerField': (0, 2147483647),
　　}
12、models.IPAddressField　　字符串类型（ip4正则表达式）
13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
　　参数protocol可以是：both、ipv4、ipv6
　　验证时，会根据设置报错
14、models.NullBooleanField　　允许为空的布尔类型
15、models.PositiveIntegerFiel　　正Integer
16、models.PositiveSmallIntegerField　　正smallInteger
17、models.SlugField　　减号、下划线、字母、数字
18、models.SmallIntegerField　　数字
　　数据库中的字段有：tinyint、smallint、int、bigint
19、models.TextField　　字符串=longtext
20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
21、models.URLField　　字符串，地址正则表达式
22、models.BinaryField　　二进制
23、models.ImageField   图片
24、models.FilePathField 文件
更多参数:

1、null=True
　　数据库中字段是否可以为空
2、blank=True
　　django的 Admin 中添加数据时是否可允许空值
3、primary_key = False
　　主键，对AutoField设置主键后，就会代替原来的自增 id 列
4、auto_now 和 auto_now_add
　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  自动创建---永远是创建时的时间
5、choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
6、max_length
7、default　　默认值
8、verbose_name　　Admin中字段的显示名称
9、name|db_column　　数据库中的字段名称
10、unique=True　　不允许重复
11、db_index = True　　数据库索引
12、editable=True　　在Admin里是否可编辑
13、error_messages=None　　错误提示
14、auto_created=False　　自动创建
15、help_text　　在Admin中提示帮助信息
16、validators=[]
17、upload-to   上传到哪个位置,更多与image,filepath配合使用
连表结构
一对多:models.ForeignKey(其他表)
多对多:models.ManyToManyField(其他表)
一对一:models.ManyToManyField(其他表)
应用场景:

应用场景：
 
一对多：当一张表中创建一行数据时，有一个单选的下拉框（可以被重复选择）
    例如：创建用户信息时候，需要选择一个用户类型【普通用户】【金牌用户】【铂金用户】等。
多对多：在某表中创建一行数据是，有一个可以多选的下拉框
    例如：创建用户信息，需要为用户指定多个爱好
一对一：在某表中创建一行数据时，有一个单选的下拉框（下拉框中的内容被用过一次就消失了
    例如：原有含10列数据的一张表保存相关信息，经过一段时间之后，10列无法满足需求，需要为原来的表再添加5列数据
看个例子:

from django.db import models
 
# Create your models here.
from django.db import models
 
# 陈超，普通用户
# 淮军，超级用户
class Gender(models.Model):
    name = models.CharField(max_length=32)
 
 
class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='用户名',editable=False)
    email = models.EmailField(db_index=True)
    memo = models.TextField()
    img = models.ImageField(upload_to='upload')
    user_type = models.ForeignKey("UserType", null=True, blank=True)# unique
    # user_type = models.OneToOneField("UserType", null=True, blank=True)# unique
    # ctime = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    # gender = models.ForeignKey(Gender)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.IntegerField(choices=gender_choices,default=1)
# 普通用户，超级用户
class UserType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
class B2G(models.Model):
    boy = models.ForeignKey('Boy')
    girl = models.ForeignKey('Girl')
class Boy(models.Model):
    name = models.CharField(max_length=32)
# 吴文煜，王建，王志刚，杜宝强
class Girl(models.Model):
    name = models.CharField(max_length=32)
    f = models.ManyToManyField(Boy)
# 铁锤，钢弹，如花
TIPS:
modles.py中class设置的数据,本身返回为一个类,如果想直接返回某一个字段的值,可以定义__str__,比如:

class TypeUser(models.Model):
    name = models.CharFiled(max_length=32)
    def __str__(self):
        return self.name
在设置ForeignKey时,参数中的第一个参数为表名,**需要注意的是,加不加引号有区别:加引号后表的定义顺序可以随便,但不加引号必须按照顺序来:

class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='用户名',editable=False)
    email = models.EmailField(db_index=True)
    memo = models.TextField()
    img = models.ImageField(upload_to='upload')
    user_type = models.ForeignKey("UserType", null=True, blank=True)# unique
    # user_type = models.OneToOneField("UserType", null=True, blank=True)# unique
    # ctime = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    # gender = models.ForeignKey(Gender)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.IntegerField(choices=gender_choices,default=1)
class UserType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
多对多,有两种创建方式

自建第三张表
自动创建,比如:

#自建第三张表
class B2G(models.Model):
    boy = models.ForeignKey('Boy')
    girl = models.ForeignKey('Girl')
class Boy(models.Model):
    name = models.CharField(max_length=32)
    # 吴文煜，王建，王志刚，杜宝强
class Girl(models.Model):
    name = models.CharField(max_length=32)
    #自动创建
    f = models.ManyToManyField(Boy)
多对多详情参考：http://www.cnblogs.com/zknublx/p/5959295.html

queryset

从数据库中提取出来的数据为queryset类型,是Django中的一种特殊类型.

w = models.Simp.objects.all()
print(w, type(w))
[<Simp: chenc>, <Simp: zan>, <Simp: zhangsan>]<class 'django.db.models.query.QuerySet'>
可以看到，从数据库取出个数据看起来像包含对象的列表。而实际上整个数据为django中的特殊类型QuerySet。

如果需要查看原来的SQL语句,可以使用queryset.query:

print(w.query)
values() 和 vlue_list() 与 all()区别

.all()是取得所有列的数据，可以加.values()取出某一列，每一个元素为一个字典：

obj = model.UserInfo.objects.filter(name='alex').values('id','email')
# select id from userinfo where name = 'alex'
queryset -> python，Django的类
[{'id':1},{'id': 2},]
values_list()，获取到的元素为一个个元组,也可以加多个参数来获取多列:

obj = model.UserInfo.objects.filter(name='alex').value_list('id','email')
# select id from userinfo where name = 'alex'
queryset -> python，Django的类
[(1,'1@qq.com'),(2,'alex@11.com'),]
表操作
基本操作
# 增
    #
    # models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs
 
    # obj = models.Tb1(c1='xx', c2='oo')
    # obj.save()
 
    # 查
    #
    # models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
    # models.Tb1.objects.all()               # 获取全部
    # models.Tb1.objects.filter(name='seven') # 获取指定条件的数据
 
    # 删
    #
    # models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据
 
    # 改
    # models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
    # obj = models.Tb1.objects.get(id=1)
    # obj.c1 = '111'
    # obj.save()                                                 # 修改单条数据
进阶操作(了不起的双下划线)
利用双下划线将字段和对应的操作连接起来

# 获取个数
    #
    # models.Tb1.objects.filter(name='seven').count()
 
    # 大于，小于
    #
    # models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值
    # models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值
    # models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
 
    # in
    #
    # models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
    # models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
 
    # contains
    #
    # models.Tb1.objects.filter(name__contains="ven")
    # models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
    # models.Tb1.objects.exclude(name__icontains="ven")
 
    # range
    #
    # models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and
 
    # 其他类似
    #
    # startswith，istartswith, endswith, iendswith,
 
    # order by
    #
    # models.Tb1.objects.filter(name='seven').order_by('id')    # asc
    # models.Tb1.objects.filter(name='seven').order_by('-id')   # desc
 
    # limit 、offset
    #
    # models.Tb1.objects.all()[10:20]
 
    # group by
    from django.db.models import Count, Min, Max, Sum
    # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
    # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"
连表操作(了不起的双下划线)
利用双下划线和 _set 将表之间的操作连接起来

数据库表结构:

class UserProfile(models.Model):
    user_info = models.OneToOneField('UserInfo')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    def __unicode__(self):
        return self.username
class UserInfo(models.Model):
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )
    user_type = models.IntegerField(choices=user_type_choice)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name
class UserGroup(models.Model):
    caption = models.CharField(max_length=64)
    user_info = models.ManyToManyField('UserInfo')
    def __unicode__(self):
        return self.caption
class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('UserGroup')
    def __unicode__(self):
        return self.hostname
一对一操作:

user_info_obj = models.UserInfo.objects.filter(id=1).first()
print user_info_obj.user_type
print user_info_obj.get_user_type_display()
print user_info_obj.userprofile.password
 
user_info_obj = models.UserInfo.objects.filter(id=1).values('email', 'userprofile__username').first()
print user_info_obj.keys()
print user_info_obj.values()
一对多操作,类似于一对一:

1、搜索条件使用 __ 连接
2、获取值时使用 .    连接
多对多操作:

user_info_obj = models.UserInfo.objects.get(name=u'武沛齐')
user_info_objs = models.UserInfo.objects.all()
 
group_obj = models.UserGroup.objects.get(caption='CEO')
group_objs = models.UserGroup.objects.all()
 
# 添加数据
#group_obj.user_info.add(user_info_obj)
#group_obj.user_info.add(*user_info_objs)
 
# 删除数据
#group_obj.user_info.remove(user_info_obj)
#group_obj.user_info.remove(*user_info_objs)
 
# 添加数据
#user_info_obj.usergroup_set.add(group_obj)
#user_info_obj.usergroup_set.add(*group_objs)
 
# 删除数据
#user_info_obj.usergroup_set.remove(group_obj)
#user_info_obj.usergroup_set.remove(*group_objs)
 
# 获取数据
#print group_obj.user_info.all()
#print group_obj.user_info.all().filter(id=1)
 
# 获取数据
#print user_info_obj.usergroup_set.all()
#print user_info_obj.usergroup_set.all().filter(caption='CEO')
#print user_info_obj.usergroup_set.all().filter(caption='DBA')
其他操作:

# F 使用查询条件的值
    #
    # from django.db.models import F
    # models.Tb1.objects.update(num=F('num')+1)
 
    # Q 构建搜索条件
    from django.db.models import Q
    # con = Q()
    #
    # q1 = Q()
    # q1.connector = 'OR'
    # q1.children.append(('id', 1))
    # q1.children.append(('id', 10))
    # q1.children.append(('id', 9))
    #
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('c1', 1))
    # q2.children.append(('c1', 10))
    # q2.children.append(('c1', 9))
    #
    # con.add(q1, 'AND')
    # con.add(q2, 'AND')
    #
    # models.Tb1.objects.filter(con)
 
    #
    # from django.db import connection
    # cursor = connection.cursor()
    # cursor.execute("""SELECT * from tb where name = %s""", ['Lennon'])
    # row = cursor.fetchone()
xx_set中的_set是多对多的固定搭配

扩展
自定义上传
def upload_file(request):
    if request.method == "POST":
        obj = request.FILES.get('fafafa')
        f = open(obj.name, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
    return render(request, 'file.html')
form上传文件实例
class FileForm(forms.Form):
    ExcelFile = forms.FileField()
models.py:

from django.db import models
class UploadFile(models.Model):
    userid = models.CharField(max_length = 30)
    file = models.FileField(upload_to = './upload/')
    date = models.DateTimeField(auto_now_add=True)
view.py:

def UploadFile(request):
    uf = AssetForm.FileForm(request.POST,request.FILES)
    if uf.is_valid():
            upload = models.UploadFile()
            upload.userid = 1
            upload.file = uf.cleaned_data['ExcelFile']
            upload.save()
            
            print upload.file
```



### 5.Django的生命周期(中间件的理解)

参考 **https://blog.csdn.net/zhoulin753/article/details/80457355**

参考  **https://www.cnblogs.com/zhaof/p/6281541.html**

```
 django的生命周期是:前端请求--->nginx--->uwsgi.--->中间件--->url路由---->view试图--->orm---->拿到数据返回给view---->试图将数据渲染到模版中拿到字符串---->中间件--->uwsgi---->nginx---->前端渲染。
 
   今天就不讲其他内容，今天就讲中间件的内容，中间件的作用非常大，可以处理所有的请求内容，中间件其实就是一个类，这个类中一共有5个方法，分别是process_request, process_response，process_view, process_exception,process_render_template，今天就讲讲他的运行顺序。

当一个请求，首先从上往下运行这些类中process_request方法，之后进入django的从上往下执行每个类中的process_view方法，在然后就进入我们自定义的view.py文件，如果你的试图中有错误，那就会从下往上执行中间件中的process_exception方法，然后把错误信息在通过process_response中返回给客户端。

process_request：在这个方法中是没有return方法的，如果有那就会执行process_response方法，直接返回给客户端，一般情况下我们是不会在这里返回内容的，除非你有需求，判断发过来的请求过来的内容，如果不是很友好的请求，那么我们直接就可以在这返回，直接卡死，让这个请求直接都进不了我们的django中的内部程序，

process_response:在这个方法中我们必须要有return方法，这样才能一步一步的返回给客户端，当然你也可以写一些东西在response里，在这里写就是会在所有的response里都会有你所添加的内容！

process_view:这个方法中是没有return方法的，如果有那就走process_response方法；

process_exception:在这个方法中是一定要有return方法的，这个方法是专门返回你的错误信息的，我可以在所有的视图函数只要出现错误就会执行这个方法，可以返回一个错误模版信息！

```

### 6.Django中间件（settings解释）

```
django中有中间件middleware在我们项目settings中的 MIDDLEWARE中 下面浅谈各个中间件含义以及自定义用法:

django.middleware.security.SecurityMiddleware’
 一些安全设置，比如XSS脚本过滤。

django.contrib.sessions.middleware.SessionMiddleware
session支持中间件，加入这个中间件，会在数据库中生成一个django_session的表。

django.middleware.common.CommonMiddleware
通用中间件，会处理一些URL，比如baidu.com会自动的处理成www.baidu.com。比如/blog/111会处理成/blog/111/自动加上反斜杠。

django.middleware.csrf.CsrfViewMiddleware
跨域请求伪造中间件。加入这个中间件，在提交表单的时候会必须加入csrf_token，cookie中也会生成一个名叫csrftoken的值，也会在header中加入一个HTTP_X_CSRFTOKEN的值来放置CSRF攻击。

django.contrib.auth.middleware.AuthenticationMiddleware
用户授权中间件。他会在每个HttpRequest对象到达view之前添加当前登录用户的user属性，也就是你可以在view中通过request访问user。

django.contrib.messages.middleware.MessageMiddleware
消息中间件。展示一些后台信息给前端页面。如果需要用到消息，还需要在INSTALLED_APPS中添加django.contrib.message才能有效。如果不需要，可以把这两个都删除。

django.middleware.clickjacking.XFrameOptionsMiddleware
防止通过浏览器页面跨Frame出现clickjacking（欺骗点击）攻击出现。

```

### 7.Django的CBV与FBV

**参考：https://www.cnblogs.com/yuanchenqi/articles/8715364.html**

#### FBV

**FBV（function base views）** 就是在视图里使用函数处理请求。

在之前django的学习中，我们一直使用的是这种方式，所以不再赘述。

#### CBV

**CBV（class base views）** 就是在视图里使用类处理请求。

Python是一个面向对象的编程语言，如果只用函数来开发，有很多面向对象的优点就错失了（继承、封装、多态）。所以Django在后来加入了Class-Based-View。可以让我们用类写View。这样做的优点主要下面两种：

1. 提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
2. 可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

#### **使用class-based views**

如果我们要写一个处理GET方法的view，用函数写的话是下面这样。

```
from django.http import HttpResponse
  
def my_view(request):
     if request.method == 'GET':
            return HttpResponse('OK')
```

如果用class-based view写的话，就是下面这样

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from django.http import HttpResponse
from django.views import View
  
class MyView(View):

      def get(self, request):
            return HttpResponse('OK')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

Django的url是将一个请求分配给可调用的函数的，而不是一个class。针对这个问题，class-based view提供了一个`as_view()`静态方法（也就是类方法），调用这个方法，会创建一个类的实例，然后通过实例调用`dispatch()`方法，`dispatch()`方法会根据request的method的不同调用相应的方法来处理request（如`get() `,` post()`等）。到这里，这些方法和function-based view差不多了，要接收request，得到一个response返回。如果方法没有定义，会抛出HttpResponseNotAllowed异常。

在url中，就这么写：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# urls.py
from django.conf.urls import url
from myapp.views import MyView
  
urlpatterns = [
     url(r'^index/$', MyView.as_view()),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

类的属性可以通过两种方法设置，第一种是常见的Python的方法，可以被子类覆盖。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from django.http import HttpResponse
from django.views import View
  
class GreetingView(View):
    name = "yuan"
    def get(self, request):
         return HttpResponse(self.name)
  
# You can override that in a subclass
  
class MorningGreetingView(GreetingView):
    name= "alex"
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

第二种方法，你也可以在url中指定类的属性：

在url中设置类的属性Python

```
urlpatterns = [
   url(r'^index/$', GreetingView.as_view(name="egon")),
]
```

#### **使用Mixin**

我觉得要理解django的class-based-view（以下简称cbv），首先要明白django引入cbv的目的是什么。在django1.3之前，generic view也就是所谓的通用视图，使用的是function-based-view（fbv），亦即基于函数的视图。有人认为fbv比cbv更pythonic，窃以为不然。python的一大重要的特性就是面向对象。而cbv更能体现python的面向对象。cbv是通过class的方式来实现视图方法的。class相对于function，更能利用多态的特定，因此更容易从宏观层面上将项目内的比较通用的功能抽象出来。关于多态，不多解释，有兴趣的同学自己Google。总之可以理解为一个东西具有多种形态（的特性）。cbv的实现原理通过看django的源码就很容易明白，大体就是由url路由到这个cbv之后，通过cbv内部的dispatch方法进行分发，将get请求分发给cbv.get方法处理，将post请求分发给cbv.post方法处理，其他方法类似。怎么利用多态呢？cbv里引入了mixin的概念。Mixin就是写好了的一些基础类，然后通过不同的Mixin组合成为最终想要的类。

所以，理解cbv的基础是，理解Mixin。Django中使用Mixin来重用代码，一个View Class可以继承多个Mixin，但是只能继承一个View（包括View的子类），推荐把View写在最右边，多个Mixin写在左边。
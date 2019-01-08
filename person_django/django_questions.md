### 1. Django里QuerySet的get和filter方法的区别?

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
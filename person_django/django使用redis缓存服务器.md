# Django分析之使用redis缓存服务器

​        时间长没有更新了，这段时间一直忙着一个项目，今天就记录一个现在经常会用到的技术吧。

​        redis相信大家都很熟悉了，和memcached一样是一个高性能的key-value数据库，至于什么是缓存服务器，度娘都有很明白的介绍了，我在这里就不一一介绍了。

​        那我们一般什么情况下才会使用缓存服务器呢？可不是什么情况都需要的哦，一般来说是在需要频繁对一个字段读取的时候才会需要将这个字段放入到缓存服务器上，而且由于key-value数据库一般只是放很简单的数据，所以在选择保存的对象的时候要注意选择好。

​        下面我就来介绍如何在Django中配置使用redis数据库，首先是先安装redis了，在Ubuntu中执行下面这句命令：

```
#安装Redis服务器端
~ sudo apt-get install redis-server
```

​        然后为了能在Django中使用redis，还需要安装redis for Django的插件：

```
pip install django-redis
```

这是一个开源的项目，github地址是<https://github.com/niwibe/django-redis>，感谢作者。

​        那么现在就是在Django的settings中配置了。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        },
    },
}
REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

其实只是需要CACHES中的那几条就可以了，后面这三句可以不需要的，只是我后面的例子里需要用到，我就在这里配置了。

​      好了，现在连接和配置都已经完成了，那么在项目中该如何使用呢？接下来看下面这段例子吧。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from django.conf import settings
from django.core.cache import cache


#read cache user id
def read_from_cache(self, user_name):
    key = 'user_id_of_'+user_name
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data

#write cache user id
def write_to_cache(self, user_name):
    key = 'user_id_of_'+user_name
    cache.set(key, json.dumps(user_name), settings.NEVER_REDIS_TIMEOUT)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

通过上面的这两个方法就可以实现对redis的读取操作了，只需要将需要的字段当参数传入到方法中就好了。

那么之前提到的memcached呢？其实也是一样的配置：

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

​       当然用法也是和我上面的例子是一样的了。其实对于redis这样的缓存服务器来说，配置都是很简单的，而具体的使用也不难，官网上面也有很多简单明了的例子可以供我们参考，只有一点需要注意的，那就是对于要将什么样的信息保存到redis才是我们真正需要关心的。
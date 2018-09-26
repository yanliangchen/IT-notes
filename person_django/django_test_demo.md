### 1. 一个简单的Django测试实例

在创建Django应用时，默认已经生成了tests.py测试文件，打开FirstApp应用下tests.py文件，编写针对模型的测试用例。tests.py文件(test.py在app的下方)代码如下：

```
from django.test import TestCase
from FirstApp.models import Event, Guest

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name='tom1',status=True,limit=2000,
            address='beijing',start_time='2017-04-19 20:00:01')
        Guest.objects.create(id=1,event_id=1,realname='tom2',
            phone='13500001111',email='tom2@mail.com',sign=False)

    def test_event_models(self):
        result=Event.objects.get(name='tom1')
        self.assertEqual(result.address, "beijing")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result=Guest.objects.get(phone='13500001111')
        self.assertEqual(result.realname,"tom2")
        self.assertFalse(result.sign)
        
        
        

##########需要先定义模型 并且进行迁移#############

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):

    name = models.CharField(max_length=30)
    address= models.CharField(max_length=30)

class Guest(models.Model):

    realname= models.CharField(max_length=30)
    email= models.CharField(max_length=30)





##########我这里先写了个简单的############
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from  app1.models import  Event,Guest
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id =1 ,name='tom1',
            address='beijing')
        Guest.objects.create(id=1,realname='tom2',
            email='tom2@mail.com',)

    def test_event_models(self):
        result=Event.objects.get(name='tom1')
        self.assertEqual(result.address, "beijing")
        
       
1）首先创建ModelTest类，继承django.test.TestCase测试类。 
2）在setUp初始化方法中，分别创建一条发布会（Event）和一条嘉宾（Guest）数据。 
3）通过test_event_models()和test_guest_models()测试方法，分别查询创建的数据，并断言是否正确。



```

### 2. 运行测试用例的命令说明

```
1）运行FirstApp应用下的所有测试用例。



\FirstProject>python3 manage.py test FirstApp1

2）运行FirstApp应用下的tests.py测试文件。



\FirstProject>python3 manage.py test FirstApp.tests1

3）运行FirstApp应用tests.py测试文件下的ModelTest测试类。

\FirstProject>python3 manage.py test FirstApp.tests.ModelTest1

4）执行ModelTest测试类下面的test_event_models测试方法（用例）。

\FirstProject>python3 manage.py test FirstApp.tests.ModelTest1

5）使用-p（或–pattern）参数模糊匹配测试文件。

\FirstProject>python3 manage.py test -p test*.py1



```



### 3. 用代码访问网址的方法：

```
class  clinettest(TestCase):
    def test(self):
        from django.test import  Client
        c = Client()
        response = c.post('/login/',{'username': 'john', 'password': 'smith'})
        print(response.status_code)
     	
     	response = c.get('/customer/details/')
     	print(response.content)
     	'<!DOCTYPE html...'
     	
     	#默认情况下CSRF检查是被禁用的，如果测试需要，可以用下面的方法：
     	from django.test import Client
     	csrf_client = Client(enforce_csrf_checks=True)
     	
     	#使用 csrf_client 这个实例进行请求即可。
     	#指定浏览USER-AGENT:
     	c = Client(HTTP_USER_AGENT='Mozilla/5.0')
     	
     	#模拟post上传附件:
     	from django.test import Client 
     	c = Client()
     	with open('wishlist.doc') as fp:
     		c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})
     		
     	#测试网页返回状态:
     	from django.test import TestCase
 	    class SimpleTest(TestCase):
         	def test_details(self):
                response = self.client.get('/customer/details/')
                self.assertEqual(response.status_code, 200)

            def test_index(self):
                response = self.client.get('/customer/index/')
                self.assertEqual(response.status_code, 200)
		
     	#我们用 self.client 即可，不用 client = Client() 这样实例化，更方便，我们还可以继承 Client，添加一些其它方法:
     	
```





```
我们用 self.client 即可，不用 client = Client() 这样实例化，更方便，我们还可以继承 Client，添加一些其它方法:

from django.test import TestCase, Client
 
class MyTestClient(Client):
    # Specialized methods for your environment
    ...
     
class MyTest(TestCase):
    client_class = MyTestClient
 
    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()
```



```
定制 self.client 的方法：

from django.test import Client, TestCase
 
 
class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = Client(enforce_csrf_checks=True)
 
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```


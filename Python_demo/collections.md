## 1.Counter类

```

是hashtable对象的计数，是dict的子类，从2.7以后的版本加入。
计数器是我们常用的一个功能，collections中的Counter类就提供了此功能。
'''
# from  collections  import  *
# a = Counter()
# b = Counter("aaabbcccd")
# c = Counter({"a":10,"b":20})
# d = Counter(a=10,b=20)
# #来统计a的个数
# print(b["a"])
# #得到列表 列表里是传递字典的键值对以元祖的形式返回
# print(c.most_common())
```



## 2.defaultdict类

```
#!/usr/bin/env python
# coding:utf-8
#这个是对统计列表里之后第一个索引作为键，之后凡是这个键后面的值都append到列表里
#统计数据
# from collections import *
# def test_defaultdict():
#     members = [
#         ['male', 'john',],
#         ['male', 'jack'],
#         ['female', 'lilly'],
#         ['female', 'lucy']
#     ]
#     result_dic = defaultdict(list)
#     for  sex ,name  in   members:
#         result_dic[sex].append(name)
#     for  k, v  in   result_dic.items():
#         print(k,v)
# test_defaultdict()
```



## 3.OrderedDict类

```
把字典利用OrderedDict来进行排序，通过键，或者值，或者键的长度 从小到
```



```

```



## 4.namedtuple 

```
x,y,z  把列表里的数据给变成坐标，可以使用名称来命名。
```

```
from collections import *

def test_namedtuple():
    Point = namedtuple('Point','x y z')
    location = [10,20,30]
    p = Point._make(location)
    print (p,type(p))
    print("p.x is: ",p.x)
    print ("p.y is: ",p.y)
    print("p.z is：",p.z)
# test_namedtuple()
```



## 5.deque

```
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
```

```
import  sys
import  time
from  collections  import  deque
# fancy_loading = deque('>--------------------')
#先生成一个队列列表,所以要把它给弄成字符串
# print(fancy_loading,type(fancy_loading))
# while True:
#     print('%s' % ''.join(fancy_loading))
#     fancy_loading.rotate(1)
#     sys.stdout.flush()
#     time.sleep(0.08)
```





## 6.demo   倒计时

```
# for i in range(22, 0, -1):
#     print('\r%s' % i, end='') # end='' 默认为换行符\n ，修改为空不换行
#     time.sleep(1) # 暂停1秒
```



## 7.给字典加缺省值 如果没有  则给赋成默认的值

```
# from  collections import  defaultdict
# students = defaultdict(lambda :60)
# students['lili'] = 70
# students['gaofei'] = 80
# students['zhouxue'] = 90
# # print(students)

# from collections import  OrderedDict
# from  string import  ascii_uppercase
# #zip对象直接通过dict转成字典
# # print(dict(zip(ascii_uppercase,range(5))))
```





## 8.得到了一个元祖  ，之后通过属性 ， 获取其中的值

```
# from  collections import  namedtuple
# Students = namedtuple('Students','name,score,weight')
# #Students为一个类
# print(Students)
# #之后往这个类里传递参数得到一个对象
# s1 = Students(name='Leo',score=100,weight=65,)
# #得到一个元祖
# print(s1)
# #通过对象来访问属性，得到属性所对应的值
# print(s1.name)
```
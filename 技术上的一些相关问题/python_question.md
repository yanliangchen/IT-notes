### 1. 类继承

问题：有如下的一段代码：

```
class A(object):
    def show(self):
        print('base  show')

class B(A):
    def show(self):
        print('derived show')
obj = B()
obj.show()
如何调用 类A 的 show 方法？
答案：方法如下:
obj.__class__ = A
obj.show()

__class__方法指向了类对象，只用给他赋值类型A,然后调用方法show,但是用完了记得改回来
```



### 2. 方法对象

问题：为了让下面这段代码运行，需要增加哪些代码？

```
class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    
    def myprint(self):
        print('a =', self.__a, 'b =',self.__b)
    
    # 这段代码为后加上的
    def  __call__(self, num):
        print('call: ', num+self.__a)

al = A(10,20)
# 到这没问题
al.myprint()
# 为了能让对象实例被直接调用，需要实现__call__方法
al(80)
```



### 3.new和init +基于new单例模式

问题：下面这段代码输出什么？

```
class B(object):
    def fn(self):
        print('B fn')

    def __init__(self):
        print('B INIT')

class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls, a):
        print('NEW',a)
        if  a > 10:
            return  super(A,cls).__new__(cls)
        return B()

    def __init__(self,a):
        print("INIT",a)
a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()

答案 输出结果:
('NEW', 5)
B INIT
B fn
('NEW', 20)
('INIT', 20)
A fn

使用__new__方法，可以决定返回哪个对象，也就是创建对象之前，这个可以用于设计模式的单例,工厂模式，__init__是创建对象是调用的

```



**单例模式概念：**

```
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
在 Python 中，我们可以用多种方法来实现单例模式
```



**单例模式（基于new）**

```
语言是共通的，想要用不同语言实现单例模式，首先要清楚什么是单例模式，单例模式即一个类有且仅有一个实例，那么通过python怎么实现一个类只能有一个实例呢。
首先先创建一个类，比如宇宙只有一个地球


class Earth:
    pass

a = Earth()
print(id(a))
b = Earth()
print(id(b))

运行结果 :
86431215	
24131866

通过打印实例的id可以发现，地球类默认创建了两个实例。那么怎么能够让类只创建一个实例，而后再创建的实例是返回上一次的对象的引用呢？我们了解到，python中，一个类创建对象实例是通过调用父类object的 __new__(cls)方法来创建对象的我们可以通过重写 __new__(cls)方法去实现类只创建一个实例代码如下：


class Earth(object):

    __instance=None #定义一个类属性做判断

    def __new__(cls):

        if cls.__instance==None:

            #如果__instance为空证明是第一次创建实例

            #通过父类的__new__(cls)创建实例

            cls.__instance==object.__new__(cls)

            return  cls.__instance

        else:

            #返回上一个对象的引用

            return cls.__instance

a = Earth()
print(id(a))
b = Earth()
print(id(b))


运行结果：
1730389200
1730389200	

可以看出它们id相同，是同一个对象

```



**单例模式（使用模块）**

```
其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：
·mysingleton.py·
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
from a import singleton
```



**单例模式（装饰器）**

```
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kargs)
        return _instance[cls]

    return _singleton

@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
print(id(a1))
a2 = A(3)
print(id(a2))
```



### 4.全局和局部变量

问题: 下面这段代码输出什么？

```
num = 9 
def f1():
    num = 20
def f2():
	print(num)
f2()
f1()
f2()

#答案
9
9

num 不是全局变量,所以每个函数都得到了自己的num拷贝,如果你想修改num,则必须用global关键字声明。比如下面这样

num = 9 
def f1():
	global num 
	num = 20
def f2():
	print(num)

f2()
f1()
f2()

```



### 5.默认方法

问题：如下的代码

```
class  A(object):
	def __init__(self,a,b):
		self.a1 = a 
		self.b1 = b
     def mydefault(self):
     	print('default')
a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
#方法 fn1/fn2/fn3 都没有定义，添加代码，使没有定义的方法都调用 mydefault 函数，上面的代码应该输出
default
default
default 

#答案  
class  A(object):
	def __init__(self,a,b):
		self.a1 = a
		self.b1 = b
		print('init')
	def mydefault(self):
		print('default')
	def __getattr__(self,name)：
		return  self.mydefault
a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()

#方法__getattr__只有当没有定义的方法调用时，才是调用他。当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容.

class A(object):
	def __init__(self,a,b):
		self.a1 = a 
		self.b1 = b
		print('init')
	def mydefault(self,*args):
		print('default:'+str(args[0]))
	def __getattr__(self,name)
		print("other fn:",name)
		return  self.mydefault
a1 = A(10,20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)
		
```



### 6.包管理

问题：一个包里有三个模块，mod1.py ,  mod2.py ,  mod3.py ，但使用 from demopack import * 导入模块时，如何保证只有 mod1 、 mod3 被导入了。

答案:增加 __init__.py 文件，并在文件中增加：

```
__all__ = ['mod1',''mod3']
```





### 7. 闭包

问题：写一个函数，接收整数参数 n ，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。

```
#答案
def mulby(num):
	def gn(val):
		return num * val
	return  gn 
zw = mulby(7)
print(zw(9))
```



### 8. 性能

问题：解析下面的代码慢在哪

```
def strtest1(num):
	str = 'first'
	for  i  in  range(num):
		str+='X'
	return  str
	
#答案: python的str是个不可变的对象，每次迭代，都会生成新的str对象来存储新的字符，num越大，创建的str对象越多，内存消耗越大.
```



### 9. input()与raw_input()区别

```
内建函数input()是eval()和raw_input()的组合，等价于eval(raw_input())。类似于
raw_input()，input()有一个可选的参数，该参数代表了给用户的字符串提示。如果不给定参数的
话，该字符串默认为空串。
从功能上看,input 不同于raw_input()，因为raw_input()总是以字符串的形式，逐字地返回用
户的输入。input()履行相同的的任务；而且，它还把输入作为python 表达式进行求值。这意味着
input()返回的数据是对输入表达式求值的结果：一个python 对象。

input：你输入数字，不会报错  然而你输入一个字符串  系统不知道你输入的 ，会在系统库中寻找它，被理解了变量的名字，就会报错 ，数字是因为系统库里面有。
```





### 10. xrange()与range()



```
xrange() 内建函数
xrange() 类似 range() , 不过当你有一个很大的范围列表时, xrange() 可能更为适合, 因为
它不会在内存里创建列表的完整拷贝. 它只被用在 for 循环中, 在 for 循环外使用它没有意义。
同样地, 你可以想到, 它的性能远高出 range(), 因为它不生成整个列表。
```





### 11.网络编程

```
from socket import * 比 import socket 化简代码
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
化简为
tcpSock = socket(AF_INET, SOCK_STREAM)
[典型的通用服务端伪代码]：
    ss = socket()       # 创建服务器套接字
    ss.bind()           # 把地址绑定到套接字上
    ss.listen()         # 监听连接
    inf_loop:           # 服务器无限循环
    cs = ss.accept()    # 接受客户的连接
    comm_loop:          # 通讯循环
    cs.recv()/cs.send() # 对话（接收与发送）
    cs.close()          # 关闭客户套接字
    ss.close()          # 关闭服务器套接字（可选）
[典型的通用客户端伪代码]：
    cs = socket()       # 创建客户套接字
    cs.connect()        # 尝试连接服务器
    comm_loop:          # 通讯循环
    cs.send()/cs.recv() # 对话（发送／接收）
    cs.close()          # 关闭客户套接字
```



### 12. Python 对象之间赋值

```
Python 中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的 copy 模块。
copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
copy.deepcopy 深拷贝 拷贝对象及其子对象。
```





### 13. 关于自定义莫款相对路径引入报错

```
 因为主 module 的 name 总是为 main , 并没有层次结构, 也就无从谈起相对引用了。 换句话, if name=="main": 和相对引用是不能并存的。
 
#不写if  __name__ =='main':
导入进来的代码就会被执行  写了 就不会执行
```



### 14. python中%r和%s的区别

```
%r用rper()方法处理对象
%s用str()方法处理对象
>>> import datetime
>>> d = datetime.date.today()
>>> print "%s" % d
2015-10-30
>>> print "%r" % d
datetime.date(2015, 10, 30)
```



### 15. copy和deepcopy的区别

python2中，需要import copy模块

python3中，直接可以使用copy（）方法，但deepcopy（）还是需要导入copy模块

下面以python2为例

```
import copy
list = ['beijing','tianjin','hebei','wuhan','shandong']
list_copy = copy.copy(list)
list[0] = 'heilongjiang'
print(list)
print(list_copy)
运行结果：
['heilongjiang', 'tianjin', 'hebei', 'wuhan', 'shandong']
['beijing', 'tianjin', 'hebei', 'wuhan', 'shandong']
list改变了，list_copy没有跟着改变

那如果list里面包含了子列表呢
```

```
import copy
list = ['beijing','tianjin','hebei',['neimeng','xinjiang'],'wuhan','shandong']
list_copy = copy.copy(list)
list[3][0] = 'taiwan'
print(list)
print(list_copy)
结果显示：
['beijing', 'tianjin', 'hebei', ['taiwan', 'xinjiang'], 'wuhan', 'shandong']
['beijing', 'tianjin', 'hebei', ['taiwan', 'xinjiang'], 'wuhan', 'shandong']
为什么结果跟着变了呢，因为copy为浅copy，只复制了第一层数据，列表里存储的子列表，打印出来是子列表，其实，在内存里，列表里只是存储了子列表的内存地址，子列表在内存里是单独存储的
改变了子列表，再打印list_copy时，子列表内存地址地址没有变，打印出来自然是修改后的子列表

浅copy的实现方法：
l1 = list[:]
l2 = copy.copy(list)
l3 = list(list)

那浅copy的用处呢
比如两口子，共有一个账号存款
card = ['name',['saving',100]]#作为一个模板
husband = copy.copy（card）
wife = copy.copy(card)
husband[0]= 'zhangsan'
wife[0]='fengjie'
husband[1][1] = 50#丈夫取出50，还剩下50
print husband
print wife
结果显示：
['zhangsan', ['saving', 50]]
['fengjie', ['saving', 50]]
两个人的账号存款同时变动


那能不能完全copy呢，可以，使用命令deepcopy就可以
import copy
list = ['beijing','tianjin','hebei',['neimeng','xinjiang'],'wuhan','shandong']
list_copy = copy.deepcopy(list)
list[3][0] = 'taiwan'
print(list)
print(list_copy)
结果显示：
['beijing', 'tianjin', 'hebei', ['taiwan', 'xinjiang'], 'wuhan', 'shandong']
['beijing', 'tianjin', 'hebei', ['neimeng', 'xinjiang'], 'wuhan', 'shandong']
这样复制就不会改变子列表的值了，是因为deepcopy将子列表也复制了一份
注：不过，deepcopy方法，如果数据很大，完全复制就是存储两份数据，占用内存，慎用！
```
### 16.Python自省

```
自省就是面向对象的语言所写的程序在运行时，所能知道对象的类型，简单一句就是运行时能够获得对象的类型，比如type(),dir(),getattr(),hasattr(),isinstance().

a = [1,2,3]
b = {'a':1,'b':2,'c':3}
c = True
print type(a),type(b),type(c) # <type 'list'> <type 'dict'> <type 'bool'>
print isinstance(a,list)  # True
```



### 17. 什么是鸭子类型

```
在鸭子类型中，关注的不是对象的类型本身，而是他如何使用的。例如，在不适用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为鸭的对象，并调用它的走和叫方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。

class duck():
   def walk(self):
       print('I am duck,I can walk...')
   def swim(self):
       print('I am duck,I can swim...')
   def call(self):
       print('I am duck,I can call...')

duck1=duck()
duck1.walk()
     # I am duck,I can walk...
duck1.call()      # I am duck,I can call...
```

### 18. lamda

```
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
[18, 9, 24, 12, 27]
print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
#求和
print reduce(lambda x, y: x + y, foo)
139

lambda 定义了一个匿名函数
　　lambda 并不会带来程序运行效率的提高，只会使代码更简洁。
　　如果可以使用for...in...if来完成的，坚决不用lambda。
　　如果使用lambda，lambda内不要包含循环，如果有，我宁愿定义函数来完成，使代码获得可重用性和更好的可读性。
　　总结：lambda 是为了减少单行函数的定义而存在的。

```



### 19. pass

```
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
```



### 20. 列表推到是和字典推倒式

**列表推倒式**

当然，通过列表推导式我们还可以有更多操作：

```
vec = [-4, -2, 0, 2, 4]  #创建一个列表

#筛选出vec列表中所有大于0的元素
print([x for x in vec if x > 0])   #[2, 4]

#对vec列表每个元素应用函数，此处为求绝对值
print([abs(x) for x in vec])   #[4, 2, 0, 2, 4]

#为列表每个元素调用方法，此处为转换字母小写
freshfruit = ['baNana', 'loGANberRY ', 'pAssiON fRUIT']
print([fruit.lower() for fruit in freshfruit])   
#输出：['banana', 'loganberry ', 'passion fruit']

#生成两个列表中不相等元素可以组成的所有对的列表
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])   
#输出：[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

通过列表推导式我们能更方便简洁地创建列表，一般是对**序列**（字符串、列表、元组）或者是**可迭代对象**（py3中range()返回就是可迭代对象）中的元素进行某些操作来生成新的列表。

假如我们想快速创建一个包含0到5的平方值的列表，我们可以：

```
squares = []
for x in range(6):    #循环添加元素
    squares.append(x**2)
print(squares)      #[0, 1, 4, 9, 16, 25]1234
```

或者我们可以选择更简洁也更易读的方式：

```
squares = [x**2 for x in range(6)]  #直接使用列表推导式
print(squares)      #[0, 1, 4, 9, 16, 25]
```

当然，通过列表推导式我们还可以有更多操作：

```
vec = [-4, -2, 0, 2, 4]  #创建一个列表

#筛选出vec列表中所有大于0的元素
print([x for x in vec if x > 0])   #[2, 4]

#对vec列表每个元素应用函数，此处为求绝对值
print([abs(x) for x in vec])   #[4, 2, 0, 2, 4]

#为列表每个元素调用方法，此处为转换字母小写
freshfruit = ['baNana', 'loGANberRY ', 'pAssiON fRUIT']
print([fruit.lower() for fruit in freshfruit])   
#输出：['banana', 'loganberry ', 'passion fruit']

#生成两个列表中不相等元素可以组成的所有对的列表
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])   
#输出：[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```



**字典推倒式**

```
#生成以x为键，x平方为值的字典
print({x: x**2 for x in (2, 4, 6)})
#输出：{2: 4, 4: 16, 6: 36}

#快速将两个关联的列表以键值对的形式生成字典
names = ['trophy','jack','bob']
ages = [19,21,23]
print({name:age for (name, age) in zip(names,ages)})
#输出：{'trophy': 19, 'jack': 21, 'bob': 23}
```



### 21. Python自带的数据结构及方法

**1.列表**

    空列表：a=[]

    函数方法：a.append(3)     　　>>>[3]    

          a.extend([3,4,5])     　　>>>[3,3,4,5]    添加一个列表序列

          a.insert(1,'hello')    　　  >>>[3,'hello',3,4,5]

          a.remove(3)        　　　  >>>['hello',3,4,5] 删除第一个出现的3，没有3则报错

          a.pop()        　　　　　　>>>['hello',3,4]

          a.pop(0)        　　　　　　>>>[3,4]

          a.index(4)       　　 >>>1    返回出现的第一个4的下标

          a.count(3)        　　>>>1    列表中元素3的个数

          a.sort        >>>[3,4]    排序

          a.reverse()        >>>[4,3]    反序

    删除元素的方法

        a.remove(3)    通过值删除元素，删除第一个为参数值得元素

        a.pop()       通过下标删除元素，默认删除列表最后一个值，带参数则删除下标为参数值的元素

        del a[0]       通过下标删除元素，

            del a[2:4] 删除a表下标为2,3的元素

        del a[:]   删除a列表所有元素

        del a       删除列表

    列表推导式：

        vec = [2,4,6]    

         [3*x for x in vec if x<6]    >>>[6,12]    3*2,3*4

        vec2 = [1,2,3]

        [x*y for x in vec for y in vec2]    >>>[2,4,6,4,8,12,6,12,18]

    嵌套列表推导式：

        mat = [

        [1,2,3],

        [4,5,6],

        [7,8,9]

        ]

        print ([[row[i] for row in mat] for i in [0,1,2]])    

        >>>[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

```
    list (zip(mat)) 和 list (zip(*mat))结果会有什么不同  
	>>> [([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],)]
	>>> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```



**2.字典**

```
    d = {'Jack':'jack@mail.com','Tom':'Tom@main.com'}
    d['Jack']    　　　　　　　　>>>'jack@mail.com
    d['Jim'] = 'Jim@sin.com'    >>>{'Jim': 'Jim@sin.com', 'Jack': 'jack@mail.com', 'Tom': 'Tom@main.com'}              
　 del d['Jim']    >>>{'Jack': 'jack@mail.com', 'Tom': 'Tom@main.com'}
    list(d.keys())    将返回一个字典中所有关键字组成的无序列表
    sorted(d.keys()) 将返回一个字典中所有关键字组成的排序列表
    dict()    构造函数可以直接从key-value对中创建字典
    dict([('Tim',123),('Tiny',234)])    >>>{'Tiny': 234, 'Tim': 123}    
    推导式创建字典：
        {d2:d2+'@main.com' for d2 in list(d.keys())}
            >>>{'Jack': 'Jack@main.com', 'Tom': 'Tom@main.com'}
    循环输出字典中的键值对：
        for name,email in d.items():
            print(name,email)

```

### 22. 什么是python的命名空间

```
对象和命名空间是python学习的两大基石。

我们常常听到在python中，一切皆对象。是的，python所操作的数据，都是对象（是对象，就意味着他们有自己独有的方法或属性）。数字、字符串、函数、类，甚至是模块。对，模块也是对象。而在对象中，有一个很重要的角色，那就是命名空间。对象被加载到内存后，需要被调用或者说被引用，就需要有一个指针去指向这个对象，这个指针就是命名空间或者说名称空间。它严格来说只是一个指针或者说对一个对象的引用，你通过查找这个指针，就可以引用这个指针所指向的对象（内存地址中的代码片段）。

上面说数字、字符串、函数、类等都是对象，因此对象是可以被嵌套的，命名空间也是可以被嵌套的。每个被嵌套的命名空间，所引用的就是在这个空间里面的巴拉巴拉一串代码。代码在执行的时候，是以一个命名空间为单位进行执行的。也就是说，你在一个模块中下面的定义了很多类、函数、变量等，但是你在模块这一级别的命名空间中没有调用他们，那么python解释器在解释这个模块的时候，模块中的代码就不会被执行，python解释器只是解释了他们，就是说python解释器只是创建了一堆的命名空间而已；因此，如果被嵌套的命名空间中有错误的代码，也不会被报错（因为他们没被调用，他们只是被命名空间引用了而已），因为当执行到他们下一级嵌套的命名空间时候，python只是把那些一串巴拉巴拉代码赋值给了一个命名空间，而如果这个命名空间没有被python解释器解释的命名空间所调用，那么你可以在这个命名空间中肆意妄为。

看下面一段代码：

name = "wang"

def func():

print(name)

name = "panda"



print(name)

func()



上面的代码，如果不是在交互式命令模式下，一定是在某个模块下面定义的，假如是命名空间为__main__的模块中定义的，那么在这个模块级别的命名空间中，又嵌套定义了两个命名空间，name和func。python解释器在解释到func这个命名空间的时候，会把这个命名空间中的代码加载到内存，而不会执行（python解释器还没解释到func()）。

接下来python解释器解释print(name)，那么在模块级别的这个命名空间内有定义name，就会执行引用name命名空间中的代码片段，而这个代码片段只是一个"wang"这个字符串对象，就会直接把这个对象拿过来，然后打印到屏幕上。学了python面向对象比较深入的时候，你会发现之所以能够使用print打印，是因为这个对象本身有个__str__方法，所以打印出来的只是一串“wang”字符串，而不再是对象。

当python解释器解释到func()的时候，__main__命名空间就会去引用fun命名空间中的代码片段，而python在解释func命名空间的时候：

先解释“print(name)”，python就会搜索name这个命名空间，这里说下命名空间的搜索顺序：这里很重要，因为python代码的执行和调用，就是按照这个顺序执行和调用的

这个可以解释python变量在函数中的搜索顺序的本质，本质就是对命名空间的搜索顺序：

当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，按照如下顺序：

1、局部命名空间（local）：特指当前函数或类的方法。如果函数定义了一个局部变量 x，或一个参数 x，Python 将使用它，然后停止搜索。

2、全局命名空间（global）：特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python 将使用它然后停止搜索。

3、内置命名空间（build-in）：对每个模块都是全局的。作为最后的尝试，Python 将假设 x 是内置函数或变量。

4、如果 Python 在这些名字空间找不到 x，它将放弃查找并引发一个 NameError 异常，如，NameError: name 'aa' is not defined。

因此，python搜索name这个命名空间，首先搜索func命名空间是否有定义，发现func命名空间中有定义，但是它是在print(name)被解释之前被定义的，因此这里报错。


变量赋值：

看下面代码：

a = 1

b = a

b = 2

print(a,b)


上面代码，定义了两个命名空间a和b，第一行定义了命名空间a，并将它指向数字对象1，第二行是将命名空间a赋值给命名空间b，这样命名空间b也同样指向了数字对象1，第三行，对命名空间b进行了重新赋值。注意：是重新赋值，因为数字1是一个不可变对象，b并没有一种方法可以改变数字1这个对象中的内容，因此这个等于号的意思是重新赋值。

因此，上面的打印结果是1 2


再看下面代码：

a = [1,2,3,4]

b = a

b[0]=8

print(a,b)


这段代码和上面的代码有个本质的不同，就是a和b所引用的对象是一个可变对象，调用a或b的方法，可以修改引用对象中的内容。因为a和b所引用的是同一个对象，因此不管是调用a或者b去修改这个对象中的内容，都会引起a和b引用对象的改变，因此打印结果是：[8, 2, 3, 4] [8, 2, 3, 4]


这样，我们再去理解python的浅拷贝或者深拷贝，就很容易了。如果一个深拷贝的对象里面嵌套了N层命名空间，可以想象会额外消耗更多的内存资源。


本文来自 wangpanda6 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/wangpanda6/article/details/77718445?utm_source=copy 
```





### 23. 类的构造器

```
# __init__ 构造函数，在生成对象时调用
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，sex等属性绑上去.
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self.
# 有了__init__的方法后，创建实例的时候，传入参数便不能为空，必须传入与__init__中方法匹配的参数
# 而self代表的是类的实例，该参数不需要另外进行传入
class people2():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def hello(self):
        print('hello {0}'.format(self.name))
test = people2('fengjin','man')
test.hello()

本文来自 菜鸟之神 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/csdntt00/article/details/78462710?utm_source=copy 
```



### 24 . Python中docstring文档的写法

```
该写法根据Python的PEP 257文档总结。
类的函数称为方法（method），模块里的函数称为函数（function）
1. 每一个包，模块，类，函数，方法都应该包含文档，包括类的__init__方法

2. 包的文档写在__init__.py文件中

3. 文档有单行文档和多行文档

4. 单行文档： 
   1.不要重复函数的声明语句，例如：function(a, b) -> list
   2.指明做什么和返回什么，例如Do X and return a list.
   3.使用三引号，方便换行
   
5. 多行文档： 
   1.如果模块是一个脚本，也就是单文件程序，模块的文档应该写明脚本的使用方法
   2.模块的文档需要写明包含的类，异常，函数
   3.如果是包，在__init__.py中，写明包里面包含的模块，子包
   4.如果是函数或类方法，应该写明函数或方法的作用，参数，返回，副作用，异常和调用的限制等
   5.如果是类，写明类的行为，和实例参数，构造方法写在__init__中
   6.使用三引号，而且两个三引号都应该单独成行

单行例子：
def function(a, b):
    """Do X and return a list."""
多行例子：
def complex(real=0.0, imag=0.0):
    """Form a complex number.
    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```



### 25. 如何将一个数字转换成一个字符串?

```
1. str() 
2. repr()
3. ``    python3中不在使用了

str和repr区别：
	一种是通过str函数，他会把值转换为合理形式的字符串，以便用户可以理解；另一种是通过repr函数，她会创建一个字符串，以合法的Python表达式的形式来表示值。
```



### 26. 理解GIL全局锁

```
熟悉python的都知道，在C语言写的python解释器中存在全局解释器锁，由于全局解释器锁的存在，在同一时间内，python解释器只能运行一个线程的代码，这大大影响了python多线程的性能。而这个解释器锁由于历史原因，现在几乎无法消除。
python GIL 之所以会影响多线程等性能，是因为在多线程的情况下，只有当线程获得了一个全局锁的时候，那么该线程的代码才能运行，而全局锁只有一个，所以使用python多线程，在同一时刻也只有一个线程在运行，因此在即使在多核的情况下也只能发挥出单核的性能。
既然python在同一时刻下只能运行一个线程的代码，那线程之间是如何调度的呢？ 
对于有io操作的线程，当一个线程在做io操作的时候，因为io操作不需要cpu，所以，这个时候，python会释放python全局锁，这样其他需要运行的线程就会使用该锁。 
对于cpu密集型的线程，比如一个线程可能一直需要使用cpu做计算，那么python中会有一个执行指令的计数器，当一个线程执行了一定数量的指令时，该线程就会停止执行并让出当前的锁，这样其他的线程就可以执行代码了。 
由上面可知，至少有两种情况python会做线程切换，一是一但有IO操作时，会有线程切换，二是当一个线程连续执行了一定数量的指令时，会出现线程切换。当然此处的线程切换不一定就一定会切换到其他线程执行，因为如果当前线程 优先级比较高的话，可能在让出锁以后，又继续获得锁，并优先执行。
在做科学计算的时候是用的单线程，因为这种计算是需要CPU一直做计算的，如果用多线程反而会降低计算速度。

```

### 26.5 并行执行、串行执行和并发执行

```
并发执行是多道程序系统中多个程序（逻辑上互相独立）或者一个程序中的多个程序段在执行的过程当中，时间互相重叠，一个程序执行没结束，另一个已经开始。

并行执行是指一组程序按照独立的，不同步的速度执行，时间上不重叠；
串行就是指令一个一个的执行。并行是指令同时并行执行。

总结：
　　并发是指多个线程轮流执行（单核CPU）；
　　并行是指多个线程同时执行（多核CPU），微观上是同时的；
　　串行是指一个一个的执行，处理完一个才能处理下一个，不轮换；
```



### 27. martch 和 search的区别

```
1. match()函数只检测字符串开头位置是否匹配，匹配成功才会返回结果，否则返回None

import re
print(re.match("func", "function"))
# 打印结果 <_sre.SRE_Match object; span=(0, 4), match='func'>

print(re.match("func", "function").span())
# 打印结果  (0, 4)

print(re.match("func1", "function"))
# 打印结果 None

注意：print(re.match("func1", "function").span())会报错，因为取不到span


2. search()函数会在整个字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

import re
print(re.search("tion", "function"))
# 打印结果 <_sre.SRE_Match object; span=(4, 8), match='tion'>

print(re.search("tion", "function").span())
# 打印结果  (4, 8)

print(re.search("tion1", "function"))
# 打印结果 None

注意：print(re.search("tion1", "function").span())会报错，因为取不到tion1


3.re模块下的其他常用方法
import re

print(re.findall("a", "a aa ab ac"))  # 返回所有满足匹配条件的结果,放在列表里
# ['a', 'a', 'a', 'a', 'a']

print(re.split('[ab]', 'abcd'))  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

import re
ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果



注意：
1 findall的优先级查询：

import re

ret = re.findall('www.(baidu|jd).com', 'www.jd.com')
print(ret)  # ['jd']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|jd).com', 'www.jd.com')
print(ret)  # ['www.jd.com']

2 split的优先级查询

ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']

#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的。

```





### 28. 协程(摘自廖雪峰老师)



协程，又称微线程，纤程。英文名Coroutine。

协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

```
def A():
    print '1'
    print '2'
    print '3'

def B():
    print 'x'
    print 'y'
    print 'z'
```

假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

```
1
2
x
y
3
z
```

但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。

看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？

最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python对协程的支持还非常有限，用在generator中的yield可以一定程度上实现协程。虽然支持不完全，但已经可以发挥相当大的威力了。

来看例子：

传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

```
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)
```

执行结果：

```
[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK
```

注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：

1. 首先调用c.next()启动生成器；
2. 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
3. consumer通过yield拿到消息，处理，又通过yield把结果传回；
4. produce拿到consumer处理的结果，继续生产下一条消息；
5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”





### 28. with及上下文管理器的原理和应用

```
【Python】with及上下文管理器的原理和应用
摘自：https://blog.csdn.net/u013034226/article/details/82730014 
这篇博客主要总结with用法，自定义上下文管理器，以及__exit__的参数相关内容。
with 语句是 Pyhton 提供的一种简化语法，适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，with 语句主要是为了简化代码操作。
with：文件使用后自动关闭

# 创建一个文件test.txt，若存在则打开，写入Hello Python

# 创建/打开文件

f = open('test.txt', 'w')

f.write("Hello Python")

# 关闭这个文件

f.close()

 


# 使用with

with open('test.txt', 'w') as f:

    f.write('Python')
可以发现：通过 with 语句在编写代码时，会使代码变得更加简洁，不用再去关闭文件。
with的执行过程：
在执行 with 语句时，首先执行 with 后面的 open 代码
执行完代码后，会将代码的结果通过 as 保存到 f 中
然后在下面实现真正要执行的操作
在操作后面，并不需要写文件的关闭操作，文件会在使用完后自动关闭
 
with的执行原理
实际上，在文件操作时，并不是不需要写文件的关闭，而是文件的关闭操作在 with 的上下文管理器中的协议方法里已经写好了。当文件操作执行完成后， with语句会自动调用上下文管理器里的关闭语句来关闭文件资源。
上下文管理器
ContextManager ,上下文是 context 直译的叫法,在程序中用来表示代码执行过程中所处的前后环境。上下文管理器中有 __enter__ 和 __exit__ 两个方法，以with为例子，__enter__ 方法会在执行 with 后面的语句时执行，一般用来处理操作前的内容。比如一些创建对象，初始化等；__exit__ 方法会在 with 内的代码执行完毕后执行，一般用来处理一些善后收尾工作，比如文件的关闭，数据库的关闭等。

自定义一个上下文管理器，模拟with文件操作

class MyOpen(object):

    def __init__(self,path,mode):

        # 记录要操作的文件路径和模式

        self.__path = path

        self.__mode = mode

 

    def __enter__(self):

        print('代码执行到了__enter__......')

        # 打开文件

        self.__handle = open(self.__path,self.__mode)

        # 返回打开的文件对象引用, 用来给  as 后的变量f赋值

        return self.__handle

 

    # 退出方法中，用来实现善后处理工作

    def __exit__(self, exc_type, exc_val, exc_tb):

        print('代码执行到了__exit__......')      

        self.__handle.close()

 

# a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

with MyOpen('test.txt','a+') as f:

    # 创建写入文件

    f.write("Hello Python!!!")

    print("文件写入成功")
执行结果：

通过执行顺序，可以看到文件写入操作执行完之后，自动调用了__exit__方法，做了善后处理工作。
 
__exit__方法的参数
__exit__ 方法中有三个参数，用来接收处理异常，如果代码在运行时发生异常，异常会被保存到这里。 
exc_type : 异常类型
exc_val : 异常值
exc_tb : 异常回溯追踪

# 编写两个数做除法的程序，然后给除数穿入0

class MyCount(object):

    # 接收两个参数

    def __init__(self,x, y):

        self.__x = x

        self.__y = y

    # 返回一个地址（实质是被as后的变量接收），实例对象就会执行MyCount中的方法:div()

    def __enter__(self):

        print('代码执行到了__enter__......')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("代码执行到了__exit__......")

        if exc_type == None:

            print('程序没问题')

        else:

            print('程序有问题，如果你能你看懂，问题如下：')

            print('Type: ', exc_type)

            print('Value:', exc_val)

            print('TreacBack:', exc_tb)


        # 返回值决定了捕获的异常是否继续向外抛出

        # 如果是 False 那么就会继续向外抛出，程序会看到系统提示的异常信息

        # 如果是 True 不会向外抛出，程序看不到系统提示信息，只能看到else中的输出

        return  True


    def div(self):

        print("代码执行到了除法div")

        return self.__x / self.__y

 
with MyCount(1, 0) as mc:
    mc.div()
执行结果：

可以看到，系统没有抛出异常，而是__exit__捕获到了异常，并按照我们的方式进行了抛出。
```



### 29.python反转字符串

```
def reverse3(s):
 l=list(s)
 l.reverse()
 print("".join(l))
reverse3("soifmi34pomOsprey，，是")
```



### 30.python垃圾回收机制

#### 引用计数机制

python里每一个东西都是对象，它们的核心就是一个结构体：`PyObject`

```
 typedef struct_object {
 int ob_refcnt;
 struct_typeobject *ob_type;
} PyObject;
```

PyObject是每个对象必有的内容，其中`ob_refcnt`就是做为引用计数。当一个对象有新的引用时，它的`ob_refcnt`就会增加，当引用它的对象被删除，它的`ob_refcnt`就会减少

```
#define Py_INCREF(op)   ((op)->ob_refcnt++) //增加计数
#define Py_DECREF(op) \ //减少计数
    if (--(op)->ob_refcnt != 0) \
        ; \
    else \
        __Py_Dealloc((PyObject *)(op))
```

当引用计数为0时，该对象生命就结束了。

引用计数机制的优点：

1. 简单
2. 实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。实时性还带来一个好处：处理回收内存的时间分摊到了平时。

引用计数机制的缺点：

1. 维护引用计数消耗资源
2. 循环引用

```
list1 = []
list2 = []
list1.append(list2)
list2.append(list1)
```

list1与list2相互引用，如果不存在其他对象对它们的引用，list1与list2的引用计数也仍然为1，所占用的内存永远无法被回收，这将是致命的。

 对于如今的强大硬件，缺点1尚可接受，但是循环引用导致内存泄露(随着时间的推移, 连接创建分配内存, 连接断开并没有释放掉内存, 所以 就会产生内存泄露. )，注定python还将引入新的回收机制。(标记清除和分代收集)

 

 

####  标记清楚机制

 标记-清除



"标记-清除"是为了解决循环引用的问题.可以包含其他对象引用的容器对象(比如:list,set,dict,class,instance)都可能产生循环引用.

 

我们必须承认一个事实,如果两个对象的引用计数都为1,但是仅仅存在他们之间的循环引用,那么这两个对象都是需要被回收的,也就是说,它们的引用计数虽然表现为非0,但实际上有效的引用计数为0.我们必须先将循环引用摘掉,那么这两个对象的有效计数就现身了.假设两个对象为A、B,我们从A出发,因为它有一个对B的引用,则将B的引用计数减1;然后顺着引用达到B,因为B有一个对A的引用,同样将A的引用减1,这样,就完成了循环引用对象间环摘除.

 

但是这样就有一个问题,假设对象A有一个对象引用C,而C没有引用A,如果将C计数引用减1,而最后A并没有被回收,显然,我们错误的将C的引用计数减1,这将导致在未来的某个时刻出现一个对C的悬空引用.这就要求我们必须在A没有被删除的情况下复原C的引用计数,如果采用这样的方案,那么维护引用计数的复杂度将成倍增加.

 

原理:"标记-清除"采用了更好的做法,我们并不改动真实的引用计数,而是将集合中对象的引用计数复制一份副本,改动该对象引用的副本.对于副本做任何的改动,都不会影响到对象生命走起的维护.

 

#### 分代回收机制

 

背景:分代的垃圾收集技术是在上个世纪80年代初发展起来的一种垃圾收集机制,一系列的研究表明:无论使用何种语言开发,无论开发的是何种类型,何种规模的程序,都存在这样一点相同之处.即:一定比例的内存块的生存周期都比较短,通常是几百万条机器指令的时间,而剩下的内存块,起生存周期比较长,甚至会从程序开始一直持续到程序结束.

 

从前面"标记-清除"这样的垃圾收集机制来看,这种垃圾收集机制所带来的额外操作实际上与系统中总的内存块的数量是相关的,当需要回收的内存块越多时,垃圾检测带来的额外操作就越多,而垃圾回收带来的额外操作就越少;反之,当需回收的内存块越少时,垃圾检测就将比垃圾回收带来更少的额外操作.为了提高垃圾收集的效率,采用"空间换时间的策略".

 

原理:将系统中的所有内存块根据其存活时间划分为不同的集合,每一个集合就成为一个"代",垃圾收集的频率随着"代"的存活时间的增大而减小.也就是说,活得越长的对象,就越不可能是垃圾,就应该减少对它的垃圾收集频率.那么如何来衡量这个存活时间:通常是利用几次垃圾收集动作来衡量,如果一个对象经过的垃圾收集次数越多,可以得出:该对象存活时间就越长.

 

### 31. 去除列表中重复的元素

```
2.去除列表中的重复元素

用集合

list(set(l))

用字典

l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
print (l2)

列表推导

l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
```



### 32. 关于sql的几个重要的点，你会了吗?

https://mp.weixin.qq.com/s/BIa3CU73JEGQOzHfs0_X0w

### 33. 画出TCP三次握手，四次挥手断开示意图。

https://www.cnblogs.com/qq78292959/p/3922231.html

### 34. MySQL半同步复制

https://www.cnblogs.com/ivictor/p/5735580.html

### 35.Python是如何进行类型转换的。

答  :  通过函数来进行转换

### 36.请写出一段python代码实现删除一个list里面的重复元素。

#### （1.）方法1.

```
方法1：使用set函数 

s=set(list)，然后再list(s)

```

#### （2.）方法2. append

```
def delList(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

print(delList([1,8,8,3,9,3,3,3,3,3,6,3]))
```

#### (3.)  方法3.

```
def delList(L):
    for i in L:
        # 看列表里的元素有几个，count方法进行计数
        # print(L.count(i))
        # 如果不为1 （证明重复） 留一个
        if L.count(i) != 1:
        	#之后通过索引留一个
            for x in range((L.count(i)-1)):
                L.remove(i)
    return L

print(delList([1,2,2,3,3,4,5]))
print(delList([1,8,8,3,9,3,3,3,3,3,6,3]))
```





### 37.python中类方法，类实例方法，静态方法有何区别？

Python中至少有三种比较常见的方法类型，即实例方法，类方法、静态方法。它们是如何定义的呢？如何调用的呢？它们又有何区别和作用呢？且看下文。

首先，这三种方法都定义在类中。下面我先简单说一下怎么定义和调用的。（PS：实例对象的权限最大。）

**实例方法**

​    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；

​    调用：只能由实例对象调用。

**类方法**

​    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；

​    调用：实例对象和类对象都可以调用。

**静态方法**

​    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；

​    调用：实例对象和类对象都可以调用。

#### 37.1 实例方法

简而言之，实例方法就是类的实例能够使用的方法。这里不做过多解释。

#### 37.2 类方法

使用装饰器@classmethod。

原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法。另外，如果需要继承，也可以定义为类方法。

如下场景：

假设我有一个学生类和一个班级类，想要实现的功能为：
    执行班级人数增加的操作、获得班级的总人数；
    学生类继承自班级类，每实例化一个学生，班级人数都能增加；
    最后，我想定义一些学生，获得班级中的总人数。

**思考**：这个问题用类方法做比较合适，为什么？因为我实例化的是学生，但是如果我从学生这一个实例中获得班级总人数，在逻辑上显然是不合理的。同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''

a = Student()
b = Student()
print(ClassTest.getNum())
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 37.2 静态方法

使用装饰器@staticmethod。

静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个**独立的、单纯的**函数，它仅仅托管于某个类的名称空间中，便于使用和维护。

譬如，我想定义一个关于时间操作的类，其中有一个获取当前时间的函数。

```
import time

class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())
t = TimeTest(2, 10, 10)
nowTime = t.showTime()
print(nowTime)
```

如上，使用了静态方法（函数），然而方法体中并没使用（也不能使用）类或实例的属性（或方法）。若要获得当前时间的字符串时，并不一定需要实例化对象，此时对于静态方法而言，所在类更像是一种名称空间。

其实，我们也可以在类外面写一个同样的函数来做这些事，但是这样做就打乱了逻辑关系，也会导致以后代码维护困难。

以上就是我对Python的实例方法，类方法和静态方法之间的区别和作用的简要阐述。





### 38. 如何用Python来进行查询和替换一个文本字符串

答：

```
find()方法可以在一个较长的字符串中查找子串，返回子串坐在位置的最左端索引

replace()方法返回某字符串的所有匹配项均被替换之后得到的字符串

可能这里问的是正则表达式的东西！！！

一、http://www.mianwww.com/html/2009/03/3258.html

可以使用sub()方法来进行查询和替换，sub方法的格式为：sub(replacement, string[, count=0])

replacement是被替换成的文本

string是需要被替换的文本

count是一个可选参数，指最大被替换的数量

例子：

import re
p = re.compile(‘(blue|white|red)’)
print(p.sub(‘colour’,'blue socks and red shoes’))
print(p.sub(‘colour’,'blue socks and red shoes’, count=1))

输出：

colour socks and colour shoes
colour socks and red shoes

subn()方法执行的效果跟sub()一样，不过它会返回一个二维数组，包括替换后的新的字符串和总共替换的数量

例如：

import re
p = re.compile(‘(blue|white|red)’)
print(p.subn(‘colour’,'blue socks and red shoes’))
print(p.subn(‘colour’,'blue socks and red shoes’, count=1))

输出

(‘colour socks and colour shoes’, 2)

(‘colour socks and red shoes’, 1)
```



### 39.python中变量的作用域，变量的查找顺序。

```
变量查找顺序：

LEGB ： locals -> enclosing function -> globals -> builtins

locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间
```



### 40.python中如何动态获取和设置对象	的属性？

```

```


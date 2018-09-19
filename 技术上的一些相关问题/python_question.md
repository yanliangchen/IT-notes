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



### 3.new和init

问题：下面这段代码输入什么？

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


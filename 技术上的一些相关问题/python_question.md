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


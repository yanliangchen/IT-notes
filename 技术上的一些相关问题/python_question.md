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



### 










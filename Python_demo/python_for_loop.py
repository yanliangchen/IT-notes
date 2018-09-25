#encoding=utf-8
'''
for...in是最常用的语句，for循环用于迭代容器对象中的元素，
这些对象可以是列表、元组、字典、集合、文件，甚至可以是自定义类或者函数

for 循环背后执行原理
for 循环是对容器进行迭代的过程，什么是迭代？迭代就是从某个容器对象中逐个地读取元素，直到容器中没有更多元素为止。
那么，哪些对象支持迭代操作？任何对象都可以吗？先随便自定义一个类试试，看行不行：
'''
'''
class MyRange:
  def __init__(self, num):
      self.num = num

 for i in MyRange(10):
    print(i)

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'MyRange' object is not iterable
'''

'''
错误堆栈日志非常清楚地告诉我们，MyRange 不是一个可迭代对象，所以它不能用于迭代，那么到底什么样的对象才称得上是可迭代对象(iterable)呢？
可迭代对象需要实现__iter__方法，并返回一个迭代器，什么是迭代器呢？迭代器只需要实现 __next__方法。
现在我们就来验证一下列表为什么支持迭代：
>>> x = [1,2,3]
>>> its = x.__iter__() # x有此方法，说明列表是可迭代对象
>>> its
<list_iterator object at 0x100f32198>

>>> its.__next__() # its有此方法，说明its是迭代器
1
>>> its.__next__()
2
>>> its.__next__()
3
>>> its.__next__()
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
StopIteration

从试验结果来看，列表是一个可迭代对象，因为它实现了 __iter__方法，并且返回了一个迭代器对象（list_iterator），因为它实现了 __next__方法。我们看到它不断地调用__next__方法，其实就是不断地迭代获取容器中的元素，直到容器中没有更多元素抛出 StopIteration 异常为止。

那么 for 语句又是如何循环的呢？到这里，恐怕你也猜到了，它的步骤是：
  先判断对象是否为可迭代对象，不是的话直接报错，抛出TypeError异常，是的话，调用 __iter__方法，返回一个迭代器
  不断地调用迭代器的__next__方法，每次按序返回迭代器中的一个值
  迭代到最后，没有更多元素了，就抛出异常 StopIteration，这个异常 python 自己会处理，不会暴露给开发者

对于元组，字典，字符串也是同样的道理，弄明白了 for 的执行原理之后，我们就可以实现自己的迭代器用在 for 循环中。
'''

'''
前面的 MyRange 报错是因为它没有实现迭代器协议里面的这两个方法，现在继续改进：
'''

'''
class MyRange():
    def __init__(self,num):
        self.i = 0
        self.num =num
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.num:
            i = self.i
            self.i += 1
            return  i
        else:
            #达到某个条件时必须抛出此异常，否则会无止境地迭代下去
            raise StopIteration
'''
#因为它实现了__next__方法，所以 MyRange 本身已经是一个迭代器了，所以 __iter__返回的就是对象本身 self。现在用在 for 循环中试试：
'''
for  i  in  MyRange(3):
    print(i)
#输出
0
1
2
'''




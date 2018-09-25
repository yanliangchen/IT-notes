#encoding=utf-8
#实现1
'''
def fibonacci():
    # 输入想要多少个项
    num = input(" your  number \n")
    i, a, b = 0, 0, 1
    if  int(num) < 0:
        print(u"你输入的数据不合理")
    elif int(num) == 1:
        print(a)
    else:
        while i < int(num):
            print(a,'a','-----',b,'b')
            #1. a起初始0 b初始为1
            #2. b给到a a=1
            #3. b=a+b  a=b
            a, b = b,a+b
            i+=1
fibonacci()
'''

'''
#实现2 使用列表的方式实现
# num还是几项
def fibonacci(num):
    #0 1 1
    fibs = [0,1]
    # num-2的目的是考虑到0，1这两个数字的条件，之后让他们排除在外
    for i in range(num-2):
        # 保证追加的元素是后两个元素
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs)
fibonacci(10)
'''

#实现三:
# 以上两种方式，都是直接调用的函数中的print打印，return值为none，因此无法进行复用。
# 将return为一个序列，可以直接复用该序列。
'''
def fibonacci(num):
    fibs = [0,1]
    for i in range(num-2):
        fibs.append(fibs[-2]+fibs[-1])   #倒数第二个+倒数第一个数的结果，追加到列表
    return(fibs)
fibonacci(5)
res = fibonacci(num=10)
print(res)
'''

#或者

'''
def fab_demo2(max):
    a, n, b = 0,0,1
    lis = []
    while n <max:
        lis.append(b)
        a,b = b,a+b
        n += 1
    print(lis)
    return lis

fab_demo2(10)
'''

#实现4:
# 可以复用了,，但是考虑到后期若要存储在list中的数据量过大，比较吃内存浪费资源，应该怎么办呢，
# 此时，考虑到利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class

'''
class Fab(object):
    def __init__(self,max):
        self.max = max
        self.n ,self.a ,self.b = 0 ,0 ,1

    def __iter__(self):        #继承object，重写__iter__后，自动调用__next__方法，返回r对象
        return self

    #如果一个类想被用于for ... in循环，类似list或tuple那样
    #就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    #然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
    #直到遇到StopIteration错误时退出循环。

    def next(self):        #此处python2为next，python3为__next__，注意区别
        if self.n < self.max:
            r = self.b
            self.a , self.b = self.b , self.a + self.b
            self.n += 1
            return r
        raise StopIteration()
#Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：
# for i in Fab(5):
#     print(i)
#或者
print(next(iter(Fab(5))))
'''
x = [1,2,3]
its = x.__iter__()
res = its.next()


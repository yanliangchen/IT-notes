###  1. enumerate 操作列表取值带索引序号

```
#demo1 对于一个列表，或者说一个序列我们经常需要打印它的index,一般传统的做法或者说比较low的写法：
cities = ['北京','上海','广州','深圳']
# i = 0
# for c in cities:
#     print(i+1,'-->',c)
#     i+=1

# 更优雅的写法是多用enumerate
# for i,city in  enumerate(cities):
#     print(i+1,'-->',city)
```



### 2.对列表长的情况用zip

```
#demo2 两个序列的循环  比较low的方法用下标去循环处理
# names = ['leo', 'jack', 'john', 'james']*250
# colors = ['red', 'green', 'blue', 'yellow']*250
# n = min(len(names), len(colors))
# print(n)
# for i  in range(n):
#     print(names[i],'-->',colors[i])

#更优雅一点的方法:用zip轻松搞定,zip对两个列表进行压缩
# for name,color in  zip(names,colors):
#     print(name,'-->',color)
```

### 3.交换变量

```

# #demo3变量交换  low
# x=1
# y=2
# print('>>Before:x={},y={}'.format(x,y))
# tmp = y
# y = x
# x = tmp
# print('>>After:x={},y={}'.format(x,y))

#优雅的做法
# x=1
# y=2
# print('Before:x={},y={}'.format(x,y))
# x,y =y,x
# print('After:x={},y={}'.format(x,y))
```



### 4.获取字典的值

```

#demo4 字典的读取  get  如果没有的话 则给设置一个空值
# Students = {
#     'Lili':18,
#     'Sam':25
# }
# student = Students.get('Lilia','??')
# print('Susan is {} years old '.format(student))
```



### 5.查找列表

```
#demo5 循环查找
# target_letter = 'd'
# letters = ['a', 'b','c','d','e']
# found = False
# for  letter   in  letters:
#     if letter == target_letter:
#         print('Found')
#         found=True
#         break
#     if  not  found:
#         print('Not foundaaaa')

#更优雅的写法： for  else  循环完了  还没有结果 就到else区间了
# target_letter = 'd'
# letters = ['a','b','c','e']
# for letter in letters:
#     if letter == target_letter:
#         print('Found')
#         break
# else:
#     print('Not found')

```



### 6.文件读取

```

#demo6文件读取查找
#通常来说，我们要打开一个文件，然后对文件的内容进行循环读取和处理，菜鸟的写法如下：
# f = open('./data.txt')
# try:
#     text = f.read()
#     for  line in  text.split('\n'):
#         print(line)
# finally:
#     f.close()

#更优雅的写法
# with  open('data.txt') as  f :
#     for line in  f :
#         print(line.strip('\n'))


```



### 7.锁的写法

```
#demo7 关于锁的写法
# 对于并发操作尤其是多线程的操作，我们对同一块内存进行读写操作的时候，通常我们都加锁保护的，想当然的写法如下：
# import  threading
# lock = threading.Lock()
# lock.acquire()
# try:
#     print('Citical part,do something....')
# finally:
#     lock.release()
# print(1111)
# #更好的写法
# lock = threading.Lock()
# with lock:
#     print('Citical part,do something....')
```


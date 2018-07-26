摘自 ： https://blog.csdn.net/liuchunming033/article/details/39080457



## **1.日志级别**

```
日志一共分成5个等级，从低到高分别是：DEBUG INFO WARNING ERROR CRITICAL。
DEBUG：详细的信息,通常只出现在诊断问题上
INFO：确认一切按预期运行
WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
ERROR：更严重的问题,软件没能执行一些功能
CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。
```



## 2.日志输出

有两种方式记录跟踪，一种输出控制台，另一种是记录到文件中，如日志文件。



### 2.1 将日志输出到控制台

```
通过logging.basicConfig函数对日志的输出格式及方式做相关配置，上面代码设置日志的输出等级是WARNING级别，
意思是WARNING级别以上的日志才会输出。另外还制定了日志输出的格式。
```

```
# # coding=utf-8
# import logging
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # use logging
# logging.info('this is a loggging info message')
# logging.warning('this is loggging a warning message')
# logging.debug('this is a loggging debug message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')
```

### 2.2 将日志输出到文件

```
	我们还可以将日志输出到文件，只需要在logging.basicConfig函数中设置好输出文件的文件名和写文件的模式。
```



```
# coding=utf-8
# __author__ = 'liu.chunming'
# import logging
# logging.basicConfig(level=logging.WARNING,
#                     filename='./log.txt',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # use logging
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
```



### 2.3 既要把日志输出到控制台，还要写入日志文件

#### 2.3.1 Logger

```
这就需要一个叫作Logger 的对象来帮忙，下面将对他进行详细介绍，现在这里先学习怎么实现把日志既要输出到控制台又要输
出到文件的功能。
```

#### 2.3.2 操作步骤

```
第一步，创建一个logger；
第二步，创建一个handler，用于写入日志文件；
第三步，再创建一个handler，用于输出到控制台；
第四步，定义handler的输出格式；第五步，将logger添加到handler里面。这段代码里面提到了好多概念，包括：Logger，Handler，Formatter。后面讲对这些概念进行讲解。
```

```
# import logging
#
# # 第一步，创建一个logger
#
# logger = logging.getLogger()
#
# logger.setLevel(logging.INFO)  # Log等级总开关
#
# # 第二步，创建一个handler，用于写入日志文件
#
# logfile = './logger.txt'
#
# fh = logging.FileHandler(logfile, mode='w')
#
# fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
#
# # 第三步，再创建一个handler，用于输出到控制台
#
# ch = logging.StreamHandler()
#
# ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
#
# # 第四步，定义handler的输出格式
#
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#
# fh.setFormatter(formatter)
#
# ch.setFormatter(formatter)
#
# # 第五步，将logger添加到handler里面
#
# logger.addHandler(fh)
#
# logger.addHandler(ch)
#
# # 日志
#
# logger.debug('this is a logger debug message')
#
# logger.info('this is a logger info message')
#
# logger.warning('this is a logger warning message')
#
# logger.error('this is a logger error message')
#
# logger.critical('this is a logger critical message')
```



## 3.多个模块中日志输出顺序

```
通常我们的工作中会有多个模块都需要输出日志。那么，具有调用关系的模块之间，它门的日志输出顺序是怎么样的？我们来演示下：
假设有两个文件，分别是util.py：
```

```
##############util.py

__author__ = 'liu.chunming'

import logging

def fun():

    logging.info('this is a log in util module')


##############main.py

# coding=utf-8

__author__ = 'liu.chunming'

import logging

import util

logging.basicConfig(level=logging.INFO,

                    filename='./log/log.txt',

                    filemode='w',

                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def main():
    logging.info('main module start')

    util.fun()

    logging.info('main module stop')

if __name__ == '__main__':
    main()
```



## 4.日志格式说明

```
logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用的信息，如上例所示：
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
我在工作中给的常用格式在前面已经看到了。就是：
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容。
```



## 5.高级进阶

### 5.1 日志组建loggers、handlers,filters,formatters.Logger

```
下来学习一些日志组件以及一些高级部分。日志组件包括：loggers、handlers,filters,formatters.Logger 对象扮演了三重角色.首先,它暴露给应用几个方法以便应用可以在运行时写log.其次,Logger对象按照log信息的严重程度或者根据filter对 象来决定如何处理log信息(默认的过滤功能).最后,logger还负责把log信息传送给相关的loghandlers.Handler对象负责分配合适的log信息(基于log信息的严重 程度)到handler指定的目的地.Logger对象可以用addHandler()方法添加零个或多个handler对象到它自身.一个常见的场景 是,一个应用可能希望把所有的log信息都发送到一个log文件中去,所有的error级别以上的log信息都发送到stdout,所有critical 的log信息通过email发送.这个场景里要求三个不同handler处理,每个handler负责把特定的log信息发送到特定的地方.
```

```
# import logging
# import os
# #获取当前路径
# FILE=os.getcwd()
# print(FILE)
# #level设置级别 ，一旦设置低级别了 ，它就都打印出来了 ，如果设置高级别，则不打印出低级别的log
# logging.basicConfig(level=logging.ERROR,
#                     format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename = os.path.join(FILE,'log.txt'),
#                     filemode='w')
# logging.info('msg')
# logging.debug('msg2')
# logging.error('msg3')
# logging.warning('msg4')
# logging.critical('msg5')
```



### 5.2 logging.getLogger([name])

```
 创建Logger对象。日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称（注：多次使用相同名称 
来调用getLogger，返回的是同一个对象的引用。），Logger实例之间有层次关系，这些关系通过Logger名称来体现，如：
  例子中，p是父logger, c1,c2分别是p的子logger。c1, c2将继承p的设置。如果省略了name参数, 
getLogger将返回日志对象层次关系中的根Logger。
```

```
#1.
# import  logging
#
# p = logging.getLogger("root")
# c1 = logging.getLogger("root.c1")
# c2 = logging.getLogger("root.c2")

#2.
# import logging
# '''命名'''
# log2=logging.getLogger('BeginMan')  #生成一个日志对象
# print (log2 ) #<logging.Logger object at 0x00000000026D1710>
#
# '''无名'''
# log3 = logging.getLogger()
# print( log3 ) #<logging.RootLogger object at 0x0000000002721630> 如果没有指定name，则返回RootLogger
#
# '''最好的方式'''
# log = logging.getLogger(__name__)#__name__ is the module’s name in the Python package namespace.
# print (log )  #<logging.Logger object at 0x0000000001CD5518>  Logger对象
# print (__name__ ) #__main__
```





## Logger对象

```
通过logging.getLogger(nam)来获取Logger对象
Class logging.Logger
有如下属性和方法：
```

#### 1.Logger.propagate

```
print log.propagate 
具体参考：http://docs.python.org/2.7/library/logging.html
```

#### 2.Logger.setLevel(lvl)

```
设置日志的级别。对于低于该级别的日志消息将被忽略
```

```
# import  logging
# import  os
# logging.basicConfig(format="%(levelname)s,%(message)s",filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# log = logging.getLogger('root.set')# Logger对象
# print(log.propagate)
# log.setLevel(logging.WARN) #设置日志级别
# log.info('msg')#不会被记录
# log.debug('msg2')#不会被记录
# log.warning('msg')
# log.error('msg')
```

#### 3.Logger.debug(msg[,*args[,**kwargs]])

```
记录DEBUG级别的日志信息。参数msg是信息的格式，args与kwargs分别是格式参数.
```

```
# import  logging
# import  os
logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# log = logging.getLogger('root')
# log.debug('%s, %s, %s',*('error', 'debug', 'info'))
# log.debug('%(module)s, %(info)s',{'module': 'log', 'info': 'error'})
```

#### 4.Logger.log(lvl,msg[,*args[,**kwargs]])

```
记录日志，参数lvl用户设置日志信息的级别。参数msg, *args, **kwargs的含义与Logger.debug一样。
```

```
# import  logging
# from  logging import  log
# log.log(logging.ERROR,'%(module)s %(info)s',{'module':'log日志','info':'error'})#ERROR,log日志 error
# log.log(logging.ERROR,'再来一遍：%s,%s',*('log日志','error'))#ERROR,再来一遍:log日志，error
```

```
import logging
import os
logging.basicConfig(format="%(levelname)s,%(message)s",filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
log = logging.getLogger('root')   #Logger对象
try:
    #执行代码  之后手抛了个异常
    print(11111)
    raise  Exception
    #捕获异常，之后日志打印了异常
except:
    log.exception('exception')  #异常信息被自动添加到日志消息中
# 打开文件，显示如下：
'''ERROR,exception
Traceback (most recent call last):
  File "E:\project\py\src\log3.py", line 12, in <module>
    raise Exception,u'错误异常'
# Exception: 错误异常
'''
```
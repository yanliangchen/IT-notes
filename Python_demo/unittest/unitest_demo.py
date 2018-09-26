#-*- coding:utf-8 -*-
#摘自 ：https://www.cnblogs.com/feng0815/p/8045850.html  （中间版本存在问题，这里python2.7）

# python官方文档-unittest : https://docs.python.org/2/library/unittest.html#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
# 初试测试
import  unittest
def division_funtion(x, y):
    return round(float(x) / y, 6)

class TestDivision(unittest.TestCase):
    def test_int(self):
        self.assertEqual(division_funtion(1,1),1)

    def test_int2(self):
        self.assertEqual(division_funtion(9, 4), 2.25)

    def test_float(self):
        self.assertEqual(division_funtion(4.2, 3), 1.4)
if __name__ == '__main__':
    unittest.main()

'''


'''
Python单元测试：unittest使用简介
一.概述
python的单元测试框架unittest，这是Python自带的标准模块unittest。
unittest是基于java中的流行单元测试框架junit设计的，
其功能强大且灵活，对于熟悉junit的人来说掌握unittest很简单。

unittest涉及的知识点较多，但核心的就那一些，本文只介绍最核心和基础的内容。
类似junit，使用unittest编写python的单元测试代码，包括如下几个步骤：
1）编写一个python类,集成unittest模块中的TestCase类,这就是一个测试类
2）在上面编写的测试类中定义测试方法（这个就是指的测试用例），每个方法的方法名要求以 test 打头，没有额外的参数。
在该测试方法中 调用被测试代码，校验测试结果，TestCase类中提供了很多标准的校验方法，如 最常见的assertEqual。
3) 在上面编写的测试类中定义测试方法（这个就是指的测试用例），每个方法的方法名要求以 test 打头，没有额外的参数。
在该测试方法中 调用被测试代码，校验测试结果，TestCase类中提供了很多标准的校验方法，如 最常见的assertEqual。
'''


'''
#二. 案例1
#我们下面看一个例子，编写如下的python文件，为了简单，我们将被测函数与测试代码放在一个文件中了：
import  unittest
#被测试方法
def cal(a,b):
    return a+b
#测试类
#类名随便  但是必须要继承unittest.TestCase
class CalTest(unittest.TestCase):
    #测试用例必须要以test为首
    def testA(self):
        expected = 6
        result = cal(2,4)
        self.assertEqual(expected,result)

    def testB(self):
        expected = 3.0
        result = cal(2,1)
        self.assertEqual(expected,result)
if __name__ == '__main__':
    unittest.main()
'''


'''
#案例2
上面的例子只有一个测试文件(python文件)。在实际的项目中，往往又多个测试文件，每个测试文件针对不同的业务代码进行测试。
那这时该怎么去执行所有测试文件中的测试用例呢？
假设我们有test1.py测试文件中定义了一个测试类CalTest1 ， 另外一个测试test2.py测试文件中定义了一个测试类CalTest2.
这样要想同时能执行这两个测试文件中的测试用例，可编写如下的一个总的测试文件，作为执行的总入口：


import  unittest
from  test1 import  ababsbdsa
from  test2 import  Casd
if __name__ == '__main__':
    unittest.main()
'''


'''
案例3
TestCase 也就是测试用例
TestSuite 多个测试用例集合在一起，就是TestSuite
TestLoader是用来加载TestCase到TestSuite中的
TestRunner是来执行测试用例的,测试的结果会保存到TestResult实例中，包括运行了多少测试用例，成功了多少，失败
写一个简单的单元测试用例:

import  unittest
class MyTest(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例之后做操作
        print('111')
    def setUp(self):
        # 每个测试用例之前做操作
        print('2222')
    @classmethod
    def tearDownClass(self):
    # 必须使用@classmethod装饰器,所有test运行完后运行一次
        print('4444444')
    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod装饰器,所有test运行前运行一次
        print('333333')

    def test_a_run(self):
        expected = 1
        self.assertEqual(expected,1) # 测试用例
        
    #测试用例  对你写的函数 进行举例测试 考虑多种情况
    里面两个参数 一个是期待的参数 一个是执行之后待比较的参数
    def test_b_run(self):
        self.assertEqual(2,2) # 测试用例

if __name__ == '__main__':
    unittest.main()

'''


'''
常用的一些断言，也就是效验结果
assertEqual(a,b) a==b
assertNotEqual(a,b) a!=b
assertTrue(x) bool(x) is True
assertFalse(x) bool(x) is False
assertIsNone(x)  x is None 
assertIsNotNone(x) x is  not None
assertIn(a,b) a in b
assertNotIn(a,b) a not in b 
'''


'''
# 案例4
那如何生成一个测试报告呢，需要加入另外一个模块了，HTMLTestRunner，这个模块需要自己安装，
使用执行测试用例就会生成一个html的测试报告，里面会有每个测试用例的执行结果，代码如下：

import  HTMLTestRunner
import  unittest

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(22222)

    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run3(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

import unittest, HTMLTestRunner
suite = unittest.TestSuite()  # 创建测试套件
all_cases = unittest.defaultTestLoader.discover('.', 'test_*.py')
# 找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来
fp = open('res.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况')
runner.run(suite)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(MyTest('test_run1'))  # 测试套件中添加测试用例
    test_suite.addTest(MyTest('test_run2'))  # 测试套件中添加测试用例
    test_suite.addTest(MyTest('test_run3'))  # 测试套件中添加测试用例


    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    fp = open('./res.html', 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    # 生成执行用例的对象
    runner.run(test_suite)
    # 执行测试套件
'''


'''
如果我们有很多个模块，每个模块下面都写了很多python文件，每个python文件里面都有测试用例，那怎么把这个目录下的用例都执行了呢，
就要先找到这个目录下的所有python文件，然后找到里面的测试用例，逐个执行，代码如下：

if __name__ == '__main__':
    import unittest,HTMLTestRunner
    suite = unittest.TestSuite()#创建测试套件
    all_cases = unittest.defaultTestLoader.discover('./','test*.py')
    #找到某个目录下所有的以test开头的Python文件里面的测试用例
    for case in all_cases:
        suite.addTests(case)#把所有的测试用例添加进来
    fp = open('rest.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='all_tests',description='所有测试情况')
    runner.run(suite)
'''


'''
我们在后续进行持续集成的时候，要让代码自动运行，就会用到Jenkins了，但是上面产生的测试报告都是html格式的，Jenkins不认识，
就在Jenkins里面显示不出来。那咱们就要产生一些Jenkins认识的测试报告，Jenkins认识xml格式的报告，
那咱们就产生xml格式的呗，就需要用一个新的模块，xmlrunner，安装直接 pip install xmlrunner即可，代码如下：

import unittest
import xmlrunner


# 导入这个模块
# c = 3
class My(unittest.TestCase):
    def test2(self,a=1,b=2):
        c=3
        self.assertEqual(a+b,c)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(My))
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定报告放的目录
    runner.run(test_suite)
#然后咱们运行，可以看到在report目录下已经产生了xml格式的报告了，而且还自动把日期加上了

'''

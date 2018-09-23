**python Autopep8——按PEP8风格自动排版Python代码**

Autopep8是一个将Python代码自动排版为PEP8风格的小工具。它使用pep8工具来决定代码中的哪部分需要被排版。Autopep8可以修复大部分pep8工具中报告的排版问题。

参考网址: 

https://www.python.org/dev/peps/pep-0008/

https://pypi.python.org/pypi/autopep8/



**安装命令**

```
#安装到指定环境中
$ python  -m  pip  install  autopep8
```



**示例代码**

```

import math, sys;

 

def example1():

    ####This is a long comment. This should be wrapped to fit within 72 characters.

    some_tuple=(   1,2, 3,'a'  );

    some_variable={'long':'Long code lines should be wrapped within 79 characters.',

    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],

    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,

    20,300,40000,500000000,60000000000000000]}}

    return (some_tuple, some_variable)

def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));

class Example3(   object ):

    def __init__    ( self, bar ):

     #Comments should have a space after the hash.

     if bar : bar+=1;  bar=bar* bar   ; return bar

     else:

                    some_string = """

                       Indentation in multiline strings should not be touched.

Only actual code should be reindented.

"""

                    return (sys.path, some_string)
```



**运行命令**

```
$ autopep8 --in-place --aggressive --aggressive test_autopep8.py
```



**运行命令后代码的排版**

```

import math

import sys

 

 

def example1():

    # This is a long comment. This should be wrapped to fit within 72

    # characters.

    some_tuple = (1, 2, 3, 'a')

    some_variable = {

        'long': 'Long code lines should be wrapped within 79 characters.',

        'other': [

            math.pi,

            100,

            200,

            300,

            9876543210,

            'This is a long string that goes on'],

        'more': {

            'inner': 'This whole logical line should be wrapped.',

            some_tuple: [

                1,

                20,

                300,

                40000,

                500000000,

                60000000000000000]}}

    return (some_tuple, some_variable)

 

 

def example2(): return ('' in {'f': 2}) in {'has_key() is deprecated': True};

 

 

class Example3(object):

    def __init__(self, bar):

        # Comments should have a space after the hash.

        if bar:

            bar += 1

            bar = bar * bar

            return bar

        else:

            some_string = """

                       Indentation in multiline strings should not be touched.

            Only actual code should be reindented.

            """

            return (sys.path, some_string)
```


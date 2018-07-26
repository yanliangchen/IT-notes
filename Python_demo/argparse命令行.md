## **1. argparse介绍**

**摘自官方文档 ：https://docs.python.org/3/library/argparse.html**

[ ‎`‎ ‎‎argparse‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#module-argparse)‎模块使编写用户友好的命令行界面变得容易。该程序定义了它所需的参数, ‎[‎ ‎`‎ ‎‎argparse‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#module-argparse)‎将计算出如何从‎[‎ ‎`‎ ‎‎sys argv‎`](https://docs.python.org/3/library/sys.html#sys.argv)‎中解析它们。当用户为程序提供无效参数时, ‎[‎ ‎`‎ ‎‎argparse‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#module-argparse)‎模块还会自动生成帮助和使用消息并发出错误。



## 2. 示例

下面的代码是一个 Python 程序, 它采用整数列表并生成总和或最大值:‎

```
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers)
```

‎假设上面的 Python 代码保存到一个调用的文件中, 它可以在命令行运行并提供有用的帮助消息:‎`prog.py`

```
$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
```

‎当使用适当的参数运行时, 它打印命令行整数的总和或最大值:‎

```
$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10
```

‎如果传入的参数无效, 则会发出错误:‎

```
$ python prog.py a b c
usage: prog.py [-h] [--sum] N [N ...]
prog.py: error: argument N: invalid int value: 'a'
```

‎以下节将介绍此示例。



### 2.1 创建分析器

使用‎[‎ ‎`‎ ‎‎argparse‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#module-argparse)‎的第一步是创建一个‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎对象:‎

```
>>> parser = argparse.ArgumentParser(description='Process some integers.')
```

[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎对象将保存将命令行解析为 Python 数据类型所需的所有信息。



### 2.2 添加参数

通过调用‎[‎ ‎`‎ ‎‎add_argument ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument)‎方法来填充‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎与程序参数有关的信息。通常, 这些调用告诉‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎如何在命令行上取字符串并将它们变成对象。当调用‎[‎ ‎`‎ ‎‎parse_args ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)‎时, 将存储并使用此信息。例如:‎

```
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.add_argument('--sum', dest='accumulate', action='store_const',
...                     const=sum, default=max,
...                     help='sum the integers (default: find the max)')
```



‎稍后, 调用‎[‎ ‎`‎ ‎‎parse_args ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)‎将返回具有两个属性的对象, 以及。该属性将是一个或多个 int 的列表, 属性将是‎[‎ ‎`‎ ‎‎sum ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/functions.html#sum)‎函数, 如果是在命令行中指定的, 或者如果不是, 则为‎[‎ ‎`‎ ‎‎max ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/functions.html#max)‎函数。‎`integers``accumulate``integers``accumulate``--sum`



### 2.3 分析参数

[ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎通过‎[‎ ‎`‎ ‎‎parse_args ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)‎方法解析参数。这将检查命令行, 将每个参数转换为适当的类型, 然后调用相应的操作。在大多数情况下, 这意味着一个简单的‎[‎ ‎`‎命名空间‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.Namespace)‎对象将由从命令行解析出来的属性生成:‎

```
>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])
```

‎在脚本中, 通常不使用参数调用‎[‎ ‎`‎ ‎‎parse_args ()‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)‎ , 并且‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎将自动从 sys 确定命令行参数‎[‎ ‎`‎ ‎‎. argv‎`](https://docs.python.org/3/library/sys.html#sys.argv)‎.





## 3. ArgumentParser对象

### 3.1 显示程序名(可自定义)

默认情况下, ‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎对象用于确定如何在帮助消息中显示程序的名称。此默认值几乎总是可取的, 因为它将使帮助消息与程序在命令行上的调用方式相匹配。例如, 考虑使用以下代码命名的文件:‎`sys.argv[0]``myprogram.py`

 

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
```



‎此程序的帮助将显示为程序名 (无论程序从何处调用):‎`myprogram.py`

```
$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
$ cd ..
$ python subdir/myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
```

 

‎若要更改此默认行为, 可以使用该参数为‎[‎ ‎`‎ ‎‎ArgumentParser‎`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎提供另一个值:‎`prog=`

 

```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.print_help()
usage: myprogram [-h]

optional arguments:
 -h, --help  show this help message and exit
```

 

‎请注意, 无论是从参数中确定的程序名称, 还是使用格式说明符帮助消息的应用程序名。‎`sys.argv[0]``prog=``%(prog)s`

 

```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.add_argument('--foo', help='foo of the %(prog)s program')
>>> parser.print_help()
usage: myprogram [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
```



### 3.2  用法

默认情况下, ‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎从其包含的参数计算使用率消息:‎

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [-h] [--foo [FOO]] bar [bar ...]

positional arguments:
 bar          bar help

optional arguments:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
```

 

‎可以使用关键字参数重写默认消息:‎`usage=`

 

```
parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
```



### 3.3 描述

对‎[‎ ‎`‎ ‎‎ArgumentParser‎‎ ‎`‎ ‎](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)‎构造函数的大多数调用将使用关键字参数。此参数简要描述了程序的作用和工作原理。在帮助消息中, 说明显示在命令行用法字符串和各种参数的帮助消息之间:‎`description=`

```
parser = argparse.ArgumentParser(description='A foo that bars')
parser.print_help()
```


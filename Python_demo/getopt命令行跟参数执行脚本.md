### 1. python命令跟参数demo

需要模块：sys  参数个数：

len(sys.argv)  脚本名：    sys.argv[0]  参数1：     sys.argv[1]  参数2：     sys.argv[2]



#### 1.1 test.py

```
import sys
print ("脚本名：", sys.argv[0]）
for i in range(1, len(sys.argv)):
  print "参数", i, sys.argv[i]
>>>python test.py hello world
```



#### 1.2 convert.py 

​	1.通过-i -o选项来区别参数是输入文件还是输出文件.

​		python convert.py -i inputfile -o outputfile

​	2.当不知道convert.py需要哪些参数时，用-h打印出帮助信息

​		python convert.py -h



//代码解释:

a) sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。

b) "hi:o:": 当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。所以"hi:o:"就表示"h"是一个开关选项；"i:"和"o:"则表示后面应该带一个参数。

c) 调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。

getopt函数的第三个参数[, long_options]为可选的长选项参数，上面例子中的都为短选项(如-i -o)

```
import sys, getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file=""
output_file=""
for op, value in opts:
  if op == "-i":
    input_file = value
  elif op == "-o":
    output_file = value
  elif op == "-h":
    usage()
    sys.exit()
    
//第二种
for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    if o in ("-o", "--output"):
        output = a

```



#### 1.3 自动化执行python脚本之后执行cmd脚本

```
import  sys
import  os
#自动化 执行cmd脚本   python  **.py  publish
if  sys.argv[-1] =='publish':
    os.system("python --version")
    os.system("python")
    sys.exit()

```


## 1.Shell的学习

**shell 教程学习连接(可作为入门学习)**

​	**http://www.runoob.com/linux/linux-shell.html**

### 1.1Shell介绍

Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。

Shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。

Ken Thompson 的 sh 是第一种 Unix Shell，Windows Explorer 是一个典型的图形界面 Shell。

### 1.2Shell脚本

Shell 脚本（shell script），是一种为 shell 编写的脚本程序。 

 业界所说的 shell 通常都是指 shell 脚本，但读者朋友要知道，shell 和 shell script 是两个不同的概念。

由于习惯的原因，简洁起见，本文出现的 "shell编程" 都是指 shell 脚本编程，不是指开发 shell 自身。

### 1.3Shell环境

Shell 编程跟 java、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类众多，常见的有：

- Bourne Shell（/usr/bin/sh或/bin/sh）
-  Bourne Again Shell（/bin/bash）
- C Shell（/usr/bin/csh）
- K Shell（/usr/bin/ksh）
- Shell for Root（/sbin/sh）
- …… 

本教程关注的是 Bash，也就是 Bourne Again Shell，由于易用和免费，Bash 在日常工作中被广泛使用。同时，Bash 也是大多数Linux 系统默认的 Shell。

在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 **#!/bin/sh**，它同样也可以改为 **#!/bin/bash**。

\#! 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。



### 1.4Shell学习环境

​	#cat  /etc/redhat-release 

​	系统(云主机)：CentOS Linux release 7.2.1511 (Core) 



### 1.5第一个Shell脚本

打开文本编辑器(可以使用 vi/vim 命令来创建文件)，新建一个文件 test.sh，扩展名为 sh（sh代表shell），扩展名并不影响脚本执行，见名知意就好，如果你用 php 写 shell 脚本，扩展名就用 php 好了。 

 输入一些代码，第一行一般是这样： 

```
#!/bin/bash
echo "Hello World !" 
```

\#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。

echo 命令用于向窗口输出文本。 



#### 1.5.1运行 Shell 脚本有两种方法：

**1、作为可执行程序**

 将上面的代码保存为 test.sh，并 cd 到相应目录：

```
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
```

注意，一定要写成 ./test.sh，而不是 **test.sh**，运行其它二进制的程序也一样，直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里，你的当前目录通常不在 PATH 里，所以写成 test.sh 是会找不到命令的，要用 ./test.sh 告诉系统说，就在当前目录找。 

**2、作为解释器参数**

  这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：

```
/bin/sh test.sh
/bin/php test.php
```

 这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。 



### 1.6 Shell变量

**有效的 Shell 变量名示例如下：**

```
RUNOOB
LD_LIBRARY_PATH
_var
var2
```

无效的变量命名：

```
?var=123
user*name=runoob
```



**使用变量**

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：

```
your_name="qinjx"
echo $your_name
echo ${your_name}
```



变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况： 

```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```



如果不给skill变量加花括号，写成echo "I am good at $skillScript"，解释器就会把$skillScript当成一个变量（其值为空），代码执行结果就不是我们期望的样子了。 

 推荐给所有变量加上花括号，这是个好的编程习惯。 

已定义的变量，可以被重新定义，如：

```
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name
```

 

 这样写是合法的，但注意，第二次赋值的时候不能写$your_name="alibaba"，使用变量的时候才加美元符（$）。 





**只读变量**

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。

下面的例子尝试更改只读变量，结果报错：

```
#!/bin/bash
myUrl="http://www.google.com"
readonly myUrl
myUrl="http://www.runoob.com"
```

运行脚本，结果如下：

```
/bin/sh: NAME: This variable is read only.
```



**删除变量**

使用 unset 命令可以删除变量。语法：

```
unset variable_name
```

**实例**

```
#!/bin/sh
myUrl="http://www.runoob.com"
unset myUrl
echo $myUrl
```

以上实例执行将没有任何输出。

**变量类型**

运行shell时，会同时存在三种变量：

 

-  **1) 局部变量**  局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
-  **2) 环境变量**  所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
-  **3) shell变量**  shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行







### 1.7 Shell字符串

字符串是shell编程中最常用最有用的数据类型（除了数字和字符串，也没啥其它类型好用了），字符串可以用单引号，也可以用双引号，也可以不用引号。单双引号的区别跟PHP类似。 

**单引号** 

```
str='this is a string'
```

单引号字符串的限制： 

-  		单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
-  		单引号字串中不能出现单引号（对单引号使用转义符后也不行）。

**双引号** 

```
your_name='qinjx'
str="Hello, I know you are \"$your_name\"! \n" 
```

 双引号的优点：  

-  		双引号里可以有变量
-  		双引号里可以出现转义字符



**拼接字符串**

```
your_name="qinjx"
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1
```



**获取字符串长度**

```
string="abcd"
echo ${#string} #输出 4
```



**提取子字符串**  

以下实例从字符串第 **2** 个字符开始截取 **4** 个字符：

```
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
```



**查找子字符串** 

查找字符 "**i** 或 **s**" 的位置：

```
string="runoob is a great company"
echo `expr index "$string" is`  # 输出 8
```

**注意：** 以上脚本中 ` 是反引号，而不是单引号 '，不要看错了哦。





### 1.8 Shell数组

bash支持一维数组（不支持多维数组），并且没有限定数组的大小。

类似与 C 语言，数组元素的下标由 0 开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于 0。  

**定义数组** 

 在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开。定义数组的一般形式为： 

```
数组名=(值1 值2 ... 值n)
```

 例如: 

```
array_name=(value0 value1 value2 value3) 
```

 或者  

```
array_name=(
value0
value1
value2
value3
) 
```

 还可以单独定义数组的各个分量：  

```
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen 
```

 可以不使用连续的下标，而且下标的范围没有限制。  

 **读取数组** 

 读取数组元素值的一般格式是：

```
${数组名[下标]} 
```

 例如： 

```
valuen=${array_name[n]} 
```

 使用 @ 符号可以获取数组中的所有元素，例如：  

```
echo ${array_name[@]}
```



**获取数组的长度**

获取数组长度的方法与获取字符串长度的方法相同，例如： 

```
#取得数组元素的个数
length=$(#array_name[@])
#或者
length=$(#array_name[*])
#取得属组单个元素的长度
lengthn=$(#array_name[n])
```



**例子:**

```
#!/bin/bash
name=(1 2 3 4)
length=${#name[@]}
echo $length
         
```



### 1.9 Shell注释

```
以"#"开头的行就是注释，会被解释器忽略。
sh里没有多行注释，只能每一行加一个#号。只能像这样： 
#--------------------------------------------
# 这是一个注释
# author：菜鸟教程
# site：www.runoob.com
# slogan：学的不仅是技术，更是梦想！
#--------------------------------------------
##### 用户配置区 开始 #####
#
#
# 这里可以添加脚本描述信息
# 
#
##### 用户配置区 结束  #####
```



如果在开发过程中，遇到大段的代码需要临时注释起来，过一会儿又取消注释，怎么办呢？

每一行加个#符号太费力了，可以把这一段要注释的代码用一对花括号括起来，定义成一个函数，没有地方调用这个函数，这块代码就不会执行，达到了和注释一样的效果。 

**多行注释**

```
:<<EOF

注释内容

EOF
```

EOF 也可以使用其他符号:

```
:<<!
注释内容...
注释内容...
注释内容...
!
```



**//shell循环**

#!/bin/bash 
for i in a b c
do
echo "i is $i" 
done
        
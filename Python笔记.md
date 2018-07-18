jtypora-root-url: F:\markdown图片

Python的安装和简介

## 1.1 Python基础常识

### 1.1.1 简介

Python是一门面向对象的解释性计算机设计语言

### 1.1.2 Python语言特色

1. python是一门解释性语言
   * 解释性语言：在系统中运行时需要使用解释器（如Java、php等）
   * 编译性语言：在系统中运行时不需要使用解释器（如C，C++）
2. 弱类型语言
   * 弱类型语言：变量在使用之前不需要提前声明变量的类型就可以直接使用
   * 强类型语言：变量在使用之前需要提前声明变量的类型
3. 面向对象的语言
   * Python支持面向对象的编程，也在一定程度上支持面向过程和面向函数
4. 胶水语言
   * Python的底层和扩张库都是由C语言写成，可以很好支持C和C++

### 1.2.3 Python语言的优点

1. 简单
2. 易学
3. 速度快（这里指python的开发速度相对较快，python的运行速度相对一般）
4. 免费，开源
5. 高层语言（这里的高低指的是距离硬件的远近，python距离硬件相对比较远）
6. 可移植性（python在linux，windows，mac os都可以使用）
7. 可扩张性
8. 可嵌入性

## 1.2 Python安装及版本检测

### 1.2.1 Python windows上安装需要注意事项

勾选add python to paith 若没有勾选就需要手动去配置环境变量

### 1.2.2 Python版本检测

1. 方法一：在cmd中直接输入python，第一行会显示python的当前版本
2. 方法二：在cmd中输入python -V 
3. 方法三：打开idle

# 2. Python基本语法

## 2.1 注释、语句分类、关键字

### 2.1.1 注释

* 定义：即注解，解释。分为单行注释和多行注释

* 作用：

  ```
  1.给代码做出标注，进行解释和说明。方便别人阅读和理解代码
  2.在debug的时候，可以通过注解来一行一行查找问题
  ```

#### 2.1.1.1 单行注释

以#号开始，#后面的内容就是注解的内容。计算机不会去阅读#后面的内容

#### 2.1.1.2 多行注释

以''' 或者""" 将注释内容包裹起来

#### 2.1.1.3 注释的选择原则

单行注释 # 里面可以使用多行注释 ''' 或者 """

多行注释''' 或者 """ 里面可以使用单行注释# 

多行注释中可以使用另一种多行注释。如：''' 中可以使用"""   在"""中可以使用'''

### 2.1.2  Python 语句分类

Python语句分为 单行语句 和 代码组（代码块）

单行语句：一行python代码

代码组：特定的语言结构，标志是：和缩进（如if ，while等）

### 2.1.3  关键字

* 定义：关键字指系统已经使用的具有特殊功能的保留标识符

* 查看系统保留关键字的方法：

  ```
  import keyword
  print（keyword.kwlist）
  ```

# 3. Python变量及数据类型

## 3.1 变量

* 变量的定义：变量就是可以变化的量（在Python中更像是把变量的值贴到值上面，之后使用这个值就直接用贴在它上面的名字即可）

* 变量赋值：（三种方式）

  ```
  方法一：（基本格式）
  	变量 = 值
  方法二：（给多个变量赋相同的值）
  	变量1 = 变量2 = 变量3 ... = 值
  方法三：（给多个变量赋不同的值）
  	变量1，变量2，变量3... = 值1，值2，值3...
  ```

* 获取变量的类型：（两种方法）

  ```
  1. type（）
  	print（type（变量））
  2. isinstance（）-------> isinstance（查看的变量，类型）  返回的值是bool True or False
  	print（isinstance（4，int））
  ```

* 获取变量在内存中的id：

  ```
  id（）
  	print（id（变量））
  ```

* 更改变量的值：（对变量重新赋值即可）

  ```
  val = 1
  val = 2
  print(val)
  ```

* 变量的命名规则：

  ```
  1. 使用英文，禁止使用中文
  2. 可以使用数字，但是不能用数字开头
  3. 特殊符号只能使用下划线_ 
  4. 区分大小写
  5. 命名必须要有意义
  6. 避免和系统保留的关键字冲突
  ```

## 3.2 数据类型

1. Number     整型		(包含 ：int、float、bool、complex)
2. String        字符串      
3. List            列表            
4. Tuple         元组       
5. Set            集合            
6. Dict           字典 

ps：

```
* Number中包含： int、float、bool、complex
* 容器数据类型： String、List、Tuple、Set、Dict
* 有序数据类型： String、List、Tuple
* 无序数据类型： Set、Dict
```

### 3.2.1 Number类型

#### 3.2.1.1  Number类型：int

* int整型的声明方式：（十进制、二进制、八进制、十六进制）

  ```
  1. 十进制（0-9）
  	变量 = 十进制数字
  2. 二进制（0-1）
  	变量 = 0b二进制数字
  3. 八进制（0-7）
  	变量 = 0o八进制数字
  4. 十六进制（0-9a-f）
  	变量 = 0x十六进制数字
  ```

#### 3.2.1.2 Number类型：float

* float浮点型声明方式：（小数和科学记数法）

  ```
  1. 小数：
  	变量 = 带小数点的数字
  	num = 3.14
  2. 科学计数法   e相当于10    
  	变量 = 314e-2
  ```

#### 3.2.1.3 Number类型：bool

* bool类型只有两个值：True  和 False   （True和False的首字母都要大写！）
* True：表示肯定的，确定的答案
* False：表示否定的答案

#### 3.2.1.4 Number类型：complex

* 复数定义：由实数部分和虚数部分组成，实数部分是实际存在的数字，虚数部分是现实世界中不存在的数字。在计算机中虚数的单位为j。

* 声明一个复数的方法：

  ```
  方法一：
  	变量 = a + bj
  方法二：
  	变量 = complex（实数 + 虚数）           实数和虚数都只要填入纯数字即可，虚数部分不需要填入单位：j
  	如：
  	complex1 = complex（3，4）   ==     complex1 = 3 + 4j
  ```


#### 

### 3.2.2 String 字符串类型

* String在所有语言中都是使用最多的数据类型

* String类型声明方式：（三种）

  ```
  方法一：单引号 ''
  	变量 = '字符串内容'
  方法二：双引号 " "
  	变量 = "字符串内容"
  方法三：三引号 ''' ''' 或者 """  """
  	变量 = '''字符串内容'''  或者   变量 = """字符串内容"""
  ```

* String声明方式选择原则：

  ```
  1. 单引号中可以使用双引号
  2. 双引号中可以使用单引号
  3. 三引号中可以使用单双引号
  ```

* 转义字符：\

  ```
  1. 转义单引号：\'   （使单引号失去原有的特殊意义）
  	str1 = '古人说：\'nnb\''
  2. 转义双引号：\"	  （使双引号失去原有的特殊意义）
  	str1 = "古人说，\"nnb\""
  3. 换行操作符：\n
  	str1 = "人之初，\n性本善。"
  4. 缩进操作符：\t
  	str1 = "\t人之初，性本善"
  5. 对\自身进行转义：\\
  	str1 = '在字符串中输出\\'
  6. 续行符：\
  	str1 = '在单行语句\'
  			'过长时使用，自动续行'
  7. 原字符串：在字符串前面加上 r 或者 R ，转义字符串中所有的字符
  	str1 = r'你好，\n再见\t！'
  ```

### 3.2.3 List 列表类型

* 列表类型的标志：[ ] 中括号

* 列表的声明方式：

  ```
  变量 = [值1，值2，值3......]
  ```

* 创建一个空列表：

  ```
  方法一：	变量 = []
  方法二：	变量 = list(转换的变量或者值)
  ```

* 列表索引值

  ```
  正向索引： 0   1   2   3   4
  list1 = [100,200,300,400,500]
  反向索引：-5  -4  -3  -2  -1
  ```

* 通过索引访问和修改列表中特定的值

  ```
  列表[index]
  列表[index] = 新的值     可以通过下标来修改列表中的值
  ```

### 3.2.4 Tuple 元组类型

* 元组类型的标志：，逗号

* 元组类型的声明方式：

  ```
  方法一：
  	变量 = (值1，值2，值3....)
  方法二：
  	变量 = 值1，值2，值3....
  ```

* 元组索引值

  ```
  正向索引    0   1   2   3   4
  tuple1 = (100,200,300,400,500)
  反向索引   -5  -4  -3  -2  -1
  ```

* 通过索引查看元组中的某个值

  ```
  元组[index]
  元组中的值不能随意修改
  ```

### 3.2.5 Set 集合类型

* 集合的标志：无

* 集合是无序容器，无法通过索引来访问其中的某个值

* 集合中所有的数据都是唯一的，出现重复的会只保留唯一的其他删除

* 集合的声明方式：

  ```
  	变量 = {100,200,300,400,500}
  ```

* 创建空集合：

  ```
  	变量 = set（）
  ```

### 3.2.6 Dict 字典类型

* 字典的标志：{ } 

* 字典是无序数据，无法通过索引来访问其中的某个值

* 字典的声明方式：

  ```
  	变量 = {键：值，键：值，键：值...}
  ```

* 访问和修改字典中的值 ：

  ```
  字典是无序容器，不能使用索引来访问字典中的值。但是可以通过字典特有的键来访问字典中的值：
  	dict[键]
  修改字典中的值：
  	dict[键] = 新的值
  ```

* 创建一个空字典：

  ```
  变量 = dict()
  	dict1 = dict()
  变量 = {}
  	dict1 = {}
  ```

### 3.2.7 查看数据类型的方法

#### 3.2.7.1 type（）

正常工作的时候不能用，因为效率太低了。工作原理是把目标数据和所有数据类型一一匹配询问，找到同目标数据类型相同的类型。

```
	result = type（变量名）
	print（result）
```

#### 3.2.7.2 isinstance（）

工作效率比较高，把目标变量和指定的类型做比对，如果目标变量和指定类型为相同类型，则返回True；否则返回False

```
* 方法一，使用isinstance查看单一类型
	isinstance(变量，类型)
	如：
	var = 123
	result = isinstance(var,int)
	print(result)

* 方法二，使用isinstance查看目标变量是否属于两个类型中
	isinstance（变量，(类型一，类型二)）
	如：
	var = 123
	result = isinstance（var，（int，str））
	print（result）
```



## 3.3 数据类型转换

### 3.3.1 自动数据类型转换

1. 自动数据类型转换是系统自发的，不需要人工干预的

2. 自动数据类型转换会从精确度较小的数据类型向精确度较高的数据类型进行转换

3. 自动数据类型转换多发生在运算或者判断的时候

   ```
   如：
   	num1 = 25
   	num2 = 25.0
   	print(num1 + num2)
   又如：
   	if 1:
   		print('1会自动转化成True')
   ```

### 3.3.2 强制数据类型转换

#### 3.3.2.1 int（）

将其他数据类型转换成整型

```
整型：		 无需转换
浮点数：	去掉小数部分，只保留整数部分
布尔值：	True 转换成 1，False 转换成 0
复数：		 复数无法转换成整型
字符串：	只有纯整数字符串才能转换成int。
列表，元组，集合，字典都不能转换成整型
```

#### 3.3.2.2 float（）

将其他数据类型转换成浮点数

```
整型：		在整数后面加上.0
浮点数：    无需转换
布尔值：	True 转换成 1.0     False 转换成 0.0
复数：		复数无法转换成浮点数
字符串：	只有纯整数字符串和纯浮点数字符串才能转换成浮点数
列表，元组，集合，字典都不能转换成浮点数
```

#### 3.3.2.3 bool（）

其他类型中，相当于bool中的False的情况

```
整型：		  0
浮点型： 	 0.0
bool：	   False
复数：		 0j  或者  0+0j
字符串：	''(空字符串)
列表：		 [] 或者 list() 
元组：		 () 或者 tuple()
集合：		 set()
字典：	 	 {} 或者 dict()
```



#### 3.3.2.4 complex()

其他类型转换成复数complex（）

```
整型：		 整型+0j
浮点数：	浮点数+0j
布尔值：	True：1+0j    False：0j 或者 0+0j
复数：	 	 无需转换
字符串：	字符串中只有纯整数，纯浮点数或者纯复数才能转换成复数
列表、元组、集合、字典都不能转换成复数
```



#### 3.3.2.5 str（）

其他类型转换成字符串

```
所有类型都可以转换成字符串，系统会自动给其他类型加上''让它变成字符串
如果要打印出带引号的字符串，可以使用命令repr()
	如： 
	list1 = [1,2,3]
	list1 = str(list1)
	print(repr（list1）)
```



#### 3.3.2.6 list（）

其他类型转换成列表

```
整型、浮点型、复数、布尔值都不能转换成列表
字符串：字符串转换成列表，把字符串中的每个值转换成列表中的每一个值，顺序保持不变
列表： 无需转换
元组： 把元组中的每个值转换成列表中的值，顺序保持变
集合： 把集合转换成列表中的每一个值，顺序随机
字典： 把字典中的键转换成列表中的值，顺序随机
```



#### 3.3.2.7 tuple（）

其他类型转换成元组

```
整型、浮点数、复数、布尔值都不能转换成元组
字符串：字符串中的每个字符转换成元组中的一个值，顺序不变
列表： 列表中的每一个值转换成元组中的值，顺序不变
元组： 无需转换
集合： 集合中的每个值转换成元组中的每个值，顺序随机
字典： 字典中的每个键转换成元组中的一个值，顺序随机
```



#### 3.3.2.8 set（）

其他类型转换成集合

```
整型、浮点型、复数、布尔值都不能转换成集合
字符串： 字符串中的每个字符转换成集合中的一个值，顺序随机
列表： 列表中的每个值转换成集合中的一个值，顺序随机
元组： 元组中的每个值转换成集合中的一个值，顺序随机
集合： 无需转换
字典： 字典中的每个键转换成集合中的一个值，顺序随机
```



#### 3.3.2.9 dict（）

其他类型转换成字典

```&amp;amp;amp;amp;#39;&amp;amp;amp;amp;#39;
* 整型、浮点型、复数、布尔值都不能转换成字典
* 字符串： 不能转换成字典
* 列表： 只有特定的列表格式可以转换成字典
	1. 二级列表（且第二级容器的长度一样）
	list1 = [[键，值],[键，值],[键，值],[键，值],[键，值]]		or  	list1 = [(键，值),(键，值),(键，值),(键，值)]
	
	2. 一级列表：只含有两个字符的一级列表
	list1 = ['键值','键值','键值','键值']

* 元组： 只有特定的元组格式才可以转换成字典
	1. 二级元组（且第二级容器的长度一样）
	tuple1 = ((键，值),(键，值),(键，值),(键，值))
	
	2. 一级元组：只含有两个字符的一级元组
	tuple1 = （'键值','键值','键值','键值'）
	
* 集合： 只有特定的集合格式才可以转换成字典
	1. 二级集合（且第二级容器的长度一样）
	set1 = {(键，值),(键，值),(jia),()}
```
# 4. Python运算符

1. 算术运算符
2. 比较运算符（关系运算符）
3. 逻辑运算符
4. 位运算符
5. 赋值运算符
6. 成员运算符
7. 身份运算符

## 4.1 算术运算符

```
**		幂运算（最高优先级）
*		乘法运算
/		除法运算
//		取商运算（地板除）
%		取余运算
+		加法运算
-		减法运算
```

## 4.2 比较运算符（关系运算符）

比较运算符运算结果为布尔值：	True 、False

```
<=		小于等于
>=		大于等于
<		小于
>		大于
==		等于
!=		不等于
```

## 4.3 赋值运算符

变量 = 变量 操作符 值 -------------------------------> 变量 操作符= 值

```
**=		幂运算赋值
*=		乘法赋值
/=		除法赋值
//=		取商赋值
%=		取余赋值
+=		加法赋值
-= 		减法赋值
=		普通赋值
```

## 4.4 逻辑运算

逻辑运算是布尔值之间的运算

1. not 逻辑非运算 （逻辑运算中优先级最高）

   ```
   真变假，假变真
   not True == False
   not False == True
   ```

2. and 逻辑与运算

   ```
   有假则假
   只有当 and 左右的两个条件都满足的时候 and 的结果才是为真
   True and False == False
   True and True == True
   False and False == False
   ```

3. or 逻辑或运算

   ```
   有真则真
   当 or 左右两个条件有一个满足，则 or 的结果就是为真
   True or False == True
   False or False == False
   True or True == True
   ```

4. xor 逻辑异或运算

   ```
   不同为真，相同为假
   在python中不支持异或操作。
   True xor False == True
   True xor True == False
   False xor False == False
   ```

## 4.5 位运算符

位运算就是在二进制基础上进行的逻辑运算

```
&		按位与运算
|		按位或运算
~		按位反转
^		按位异或运算
<<		左移			<< 1 左移1位，相当于*2
>>		右移			>> 1 右移1位，相当于//2
```

## 4.6 成员运算符

检测变量是否在容器类数据中

```
in ：
	变量 in 容器类数据（string,list,tuple,set,dict），检测字典的时候，只检测字典的键
	检测变量是不是在容器中
	
not in :
	变量 not in 容器类数据
	检测变量是不是不在容器中
```

## 4.7 身份运算符

判断两个变量在内存中的地址是否相同。

```
is：
	检测两个变量是否是同一个值

is not：
	检测两个变量是否不是同一个值
```

```
当数值相同的时候，哪些数据类型的id会相同
1. 整数：	-5以上的整数
2. 浮点数： 0以上的浮点数
3. 布尔值： 永远相同
4. 复数：	实数部分为0，虚数部分在0j以上
5. 字符串： 永远相同 
```



# 5.流程控制

1. 流程:

   ```
   做事情的顺序就是流程,计算机中的流程就是代码执行的顺序.默认是从上到下
   ```

2. 流程分类:

   1. 顺序结构
   2. 分支结构(单向分支,双向分支,多向分支,巢状结构)
   3. 循环结构(while循环  死循环  for...in循环)

## 5.1 顺序结构

python默认的代码执行顺序,默认从上到下执行代码



## 5.2 分支结构

### 5.2.1 单向分支

基本格式:

```
if 条件判断:
	条件为真时,执行语句
	...
```

如:

```
num = 10
if num > 9:
	print(num)
```



### 5.2.2 双向分支

基本格式:

```
if 条件判断:
	条件为真的时候执行代码
	...
else:
	条件为假的时候执行代码
	...
```

如:

```
num = 10
if num > 10:
	print(num)
else:
	print(num,'比10小')
```



### 5.2.3 多向分支

基本格式:

```
if 条件1判断:
	条件1为真的时候执行代码
	...
elif 条件2判断:
	条件2为真的时候执行代码
	...
elif 条件3判断:
	条件3为真的时候执行代码
	...
else:
	条件1,条件2,条件3都不满足执行代码
	...

```

如:

```
day = 1
if day == 1:
	print('黄焖鸡')
elif day == 2:
	print('面条')
elif day == 3:
	print('快餐')
elif day == 4:
	print('汉堡')
else:
	print('不吃了')
```



### 5.2.4 巢状分支

基本结构:

```
if 条件1判断:
	条件1满足执行代码
	if 条件2判断:
		条件2满足执行代码
		if 条件3判断:
			条件1,条件2,条件3都满足执行代码
		else:
			条件3不满足执行代码
	else:
		条件2不满足执行代码
else:
	条件1不满足执行代码
```

如:

```
schooldoor = True
buildingdoor = True
classdoor = True


if schooldoor == True:
	print('校门开了,走到教学楼')
	if buildingdoor == True:
		print('教学楼门开了,走到教室')
		if classdoor == True:
			print('教室门开了,走进教室开始学习')
		else:
			print('教室门没开,班长帮忙开个门')
	else:
		print('教学楼门没开,班主任帮忙开个门')
else:
	print('校门没开,大爷帮忙开个门')
	
	
```



## 5.3 循环结构

### 5.3.1 while 循环

基本格式:

```
while 条件判断:
	条件为真时,执行代码
	....
```

如: 计算0-100(包含100)所有数之和

```
num = 0
total = 0
while num <= 100:
	total += num
	num += 1
print(total)
```

又如: 输出十行十列的星星

```
i = 0
while i < 10:
	j = 0
	while j < 10:
		print('✨',end= '')
		j += 1
	
	print('\n',end='')
	i += 1
```

又如: 使用单循环输出10行10列的星星

```
i = 0
while i < 100:
	print('✨',end = '')
	if i % 10 == 9:
		print()
	i += 1
```

又如: 输出十行十列星星,隔行变色

```
i = 0 
while i < 10:
	j = 0
	while j < 10:
		if i % 2 == 0:
			print('✨',end = '')
		else:
			print('❤️',end = '')
		j += 1
		
	print()
	i += 1
```

又如: 使用单循环实现隔行变色

```
i = 0
while i < 100:
	if (i // 10) % 2 == 0: 
		print('✨',end = '')
	else:
		print('❤️',end = '')
	if i % 10 == 9:
		print()
	i += 1
```



### 5.3.2 死循环

基本格式:

```
while True:
	循环内容
	...	
```

如: 判断用户输入的密码是否正确

```
error = False
passwd = 123

while True:
	userinput = input('请输入密码:')
	
	# 检查密码格式是否正确
	for each in userinput:
		if each not in '0987654321':
			error = True
			break
	
	if error == True:
		print('密码格式错误,请重新输入纯数字密码!')
		error = False
		continue
	else:
		if userinput == str(passwd):
			print('密码正确,登录成功!')
			break
		else:
			print('密码错误,请重新输入!')
		
```



### 5.3.3 for … in 循环

基本格式:

```
for 变量 in 容器:
	循环体
	...
```



遍历除字典外的不等长的二级容器(列表,元组,集合)

```
for 变量1 in 容器:
	for 变量2 in 变量1:
		循环体
		...
```



遍历字典中的键和值:

```
for key in dict1:
	print(key,dict1[key])
	
或者

for key,value in dict1.items():
	print(key,value)
```



遍历等长的二级容器;

```
list1 = [
  ['a','b','c'],
  ['d','e','f'],
  ['g','h','i']
]
for x,y,z in list1:
	print(x,y,z)
```



### 5.3.4 break 和 continue 

break: 终止循环

如: 输出0-100(包含100)的数字,遇到44则停止循环

```
i = 0:
while i <= 100:
	if i == 44:
		break
	print(i)
	i += 1
```



continue: 跳过本次循环,开始下一次循环. 开始下一次循环的同时要进行判断

如: 输出0 -100(包含100)的数字,遇到任何带4的则跳过

```
i = 0
while i <= 100:
	if i % 10 == 4 or i // 10 == 4:
		i += 1
		continue
	else:
		print(i)
		i += 1
```

### 5.3.5 关于重置变量标识

#### 1. 数字类

1.密码解锁为例

a="111"

//先定义了一个变量  如果为True   进入死循环

c=1

//第二种情况  如果c不等于2就进来了

while c!=2:

​	//获取用户输入的密码

​	n=input("请输入密码")

​	//如果用户输入的密码n==a

​	if n==a:

​		//那么我给他重置变量

​		//重置变量为2 就进入不到循环了 循环就停止了

​		c=2

#### 2.True   和 False

a="111"
c=True

while c:

​	n= input('请输入密码')

​	//如果输入的密码n==a	

​	if n==a :

​	//那么我就给她重置变量

​	//重置为false   循环  就停止了 

​		c=False

# 6.函数

* 定义: 把具有特定功能的代码打包就是函数
* 作用
  1. 提高代码的复用率
  2. 提高开发效率
  3. 便于程序的维护

## 6.1 函数声明方式

def 函数名( ) :

​	pass(函数内容)



函数名( )	# 调用函数



## 6.2 函数名命名规则

1. 使用英文,禁止使用中文
2. 可以使用数字,但是不能用数字开头
3. 所有的符号只能用_下划线
4. 命名要有意义
5. 严格区别大小写
6. 避免和系统保留的关键字重名
7. 避免和系统保留的函数重名



## 6.3 函数的参数

### 6.3.1 形参

函数在定义过程中,( )中的参数就是形参.形参没有实际意义,只是为了占位接收实参的值

#### 6.3.1.1 普通形参

* 没有实际意义,只是为了占位,等待接收实参对他赋值.
* 如果定义了形参,形参也没有设置默认值,那么在调用函数的时候如果没有实参就会报错

如:

```
def hanshu(a,b):
	print(a)
	print(b)
hanshu(1,2)
```

#### 6.3.1.2 带有默认值的形参

* 在函数定义的时候如果给了形参默认值,那么就是带有默认值的形参
* 那么如果调用的时候如果没有传入实参,形参会按默认值进行运算
* 若调用的时候传入了实参,那么实参的值会覆盖形参的默认值,按实参的值进行运算

如:

```
def hanshu(a = 1, b = 2):
	print(a)
	print(b)


hanshu()
hanshu(3,5)
```



#### 6.3.1.3 普通收集形参 * 

* 在不确定有多少实参传入的时候,可以使用普通收集形参:    * 变量名
* 收集到的实参会组成一个元组
* 形参优先级: 普通形参 > 普通收集形参 > 关键字收集形参

如:

```
def hanshu(*tuple1):
	total = 0
	for each in tuple1:
		total += each
	print(total)

hanshu(1,2,3,4,5,6,7)
```



#### 6.3.1.3 关键字收集形参 **

* 关键字收集形参只能收集关键字实参的值
* 收集到的关键字实参会组成一个字典,关键字作为字典的键,实参的值作为字典的值
* 形参优先级: 普通形参 > 普通收集形参 > 关键字收集形参

```
def age(**dict1):
	total = 0
	for key in dict1:
		print(key)
		total += dict1[key]
		print(dict1[key])
	print(total)

age(a=1,b=2,c=3,d=4)
```



### 6.3.2 实参

#### 6.3.2.1 普通实参

* 在调用函数的时候,( )中的值就是实参.若没有通过关键字的方式进行传参的就是普通实参
* 实参的优先级: 普通实参 > 关键字实参

如:

```
def hanshu(a):
	print(a)

hanshu('哗啦啦')
```



#### 6.3.2.2 关键字实参

* 在调用函数的时候,通过关键字=值的方式来进行传参,这就是关键字实参
* 实参的优先级: 普通实参 > 关键字实参

如:

```
def hanshu(a,b):
	print(a)
	print(b)

hanshu(a='关键',b='字')
```



## 6.4 函数的返回值

* 函数按照有无返回值可以分为两类:

   1. 有返回值的函数 — 含有return , 函数执行之后,会返回一个结果,可以用变量接受
   2. 执行过程的函数 — 没有返回值的函数, 没有return , 函数执行只有不会返回一个结果,用变量接受为 none

* return的作用

1. 为函数的运行返回一个结果
2. 终止函数执行,一旦函数运行到了return,则在return之后的代码将不会运行





## 6.5 函数文档

### 6.5.1 查看函数文档的方法

* 方法一: 	help( ) —help(函数名)

  如: 

  ```
  help(print)

  help(id)

  help(type)

  ```

  ​



* 方法二:	函数名. _ _ _doc_ _ _ 

  如:

  ```
  print.__doc__

  id.__doc__

  type.__doc__
  ```



### 6.5.2 定义函数文档的方法

```
def 函数名():
	'''
	功能:
	参数:
	返回值:
	'''
	
	函数内容...
	
	
```



## 6.6 变量的作用域

### 6.6.1 全局变量

1. 在任何区域或者页面都有效的变量
2. 在全局环境中直接声明的变量就是全局变量
3. 在局部环境中修改全局变量的值需要使用global关键字

```
var = '我是全局变量'
def hanshu():
	jubuvar = '我是局部变量'
	
```



### 6.6.2 局部变量

1. 在特定的局部区域有效的变量就是局部变量
2. 在函数内部(局部环境中)声明的变量就是局部变量
3. 在内部函数中修改内部函数外部的非全局变量,需要使用nonlocal关键字

### 6.6.3 局部变量和全局变量的关系

1. 在全局环境中不能直接使用局部变量和内部函数,需要闭包之后才能使用
2. 在局部环境中可以访问全局变量,但是不能修改全局变量的值,需要使用global关键字

### 6.6.4 global 关键字

1. 作用一: 使全局变量能进入局部环境

   ```
   var = '我是全局变量'

   def hanshu():
   	global var
   	var = '全局变量进入局部环境,修改全局变量'
   	
   hanshu()
   print(var)
   ```

2. 作用二: 将局部变量升级为全局变量

   ```
   def hanshu():
   	global var
   	var = '我升级成全局变量'

   hanshu()
   print(var)
   ```



### 6.6.5 内部函数

1. 定义: 在一个函数的内部在定义一个函数,再定义的函数就是内部函数. 内部函数本质上相当于一个局部变量

   ```
   def outer():
   	def inner():
   		print('我是内部函数')
   	inner()

   outer()
   ```



2. 内部函数的作用域:
     1. 内部函数不能直接在全局环境中使用,需要使用闭包将它带到全局环境中
       2. 在函数内部可以调用内部函数
       3. 在函数内部需要先定义内部函数,之后才能调用



### 6.6.6 闭包

1. 定义: 让局部变量和内部函数在函数的外部可以使用即闭包
2. 作用: 让局部变量和内部函数突破局部作用域

闭包实现方法:

       	1. 方法一: 使用global关键字实现闭包

```
lists = []

def hanshu():
	global lists
	
	a = '局部变量a'
	b = '局部变量b'
	
	def inner1():
		print('内部函数inner1')
	def inner2():
		print('内部函数inner2')
	
	lists = [a,b,inner1,inner2]

hanshu()

num_a = lists[0]
num_b = lists[1]
neibu1 = lists[2]
neibu2 = lists[3]

neibu1()
neibu2()
```



2. 方法二: 使用return实现闭包

```
def hanshu():
	
	a = '局部变量a'
	b = '局部变量b'
	
	def inner1():
		print('我是内部函数inner1')
	def inner2():
		print('我是内部函数inner2')
	
	return [a,b,inner1,inner2]

lists = hanshu()

num_a = lists[0]
num_b = lists[1]
neibu1 = lists[2]
neibu2 = lists[3]

neibu1()
neibu2()
```



3. 方法三: 使用return内部函数实现闭包

```
def hanshu():
	
	a = '局部变量a'
	b = '局部变量b'
	
	def inner1():
		print('我是内部函数inner1')
	def inner2():
		print('我是内部函数inner2')
	
	def bibao():
		return [a,b,inner1,inner2]
	
	return bibao
	

result = hanshu()
lists = result()

num_a = lists[0]
num_b = lists[1]
neibu1 = lists[2]
neibu2 = lists[3]

neibu1()
neibu2()

```



### 6.6.7 nonlocal 关键字

用于在内部函数中修改内部函数外部的非全局变量的值

如:

```
def user():
	
	jubuvar = '我是局部变量'
	
	def change(newvar):
		nonlocal jubuvar
		jubuvar = newvar
	
	def look():
		print(jubuvar)
	
	def bibao():
		return [jubuvar,change,look]
	
	return bibao

result = user()
lists = result()

jubu = lists[0]
modif = lists[1]
kan = lists[2]

modif('修改局部变量')

kan()
```

---

## 6.7 lambda 表达式

1. 基本格式:

   ```
   函数名 = lambda 形参1,形参2,... : (自带return) 函数内容
   ```

   如:

   ```
   total = lambda no1,no2,no3 : no1 + no2 + no3

   result = total(1,2,3)
   print(result)
   ```

2. 带有分支结构的lambda表达式:

   ```
   函数名 = lambda 形参1,形参2,... : 条件为真时执行结果 if 条件判断 else 条件为假时执行结果
   ```

   如:

   ```
   large = lambda no1,no2 : no1 if no1 > no2 else no2

   ```

   又如:

   ```
   large = lambda no1,no2,no3: no1 if no1 > no2 and no1 > no3 else no2 if no2 > no3 else no3
   ```


----

## 6.8 递归函数

在函数中调用函数自身的函数就叫做递归函数

如:

```
def digui(num):
	
	print(num)
	
	if num > 0:
		digui(num - 1)
	else:
		print('-------------------')
	
	print(num)
```



----

# 7. 字符串

## 7.2 字符串基本操作

1. 字符串连接操作:	 +

   ```
   string1 = '大风车'
   string2 = '吱呀吱呀转'
   result = string1 + string2 
   print(result)
   ```

2. 字符串复制操作:       *

   ```
   string1 = '女神'
   result = string1 * 3
   print(result)
   ```

3. 字符串索引操作:      [ ]

   ```
   string1 = '我是字符串'
   print(string1[4])
   print(string1[-1])
   ```

4. 字符串分片操作:      [::]

   ```
   分片 [起始位置:结束位置:间隔]     --- 不包含结束位置

   string1 = '我是字符串'
   string2 = string1[1:3]
   string3 = string1[::2]

   ```


---

## 7.2 字符串函数

### 7.2.1 大小写相关



#### capitalize( )	

使字符串第一个第一个字母大写

```
string1 = 'i love you'
result = string1.capitalize()
print(result)
```



#### title( )

使字符串字母满足标题化格式(所有单词首字母大写)

```
string1 = 'i love you'
result = string1.title()
print(result)
```



#### upper( )

使字符串中的所有字母都大写

```
string1 = 'who is your dad ?'
result = string1.upper()
print(result)
```



#### lower( )

使字符串中所有字母都小写

```
string1 = 'who is your Dad ? '
result = string1.lower()
print(result)
```



#### swapcase( )

将字符串中的大小写互换

```
string1 = 'I am your Dad !'
result = string1.swapcase()
print(result)
```



### 7.2.2 获取长度及出现次数

#### len( )

len( )为内置函数

获取字符串或其他容器的长度

```
string1 = '我是字符串'
result = len(string1)
print(result)
```



#### count( )

count(指定字符,起始,终止)

获取指定字符在指定范围内出现的次数,若没有出现过,返回 0

```
string1 = 'the only way to longer the day is to steal time from night!'
result = string1.count('o',2,6)
print(result)
```



### 7.2.3 获取索引值

#### find( )

获取指定字符在字符串中指定范围内第一次出现的索引值. 若没有出现则返回 -1

find(指定字符,起始,终止)

```
string1 = '8000 words in the world, only the love can kill man'
result = string1.find('a')
print(result)
```



#### index( )

获取指定字符在字符串中指定范围内第一次出现的索引值,若没有出现则直接报错

```
string1 = '8000 words in the world, only the love can kill man'
result = string1.index('a')
print(result)
```



### 7.2.4 检测类字符串函数

#### startswith( )

检测字符串是否以指定字符在指定范围内开头

startswith(指定字符,起始,终止)

```
string1 = 'you are the sun in the world'
result = string1.startswith('a',4,8)
print(result)
```



#### endswith( )

检测字符串是否以指定字符在指定范围内结尾

endswith(指定字符,开始,结束)

```
string1 = 'you are the sun in the world'
result = string1.endswith('w',-5)
print(result)
```



#### istitle( )

检测字符串是否满足标题格式

```
string1 = 'we all forgot the story of the passtime'
result = string1.istitle()
print(result)
```



#### isupper( )

检测字符串是否满足全部大写

```
string1 = 'WE ARE THE DOTA-ALLSTARS'
result = string1.isupper()
print(result)
```



#### islower( )

检测字符串是否满足全部字母小写

```
string1 = 'we are dota-allstars'
result = string1.islower()
print(result)
```



#### isdigit( )  

和 isnumeric(  )  isdecimal(  ) 相同

判断字符串是否全部都是数字

```
num = '123456'
result = num.isdigit()
print(result)
```



#### isalnum( )

判断字符串是否由字母或者其他文字或者数字组成	(不包含符号)

```
string1 = 'sad is the reason of thinking too much'
result = string1.isalnum()
print(result)
```



#### isalpha( )

判断字符串是否由字母或者其他文字组成(不包含符号和数字)

```
string1 = 'these are only words'
result = string1.isalpha()
print(result)
```



#### isspace( )

判断字符串是否由空白字符组成

```
string1 = '\n\t\r\\ '
result = string1.isspace()
print(result)
```



### 7.2.5 切割和拼接

#### split( )

将字符串按指定字符进行切割,切割之后放入列表内

split(指定字符)

```
string1 = '我-有一剑-可开天门!'
list1 = string1.split('-')
print(list1)
```



#### join( )

用指定字符将列表中的元素拼接成字符串

'指定字符'.join(列表)

```
list1 = ['我','有一剑','可开天门']
string2 = '!'.join(list1)
print(string2)
```



#### splitlines( )

使用字符串中的换行符号\n来切割字符串

```
string1 = '天不生李淳罡,\n剑道万古如长夜'
list1 = string1.splitlines()
print(list1)
```



### 7.2.6 填充类

#### zfill( )

指定字符长度,用0从左到右进行填充

```
string1 = '123'
result = string1.zfill(10)
print(result)

0000000123

```



#### center( )

指定字符长度,原字符串居中,使用指定字符填充到指定长度

center(长度,指定字符)

```
string1 = '呵呵姑娘'
result = string1.center(10,'_')
print(result)

---呵呵姑娘---
```



#### ljust( )

指定字符长度,原字符串居左,使用指定字符填充至指定长度

ljust(长度,指定字符)

```
string1 = '呵呵姑娘'
result = string1.ljust(10,'-')
print(result)

呵呵姑娘------
```



#### rjust( )

指定字符长度,原字符串居右,使用指定字符填充至指定长度

rjust(长度,指定字符)

```
string1 = '呵呵姑娘'
result = string1.rjust(10,'-')
print(result)

------呵呵姑娘
```



### 7.2.7 清除字符串类

#### strip( )

清除字符串左右两边的指定字符

```
string1 = '___呵呵___'
result = string1.strip('_')
print(result)

呵呵
```



#### lstrip( )

清除字符串左边指定的字符

```
string1 = '___呵呵___'
result = string1.lstrip('_')
print(result)

呵呵___
```



#### rstrip( )

清除字符串右边指定的字符

```
string1 = '___呵呵___'
result = string1.rstrip('_')
print(reuslt)

___呵呵
```



### 7.2.8 字符的替换操作

#### maketrans( )

字典名 = ''.maketrans(所有要替换的字符,新的字符)

制作存有替换映射关系的字典

```
string1 = '十年修得宋玉树,百年修得徐凤年,千年修得吕洞玄'
dict1 = ''.maketrans('十百千','百千万')
```



#### translate( )

字符串.translate(字典名)

将字符串按照存有映射关系的字典进行修改

```
newstring = string1.translate(dict1)
print(newstring)

百年修得宋玉树,千年修得徐凤年,万年修得吕洞玄
```



### 7.2.9 format( ) 格式化

#### format( ) 基本格式:

```
string1 = '{}在{}看见了{}'
result = string1.format('我','莆田','刘姥姥')
print(result)

我在莆田看见了刘姥姥
```

#### format( ) 四种传参方式:

1. 按位置进行传参

```
string1 = '{}在{}看见了{}'
result = string1.format('我','莆田','刘姥姥')
print(result)

我在莆田看见了刘姥姥
```



2. 按位置标识传参

```
string1 = '{2}在{1}看见了{0}'
result = string1.format('刘姥姥','莆田','我')
print(result)

我在莆田看见了刘姥姥
```



3. 按关键字传参

```
string1 = '{who}在{where}看见了{what}'
result = string1.format(what='刘姥姥',where='莆田',who='我')
print(result)

我在莆田看见了刘姥姥
```



4. 使用容器传参

```
string1 = '{0[0]}在{0[1]}看见了{0[2]}'
result = string1.format(['我','莆田','刘姥姥'])
print(result)

我在莆田看见了刘姥姥
```



#### format( )实现居中 居左 居右

1. 居中填充 center( )     {:填充物^长度}

```
string1 = '我喜欢吃{:*^11}你喜欢么'
result = string1.format('小龙虾')
print(result)

我喜欢吃****小龙虾****你喜欢么
```



2. 居左填充 ljust( )	{:填充物<长度}

```
string1 = '我喜欢吃{:*<11}你喜欢么'
result = string1.format('小龙虾')
print(result)

我喜欢吃小龙虾********你喜欢么
```



3. 居右填充 rjust( )	{:填充物>长度}

```
string1 = '我喜欢吃{:*>11}你喜欢么'
result = string1.format('小龙虾')
print(result)

我喜欢吃*******小龙虾你喜欢么
```



#### format( ) 实现进制转换

1. 二进制 {:b}

```
num = '{}转换成二进制为:{:b}'
result = num.format(10,10)
print(result)
```



2. 八进制 {:o}

```
num = '{}转换成八进制为:{:o}'
result = num.format(10,10)
print(result)
```



3. 十进制: {:d}

```
num = '{}转换成十进制为:{:d}'
result = num.format(10,10)
print(result)
```



4. 十六进制: {:x}

```
num = '{}转换成十六进制为"{:x}'
result = num.format(10,10)
print(result)
```



# 8. 内建函数

## 8.1 类型转换相关

int( ):		

​	将其他类型转换成整型

float( ):		

​	将其他类型转换成浮点型

bool( ):		

​	将其他类型转换成布尔值

complex( ):	

​	将其他类型转换成复数

str( ):		

​	将其他类型转换成字符串

list( ):		

​	将其他类型转换成列表

tuple( ):		

​	将其他类型转换成元组

set( ):		

​	将其他类型转换成集合

dict( ): 		

​	将其他类型转换成字典



## 8.2 变量相关

type( ):		

​	查看变量的类型

id( ):			

​	查看变量的内存id

print( ):		

​	打印

locals( ):		

​	查看当前环境中的所有变量



## 8.3 数学相关

* abs( )		

  获取一个数值的绝对值

```
num = -99
result = abs(num)
print(result)
```



* max( )		

  获取序列或者多个参数的最大值

```
list1 = [1,2,3,4,5,6,7,8,9]
result = max(list1)
print(result)

result = max(1,2,3,4,5,6,7,88,0)
print(result)
```



* min( )		

  获取序列或者多个参数的最小值

```
list1 = [1,2,5,6,4,1,345,68,2]
result = min(list1)
print(result)

result = min(1,214,5,6,7235,67)
print(result)
```



* round( )		

  四舍五入,可以加参数来指定保留几位小数

```
num = 3.1415
result = round(num,3)
print(num)
```



* pow( )

  计算指定数字的n次方

```
result = pow(2,3)   # 2 ** 3
print(result)
```



* bin( )

  将数字转换成二进制

```
result = bin(10)
print(result)
```

* oct( )

  将数字转换成八进制

```
result = oct(10)
print(result)

```



* hex( )

  将数字转换成十六进制

```
result = hex(10)
print(result)
```



## 8.4 Ascii码相关

* chr( )

  将指定的Ascii码转换成对应字符

```
result = chr(97)
print(result)
```

* ord( )

  将指定的字符转换成ascii码

```
result = ord('a')
print(result)
```

* eval( )

  将字符串转换成代码

```
string1 = 'num + 1'
num = 1
num = eval(string1)
print(num)
```



# 9. 数学模块

在使用数学模块之前需要先导入模块

import math



* ceil( )

  向上取整

```
num = 0.1
result = math.ceil(num)
print(result)
```



* floor( )

  向下取整

```
num = 1.9
result = math.floor(num)
print(result)
```



* pow( )	

  和内置函数功能一样,计算指定值的n次方,返回值是浮点数

```
result = math.pow(2,3)
print(result)
```



* sqrt( )

  开平方根

```
result = math.sqrt(4)
print(result)
```



* fabs( )

  功能和内建函数abs( )功能一样,取绝对值,返回值是浮点数

```
num = -9
result = fabs(num)
print(result)
```



* modf( )

  将指定数字拆分成两部分,一部分为小数部分,一部分为整数部分

```
num = 12.55
result = math.modf(num)
print(result)

```



* copysign( )

  让前面数字的符号和后面数字的符号始终保持一致

```
result = math.copy(-9,-2)
print(result)
```



* fsum( )

  功能和sum( )一样,计算序列的和. 返回值是浮点数

```
list1 = [1,2,3,4,5,6]
result = math.fabs(list1)
print(result)
```



* Pi 和 e

```
result = math.pi
print(result)

result = math.e
print(result)
```



# 10. 随机数模块

使用随机数模块前需要先载入该模块

import random



* random( )

  随机获取 0-1 不包含1的随机浮点数

```
num = random.random()
print(num)
```



* shuffle( )

  将一个序列随机打乱,直接改变原序列的顺序

```
list1 = [1,2,4,5,6,7,89]
random.shuffle(list1)
print(list1)

```



* choice( )

  随机从一个序列中取出一个元素

```
list1 = [1,2,4,5,7,8,5,3]
result = random.choice(list1)
print(result)
```



* uniform( )

  随机获取指定范围内的一个浮点数

```
result = random.uniform(1,100)
print(result)
```



* randrange( )

  随机获得指定范围内的整数

```
result = random.randrange(1,100)
print(result)
```



#  11. 列表

## 11.1 列表基本操作

### 11.1.1 创建列表

#### 11.1.1.1 创建空列表

```
list1 = list()

list1 = []
```

#### 11.1.1.2 创建有数据的列表

```
list1 = [1,23,4,5]
list2 = [1]
```

### 11.1.2 访问列表中的值

列表名[索引值]

```
list1 = ['徐凤年','姜泥','裴南苇','青鸟']
result = list1[1]
print(result)
```



### 11.1.3 修改列表中的值

列表名[索引值] = 新的值

```
list1[1] = '白狐'
print(list1[1])
```



### 11.1.4 删除列表中的值

del 列表名[索引值]

```
del list1[1]
pirnt(list1)
```



del 可以删除任何变量

```
del list1
```



## 11.2 列表的序列操作

### 11.2.1 序列相加 +

```
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
```



### 11.2.2 序列相乘 *

```
list1 = ['徐凤年']
list2 = list1 * 3
print(list2)

```



### 11.2.3 分片 [ : : ]

[起始:终止:间隔]  都不包含终止位置

```
list1 = [1,2,3,4,5,6,8,9]
result = list1[1:2]
print(result)

result = list1[:4]
print(result)

result = list1[::2]
print(result)
```



### 11.2.4 成员检测

in     not in 

```
list1 = ['徐凤年','姜泥','王初东','裴南苇']
result = '徐凤年' in list1
print(result)

result = '白狐脸' not in list1
print(result)
```



### 11.2.5 len( ) \ max( )	\ min( )

```
list1 = [1,23,4,5,6,7,8]
result = len(list1)
print(result)

result = max(list1)
print(result)

result = min(list1)
print(result)
```



## 11.3 遍历列表

### 遍历一级列表

```
list1 = ['徐凤年','姜泥','白狐脸','裴南苇','鱼幼薇','青鸟']
for each in list1
	print(each)
	

num = 0
while num < len(list1):
	print(list1[num])
```



### 遍历等长二级列表

```
list1 = [
  ['北凉','徐凤年','徐骁'],
  ['西蜀','曹常卿','姜泥'],
  ['离阳','人猫','元本溪']
]
for x,y,z in list1:
	print(x)
	print(y)
	print(z)
	
```



###  遍历不等长的二级列表

```
list1 = [
  ['北凉','徐凤年'],
  ['曹常卿','姜泥'],
  ['离阳','人猫','元本溪','徐骁']
]

for i in list1:
	for j in i:
		print(j)
```



## 11.4 列表推导式

### 11.4.1 普通格式

```
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [i * 2 for i in list1]
print(list2)
```



###  11.4.2 带有条件的列表推导式

```
list1 = [1,2,3,4,5,6,7,8]
list2 = [i for i in list1 if i % 2 == 0]
print(list2)
```



### 11.4.3 多循环列表推导式

```
list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,13,14]
list3 = [i + j for i in list1 for j in list2]
print(list3)
```



### 11.4.4 带条件的多循环列表推导式

```
list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,13,14]
list3 = [i + j for i in list1 for j in list2 if list1.index(i) == list2.index(j)]
print(list3)
```



## 11.5 列表函数

* append( )

  向列表的末尾添加元素

  ```
  list1 = [1,2,3,4]
  list1.append(5)
  print(list1)
  ```

* insert( )

  向列表指定索引位置前添加指定元素

  insert(索引,值)

  ```
  list1 = [1,2,3,4]
  list1.insert(1,'人')
  print(list1)
  ```

* extend( )

  使用一个列表去扩充另一个列表

  ```
  list1 = [1,2,3,4,5,6]
  list2 = [7,8,9,10,11]
  list1.extend(list2)
  print(list1)

  ```

* pop( )

  将列表指定位置的值取出来. 默认取出最后一位

  ```
  list1 = [1,2,3]
  result = list1.pop(0)
  print(result)
  print(list1)

  result = list1.pop()
  print(result)
  print(list1)
  ```

* remove( )

  将列表中的指定元素删除

  remove(值)

  ```
  list1 = ['人猫','徐凤年','姜泥']
  list1.remove('人猫')
  print(list1)
  ```

* clear( )

  将列表清空

  ```
  list1 = [1,2,3]
  list1.clear()
  print(list1)
  ```

* copy( )

  复制列表,复制得到的列表和原列表的内存id不同

  ```
  list1 = [1,2,3,4]
  list2 = list1.copy()
  print(list2)
  print(id(list2))
  ```

* count( )

  计算字符串中指定字符出现的次数    不同于字符串的函数count(指定字符,起始,终止)  

  ```
  list1 = [1,1,1,23,44,24,15,66,3]
  result = list1.count(1)
  print(result)
  ```

* index( )

  获取列表中指定元素出现的索引值

  ```
  list1 = ['徐骁','徐凤年','姜泥','裴南苇']
  result = list1.index('徐凤年')
  print(result)
  ```

* reverse( )

  将列表排列顺序颠倒,直接改变原列表

  ```
  list1 = [1,2,3,4]
  list1.reverse()
  print(list1)
  ```

* sort( )

  将列表按从小到大的顺序排列. 可用参数key reverse 

  ```
  list1 = [1,2,3,4,5]
  list1.sort()
  print(list1)
  ```

  将列表按从大到小的顺序排列

  ```
  list1.sort(reverse=True)
  print(list1)
  ```

  将列表按自定义的规则排列

  ```
  def func(num):	#一定要有形参
  	return num // 10		# 一定要有return

  list1.sort(key=func,reverse=True)
  print(list1)
  ```

  ​

# 12.元组

## 12.1 创建元组

### 12.1.1 创建空元组

方法一: 使用tuple( )

```
tuple1 = tuple()
print(tuple1,type(tuple1))
```

方法二:使用( )

```
tuple1 = ()
print(tuple1,type(tuple1))
```

### 12.1.2 创建一个元素的元组

```
tuple1 = (1,)
print(tuple1,type(tuple1))

tuple1 = 1,
print(tuple1,type(tuple1))
```

### 12.1.3 创建多个元素的元组

```
tuple1 = (1,23,2,4,5)
print(tuple1,type(tuple1))
```



## 12.2 元组的基本操作(增删改查)

元组不能直接增加,删除,修改元素,

元组基本操作只支持查看元组内的元素: 元组名[索引]

```
tuple1 = (1,23,4,5,5,67)
print(tuple1[1])
```



## 12.3 元组的序列操作

### 12.3.1 序列相加

```
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)
result = tuple1 + tuple2
print(result)
```



### 12.3.2 序列相乘

```
tuple1 = (1,2,3)
result = tuple1 * 2
print(result)

```



### 12.3.3 分片 [ : : ]

```
tuple1 = ('徐凤年','徐骁','姜泥','青鸟','王仙之','曹长青','白狐脸儿')
print(tuple1[:2])	
print(tuple1[3:])	
print(tuple1[1:4])
print(tuple1[::2])	# [起始:终止(不包含):间隔]
```



### 12.3.4 成员检测

```
tuple1 = ('徐凤年','徐骁','姜泥','青鸟','王仙之','曹长青','白狐脸儿')
result = '徐凤年'in tuple1
print(result)

result = '啦啦啦' not in tuple1
print(result)
```



## 12.4 元组的序列函数

### 12.4.1 len() , max(), min(), tuple()

```
tuple1 = ('徐凤年','徐骁','姜泥','青鸟','王仙之','曹长青','白狐脸儿')

length = len(tuple1)
print(length)

tuple2 = (1,23,22,4,5,53,6)
print(max(tuple2))
print(min(tuple2))

list1 = [1,2,3]
tuple3 = tuple(list1)
print(tuple3)
```



## 12.5 元组的遍历

### 12.5.1 遍历普通元组

```
tuple1 = ('徐凤年','徐骁','姜泥','青鸟','王仙之','曹长青','白狐脸儿')
for i in tuple1:
	print(i)
```



### 12.5.2 遍历等长的二级元组

```
tuple1 = ((1,2),(3,4),(5,6))
for x,y in tuple1:
	print(x,y)
```



### 12.5.3 遍历不等长的二级元组

```
tuple1 = ((1,2),(3,4,5),(6,7,8,9))
for i in tuple1:
	for j in i:
		print(j)
```



### 12.5.4 访问多级元组中的值

```
tuple1 = ((1,2),(3,4,5),(6,7,8,9))
print(tuple1[0][1])
```



## 12.6 元组推导式

元组推导式的结果是一个生成器,生成器如果不遍历一遍的话,是不会使用的.

### 12.6.1 普通元组推导式

```
tuple1 = (1,2,3,4,5,6)

tuple2 = (i * 10 for i in tuple1)

for each in tuple2:  # 如果不遍历的话,tuple2这个生成器将一直存在但是不做任何操作
	print(each)
```



### 12.6.2 带有条件的元组推导式

```
tuple1 = (1,2,3,4,5,6)

tuple2 = (i * 10 for i in tuple1 if i % 2 == 0)

for each in tuple2:
	print(each)
```



### 12.6.3 多循环元组推导式

```
tuple1 = (1,2,3,4,5)
tuple2 = (10,20,30,40)

tuple3 = (i + j for i in tuple1 for j in tuple2)

for each in tuple3:
	print(each)
```



### 12.6.4 带有条件判断的多循环元组推导式

```
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)

tuple3 = (i * j for i in tuple1 for j in tuple2 if tuple1.index(i) == tuple2.index(j))

for each in tuple3:
	print(each)
```



## 12.7 元组专用函数

1. index( ) 查看指定元素在元组中的索引值

   ```
   tuple1 = ('华为','小米','大米','三星','iphone')

   print(tuple1.index('华为'))

   print(tuple1.index('三星'))
   ```


2. count( ) 计算指定元素在元组中出现的次数

   ```
   tuple1 = ('华为','华为','三星','三星','iphone')

   print(tuple1.count('华为'))

   print(tuple1.count('三星'))
   ```

   ​

# 13. 字典

## 13.1 创建字典

### 13.1.1 创建空字典

方法一: 使用{ }来创建空字典

```
dict1 = {}
print(dict1,type(dict1))
```

方法二: 使用 dict( ) 来创建空字典

```
dict1 = dict()
print(dict1,type(ditc1))
```



### 13.1.2 创建多个元素的字典

方法一: 使用 { } 来创建多个元素的字典

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
print(dict1,type(ditc1))
```



方法二: 使用dict( ) 来创建多个元素的字典

```
#1.dict(字典)
dict1 = dict({'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'})
print(dict1,type(dict1))

#2.dict(等长二级容器)
tuple1 = (('小丽','马丽丽'),('静静','刘文静'),('瑶瑶','王瑶'),('紫薇','孙紫薇'))
dict1 = dict(tuple1)
print(dict1,type(dict1))

#3.dict(关键字传参)
dict1 = dict(小丽='马丽丽',静静='刘文静',瑶瑶='王瑶',紫薇='孙紫薇')
print(dict1,type(dict1))

#4.dict(zip(键的容器,值的容器))
keys = ('小丽','静静','瑶瑶','紫薇')
values = ('马丽丽','刘文静','王瑶','孙紫薇')
dict1 = dict(zip(keys,values))
```



## 13.2 字典的基本操作(增删改查)

### 13.2.1 字典中直接增加新元素

字典[键] = 值

如果键不存在在字典中,则直接将这个键值对添加到字典中作为新元素

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

dict1['班长'] = '戴帅林'

print(dict1)
```



### 13.2.2 字典中直接删除元素

del 字典[键] 

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
del dict1['小丽']
print(dict1)
```



### 13.2.3 字典中直接修改元素

```
dict1 =  {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
dict1['小丽'] = '马冬梅'

print(dict1)
```



### 13.2.4 字典中查看元素的值

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

print(dict1['小丽'])
```



## 13.3 字典的序列操作

序列相加,序列相乘,分片这些序列操作字典都不支持

字典只能进行成员检测(只检测字典中的键)

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
result = '小丽' in dict1
print(result)

reslut = '王贷' not in dict1
print(result)
```



## 13.4 字典的序列函数

### len( ) , max( ) , min( ), dict( ) 

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

length = len(dict1)
print(length)

dict2 = {1:'数字',2:'数字',3:'数字',4:'数字',5:'数字',6:'数字',}
maxnum = max(dict2) 键
print(maxnum)

minnum = min(dict2)
print(minnum)
```



## 13.5 遍历字典

### 13.5.1 遍历一级字典

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

#方法一:
for i in dict1:
	print(i , dict1[i])

#方法二:
for i,j in dict1.items():
	print(i,j)

```



## 13.6 字典推导式

### 13.6.1 基本字典推导式

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

dict2 = {key:'@'+value for key,value in dict1.items()}

print(dict2)
```

### 13.6.2 带有条件的字典推导式

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}

dict2 = {key:value for key,value in dict1.items() if len(key) == len(value)}

print(dict2)
```

###  13.6.3 带有循环的字典推导式

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
dict2 = {'班长':'戴帅林'}

dict3 = {key+i : value+j for key,value in dict1.items() for i,j in dict2.items()}

print(dict3)

```

### 13.6.4 带有判断的多循环字典推导式

```
dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
dict2 = {'班长':'戴帅林'}

dict3 = {key+i : value+j for key,value in dict1.items() for i,j in dict2.items() if len(value) == len(j)}

print(dict3)
```



## 13.7 字典的专用函数

1. ### clear( )	清空字典

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   dict1.clear()
   print(dict1)
   ```

2. ### copy( )     复制字典

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   dict2 = dict1.copy()
   print(dict2)
   ```

3. ### fromkeys( ) 将容器中的值作为键,设定的第二个参数作为所有键的值,创建字典

   ```
   list1 = [1,2,3,4,5]
   dict1 = {}.fromkeys(list1,'数字')
   print(dict1)

   输出结果:{1:'数字',2:'数字',3:'数字',4:'数字'}
   ```

4. ### get( ) 通过键获取字典中的值

   ```
   # 若键存在,则返回值
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.get('小丽')
   print(result)

   # 若键不存在,则返回None.
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.get('班长')
   print(result)

   # 若键不存在,但是设定了返回值.则返回返回值
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.get('班长','不在')
   print(result)

   ```

   ​

5. ### items( ) 将字典转换成等长的二级元组

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.items()
   print(result)

   ```

6. ### keys( ) 将字典中的键取出来,放进容器中 

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   list1 = dict1.keys()
   print(list1)
   ```

7. ### values( ) 将字典中的值取出来,放进容器中

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   list1 = dict1.values()
   print(list2)
   ```



8. ### pop( ) 删除字典中指定键值对  pop(指定的键,默认值)

   ```
   # 移除存在的键和值
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.pop('小丽')
   print(dict1,result)

   # 移除不存在的键,未设置默认值,则报错!!! pop(不存在的键,还tm没设置默认值) 等着报错吧!!!
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.pop('班长')
   print(dict1,result)

   # 移除不存在的键,设置了默认值 pop(不存在的键,设置了默认值),则返回默认值
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.pop('班长','不在')
   print(dict1,result)
   ```



9. ### popitem( ) 随机移除出字典中的一个键值对

   ```
   dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
   result = dict1.popitem()
   print(result)
   ```



10. ### setdefault( ) 向字典中添加元素

 ```
 # 若要添加的键不存在,则新增进字典中
 dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
 dict1.setdefault('班长','戴帅林')
 print(dict1)

 # 若要添加的键已经在字典中,则不做任何操作
 dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
 dict1.setdefault('小丽','马丽丽')
 print(dict1)
 ```



11. ### update( ) 更新字典,直接改变原字典

    ```
    # update(关键字传参)
    dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
    dict1.update(小丽='马丽丽',静静='刘文静',瑶瑶='大熊太美',紫薇='戏精')
    print(dict1)

    # update(新的字典)
    dict1 = {'小丽':'马丽丽','静静':'刘文静','瑶瑶':'王瑶','紫薇':'孙紫薇'}
    dict1.update({'小丽':'马里奥','静静':'静毛线','瑶瑶':'大熊太美','紫薇':'戏精'})
    print(dict1)
    ```

    # 14.集合

    集合的特征:

    * 集合是无序数据
    * 集合中所有元素都是唯一的,集合自带去重功能
    * 集合中可以包含Number(int,float,bool,complex) , string  , tuple 和 冰冻集合 

## 14.1 创建集合

### 14.1.1 创建空集合

```
使用set() 来创建空集合

set1 = set() 
print(set1,type(set1))
```



### 14.1.2 创建具有多个元素的集合

```
set1 = {1,2,3,4,5,6}
print(set1,type(set1))
```



## 14.2 集合的基本操作(增删改查都不行)



## 14.3 集合的序列操作

集合只支持成员检测这一个序列操作

### 14.2.1 成员检测 in     not in

```
set1 = {1,2,3,44,51,6}
result = 1 in set1
print(result)

result = 222 not in set1
print(result)
```



## 14.5 集合的序列函数

### len() , max() , min() , set() 

```
set1 = {1,2,3,4,5,6}

length = len(set1)
print(length)

maxnum = max(set1)
print(maxnum)

minnum = min(set1)
print(minnum)

list1 = [1,2,3,4,5,6,7]
set1 = set(list1)
print(set1,type(set1))
```



## 14.6 遍历集合

### 14.6.1 遍历一级集合

```
set1 = {1,23,45,3,7,54}
for each in set1:
	print(each)
```



### 14.6.2 遍历二级集合(等长)

```
set1 = {('徐骁','徐凤年'),('西楚姜皇帝','姜泥'),('谢灵云','白狐脸'),('无名氏','呵呵')}
for x,y in set1:
	print(x,y)
```



### 14.6.3 遍历二级集合(不等长)

```
set1 = {('不才','任然'),('张楚','窦唯','何勇'),('陈粒')}

for i in set1:
	for j in i:
		print(j)
```



## 14.7 集合推导式

### 14.7.1 基本集合推导式

```
set1 = {1,2,3,4,5,6,7,8}
result = {i*2 for i in set1}
print(result)
```



### 14.7.2 带条件判断的集合推导式

```
set1 = {1,2,3,4,5,6,7,8}
result = {i * 10 for i in set1 if i % 2 == 0}
print(result)
```



### 14.7.3 多循环集合推导式

```
set1 = {'窦唯','Gai','万晓利'}
set2 = {'女儿情','天干物燥','噢,乖'}

result = {i + j for i in set1 for j in set2}
print(result)
```



### 14.7.4 带条件判断的多循环集合推导式

```
set1 = {'窦唯','Gai','万晓利'}
set2 = {'女儿情','天干物燥','噢,乖'}

result = {i + j for i in set1 for j in set2 if len(i) == len(j)}
```



## 14.7 集合的函数操作

### add( ) 向集合中添加元素

```
set1 = {'窦唯','Gai','万晓利'}

set1.add('朴树')
print(set1)
```



### pop( ) 从集合中随机取出一个元素

```
set1 = {'窦唯','Gai','万晓利'}
result = set1.pop()
print(result)
```



### remove( ) 从集合中删除指定元素

```
set1 = {'窦唯','Gai','万晓利'}

# remove(不存在的元素)   ---  报错
set1.remove('窦唯老婆')

# remove(存在的元素)     --- 正常删除
set1.remove('窦唯')

```



### discard( ) 从集合中删除指定元素

```
set1 = {'窦唯','Gai','万晓利'}

# discard(不存在的元素)  ---  不做任何操作
set1.discard('窦唯老婆')

# discard(存在的元素)    ---  正常删除
set1.discard('窦唯')
```



### clear( ) 清空集合

```
set1 = {'窦唯','Gai','万晓利'}

set1.clear() 

print(set1)
```



### copy( ) 复制集合

```
set1 = {'窦唯','Gai','万晓利'}
set2 = set1.copy()
print(set2,type(set2))
```



## 14.8 集合之间运算函数

### difference( ) 计算一个集合相对另一个集合的差集

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.difference(set2)
print(result)

```



### difference_update( ) 计算一个集合相对另一个集合的差集,并直接改变原集合

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

set1.difference_update(set2)
print(set1)
```



### intersection( ) 计算一个集合和另一个集合的差集

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.intersection(set2)
print(result)
```



### intersection_update( ) 计算一个集合和另一个集合的交集,并直接改变原集合

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

set1.intersection_update(set2)
print(set1)
```



### union( ) 计算两个集合的并集

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.union(set2)
print(result)
```



### update( ) 计算两个集合的并集,并更新原集合

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

set1.update(set2)
print(set1)
```



### symmetric_difference( ) 计算两个集合的对称差集

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.symmetric_difference(set2)
print(result)
```



### symmetric_difference_update( ) 计算两个集合的对称差集并更新原集合

```
set1 = {'徐凤年','徐骁','李义山'}
set2 = {'徐凤年','姜泥','青鸟'}

set1.symmetric_difference_update(set2)
print(set1)
```



## 14.9 集合检测类函数

### issuperset( ) 检测一个集合是否是另一个集合的超集

```
set1 = {'徐凤年','徐骁','李义山','姜泥','青鸟'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.issuperset(set2)
print(result)
```



### issubset( ) 检测一个集合是否是另一个集合的子集

```
set1 = {'徐凤年','徐骁','李义山','姜泥','青鸟'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set2.issubset(set1)
print(result)
```



### isdisjiont( ) 检测两个集合是否没有交集

```
set1 = {'徐凤年','徐骁','李义山','姜泥','青鸟'}
set2 = {'徐凤年','姜泥','青鸟'}

result = set1.isdisjoint(set2)
print(result)
```



## 14.10 冰冻集合

1. 创建空冰冻集合

```
set1 = frozenset()
print(set1,type(set1))
```



2. 创建多个元素的冰冻集合

```
set1 = frozenset({1,2,3,4,5,6,8,7,9})
print(set1,type(set1))
```



3. 遍历冰冻集合

```
set1 = frozenset({1,2,3,4,5,6,8,7,9})
for i in set1:
	print(i)
```



4. 冰冻集合推导式

```
result = {i+2 for i in set1}
print(result)

```



5. 冰冻集合函数

```
冰冻集合没有专用的函数
但是
冰冻集合可以使用所有不改变原集合的集合函数
```



# 15. 文件操作

## 15.1 文件操作的步骤

1. 打开文件
2. 对文件进行操作
3. 关闭文件

### 15.1.1 文件写入操作

```
# 1. 使用open()打开指定文件
fp = open('/Users/apple/desktop/01.txt','w')

# 2. 对文件进行写入操作
fp.write('写入操作,输入........')

# 3. 关闭文件
fp.close()
```

### 15.1.2 文件读取操作

```
# 1. 使用open()打开指定文件
fp = open('/Users/apple/desktop/01.txt','r')

# 2. 对文件进行读取操作
result = fp.read()
print(result)

# 3. 关闭文件
fp.close()
```



## 15.2 文件操作函数

### 1. open() 打开或新建文件

```
变量 = open('文件绝对路径','打开模式')

打开模式:

基础模式:( w,a,x,r )
w:	write 	写入模式	若文件不存在,则新建. 若已经存在,打开文件并清空原有内容
a:  append 	追加模式	若文件不存在,则新建. 若已经存在,则打开文件,则原有内容基础上添加
x:	xor		异或模式	若文件不存在,则新建. 若已经存在,则报错
r:	read	读取模式	可执行读取文件的相关操作

增强模式( +,b ) 只能和基础模式配合使用 
+:	plus	读写模式	在w,a,x 或者 r 的基础上加+,则实现读写都可的功能
b:	byte	位模式		 在位模式下进行读或者写或者读写的操作

组合方式:
w:		若文件不存在,则新建文件等待写入操作. 若文件已存在,则打开文件并清空原内容,之后可以进行写入操作. 
a:  	若文件不存在,则新建文件等待写入操作. 若文件已存在,则打开文件并清空原内容,之后可以进行写入操作.
x: 		若文件不存在,则新建文件等待写入操作. 若文件已存在,则直接报错!
r: 		若文件不存在,则报错! 若文件已存在,则打开文件,并可进行读取相关的操作

w+:		若文件不存在,则新建文件等待写入操作. 若文件已经存在,则打开文件并清空内容,之后可执行写入或读取
r+:		若文件不存在,则报错! 若文件已经存在,则打开文件,之后可执行写入操作和读取操作
x+:		若文件不存在,则新建文件等待写入操作, 若文件已经存在,则报错!
a+:		若文件不存在,则新建文件等待写入操作, 若文件已经存在,则打开原文件,在原文件的基础上可追加或读取

wb:		若文件不存在,则新建文件等待写入操作.若文件已经存在,则打开文件并清空内容.所有写入需要用encode()编码
rb:		若文件不存在,则报错! 若文件已经存在,则打开文件可进行读取操作.所有读取内容要用decode()解码
ab:		若文件不存在,则新建文件等待写入操作,若文件已经存在,则打开文件并追加内容.所有写入需要用encode()编码
xb:		若文件不存在,则新建文件等待写入操作,若文件已经存在,则报错!

wb+:	若文件不存在,则新建文件且可读可写.若文件已存在,清空内容,可读可写.读要用decode()解码.写要用			encode()编码
rb+:	若文件不存在,则报错! 若文件已存在,则打开文件,可读可写.读要用decode()解码.写要用encode()编码
ab+:	若文件不存在,则新建文件且可读可写.若文件已存在,打开原内容,追加内容.读要用decode()解码.写要用			encode()编码
xb+:	若文件不存在,则新建文件且可读可写,若文件已存在,直接报错! 读要用decode()解码.写要用encode()编码
```



如: 	 使用r+模式打开文件

```
# 打开文件
fp = open('/Users/apple/desktop/01.txt','r+')   # 若此时01.txt不存在,则直接报错

# 先读取原有内容
content = fp.read()
print(content)

# 写入新内容
fp.write('写入内容')

# 移动指针
fp.seek(0) #单位是字节 0表示移动到开头位置

# 再读取现在的内容
content = fp.read()
print(content)

# 关闭文件
fp.close()
```



如: a+b模式打开或新建文件

```
# 打开文件
fp = open('/Users/apple/desktop/01.txt','a+b')

# 追加内容
fp.write('在原有基础上追加内容'.encode())

# 移动指针到开头
fp.seek(0)

# 读取全部内容
content = fp.read().decode()
print(content)

# 关闭文件
fp.close()
```



### 2. read() 读取文件内容

1. 文件.read( ) 默认读取全部文件内容

```
fp = open('/Users/apple/desktop/01.xtx' ,'r')

content = fp.read()
print(content)

fp.close()
```



2. 文件.read(指定字符个数) 读取指定的字符个数

```
fp = open('/Users/apple/desktop/01.txt','r')

content = fp.read(20)
print(content)

fp.close()
```



### 3. readline() 读取一行文件内容

文件.readline( ) 默认读取一行内容

文件.readline(指定字符个数) 默认读取指定字符长度内容,超过一行按一行算,不够一行就不够呗 

```
fp = open('/Users/apple/desktop/01.txt','r')

# 读取一行文件的内容
content = fp.readline()  
print(content)

# 移动指针
fp.seek(0)

# 读取指定字符长度,若不满足一行则只读5个字符,若超过一行,则只读一行字符
content = fp.readline(5) 
print(content)

# 关闭文件
fp.close()
```



### 4. readlines() 一次读取多行内容

```
# 打开文件
fp = open.(''/Users/apple/desktop/01.txt','r')

# 默认读取全部行
content = fp.readlines()
print(content)

# 移动指针
fp.seek(0)

# 读取指定字符长度的行数
content = fp.readlines(20)  # 字符长度若不足一行,则按一行算,若超过一行,则显示下一整行
print(content)

# 关闭文件
fp.close()
```



### 5. truncate() 文件截取

保留指定的字节长度,其他都删除   单位:字节!!!!

```
fp = open('/Users/apple/desktop/01.txt'.'r+')

fp.truncate(12)  # 保留指定的字节长度,其他都删除

fp.close()
```



### 6. tell() 获取当前打开的文件的指针位置

```
fp = open('/Users/apple/desktop/01.txt','r')

num = fp.tell()
print(num)

fp.close()
```



### 7. seek() 将指针移动指定的字节长度

```
fp = open('/Users/apple/desktop/01.txt','r')

fp.seek(21)

content = fp.read()   # read() 的内容是在指针之后的内容才能读取
print(content)   

fp.close()
```



### 8. 自定义函数获取指定行数

```
# 自定义函数实现读取文件中的指定行数

def myReadLines(path,hang=-1,sep='\n'):  
# path:要打开的文件路径  hang:显示文件内容的行数  sep:当前操作系统中默认的换行符号

    # 打开指定文件
    fp = open(path,'r')

    # 获取文件内所有内容
    content = fp.read()

    # 使用换行符号切割字符串,放入列表lists中
    #若最后一行切完是一个空字符串,则需要分片去掉最后一个 lists = content.split(sep)[0:-1]
    lists = content.split(sep) 

    # 判断用户输入的行数,并确认最终输出的总行数
    maxhang = len(lists)

    if hang < 0 or hang >= maxhang:
        hang = maxhang
    else:
        hang = int(hang)

    result = [i + sep for i in lists[:hang]]  # 用分片来控制最终的列表的长度

    # 如果要用列表的形式直接呈现,直接输入result就可以了
    #print(result)

    # 遍历最终的列表result 输出内容
    for i in result:
        print(i,end='')

myReadLines('/Users/apple/desktop/01.txt',5)
```



# 16. os (操作系统)模块

使用os模块之前要先导入

import os

## 16.1 os模块函数



### 16.1.1 文件夹类os操作

#### 1. os.listdir() 

功能: 获取指定路径文件夹下所有的文件及文件夹的列表

格式: os.listdir(目标文件夹路径)

返回值: 所有文件及文件夹的列表

```
lists = os.listdir(/Users/apple/desktop)
print(lsits)
```



#### 2. os.mkdir() 

功能: 在指定路径创建空文件夹

格式:os.mkdir(目录路径,0o权限数组) 未设定则按默认权限创建

返回值:创建的文件夹绝对路径

```
os.mkdir('/Users/apple/dekstop/a',0o755)

os.mkdir('/Users/apple/desktop/b)
```



#### 3. os.rmdir() 

功能: 删除指定路径的空文件夹

格式: os.rmdir(目录路径)

返回值:None

```
os.rmdir('/Users/apple/desktop/a')
```



#### 4. os.makedirs()

功能: 递归创建空文件夹

格式: os.makedirs(目录路径)

返回值: 创建的目录的字符串路径

```
os.makedirs('/Users/apple/desktop/aaa/bb/c')
```



#### 5. os.removedirs()

功能: 递归删除空文件夹

格式: os.removedirs(目录路径)

返回值: None

```
os.removedirs('/Users/apple/desktop/aaa/bb/c')
```



#### 6. os.getcwd() 

功能: 获取当前默认工作的文件夹路径

格式: os.getcwd() 

返回值:当前工作的目录路径字符串

```
pathnow = os.getcwd()
print(pathnow)
```



#### 7.os.chdir()

功能: 改变当前工作的文件夹路径

格式: os.chdir(目的地路径)

返回值:None

```
# 改变文件夹,在桌面创建新文件

os.chdir('/Users/apple/desktop')
fp = open('01.txt','w')
print(os.getcwd())
fp.close
```



### 16.1.2 通用os操作

#### 1. os.rename( ) 

功能: 重命名文件夹

格式: os.rename(原文件夹或文件路径,新名文件夹或文件路径)

返回值: None

```
os.rename('/Users/apple/desktop/01.txt','/Users/apple/desktop/02.txt')
```



#### 2. os.stat( )

功能: 获取指定文件夹或文件的相关信息(属性)

格式: os.stat(指定文件夹或文件的目录)

返回值: 包含属性信息的元组

```
result = os.stat('/Users/apple/desktop/01.txt)
print(result)
```



#### 3. os.getenv()

功能: 获取当前系统的环境变量信息

格式: os.getenv(获取的环境变量名称) 'PATH' 要大写

返回值: 字符串

```
result = os.getenv('PATH')
print(result.split(':'))
```



#### 4. os.putenv()

功能: 设置环境变量信息

格式: os.putenv(环境变量参数,新增值)

返回值: None

```
os.putenv('PATH','/')
os.system('mydir')
```



#### 5. os.system()

功能: 在python中使用系统命令

格式: os.system(系统命令)

返回值: 系统命令返回的结果

```
os.system('ls')
```



### 16.1.3 os模块中子模块path

#### 1. os.path.abspath() 

功能:路径返回绝对路径

格式: os.path.abspath(指定路径)

```
result = os.path.abspath('/Users/apple/desktop)
print(result)

```



#### 2. os.path.dirname() 

功能: 获取路径中的路径部分

格式: os.path.dirname(指定路径)

返回值: 返回路径部分

```
dname = os.path.dirname('/Users/apple/desktop')
print(dname)

```



#### 3. os.path.basename()

功能: 获取路径中文件的主体部分(文件名.扩展名)

格式: os.path.basename()

返回值: 返回指定路径的主体部分

```
bname = os.path.basename('/Users/apple/desktop')
print(bname)
```



#### 4. os.path.join()

功能: 将两个路径连接起来,合成一个路径

格式: os.path.join(路径1,路径2)

返回值: 合成之后的路径

```
fullpath = os.path.join('/Users/apple','desktop')
print(fullpath)
```



#### 5. os.path.split()

功能: 将指定路径的文件拆分成路径和主体部分,放入元组中

格式: os.path.split(指定绝对路径)

返回值: 元组 (路径部分,主体部分)

```
path1 = '/Users/apple/desktop/01.txt'
tuple1 = os.path.split(path1)
print(tuple1)

```



#### 6. os.path.splitext()

功能: 将指定路径的文件拆封成路径主体 和 扩展名,放入元组

格式: os.path.splitext(指定路径)

返回值: 元组 (名称,扩展名)

```
path1 = '/Users/apple/desktop/01.txt'
tuple1 = os.path.splitext(path1)
print(tuple1)
```



#### 7. os.path.getsize()

功能: 获取指定路径的文件大小.无法获取文件夹大小!

格式: os.path.getsize(指定文件路径)

返回值: 文件大小

```
path1 = '/Users/apple/desktop/01.txt'
size = os.path.getsize(path1)
print(size)
```



#### 8. os.path.isdir()

功能: 判断指定路径是不是文件夹

格式: os.path.isdir(指定路径)

返回值: True 是文件夹  False  不是文件夹

```
result = os.path.isdir('/Users/appple/desktop')
print(result)
```



#### 9. os.path.isfile()

功能: 判断指定路径是不是文件

格式: os.path.isfile(指定路径)

返回值: True 是文件  False 不是文件

```
result = os.path.isfile('/Users/apple/desktop/01.txt')
print(result)
```



#### 10. os.path.islink()

功能: 判断指定路径是不是快捷方式

格式: os.path.islink(指定路径)

返回值: True 是链接  False 不是链接

```
result = os.path.islink('/Users/apple/desktop/01.txt')
print(result)
```



#### 11. os.path.getctime()

功能: 获取指定路径的文件或者文件夹的创建时间

格式: os.path.getctime(指定路径)

返回值: 时间戳

```
creattime = os.path.getctime('/Users/apple/desktop/test/')
print(creattime)

```



#### 12. os.path.getatime()

功能: 获取指定路径的文件或者文件夹的访问时间

格式: os.path.getatime(指定路径)

返回值: 时间戳

```
activetime = os.path.getatime('/Users/apple/desktop')
print(activetime)
```



#### 13. os.path.getmtime() 

功能: 获取指定路径文件或者文件夹的修改时间

格式: os.path.getmtime(指定路径)

返回值: 时间戳

```
modifytime = os.path.getmtime('/Users/apple/desktop/01.txt)
print(modifytime)
```



#### 14. os.path.exists() 

功能: 判断指定路径的文件或者文件夹是否存在

格式: os.path.exists(指定路径)

返回值: True 存在  False 不存在

```
result = os.path.exists(指定路径)
print(result)
```



#### 15. os.path.isabs()

功能: 判断指定路径是不是一个绝对路径

格式: os.path.isabs(指定路径)

返回值: True 是绝对路径 False 不是绝对路径

```
result = os.path.isabs('/Users/apple/desktop/01.txt')
print(result)

```



#### 16. os.path.samefile()

功能: 判断两个路径指向的是不是同一个文件

格式: os.path.samefile(指定路径1,指定路径2)

返回值: True 是相同文件  False 不是同一个文件

```
path1 = '../../desktop/01.txt
path2 = '/Users/apple/desktop/01.txt'
result = os.path,sanmefile(path1,path2)
print(result)
```



### 16.1.4 os模块中的值

#### 1. os.curdir

print(os.dir)

当前文件夹符号     

用 . 来表示



#### 2. os.pardir

print(os.pardir)

当前文件夹的上一层目录   即父级文件夹

用 .. 表示



#### 3. os.name

print(os.name)

当前系统的内核名称

win — > nt    linux/unix -> posix



#### 4. os.linsep

print(os.sep)

当前系统的默认换行符

win -> \r\n    linux/unix -> \n



#### 5.os.sep

print(os.sep)

当前系统的路径分隔符

win -> / or \    linux/unix -> /



#### 6. os.extsep

print(os.extsep)

当前系统的文件名和后缀之间的分隔符

win/linux/unix -> .



### 16.1.5 自定义函数获取文件夹大小

```
# 自定义函数获取文件夹大小
import os

def get_dir_size(path):
    # 获取指定文件夹的文件信息
    lists = os.listdir(path)
    
    # 初始化大小计数
    size = 0
    # 通过拼接获取完整路径
    for i in lists:
        fullpath = os.path.join(path,i)
        
        # 判断路径是不是文件,是文件则获取大小并累加到size.
        if os.path.isfile(fullpath) or os.path.islink(fullpath):
            size += os.path.getsize(fullpath)
        
        # 判断路径是不是文件夹,如果是文件夹则递归计算大小,累加到size中
        elif os.path.isdir(fullpath):
            size += get_dir_size(fullpath)
    return size

# 调用函数
result = get_dir_size('/Users/apple/desktop/python教材')
print(result)
```



# 17. shutil 高级系统模块

使用shutil高级系统模块需要先导入该模块

import shutil

## 17.1 复制功能函数

### 17.1.1 文件复制类函数

#### 1. shutil.copy()

功能: 将指定路径的文件复制到另一个路径

格式: shutil.copy('原文件路径','目标路径')

返回值: 目标路径

```
import shutil
shutil.copy('/Users/apple/desktop/01.py','/Users/apple/desktop/test/a.py')
```



#### 2. shutil.copy2()

功能: 复制指定路径的文件和文件信息到指定另一个路径

格式: shutil.copy2('原文件路径','目标路径')

返回值: 目标路径

```
import shutil
shutil.copy2('/Users/apple/desktop/01.py','/Users/apple/desktop/test/a.py')
```



#### 3. shutil copyfile()

功能: 复制指定文件的内容到另一个文件中(默认清空另一个文件)

格式: shutil.copyfile('原文件路径','目标路径')

返回值: 目标文件路径

```
import shutil
shutil.copyfile('/Users/apple/desktop/01.txt','/Users/apple/desktop/test/a.txt')
```



#### 4. shutil copyfileobj()

功能: 复制指定文件的内容到另一个文件中(可选择打开模式)

格式: shutil.copyfileobj(open('原文件路径','打开模式'),open('目标地址','打开模式'))

```
import shutil
shutil.copyfileobj(open('/Users/apple/desktop/01.txt','r'),open('/Users/apple/desktop/test/a.txt','a'))
```



### 17.1.2 文件夹复制类函数

#### 1. copytree()

功能: 复制一个文件夹到指定位置

格式: shutil.copy('原文件夹路径','指定路径') 

```
import shutil
shutil.copytree('/Users/apple/desktop/test/','/Users/appple/desktop/a/')
```



#### 2. copymod()

功能: 复制一个文件夹的权限给另一个文件夹(两个必须都存在)

格式: shutil.copymod('原文件夹路径','指定路径')

```
import shutil
shutil.copymod('/Users/apple/desktop/test/','/Users/apple/deskt/a/)
```



#### 3. copystat()

功能: 复制一个文件夹的相关信息给另一个文件夹(两个都必须存在)

格式: shutil.copystat('原文件夹路径','目标文件夹路径')

```
import shutil
shutil.copystat('/Users/apple/desktop/a','/Users/apple/desktop/test/')
```



### 17.1.3 文件夹(非空)递归删除函数

#### 1. rmtree()

功能: 递归删除非空文件夹 (os.removedirs()只能递归删除空文件夹)

格式: shutil.rmtree('删除文件夹的路径')

```
import shutil
shutil.rmtree('/Users/apple/desktop/test')
```



### 17.1.4 文件和文件夹通用函数

#### 1. move() 

功能: 剪切,将指定文件剪切到另一个位置

格式: shutil.move('原文件路径','指定路径')

```
import shutil

shutil.move('/Users/apple/desktop/a/01.py','/Users/apple/desktop')

shutil.move('/Users/apple/PycharmProjects','/Users/apple/desktop/')
```



### 17.1.5 系统相关函数

#### 1. which()

功能: 查找系统命令所在的文件路径

格式: shutil.which('系统命令')

返回值: 命令所在的系统变量PATH

```
import shutil
result = shutil.which('ls')
print(result)
```



#### 2. disk_usage()

功能: 获取指定系统磁盘的使用情况

格式: shutil.disk_usage('系统磁盘路径')

```
import shutil
result = shutil.disk_usage('/')
print(result)
```



### 17.1.6 归档和解档函数

#### 1. shutil.make_archive()

功能: 创建一个归档文件,指定归档文件的格式.再将其他文件或文件夹放入归档文件中

格式: shutil.make_archive('归档文件路径','归档文件格式','放入的文件或文件夹路径')

```
import shutil
shutil.make_archive('/Users/apple/desktop/guidan','zip','/Users/apple/desktop/test')
```



#### 2. shutil.unpack_archive()

功能: 将归档文件夹中的全部文件解包到指定路径

格式: shutil.unpack_archive('归档文件路径','输出路径')

```
import shutil
shutil.unpack_archive('/Users/apple/desktop/guidan.zip','/Users/apple/desktop/nimabi')
```



#### 3. shutil.get_archive_formats()

功能: 获取当前系统允许的压缩文件格式

```
import shutil
result = shutil.get_archive_formats()
print(result)
```



#### 4. shutil.get_unpack_foramats()

功能: 获取当前系统中允许的解包格式

```
import shutil
result = shutil.get_unpack_formats()
print(result)
```





#### 18. zipfile模块-zip压缩

进行压缩操作之前要先导入压缩模块

import zipfile

## 18.1 zipfile模块常用函数



### 1. zipfile.ZipFile() 

功能: 创建一个压缩文件

格式: zipfile.ZipFile(1.创建压缩文件位置, 2.打开模式, 3.是否压缩, 4.压缩文件是否大于2G)

```
参数:
1. 创建压缩文件绝对路径
2. 打开模式 
	w : 新建一个压缩文件夹,或者覆盖一个已有的zip文档
	a : 将数据追加到一个现存的zip文档中
	r : 打开一个已有的zip文件
3. 压缩方式:
	zipfile.ZIP_STORED 		不存储不进行压缩(默认)
	zipfile.ZIP_DEFLATED 	对文件进行压缩
4. 压缩文件是否大于2G
	若创建的压缩文件要大于2G,则将zip64 设为 True
	若创建的压缩文件不需要2G,则默认False
```



### 2. zipfile.write()

功能: 将指定文件添加到zip文件中

格式: zipfile.write(要添加的文件,添加后新名字,压缩方式)

```
参数:
1. 要添加的文件:  
	要写入压缩文件中的添加文件的绝对路径
2. 添加后的新名字:
	在压缩文件中的名字,如果不需要更改则不需要传参即可
3. 压缩方式:
	压缩方式,若指定则可以单独设定,不指定则按创建zip文件时设定的进行
```



### 3. extractall()

功能: 从zip压缩文件中解压缩所有的文件

格式: zipfile.extractall(指定输出路径)



### 4. extarct()

功能: 从zip压缩文件中取出指定的文件

格式: zipfile.extract(指定文件,指定输出路径)

## 18.2 压缩文件操作范例

```
import zipfile

# 打开或者创建一个压缩文件
zp = zipfile.ZipFile('/Users/apple/desktop/01.zip','w',zipfile.ZIP_DEFLATED)

# 向创建好的压缩文件中添加要压缩的文件
zp.write('/Users/apple/desktop/01.txt)
zp.write('/Users/apple/desktop/test.py','hellotest.py')

# 关闭压缩文件
zp.close()
```



## 18.3 解压文件操作范例

```
import zipfile

# 打开压缩文件
zp = zipfile.ZipFile('/Users/apple/desktop/01.zip','r')
# 将需要的指定文件或者全部文件解压缩出来
zp.extract('01.txt','/Users/apple/desktop/aa')
zp.extractall('/Users/apple/desktop/bbb')

# 关闭压缩文件
zp.close()
```



## 18.4 zipfile模块其他函数

### 1. zipfile.namelist()

功能: 获取zip文件中的所有文件列表

格式: zipfile.namelist()

```
zp = zipfile.ZipFile('/Users/apple/desktop/01.zip','r')

print(zp.namelist())

zp.close()
```



### 2. zipfile.infolist()

功能: 获取zip文件中的所有信息列表

格式: zipfile.infolist()

```
zp = zipfile.ZipFile('/Users/apple/desktop/01.zip','r')

print(zp.infolist())

zp.close()
```



### 3. zipfile.getinfo()

功能: 获取zip文件中指定文件的信息

格式: zipfile.getinfo(指定文件)

```
zp = zipfile.ZipFile('/Users/apple/desktop/01.zip','r')

print(zp.getinfo('test.txt'))

zp.close()
```



# 19. tar 模块

使用tar模块之前需要先导入模块

import tar

## 19.1 tar 模块常用函数

### 1. tar.open()

功能: 创建或者打开压缩文件

格式: tar.open('创建或者打开的压缩文件名','打开模式')

注意: 打开模式中 使用w则默认不压缩  要压缩的话使用w:gz等压缩格式



### 2. tar.add() 

功能: 向压缩文件中添加内容

格式: tar.add('添加到压缩文件中的文件或文件夹路径','可为空新名字')



### 3. tar.extract() 

功能: 将压缩文件中的指定文件解压到指定路径

格式: tar.extract('指定路径','解压目标路径')



### 4. tar.extractall()

功能: 将压缩文件中的所有文件解压到指定路径

格式: tar.extarctall('解压目标路径')



### 5. tar压缩范例

```
import tar
tarfp = tar.open('/Users/apple/desktop/01.tar','w:gz')

tarfp.add('/Users/apple/desktop/01.py')
tarfp.add('/Users/apple/desktop/test/')


tarfp.close()
```



### 6. tar解压范例

```
import tar
tarfp = tar.open('/Users/apple/desktop/01.tar','r')

tarfp.extract('01.py','/Users/apple/desktop/')
tarfp.extarctall('/Users/apple/desktop/a/')

tarfp.close()
```



# 20. calendar 日历模块

使用日历模块之前需要先导入日历模块

import calendar

## 20.1 日历模块函数

### 1. calendar.calendar()

功能: 获取指定年份的日历字符串

格式: calendar.calendar(年份)

```
import calendar
result = calendar.calendar(2017)
print(result)
```



### 2. calendar.month()

功能: 获取指定年月的日历字符串

格式: calendar.month(年份,月份)

```
import calendar
result = calendar.month(2017,10)
print(result)
```



### 3. calendar.monthcalendar()

功能: 指定年份和月份获取一个时间矩阵列表

格式: calendar.monthcalendar(年份,月份)

```
import calendar
result = calendar.monthcalendar(2017,10)
print(result)

```



### 4. calendar.monthrange()

功能: 通过指定的年月,获取该月份第一天是周几,一共多少天

格式: calendar.monthrange(年份,月份)

```
import calendar
result = calendar.monthrange(2017,10)
print(result)
```



### 5. calendar.isleap()

功能: 判断指定年份是不是闰年

格式: calendar.isleap(年份)

```
import calendar
result = calendar.isleap(2017)
print(result)
```



### 6. calendar.leapdays()

功能: 判断两个指定年份之间有多少个闰年

格式: calendar.leapdays(开始年份,结束年份)

```
import calendar
result = calendar.leapdays(2000,2011)
print(result)
```



### 7. calendar.weekday()

功能: 通过指定年月日,计算这一天是周几

格式: calendar.weekday(年份,月份,日期)

注意: 0–6 表示 周一 — 周天

```
import calendar
result = calendar.weekday(2017,10,13)
print(result)
```



### 8. calendar.timegm()

功能: 将时间元组转换成时间戳

格式: calendar.timegm(时间元组)

```
import calendar
ttp = (2018,1,1,0,0,0,0,0,0)
result = calendar.timegm(ttp)
print(result)
```



# 21. time 日历模块

## 21.1 时间术语解释

### 21.1.1 UTC时间

```
UTC时间又称为世界协调时间,特指格林尼治天文台所在的位置的时间,也叫格林尼治时间.
中国的时区是东八区,比世界协调时间快了8个小时
```



### 21.1.2 夏令时

```
夏令时就是通过在夏季将时间人为调快1个小时.
```



### 21.1.3 时间元组

```
ttp = (年,月,日,时,分,秒,周几,第几天,是否夏令时)
年 : 4位数字
月 : 1-12
日 : 1-31
时 : 0-23
分 : 0-59
秒 : 0-59
周几 : 0-6 对应 周一 - 周天
是否不是夏令时: 0是,其他不是
```



## 21.2 时间模块的值

### 1. timezone

功能: 获取UTC和当前时区时间戳的差值 (UTC时间戳 - 当前时区时间戳)

```
import time 
print(time.timezone)
```



### 2. altzone

功能: 在夏令时的情况下,获取UTC时间和当前时区的差值

```
import time 
print(time.altzone)
```



### 3. daylight

功能: 检测是否是夏令时,0 就是 夏令时  非零不是夏令时

```
import time 
print(time.daylight)
```



## 21.3 时间模块的函数

### 1. time.asctime() 

功能: 把时间元组转换成可读字符串

格式: time.asctime(时间元组)

```
import time 
result = time.asctime((1992,2,1,21,33,44,0,0,0))
print(result)
```



### 2. time.localtime()

功能: 获取当前的时间元组

格式一: time.localtime()

​	返回值: 当前的时间元组

格式二: time.localtime(时间戳)

​	返回值: 指定时间戳转换成本地时间元组

```
import time 
result = time.localtime()
print(result)

result = time.localtime(1231424)
print(result)

```



### 3. time.gmtime()

功能: 获取当前UTC时间元组

格式一: time.gmtime()

​	返回值: 当前UTC时间元组

格式二: time.gmtime(12414413)

​	返回值: 将指定时间戳转换成UTC时间元组

```
import time
result = time.gmtime()
print(result)

result = time.gmtime(135454426)
print(result)
```



### 4. time.ctime()

功能: 获取本地时间的字符串格式

time.ctime() == time.asctime(time.locatime())

```
import time 
result = time.ctime()
print(result)
```



### 5. time.mktime()

功能: 将时间元组转换成时间戳

格式: time.mktime(时间元组)

```
import time
result = time.mktime((1992,2,1,23,45,22,0,0,0))
print(result)

```



### 6. time.clock()

功能: 获取当前cpu时间,多用于计算程序运行时间

格式: time,clock()

```
import time

starttime = time.clock()

lists = [i *  2 for i in range(1,10000)]

endtime = time.clock()

ptime = endtime - starttime
print(ptime)
```



### 7. time.perf_counter()

功能: 获取当前cpu时间,可计算sleep()的时间.推荐使用

格式: time.perf_counter

```
import time

starttime = time.perfcounter()

time.sleep(2)

endtime = time.perf_counter()

ptime = endtime - starttime
print(ptime)
```



### 8. time.sleep() 

功能: 使程序睡眠,在此处等待指定的秒数

格式: time.sleep(秒数)

```
import time

time.sleep(15)

print('有完没完了测试需要15s么!?')
```



### 9. time.strftime()

功能: 指定时间字符的格式,将指定的时间元组转换成指定格式字符

格式: time.strftime('字符格式',时间元组)

字符格式中:

​	%Y		代表年

​	%m		代表月

​	%d		代表日

​	%H		代表时

​	%M		代表分

​	%S		代表秒

```
import time
ttp = (1992,2,1,0,2,3,0,0,0)

result = time.strftime('%Y年%m月%d日,%H时%M分%S秒',ttp)
print(result)

```



### 10. time.strptime()

功能: 将格式化之后的时间字符按之前的格式还原到时间元组

格式: time.strptime('格式化之后的字符串','格式化的格式')

```
import time

result = time.strptime('1992年2月1日,0时2分3秒','%Y年%m月%d日,%H时%M分%S秒')

print(result)
```



### 11. time.time()

功能: 获取本地的时间戳

格式: time.time()

```
import time
print(time.time())
```



# 22.面向对象 Object Oriented

面向对象和面向过程的区别：

面向过程开发，以函数作为基本结构使用：

~~~
吃饭      -> 吃饭的函数
喝水      -> 喝水函数
洗衣服    -> 洗衣服的函数
睡觉      -> 使用充气娃娃的函数
看电影    -> 买票开电影函数
....
~~~

面向对象的开发，以对象作为基本结构使用：

~~~
吃饭->调用女盆友的喂饭功能
喝水->调用女朋友的喂水功能
洗衣服->调用女朋友的洗衣服功能
睡觉->调用女朋友的陪睡功能
...
~~~

面向对象的开发非常适合大型程序开发，开发速度和后期维护都比过程化开发要好很多。同时，也会降低一点效率。



## 22.1 类和对象

加一道笔试题：

print(dir('a')) 输出结果是什么

从类中 和对象中来回答这个问题 

正常类中的属性和方法都能访问  来用print (类.__dict__)

之后实例化对象

来用ptint(对象.__dict__)

而这个print('a'.__dict__)则两个都有 也就是无论是在类中和对象中的成员方法和属性 都能来访问

#### 1.类

什么是类：

类是一个实物的特征的集合，是抽象的概念。

~~~啊
人类就是一个类  
动物类也是一个类
鸟类就是一个类
女朋友也是一个类
基友也是一个类
瓶子都是一个类

打蛋蛋是一个类
XXOO也是一个类
撩妹也是一个类
开车也是一个类
打人也是一个类


~~~



#### 2.对象

什么是对象：

对象就是具体存在的看得见摸得着的某个实物。

```
霍云瑞这个人他是一个对象
霍云瑞家的那个小鸡鸡是一个对象
霍云瑞的第一个女朋友就是一个对象
霍云瑞的当前的基友就是一个对象    
这个瓶子就是一个对像。
教室后面那个空调就是一个对象。

昨天霍云瑞打一次自己的蛋蛋，就是一个对象
今天中午霍云瑞吧马浚龙XXOO了就是一个对象
今天上午霍云瑞吧马俊龙撩了就是一个对象
马俊龙今天晚上把霍云瑞打了，这就是一个对象
```



#### 3.类和对象的关系

**类是多个对象归纳总结而来的，是一种概念，包含所有对象。**

```
由对象总结出类的过程，叫做抽象化
```

**对象是类的具体实现或者实施而来，他是真实的，特指某个事物**

```
由类制作出对象的过程，叫做实例化
```

## 

### 22.1.1 如何书写类文件

推荐使用驼峰命名法来书写文件：

**驼峰命名法：**

```
类名：每个单词的首字母大写

    人类  Person
    开车  DriveCar
    撩妹  LiaoMei
    ....

函数名/变量：除了第一个单词之外首字母大写

    泷泽萝拉  longZeLuoLa

    约炮函数  yuePao  或者yue_pao（不是驼峰命名）
    
    一个文件如果是一个单独的类，那么直接使用类名来当作文件名即可
```



### 22.1.2 类的组成

**类中只有2种内容：成员属性和成员方法**

```
成员属性:
    用于描述类的特征的变量就是成员属性

成员方法：
    用于描述类的功能的函数就是成员方法
```



### 22.1.3 类的书写规则

```
1.必须使用class关键字来声明一个类
2.类的名称需要符合驼峰命名法（规范）
3.类中只能存在2种内容，成员属性和成员方法，除此之外，所有的代码都禁止出现！
4.声明成员属性时，所有成员属性必须有值，如果没值会报错！，推荐使用None等值代替
5.成员方法只需要按照函数的规则声明即可
```



### 22.1.4 实例化对象

**例化对象格式**

```
对象变量 = 类()

```

**类的类型为 type**

```
<class 'type'>

```

**类的值就是类本身**

```
<class '__main__.Person'>
```

**对象的类型为类**

```
<class '__main__.Person'>
```

**对象的值，对象本身**

```
<__main__.Person object at 0x020DC650>
```



### 22.1.5 检测类和对象的成员

检测类成员

```
类名.__dict__

```

检测对象成员

```
对象.__dict__
```



### 22.1.6 类和对象成员的操作

#### 1.类成员操作

```
访问类中成员
    类名.成员属性名
    类名.成员方法名()      （没有参数要求，所有方法都可以通过类访问）

修改类中成员
    类名.成员属性名 = 值
    类名.成员方法名 = 新值  （如果需要函数只能用lambda）

删除类中成员
    del 类名.成员属性名
    del 类名.成员方法名

添加类中成员
    类名.新成员属性名 = 值
    类名.新成员方法名 = 值  （如果需要函数只能用lambda）
```



#### 2.对象成员操作

```
访问对象中成员
    对象变量.成员属性名  需要print
    对象变量.成员方法名()  （必须有一个用于接收对象本身的形参）

修改对象中成员    
    对象变量.成员属性名 = 值
    对象变量.成员方法名 = 新值  （如果需要函数只能用lambda）

删除对象中成员
    del 对象变量.成员属性名
    del 对象变量名.成员方法名

添加对象中成员
    对象变量.新成员属性名 = 值
    对象变量.新成员方法名 = 值 （如果需要函数只能用lambda）
```



### 22.1.7 关于self

他不是关键字，是一个随意书写的字符串而已

```
1.英文单词的意义 ：自己
2.绑定类的方法，只能通过类来访问的方法，就是绑定类的方法
3.非绑定类的方法，就是可以通过对象访问的方法就是非绑定的方法
4.绑定类与非绑定类的方法不取决于语法，而取决于设计者如何设计该方法
5.一般情况下非绑定类的方法第一个参数写单词self，但是这不是唯一的单词，写什么都行，self不是关键字，不是关键字，
```

#### 1.绑定类和非绑定类的区别

class Mangseng:

    class Mangseng:
        #属性
        name='李青'
        color='龙虾皮肤'
        wuqi='拳头'
        #方法
        #绑定类的方法
        def rshanxian():
            print('先R,后闪现')
        #非绑定类的方法：（有参数接受对象）
        def qrq(self):
            print('QRQ伤害最高')
    xiazi=Mangseng()
    #关于self
    #通过类访问(可以访问)绑定类的方法
    #通过对象访问(不可以访问)属于非绑定类的方法： 需要(有参数接受对象）
    xiazi.qrq()
    
    #通过对象访问
    #会自动将对象传入方法的第一个参数中
    #self不是关键字是推荐使用的专用于接受当前对象的形参而已！
    xiazi.qrq()
    #通过类访问
    Mangseng.rshanxian()

# 23. 面向对象的三大特性

面向对象都具有三大特性：**封装**，**继承** 和 多态

## 23.1 封装 

```
私有化封装      -> private  英文单词而已不是关键字
受保护的封装     -> protected  英文单词而已不是关键字
公共的封装      -> public 英文单词而不是关键字
```

**检测封装的三个位置：**

```
类中/对象中
类外部/对象外部
子类中
```

### 1.私有化封装 private

私有化封装是最高级别的封装。私有化封装之后的成员,只能在类中/对象中访问，类的外部，子类中都不可以访问到。

```
私有化封装：在成员名称前添加2个_即可
例如：封装heart -> __heart  

python将heart 改名为 _类名__成员名  

封装后的访问限制：
    类中/对象中      可以访问
    类外/对象外      不可以访问
    子类/子类对象     不可以访问
```

~~~
例子：
class Feiji:
    #属性
    name='战斗机'
    color='灰色'
    ##加两个下划线,就变成私有的了
    ##重量不能在飞机的外部进行访问,将weight(私有化)
    #访问的意思就是在外部无法print(fj.weight)了
    __weight='1000KG'
    #方法
    def fei(self):
        print(self.__weight)
        print('我能飞很高')
    def __jiasu(self):#不可以在飞机外部访问(私有化)
        print('一踩离合，我速度就变快了')
    def jiansu(self):#2.这是之前被封装的东西在这
        self.__jiasu()###1.这是给私有化的东西换了个位置,。再想访问这个的话就得访问2
        print('一踩刹车，我速度就变慢了')
#实例华对象
fj=Feiji()
#成员属性的测试
#在对象外访问成员方法
#Feiji.jiansu(1)
#相当于给被封装的就__jiasu方法改了名字,并且上jiansu里给它私有化
fj.jiansu()#只能在对象内部使用,#在对象内部访问私有方法
fj.fei()#只能在内部访问
~~~



### 2.受保护的封装 protected

受保护的封装是一定级别的封装，封装之后，只有部分位置可以访问（类和子类），部分位置（类外）不可以访问。

```
受保护的封装： 在成员名称前添加1个_即可
例如:受保护 money -> _money

封装后的访问限制：
    类中/对象中      可以访问
    类外/对象外      可以访问（原则上类外不行，但是没实现）
    子类/子类对象     可以访问
```



### 3.公共的封装（默认)

#### 公共的封装 public

所有的成员默认都是公共的封装级别，可以在类中，类外，及子类中正常访问

```
类中/对象中            可以访问
类外/对象外            可以访问
子类/子类对象            可以访问
```

# 24. 继承

#### 1 继承的两个概念

```
父类
    用于被继承的类，称之为父类，也叫做基类，或者超类

子类
    继承其他类的类，称之为子类，也叫做派生类
```



#### 2 继承的格式

```
class 父类：
    pass

class 子类(父类)：#继承操作的关键步骤
    pass
```



#### 3 继承的特征

```
1.所有类都是继承自object类（object类对应的对象就是object对象，也是万物皆对象）
2.子类继承父类则可以访问父类的所有成员。（私有成员除外）
3.子类继承父类并不会将父类的所有成员复制到子类当中去，访问父类成员是间接通过父类来访问的，
4.子类可以具有自己独有的属性和方法
5.子类可以重载父类中的方法，只需要设置和父类指定成员相同的名称即可实现重载，重载之后的成员，子类只会访问当前类中的成员，而不会调用父类中同名的成员
6.子类中如果重载父类的方法，并且还想将重载的父类方法借调过来使用，可以在重载的方法中使用如下方法
[父类名.方法()](适合类)  或者  [super().方法()](适合对象)
```





## 24.1单继承和多继承

**单继承：**每个类只能继承一个类的方式称为单继承。

**多继承：**每个类可以同时继承多个类的方式称为多继承。

#### 24.1.1多继承格式

```
class 父类1:
    pass

class 父类2:
    pass

class 子类(父类1,父类2)：
    pass
```

~~~
class Taiye:
    def duanlian(self,b,c):
        print(self,b,c)
        print('锻炼身体,从太爷开始',)
class Yeye:
    def damajiang(self):
        print('点炮了')
class Mama:
    def zuofan(self):
        print('做饭')
class Yiyi:
    def guangjie(self):
        print('逛街')
class Erzi(Yiyi,Mama,Yeye,Taiye):
    def sleep(self):
        print('睡觉')
Erzi.sleep(1)
Erzi.guangjie(1)
Erzi.zuofan(1)
Erzi.duanlian(7,8,9)
~~~



#### 24.2.2 单继承格式

```
class 父类：
    pass

class 子类(父类)：#继承操作的关键步骤
    pass
```

~~~
class Yeye:
    def xiaxiangqi():
        print('爷爷交你下一盘棋')

class Baba(Yeye):
    def dungecai():
        print('爸爸教你做炖菜')

class Gege(Baba):
    def shangwang():
        print('哥哥教你上网')
class Erzi(Gege):
    def sleep():
        print('睡大觉')
Erzi.shangwang()
Erzi.xiaxiangqi()
Erzi.sleep()
Erzi.dungecai()
~~~



## 24.2菱形继承和钻石继承

#### 24.2.1菱形继承格式

```
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

    A
   / \
  B   C
   \ /
    D
菱形继承存在的问题
如果BC类同时继承了A类，D类又继承了BC两个类的情况下(菱形继承)，
在调用BC中某个同名方法(该方法都继承自A类)时会导致继承自A类的该方法被多次调用。产生逻辑问题！
```

#### 

## 24.3 MRO列表

```
原则:
1.子类永远在父类的前面
2.如果继承了多个父类，那么按照()中的顺序在列表中摆放
[最底层的类,之后中间从上到下这个顺序,最上面的父类,object类]
```



## 24.4 super()

~~~
super不是一个关键字,也是不是有函数,他是一个类

super()的作用不是查找父类，而是找MRO列表的上一个类

super()和父类没有任何实质性的关系，只是有时候能调用到父类而已。

在单继承的情况下，super()永远调用的是父类/父对象

格式 :super().方法()   

~~~

## 24.5 mixin设计模式  多继承的使用

```
优点：
1.mixin可以在对类不做任何修改的情况下，扩展类的功能（添加父类）
2.可以方便的组织和维护各种不同组件的划分。
3.可以根据需要任意调整
4.可以避免创建更多的类，也可以避免继承导致的混乱
```

```
#水果类
class Fruit:
    pass

#礼物类和非礼物类
class Gift:
    pass
class NotGift:
    pass

#南方北方类
class South:
    pass
class North:
    pass

#爽和不爽的苹果
class Cool:
    pass
class NotCool:
    pass

#真实水果类
class Apple(Fruit,Gift,North,NotCool):
    pass

class Pear(Fruit,NotGift,North,NotCool):
    pass

class Banana(Fruit,NotGift,North,Cool):
    pass

class Orange(Fruit,Gift,South,NotCool)
```

# 25. 常用的魔术方法

魔术方法就是一个类/对象中的方法，和普通方法唯一的不同时，普通方法需要调用！而魔术方法是在特定时刻自动触发。

## 25.1  __init__

__init__将对象初始化  可以直接给对象里加属性 也可以加方法

```
初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
参数：至少有一个self，接收对象
返回值：无
作用：初始化对象的成员
注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有
```



## 25.2 __new__

```
实例化魔术方法
触发时机： 在实例化对时触发
参数：至少一个cls 接收当前类
返回值：必须返回一个对象实例
作用：实例化对象
注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
没事别碰这个魔术方法，先触发__new__才会触发__init__ 
```



## 25.3 __del__

__del __让程序里运行完 回收变量或者对象里的一些东西 在里面加del self .成员属性，或者是成员方法

```
析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发
参数：一个self 接收对象
返回值：无
作用：使用完对象是回收资源
注意：del不一定会触发当前方法，只有当前对象没有任何变量接收时才会触发
```



## 25.4 __call__

把对象当作函数调用时触发 __call__  意思就是把定义的函数写在call函数里 前面加self.最后在实例化对象 把对象当作函数调用 就直接把call函数里面的功能实现了

```
调用对象的魔术方法
触发时机:将对象当作函数调用时触发 对象()
参数:至少一个self接收对象，其余根据调用时参数决定
返回值：根据情况而定
作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
注意：无
```



## 25.5 __len__

__len__ 检测对象的成员属性的多少 在__len__函数下面 加num=len (self.__dict__)之后给个返回值。在下面实力话对象 之后被变量接收 result=len(对象）

```
触发时机：使用len(对象) 的时候触发
参数：一个参数self
返回值：必须是一个整型
作用：可以设置为检测对象成员个数，但是也可以进行其他任意操作
注意：返回值必须必须是整数，否则语法报错，另外该要求是格式要求。
```



## 25.6 __str__

__str__ 不加这个 正常实力话对象 打印我这个对象出来的结果是一个函数的内存地址 加上这个str  在这个函数 返回一个字符串 在打印 就出现我这个字符串！

```
触发时机:使用print(对象)或者str(对象)的时候触发
参数：一个self接收对象
返回值：必须是字符串类型
作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
注意：无
```



## 25.7 __bool__

__bool__  魔术方法 需要返回值 而且需要是布尔类型的返回值 在__bool__可以加条件  if self.什么等于已婚 return True   根据需求检测对象成员 在使用bool转换对象时候时候触发

```
触发时机: 使用bool(对象)的时候触发
参数：一个self接收对象
返回值：必须是布尔值
作用：根据实际情况决定，可以作为快捷方式使用
注意:仅适合于返回布尔值的操作
```



## 25.8 __repr__

repr

```
触发时机:在使用repr(对象)的时候触发
参数：一个self接收对象
返回值：必须是字符串
作用：将对象转使用repr化为字符串时使用，也可以用于快捷操作
```



## 25.9 __format__

__format__ 魔术方法  实力话对象 result='｛0｝去上学！' .format（） 这里可以把实力话对象传入进来 不过在format魔术方法里面 需要返回值 format魔术方法需要有个参数  这个参数 是format函数里面的 冒号后面的向左还是向右居中的参数

```
触发时机：使用字符串.format(对象)时候触发
参数：一个self接收对象，一个参数接收format的{}中的格式，例如:>5
返回值:必须是字符串
作用：设置对象可以作为format的参数，并且自定义对象格式化的规则
注意：无
```

# 26.描述符相关的魔术方法

## 1.描述符例子 第一种

~~~
#描述符1
class MSF:

    def __init__(self):
        #为描述符新建一个成员属性var用于和被管理的成员username做映射（起个外号容易管理）
        self.var = '田鸡'


    #三个操作（操作成员属性）


    #获取
    # self 描述符对象  obj 表示被管理的成员username的对象e  cls 被管理的成员username的类Email
    def __get__(self,obj,cls):
        '''
        #print('get魔术方法被触发')
        #返回任何用户名隐藏中间的文字  赵铁住 -》 赵*住   马敏 -> 马*
        if len(self.var) == 3:
            result = self.var[0]+'*'+self.var[2]
        elif len(self.var) == 2:
            result = self.var[0]+'*'
        #get中添加返回值（get的返回值就表示username的值）
        return result
        '''

        return self.var

    #设置添加
    #self 接受当前描述符对象  obj 修饰的成员属性username的对象e  value 要设置的值
    def __set__(self,obj,value):
        #print('set魔术方法被触发')

        #代替系统进行值的设置（不允许多余5个字符）
        if len(str(value)) <= obj.usernamelength:
            self.var = value
        else:
            self.var = value[:obj.usernamelength]

    #删除
    def __delete__(self,obj):
        #print('delete魔术方法被触发')

        #根据对象自身的成员属性 决定是否允许删除成员
        if obj.usernamedelete == True:
            #删除成员
            del self.var




class Email:

    #属性
    username = MSF()#将用户名成员 交给描述符对象管理
    usernamedelete = False#禁止删除用户名  标志
    usernamelength = 3
    password = '123456'

    #方法
    def login(self):
        print('登录操作')

    def logout(self):
        print('退出操作')


#实例化邮箱类
e = Email()

#获取操作
#print(e.username)


#设置操作
e.username = '大黄色嗲菠萝'
#获取操作
print(e.username)


#删除操作
#del e.username
#print(e.username)
~~~

## 2.描述符例子 第二种

~~~
#描述符 2


#邮箱类
class Email:

    #成员属性

    usernamedelete = False#True 允许删除 False 不允许
    password = '123456789'

    #成员方法
    def __init__(self):
        #描述符用于和成员属性映射的变量
        self.var = '大爷'

    def login(self):
        print('登录操作')

    def logout(self):
        print('退出操作')

    #描述符操作

    #获取操作 __get__
    def getusername(self):#函数名自定义
        '''
        #控制成获取的结果 名字中间假*
        if len(self.var) == 3:
            result = self.var[0] +'*'+ self.var[-1]
        elif len(self.var) == 2:
            result = self.var[0]+'*'
        else:
            result = self. var

        return result
        '''
        return self.var


    #设置操作 __set__
    def setusername(self,value):#函数名自定义
        #print(value)
        #进行设置操作
        if len(str(value)) <= 3:
            self.var = value
        else:
            self.var = value[:3]


    #删除操作 __delete__
    def delusername(self):#函数名自定义
        #print('删除成员属性操作被触发')
        #根据对象设置 决定是否删除成员
        if self.usernamedelete == True:
            del self.var



    #将username成员属性和描述符进行绑定的操作 相当于方法1  username = MSF()
    username = property(getusername, setusername, delusername)

#实例化邮箱对象
e = Email()

#获取成员属性
#print(e.username)

#设置成员属性
#e.username = '张石石石'
#print(e.username)

#删除成员属性
del e.username
print(e.username)
~~~

## 3.描述符例子第三种

~~~
#描述符3

#邮箱类
class Email:

    #属性
    #username = '老张'
    usernamedelete = False# True 允许删除  False 不允许删除
    password = '123456789'

    def __init__(self):
        self.var = '韩梅梅'

    #方法
    def login(self):
        print('登录操作')

    def logout(self):
        print('退出操作')

    #描述符的三个部分
    #获取操作
    @property  #声明当前函数为一个成员属性  负责获取操作
    def username(self):

        #返回数据之前进行操作
        if len(self.var) == 3:
            result = self.var[0] + '*' + self.var[-1]
        elif len(self.var) == 2:
            result = self.var[0] + '*'
        else:
            result = self.var

        return result

    #设置操作
    @username.setter
    def username(self,value):
        #print(value)

        #设置操作
        self.var = value

    #删除操作
    @username.deleter
    def username(self):
        if self.usernamedelete == True:
            #删除成员
            del self.var


#实例化对象
e = Email()

#获取对象成员
#print(e.username)

#设置对象成员
#e.username = '小龙虾'
#print(e.username)

#删除对象成员
del e.username
print(e.username)
~~~

## 4.描述符自我总结

~~~
-----第一种描述符！-------
8.描述符的作用：可以限制和控制我们对成员的属性操作  也就是给用户名或者是等等属性 加操作
比如李良 这里就需要用到描述符  在get里面对其进行把控
这段代码如下 ：
 class MSF（）：
      def __init __(self):
           self.var='李彦良'
      def __get__(self,obj,cls):
           if len(self.var)==3:
               result=self.var[0]+''+self.var[2]
           elif len(self.var)==2:
                result=self.var[0]+''
           return result 

将描述符的对象给想要控制的类的成员 例如：类里面的成员属性 username=MSF（）
然后再描述符里的类里面 加get set del进行获取修改删除等控制操作！
get 后面有三个参数  self 当前MSF对象， obj,是被管理的对象也就是被管理的实力话的对象e  cls是被管理的类 也就是Email类
get后面要给返回值 这里的返回值是被管理的值 也就是username的值  获取e.username 之后也可以通过MSF里面的init 对这个值进行修改  但是这么做返回值要return那个init里的变量

9.描述符里的set 三个参数 一个self接收当前描述符对象，一个参数是修饰成员属性就是控制的那个类的对象  还有一个是要设置的值 
对对象的值的修改进行控制 以及数量进行控制
代码如下：
def __set__(self,obj,value)
#如果修改的字符串的值的长度小于等于5
     If len(str(value))<=5:
 那么这个值就是self.var 
         self.var=value
否则就是取这个值的5个字给self.var 
     else：
         self.var=value［：：5］

9.delete 删除被管理的成员属性  要是不定义这个函数 那就是直接删除 之后确实给删了 相当于object类里的方法帮忙给删了 要是定义了这个函数 你写个Pass在函数下面 就相当于你定义这个函数把object里的函数给代替了 就删不了了 除非你在函数下面写上你要删除的成员属性 这里的成员属性还是通过描述符来控制的成员属性！
这里的对象是e  根据对象自带的某些成员来决定其  ，对象自带的这个成员是否可以进行删除？ 意思就是可以通过这个自带的成员加上是否可以删除的条件  来在描述符里写 如果这个对象 让删 那么我们就删 代码如下：
def delete (self,obj)
if obj.username ==True:
    del self.var 

-----第二种描述符------
class Email：
  password=123455
def __init __(self):
    # 管理的名字 用来映射 就是操作前后做对比
     self.var='李大妈'
def getusername  (self):
   控制成获取的结果 
         return self.var
   
def setusername (self):

def deleteusername(self):


username=property（getusername，setusername,deleteusername)



-----第三种描述符-------

和第二种差不多 就是在函数名上面做事情
@property 获取操作
def username(self)

@username.setter设置操作
def username(self)


@username.deleter 删除操作
def username(self)



总结：第一种，就是拿描述符的对象去关联 你想控制的类的成员 第二种和第三种更专注于在一个类里操作


~~~



#### 26.1.__get__()

```
触发时机：在获取指定描述符操作的成员属性的值的时候触发
参数：1描述符对象本身，2描述符描述的属性所在的对象，描述符描述的对象的类
返回值：必须有，不然无法获取相应属性值
注意：仅在描述符中使用
```

#### 26.2.__set__()

```
触发时机：在设置或者添加指定描述符操作的成员属性的时候触发
参数：1描述符对象本身，2描述符描述的属性所在的对象,3要设置的值
返回值：无
注意：仅在描述符中使用
```

#### 26.3.__delete__()

```
触发时机：在删除指定描述符操作的成员属性的时候触发
参数：1描述符对象本身，2描述符描述的属性所在的对象
返回值：无
注意：仅在描述符中使用
```

# 27.与属性相关的魔术方法

#### 27.1.__getattr__()

```
触发时机：获取不存在的对象成员时触发
参数：1接收当前对象的self，一个是获取成员名称的字符串
返回值：必须有值
作用:为访问不存在的属性设置值
注意：getattribute无论何时都会在getattr之前触发，触发了getattribute就不会在触发getattr了
```

#### 27.2.__setattr__（）

```
触发时机:设置对象成员值的时候触发
参数:1个当前对象的self,一个是要设置的成员名称字符串,一个是要设置的值
返回值:无 过程操作
作用:接管设置操作,可以在设置前之前进行判断验证等行为
注意:在当前方法中无法使用成员=值的方式直接设置成员，否则会无限递归，必须借助object的设置方法来完成

object.__setattr__（参数1，参数2，参数3）
```

#### 27.3__delattr__（）

```
触发时机：删除对象成员时触发
参数：一个当前对象的self
返回值：无
作用:可以在删除成员时进行验证。
```

#### 27.4__getattribute__（）

```
触发时机：使用对象成员时触发，无论成员是否存在
参数：1个接收当前对象self，一个是获取的成员的名称字符串
返回值：必须有
作用：在具有封装操作（私有化时），为程序开部分访问权限使用
```

```
ex:#与属性相关的魔术方法


class CangYing:
    #属性
    sex = '雌性'
    age = 0.1
    name = '绿豆蝇'


    #方法
    def __init__(self):
        #为对象添加一个成员 方便测试delattr方法
        self.color = 'green'


    def fly(self):
        print('嗡嗡翁～～～')

    def clear(self):
        print('擦擦手～～～')

    #
    '''
    触发时机：访问不存在的对象成员属性的时候触发
    功能：设定不存在成员被访问的结果
    参数：一个self接受对象，一个参数接受不存在的成员属性名称
    返回值：可有可无，推荐写返回值
    
    def __getattr__(self,attrname):
        print('getattr被触发')

        #逻辑判断
        if attrname == 'bf':
            return '红蝇'
        elif attrname == 'baba':
            return '大绿豆蝇'
        else:
            return '对不起不存在该成员！'
    '''

    #__getattribute__魔术方法
    '''
    触发时机：访问对象成员时触发，优先与getattr被触发！
    功能：设置成员访问的值，也可以限制访问
    参数：属性名称
    返回值：可有可无
    
    
    def __getattribute__(self, attrname):
        #print('被触发__getattribute__')
        #内部不可以出现任何对象.成员的操作 会触发递归操作！
        if attrname == 'age':
            return '隐私，不告诉你！'
        elif attrname == 'sex':
            return '雌性'
        elif attrname == 'name':
            #借助object的获取成员的操作
            return object.__getattribute__(self,attrname)

    '''

    '''
    触发时机：设置对象成员属性时候触发
    功能：控制成员属性设置操作
    参数：一个self接受对象  一个接受属性名 一个接受属性的值
    返回值：无
    
    '''

    def __setattr__(self,attrname,attrvalue):
        #print(a,b)
        #设定除了性别，其余都可以修改
        if attrname == 'sex':
            pass
        else:
            object.__setattr__(self,attrname,attrvalue)



    #delattr魔术方法
    '''
    触发时机：删除对象成员时候触发
    功能：用于控制成员删除的操作
    参数：一个self接受对象 一个用于接受要删除属性名称
    返回值：无
    
    '''

    def __delattr__(self,attrname):
        #print(attrname)
        #限制某个属性是否允许被删除
        if attrname == 'color':
            pass
        else:
            object.__delattr__(self,attrname)




#实例化对象
ldy = CangYing()

#访问成员属性
#print(ldy.sex)
#print(ldy.age)
#print(ldy.name)

#访问不存在的成员属性
#print(ldy.bf)
#print(ldy.baba)
#print(ldy.mama)

#设置对象成员
#ldy.sex = '雄性'
#print(ldy.sex)
#ldy.age = 25
#print(ldy.age)

#删除对象成员
del ldy.color
print(ldy.color)

#del ldy.sex
#print(ldy.sex)

```



# 28.类和对象的常用函数

#### 28.1.issubclass()

```
检测一个类是否是另外一个类的子类

格式1：issubclass(被检测类，父类)
返回值：布尔值

格式1：issubclass(被检测类，(父类1,父类2，父类3...))
返回值：布尔值

注意：只要有一个类是当前被检测类的父类，那么最终结果就是True

ex:
#issubclass() 检测一个类是否是另外一个类的子类

class Father:
    pass

class Mother:
    pass

class Son(Father,Mother):
    pass

#单个类的检测
#result = issubclass(Son,Father)
#print(result)

#多个类的检测
result = issubclass(Son,(Father,Mother))
print(result)
```

#### 28.2.isinstance()

```
检测一个对象是否是某个类的对象

格式1：isinstance(对象,类)
返回值：布尔值

格式2：isinstance(对象,（类1，类2，类3...）)
返回值：布尔值

注意：只要一个类是当前对象的类，那么最终结果就是True

ex:
class JianPeng:
    pass

jp = JianPeng()

#单个类的检测
result = isinstance(jp,JianPeng)
print(result)

#多个类的检测
result = isinstance(jp,(JianPeng,Father))
print(result)
```

#### 28.3.hasattr()

```
检测对象/类是否具有某个成员

格式：hasattr（对象/类,'成员名'）
返回值：布尔值
```

#### 28.4.getattr()

```
获取对象/类中的成员值

格式：getattr(对象,'成员名'[,成员不存在时的默认值])
返回值：成员的值
```

#### 28.5.setattr()

```
设置或者添加对象/类中的成员

格式：setattr(对象,'成员名',值)
返回值：None
```

#### 28.6delattr()

```
删除对象/类中的成员

格式： delattr(对象,成员)
返回值:None

以上这四个的例子: 
   hesattr() getattr() setattr() delattr()
class Human:
    #属性
    name = '剑朋'
    sex = 'unknow'
    age = 18

    #方法
    def la(self):
        print('有史以来la的最好的人')

    def chi(self):
        print('有shi以来吃的最快的人')

#实例化对象
jp = Human()

#hasattr()
result = hasattr(jp,'petname')
print(result)

#getattr()
result = getattr(jp,'name','yellow') #相当于jp.age
print(result)

#setattr()
setattr(jp,'color','black') #相当于  jp.color = 'black'
print(jp.color)

#delattr()
delattr(jp,'color')#del jp.color
print(jp.__dict__)

```



##### 28.1.类的内置属性 __dict__  

```
#类的内置属性
#__dict__  获取类或者对象的所属成员

class Father:
    pass

class YaoJie(Father,object):
    '''
    这里就是类的文档，
    您来向干啥就写啥！
    '''
    #属性
    name = '瑶瑶'
    age = 18
    sex = '女'


    #方法
    def __init__(self):
        self.color = 'yellow'
        self.bf = '吴彦祖'
        self.gf = '张正阳'

    def study(self):
        print('好好学习，天天想上')

    def eat(self):
        print('吃甘蔗～')

    def drink(self):
        print('喝牛奶')

#实例化对象
yj = YaoJie()

#检测类的成员
print(YaoJie.__dict__)

#检测对象成员
print(yj.__dict__)

#查看类文档
print(YaoJie.__doc__)
help(YaoJie)

#表示类的名称
print(YaoJie.__name__)
print(__name__)#值为__main__，表示运行的就是当前文件

#__bases__ 获取类的继承列表
print(YaoJie.__bases__)
```

# 29.装饰器

```
#装饰器  增加函数的功能

#1.声明一个普通函数

def niao():
    print('嘘嘘嘘嘘～～～～～')

#调用函数
niao()
niao()


#2.对函数进行功能的增加

#用于增功能的函数
def adorn(func):
    #1.扩展功能1
    print('尿前洗洗手')
    #调用niao的函数
    func()
    print('尿后抖一抖')



#niao函数
def niao():
    print('嘘嘘嘘嘘～～～～～')

niao = adorn(niao)

#调用函数
niao()
niao()

#3.对于第二部语法的概念

def adorn(func):
    #1.扩展功能1
    def   inner():
    print('尿前洗洗手')
    #调用niao的函数
    func()
    print('尿后抖一抖')
    return   inner

#niao函数
@adorn  #相当于niao = adorn(niao)
def niao():
    print('嘘嘘嘘嘘～～～～～')

#调用函数
niao()
niao()


#4.让我们的装饰器变成真的装饰器

def adorn(func):#func是形参 用于接受传入的实参niao函数
    #函数inner（就是未来的装饰之后的niao函数)
    def inner():
        # 1.扩展功能1
        print('尿前洗洗手')
        # 调用niao的函数
        func()
        # 2.扩展功能2
        print('尿后抖一抖')

    return inner

#niao函数
@adorn  #相当于niao = adorn(niao)
def niao():
    print('嘘嘘嘘嘘～～～～～')

#调用函数
niao()
niao()


#5.为具有参数和返回值的函数进行装饰操作

#添加了返回值
#用于装饰的函数
def adorn(func):
    #定义内部函数 inner  用来作为未来的尿函数
    def inner():
        #扩展功能1
        print('尿前洗洗手')
        #调用原有尿函数
        result = func()
        #扩展功能2
        print('尿后抖一抖')

        #为函数添加返回值（相当于niao函数的返回值）
        return result

    #返回值  必须是函数  扩展之后的niao函数
    return inner

#定义函数
@adorn # niao = adorn(niao)
def niao():
    print('嘘嘘嘘嘘～～')
    return '一碗尿结石'

#调用函数
result1 = niao()
print(result1)
result2 = niao()
print(result2)



#添加参数
#用于装饰的函数
def adorn(func):
    #定义内部函数 inner  用来作为未来的尿函数
    def inner(w,t):
        #扩展功能1
        print('尿前洗洗手')
        #调用原有尿函数
        func(w,t)
        #扩展功能2
        print('尿后抖一抖')



    #返回值  必须是函数  扩展之后的niao函数
    return inner

#定义函数
@adorn # niao = adorn(niao)
def niao(who,times):
    print(who,'在女厕所尿了',times,'分钟')
    print('嘘嘘嘘嘘～～')


#调用函数
niao('老郭',10)
niao('老田',15)



#6.收集参数装饰器

#装饰器函数
def adorn(func):
    #定义内部函数 作为未来的尿
    def inner(*w,**t):
        #功能扩展1
        print('尿前站一排')
        #调用niao函数
        func(*w,**t)
        #扩展功能2
        print('尿后甩一甩')

    return inner

#定义尿函数
@adorn
def niao(*who,**times):
    print('参与撒尿的人分别有：',who)
    print('每人分别撒尿时间为:',times)
    print('嘘嘘嘘嘘嘘嘘`~~')

#调用函数
niao('戎宇','张东伟','胡明瑞','吴琦',ry = '10mins',zdw = '60mins',hmr = '1s',wq = '1mins')


#7.为装饰器添加参数

#装饰器函数
def adorn(arg):#arg用于接受装饰器自身传入的参数
    def _adorn(func):#func用于接受需要修饰的函数
        #声明内部函数
        def inner():
            #扩展功能1(判断给尿还是拉添加功能)
            if arg == '尿':
                print('尿前洗洗手')
            elif arg == '拉':
                print('拉前搓搓纸')

            #调用基本函数
            func()

            #扩展功能2
            if arg == '尿':
                print('尿后抖一抖')
            elif arg == '拉':
                print('拉后蹭蹭屎')

        return inner

    #返回内部函数
    return _adorn


#基本函数1
@adorn('尿') #@  +  adorn('尿') -> @_adorn  代表最基本的装饰器函数
def niao():
    print('嘘嘘～')

#基本函数2
@adorn('拉')
def la():
    print('噗哧～')

#调用niao函数
niao()

#调用la函数
la()


#8.使用类作为装饰器的参数

#便便类
class BianBian:
    #属性
    #方法
    def before():
        print('尿前洗洗手')

    def after():
        print('尿后抖一抖')

#装饰器函数

def adorn(arg):
    def _adorn(func):
        def inner():
            #功能扩展1
            arg.before()
            #调用基本函数
            func()
            #功能扩展2
            arg.after()

        return inner

    return _adorn

#基本函数定义
@adorn(BianBian)
def niao():
    print('嘘嘘虚～～～')


#调用函数
niao()




#9.将类作为装饰器使用

#声明装饰器类
class Adorn:

    #接受装饰器参数的方法
    def __init__(self,arg):#相当于adorn
        #print(arg)
        pass

    #用于接受传入函数的方法
    def __call__(self,func):# 相当于_adorn
        #print(func)
        #将接受到的函数存入对象
        self.func = func
        #返回结果作为未来的尿函数
        return self.inner

    #将定义的未来的函数在这里写
    def inner(self):
        # 扩展功能1
        print('尿前洗洗手')
        # 调用基本函数
        self.func()
        # 扩展功能2
        print('尿后抖一抖')

#基本函数
@Adorn('尿')  # niao = Adorn对象(niao)
def niao():
    print('嘘嘘～～～')


#调用函数
niao()



#10：为类添加装饰器


#装饰器函数
def adorn(cls):

    def inner():
        #扩展功能1
        print('准备好一桶水，和一袋水泥')
        #调用类
        obj = cls()
        #扩展功能2
        print('给紫薇涂上颜色！')
        #返回对象
        return obj


    #返回结果
    return inner

#被装饰的类
@adorn
class ZiWei:

    #属性
    name = '紫薇'
    sex = '女'
    age = 24

    #方法
    def eat(self):
        print('吃葡萄')

    def drink(self):
        print('喝葡萄汁')

#实例化对象
zw = ZiWei()
print(zw)



#11.多层装饰器嵌套

#装饰器1
def adorn1(func):
    def inner():
        #扩展功能1
        print('推开厕所门')
        #基本函数
        func()
        #扩展功能2
        print('关上厕所门')

    return inner


#装饰器2
def adorn2(func):
    def inner():
        # 扩展功能1
        print('尿前洗洗手')
        # 基本函数
        func()
        # 扩展功能2
        print('尿后抖一抖')

    return inner


#基本函数
@adorn1  #多层装饰器是丛下到上追个装饰
@adorn2
def niao():
    print('嘘嘘～～～')

#调用函数
niao()
```

# 30.抽象类

```
具有抽象方法的类就是抽象类。

抽象方法就是没有完成的方法。只有方法名称和参数，没有方法内容的方法。

作用：适合于领导指定开发规范及多人协作完成类。

abc abstract class 抽象类的缩写
```



## 30.1方法的分类

#### 30.1.1非绑定类 绑定类 类方法 静态

```
#方法的分类
class Car:
    name='奥迪'
    logo='0000'
    color='red'
    #方法的种类
    #非绑定方法(对象方法)
    def turnright(self):
        print('方向盘右打死，向右转')
    #绑定类方法
    def turnleft():
        print('方向盘左打死,向左转')
     #类方法(会将类作为第一个参数传入)
    @classmethod
    def  goon(cls):
        print(cls)
        print('方向盘前打死,向前走')
    #静态方法(什么类和对象都不传入,可通过类和对象调用)
    @staticmethod
    def  goback():
        print('方向盘后打死,向后走')
#实例化对象
c=Car()
#非绑定类的方法,通过对象来调用,如果是通过类来调用,类里面要加参数!
Car.turnright(1)
c.turnright()

#绑定类的方法,只能用类来调用
Car.turnleft()

#类方法(会将类的第一个参数传入) 类和对象都能调用!
Car.goon()
c.goon()

#静态方法  类和对象都能调用
Car.goback()
c.goback()

```



#### 30.1.2抽象类

```
1.抽象类中可以包含具体的方法也可以包含抽象方法
2.抽象类中可以包含成员属性,而且属性没有抽象不抽象之分
3.抽象类无法实例化使用.
4.抽象类只能被其他类继承使用，（唯一的用法）
5.只有子类实现了抽象类的所有抽象方法之后，该子类才可以正常实例化使用。有一个抽象方法没有实现都不可以实例化
6.抽象类的作用是指定程序开发的标准（方法名，参数等）
```

```
#抽象类
#具有抽象的方法就是抽象类
#抽象方法
#没有方法体(方法的内容)就是抽象方法
import  abc #abstract  class
class  FeiJi(metaclass=abc.ABCMeta):# 元类
    name='和谐号'
    color='粉色'
    age='20years'
    #成员方法
    #绑定类的方法
    @abc.abstractmethod
    def fei():
        pass
    #非绑定类的方法/对象方法
    @abc.abstractmethod
    def luodi(self):
        pass
    #类方法 类方法(会将类作为第一个参数传入) 就是下面的cls
    @abc.abstractclassmethod
    def jiayou(cls):
        pass
    #静态方法
    #静态方法(什么类和对象都不传入，可以通过类和对象调用)
    @abc.abstractstaticmethod
    def  zhisheng():
        pass
#实例化对象(抽象类无法实例化)
#抽象类的作用 制定开发规范  用于协同开发

```

#### 30.1.3用户操作类

```
#用户操作类
'''
组长：老丛
组员1：婶婶
组员2：文静
组员3：竹琪
组员4：丽丽

类的内容：
    添加用户
    修改用户
    删除用户
    查找用户
    冻结用户


'''

#使用抽象类来完成（老丛来制定的抽象类）
import abc

class User(metaclass = abc.ABCMeta):

    #添加用户(老丛)
    def add(self):
        print('老丛的添加用户操作')

    #修改用户(婶婶)
    @abc.abstractmethod
    def modi(newname):
        pass

    #删除用户(文静)
    @abc.abstractclassmethod
    def dele(cls):
        pass

    #查找用户(竹琪)
    @abc.abstractstaticmethod
    def find():
        pass
    #冻结用户(丽丽)
    @abc.abstractmethod
    def frozen(self):
        pass


#声明一个婶婶的用户类继承抽象类
class SSUser(User):
    # 修改用户(婶婶)
    def modi(newname):
        print('婶婶的修改用户操作')


#声明一个文静类继承婶婶的用户类
class WJUser(SSUser):
    # 删除用户(文静)
    @classmethod
    def dele(cls):
        print('文静的删除用户操作')


#声明一个竹琪类集成文静的类
class ZQUser(WJUser):
    # 查找用户(竹琪)
    @staticmethod
    def find():
        print('竹琪的查赵用户操作')


#声明一个丽丽的类 继承竹琪的类
class LLUser(ZQUser):
    # 冻结用户(丽丽)
    def frozen(self):
        print('丽丽的冻结用户操作')


#到丽丽类位置 所有抽象方法都实现了，可以使用最后一个类
u = LLUser()
u.add()
LLUser.modi('老大')
u.find()
LLUser.dele()
u.frozen()
```



#### 30.1.4  多态

```
多态，多种状态！就是一个类，根据不同的情况，相同的方法产生不同的结果。
```

```
ex:
#多态

#抽象类 定义动物的行为规范
import abc
class Animal(metaclass = abc.ABCMeta):

    #撒尿  对象抽象方法
    @abc.abstractmethod
    def saniao(self):
        pass

    #拉屎  对象抽象方法
    @abc.abstractmethod
    def lashi(self):
        pass

    #吹口哨  对象抽象方法
    @abc.abstractmethod
    def chuikoushao(self):
        pass


#实现三个类  猫狗鸡

class Cat(Animal):
    # 撒尿
    def saniao(self):
        print('蹲着撒尿')

    # 拉屎
    def lashi(self):
        print('蹲着拉屎')

    # 吹口哨
    def chuikoushao(self):
        print('喵喵～～')



#狗类
class Dog(Animal):
    # 撒尿
    def saniao(self):
        print('抬起后退')

    # 拉屎
    def lashi(self):
        print('蹲着拉屎')

    # 吹口哨
    def chuikoushao(self):
        print('汪汪～')


#鸡类
class Chick(Animal):
    # 撒尿
    def saniao(self):
        print('站着撒尿')

    # 拉屎
    def lashi(self):
        print('站着拉屎')

    # 吹口哨
    def chuikoushao(self):
        print('大爷老玩啊～')


#实例化三个对象
#小狗
xiaohei = Dog()
#小猫
mimi = Cat()
#小鸡
xiaohua = Chick()



#定义行为类
class Action:
    #定义成员属性  存储动物
    def __init__(self,obj):
        self.animal = obj

    # 撒尿
    def saniao(self):
        self.animal.saniao()

    # 拉屎
    def lashi(self):
        self.animal.lashi()

    # 吹口哨
    def chuikoushao(self):
        self.animal.chuikoushao()




#实例化行为类对象(状态1  猫)

action = Action(mimi)

#调用行为类的操作
action.saniao()
action.lashi()
action.chuikoushao()

#实例化行为类对象 （状态2 狗）

action = Action(xiaohei)

#调用行为类的操作
action.saniao()
action.lashi()
action.chuikoushao()

#实例化行为类对象(状态3 鸡)

action = Action(xiaohua)

#调用行为类的操作
action.saniao()
action.lashi()
action.chuikoushao()
```

# 31.导入模块和包

## 31..模块的导入

### 31.1  方法一:import 导入

```
ex:
#导入py05模块
'''
#导入模块方法1
import py05

#调用变量
print(py05.leader)

#调用函数
py05.havebaby()

#调用类中成员
print(py05.MakeBaby.wife)
print(py05.MakeBaby.husband)

py05.MakeBaby.tuidao()
py05.MakeBaby.setbed()

```

### 31.2 方法二:别名

```
import py05 as p

#调用变量
print(p.leader)

#调用函数
p.havebaby()

#调用类中成员
print(p.MakeBaby.wife)
print(p.MakeBaby.husband)

p.MakeBaby.tuidao()
p.MakeBaby.setbed()
```

### 31.3 方法三: 按需导入

```
#导入模块方法3（按需导入1）  只能使用到导入的内容
from py05 import havebaby

#调用havababy函数
havebaby()


##导入模块方法4（按需导入2）  只能使用到导入的内容

from py05 import havebaby,leader

#调用havababy函数
havebaby()

#调用leader变量
print(leader)
```

### 31.4 方法四:按需导入

```
#导入模块方法5（按需导入3）
from py05 import *

#调用havababy函数
havebaby()

#调用leader变量
print(leader)

#调用类中内容
print(MakeBaby.wife)
print(MakeBaby.husband)

MakeBaby.clearclosth()
MakeBaby.setbed()
```

## 31..包的导入

### 31.1 方法一: 导入包(中的模块)

```
import lv.dog

#使用dog模块中的内容
print(lv.dog.name)
lv.dog.jiao()
lv.dog.ChiShi.wenwen()

```

### 31.2 方法二: as 语法

```
#导入包(中的模块)
import lv.cat as c

#使用cat模块中的内容
c.jiao()
print(c.name)
c.Chiyu.kankan()
```



### 31.3方法三: from import 语法

```
from lv.fish import name,piao

print(name)
piao()
```



### 31.4 方法四: from import 语法

```
from lv.human.man import *

print(sex)
print(hobby)

kiss()
LiaoMei.ll()
```

### 31.5 直接导入包

```
#直接导入包
import gucci

#使用init文件中的内容

#访问变量
print(gucci.pinpai)

#访问函数
gucci.sell()

#类调用
print(gucci.Glass.color)
gucci.Glass.zhuangb()

```

### 31.6 通过包一次导入多个模块

```
from anima import * #丛anima包中导入所有定义的模块

#使用老王模块
print(laowang.name)

#老王模块的函数
laowang.maiduiyou()


#使用伟哥模块
print(weige.face)
print(weige.heart)
weige.thief()


#尝试使taoge模块
print(taoge.sex)
taoge.play()

```



### 31.7书写模块内容  测试代码

```
#书写模块内容
'''
如果当前模块用于多次复用，推荐书写一下内容

1.变量
2.函数
3.类
4.测试代码

'''

#变量
leader = '代大'

#函数
def havebaby():
    print('噔谁谁怀孕！')


#类
class MakeBaby:

    #属性
    husband = '隔壁老王'
    wife = '潘金莲'

    #方法

    def tuidao():
        print('推到媳妇')

    def setbed():
        print('放到床上')

    def clearclosth():
        print('把媳妇脱光光～')



#测试代码
if __name__ == '__main__':
    print(__name__)
    print('---------以后内容为测试代码---------')
    print(leader)
    havebaby()
```

# 32.异常

## 32.1 异常的解释

```
异常是指在语法正确的前提下，程序的报错就是异常。

它是在程序异常时单独存在的一个对象，可以对其进行获取或其他操作
```

#### 32.1.1异常的分类

```
AssertError               断言语句（assert）失败
AttributeError            尝试访问未知的对象属性
EOFError                  用户输入文件末尾标志EOF（Ctrl+d）
FloatingPointError        浮点计算错误
GeneratorExit             generator.close()方法被调用的时候
ImportError               导入模块失败的时候
IndexError                索引超出序列的范围
KeyError                  字典中查找一个不存在的关键字
KeyboardInterrupt         用户输入中断键（Ctrl+c）
MemoryError               内存溢出（可通过删除对象释放内存）
NameError                 尝试访问一个不存在的变量
NotImplementedError       尚未实现的方法
OSError                   操作系统产生的异常（例如打开一个不存在的文件）
OverflowError             数值运算超出最大限制
ReferenceError            弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
RuntimeError              一般的运行时错误
StopIteration             迭代器没有更多的值
SyntaxError               Python的语法错误
IndentationError          缩进错误
TabError                  Tab和空格混合使用
SystemError               Python编译器系统错误
SystemExit                Python编译器进程被关闭
TypeError                 不同类型间的无效操作
UnboundLocalError         访问一个未初始化的本地变量（NameError的子类）
UnicodeError              Unicode相关的错误（ValueError的子类）
UnicodeEncodeError        Unicode编码时的错误（UnicodeError的子类）
UnicodeDecodeError        Unicode解码时的错误（UnicodeError的子类）
UnicodeTranslateError     Unicode转换时的错误（UnicodeError的子类）
ValueError                传入无效的参数
ZeroDivisionError         除数为零
```

#### 32.1.2常见的错误操作

```
IndexError 索引错误

lists = [1,3,6]
print(lists[3])
KeyError 键不存在

dicts = {'gp':'高坡','cr':'曹睿','tw':'唐伟'}
print(dicts['zj'])
nameError 变量不存在

print(ch)
AssertError 断言错误

assert 1>0
assert 3>5
IndentationError缩进错误

def myfunc():
    print('眼残')
   print('眼残')
```

####32.1.3 错误异常处理:  try...except语法

```
# try...except语法   属于流程控制分支的一种

#try尝试
try:
    #尝试执行代码的取余
    #lists = ['绿茶','红茶','乌龙茶','菊花茶']
    #访问一个不存在的索引
    #print(lists[10])


    dicts = {'baba':'小头','mama':'围裙','shushu':'老王','婶婶':'紫薇'}
    #访问一个不存在的键
    print(dicts['mama2'])

except IndexError:#只能接受索引错误
    print('索引错误')


except KeyError:#只能接受键出现的错误
    print('键出现错误！')

#接受错误的区域
except:#except区域接受任何的异常！
    print('程序出现了错误')

#没有异常出现时候执行的区域
else:
    print('恭喜，没有任何错误出现！')

#最终区域，无论有没有错误都会被执行的取余
finally:
    print('报告老板，程序执行完毕')
    
    
#try  except。。


try:
    #每次产生的错误都是一个类中的对象
    print(result)

except NameError as error:
    print('变量没有定义')
    print(type(error))
    print(error)
   
   
#异常的解决方案

try:

    lists = ['百岁山','康师傅','昆仑山','恒大山泉']
    print(lists[99])

except IndexError:
    #解决错误！
    print(lists[-1])
```

#### 32.4 自定义错误类型

```
#自定义错误类型

'''
odd 奇数
even 偶数

'''
#自定义错误（逻辑错误）
class OddError(RuntimeError):
    #init魔术方法添加记录错误信息的成员
    def __init__(self,errmsg,errcode,errexp):
        #错误介绍
        self.errmsg = errmsg
        #错误代码
        self.errcode = errcode
        #错误解释
        self.errexp = errexp


    #自定义错误对象的输出
    def __str__(self):
        #自己组合错误信息
        return '错误信息为：'+self.errmsg+'\n'+'错误代码为：'+str(self.errcode)+'\n'+'错误解释为：'+self.errexp



#try。。except语法

try:
    no1 = 100
    no2 = 20
    result =  no1 / no2

    #判断结果是否是计数
    if result % 2 == 1:
        #将错误抛出 给except块接受
        raise OddError('运算结果为计奇数',1,'由于我不高兴，结果不要奇数！')


except OddError as error:
    print('奇数错误')
    print(error)
```

#### 32.5 with语法操作

```
#文件操作的with语法

'''
#1.打开文件
fp = open('06.txt','w')

#2.读取或者写入文件
fp.write('哥也是皇族后裔～')

#3.关闭文件
fp.close()
'''


try:
    #1.打开文件（with起到监视文件的作用）  3.with 自动关闭文件
    with open('06.txt', 'r') as fp:#相当于  fp = open('06.txt', 'r')
        #2.读取文件
        txt = fp.read()
        print(txt)

except:
    print('文件操失败')
```

# -------------------------------------------

# 1 . HTML前端

前端开发系统化学习教程，包括HTML、CSS、JavaScript、jQuery、js特效制作、ajax前后台交互等。以及前端框架 Bootstarp.快速搭建响应式页面



## 1.1HTML概述和基本结构

### 1.1.1 HTML是什么?

 HTML是 HyperText Mark-up Language 的首字母简写，意思是超文本标记语言，

  超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个的标签组成，

  用这种语言制作的文件保存的是一个文本文件，文件的扩展名为html或者htm，

  一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方式编辑它，

  如果用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。



### 1.1.2 HTML是由：标签和内容构成

<title>这是文档中的标题</title>

**HTML基本结构**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>网页标题</title>
</head>
<body>
    网页显示内容
</body>
</html>

```

### 1.1.3 html文档规范

xhtml制定了文档的编写规范，html5可部分遵守，也可全部遵守，看开发要求。

1、所有的标签必须小写

2、所有的属性必须用双引号括起来

3、所有标签必须闭合

4、img必须要加alt属性(对图片的描述)



### 1.1.4 html注释：

tml文档代码中可以插入注释，注释是对代码的说明和解释，注释的内容不会显示在页面上，html代码中插入注释的方法是：

```
<!-- 这是一段注释  -->
```



## 1.2 HTML中Head头

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>网页标题</title>
</head>
<body>
    网页显示内容
</body>
</html>

```

HEAD标签里面负责对网页进行一些设置以及定义标题，

设置包括定义网页的编码格式，外链css样式文件和javascript文件等，

设置的内容不会显示在网页上，标题的内容会显示在标题栏

```
设置网页编码：<meta charset="utf-8"/>
关键字：<meta name="Keywords" content="关键字" />
描述：  <meta name="Description" content="简介、描述" />
网页标题：<title>本网页标题</title>
导入CSS文件：<link type="text/css" rel="stylesheet" href="**.css"/>
CSS代码：<style type="text/css">嵌入css样式代码</style>
JS文件或代码： <script >。。。</script>
```



## 1.3 HTML标题

通过 <h1>、<h2>、<h3>、<h4>、<h5>、<h6>,标签可以在网页上定义6种级别的标题。

6种级别的标题表示文档的6级目录层级关系，比如说： <h1>用作主标题（最重要的），其后是 <h2>（次重要的），

再其次是 <h3>，以此类推。搜索引擎会使用标题将网页的结构和内容编制索引，所以网页上使用标题是很重要的。

```
<h1>这是一级标题</h1>
<h2>这是二级标题</h2>
<h3>这是三级标题</h3>
```



## 1.4 HTML段落,换行,字符实体

### 1.4.1 html段落 

<p>标签定义一个文本段落，一个段落含有默认的上下间距，段落之间会用这种默认间距隔开，代码如下:

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>段落</title>
</head>
<body>
    <p>HTML是 HyperText Mark-up Language 的首字母简写，意思是超文本标记语言，超
    文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个的
    标签组成，用这种语言制作的文件保存的是一个文本文件，文件的扩展名为html或者htm。
    </p>

    <p>一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方
    式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网
    页可以从一个网页链接跳转到另外一个网页。</p>
</body>
</html>
```

### 1.4.2 html换行 

```
<p>
一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用<br />
文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件<br />
渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。
</p>
```

### 1.4.3 html字符实体 

```
<!--  在段落前想缩进两个文字的空格，使用空格的字符实体：&nbsp;   -->
<p>
    &nbsp;&nbsp;一个html文件就是一个网页，html文件用编辑器打开显示的是文本，可以用<br />
    文本的方式编辑它，如果用浏览器打开，浏览器会按照标签描述内容将文件<br />
    渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。
</p>

<!-- “<” 和 “>” 的字符实体为 &lt; 和 &gt;  -->
<p>
    3 &lt; 5 <br>
    10 &gt; 5
</p>
```



## 1.5 HTML块,含样式的标签

### 1.5.1 html块

1. div标签 块元素，表示一块内容，没有具体的语义。
2. span标签 行内元素，表示一行中的一小段内容，没有具体的语义。

### 1.5.2 含样式和语义的标签

1. em标签 行内元素，表示语气中的强调词

2. i标签 行内元素，原本没有语义，w3c强加了语义，表示专业词汇

3. b标签 行内元素，原本没有语义，w3c强加了语义，表示文档中的关键字或者产品名

4. strong标签 行内元素，表示非常重要的内容

5. del 删除线

   ```
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<title>块元素和行内元素</title>
   </head>
   <body>
   	<div>iloveyou1</div>
   	<div>iloveyou2</div>
   	<span>imissyou1abcabc</span>
   	<span>imissyou2</span>
   	<div>iloveyou1</div>

   	<hr>

   	这很<em>强调</em>哦
   	这很<i>专业</i>哦
   	这很<b>关键</b>哦
   	这很<strong>非常重要</strong>哦
   	原价<del>100</del>,现价66

   	<hr>

   	<h2>块元素</h2>
   	<p>one</p>
   	<p>one</p>
   	<p>one</p>
   	<div>div1</div>
   	<div>div2</div>
   	<!-- h1  h6 -->
   	
   	<h2>行内元素</h2>
   	<em></em>
   	<i></i>
   	<b></b>
   	<span></span>
   </body>
   </html>
   ```

### 1.5.3 语义化的标签

语义化的标签，就是在布局的时候多使用语义化的标签，搜索引擎在爬网的时候能认识这些标签，理解文档的结构，方便网站的收录。比如：h1标签是表示标题，p标签是表示段落，ul、li标签是表示列表，a标签表示链接，dl、dt、dd表示定义列表等，语义化的标签不多。

## 1.6 HTML图片

### 1.6.1 html图片

<img>标签可以在网页上插入一张图片，它是独立使用的标签，通过“src”属性定义图片的地址，通过“alt”属性定义图片加载失败时显示的文字，以及对搜索引擎和盲人读屏软件的支持

```
<img src="images/pic.jpg" alt="产品图片" />
```

### 1.6.2  绝对路径和相对路径

img标签  单标签
属性:
src 必须属性 写明当前加载的图片的位置(路径)
alt: 通过“alt”属性定义图片加载失败时显示的文字，以及对搜索引擎和盲人读屏软件的支持。
title: 鼠标放到图片上时 展示的一个说明

路径:
相对路径  相对于当前你打开的这个html文件目录
images/1.jpg  当前目录下images目录下的1.jpg文件
./images/1.jpg  当前目录下
../images/2.jpg  上一级目录下   
绝对路径
/images/1.jpg  在windows下指的是盘符目录 C:
/images/1.jpg  在有http服务器的环境下/根  指的是你网站域名或ip地址指向的位置

```
<img src="../images/1.jpg" alt="这是一个美眉" title="这个图片很好看">
```

## 1.7 HTML链接

### 1.7.1 <a>标签

<a>标签可以在网页上定义一个链接地址，通过href属性定义跳转的地址，通过title属性定义鼠标悬停时弹出的提示文字框。

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>a链接</title>
</head>
<body>
	<a href="./3.html">跳转到3.html</a>
	<a href="http://www.baidu.com" title="接下来要跳转" target="_blank">跳转到百度</a>
	<a href="">跳转到百度</a>
	<a href="./2.html" title="" target="">abc</a>

	<!-- a链接在跳转页面的同时 可以携带 参数 a="abc" b="ccc" id="12" 
		在url地址 后面 ?携带参数  多个参数之间 用&分割

	-->
	<a href="2.html?a=abc&b=ccc&id=12">携带参数 跳转到2.html页面</a>

</body>
</html>
```

### 1.7.2 锚点:定义页面内滚动跳转

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>锚点</title>
	<style type="text/css">
		/*div{} 选择页面中所以得div标签*/
		div{
			/*设置高度*/
			height: 500px;
			/*设置边框*/
			border:1px solid red;
		}
	</style>
</head>
<body>
	<!-- web 网站 -->
	<a href="#one">one</a>
	<br>
	<a href="#two">two</a>
	<br>
	<a href="#three">three</a>
	<br>
	<a href="#four">four</a>
	<br>
	<a href="#five">five</a>
	<br>
	
	<!-- 在html页面中 id的值 要保持唯一  -->

	<div id="one">1</div>
	<div id="two">2</div>
	<div id="three">3</div>
	<div id="four">4</div>
	<div id="five">5</div>

</body>
</html>
```



## 1.8 HTML列表

### 1.8.1 无序列表

在网页上定义一个无编号的内容列表可以用<ul>、<li>配合使用来实现，代码如下：

```
<ul>
    <li>列表文字一</li>
    <li>列表文字二</li>
    <li>列表文字三</li>
</ul>

```

在网页上生成的列表，每条项目上会有一个小图标，这个小图标在不同浏览器上显示效果不同，所以一般会用样式去掉默认的小图标，如果需要图标，可以用样式自定义图标，从而达到在不同浏览器上显示的效果相同,实际开发中一般用这种列表。

### 1.8.2 有序列表

在网页上定义一个有编号的内容列表可以用<ol>、<li>配合使用来实现，代码如下：

```
<ol>
    <li>列表文字一</li>
    <li>列表文字二</li>
    <li>列表文字三</li>
</ol>

```

在网页上生成的列表，每条项目上会按1、2、3编号，有序列表在实际开发中较少使用。

其中type类型值：A a I i 1 start属性表示起始值

## 1.9 HTML表格

### 1.9.1 table常用标签

1、table标签：声明一个表格

2、tr标签：定义表格中的一行

3、td和th标签：定义一行中的一个单元格，td代表普通单元格，th表示表头单元格

### 1.9.2 table常用属性

1、border 定义表格的边框

2、cellpadding 定义单元格内内容与边框的距离

3、cellspacing 定义单元格与单元格之间的距离

4、align 设置单元格中内容的水平对齐方式,设置值有：left | center | right

5、valign 设置单元格中内容的垂直对齐方式 top | middle | bottom

6、colspan 设置单元格水平合并

7、rowspan 设置单元格垂直合并

代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>table表格</title>
</head>
<body>
	<table border="1" cellpadding="5" cellspacing="0" width="600" height="600" align="center">
		<tr>
			<th>姓名</th>
			<th>性别</th>
			<th>年龄</th>
			<th>邮箱</th>
			<th>段位</th>
		</tr>
		<tr align="center">
			<td>张三</td>
			<td>男</td>
			<td>20</td>
			<td>buzhidao@qq.com</td>
			<td rowspan="3">青铜1</td>
		</tr>
		<tr valign="top">
			<td>李四</td>
			<td>男</td>
			<td>20</td>
			<td>buzhidao@qq.com</td>
		</tr>
		<tr>
			<td>王五</td>
			<td>男</td>
			<td>20</td>
			<td>buzhidao@qq.com</td>
		</tr>
		<tr>
			<td>赵六</td>
			<td colspan="2">未知</td>
			<td>buzhidao@qq.com</td>
			<td>青铜5</td>
		</tr>
		<tr>
			<td>田七</td>
			<td>男</td>
			<td>20</td>
			<td>buzhidao@qq.com</td>
			<td>青铜5</td>
		</tr>
	</table>
</body>
</html>
```



## 1.10 HTML表单

表单用于搜集不同类型的用户输入，表单由不同类型的标签组成，实现一个特定功能的表单区域（比如：注册），

首先应该用<form>标签来定义表单区域整体，在此标签中再使用不同的表单控件来实现不同类型的信息输入

实现代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>form表单</title>
</head>
<body>
	<!-- 
		form 表单
		属性
			action  表单数据提交的地址 url 
			method 提交方式 
					默认 get方式    提交数据时 在url地址栏的位置会明文显示数据 数据长度受限 
					post方式  提交时不会再url地址栏显示数据 携带的数据相对多,主要受限于服务器(2M)

				数据格式
					get  1.py?username=abc&password=123
					post 1.py  usernname=abc password= 123
			enctype="multipart/form-data"
					负责将文件进行编码,如果有文件上传时 必须写该属性

	 -->
	<form action="./cgi-bin/1.py" method="get" enctype="multipart/form-data">
		<!-- 表单项 表单控件 -->
		用户名: <input type="text" name="username" ><br>
		密码: <input type="password" name="password" ><br>
		性别:
			<!-- 单选 type="radio" 注意 name值必须一样-->
			<input type="radio" name="sex" value="0" checked>女
			<input type="radio" name="sex" value="1">男
		<br>
		<!-- 多选 type="checkbox" checked 默认选中  -->
		爱好:
			<input type="checkbox" name="hobby[]" value="0">抽烟
			<input type="checkbox" name="hobby[]" value="1" checked>喝酒
			<input type="checkbox" name="hobby[]" value="2">烫头
		<br>
		<!-- 下拉选框  selected 设置默认 -->
		段位:
			<select name="dw">
				<option value="0">青铜</option>
				<option value="1">白银</option>
				<option value="2" selected>黄金</option>
				<option value="3">铂金</option>
			</select>
		<br>
			<!-- 文件控件  没有value 如果需要上传文件,要求form表单提交方式必须是post 必须有enctype属性-->
		上传头像:
			<input type="file" name="pic">
		<br>
		个人简介:
		<br>
		<textarea name="info" cols="60" rows="10" >这个小伙子真不错...</textarea>
			
		<!-- 隐藏域 -->
		<input type="hidden" name="id" value="110">

		<br>
		<!-- 提交按钮 -->
		<input type="submit" value="注册">

		<button>添加</button>

		<!-- 重置按钮 回到初始化状态-->
		<input type="reset">
		<!-- 图片按钮 -->
		<input type="image" src="./images/reset.gif">

	</form>
</body>
</html>
```

表单项中的属性:

```
*type属性:表示表单项的类型:值如下:

    text:单行文本框

    password:密码输入框

    checkbox:多选框 注意要提供value值

    radio:单选框 注意要提供value值

    file:文件上传选择框

    button:普通按钮

    submit:提交按钮

    image:图片提交按钮

    reset:重置按钮, 还原到开始\(第一次打开时\)的效果

    hidden:主表单隐藏域,要是和表单一块提交的信息,但是不需要用户修改

*name属性:表单项名,用于存储内容值的

*value属性:输入的值\(默认指定值\)

size属性:输入框的宽度值

maxlength属性:输入框的输入内容的最大长度

readonly属性:对输入框只读属性

*disabled属性:禁用属性

*checked属性:对选择框指定默认选项

src和alt是为图片按钮设置的

    注意：reset重置按钮是将表单数据恢复到第一次打开时的状态，并不是清空

    image图片按钮，默认具有提交表单功能。

placeholder 属性规定可描述输入字段预期值的简短的提示信息（比如：一个样本值或者预期格式的短描述）。
    该提示会在用户输入值之前显示在输入字段中。
    注意：placeholder 属性适用于下面的 input 类型：text、search、url、tel、email 和 password
```



# 2 .CSS

为了让网页元素的样式更加丰富，也为了让**网页的内容和样式能拆分开**，CSS由此思想而诞生，CSS是 Cascading Style Sheets 的首字母缩写，意思是层叠样式表。有了CSS，html中大部分表现样式的标签就废弃不用了，**html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁**。

## 2.1 css基本语法及页面引用

###  2.1.1 css基本语法

css的定义方法

选择器 { 属性:值; 属性:值; 属性:值;}

选择器是将样式和页面元素关联起来的名称，属性是希望设置的样式属性每个属性有一个或多个值。代码示例：

```
div{ width:100px; height:100px; color:red }
```

###  2.1.2 css页面引入方法

1、外联式：通过link标签，链接到外部样式表到页面中。

```
<link rel="stylesheet" type="text/css" href="css/main.css">

```

2、嵌入式：通过style标签，在网页上创建嵌入的样式表。

​     在head中写 style标签 在标签内写css 

```
<style type="text/css">

    div{ width:100px; height:100px; color:red }
    ......

</style>
```

3、内联式：通过标签的style属性，在标签上直接写样式。

```
<div style="width:100px; height:100px; color:red ">
......
</div>
```

三种方式完整版

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>css语法和使用方式</title>
	<!-- 1 在head中写 style标签 在标签内写css -->
	<!-- 嵌入式css -->
	<style type="text/css">
		div{
			width: 100px;
			height: 100px;
			color:red;
		}

	</style>

	<!-- 2 把写好的css引入到页面中使用 -->
	<link rel="stylesheet" href="./1.css">
</head>
<body>
	<div>love</div>
	<!-- 3 在标签内直接写style属性,在style属性中写css -->
	<div style="font-size:30px">miss</div>
</body>
</html>
```



## 2.2 Css选择器

### 2.2.1  标签选择器

标签选择器，此种选择器影响范围大，建议尽量应用在层级选择器中。
举例：

```
*{margin:0;padding:0}
div{color:red}   


<div>....</div>   <!-- 对应以上两条样式 -->
<div class="box">....</div>   <!-- 对应以上两条样式 -->
```



### 2.2.2  id选择器

通过id名来选择元素，元素的id名称不能重复，所以一个样式设置项只能对应于页面上一个元素，不能复用，id名一般给程序使用，所以不推荐使用id作为选择器。
举例：

```
#box{color:red} 

<div id="box">....</div>   <!-- 对应以上一条样式，其它元素不允许应用此样式 -->
```

### 2.2.3 类选择器

通过类名来选择元素，一个类可应用于多个元素，一个元素上也可以使用多个类，应用灵活，可复用，是css中应用最多的一种选择器。
举例：

```
.red{color:red}
.big{font-size:20px}
.mt10{margin-top:10px} 

<div class="red">....</div>
<h1 class="red big mt10">....</h1>
<p class="red mt10">....</p>
```

### 2.2.4 层级选择器

主要应用在选择父元素下的子元素，或者子元素下面的子元素，可与标签元素结合使用，减少命名，同时也可以通过层级，防止命名冲突。

空格 层级关系选择器  

举例：

```
.box span{color:red}
.box .red{color:pink}
.red{color:red}

<div class="box">
    <span>....</span>
    <a href="#" class="red">....</a>
</div>

<h3 class="red">....</h3>
```

### 2.2.5   组选择器

多个选择器，如果有同样的样式设置，可以使用组选择器。也成为 并列选择      

 逗号 组选择器 并列选择 共同设置
举例：

```
.box1,.box2,.box3{width:100px;height:100px}
.box1{background:red}
.box2{background:pink}
.box2{background:gold}

<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
```



### 2.2.6  伪类及伪元素选择器

常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after,它们可以通过样式在元素中插入内容。

```
.box1:hover{color:red}

<div class="box1">....</div>

a:hover {color: #FF00FF; text-decoration: underline} /* 鼠标在该元素上时 */


a:before{content:"Hello";}         /*在每个<a>元素之前插入内容*/
a:after{content:"world";}        /*在每个<a>元素之后插入内容*/
```

所有代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>选择器</title>
	<style type="text/css">
	/*  * 代表 选择页面中所以得标签,在html5得规范中不让使用*/
	/*	
		*{
			margin: 0px;
			padding: 0px;
		}
	*/
	/*选择页面中的body,div,p,h3,img,ul,li标签 组*/
	/*	
		body,div,p,h3,img,ul,li{
			margin: 0px;
			padding: 0px;
		}
	*/

	/* 标签选择器 写标签名,代表的是页面中所以得这个标签*/
	div{
		width: 100px;
		height: 100px;
		background: #369;
	}

	/* id  选择器  通过标签中的id属性值 来找元素*/
	#three{
		color:yellow;
		font-size:30px;
	}

	/* 类选择器 class 获取所有的当前这个类名的元素 */
	.fs{
		font-size:50px;
	
	}

	.fc{
		color:green;
	}


	</style>
</head>
<body>
	<div>1</div>
	<p class="fs">2</p>
	<div id="three">3</div>
	<h3 class="fs fc">4</h3>
</body>
</html>
```

### 2.2.7 优先级

1.同级别的选择器产生冲突时,谁离元素更近,谁优先级高

2.不同选择器的优先级不同,权重不同

3.标签内的行内样式 > id选择器 > class类选择器 > 标签选择器

代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>优先级</title>
	<style type="text/css">


		div{
			width: 100px;
			height: 100px;
			background: #369;

			font-size:40px;
			color:green;
		}


		div{
			color:yellow;
			border:1px solid red;
		}

		/*同级别的选择器产生冲突时,谁离元素更近,谁优先级高*/

		#one{
			width: 200px;
			height: 200px;
			color:blue;
		}


		.abc{
			width: 150px;
			height: 150px;
			background: #f39;
		}
	
	/*不同选择器的优先级不同,权重不同

	标签内的行内样式 > id选择器 > class类选择器 > 标签选择器
	*/


	</style>
</head>
<body>
	<div style="color:pink">1</div>
	<div id="one" class="abc" style="width: 50px;height: 50px;">2</div>
	<div class="abc">3</div>
	<div>4</div>
</body>
</html>
```



## 2.3  Css颜色,文本字体

### 2.3.1 css颜色表示法

1. 颜色名表示，比如：red 红色，gold 金色
2. 16进制数值表示，比如：#ff0000 表示红色，这种可以简写成 #f00
3. RGB颜色: 红(R)、绿(G)、蓝(B)三个颜色通道的变化 background-color: rgba(200,100,0);
4. RGBA颜色: 红(R)、绿(G)、蓝(B)、透明度(A) background-color: rgba(0,0,0,0.5);

```
16进制  0-9 a-f
rgb的值 0-255
```

###  2.3.2 css文本设置

常用的应用文本的css样式：

```
color 设置文字的颜色，如： color:red;

font-size 设置文字的大小，如：font-size:12px;

font-family 设置文字的字体，如：font-family:'微软雅黑';

font-style 设置字体是否倾斜，如：font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜

font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗

font 同时设置文字的几个属性，写的顺序有兼容问题，建议按照如下顺序写：
font：是否加粗 字号/行高 字体；如： font:normal 12px/36px '微软雅黑';

line-height 设置文字的行高，如：line-height:24px;

text-decoration 设置文字的下划线，如：text-

decoration:none; 将文字下划线去掉

text-indent 设置文字首行缩进，如：text-indent:24px; 设置文
字首行缩进24px

text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中
```

ex:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<style type="text/css">
		
		.a{
			width: 390px;
			height: 50px;
			border-top:1px solid #f00;
			border-bottom:3px solid #666;
			font:20px/50px '微软雅黑';
			color:#333;
			padding-left:10px;
		}

		div{
			width: 100px;
			height: 100px;
			border:1px solid red;

			margin: 10px;
		}

	/*	.c{
			margin-bottom: -1px;
		}*/

		.d{
			margin-top: 20px;
		}


	</style>
</head>
<body>
	<div class="a">新闻列表</div>
	<hr>
	<div class="c"></div>
	<div class="d"></div>
</body>
</html>
```

## 2.4 边框,背景,边距,溢出

### 2.4.1 css边框属性

```
border:宽度 样式 颜色;
border-color;
border-style; 边框样式：solid实线，dotted点状线，dashed虚线
border-width:
border-left-color;
border-left-style;
border-left-width:
CSS3的样式
border-radius：圆角处理
box-shadow: 设置或检索对象阴影
```

ex:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>边框</title>
	<style type="text/css">
		
		.a{
			width: 200px;
			height: 200px;
			/*	
			border-width:2px;
			border-style:solid;
			border-color:red;
			*/
			border:5px solid blue;
			/*	
			border-top:1px solid red;
			border-bottom:2px dashed blue;
			border-left:3px dotted yellow;
			border-top:none;*/
			/*border-radius:50%;*/
			border-radius:10px;
			/*border-radius:10px 20px;*/
			/*border-radius:10px 20px 30px;*/
			/*border-radius:10px 20px 30px 40px;*/

			
		}

		.a:hover{
			box-shadow:5px 5px rgba(0,0,0,.6);
		}


	</style>
</head>
<body>
	<div class="a"></div>
</body>
</html>
```



### 2.4.2 背景属性：background

```
background-color: 背景颜色
*background-image: 背景图片
*background-repeat：是否重复，如何重复?(平铺)
*background-position：定位
background-attachment： 是否固定背景，
            scroll:默认值。背景图像是随对象内容滚动
            fixed:背景图像固定 

css3的属性                
*background-size: 背景大小，如 background-size:100px 140px;

多层背景：
background: 
            url(./images/game/map_14.gif) no-repeat 100px 200px,
            url(./images/game/map_17.gif) no-repeat 150px 200px,
            url(./images/game/map_03.gif);
```

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>背景属性：background</title>
	<style type="text/css">
	
		.a{
			width: 500px;
			height: 500px;
			border:1px solid red;
			/*background-color:rgb(100,150,100);*/
			/*background: rgb(100,150,100);*/

			
			/*设置背景图片*/
			background-image:url(./images/1.jpg);
			/*background:url(./images/8.jpg);*/
			background-repeat:no-repeat;
			/*background-repeat:repeat-y;*/

			background-size:auto 500px;
		}

		.b{
			width: 60px;
			height: 60px;
			border:1px solid red;
			background:url(./images/tag.jpg) no-repeat -50px -130px;
			/*background-position:-50px -130px;*/
		}

		.b:hover{
			background-position:-363px -133px;
		}


	</style>
</head>
<body>

	<div class="a"></div>
	<div class="b"></div>
</body>
</html>
```

多层背景ex:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>多层背景</title>
	<style type="text/css">
	.game{
		width: 500px;
		height: 500px;
		background: 
			url(./images/game/map_04.gif) no-repeat 300px 100px,
			url(./images/game/map_04.gif) no-repeat 300px 134px,
			url(./images/game/map_05.gif) no-repeat 300px 169px,
			url(./images/game/map_15.gif) no-repeat 200px 250px,
			url(./images/game/map_03.gif);
	}

	</style>
</head>
<body>
	<div class="game"></div>
</body>
</html>
```

### 2.4.3 元素溢出

当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，设置的方法是通过overflow属性来设置。

**overflow的设置项：**
1、visible 默认值。内容不会被修剪，会呈现在元素框之外。
2、hidden 内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
3、scroll 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
4、auto 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>元素溢出</title>
	<style type="text/css">
		
		.a{
			width: 200px;
			height: 200px;
			background: #369;
			/*overflow: hidden;*/ /*超出隐藏*/
			/*overflow: scroll;以滚动条形式展现超出的内容*/
			overflow: auto;/*自动以滚动条形式展现超出的内容*/
		}

		.b{
			width: 300px;
			height: 100px;
			background: #f39;
		}

	</style>
</head>
<body>
	<div class="a">
		<div class="b">aaaaaaaaabbbbbbbbbbbbbbccccccccc</div>
	</div>
</body>
</html>

```

### 2.4.4 CSS边距

#### 2.4.4.1 内补白（内补丁）  

```
padding： 检索或设置对象四边的内部边距,如padding:10px; padding:5px 10px;
padding-top： 检索或设置对象顶边的内部边距
padding-right： 检索或设置对象右边的内部边距
padding-bottom：检索或设置对象下边的内部边距
padding-left： 检索或设置对象左边的内部边距
```

#### 2.4.4.2 外补白（外补丁）

```
margin： 检索或设置对象四边的外延边距,如 margin:10px; margin:5px auto;
margin-top： 检索或设置对象顶边的外延边距
margin-right： 检索或设置对象右边的外延边距
margin-bottom： 检索或设置对象下边的外延边距
margin-left： 检索或设置对象左边的外延边距
```



## 2.5 盒子

盒子的width和height设置的是盒子内容的宽和高，不是盒子本身的宽和高，盒子的真实尺寸计算公式如下：

- 盒子宽度 = width + padding左右 + border左右
- 盒子高度 = height + padding上下 + border上下

在布局中，如果我想增大内容和边框的距离，又不想改变盒子显示的尺寸，应该怎么做？

也就是使用padding时会让改变当前元素的尺寸,可以使用

box-sizing：border-box;  默认值是content-box



**外边距合并**

**margin相关技巧**
1、设置元素水平居中： margin:x auto;
2、margin负值让元素位移及边框合并

外边距合并指的是，当两个垂直外边距相遇时，它们将形成一个外边距。合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。解决方法如下：

1、使用这种特性
2、设置一边的外边距，一般设置margin-top
3、将元素浮动或者定位

**margin-top 塌陷**

两个元素 一个大块元素里面有一个小块元素,想给小元素设置单独margin-top 经过设置 他一设置 把大元素也给拽下来了, 这个问题属于塌陷的问题但是经过我给大元素 也就是这个小元素的父级元素设置 overflow:hidden 就解决了塌陷的问题

在两个盒子嵌套时候，内部的盒子设置的margin-top会加到外边的盒子上，导致内部的盒子margin-top设置失败，解决方法如下：

1、外部盒子设置一个边框
2、外部盒子设置 overflow:hidden
3、使用伪元素类：

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>margin-top塌陷</title>
	<style type="text/css">
		body{
			margin: 0;
			padding: 0;
		}
		/*.clearfix:before{
		    content: '';
		    display:table;
		}*/
		.a{
			width: 300px;
			height: 300px;
			background: #369;
			/*border:1px solid red;*/
			/*overflow: hidden;*/
		}

		.b{
			width: 200px;
			height: 200px;
			background: #f39;
			margin-top: 20px;
		}

	</style>
</head>
<body>
	<div class="a clearfix">
		<div class="b"></div>
	</div>
</body>
</html>
}
```

## 2.6块元素,内联元素,内联块元素

元素就是标签，布局中常用的有三种标签，块元素、内联元素、内联块元素，了解这三种元素的特性，才能熟练的进行页面布局。

### 2.6.1 块元素

块元素，也可以称为行元素，布局中常用的标签如：div、p、ul、li、h1~h6、dl、dt、dd等等都是块元素，它在布局中的行为：

- 支持全部的样式
- 如果没有设置宽度，默认的宽度为父级宽度100%
- 盒子占据一行、即使设置了宽度

### 2.6.2 内联元素

内联元素，也可以称为行内元素，布局中常用的标签如：a、span、em、b、strong、i等等都是内联元素，它们在布局中的行为：

- 支持部分样式（不支持宽、高、margin上下、padding上下）
- 宽高由内容决定
- 盒子并在一行
- 代码换行，盒子之间会产生间距
- 子元素是内联元素，父元素可以用text-align属性设置子元素水平对齐方式，用line-height属性值设置垂直对齐方式

### 2.6.3 内联块元素

内联块元素，也叫行内块元素，是新增的元素类型，现有元素没有归于此类别的，img和input元素的行为类似这种元素，但是也归类于内联元素，我们可以用display属性将块元素或者内联元素转化成这种元素。它们在布局中表现的行为：

- 支持全部样式
- 如果没有设置宽高，宽高由内容决定
- 盒子并在一行
- 代码换行，盒子会产生间距
- 子元素是内联块元素，父元素可以用text-align属性设置子元素水平对齐方式，用line-height属性值设置子元素垂直对齐方式

这三种元素，可以通过display属性来相互转化，不过实际开发中，块元素用得比较多，所以我们经常把内联元素转化为块元素，少量转化为内联块，而要使用内联元素时，直接使用内联元素，而不用块元素转化了。

### 2.6.4 display属性

display属性是用来设置元素的类型及隐藏的，常用的属性有：
1、none 元素隐藏且不占位置
2、block 元素以块元素显示
3、inline 元素以内联元素显示
4、inline-block 元素以内联块元素显示

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>display</title>
	<style type="text/css">

	.a{
		width: 200px;
		height: 200px;
		background: #369;
		
		/*不占位隐藏*/
		/*display: none;*/

		/*以块元素显示*/
		/*display: block;*/

		/*以内联元素显示*/
		/*display: inline;*/

		/*转为内联块 显示*/
		display: inline-block;
	}

	.b{
		width: 200px;
		height: 200px;
		background: #f39;
		display: inline-block;
	}

	</style>
</head>
<body>
	<div class="a"></div>
	<div class="b"></div>
</body>
</html>
```

## 2.7  浮动

**文档流**
文档流，是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置

**浮动特性**

1、浮动元素有左浮动(float:left)和右浮动(float:right)两种

2、浮动的元素会向左或向右浮动，碰到父元素边界、浮动元素、未浮动的元素才停下来

3、相邻浮动的块元素可以并在一行，超出父级宽度就换行

4、浮动让行内元素或块元素自动转化为行内块元素

5、浮动元素后面没有浮动的元素会占据浮动元素的位置，没有浮动的元素内的文字会避开浮动的元素，形成文字饶图的效果

6、父元素内整体浮动的元素无法撑开父元素，需要清除浮动

7、浮动元素之间没有垂直margin的合并

**清除浮动**

- 父级上增加属性overflow：hidden
- 在最后一个子元素的后面加一个空的div，给它样式属性 clear:both（不推荐）
- 使用成熟的清浮动样式类，clearfix

```
.clearfix:after,.clearfix:before{ content: "";display: table;}
.clearfix:after{ clear:both;}
.clearfix{zoom:1;}
```

清除浮动的使用方法：

```
.con2{... overflow:hidden}
或者
<div class="con2 clearfix">
```

代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>浮动</title>
	<style type="text/css">
		
		.a{
			width: 200px;
			height: 200px;
			background: #369;
			margin: 5px;
			
			float: left;
			/*float: right;*/
		}

		.b{
			width: 300px;
			height: 100px;
			background: #f39;
		}


		.all{
			width: 500px;
			
			border:1px solid red;

			/*overflow: hidden;*/
		}

		.clearfix:after,.clearfix:before{ content: "";display: table;}
		.clearfix:after{ clear:both;}
		.clearfix{zoom:1;}

	</style>
</head>
<body>
	<div class="b"></div>
	<div class="all clearfix">
		<div class="a">1</div>
		<div class="a">2</div>
		<div class="a">3</div>
		<!-- <div style="clear:both"></div> -->
	
		
	</div>

	<div class="b" style="width: 100%;background: #909;">aabbccddeeff</div>

</body>
</html>
```



## 2.8  定位

**关于定位**
我们可以使用css的position属性来设置元素的定位类型，postion的设置项如下：

- relative 生成相对定位元素，元素所占据的文档流的位置不变，元素本身相对文档流的位置进行偏移
- absolute 生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于上一个设置了相对或者绝对或者固定定位的父级元素来进行定位，如果找不到，则相对于body元素进行定位。
- fixed 生成固定定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。
- static 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性

```
relative 相对定位,不脱离文档流,相对于自己本身的位置进行定位,
absolute 绝对定位,脱离文档流,位置相对于已定位的父级,
    如果没有父级,或父级没有定位,那么相对于文档的00点 (body)
fixed 固定定位,脱离文档流,位置相对于浏览器窗口 进行定位
```

代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>position定位</title>
	<style type="text/css">

	body{
		height: 5000px;
	}
	
	.a{
		width: 200px;
		height: 100px;
		background: #369;


	}


	.b{
		width: 200px;
		height: 200px;
		background: #909;


		/*relative   相对定位  不脱离文档流 相对于自己本身的位置进行定位*/
		/*position: relative;*/

		/*absolute 绝对定位  脱离文档流 不在占据位置 
				定位时如果没有父级或者父级没有定位时 那么就参考文档(body)
				如果有父级并且父级已经进行了定位时 参考的是父级
		*/
		/*position: absolute;*/
		
		/*fixed 固定定位  脱离文档流 不在占据位置 定位时 参考浏览器窗口*/
		/*position: fixed;*/
		top:50px;left:10px;


	}

	.all{
		width: 500px;
		height: 500px;
		border:1px solid red;
		/*position: relative;*/
		position: absolute;
	}

	</style>
</head>
<body>
	<div class="a">1</div>
	<div class="all">
		<div class="b">2</div>
	</div>
</body>
</html>
```

### 2.8.1 楼层导航

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>楼层导航</title>
	<style type="text/css">
		body,ul{
			margin: 0;
			padding: 0;
			list-style:none;
		}
		

		#f1{height: 900px;background: #909;}
		#f2{height: 900px;background: #369;}
		#f3{height: 900px;background: #969;}
		#f4{height: 900px;background: #460;}
		#f5{height: 900px;background: #911;}
		#f6{height: 900px;background: #501;}
		#f7{height: 900px;background: #820;}
	
		.dh{
			width: 60px;
			position: fixed;
			top:100px;left:20px;
		
		}

		.dh li{
			height: 40px;
			background: #f9c;
			text-align:center;
			line-height:40px;
			border-bottom:1px solid #fff ;
		}

		.dh .active{
			background: #666;
		}



	</style>
</head>
<body>

	<div id="f1">1</div>
	<div id="f2">2</div>
	<div id="f3">3</div>
	<div id="f4">4</div>
	<div id="f5">5</div>
	<div id="f6">6</div>
	<div id="f7">7</div>

	<div class="dh">
		<ul>
			<li class="active"><a href="#f1">一楼</a></li>
			<li><a href="#f2">二楼</a></li>
			<li><a href="#f3">三楼</a></li>
			<li ><a href="#f4">四楼</a></li>
			<li><a href="#f5">五楼</a></li>
			<li><a href="#f6">六楼</a></li>
			<li><a href="#f7">七楼</a></li>
		</ul>
	</div>
	
</body>
</html>
```

### 2.8.2 z-index 层级

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>z-index 层级</title>
	<style type="text/css">

	div{
		width: 200px;
		height: 150px;

		position: absolute;
		/*top:100px;left:100px;*/
	}
	
	.a1{
		background: #909;
		z-index:1;
	}

	.a2{
		background: #996;
		z-index:2;
	}
	.a3{
		background: #363;
	}

	.a4{
		position: static;
		background: #911;
		z-index:99999999;
	}

	</style>
</head>
<body>
	<div class="a1">1</div>
	<div class="a2">2</div>
	<div class="a3">3</div>

	<div class="a4">4</div>
</body>
</html>
```



# 3. web布局方案

PC及移动端页面适配方法

设备屏幕有多种不同的分辨率，页面适配方案有如下几种：

1、全适配：流体布局+响应式布局
2、移动端适配：

- 流体布局+少量响应式
- 基于rem的布局
- 弹性盒模型

什么是 Viewport?

> viewport 是用户网页的可视区域。
>
> viewport 翻译为中文可以叫做"视区"。
>
> 手机浏览器是把页面放在一个虚拟的"窗口"（viewport）中，通常这个虚拟的"窗口"（viewport）比屏幕宽，这样就不用把每个网页挤到很小的窗口中（这样会破坏没有针对手机浏览器优化的网页的布局），用户可以通过平移和缩放来看网页的不同部分。

设置方法如下：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>viewport</title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <!-- 
        width：控制 viewport 的大小，可以指定的一个值，如果 600，或者特殊的值，如 device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。
        height：和 width 相对应，指定高度。
        initial-scale：初始缩放比例，也即是当页面第一次 load 的时候缩放比例。
        maximum-scale：允许用户缩放到的最大比例。
        minimum-scale：允许用户缩放到的最小比例。
        user-scalable：用户是否可以手动缩放。
     -->
    <style>
        .header{
            width: 100%;
            height: 50px;
            background: #369;
            line-height: 50px;
            text-align: center;
            font-size: 30px;
        }

    </style>
</head>
<body>
    <div class="header">页面header</div>
</body>
</html>
```

# 4.JavaScript

学习前端脚本语言javascript的基本概念、页面引入方式、获取页面元素及操作元素属性的技巧，学习函数的基本定义方法和使用方法。

**前端三大块**

```
1、HTML：页面结构
2、CSS：页面表现：元素大小、颜色、位置、隐藏或显示、部分动画效果
3、JavaScript：页面行为：部分动画效果、页面与用户的交互、页面功能

```

**什么是JavaScript？**

JavaScript是运行在浏览器端的脚步语言，JavaScript主要解决的是前端与用户交互的问题，包括使用交互与数据交互。 JavaScript是浏览器解释执行的，前端脚本语言还有JScript（微软，IE独有），ActionScript( Adobe公司，需要插件)等。

```
1. JavaScript 是一种客户端脚本语言（脚本语言是一种轻量级的编程语言）。 
2. JavaScript 通常被直接嵌入 HTML 页面。
3. JavaScript 是一种解释性语言（就是说，代码执行不进行预编译）。

```

**特点：**

```
1. 弱类型 
2. 基于对象。(因为面向对象需要具有封装、继承、多态的特征)
3. 安全
4. 兼容性
```

## 4.1 javascript嵌入页面的方式

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>js的使用方式</title>
	<style type="text/css">
		.a{
			width: 100px;
			height: 100px;
			background: #909;
		}

	</style>
</head>
<body>
	
	<!-- 第一种  在html页面中 写script标签 在标签内书写js代码 -->
	<script type="text/javascript">
		alert('hello  world')
		alert('2')

		/*
			在js中默认以分号作为语句的结尾,
			如果没有写分号,就以换行作为语句的结尾,
			如果没有分号,也没有换行 就报错
		*/ 
	</script>

	<!-- 第二种 在html种导入一个js文件 注意 在含有src属性的标签中不能再写js-->
	<script type="text/javascript" src="./1.js">
		//此处代码不执行
		// alert('h3');
	</script>

	<!-- 第三种 再html的标签中写js事件,再事件中执行js -->
	<div class="a" onclick="alert(1)"></div>

</body>

</html>
```

## 4.2 js变量

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>变量</title>
</head>
<body>
	<script type="text/javascript">
	//这里如果加上user strict 则必须写var,
	//如果不加上这个use strict 则可以写a=1
	"use strict";
	var a;
	a = 1;
	// var 爱 = 'love';//不推荐使用
	//关键字 if else true  false def function static  name
	// var $abc = 'abc';
	// var a =1,b=2,c=3;


	// alert(a);//在页面中弹出确认框
	console.log(a);//在控制台打印结果



	</script>
</body>
</html>
```

## 4.3 js数据类型转换 

### 4.3.1 js数据类型 

//  布尔类型  字符串  数字(整型,浮点,NaN)  对象(对象 数组 null) 函数  undefined

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<script type="text/javascript">

		//  布尔类型  字符串  数字(整型,浮点,NaN)  对象(对象 数组 null) 函数  undefined

		// typeof() 检测当前变量的数据类型

		// 布尔类型 boolean
		var a = true;
		var a = false;


		//字符串类型 '' "" string
		var a = 'abc';
		var a = "abc";
		var a = 'jdouohadusahdiuhad';
		var a = 'love="iloveyou"';
		var a = "love='iloveyou'";
		var n = 'love';
		var a = 'i'+n+'you';
		var a = 'ilove\r\nyou';

		//数字类型  number 整型  浮点  NaN ( not a number)
			var a = 521;
			var a = 5.21;
			var a = -521;
			var a = 010;//8
			var a = 012;//8+2

			//特殊的类型
			var a = NaN;



		// 对象类型 object
			//数组
			// var a = [1,2,3,4,5];

			//对象
			// var a = new Object();

			// null
			// var a = null;

		// 函数  function
			function love(){
				alert('iloveyou');
			}

			// love();

		// undefined 未定义


		// var s;
		// var s = undefined;



		console.log(a);
		console.log(typeof(a));

	</script>
</body>
</html>
```

### 4.3.2   js数据类型转换

使用：Number（）、parseInt() 和parseFloat（） 做类型转换

```
Number()强转一个数值(包含整数和浮点数)。

*parseInt()强转整数，

*parseFloat（）强转浮点数
```

函数isNaN()检测参数是否不是一个数字。

```
isNaN()  is not a number
```

//检测js中有哪些数据为假  false 0   0.0  NaN  ' '  null  undefined

```
代码:

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>数据类型转换</title>
</head>
<body>
	<script type="text/javascript">

	var a = '521';
	var a = '5.21';
	var a = '521a';
	var a = '52.1a';
	var a = 'a521';


	var r1 = Number(a);
	var r2 = parseInt(a);
	var r3 = parseFloat(a);

	// console.log(a,typeof(a));
	// console.log(r1,typeof(r1),'Number');
	// console.log(r2,typeof(r2),'parseInt');
	// console.log(r3,typeof(r3),'parseFloat');


	// Boolean(value) - 把给定的值转换成 Boolean 型；
	//检测js中有哪些数据为假  false 0 0.0 NaN '' null undefined

	var b = false;
	var b = 0;
	var b = 0.0;
	var b = '';
	var b = '0';//true 
	var b = NaN;
	var b = [];//true
	var b = Object();//true
	var b = null;//false
	// true
	var b = function(){
		alert(1);
	}

	var b = undefined;//false 

	// b();

	// console.log(b,typeof(b));

	var r  = Boolean(b);

	// console.log(r,typeof(r));

	var res = 0;

	if(res){
		console.log('ok');
	}else{
		console.log('no');
	}

	</script>
</body>
</html>
```

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
<script type="text/javascript">
// NaN  当把其它类型的值转为数字类型时,
	// 如果没办法用任何数字来表示,把类型转为number 但是值表示不了就成为NaN


	// Number() 可以将其他类型的值 转为数字类型
	// var a = '123px';


	// var res = Number(a);

	// console.log(a,typeof(a));
	// console.log(res,typeof(res));


	// 任何数字和NaN进行运算 得到的结果都是NaN
	var res = 100+NaN;


	// 任何数字和NaN进行比较 得到的结果都为false 除了 != !==
	var res = 100 < NaN;
	var res = 100 > NaN;
	var res = 100 >= NaN;
	var res = NaN > NaN;
	var res = NaN == NaN;
	var res = 100 != NaN;
	var res = NaN != NaN;


	//如何检测一个变量的值为NaN isNaN()
	// var a = NaN;
	var a = 100;
	var res = isNaN(a)
	console.log(res);
	</script>
</body>
</html>
```

## 4.4  js运算符

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
<!-- 这个如果用户点了这个 那么在窗口左下角会看到我们的代码 -->
<!-- <a href="javascript:alert(2)">百度一下</a> -->
<a href="javascript:void(1)"  onclick="alert(5)">百度一下</a>
	
<!-- 运算符 -->
<script type="text/javascript">
// 算数运算符 + - * / % ++ --
 var i =0;
 var b =5;
 // 前++给i +1了 我们在这里学的后++运算完自动给他+1
 var c = ++i ;
 console.log(c);

 var i = 0;
  i ++;
  console.log(i);

  // 字符串连接
   var b =100+100
   var b =100+'100'+100 //100100100
   var b =100+100+'100'//200100
   var b ='100'+100+100//100100100
   var b ='100'+100+'100'//100100100

   console.log(b)

 //赋值运算 = += -=
 
 //比较运算  > <　 >=    <=    ==    全等于=== //值 和类型都相等   不等于!=    不全等于!==
 

 var a = 100;
 var b = 200;
 if (a!=b){
 	console.log('a确实不等于b')
 }else{
 	console.log('~~~')
 }

 //逻辑运算符
 var a =true;
 var b = false;

res=a&&b; //相当于and 有假则加 两面同时为真才是真
console.log(res);

res =a||b;
console.log(res); //相当于or 有真则真  两面同时为假才是假


//三位运算符
// var a = false;
 var res = 1 > 2 ? 1 : 2;
 console.log(res);


</script>
</body>
</html>
```



## 4.5 js流程控制

js流程控制

> 流程控制用于基于不同的条件来执行不同的动作。

If 语句

> if... else ...
>
> if ... else if ... else...
>
> 可以单分支,双分支,也可以多分支,需要注意 else if中间必须要有空格

```
if (condition){
    //当条件为 true 时执行的代码
}else{
    //当条件不为 true 时执行的代码
}

```

switch 语句

> 多分支语句： switch（）{。 case ：。。。。}
>
> switch 语句用于基于不同的条件来执行不同的动作。

```
 switch(n){
    case 1:
        //执行代码块 1
        break;
    case 2:
        //执行代码块 2
        break;
    default:
        //与 case 1 和 case 2 不同时执行的代码
}
```



ex:

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>

	</title>
</head>
<body>
<script type="text/javascript">
var a = 2;
if (a==2){
	console.log('今天是周二')
}else{
	console.log('今天不是周二')
}


// 来判断条件
var b=15;
if (b==1){
	console.log('今天是周一')
}else if(b==2){
	console.log('今天是周二')
}else if(b==3){
	console.log('今天是周三')
}else if (b==4){
	console.log('今天是周四')
}else if (b==5){
	console.log('今天是周五')
}else{
	console.log('今天特么不上班')
}

//  switch多分支
//  switch 多分支
   var i =10;
   // 如果i =2了 那么直接跳到2了  但是如果底下没写break 他会都输出  如果写了break 
   // 也要看他写的位置  写的位置在输出的条件下面  那么也会输出! 
   // 如果 i= 10里面条件没有 那么直接跳到default里 !
   switch(i){
	    case 1:

	     console.log('1');
	      break

	    case 2:
	   	 console.log('2');
	   	case 3:
	   	 console.log('3');
	   	case 4:

	   	default:
	   		console.log('?')
   }

</script>
	
</body>
</html>
```

## 4.6 js循环

> 程序中进行有规律的重复性操作，需要用到循环语句。
>
> break 和 continue 语句对循环中的代码执行提供了更严格的控制。

#### 4.6.1**for循环**

```
for(var i=0;i<len;i++){
    ......
}

```

#### **4.6.2while循环**

```
var i=0;

while(i<8){

    ......

    i++;

}
```

#### 4.6.3for-in 语句

> for-in 语句是严格的迭代语句，用于枚举对象的属性。

```
var a = [10,20,30,40,50];
//迭代的是数组的下标。
for(i in a){
   document.write(a[i]);
}
//输出： 1020304050
```

## 4.7 js元素获取与操作

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>JS元素获取操作</title>
   <style type="text/css">
   #b{ width: 100px;
   	height: 100px;
   	background: #555;

   }

   </style>
</head>
<body>
	<div id="b"> </div>
	<input type="text" id="num1" value="123">

	<script type="text/javascript">
	// 获取页面中的元素 标签 节点 document文档对象  get 获取 通过ID
	var ys=document.getElementById('b')
	console.log(ys)

	// 操作
	// 样式操作
	ys.style.width='100px';
	ys.style.height='100px';
	// 获取样式
	var a = ys.style.width;
	console.log(a);

	// 文本操作
	// var c =document.getElementById('num1')
 // //  表单中的值设置操作
	// c.value='5555'
	// console.log(c.value)

	// 设置文本内容
	// 这个是在元素上面设置的内容 !
	 
	ys.innerHTML='wocaonidie'
	console.log(ys.innerHTML);
```



## 4.8 js定时器

定时器：
setTimeout  只执行一次的定时器 
clearTimeout 关闭只执行一次的定时器
setInterval  反复执行的定时器
clearInterval 关闭反复执行的定时器

#### 4.8.1 定时应用

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>定时器</title>
</head>
<body>
	<script type="text/javascript">
// 单词定时  隔多长时间就执行一次代码
// 这个清除定时写顶上写底下都行
// 格式    定时函数(要定时的函数,多少秒)
  var a =setTimeout(function(){
  	console.log(1);
 },3000 );
 // 这就表示已经清除了 虽然结果还是会被打印出来! 这个结果是对象的瞬间给到a的  
  clearTimeout(a)
 console.log(a)


// 多次定时  清除定时的时候要写底下
  var b = setInterval(function(){
  	console.log(2)
  },3000)

  clearInterval(b);
	</script>
</body>
</html>

```

#### 4.8.2图片定时更换

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>图片定时更换</title>
	<img src='./img/p1.png' id='img'>
	<script type="text/javascript">
	var b=document.getElementById('img');

	var i=1;
	setInterval(function(){
		i++;
		if (i==6) {
			i=1;
		}
		 img.src='./img/p'+i+'.png';
		
	},500)
	</script>

</head>
<body>
	
</body>
</html>
```



## 4.9 js函数

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>函数</title>
</head>
<body>
  <script type="text/javascript">
  chifan();

  // 这么定义可以在函数之前来调用
  function chifan(){
  	alert('你什么时候去吃饭呢?')
  }
 


 // 这么定义不可以在函数之前来调用 
 // 注意函数名字!
  var b =  function(){
  	alert('how do you do you');
  }
  
  b();


  </script>
	
</body>
</html>
```

#### 4.9.1关于参数

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>关于参数的问题</title>
</head>
<body>
<script type="text/javascript">
 function lyl(a,b,c){
 	console.log(a,b,c);
 	// console.log(arguments);
 }   //这里少传参数,会打印参数的时候说未定义
 lyl(1);


function ren(d,e,f){
	// arguments 可以获取当前函数传递的所有实参 已数组的方式给我们
	
	console.log(d,e,f);
	// love(1,2,3,4,5,6);//调用函数时 如果多传递参数,那么多传递的参数会被'忽略',使用arguments找到所有参数
	console.log(arguments);
}
ren(1,2,3,5,6,4);

</script>
	
</body>
</html>
```

#### 4.9.2关于函数的返回值

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>关于函数返回值</title>
</head>
<body>
	<script type="text/javascript">



	function love(){
		console.log(1);

		//如果在函数中不写 return 或者只写了return  默认范湖undefined
		// return;

		//在js中可以返回任意值,
		return function(){
			console.log(2);
		};
	}

	var res = love();

	// console.log(res);

	res();

	</script>
</body>
</html>
```



## 4.10 js对象

### 4.10.1对象的定义方式

```
1.使用原始的方式创建内置对象
    var myObject = new Object();
    myObject.name = “lijie”;
    myObject.age = 20;
    myObject.say = function(){...
```

```
2.直接创建自定义对象
    var 对象名 = {属性名1：属性值，属性名2：属性值2，…….}
```

```
3.使用自定义构造函数创建对象
    function pen(name,color,price){
        //对象的name属性
        this.name = name;
        //对象的color属性
        this.color = color;
        //对象的piece属性
        this.price = price;
        //对象的say方法
        this.say = function(){};
    }
     var pen = new pen(“铅笔”,”红色”,20);
    pen.say();
```

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>对象的定义方式</title>
</head>
<body>
	<script type="text/javascript">


	// new Object() 创建一个空对象
	var abc = new Object();


	//属性操作 . 成员访问符
		//添加
			abc.name = 'zhangsan';
			a = 'age';
			abc[a] = 21;//当成员名存在于变量中时,使用中括号
			abc['a'] = 20;//如果中括号中加引号,那么就是一个字符串
		//获取
			// var n = abc.name;
			// var n = abc['name'];
			// var n = abc[a];

			// alert(n);

		//修改
			// abc.name = 'lisi';
		//删除
			// delete abc.age;

	//方法
		abc.say = function(){
			alert('我在说话');
		}

		s = 'sing';
		abc[s] = function(){
			console.log('是谁在唱歌');
		}


		// this  这个  在成员方法中使用  代表的是当前这个对象
		abc.info = function(){
			alert(this.name);
		} 

	abc.info();


	// abc.say();
	// abc[s]();
	// abc['sing']();

	// alert(abc);
	console.log(abc);


	</script>
</body>
</html>
```

### 4.10.2this关键字

```
this单词本身就是  这个 的意思
在对象的方法中使用,代表着当前这个对象
意味着当对象调用这个方法时,方法中的this就代表着这个对象
```

### 4.10.3遍历对象属性

```
for(var i in window){
    document.write(i+”----”+window[i]);
}
这种语句可以遍历对象中的所有属性或数组中的所有元素。
```

### 4 json格式定义对象

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>对象快速定义方式,json格式定义对象</title>
</head>
<body>
	<script type="text/javascript">


	//对象快速定义方式,json格式定义对象
	//属性名与属性值 之间  用冒号分割,多个属性之间用逗号分割

	//{属性名:属性值,属性名:属性值,方法名:函数, ....}

	var dd = {
			name:'钉钉',
			age:18,
			say:function(){
				console.log('ok');
			}
		}

	console.log(dd);



	</script>
</body>
</html>
```

json对象定义方式--构造函数

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>js对象定义方式--构造函数</title>
</head>
<body>
	<script type="text/javascript">

	//构造函数
	function person(n,a,s,func){
		//为当前这个对象的属性进行赋值
		this.name = n;
		this.age = a;
		this.sex = s;

		this.dance = func;


	}

	//实例化对象

	var zs = new person('张三',21,'男',function(){
		console.log(this.name+'在跳舞');
	});
	var ls = new person('李四',22,'男',function(){
		console.log(this.name+'在跳舞');
	});

	// console.log(zs);
	// console.log(ls);

	// zs.dance();
	// ls.dance();

	// console.log(this);


	//对象的遍历
	// for(var i in zs){
	// 	//i 代表的是属性名或方法名
	// 	// console.log(i);
	// 	console.log(zs[i]);
	// }

	var abc = new Object();


	// 对象.constructor; //查看当前对象的构造函数是谁

	//object
	var r = abc.constructor
	console.log(r);

	//person
	var r = zs.constructor
	console.log(r);


	var arr = [1,2,3,4];
	//Array() 
	var r = arr.constructor
	console.log(r);






	</script>
</body>
</html>
```



## 4.11 js数组

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>js数组</title>
</head>
<body>
	<script type="text/javascript">


	//定义数组 1
		// var arr = new Array();
		// var arr = new Array(1,2,3,4,5);
		// var arr = new Array(5);//直接定义数组元素的个数,元素的值为undefined

	//定义数组 2
		// var arr = [];
		// var arr = [1,2,3,4,6];
		// var arr = [6];//定义数组的一个元素 值为6

	//数组中的值可以是任意类型的
	// var arr = [true,false,521,3.1415926,'ok',NaN,undefined,null,new Object(),[1,2,3,4],function love(){alert('11')}];

	// arr[10]();

	//js中的数组 下标永远保持连续
	var arr = [1,2];
	//通过下标进行元素的操作
	arr[2] = 'ok';
	arr[100] = '100ok';
	// console.log(arr);

	//数组中常用的属性  length
	// console.log(arr.length);

	//对象没有这个length属性
	// var obj = {name:'zhangsan',age:21}
	// console.log(obj.length);

	var arr = [1,2,3,4,5];

	// 添加元素
		arr[5] = 'a';
		arr[arr.length] = 'b';

	// push() 和 pop() 从数组最后增加成员或删除成员
		var r = arr.push('c');//在数组尾部添加元素.,返回数组最新的长度
		var r = arr.pop();//在数组尾部删除一个元素,返回删除的元素

	// unshift()和 shift() 从数组前面增加成员或删除成员
		var r = arr.unshift('aa');//在数组的头部添加一个元素.返回数组最新长度
		var r = arr.shift();//在数组的头部删除一个元素.,返回删除的元素

	// splice() 在数组中增加或删除成员
	// console.log(arr);
		// var r = arr.splice(2,2);//从第几个下标开始,删除几个元素
		// var r = arr.splice(2,2,'a1','a2');//从第几个下标开始,删除几个元素,添加几个元素
		var r = arr.splice(2,0,'aa','bb');

	// console.log(r);
	// console.log(arr);


	//多维数组 
	// var arr = [1,2,3,[11,22,33,[111,222,333,[1111,2222,3333]]],4,5];
	// arr[3][1];
	// console.log(arr[3][1]);
	// console.log(arr[3][3][3][2]);


	// var arr = [];
	// arr['name'] = '张三';

	// // alert(arr.name);
	// console.log(arr.length);

	</script>
</body>
</html>
```



### 4.11.1 js数组循环

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>数组循环</title>
</head>
<body>
	<script type="text/javascript">

	var arr = [1,2,3,4,5,'aa','bb','cc'];

	arr[20] = 'love';


	//循环
	for (var i = 0; i < arr.length; i++) {
		// console.log(i);
		console.log(arr[i]);
	};


	for(var i in arr){
		// console.log(i);
		console.log(arr[i]);
	}
	

  console.log(arr);


	</script>
</body>
</html>
```

全选,全不选,反选

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>全选,全不选,反选</title>
</head>
<body>
	<h3>独自的解释:</h3>
	
	<label><input type="checkbox">滚犊子</label><br>
	<label><input type="checkbox">扯犊子</label><br>
	<label><input type="checkbox">王八犊子</label><br>
	<label><input type="checkbox">牛犊子</label><br>
	<label><input type="checkbox">瘪犊子</label><br>
	<label><input type="checkbox">完犊子</label><br>
	<label><input type="checkbox">损犊子</label><br>
	<button onclick="func(1)">全选</button>
	<button onclick="func(2)">全不选</button>
	<button onclick="func(3)">反选</button>

	<script type="text/javascript">
	//获取页面中的所有input  获取的是集合
	var inps = document.getElementsByTagName('input');

	function func(n){
		//遍历
		for (var i = 0; i < inps.length; i++) {
			switch(n){
				case 1:
					//设置全选
					inps[i].checked = true;
					break;
				case 2:
					//设置全不选
					inps[i].checked = false;
					break;
				case 3:
					//设置反选
					inps[i].checked = !inps[i].checked;
					break;
			}
		};
	}




	</script>
</body>
</html>
```



### 4.11.2 js Math 数学对象

//随机一个从m到n的随机整数  (n-m+1)+m

	function rand(m,n){
		return Math.floor(Math.random()*(n-m+1))+m;
	}
```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Math数学对象</title>
</head>
<body>
	<script type="text/javascript">

	//四舍五入
	var res = Math.round(5.421);

	// /退一取整
	var res = Math.floor(1.9);

	//进一取整
	var res = Math.ceil(1.0);

	//幂运算 用来获取x的y次方 2的3次方
	var res = Math.pow(2,3);

	//开方运算 返回一个数的平方根
	var res = Math.sqrt(9);


	//随机数  random() 返回一个从0到1的随机小数,注意 可能取到0  但是取不到1
	var res = Math.random();

	//随机 0 - 9 之间的随机小数,包含9的小数
	var res = Math.random()*10;

	//随机 0 - 9 之间的随机整数
	var res = Math.floor(Math.random()*10);

	//随机 1 - 10 之间的随机整数
	var res = Math.floor(Math.random()*10)+1;

	// 随机 5 - 15 之间的随机整数 15-5+1   
	var res = Math.floor(Math.random()*11)+5;

	// 3 - 99   99-3+1  +3

	//随机一个从m到n的随机整数  (n-m+1)+m
	function rand(m,n){
		return Math.floor(Math.random()*(n-m+1))+m;
	}

	var res = rand(20,30);



	console.log(res);


	</script>
</body>
</html>
```

### 4.11.3随机数组,随机点名

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>随机数组</title>
	<style type="text/css">
	#names{
		width: 200px;
		height: 200px;
		margin: 100px auto;
		border:1px solid red;
		text-align:center;
		line-height:200px;
		margin-bottom: 10px;
		font-size:30px;
	}

	</style>
</head>
<body>
	<div id="names"></div>

	<center>
		<button onclick="func()">点名</button>
	</center>


	<script type="text/javascript">
	//扩展要求  点名不能重复

	//定义全局变量
	var isStart = false;
	var init = null;

	//获取元素
	var names = document.getElementById('names');
	//定义人名数组
	var arr = ['张三','李四','王五','赵六','田七','张三1','李四1','王五1','赵六1','田七1'];

	//获取最大下标
	var len = arr.length-1;

	//封装函数
	function func(){
		if(isStart){
			//如果已经开始,再点击就是关闭
			clearInterval(init);
			isStart = false;
			return;
		}

		isStart = true;
		//启动定时器	
		init = setInterval(function(){
			//随机下标
			var n = rand(0,len);
			//获取当前随机下标的人名放入到标签中
			names.innerHTML = arr[n];
		},100)
		
	}


	//封装随机函数
	function rand(m,n){
		return Math.floor(Math.random()*(n-m+1))+m;
	}


	</script>
</body>
</html>
```

## 4.12  js正则

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<script type="text/javascript">
  	var str = 'iloveyouadasq521simiada';
  	//1. 用它匹配 转义字符 
  	var reg =/\w/; //匹配单个字母数字下划线;		进门有的话取走就走了!/意思就是只取一次
  	var reg =/\W/; //匹配单个的非字母数字下划线;	进门有的话取走就走了!/意思就是只取一次
  	var reg =/\d/; //匹配单个数字;  			进门有的话取走就走了!/意思就是只取一次
  	var reg = /\D/; //匹配单个非数字; 		进门有的话取走就走了!/意思就是只取一次
  	var reg =/\s/;  //匹配单个空白字符;		进门有的话取走就走了!/意思就是只取一次
  	var reg =/\S/; //匹配单个非空白字符;		进门有的话取走就走了!/意思就是只取一次

	// test 只返回true 或者false 
  	var res1=reg.test(str);
  	var res2=reg.exec(str);
  	// 打印出来的 是否匹配到 , 第一个给ture  或者false 第二个会给结果!
  	// console.log(res1);
  	// console.log(res2);




  	//2.元字符  . * + ? {} [] () | ^ $
  	var str ='wwwwwww.wwwwbaaaaaidu.aaacom defiloveyou  nihao WLQDMAS ';
  	var reg =/./;//匹配除了换行之外的任意单个字符 
  	var reg=/w*/;//匹配0次或者多次    没有也是true 有的话 连着有几个就拿几个
  	var reg=/a+/;// 匹配一次或者多次 有一次就不接着取了  要是连着有的话就都拿
  	var reg=/a+?/; //拒绝贪婪  有一个就取出来 , 连着有也不取了
  	var reg =/a*?///拒绝贪婪
  	var reg = /a{2}/;//限制匹配次数  取两个
  	var reg =/a{2,5}/;//限制匹配2到5次
  	var reg =/[a-zA-Z0-9_$]/;//[]限制取值范围  //这些都取一次
  	var reg =/i(love)you/;//俩都取出来了  想单拿出来love  ()这是子组
  	var reg=/abc|def/;//或 这俩只要有一个就给你取出来一个


  	var res3 = reg.test(str);
  	var res4 = reg.exec(str);
  	// console.log(res3);
  	// console.log(res4);

  	var str = 'adm5insaasa';

  	

  	//3. ^ $ 限制开始  和  结尾  ?
  	var reg=/^\d\w{6,18}$/;
  	var res1 = reg.test(str);
  	var res2 = reg.exec(str);
  	console.log(res1);
  	console.log(res2);





// var str = '<a href="http://www.baidu.com">百度一下</a>';

// var reg = /<a href="(.*?)">(.*?)<\/a>/;


// 	var res1=reg.exec(str);
//  返回true或者false
// 	console.log(res);
// 	console.log(res1);





	</script>
</body>
</html>
```



# 5.jQuery

> jQuery是一个是免费、开源的javascript库, 也是目前使用最广泛的javascript函数库。
>
> jQuery极大的方便你完成web前段的相关操作,例如节点操作,元素操作,事件绑定,ajax操作, 且解决了大多数的兼容性问题
>
> jQuery的版本分为1.x系列和2.x、3.x系列，1.x系列兼容低版本的浏览器，2.x、3.x系列放弃支持低版本浏览器，目前使用最多的是1.x系列的。
>
> [http://jquery.com/](http://jquery.com/)官方网站

jquery是一个函数库，一个js文件，页面用script标签引入这个js文件就可以使用。

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>jquery使用</title>
</head>
<body>
	<script type="text/javascript" src="./jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	//检测jquery是否引入成功
	alert($);


	</script>
</body>
</html>
```



## 5.1 jquery选择器 

**jquery用法思想**
选择某个网页元素，然后对它进行某种操作

**jquery选择器**
jquery选择器可以快速地选择元素，选择规则和css样式相同

### 5.1.1基础选择器

```
//通过id来获取元素 document.getElementById();
// $('#logo').css('border','solid 2px red');
//通过标签名来获取元素
// $('li').css('background','#369');
//通过class类名获取元素
// $('.w').css('background','#369');
//逗号 并列获取
// $('#logo,#menu').css('background','#369');
//空格 层级获取
// $('#images li').css('background','#369');

```

### 5.1.2过滤获取

```
//获取第一个和最后一个元素
// $('li:first').css('background','#369');
// $('li:last').css('background','#369');
//获取指定索引的元素 索引从0开始 
// $('li:eq(7)').css('background','#369');
// $('li').eq(7).css('background','#369');
//获取包含指定文本的元素
// $('li:contains(国)').css('background','#369');
//通过包含指定属性来获取元素 通过属性来获取
// $('li[name=y]').css('background','#369');

```

### 5.1.2父子关系获取

```
//获取所有的子元素
// $('#images').children().css('background','#369');
//获取第一个子元素
// $('ul li:first-child').css('background','#369');
//获取最后一个子元素
// $('ul li:last-child').css('background','#369');
//获取指定索引的子元素 索引从1开始
// $('ul li:nth-child(3)').css('background','#369');

//获取元素上一个同级元素
// $('#f').prev().css('background','#369');
//获取元素下一个同级元素
// $('#f').next().css('background','#369');
//获取同辈元素 (同辈元素不包含自己)
// $('#f').siblings().css('background','#369');


//获取父级元素
// $('#f').parent().css('background','#369');
//获取先辈级元素
// $('#f').parents('#all').css('border','solid 1px red');

//在父级元素中查找指定的子元素
$('#images').find('.w').css('background','#369');
```



## 5.2  jQuery元素操作

通过jQuery可以操作控制元素的样式,文本,属性等

### 5.2.1jquery样式操作

**css操作行内样式**

```
// 获取div的样式
$("div").css("width");
$("div").css("color");


//设置div的样式
$("div").css("width","30px");
$("div").css("height","30px");
$("div").css({fontSize:"30px",color:"red"});

```

**特别注意**
选择器获取的多个元素，获取信息获取的是第一个，比如：$("div").css("width")，获取的是第一个div的width。

### 5.2.2类名class操作

**操作样式类名**

```
$("#div1").addClass("divClass2") //为id为div1的对象追加样式divClass2
$("#div1").removeClass("divClass")  //移除id为div1的对象的class名为divClass的样式
$("#div1").removeClass("divClass divClass2") //移除多个样式
$("#div1").toggleClass("anotherClass") //重复切换anotherClass样式

```

### 5.2.3文本操作

**1、html() 取出或设置html内容**

```
// 取出html内容

var $htm = $('#div1').html();

// 设置html内容

$('#div1').html('<span>添加文字</span>');

```

**2、text() 取出或设置text内容**

```
// 取出文本内容

var $htm = $('#div1').text();

// 设置文本内容

$('#div1').text('<span>添加文字</span>');

```

### 5.2.4属性操作

**1、attr() 取出或设置某个属性的值**

```
// 取出图片的地址

var $src = $('#img1').attr('src');

// 设置图片的地址和alt属性

$('#img1').attr({ src: "test.jpg", alt: "Test Image" });

//也可以用户设置class属性
$('#abc').attr('class','all')

//也可以自定义 属性
$('#abc').attr('love','iloveyou')
```

**2、removeattr()删除属性**

```
$('#abc').removeattr('class')

$('#abc').removeattr('love')
```



## 5.3 相关尺寸

### 5.3.1获取元素相对于文档的偏移量

> var pos = $('#small').offset();
>
> // console.log(pos.left);
>
> // console.log(pos.top);

### 5.3.2获取当前元素相对于父级元素的偏移量

> var l = $('#small').position().left;
>
> var t = $('#small').position().top;
>
> // console.log(l,t);

### 5.3.3获取文档滚动距离

> var st = $(document).scrollTop();
>
> var sl = $(document).scrollLeft();

### 5.3.4获取元素的宽度和高度

> var w = $('#big').width();
>
> var h = $('#big').height();

### 5.3.5设置元素的宽度和高度

> $('#big').width(400);
>
> $('#big').height(400);
>
> // console.log(w,h);

### 5.3.6获取可视区域的宽度和高度

> var cw = $(window).width();
>
> var ch = $(window).height();

### 5.3.7获取文档的宽度和高度

> var cw = $(document).width();
>
> var ch = $(document).height();
>
> console.log(cw,ch);

## 5.4关于事件的绑定

#### 5.4.1基本绑定

$(element).click(function(){})

$(element).dblclick(function(){})

#### 5.4.2加载完毕事件

$(document).ready(function(){})

$(function(){})

#### 5.4.3方法绑定

$(element).bind('click', function(){})//绑定事件

$(element).unbind();//解除事件绑定

#### 5.4.4动态绑定

$(element).live('click', function(){})

需注意，live方法在高版本的jquery中移出了,在使用时请注意版本

#### 5.4.5事件触发

当我们想要去触发某个元素的事件时可以使用 trigger,注意需指定元素的事件类型

$(element).trigger('click')

事件冒泡和默认行为

**上面几个代码**

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<style type="text/css">
	.a{
		width: 100px;
		height: 100px;
		background: #369;
		margin: 10px;
	}

	</style>



</head>
<body>



	<div class="a">1</div>




	<script type="text/javascript" src="./jquery-1.8.3.min.js"></script>
	<script type="text/javascript">


	//文档加载完毕事件  onload
	
// $(function(){
// 		$('.a').css('border','5px solid red')
// 	})

	//事件的绑定  基本绑定
		// $('.a').click(function(){alert(1);})
		// $('.a').dblclick(function(){alert(2);})

	// //方法绑定  bind()
		$('.a').bind('click',function(){
			console.log(2);
		})
	
	//动态绑定 live() 在高版本中移除了此方法
		$('.a').live('click',function(){
			console.log(3);
		})
	
	//创建标签
	var d = $('<div class="a">动态创建的标签</div>')
	// 将创建标签 加入到body中
	$('body').append(d);


	// 事件触发 
	// 当我们想要去触发某个元素的事件时可以使用 trigger,注意需指定元素的事件类型
	// $('.a').trigger('dblclick')


	//解除事件绑定  unbind
	// $('.a').unbind('click')//解除元素的指定事件
	// $('.a').unbind()//解除元素的所有事件


	</script>


</body>
</html>
```

#### 5.4.6事件冒泡

当触发一个元素的事件时,会自动触发该元素的父级和先辈级的同类型事件,造成事件并发,导致页面混乱,我们称为事件冒泡

此时我们可以在元素的事件处理函数中 返回一个false 来进行阻止,注意这个方法仅限于在jquery中使用

默认行为

在页面中有些元素是具备默认行为的,例如a链接的单击,表单的提交,都会进行跳转或提交,这些我们成为默认行为

但是在绑定上事件后,它首先会先执行事件,再去执行默认行为,而有时我们只想让其触发事件,但不执行默认行为时,

我们可以在该元素的事件中 返回一个false来进行阻止默认行为

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>事件冒泡和默认行为</title>
	<style type="text/css">
	div{
		position: absolute;top:50px;left:50px;
		border-radius:50%;
	}
	#one{width: 500px;height: 500px;background: #369;}
	#two{width: 400px;height: 400px;background: #909;}
	#three{width: 300px;height: 300px;background: yellow;}
	#four{width: 200px;height: 200px;background: #f39;}
	#five{width: 100px;height: 100px;background: red;}

	</style>
</head>
<body>
	<div id="one">
		<div id="two">
			<div id="three">
				<div id="four">
					<div id="five"></div>
				</div>
			</div>
		</div>
	</div>

	<hr>
	<a href="./7.html">baiduyixia </a>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">
	/*
	事件冒泡:
		当触发一个元素的事件时  会自动触发所有先辈级的同类型事件
		造成事件并发,导致页面混乱,这种情况我们称为 事件冒泡
	如何解决事件冒泡
		在事件的处理中 return false;

	*/

	//获取页面中所有的div 绑定单击事件
	$('div').click(function(){
		//改变背景颜色
		$(this).css('background','#000');

		//阻止事件冒泡
		return false;
	})

	$('a').click(function(){
		alert(2);

		//阻止默认行为
		return false;
	})


	</script>
</body>
</html>
```



## 5.5 事件案例

### 5.5.1  点击随机变换颜色

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<style type="text/css">
	div{
		width: 150px;
		height: 150px;
		background: #909;
		margin: 10px;
		float: left;
	}

	</style>
</head>
<body>
	<div></div>
	<div></div>
	<div></div>
	<div></div>
	<div></div>

	<script type="text/javascript">

	//获取页面中所有的div
	var divs = document.getElementsByTagName('div');

	for (var i = 0; i < divs.length; i++) {
		//绑定单击事件
		divs[i].onclick = function(){
			//随机颜色
			var rgb = 'rgb('+rand(0,255)+','+rand(0,255)+','+rand(0,255)+')';
			// divs[i].style.background = rgb;
			this.style.background = rgb;
			// console.log(i);
		}
	};


	function rand(m,n){
		return Math.floor(Math.random()*(n-m+1))+m;
	}

	</script>
</body>
</html>
```

### 5.5.2 用户注册用户名,涉及到正则 焦点事件 form表单

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

	<form action="" class="login">
		用户名: <input type="text" name="username" readmin="请输入6-18位用户名"><span></span><br>
		密码 : <input type="password" name="password" readmin="请输入6-18位密码"><span></span><br>
		邮箱: <input type="text" name="email" readmin="请输入正确的邮箱"><span></span><br>
		<button>注册</button>
	</form>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>

	<script type="text/javascript">
	//全局变量
	var isUser = false;
	var isPass = false;
	var isEmail = false;
// alert($);


	// 获取焦点事件 focus() 丧失焦点事件 blur()  表单提交事件 submit()

	//表单提交事件
	$('form').submit(function(){
		//触发所有的丧失焦点事件 如果有一个错了就不
		$('input').trigger('blur')
		
		if(isUser && isPass && isEmail){
			return true;
		}else{
			return false;
		}
	})

	//绑定获取焦点事件
	$('input').focus(function(){
		//获取提醒信息  这个标签里的属性给提示出去
		var v = $(this).attr('readmin');
		//设置到span中   把这个标签的下一个标签同级别的给添加颜色
		$(this).next().html(v).css('color','blue')
	})

	//绑定用户名的丧失焦点事件
	$('input[name=username]').blur(function(){
		//获取当前输入的信息
		var v = $(this).val();
		// res是他的输入长度
		var res = v.length;
		// 接下来做判断
		if(res < 6 || res > 18){
			$(this).next().html('用户名输入错误').css('color','red')
			isUser = false;
		}else{
			$(this).next().html('√').css('color','green')
			isUser = true;
		}
	})

	//绑定密码的丧失焦点事件
	$('input[name=password]').blur(function(){
		//获取当前输入的信息
		var v = $(this).val();
		var res = v.length;
		if(res < 6 || res > 18){
			$(this).next().html('密码输入错误').css('color','red')
			isPass = false;
		}else{
			$(this).next().html('√').css('color','green')
			isPass = true;
		}
	})

	$('input[name=email]').blur(function(){
		//获取当前输入的信息
		var v = $(this).val();
		var reg = /^\w+@\w+\.(com|cn|org|net)$/
		// 使用正则检测他输入的字符 
		if(reg.test(v)){
			$(this).next().html('√').css('color','green')
			isEmail = true;
		}else{
			$(this).next().html('邮箱格式不正确').css('color','red')
			isEmail = false;
		}
	})
	</script>
</body>
</html>
```



### 5.5.3 选项卡

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>选项卡</title>
	<style type="text/css">
	body,ul,li{
		margin: 0;
		padding:  0;
		list-style:none;
	}

	.all{
		width: 600px;
		height: 300px;
		margin: 100px auto;
	}
	.options li{
		width: 100px;
		height: 50px;
		float: left;
		border:1px solid #333;
		box-sizing:border-box;
		text-align:center;
		line-height:50px;
		border-right:none;
		cursor:pointer ;
	}
	.options li:last-child{
		border-right:1px solid #333;
	}

	.card li{
		height: 300px;
		border:1px solid #333;
		text-align:center;
		line-height:300px;
		display: none;
	}
	.options .active{
		/*display: block;*/
		background: #369;
		color:#fff;
	}
	.card .active{
		display: block;
	}


	</style>
</head>
<body>
	<div class="all">
		<ul class="options">
			<li class="active">社会新闻</li>
			<li >体育新闻</li>
			<li>娱乐新闻</li>
			<li>金融新闻</li>
			<li>科技新闻</li>
			<li>汽车新闻</li>
		</ul>
		<ul class="card">
			<li class="active">科技新闻 的内容</li>
			<li >体育新闻 的内容</li>
			<li>娱乐新闻 的内容</li>
			<li>金融新闻 的内容</li>
			<li>科技新闻 的内容</li>
			<li>汽车新闻 的内容</li>
		</ul>
	</div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	//获取页面中所有得选项 绑定点击事件
	$('.options li').click(function(){
		//给当前点击的选项添加active类,给其它同辈元素移除active类
		$(this).addClass('active').siblings().removeClass('active');
		// 在jquery中提供一个方法 index 代表当前元素的索引
		var n = $(this).index();
		//找到对应的卡片,添加类,其它的移除类
		$('.card li').eq(n).addClass('active').siblings().removeClass('active');
	})

	</script>
</body>
</html>
```

### 5.5.4二级菜单

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>二级菜单</title>
	<style type="text/css">
	ul,li,h3{
		margin: 0;
		padding: 0;
		list-style:none;
	}

	li{
		width: 100px;
		height: 50px;
		text-align:center;
		line-height:50px;
		border:1px solid red;
		position: relative;
	}

	.ops{
		width: 300px;
		height: 500px;
		border:1px solid red;
		position: absolute;
		top:0px;left:100px;
		display: none;
	}

	.ops li{
		width: 100px;
		height: 100px;
		background: #369;
		margin: 10px;
		float: left;
	}



	</style>
</head>
<body>
	<div class="all">
		<ul>
			<li>
				<h3>手机</h3>
				<div class="ops">
					<ul>
						<li>一加手机</li>
						<li>锤子手机</li>
						<li>小辣椒手机</li>
						<li>苹果手机</li>
						<li>小米手机</li>
						<li>金立手机</li>
					</ul>
				</div>
			</li>
			<li>
				<h3>电脑</h3>
				<div class="ops">
					<ul>
						<li>一加 电脑</li>
						<li>锤子 电脑</li>
						<li>小辣椒 电脑</li>
						<li>苹果 电脑</li>
						<li>小米 电脑</li>
						<li>金立 电脑</li>
					</ul>
				</div>
			</li>
			<li>
				<h3>电视</h3>
				<div class="ops">
					<ul>
						<li>一加 电视</li>
						<li>锤子 电视</li>
						<li>小辣椒 电视</li>
						<li>苹果 电视</li>
						<li>小米 电视</li>
						<li>金立 电视</li>
					</ul>
				</div>
			</li>
		</ul>
	</div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">



	//鼠标移入 事件  mouseover
	$('.all li').mouseover(function(){
		$(this).find('.ops').css('display','block')
	})
	//鼠标移出 事件  mouseout
	$('.all li').mouseout(function(){
		$(this).find('.ops').css('display','none')
	})

	</script>
</body>
</html>
```



### 5.5.5鼠标事件

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>鼠标事件</title>
	<style type="text/css">
		.move{
			width: 150px;
			height: 150px;
			background: #369;
		}

		body{
			height: 3000px;
		}

	</style>
</head>
<body>
	<div class="move"></div>
	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">


	/*
		click() 单击事件
		dblclick() 双击事件
		mouseover() 鼠标移入事件
		mouseout() 鼠标移出事件
		mouseup() 鼠标抬起
		mousedown() 鼠标按下
		mousemove() 鼠标移动

		在所有的鼠标事件中都可以获取鼠标位置
		在事件的函数中传递一个 事件对象 event e
		clientX,clientY
		pageX,pageY
	*/ 

	// hover() 鼠标悬停
		// $('.move').hover(function(){
		// 	//鼠标移入事件
		// 	console.log('over');
		// },function(){
		// 	//鼠标移除事件
		// 	console.log('out');
		// })
	
	// $(window).mousedown(function(){
	// 	console.log('down')
	// })
	// $(window).mouseup(function(){
	// 	console.log('up')
	// })


	$(window).mousemove(function(e){
		//获取鼠标位置 相对的是浏览器窗口
		var x1 = e.clientX;
		var y1 = e.clientY;
		console.log('client:'+x1,y1);


		//获取鼠标位置  相对的是 文档     文档比窗口大多了
		var x2 = e.pageX;
		var y2 = e.pageY;
		console.log('page:'+x2,y2);

	})
  // 通过点击鼠标获取鼠标的位置 相对于浏览器窗口

	$(window).click(function(e){
		var x = e.clientX;
		var y = e.clientY;
		// console.log(x,y);
	})


	// oncontextmenu 鼠标右键菜单事件  原生js (javascript)

	window.oncontextmenu = function(){
		console.log('你右键了谁');

		// return false;
	}




	</script>
</body>
</html>
```



### 5.5.6鼠标移动DIV

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>鼠标移动div</title>

	<style type="text/css">
	#move{
		width: 150px;
		height: 150px;
		background: #369;
		position: absolute;
	}


	</style>
</head>
<body>
	<div id="move"></div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">


	//鼠标按下事件
	$('#move').mousedown(function(e){
		//获取当前鼠标按下时的位置
		var x = e.clientX;
		var y = e.clientY;

		//获取当前元素的位置
		var t = $(this).offset().top;

		var l = $(this).offset().left;


		//绑定鼠标移动事件
		$(window).mousemove(function(e){
			//获取鼠标移动时的位置
			var mx = e.clientX;
			var my = e.clientY;

			//计算位置
			var newT = my - y + t;
			var newL = mx - x + l;

			//给元素设置位置
			$('#move').css({top:newT+'px',left:newL+'px'})
		})
	})

	//鼠标抬起事件
	$('#move').mouseup(function(){
		//清除元素的移动事件
		$(window).unbind('mousemove')
	})

	</script>
</body>
</html>
```



### 5.5.7键盘移动DIV

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>键盘控制div移动</title>
	<style type="text/css">
	#move{
		width: 150px;
		height: 150px;
		background: #369;
		position: absolute;
	}


	</style>
</head>
<body>
	<div id="move"></div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	// 扩展 既能鼠标移动.又可以键盘移动


	//全局变量
	// 这个是控制移动时候的像素   相当于视野中看的速度
	var step = 20;


	//绑定键盘事件
	$(window).keydown(function(e){
		//获取按键信息
		var k = e.keyCode;
		console.log(k);
		//判断
		switch(k){
			//当获取的按键asci码为87 和38的时候 向上移动!
			case 87:
			case 38:
				moveUp();
				break;
			case 83:
			case 40:
				moveDown();
				break;
			case 37:
			case 65:
				moveLeft();
				break;
			case 39:
			case 68:
				moveRight();
		}
	})

	//封装函数
	function moveDown(){
		//获取当前元素距离文档顶部偏移量 + step
		var top = $('#move').offset().top;

		//计算新的top  +上像素是往下移动
		var newTop = top+step;

		//设置新的top
		$('#move').css('top',newTop+'px');
	}


	//封装函数
	function moveUp(){
		//获取当前元素距离文档顶部偏移量 + step
		var top = $('#move').offset().top;

		//计算新的top  减去像素是往上移动
		var newTop = top-step;
		// 往上移动的时候如果新的文档偏移量为负值  就相当于是移动没了  让他定格在文档最上面 所以加上判断条件
		if(newTop <= 0){
			newTop = 0;
		}

		//设置新的top
		$('#move').css('top',newTop+'px');
	}



	//封装函数
	function moveRight(){
		//获取当前元素距离文档左侧偏移量 + step
		var top = $('#move').offset().left;

		//计算新的top
		var newTop = top+step;

		//设置新的top
		$('#move').css('left',newTop+'px');
	}


		//封装函数
	function moveLeft(){
		//获取当前元素距离文档左侧偏移量 + step
		var top = $('#move').offset().left;

		//计算新的top
		var newTop = top-step;
		if(newTop <= 0){
			newTop = 0;
		}


		//设置新的top
		$('#move').css('left',newTop+'px');
	}





	</script>
</body>
</html>
```

### 5.5.8多级联动

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>多级联动</title>
</head>
<body>
	<select name="" id="sheng">
		<option value="">--请选择省--</option>
	</select>
	<select name="" id="shi">
		<option value="">--请选择市--</option>
	</select>
	<select name="" id="xian">
		<option value="">--请选择县--</option>
	</select>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	//定义数据 省 市
	var ss = {};
	ss['山东'] = ['济南','济宁'];
	ss['山西'] = ['太原','大同'];
	ss['河南'] = ['洛阳','驻马店'];
	ss['河北'] = ['石家庄','保定'];

	// console.log(ss);

	//定义 市 县
	var sx = {};
	sx['济南'] = ['济南1区','济南2区','济南3区'];
	sx['济宁'] = ['汶上县','梁山县','兖州区'];
	sx['太原'] = ['杏花岭区','迎泽区','小店区'];
	sx['大同'] = ['大同1区','大同2区','大同3区'];
	sx['洛阳'] = ['龙门区','洛城区','回族区'];
	sx['驻马店'] = ['驻马店1区','驻马店2区','驻马店3区'];
	sx['石家庄'] = ['石家庄1区','石家庄2区','石家庄3区'];
	sx['保定'] = ['保定1区','保定2区','保定3区'];

	function init(){
		// 这个是默认给加上去的  提示 
		var str = '<option value="">--请选择省--</option>';
		for(var i in ss){
			// 把遍历的值给加入到上面的标签中
			str += '<option value="'+i+'">'+i+'</option>'
		}
		//赋值
		$('#sheng').html(str);
	}
	init();


	//给省绑定 change事件
	$('#sheng').change(function(){
		//获取当前选择的省
		var v = $(this).val();
		// ss[v]是省这个属性里面的值    是市
		var s = ss[v];
		var str = '<option value="">--请选择市--</option>';
		for(var i in s){
			//遍历之后的值给驾到选项条中的标签上
			//value 里面的值 是我选上的时候 触发change 事件
			str += '<option value="'+s[i]+'">'+s[i]+'</option>'
			// console.log(i);
		}
		//赋值 把所选的市给放到上面显示了
		$('#shi').html(str);
	})



	//给市绑定 change事件
	$('#shi').change(function(){
		//获取当前选择的市
		var v = $(this).val();
		var p = sx[v];
		// console.log(p);
		var str = '<option value="">--请选择县--</option>';
		for(var i in p){
			str += '<option value="'+p[i]+'">'+p[i]+'</option>'
			// console.log(i);
		}
		//赋值 把县给放上去了
		$('#xian').html(str);
	})
	
	




	</script>
</body>
</html>
```

### 5.5.9节点操作

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>节点操作</title>
	<style type="text/css">
	.all{
		width: 500px;
		height: 500px;
		border:1px solid blue;
	}

	.item{
		width: 100px;
		height: 100px;
		border-radius:50%;
		background: #909;
		float: left;
	}

	.w{
		width: 200px;
		height: 100px;
		background: #909;
	}


	</style>
</head>
<body>
	<button>在元素的内部尾部添加一个元素</button>
	<button>在元素的内部头部添加一个元素</button>
	<button>在元素的外部之后添加一个元素</button>
	<button>在元素的外部之前添加一个元素</button>
	<button>清空所有元素</button>
	<button>删除第一个子元素</button>
	<button>克隆最后一个元素插入到最前面</button>
	<div class="all"></div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	//绑定单击事件
	$('button').eq(0).click(function(){
		// $('.all').html('<div class="item">1</div>');
		var newDiv = CreateDiv();

		//把创建的元素 追加到标签中
		// $('.all').append(newDiv)
		newDiv.appendTo('.all')
	})

	$('button').eq(1).click(function(){
		//创建元素
		var newDiv = CreateDiv();

		//把元素插入到头部
		$('.all').prepend(newDiv)

	})

	$('button').eq(2).click(function(){
		//创建元素
		var newDiv = $('<div class="w"></div>');
		//添加到元素的外部的尾部,在这个元素的后面添加一个元素
		$('.all').after(newDiv);
	})

	$('button').eq(3).click(function(){
		//创建元素
		var newDiv = $('<div class="w"></div>');
		//添加到元素的外部的尾部,在这个元素的后面添加一个元素
		$('.all').before(newDiv);
	})

	$('button').eq(4).click(function(){
		//清空
		$('body').empty();
	})


	$('button').eq(5).click(function(){
		//清空
		$('.all .item').eq(0).remove();
	})


	$('button').eq(6).click(function(){
		//克隆 clone(true) 如果有参数true代表克隆所有,包括事件
		var d = $('.all .item:last').clone(true);
		$('.all').prepend(d)
	})


	//给所有class=item的元素绑定单击事件
	// $('.item').click(function(){
	// 	alert(2);
	// })

	$('.item').live('click',function(){
		//confirm()弹出一个带提醒信息的确认框,如果点击确认返回true,
		var res = confirm('您确认要删除当前元素吗?');
		if(res){
			$(this).remove();
		}
		console.log(res);
	})



	function CreateDiv(){
		//创建节点 标签  元素
		// 创建了一个元素  自带<span标签
		var nd = $('<div class="item"><span>love</span></div>');
		nd.css('background','rgb('+rand(0,255)+','+rand(0,255)+','+rand(0,255)+')');

		//绑定事件
		// nd.click(function(){
		// 	alert(1);
		// })

		//返回div
		return nd;
	}


	//封装随机函数
	function rand(m,n){
		return Math.floor(Math.random()*(n-m+1))+m;
	}

	</script>
</body>
</html>
```



### 5.6.0操作元素特效

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>特效</title>
	<style type="text/css">
	

	.item{
		width: 500px;
		height: 500px;
		background: #369;
		position: absolute;
	}


	</style>
</head>
<body>
	<button>显示</button>
	<button>隐藏</button>
	<button>切换</button>
	<button>自定义动画</button>
	<button>stop</button>
	<div class="item"></div>


	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript" src="jquery-color.js"></script>
	<script type="text/javascript">

    // 不加隐藏的话一直显示
	$('button').eq(0).click(function(){
		// $('.item').show();
		// $('.item').slideDown(2000,function(){
		// 	alert('显示完毕');
		// });
		$('.item').fadeIn();
	})
  
	$('button').eq(1).click(function(){
		// $('.item').hide();
		// $('.item').slideUp(2000,function(){
		// 	alert('隐藏完毕');
		// });
		$('.item').fadeOut();

	})

	$('button').eq(2).click(function(){
		// $('.item').toggle(2000);
		// $('.item').toggle(2000,function(){
		// 	alert('哇哦');
		// });

		// $('.item').slideToggle();
		$('.item').fadeToggle(2000);
	})

	// 推迟两千毫秒 开始这个动画

	$('button').eq(3).click(function(){
		$('.item').delay(2000).animate({
			width:'100px',
			height:'100px',
			top:'200px',
			left:'550px',
			borderRadius:'50%',
			backgroundColor:'#909'
		},3000)
	})

  // k可以中间叫停
	$('button').eq(4).click(function(){
		$('.item').stop();
	})

	</script>
</body>
</html>
```

### 5.6.1楼层导航

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>楼层导航</title>
	<style type="text/css">

	body,ul,li{
		margin: 0;
		padding: 0;
		list-style:none;
	}
		
	#f1{height: 900px;background: #909;}
	#f2{height: 920px;background: #963;}
	#f3{height: 950px;background: #369;}
	#f4{height: 900px;background: #710;}
	#f5{height: 950px;background: #936;}
	#f6{height: 980px;background: #360;}
	#f7{height: 900px;background: #520;}
	/*给导航这个快进行绝对定位*/

	#dh{
		width: 80px;
		position: fixed;
		top:200px;left:10px;
	}
	 /*给导航这个快里的li  和这个返回顶部这个div 进行设置*/

	#dh li,#dh div{
		height: 50px;
		background: #918888;
		color:#fff;
		line-height:50px;
		text-align:center;
		border-bottom:1px solid #f5f5f5;
		/*鼠标移入会产生小手指的样式*/
		cursor:pointer
	}
	/*导航栏里的一个li设置背景颜色*/

	#dh .cur{
		background: #f39;
	}
	

	</style>
	
</head>
<body>
<!-- 7个楼  -->
	<div id="f1">一楼</div>
	<div id="f2">二楼</div>
	<div id="f3">三楼</div>
	<div id="f4">四楼</div>
	<div id="f5">五楼</div>
	<div id="f6">六楼</div>
	<div id="f7">七楼</div>
	<!-- dh这一整块是固定在左侧的导航  -->
	<div id="dh">
		<ul>
			<li class="cur">一楼</li>
			<li>二楼</li>
			<li>三楼</li>
			<li>四楼</li>
			<li>五楼</li>
			<li>六楼</li>
			<li>七楼</li>
		</ul>
		  <!-- 这个是和7楼底下的返回顶部 -->
		<div>返回顶部</div>
	</div>

	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">


	// 返回顶部   给返回顶部绑定一个单击事件
	$('#dh div').click(function(){
			// 点击他之后  让他动画到这个顶部   0是时间 在多久能完成
		$('html,body').animate({scrollTop:'0px'},0)
	})

	//给楼层号绑定单击事件 跳转到对应楼层
	$('#dh li').click(function(){
		//获取当前点击的楼层号 因为索引是从0开始的 所以后面要+1  div的索引 和li的索引是一样的	
		//这个li的索引是从0开始的 给这个li的索引加1 这样和div的索引是一样的  通过这个div的距离顶部的高度来跳转
		var inx = $(this).index()+1;
		//获取当前楼层距离文档顶部偏移量   文档顶部就是华东的越多 距离越多
		var top = $('#f'+inx).offset().top;
		//设置  获取完了之后  直接给他已动画的形式设置到这个距离
		$('html,body').animate({scrollTop:top+'px'},1500)
	})



 // 这一步是要把这个窗口 跟随着滚动的位置显示导航左侧要显示的变色  和所在的是哪一个楼层!!
	//给浏览器绑定 文档滚动事件 scroll
	$(window).scroll(function(){
		//获取当前文档的滚动距离
		var top = $(document).scrollTop();
		//获取所有楼层距离文档顶部距离
		var f1 = $('#f1').offset().top;
		var f2 = $('#f2').offset().top;
		var f3 = $('#f3').offset().top;
		var f4 = $('#f4').offset().top;
		var f5 = $('#f5').offset().top;
		var f6 = $('#f6').offset().top;
		var f7 = $('#f7').offset().top;
		// 如果滚动的距离大于楼层距离文档顶部的距离  那么就给同辈清除 给自己加上! -200是相当于让他提前到这个楼层了显示的能快一些

		if(top >= f1){ $('#dh li').eq(0).addClass('cur').siblings().removeClass('cur') }
		if(top >= f2 - 200){ $('#dh li').eq(1).addClass('cur').siblings().removeClass('cur') }
		if(top >= f3 - 200){ $('#dh li').eq(2).addClass('cur').siblings().removeClass('cur') }
		if(top >= f4 - 200){ $('#dh li').eq(3).addClass('cur').siblings().removeClass('cur') }
		if(top >= f5 - 200){ $('#dh li').eq(4).addClass('cur').siblings().removeClass('cur') }
		if(top >= f6 - 200){ $('#dh li').eq(5).addClass('cur').siblings().removeClass('cur') }
		if(top >= f7 - 200){ $('#dh li').eq(6).addClass('cur').siblings().removeClass('cur') }
	})

	</script>
</body>
</html>
```

### 5.6.2滚动栏

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>滚动栏</title>
	<style type="text/css">
	body,ul,li{
		margin: 0px;
		padding: 0px;
		list-style: none;
	}
	/*给这个块进行设置*/
	
	.all{
		
		width: 600px;
		height: 300px;
		/*border: 1px solid #242429;*/
		margin: 100px auto;
		/*超出这个块的内容给隐藏*/
		overflow: hidden;

	}
	/*li 这个标签里面的每一个都各占一排在这个块中*/
	li{ 
		/*可以加个边框来看*/
		/*border:1px solid #242429; */
		background: #4652DE;
		
		width:600px;
		height: 300px;
		text-align:center;
		line-height: 300px;
		font-family: '宋体';
		font-size: 50px;
	/*	overflow: hidden;*/
		color:red;
		margin: 0px auto;


	}

	body{
		background:#670301;
	}
	
	</style>
</head>
<body>
   <div class="waimian">
    <div class="all">
    <!-- ul li标签 竖着显示 -->
    	<ul>
		   <li>无限极</li>
		   <li>高级业务总监:高淑芹女士</li>
		   <li>高级业务经理:高淑英女士</li>
		   <li>IT总监:刘公伯先生</li>
		   <li>百信药行老板:李姗姗女士</li>
		   <li>本田CRV车主:高金宝先生</li>
    	</ul>
    </div>
   </div>
    <script type="text/javascript" src="jquery-1.8.3.min.js"></script>
    <script type="text/javascript">
    // alert($)
     setInterval(function(){
     	//找到页面all中第一个li  让他开始滚动  这个时间是滚动的效果时间
     	$('.all li:first').slideUp(500,function(){
     			//把这个li给追加到ul后面
     		$(this).appendTo('.all ul').show()
     	})
     	// 定时器的时间
     },2500)

    </script>
	
</body>
</html>
```



### 5.6.3 轮播版本(1) 先布的局

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>轮播版本1.0 先布的局</title>
	<style type="text/css">
		body,ul,li{
			margin: 0;
			padding: 0;
			list-style:none;
		}
		/*给banner图的区域固定一下*/
		#banner{
			width: 1190px;
			height: 410px;
			margin: 100px auto;
			overflow: hidden;
			position: relative;
		}
		/*这给多余的图片隐藏 li是控制图片的 */
		.imgs li{
			width: 1190px;
			height: 410px;
			display: none;
		}

		/*是控制里面的按钮的类*/
		.num{ 
			width: 100%;
			/*给他绝对定位 就要给他的父级来个相对定位*/
			position: absolute;
			bottom:5px;
			text-align:center;
		}

		/*这个是设置按钮的一系列操作*/
		.num li{
			width: 10px;
			height: 10px;
			border-radius:50%;
			display: inline-block;
			background: #fff;
			margin: 0 5px;
			cursor:pointer;
		}
				/*控制按钮  */
		.btn{
			position: absolute;
			top:45%;
			width: 50px;
			height: 50px;
			text-align:center;
			font-size:50px;
			color:#fff;
			font-family:'宋体';
			cursor:pointer;
		}

			/*控制左侧的按钮*/
		.btn_l{
			left:2px;
		}
		/*控制右侧的按钮*/
		.btn_r{
			right:2px;
		}
		/*给底下的按钮一个颜色*/
		.num .cur{
			background: #f39;
		}


	</style>
</head>
<body>
   <div id="banner">
   	<!-- 控制图片 -->
	 <ul class="imgs">
	 <!-- 这里让他先出现一个图片 -->
	 	<li style="display: block;"><img src="./bannerImg/001.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/002.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/003.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/004.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/005.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/006.jpg" width="100%"></li>
	</ul>
	<!-- 控制底下小圆点 -->
	<ul class="num">
		<li class="cur"></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
	</ul>
	<!-- 左右的按钮 -->
	
	<div class="btn  btn_l">&lt;</div>
	<div class="btn  btn_r">&gt;</div>


   </div>
	
</body>
</html>
```

### 5.6.3轮播版本(2)轮播版本2.能切换 但不带动画 底下小点也跟着动

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>轮播版本2.0 实现能切换 但是不带动画 底下小点也跟着动 </title>
	<style type="text/css">
		body,ul,li{
			margin: 0;
			padding: 0;
			list-style:none;
		}
		/*给banner图的区域固定一下*/
		#banner{
			width: 1190px;
			height: 410px;
			margin: 100px auto;
			overflow: hidden;
			position: relative;
		}
		/*这给多余的图片隐藏 li是控制图片的 */
		.imgs li{
			width: 1190px;
			height: 410px;
			display: none;
		}

		/*是控制里面的按钮的类*/
		.num{ 
			width: 100%;
			/*给他绝对定位 就要给他的父级来个相对定位*/
			position: absolute;
			bottom:5px;
			text-align:center;
		}

		/*这个是设置按钮的一系列操作*/
		.num li{
			width: 10px;
			height: 10px;
			border-radius:50%;
			display: inline-block;
			background: #fff;
			margin: 0 5px;
			cursor:pointer;
		}
				/*控制按钮  */
		.btn{
			position: absolute;
			top:45%;
			width: 50px;
			height: 50px;
			text-align:center;
			font-size:50px;
			color:#fff;
			font-family:'宋体';
			cursor:pointer;
		}

			/*控制左侧的按钮*/
		.btn_l{
			left:2px;
		}
		/*控制右侧的按钮*/
		.btn_r{
			right:2px;
		}
		/*给底下的按钮一个颜色*/
		.num .cur{
			background: #f39;
		}


	</style>
</head>
<body>
   <div id="banner">
   	<!-- 控制图片 -->
	 <ul class="imgs">
	 <!-- 这里让他先出现一个图片 -->
	 	<li style="display: block;"><img src="./bannerImg/001.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/002.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/003.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/004.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/005.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/006.jpg" width="100%"></li>
	</ul>
	<!-- 控制底下小圆点 -->
	<ul class="num">
		<li class="cur"></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
	</ul>
	<!-- 左右的按钮 -->
	
	<div class="btn  btn_l">&lt;</div>
	<div class="btn  btn_r">&gt;</div>
		


   </div>
 <script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

		//全局变量 相当于索引值
	var i = 0; 

	//绑定左右按钮事件
	$('.btn_r').click(moveRight);
	$('.btn_l').click(moveLeft);

	//启动定时器 自动运行
	var init = setInterval(moveRight,2000)

	//鼠标悬停
	 //移入  移出 移入清除定时器  
	$('#banner').hover(function(){
		//清除定时器
		clearInterval(init);
	},function(){
		//重新启动定时器  重启之后还会返回一个变量 返回给上面 需要启动定时器来接受
		init = setInterval(moveRight,2000)
	})

	//给小圆点 绑定 单击事件
	$('.num li').click(function(){
		// 获取当前点击的索引 小圆点的索引
		i = $(this).index();
		$('.imgs li').eq(i).show().siblings().hide();
		$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');
	})


	//封装函数
	function moveRight(){
		i++;
		if(i == 6){
			i = 0;
		}
		//// i是上面图片的索引  li的索引 如果i等于6了  让他从0开始
		/// 因为最后一张的图片索引是5  也就是从第一张图片开始
		$('.imgs li').eq(i).show().siblings().hide();
			// 这个是底下的小园图标  让索引的变色   其他的移除变色
		$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');
	}

	//封装函数
	function moveLeft(){
		i--;
		//// i是上面图片的索引  li的索引 如果i等于-1 也就是从第一张图片向左移动了  
		///这个索引就变成-1了 让他变成第6张图片 /也就是i=5的那张
		if(i == -1){
			i = 5;
		}

		$('.imgs li').eq(i).show().siblings().hide();
		$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');
	}


	</script>
</body>
</html>
```

### 5.6.3轮播版本3.0 带动画轮播

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>轮播版本3.0 带动画轮播 </title>
	<style type="text/css">
		body,ul,li{
			margin: 0;
			padding: 0;
			list-style:none;
		}
		/*给banner图的区域固定一下*/
		#banner{
			width: 1190px;
			height: 410px;
			margin: 100px auto;
			overflow: hidden;
			position: relative;
		}
		/*给横着这些图片一个宽度 让他横着显示*/

		.imgs{
			width: 9000px;
			position: absolute;
		}
		/*这给多余的图片隐藏 li是控制图片的 */
		.imgs li{
			width: 1190px;
			height: 410px;
			/*display: none;*/
			/*让这些图片进行漂浮*/
			float: left;
		}

		/*是控制里面的按钮的类*/
		.num{ 
			width: 100%;
			/*给他绝对定位 就要给他的父级来个相对定位*/
			position: absolute;
			bottom:5px;
			text-align:center;
		}

		/*这个是设置按钮的一系列操作*/
		.num li{
			width: 10px;
			height: 10px;
			border-radius:50%;
			display: inline-block;
			background: #fff;
			margin: 0 5px;
			cursor:pointer;
		}
				/*控制按钮  */
		.btn{
			position: absolute;
			top:45%;
			width: 50px;
			height: 50px;
			text-align:center;
			font-size:50px;
			color:#fff;
			font-family:'宋体';
			cursor:pointer;
		}

			/*控制左侧的按钮*/
		.btn_l{
			left:2px;
		}
		/*控制右侧的按钮*/
		.btn_r{
			right:2px;
		}
		/*给底下的按钮一个颜色*/
		.num .cur{
			background: #f39;
		}


	</style>
</head>
<body>
   <div id="banner">
   	<!-- 控制图片 -->
	 <ul class="imgs">
	 <!-- 这里让他先出现一个图片 -->
	 	<li style="display: block;"><img src="./bannerImg/001.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/002.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/003.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/004.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/005.jpg" width="100%"></li>
	 	<li><img src="./bannerImg/006.jpg" width="100%"></li>
	</ul>
	<!-- 控制底下小圆点 -->
	<ul class="num">
		<li class="cur"></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
	</ul>
	<!-- 左右的按钮 -->
	
	<div class="btn  btn_l">&lt;</div>
	<div class="btn  btn_r">&gt;</div>
		


   </div>
 <script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

		//全局变量 相当于索引值
	var i = 0; 

	//无缝轮播
	//克隆第一张图片给放到最后
	 var nli=$('.imgs li:first').clone(true);
	 $('.imgs').append(nli)

	//绑定左右按钮事件
	$('.btn_r').click(moveRight);
	$('.btn_l').click(moveLeft);

	//启动定时器 自动运行
	var init = setInterval(moveRight,2000)

	//鼠标悬停
	 //移入  移出 移入清除定时器  
	$('#banner').hover(function(){
		//清除定时器
		clearInterval(init);
	},function(){
		//重新启动定时器  重启之后还会返回一个变量 返回给上面 需要启动定时器来接受
		init = setInterval(moveRight,2000)
	})

	//给小圆点 绑定 单击事件
	$('.num li').click(function(){
		//获取当前点击的索引
		i = $(this).index();

		// 新的距离文档距离  因为图片宽度是1990
		 //i*这个宽度 是点击第几张图片 从而获得的宽度 之后  结果为负的是因为往左移动
		 //图片都移动到左面去了  相对于现在这个ul 里的位置 这个位置一直没变这个位置就是0 所以是负 的 
		var newLeft = i*1190;
		$('.imgs').stop().animate({left:-newLeft+'px'},800)
		$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');
	})


	//封装函数
	function moveRight(){
		i++;
		// 现在是6张图片  如果是第七张图片  则让他变成第一张 也就是通过改变他的索引
		 
		if(i == 7){
			//用css把ul快速定位到0px;
			$('.imgs').css('left','0px');
			i = 1;
		}
		var newLeft = i*1190;
		// 让他已动画的方式移动到他的距离
		$('.imgs').stop().animate({left:-newLeft+'px'},800)
		//这是给小圆点  移动到这了的时候给小圆点加上这个颜色  其他的移除
		if(i == 6){
			$('.num li').eq(0).addClass('cur').siblings().removeClass('cur');
		}else{
			$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');
		}
	}
	//封装函数
	function moveLeft(){
		i--;
		if(i == -1){
			// i = 5;
			//把ul定位到最后一张
			$('.imgs').css('left',-6*1190+'px')
			i = 5;
		}
		var newLeft = i*1190;
		$('.imgs').stop().animate({left:-newLeft+'px'},800)
		$('.num li').eq(i).addClass('cur').siblings().removeClass('cur');

	}


	</script>
</body>
</html>
```



### 5.7放大镜

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>放大镜 版本2.0 往放大镜里面加入了一个指定的放大镜</title>
	<style type="text/css">
	.small{
		/*我现在给了一个400*400的块*/
		/*这个图正常是1000成1000的 
		 我现在让他以高和宽各400百分之百的占据我这个div 
		 我给他加上宽度100%他就完全占据我这个div了*/

		width: 400px;
		height: 400px;
		/*之后给这个块进行绝对定位让他移动个位置*/
		position: absolute;
		/*绝对定位不占据我原先的位置*/
		top: 100px;left: 100px;

	}
/*我给了一个高400 宽400的块的定了个位置*/
	.big{
		width: 400px;
		height: 400px;
		position: absolute;
		/*正好让他在这个原图的右面*/
		top: 100px; left: 510px;
		/*这个块元素下的img会超出他这个块 所以给他的父类加上一个隐藏溢出的部分*/
		overflow: hidden;
	/*不让他这个元素下的这个块显示 把他隐藏*/
		display: none;


	}
	body,ul,li{
		margin: 0;
		padding: 0;
		list-style: none;
	}
	ul{
		width: 400px;
		height: 400px;
		/*border 方便看距离*/
		/*border: 1px solid red;*/
		/*给ul定位到被放大的图底下去*/
		position: absolute;
		top: 510px;left: 100px;

	}
	li{
		/*给这里面的li加上高度和宽度 想在底下显示的*/
	  width: 80px;
	  height: 80px;
	  float: left;
	  margin-right:  10px;
	  border:1px dashed blue;
	}

		.move{width: 100px;
			height: 100px;
			background: url(./images/bg.png);
			position: absolute;
			top:0px;left: 0px;
			/*让他消失  一入进来的时候才显示*/
			display: none;

	</style>
}
</head>
<body>
	<div class="small">
		<img  class="simg" src="./images/2.jpg" width="100%">
		<!-- 这个是里面的那个来回移动的放大镜 -->
		<div class="move"></div>
	</div>
	<div class="big">
		<img  class="bimg" src="./images/2.jpg">
	</div>
	<!-- 往这个图片的底部加了两个小图片  为了点击更换 -->
	<ul class="imgs">
		<li><img src="./images/2.jpg"  width="100%"></li>
		<li><img src="./images/3.jpg"  width="100%"></li>
	</ul>
	<script type="text/javascript" src="jquery-1.8.3.min.js"></script>
	<script type="text/javascript">
	// 同时绑定三个事件
	// 鼠标移入 , 
	 $('.small').mouseover(function(){
	 	// 鼠标移入的时候 显示放大图片
	 	$('.big').show();
	 }).mouseout(function(){
	 	// 鼠标移出的时候  隐藏这个放大的图片
	 	$('.big').hide();
	 	// 计算当前鼠标在元素内移动的距离
	 }).mousemove(function(){
	 	// 鼠标当前的位置-当前元素距离文档的偏移量
	  var moveLeft=e.clientX-$(this).offset.left;
	  var moveTop=e.clientY-$(this).offset.top;
	  // 计算 大图移动的距离
	  // 因为小图是你原图缩小的2.5倍  所以大图要乘以2.5 为了让他上正中心 所以剪掉200
	   var newLeft =moveLeft*2.5 -200
	   //设置大图的移动
	   $('.bimg').css({top:-newTop+'px',left:-newLeft+'px'})
	 })



  // 这里实现功能
   //绑定三个时间
    $('.small').mouseover(function(){
		//鼠标移入时 显示放大图片
		$('.big').show();
		$('.move').show();
	// 计算小div的高  就是移入进去显示的这个块
	// 这个小块是外面被放大的块 他们之间相等  但和原图有比例关系
	// 这个放大的图片宽度	 除以这个原图的宽度 得到的百分比 在乘以被缩小的原图图片就是这个宽度了
	 var w  =$('.big').width()/$('.bimg').width()*$('.small').width();
	 var h = $('.big').height()/$('.bimg').height() * $('.small').height();
	// 这个元素的宽度和高度出来了
	$('.move').width(w);
	$('.move').height(h);
	}).mouseout(function(){
		//鼠标移除时 隐藏放大镜
		$('.big').hide();
		$('.move').hide();
	}).mousemove(function(e){
		//获取当前鼠标的位置
		var x = e.clientX;
		var y = e.clientY;

		//获取当前small元素距离文档顶部偏移
		var top = $('.small').offset().top;
		var left = $('.small').offset().left;

		//计算当前move元素移动距离
		var newLeft = x-left- ($('.move').width()/2);
		var newTop = y -top- ($('.move').height()/2);
		//越界判断 是看里面的元素移动到相对他父级的位置 让他不能越界 的距离
		if(newTop <= 0){ newTop = 0 }
		var	MaxTop = $('.small').height()-$('.move').height();
		if(newTop >= MaxTop){newTop = MaxTop}
		if(newLeft <= 0){ newLeft = 0}
		var MaxLeft = $('.small').width()-$('.move').width();
		if(newLeft>=MaxLeft){ newLeft = MaxLeft}

		//设置小div move移动
		$('.move').css({top:newTop+'px',left:newLeft+'px'})

		//计算放大镜移动的距离
		var bigTop = newTop*2.5;
		var bigLeft = newLeft*2.5;

		$('.bimg').css({top:-bigTop+'px',left:-bigLeft+'px'})
})
  	$('.imgs li').click(function(){
  		// 获取当前点击的图片src属性
  		// 通过li 找到img的属性 路径 给个变量
  		var s=$(this).find('img').attr('src')
  		// 把这个属性给.simg 把这个属性给.bimg
  		$('.simg').attr('src',s)
  		$('.bimg').attr('src',s)
  	})
	</script>
</body>
</html>
```
## 6. ajax的基本使用

1.get请求 显示携带参数 访问时 浏览器限制他携带参数的长度

//绑定单击事件

$('button').eq(0).click(function(){

//发送ajax请求,参数1:请求url地址 参数2:请求时携带的参数 参数3:回调函数,请求成功后的处理方法

$.get('/cgi-bin/2.py',{name:'admins'},function(data){

//参数4,限制返回的数据格式 为json格式,如果返回的是jso格式,直接eval转完,如果返回的不是json格式,进不到回调函数了

},'json')

});

**2.post请求 不显示参数信息 并且携带量大 服务器接收他的参数**

//绑定单击事件

$('button').eq(0).click(function(){

//发送ajax请求,参数1:请求url地址 参数2:请求时携带的参数 参数3:回调函数,请求成功后的处理方法

$.post ('/bin/2.py',{name:'admins'},function(data){

//参数4,限制返回的数据格式 为json格式,如果返回的是jso格式,直接eval转完,如果返回的不是json格式,进不到回调函数了

},'json')

}



ajax 请求

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>ajax的基本使用</title>
</head>
<body>
	<button>get请求</button>
	<button>post请求</button>
	<button>ajax请求</button>

	<script type="text/javascript" src="/public/js/jquery-1.8.3.min.js"></script>
	<script type="text/javascript">


	//绑定单击事件
	$('button').eq(0).click(function(){
		//发送ajax请求 参数1 请求的url地址  参数2 请求时携带的参数  参数3 回调函数,请求成功后的处理方法
		$.get('/cgi-bin/2.py',{name:'admins'},function(data){
			//data是服务器返回的数据
			// eval('var arr = '+data)
			console.log(data);
			// console.log(arr);
			
		},'json')
		//参数4 限制返回的数据格式 为json格式,如果返回的是json格式,直接eval转完,如果返回的不是json格式,进入不到回调函数
	})

	//绑定单击事件
	$('button').eq(1).click(function(){
		//发送ajax请求 参数1 请求的url地址  参数2 请求时携带的参数  参数3 回调函数,请求成功后的处理方法
		$.post('/cgi-bin/2.py',{name:'adminss'},function(data){
			//data是服务器返回的数据
			console.log(data);
		})
	})

	$('button').eq(2).click(function(){
		//发送ajax请求
		$.ajax({
			//请求的url地址
			url:'/cgi-bin/2.py',
			//请求的方式 get  post
			type:'GET',
			//传递的参数 
			data:{id:1,names:'zhangsan'},
			//返回的数据格式
			dataType:'json',
			//ajax请求成功后调用的函数
			success:function(data){
				console.log(data);
			},
			//ajax请求失败时执行的代码
			error:function(){
				console.log('ajax请求错误')
			},
			//是否异步 true 异步  false 同步 
			async:true,
			// //注意:异步,默认一般是,意思就是我这边ajax请求的过程中可以去做别的事情,不在这等他
			//  请求完毕,而同步是在执行请求的过程中需要等待请求完毕才走.
			//设置ajax请求超时时间 注意 请求超时时间只有在异步请求时才会生效
			timeout:2000

		})
	})
```

ajax例子删除操作

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<h3>用户列表</h3>
	<table border='1' width="600">
		<tr>
			<td>id</td>
			<td>用户名</td>
			<td>性别</td>
			<td>邮箱</td>
			<td>操作</td>
		</tr>
		<tr>
			<td>1</td>
			<td>admin</td>
			<td>男</td>
			<td>admin@qq.com</td>
			<td><a href="/cgi-bin/del.py?id=1">删除</a></td>
		</tr>
		<tr>
			<td>2</td>
			<td>张三</td>
			<td>男</td>
			<td>zhangsan@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>3</td>
			<td>李四</td>
			<td>男</td>
			<td>lisi@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>4</td>
			<td>wanwu</td>
			<td>男</td>
			<td>wangwu@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>5</td>
			<td>zhaoliu</td>
			<td>男</td>
			<td>zhaoliu@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>6</td>
			<td>李四</td>
			<td>男</td>
			<td>lisi@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>7</td>
			<td>wanwu</td>
			<td>男</td>
			<td>wangwu@qq.com</td>
			<td><a href="">删除</a></td>
		</tr>
		<tr>
			<td>8</td>
			<td>zhaoliu</td>
			<td>男</td>
			<td>zhaoliu@qq.com</td>
			<td>
				<a href="">删除</a>
			</td>
		</tr>
	</table>
	<script type="text/javascript" src="/public/js/jquery-1.8.3.min.js"></script>
	<script type="text/javascript">

	//给a标签绑定单击事件
	$('a').click(function(){
		//获取当前的用户id
		var uid = $(this).parents('tr').find('td').eq(0).text();
		// alert(uid);
		var a = $(this);
		//发送ajax请求 给del.py  把uid传递过去
		$.get('/cgi-bin/del.py',{id:uid},function(data){
			if(data == 0){
				alert('删除成功');
				// $(this).parents('tr').remove();//  X
				// console.log($(this));//此处的 $(this) 指向了ajax对象 XMLHttpRequest
				a.parents('tr').remove()
			}else{
				alert('删除失败')
			}
		})
		//阻止 a链接的默认行为
		return false;
	})


	</script>
</body>
</html>
```



# -----------------数据库------------------

# MySQL



使用方法:

​ 方式一: 通过图型界面工具,如 Navicat 等( 高级课使用 )

​ 方式二: 通过在命令行敲命令来操作 ( 基础阶段使用 )

 操作数据库的步骤

 连接, 打开库, 操作, 关闭退出



## 1.SQL语句中的快捷键

\G 格式化输出（文本式，竖立显示）

\s 查看服务器端信息

\c 结束命令输入操作

\q 退出当前sql命令行模式

\h 查看帮助

连接mysql: mysql -u root -p123456;



## 2.数据库操作

查看数据库 **show databases;**

创建数据库 **create database 库名 default charset=utf8;**

删除数据库 **drop database 库名;**

## 打开数据库 **use 库名;**

**数据导出**  **和   数据导入**

```
-- 将lamp138库导出
D:\>mysqldump -u root -p lamp138 >lamp138.sql
Enter password:
---- 将lamp138库中的stu表导出
D:\>mysqldump -u root -p lamp138 stu >lamp138_stu.sql
Enter password:
```

```
-- 将lamp138库导入
D:\>mysql -u root -p lamp138<lamp138.sql
Enter password:
-- 将lamp138库中stu表导入
D:\>mysql -u root -p lamp138 stu <lamp138_stu.sql
Enter password:
```

## 3.表操作增删改查

1.查看当前数据库下的所有表  **show tables;**

2.创建表  **create table 表名 (id int(10) unsigned auto_increment primary key,name varchar(255),pass varchar(255),email varchar(255),age int(10))engine=innodb default charset=utf8;**  //创建 表明  字段 类型 表引擎 字符集

3.查看表 **show tables;**

4.查看当前表中的所有数据 **select * from 表名**

5.添加数据 **insert into 表名(id,name,pass,email,age)values**

**(11,'zhangsan','123456','zs@qq.com',21);**

6.查看表结构 **desc 表名;**

7.查看建表语句 **show create table 表名; **

8.批量添加数据 **insert into表名(id,name,pass,email,age)values**

**(2,'李四','123456','zs@qq.com',21),**

(2,'李四','123456','zs@qq.com',21),

(2,'李四','123456','zs@qq.com',21),

(2,'李四','123456','zs@qq.com',21);

where条件

//带条件的删除 注意 delete from user是没有问题,它是删除当前user表中所有数据,一般情况需要指定条件删除

 9.删除 :**delete from  表名 where id=6;	**

10. 修改: **update 表名 set pass='22334455',email='tianqi@qq.com' where id =6;**

11.以格式化的数据 来进行显示 \G :**select * from 表名\G;** 

12.建表

```

create table user(
	// id 整型   不允许有符号  不允许空  主键自增
	id int unsigned not null AUTO_INCREMENT PRIMARY KEY,
	username varchar(30) not null,
	password char(32) not null,
	email varchar(100) not null,
	pic varchar(50) default './public/img/pic.jpg'
)engine=innodb default charset=utf8;
```



13.复制表结构

mysql> create table 目标表名 like 原表名;

复制表数据

mysql> insert into 目标表名 select * from 原表名;



## 4.添加字段操作

1.//在表中添加一个account 的字段  不允许为空 默认值为0

alter table user  add  account int not  null  default 0;

2.//在表中删除字段

alter table 表名 drop 字段名

3.//修改表中age字段的  类型 不修改字段名 

alter table user modify  age  tinyint unsigned not null default 21;

4.//修改表中account的字段名称和类型

alter table user change account num int not null default 0;



## 5 表的查询 和索引

统计当前表的数据总数
select count(*) from user;


提取一部分数据 limit   只提取前10条数据
select * from user limit 10;

 查询当前user表中所有数据(*) 按照 id 进行降序 排序后 提取10条
select * from user order by id desc limit 10;


 面试题  当前数据表中最大的id为20;删除了id为20 的数据,
 然后服务器重启之后,在当前表中重新添加一条数据,问添加的这条数据的id是多少?

  答案:当表引擎为 innodb 时  重启服务器后 最后添加的id是在现有的id最大的基础上自增 19+1
 当表引擎为myisam时 重启服务器后,被使用过的id记录依然存在,在原有基础上自增 20+1

表引擎的区别:

	myisam  由三个文件存储当前表  一个存表结构,一个存索引,一个存数据
	innodb  现在由两个文件组成  一个存表结构  另一个存索引和数据
	
	myisam 不支持 事务
	innodb 支持 事务
	
	myisam 相对速度快


1.添加普通索引 index
mysql> alter table user add index index_uname(username);
Query OK, 736 rows affected (0.19 sec)
Records: 736  Duplicates: 0  Warnings: 0

2.删除普通索引
mysql> alter table user drop index index_uname;
Query OK, 736 rows affected (0.08 sec)
Records: 736  Duplicates: 0  Warnings: 0


3.删除一个不存在的数据时  受影响行数为0
mysql> delete from user where id = 200;
Query OK, 0 rows affected (0.00 sec)


4.修改表名
mysql> alter table user rename as users;
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+---------------+
| Tables_in_py5 |
+---------------+
| users         |
+---------------+
1 row in set (0.06 sec)


5.重置表的自增值
mysql> alter table users auto_increment = 1;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0


-- 创建表 学员信息表
create table stu(
	id int unsigned not null AUTO_INCREMENT PRIMARY KEY,
	name varchar(30) not null,
	age int not null,
	sex enum('w','m','x')  not null default 'x',
	classid varchar(50) not null
)engine=innodb default charset=utf8;

-- 添加数据
insert into stu(name,age,sex,classid) values
	('zhangsan',20,'m','py1'),
	('lisi',20,'w','py1'),
	('wangwu',20,'m','py1'),
	('zhaoliu',20,'m','py2'),
	('tianqi',20,'w','py2'),
	('wangba',20,'w','py2'),
	('user1',20,'w','py1'),
	('user2',20,'w','py1'),
	('user3',20,'m','py1'),
	('user4',20,'m','py3'),
	('user5',20,'m','py3'),
	('user6',20,'w','py4'),
	('user7',20,'w','py4'),
	('user8',20,'w','py4'),
	('user9',20,'m','py4'),
	('user10',20,'m','py4'),
	('user11',20,'w','py5'),
	('user12',20,'m','py5'),
	('user13',20,'m','py5'),
	('user14',20,'w','py5'),
	('user15',20,'w','py5'),
	('user16',20,'m','py5');



-- 1. 查询班级为lamp138期的学生信息
mysql> select * from stu where classid='lamp138';

-- 2. 查询lamp138期的男生信息（sex为m）
mysql> select * from stu where classid='lamp138' and sex='m';

-- 3. 查询id号值在10以上的学生信息
mysql> select * from  stu where id>10;

-- 4. 查询年龄在20至25岁的学生信息
mysql> select * from stu where age>=20 and age<=25;
mysql> select * from stu where age between 20 and 25;

-- 5. 查询年龄不在20至25岁的学生信息
mysql> select * from stu where age not between 20 and 25;
mysql> select * from stu where age<20 or age>25;

-- 6. 查询id值为1,8,4,10,14的学生信息
select * from stu where id in(1,8,4,10,14);
mysql> select * from stu where id=1 or id=8 or id=4 or id=10 or id=14;

-- 7. 查询lamp138和lamp94期的女生信息
mysql> select * from stu where classid in('lamp138','lamp94') and sex='w';
mysql> select * from stu where (classid='lamp138' or classid='lamp94') and sex='w'







-- 统计班级classid值为2的男女生各多少人？
mysql> select sex,count(*) from stu where classid=2 group by sex;

-- 获取年龄最大的5位学生信息？
mysql> select * from stu order by age desc limit 5;

-- 获取每个班级的平均年龄，并按平均年龄降序，
mysql> select classid,avg(age) from stu group by classid order by avg(age) desc;
mysql> select classid,avg(age) anum from stu group by classid order by anum desc;

-- 统计每个班级的人数，按人数从大到小排序，取前3条。
mysql> select classid,count(*) num from stu group by classid order by num desc limit 3;





-- 授权用户 

grant select,insert on py5.stu to zhangsan@'%' identified by '123';




-- ubuntu 下, mysql忘记密码后重置mysql密码

-- 修改配置文件
 sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

 在[mysqld]的段中加上一句：skip-grant-tables 保存并且退出vim。


-- 重启mysqld
sudo /etc/init.d/mysqld restart


-- 登录并修改MySQL的root密码
mysql
mysql> USE mysql ; 
mysql> update mysql.user set authentication_string=password('abc123') where user='root' and Host = 'localhost';
mysql> flush privileges ; 
mysql> quit


-- 重新修改配置文件 把刚才添加的一句注释或者删除
 sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

-- 重新启动服务
 sudo /etc/init.d/mysqld restart

 -- 使用新密码重新登录mysql
 mysql -u root -pabc123
 mysql>



## 6 表的关联操作

-- 查询当前中表的最大年龄
mysql> select max(age) from stu;
+----------+
| max(age) |
+----------+
|       28 |
+----------+
1 row in set (0.00 sec)


-- 根据最大年龄查询信息
mysql> select * from stu where age = 28;
+----+--------+-----+-----+---------+
| id | name   | age | sex | classid |
+----+--------+-----+-----+---------+
| 16 | user10 |  28 | m   | py4     |
+----+--------+-----+-----+---------+
1 row in set (0.00 sec)

-- 查询年龄最大的所有学生信息
select * from stu where age = (select max(age) from stu);



-- 查询python02期的所有学生信息
select id from class where classname= 'python2';
select * from stu where classid = 2;

-- 查询python02期的所有学生信息
select * from stu where classid =(select id from class where classname= 'python2');


-- where
-- 查询所有学生信息，并跨表显示对应的班级名称信息
select stu.*,class.classname from stu,class where stu.classid = class.id;

mysql> select stu.*,class.classname from stu,class where stu.classid = class.id; 
+----+----------+-----+-----+---------+-----------+
| id | name     | age | sex | classid | classname |
+----+----------+-----+-----+---------+-----------+

| 1    | zhangsan | 20   | m    | 1    | python1 |
| ---- | -------- | ---- | ---- | ---- | ------- |
|      |          |      |      |      |         |

|  2 | lisi     |  20 | w   | 2       | python2   |
|  3 | wangwu   |  24 | m   | 3       | python3   |
|  4 | zhaoliu  |  20 | m   | 1       | python1   |
|  5 | tianqi   |  20 | w   | 2       | python2   |
|  6 | wangba   |  21 | w   | 3       | python3   |
|  7 | user1    |  20 | w   | 3       | python3   |
|  8 | user2    |  20 | w   | 3       | python3   |
|  9 | user3    |  26 | m   | 2       | python2   |
| 10 | user4    |  20 | m   | 2       | python2   |
| 11 | user5    |  20 | m   | 1       | python1   |
| 12 | user6    |  20 | w   | 1       | python1   |
| 13 | user7    |  23 | w   | 4       | python4   |
| 14 | user8    |  20 | w   | 5       | python5   |
| 15 | user9    |  20 | m   | 5       | python5   |
| 16 | user10   |  28 | m   | 5       | python5   |
| 17 | user11   |  20 | w   | 4       | python4   |
| 18 | user12   |  20 | m   | 5       | python5   |
| 19 | user13   |  20 | m   | 4       | python4   |
| 20 | user14   |  20 | w   | 2       | python2   |
| 21 | user15   |  20 | w   | 3       | python3   |
| 22 | user16   |  20 | m   | 1       | python1   |
+----+----------+-----+-----+---------+-----------+
22 rows in set (0.01 sec)


select stu.*****,class.***** from stu,class where stu.classid = class.id;

mysql> select stu.*****,class.***** from stu,class where stu.classid = class.id;
+----+----------+-----+-----+---------+----+-----------+-----------+-----------+---------+
| id | name     | age | sex | classid | id | classname | classbzr  | classxmjl | classjs |
+----+----------+-----+-----+---------+----+-----------+-----------+-----------+---------+
|  1 | zhangsan |  20 | m   | 1       |  1 | python1   | 张巧玲    | 张环宇    | 丛浩    |
|  2 | lisi     |  20 | w   | 2       |  2 | python2   | 齐婷婷    | 刘晓松    | 伊川    |
|  3 | wangwu   |  24 | m   | 3       |  3 | python3   | 张巧玲    | 张环宇    | 伊川    |

| 4    | zhaoliu | 20   | m    | 1    | 1    | python1 | 张巧玲  | 张环宇  | 丛浩   |
| ---- | ------- | ---- | ---- | ---- | ---- | ------- | ---- | ---- | ---- |
|      |         |      |      |      |      |         |      |      |      |

|  5 | tianqi   |  20 | w   | 2       |  2 | python2   | 齐婷婷    | 刘晓松    | 伊川    |
|  6 | wangba   |  21 | w   | 3       |  3 | python3   | 张巧玲    | 张环宇    | 伊川    |
|  7 | user1    |  20 | w   | 3       |  3 | python3   | 张巧玲    | 张环宇    | 伊川    |
|  8 | user2    |  20 | w   | 3       |  3 | python3   | 张巧玲    | 张环宇    | 伊川    |
|  9 | user3    |  26 | m   | 2       |  2 | python2   | 齐婷婷    | 刘晓松    | 伊川    |
| 10 | user4    |  20 | m   | 2       |  2 | python2   | 齐婷婷    | 刘晓松    | 伊川    |
| 11 | user5    |  20 | m   | 1       |  1 | python1   | 张巧玲    | 张环宇    | 丛浩    |
| 12 | user6    |  20 | w   | 1       |  1 | python1   | 张巧玲    | 张环宇    | 丛浩    |
| 13 | user7    |  23 | w   | 4       |  4 | python4   | NULL      | NULL      | NULL    |
| 14 | user8    |  20 | w   | 5       |  5 | python5   | NULL      | NULL      | NULL    |
| 15 | user9    |  20 | m   | 5       |  5 | python5   | NULL      | NULL      | NULL    |
| 16 | user10   |  28 | m   | 5       |  5 | python5   | NULL      | NULL      | NULL    |
| 17 | user11   |  20 | w   | 4       |  4 | python4   | NULL      | NULL      | NULL    |
| 18 | user12   |  20 | m   | 5       |  5 | python5   | NULL      | NULL      | NULL    |
| 19 | user13   |  20 | m   | 4       |  4 | python4   | NULL      | NULL      | NULL    |
| 20 | user14   |  20 | w   | 2       |  2 | python2   | 齐婷婷    | 刘晓松    | 伊川    |
| 21 | user15   |  20 | w   | 3       |  3 | python3   | 张巧玲    | 张环宇    | 伊川    |
| 22 | user16   |  20 | m   | 1       |  1 | python1   | 张巧玲    | 张环宇    | 丛浩    |
+----+----------+-----+-----+---------+----+-----------+-----------+-----------+---------+
22 rows in set (0.01 sec)


select stu.id as uid,stu.name,stu.age,class.id as cid,class.classname from stu,class where stu.classid = class.id;

mysql> select stu.id as uid,stu.name,stu.age,class.id as cid,class.classname from stu,class where stu.classid = class.id; 
+-----+----------+-----+-----+-----------+
| uid | name     | age | cid | classname |
+-----+----------+-----+-----+-----------+
|   1 | zhangsan |  20 |   1 | python1   |
|   2 | lisi     |  20 |   2 | python2   |
|   3 | wangwu   |  24 |   3 | python3   |
|   4 | zhaoliu  |  20 |   1 | python1   |
|   5 | tianqi   |  20 |   2 | python2   |
|   6 | wangba   |  21 |   3 | python3   |
|   7 | user1    |  20 |   3 | python3   |
|   8 | user2    |  20 |   3 | python3   |
|   9 | user3    |  26 |   2 | python2   |
|  10 | user4    |  20 |   2 | python2   |
|  11 | user5    |  20 |   1 | python1   |
|  12 | user6    |  20 |   1 | python1   |
|  13 | user7    |  23 |   4 | python4   |
|  14 | user8    |  20 |   5 | python5   |
|  15 | user9    |  20 |   5 | python5   |
|  16 | user10   |  28 |   5 | python5   |
|  17 | user11   |  20 |   4 | python4   |
|  18 | user12   |  20 |   5 | python5   |
|  19 | user13   |  20 |   4 | python4   |
|  20 | user14   |  20 |   2 | python2   |
|  21 | user15   |  20 |   3 | python3   |
|  22 | user16   |  20 |   1 | python1   |
+-----+----------+-----+-----+-----------+
22 rows in set (0.00 sec)

select s.id as uid,s.classid as sid,s.name,s.age,c.id as cid,c.classname from stu as s,class as c where s.classid = c.id;



-- 统计每个班级的人数
select c.classname,count(s.id) from class c,stu s where c.id=s.classid group by c.id;
mysql> select c.classname,count(s.id) from class c,stu s where c.id=s.classid group by c.id;
+-----------+-------------+

| classname | count(s.id) |
| --------- | ----------- |
|           |             |

+-----------+-------------+
| python1   |           5 |
| python2   |           5 |
| python3   |           5 |
| python4   |           3 |
| python5   |           4 |
+-----------+-------------+
5 rows in set (0.01 sec)


-- 统计每个班级的人数 排序
select c.classname,count(s.id) num from class c,stu s where c.id=s.classid group by c.id order by num desc;

mysql> select c.classname,count(s.id) num from class c,stu s where c.id=s.classid group by c.id order by num desc; 
+-----------+-----+
| classname | num |
+-----------+-----+
| python1   |   5 |
| python2   |   5 |
| python3   |   5 |
| python5   |   4 |
| python4   |   3 |
+-----------+-----+
5 rows in set (0.00 sec)


-- where

mysql> select news.id,news.title,newstype.name from news,newstype where news.nid=newstype.id;
+----+-------------------------------------------------------------+--------------+
| id | title                                                       | name         |
+----+-------------------------------------------------------------+--------------+
|  1 | 骑共享单车违法 将被禁用或冻结账户                           | 社会新闻     |
|  2 | 武警特战排爆手                                              | 军事新闻     |
|  3 | 国外武装直升机型号发展与作战能力分析                        | 军事新闻     |
|  4 | 俄战机过去一周在边境拦截外国侦察机11次                      | 军事新闻     |

| 5    | 中国空军战机进行远洋训练。 | 军事新闻 |
| ---- | ------------- | ---- |
|      |               |      |

|  6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    | 国际新闻     |
|  7 | 热烈庆祝十九大胜利召开                                      | 国际新闻     |
|  8 | 上海举办维密秀内衣展览                                      | 娱乐新闻     |
|  9 | 王宝强和谁谁第几次开庭                                      | 娱乐新闻     |
| 10 | 大兴失火死亡19人,北京全面严查                               | 社会新闻     |
| 11 | 自从川哥来了后,这罚单多的呀....                             | 班级新闻     |
+----+-------------------------------------------------------------+--------------+
11 rows in set (0.00 sec)


-- inner join 
select news.id,news.title,newstype.name from news inner join newstype on news.nid=newstype.id;

mysql> select news.id,news.title,newstype.name from news inner join newstype on news.nid=newstype.id;
+----+-------------------------------------------------------------+--------------+
| id | title                                                       | name         |
+----+-------------------------------------------------------------+--------------+
|  1 | 骑共享单车违法 将被禁用或冻结账户                           | 社会新闻     |
|  2 | 武警特战排爆手                                              | 军事新闻     |
|  3 | 国外武装直升机型号发展与作战能力分析                        | 军事新闻     |
|  4 | 俄战机过去一周在边境拦截外国侦察机11次                      | 军事新闻     |

| 5    | 中国空军战机进行远洋训练。 | 军事新闻 |
| ---- | ------------- | ---- |
|      |               |      |

|  6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    | 国际新闻     |
|  7 | 热烈庆祝十九大胜利召开                                      | 国际新闻     |
|  8 | 上海举办维密秀内衣展览                                      | 娱乐新闻     |
|  9 | 王宝强和谁谁第几次开庭                                      | 娱乐新闻     |
| 10 | 大兴失火死亡19人,北京全面严查                               | 社会新闻     |
| 11 | 自从川哥来了后,这罚单多的呀....                             | 班级新闻     |
+----+-------------------------------------------------------------+--------------+
11 rows in set (0.00 sec)



-- left join  以左表为准 
select news.id,news.title,newstype.name from news left join newstype on news.nid=newstype.id;

mysql> select news.id,news.title,newstype.name from news left join newstype on news.nid=newstype.id;
+----+-------------------------------------------------------------+--------------+

| id   | title | name |
| ---- | ----- | ---- |
|      |       |      |

+----+-------------------------------------------------------------+--------------+

| 1    | 骑共享单车违法 将被禁用或冻结账户 | 社会新闻 |
| ---- | ----------------- | ---- |
|      |                   |      |

|  2 | 武警特战排爆手                                              | 军事新闻     |
|  3 | 国外武装直升机型号发展与作战能力分析                        | 军事新闻     |

| 4    | 俄战机过去一周在边境拦截外国侦察机11次 | 军事新闻 |
| ---- | -------------------- | ---- |
|      |                      |      |

|  5 | 中国空军战机进行远洋训练。                                  | 军事新闻     |
|  6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    | 国际新闻     |
|  7 | 热烈庆祝十九大胜利召开                                      | 国际新闻     |
|  8 | 上海举办维密秀内衣展览                                      | 娱乐新闻     |
|  9 | 王宝强和谁谁第几次开庭                                      | 娱乐新闻     |
| 10 | 大兴失火死亡19人,北京全面严查                               | 社会新闻     |
| 11 | 自从川哥来了后,这罚单多的呀....                             | 班级新闻     |
+----+-------------------------------------------------------------+--------------+
11 rows in set (0.00 sec)

-- 以左表为准,补充右边的信息进来,如果没有对应信息,补上NULL
mysql> select news.id,news.title,newstype.name from news left join newstype on news.nid=newstype.id;
+----+-------------------------------------------------------------+--------------+
| id | title                                                       | name         |
+----+-------------------------------------------------------------+--------------+
|  1 | 骑共享单车违法 将被禁用或冻结账户                           | 社会新闻     |
|  2 | 武警特战排爆手                                              | 军事新闻     |
|  3 | 国外武装直升机型号发展与作战能力分析                        | 军事新闻     |
|  4 | 俄战机过去一周在边境拦截外国侦察机11次                      | 军事新闻     |
|  5 | 中国空军战机进行远洋训练。                                  | 军事新闻     |
|  6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    | 国际新闻     |
|  7 | 热烈庆祝十九大胜利召开                                      | 国际新闻     |
|  8 | 上海举办维密秀内衣展览                                      | 娱乐新闻     |
|  9 | 王宝强和谁谁第几次开庭                                      | 娱乐新闻     |
| 10 | 大兴失火死亡19人,北京全面严查                               | 社会新闻     |
| 11 | 自从川哥来了后,这罚单多的呀....                             | 班级新闻     |
| 12 | 年年都搬家,实在不想搬家了                                   | NULL         |
+----+-------------------------------------------------------------+--------------+
12 rows in set (0.00 sec)


-- right join 以右表为准,补充左表信息
 select news.id,news.title,newstype.name from newstype right join news on news.nid=newstype.id;
 mysql>  select news.id,news.title,newstype.name from newstype right join news on news.nid=newstype.id;
+----+-------------------------------------------------------------+--------------+
| id | title                                                       | name         |
+----+-------------------------------------------------------------+--------------+
|  1 | 骑共享单车违法 将被禁用或冻结账户                           | 社会新闻     |
|  2 | 武警特战排爆手                                              | 军事新闻     |
|  3 | 国外武装直升机型号发展与作战能力分析                        | 军事新闻     |
|  4 | 俄战机过去一周在边境拦截外国侦察机11次                      | 军事新闻     |
|  5 | 中国空军战机进行远洋训练。                                  | 军事新闻     |
|  6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    | 国际新闻     |
|  7 | 热烈庆祝十九大胜利召开                                      | 国际新闻     |
|  8 | 上海举办维密秀内衣展览                                      | 娱乐新闻     |
|  9 | 王宝强和谁谁第几次开庭                                      | 娱乐新闻     |
| 10 | 大兴失火死亡19人,北京全面严查                               | 社会新闻     |
| 11 | 自从川哥来了后,这罚单多的呀....                             | 班级新闻     |
| 12 | 年年都搬家,实在不想搬家了                                   | NULL         |
+----+-------------------------------------------------------------+--------------+

mysql> select newstype.name,news.id,news.title from news right join newstype on news.nid=newstype.id;
+--------------+------+-------------------------------------------------------------+
| name         | id   | title                                                       |
+--------------+------+-------------------------------------------------------------+

| 社会新闻 | 1    | 骑共享单车违法 将被禁用或冻结账户 |
| ---- | ---- | ----------------- |
|      |      |                   |

| 军事新闻     |    2 | 武警特战排爆手                                              |
| 军事新闻     |    3 | 国外武装直升机型号发展与作战能力分析                        |
| 军事新闻     |    4 | 俄战机过去一周在边境拦截外国侦察机11次                      |
| 军事新闻     |    5 | 中国空军战机进行远洋训练。                                  |
| 国际新闻     |    6 | 中国驻韩使馆举行中韩建交25周年纪念招待会                    |
| 国际新闻     |    7 | 热烈庆祝十九大胜利召开                                      |
| 娱乐新闻     |    8 | 上海举办维密秀内衣展览                                      |
| 娱乐新闻     |    9 | 王宝强和谁谁第几次开庭                                      |
| 社会新闻     |   10 | 大兴失火死亡19人,北京全面严查                               |
| 班级新闻     |   11 | 自从川哥来了后,这罚单多的呀....                             |
| 体育新闻     | NULL | NULL                                                        |
+--------------+------+-------------------------------------------------------------+
12 rows in set (0.00 sec)



-- 统计每个新闻类别下的新闻数量，采用左联统计
select t.name,count(n.id) from newstype t left join news n on t.id=n.nid group by t.id;
mysql> select t.name,count(n.id) from newstype t left join news n on t.id=n.nid group by t.id order by count(n.id) desc ;
+--------------+-------------+
| name         | count(n.id) |
+--------------+-------------+
| 军事新闻     |           4 |
| 社会新闻     |           2 |
| 国际新闻     |           2 |
| 娱乐新闻     |           2 |
| 班级新闻     |           1 |
| 体育新闻     |           0 |
+--------------+-------------+
6 rows in set (0.00 sec)





## 7. mysql的触发器

-- mysql的触发器

//意思就是当删除这个表里的数据把他给加到另一个表中

创建一个触发器名叫 del_stu 当删除stu表里的每一个数据 那么 我给他加入到stu_bak中  这个是我们创建好的!

-- 把mysql的结束符改为$$
\d $$

create trigger del_stu before delete on stu for each row
begin

```
insert into stu_bak(uid,name,sex,age) values(old.id,old.name,old.sex,old.age);
```

end;
$$

drop trigger del_stu;    //删除触发器



## 8. mysql的存储过程

-- mysql 存储过程
-- (修改语句结束符号)
\d //
create procedure p2()
begin
set @i=0;
while @i<10 do

//往user表  字段名 加值  concat函数 字符串连接

insert into user(username) values(concat('user',@i));
set @i=@i+1;
end while;
end;
//
\d ;

## 9.创建视图

-- 创建视图 //意思就是当我往视图里加数据或者是删除数据 那么都是从我的这个视图所在的表进行操作的 但是他不是个表
mysql> create view age25 as select * from stu where age > 25;
Query OK, 0 rows affected (0.07 sec)

-- 查看
mysql> show tables;
+---------------+
| Tables_in_py5 |
+---------------+
| age25         |
| class         |
| news          |
| newstype      |
| stu           |
| user          |
| users         |
+---------------+
7 rows in set (0.00 sec)





## 10.模仿删库恢复操作

-- 刷新 日志
mysql> reset master;
Query OK, 0 rows affected (0.39 sec)

mysql> create database ops;
Query OK, 1 row affected (0.28 sec)

mysql> use ops;
Database changed

create table customers(
id int not null auto_increment,
name char(20) not null,
age int not null,
primary key(id)
)engine=InnoDB;

insert into customers values(1,"wangbo","24"),(2,"guohui","22"),(3,"zhangheng","27");

mysql> select *  from customers;
+----+-----------+-----+
| id | name      | age |
+----+-----------+-----+

| 1    | wangbo | 24   |
| ---- | ------ | ---- |
|      |        |      |

|  2 | guohui    |  22 |
|  3 | zhangheng |  27 |
+----+-----------+-----+
3 rows in set (0.00 sec)

-- （2）现在进行全备份
mysqldump -uroot -p -B -F -R -x --master-data=2 ops >/home/yc/ops.sql

------

参数说明：
-B：指定数据库
-F：刷新日志
-R：备份存储过程等
-x：锁表
--master-data：在备份语句里添加CHANGE MASTER语句以及binlog文件及位置点信息



-- 再添加新的数据
insert into customers values(4,"liupeng","21"),(5,"xiaoda","31"),(6,"fuaiai","26");

mysql> select * from customers;
+----+-----------+-----+
| id | name      | age |
+----+-----------+-----+
|  1 | wangbo    |  24 |
|  2 | guohui    |  22 |
|  3 | zhangheng |  27 |
|  4 | liupeng   |  21 |
|  5 | xiaoda    |  31 |
|  6 | fuaiai    |  26 |
+----+-----------+-----+
6 rows in set (0.00 sec)



-- （4）此时误操作，删除了test数据库
drop database ops;

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| python4            |
| sys                |
| wx                 |
+--------------------+
6 rows in set (0.00 sec)



将binlog文件导出sql文件，并vim编辑它删除其中的drop语句
[root@vm-002 backup]# mysqlbinlog -d ops /var/lib/mysql/mysql-bin.000002> /home/yc/002bin.sql
sudo mysqlbinlog -d ops /var/lib/mysql/mysql-bin.000002> /home/yc/002bin.sql



[root@vm-002 backup]# ls
002bin.sql mysql-bin.000002 ops_2016-09-25.sql
[root@vm-002 backup]# vim 002bin.sql #删除里面的drop语句

-- 首先导入备份的数据文件
mysql -uroot -p < /home/yc/ops.sql 



再导入删除 drop语句后的 binlog日志文件
mysql -uroot -p ops < /home/yc/002bin.sql



## 11.事务处理

- **BEGIN** 开始一个事务
- **ROLLBACK** 事务回滚
- **COMMIT** 事务确认



- 方法1

```
开启事务
BEGIN;
执行sql...

成功执行 事务提交
commit

失败执行 事务回滚
rollback 
```

- 方法2


- **SET AUTOCOMMIT=0** 禁止自动提交
- **SET AUTOCOMMIT=1** 开启自动提交

```
1. set autocommit = 0;
2. 增删改语句
3. savepoint aaa;
4. 继续执行语句
5. savepoint bbb;
6. rollback to aaa; 回滚到aaa;
7. commit
```

## 12.python 连接mysql 增删改查

最开始要有一个服务器的环境, 这里我们用server.py 来作为环境,

建立一个文件夹叫cgi-bin 把py文件卸载这个文件夹的里面, 之后在终端运行server.py的时候要在这个文件的所在目录运行这行代码 python3 server.py 这个文件和cgi-bin这个文件夹在一个目录下

1.首先要有一个html页面 留言为例 代码如下: 跳add.py

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>留言</title>
</head>
<body>
  // 当用户输入完 点击注册 请求到add.py 来进行处理
	<form action="/cgi-bin/add.py" method="post" >
	//通过name属性 来获取用户输入的值
	用户名:<input type="text" name="yhm"><br>
	留言内容:
	<br>
		<textarea name="content">请输入留言信息</textarea>
	<br>
	<input type="submit" name="" value="提交">
	</form>
</body>
</html>

```

1.add.py 注册 增加功能的py文件  跳caozuo.py

```
#这行代码是生命python3这个环境所在的目录
#!/usr/bin/env python3 

#导入pymysql这个包,和时间模块
import cgi,cgitb,pymysql,time

#这个是必须的
print('Content-type:text/html;charset=utf8')
print()

#接收浏览器传来的数据 这里调用cgi包里的一个方法

fs=cgi.FieldStorage()

#定义一个变量 来接收表单提交过来的值 通过表单的属性yhm
uname=fs['yhm'].value
#定义一个变量 来接收表单里面提交过来的内容 通过表单的属性content
con=fs['content'].value
#定义一个时间的变量来获取当前的时间
addtime = time.time()

#连接数据库  调用pymysql里的方法connect  第一个参数是服务器端口号 ,
第二个参数是数据库主人root用户名,第三个参数是密码,第四个参数是库名,第五个参数是字符集 
db=pymysql.connect('127.0.0.1','root','123456','liuyandb',charset='utf8')

# 使用cursor()方法获取操作游标 
cursor=db.cursor()

#sql语句 往数据库里的表添加值 这里用到了format 函数 
#sql里的uname  是format 函数里面往里传入的内容也是一个变量,但是在数据库里他是一个值
sql='insert into liuyanba values (null,"{uname}","{con}","

#   这里参数第一个uname是fomat函数的参数  第二个uname是上面的变量
{addtime}")'.format(uname=uname,con=con,addtime=str(addtime))

#这个是一个一个变量   内容是要返回浏览器的html内容,只能通过浏览器来进行解析 
num1="""
	<script>
	alert
	('添加留言成功');location.href='/cgi-bin/caozuo.py';
	</script>
	"""
#之后执行这个try except 如果正确了 ,我给浏览器返回个页面, 如果错了那么我走except 这个区间 让他进行回滚
try:
	cursor.execute(sql)
	db.commit()
	print(num1)

except:
	db.rollback()
	#如果出现错误 那么我还给跳转到liuyan的这个页面
	print("<script>alert('tianjia  shibai');location.href='/liuyan.html';</script>")

db.close()
```



2. caozuo.py 查询  这个页面相当于是显示页面   选择跳转

```
#!/usr/bin/env python3

import cgi,cgitb,pymysql,time

print('Content-type:text/html;charset=utf8')
print()

db=pymysql.connect('127.0.0.1','root','123456','liuyandb',charset='utf8')

cursor=db.cursor()



sql='select * from liuyanba'

try:
	cursor.execute(sql)
#获取数据库里的所有数据
	res=cursor.fetchall()
#定义一个字符串变量
	trs=''

#遍历数据,通过format 函数给遍历出来的数据给放到trs这个变量html中

	for row in res:
		abc=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(row[3])))
		trs+="""
		<tr>
			<td>{id}</td>
			<td>{username}</td>
			<td>{content}</td>
			<td>{addtime}</td>
			<td>
			#删除跳转删除功能的py文件
				<a href="/cgi-bin/del.py?id={id}">删除</a>
				<br>
			#修改的话先跳到显示功能页面 也就是xiugai这个py文件
				<a href="/cgi-bin/xiugai.py?id='{id}'">修改</a>
			</td>
		</tr>
		""".format(id=row[0],username=row[1],content=row[2],addtime=abc)

except:
	print('chaxun shibai')

#这里给html完整版的写好 把上面那个变量加进来给他返回出去!
html="""

<!DOCTYPE html>
<html>
<head>
		<meta charset="utf-8">
	<title>留言列表</title>
</head>
<body>
	<a href="/add.html">添加留言</a>
	<table width="700" border="1">
		<tr>
			<th>ID</th>
			<th>用户名</th>
			<th>留言信息</th>
			<th>时间</th>
			<th>操作</th>
		</tr>
		{trs}
	</table>
</body>
</html>
""".format(trs = trs)

print(html)
```

3.修改显示页面 xiugai.py

```
#!/usr/bin/python3

import cgi,cgitb,pymysql
cgitb.enable()


print("Content-Type: text/html;charset=utf-8")#HTML is following
print()


fs=cgi.FieldStorage()
uid=fs['id'].value

db=pymysql.connect('127.0.0.1','root','123456','liuyandb',charset='utf8')

cursor=db.cursor()

sql='SELECT * FROM  liuyanba where id='+uid


cursor.execute(sql)

result=cursor.fetchone()


hjs="""
<!DOCTYPE html>

<head>
	<meta charset="utf-8">
	<title>修改留言</title>
</head>
<body>

	<form action="/cgi-bin/xiugai2.py" method="post">
	用户名:<input type="text" name="yhm" value="%(uname)s"><br>
		留言内容:
		<br>
			<textarea name="content">%(ucontent)s</textarea>
		<br>
		<input type="hidden" name="id" value="%(id)s">
		<input type="submit" name="" value="提交">

	</form>
</body>
</html>
"""%{'uname':result[1],'ucontent':result[2],'id':result[0]}
print(hjs)

```



4.修改过程页面 xiugai2.py

```
#!/usr/bin/python3
import cgi,cgitb,pymysql,time
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")#HTML is following
print()

fs=cgi.FieldStorage()
inputs={}
for key in fs.keys():
	inputs[key]=fs[key].value


addtime=time.time()



db=pymysql.connect("127.0.0.1","root","123456","liuyandb",charset="utf8")

cursor=db.cursor()


sql='update liuyanba set neirong="'+inputs['content']+'",shijian="'+str(addtime)+'" where id='+inputs['id']+''


hjs="""
<script>
alert('xgcg');
location.href='/cgi-bin/caozuo.py';
</script>

"""

try:
	cursor.execute(sql)
	db.commit()
	print(hjs)
except:
	db.rollback()
	print('error')

db.close()


```

5.del.py 删除操作

```
#!/usr/bin/python3

import cgi,cgitb,pymysql
cgitb.enable()

print("Content-Type:text/html;charset=utf-8")#HTML is following
print()

fs=cgi.FieldStorage()

uid=fs['id'].value


db=pymysql.connect('127.0.0.1','root','123456','liuyandb',charset='utf8')

cursor=db.cursor()

sql='delete from liuyanba where id='+uid


hjs="""
	<script>
	alert('abcdefg');
	#删完之后又给跳到了查询页面
	location.href='/cgi-bin/caozuo.py';
	</script>
	"""

try:
	cursor.execute(sql)
	db.commit()
	print(hjs)

except:
	db.rollback()
	print('error')


db.close()
```

## 13.mysql 瀑布流 ajax 请求

html 页面

```
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<style type="text/css">
		
	ul,li,h3,p{
		margin: 0;
		padding: 0;
		list-style:none;
	}

	ul{
		width: 24%;
		height: 500px;
		float: left;
		box-sizing:border-box;
		margin: 0 5px;
	}

	li{
		width: 300px;
		height: 450px;
		margin: 0 auto;
		text-align:center;
		margin-bottom: 20px;
	}

	li div{
		margin-top: -50px;
	}
	


	</style>
</head>
<body>
   <li style="display: none;">
   	<img src="./images/3aa3744cf515f5c0b7fd8b21c4c6edaf.jpg" width="100%" height="100%">
		<div>
			<h3>小清新格子包臀裙</h3>
			<p>155.00</p>
		</div>
   </li>
   <ul></ul>
   <ul></ul>
   <ul></ul>
   <ul></ul>
   <script type="text/javascript" src="./jquery-1.8.3.min.js"></script>
   <script type="text/javascript">
	var p=1;
	RequestGoods();
	
	function RequestGoods(){

		$.get('/cgi-bin/goodss.py',{p:p},function(data){
	  	
	  	
	
		  	for (var i = 0; i < data.length; i++) {
	  			console.log(data[i][1],typeof(data[i][1]));

		  		var cli=$('li:first').clone();
		  		// 这里的关键是把拿来的二级列表的值给取出来
		  		cli.find('img').attr('src',data[i][2]);
		  		cli.find('h3').html(data[i][1]);
		  		cli.find('p').html(data[i][3]);
		  		cli.show()
		  		
		  		 var inx=i%4;
		  		 $('ul').eq(inx).append(cli)

		  		
		  	};
	  		p++;
	  	},'json')
	}
	 

	  $(window).scroll(function(){
	  	var dH=$(document).height();
	  	var wH=$(window).height();
	  	var dT=$(document).scrollTop();
	  	if(dH==dT+wH){
	  		RequestGoods();
	  	}
	  })



   </script>
</body>
</html>
```



py 文件

```
#!/usr/bin/env python3
import cgi,cgitb,json,pymysql
cgitb.enable()

print('Content-type:text/html;charset=utf-8')
print()


fs = cgi.FieldStorage()

p = fs["p"].value

p=int(p)
end=p*16
start=end-16

# print(p)
# exit()



db = pymysql.connect("localhost","root","123456","liuyandb",charset="UTF8")


cursor=db.cursor()



sql="select * from goods limit {start},16".format(start=str(start))

# sql="select * from goods where id>="+str(start)+" and id<="+str(end)+" "


	# cursor.execute('select * from goods where id >%s limit '+16+' ',args)
cursor.execute(sql)
#  huoqu suoyou shuju
result=cursor.fetchall()
# print(result)
arr=list(result)

# 关闭数据库连接
db.close()



print(json.dumps(arr))
```



## 14. btree索引和hash索引的区别

```
hash 索引结构的特殊性，其检索效率非常高，索引的检索可以一次定位，不像B-Tree 索引需要从根节点到枝节点，最后才能访问到页节点这样多次的IO访问，所以 Hash 索引的查询效率要远高于 B-Tree 索引。 
可 能很多人又有疑问了，既然 Hash 索引的效率要比 B-Tree 高很多，为什么大家不都用 Hash 索引而还要使用 B-Tree 索引呢？任何事物都是有两面性的，Hash 索引也一样，虽然 Hash 索引效率高，但是 Hash 索引本身由于其特殊性也带来了很多限制和弊端，主要有以下这些。

（1）Hash 索引仅仅能满足”=”,”IN”和”<=>”查询，不能使用范围查询。

由于 Hash 索引比较的是进行 Hash 运算之后的 Hash 值，所以它只能用于等值的过滤，不能用于基于范围的过滤，因为经过相应的 Hash 算法处理之后的 Hash 值的大小关系，并不能保证和Hash运算前完全一样。

（2）Hash 索引无法被用来避免数据的排序操作。

由于 Hash 索引中存放的是经过 Hash 计算之后的 Hash 值，而且Hash值的大小关系并不一定和 Hash 运算前的键值完全一样，所以数据库无法利用索引的数据来避免任何排序运算；

（3）Hash 索引不能利用部分索引键查询。

对于组合索引，Hash 索引在计算 Hash 值的时候是组合索引键合并后再一起计算 Hash 值，而不是单独计算 Hash 值，所以通过组合索引的前面一个或几个索引键进行查询的时候，Hash 索引也无法被利用。

（4）Hash 索引在任何时候都不能避免表扫描。

前面已经知道，Hash 索引是将索引键通过 Hash 运算之后，将 Hash运算结果的 Hash 值和所对应的行指针信息存放于一个 Hash 表中，由于不同索引键存在相同 Hash 值，所以即使取满足某个 Hash 键值的数据的记录条数，也无法从 Hash 索引中直接完成查询，还是要通过访问表中的实际数据进行相应的比较，并得到相应的结果。

（5）Hash 索引遇到大量Hash值相等的情况后性能并不一定就会比B-Tree索引高。

对于选择性比较低的索引键，如果创建 Hash 索引，那么将会存在大量记录指针信息存于同一个 Hash 值相关联。这样要定位某一条记录时就会非常麻烦，会浪费多次表数据的访问，而造成整体性能低下。
```



# MongoDB

## 1.数据库操作

进入mongo 环境  **mongod**

进入mogo      **mongo**

进入py5 数据库,如果不存在则创建  **use py5**

查看当前所在库  **db**

查看库 如果库里没有数据,则不显示  **show dbs**

1.在当前库中创建一个user集合(表) 进行数据的添加

**db.user.insert(  {"name": "zhangsan", "age" :20} )**

2.查看当前库中所有集合(表)

**show tables**

3.查看user 集合中的所有文档

**db.user.find()**

4.插入文档也可以使用db.user.save(document)的命令,

如果不指定_id字段 save()方法类似于  insert()方法 .

如果指定_id 字段,则会更新该 _id 的数据

ab=( { 

_id: ObjectId("5a17b8f80db5700d39d9e990"),

name:"zhangsan",

age:22,

sex:"女"

})

db.user.save(ab)



## 2.update( )

注意 一下语句在mongo中默认只修改第一条符合要求的数据

第一个条件 ,第二个是要设置的内容

1.db.col.update({ 'title' :'MongoDB 教程'},{ $set:{ 'title' :'MongoDB' }})

2.**multi**

{multi:true} 设置参数为true 即可修改符合要求的全部数据

db.col.update( {'title': 'MongoDB 教程'},{ $set:{'title':'MongoDB'}} ,{multi:true})



false (upsert) 

​			默认false 如果为false 通过条件没有 不插入

​			 true  如果为true  没有 插入

true(multi) 

​			默认false 如果为false 只更新一条 

​			true 如果为true  符合条 全更新按照字段

​												upsert,multi		

db.user.update( { " classid" : { $gt:5} }, {set: { "age":90,"num" :1} } ,false,true)





## 3.find()

1.通过字段来搜索

db.user.find({ username:"熊二",age:27})

db.user.find().pretty()以格式化来进行显示

2.or 条件 

找到年龄大于26的熊大或者是熊二

```
db.user.find({"age": {$gt:26}, $or: [{"username": "熊二"},{"username": "熊大"}]}).pretty()
```

3.限制返回数据字段 只要_id 和username 

如果有一些数据存在_id字段,但是不存在username字段,也在当前返回的数据结果中

db.user.find({},{"_id":1,"username":1}).pretty()

4.修改一个数据

```
db.user.save({
	"_id" : ObjectId("5a17c5240db5700d39d9e992"),
	"username" : 2,
	"age" : 27,
	"email" : "熊二@qq.com",
	"classid" : 4
})
查询
db.user.find()
查询username 字段类型为2(字符串)
db.user.find(username:{$type:2})
查询username 字段类型为1(数字类型)
db.user.find({username:{$type:1}}).pretty()
```



## 4.remove()

删除文档:db.collection.remove(   <query>,   <justOne>)

2.6版本以后 db.collection.remove(   <query>,   {     justOne: <boolean>,     writeConcern: <document>   })

## 5.limit()

--  limit方法 指定取出的数据数量
db.user.find().limit(5)


db.user.find({},{"username":1}).limit(5)


-- skip方法 指定跳过多少条数据
db.user.find({},{"username":1}).limit(2).skip(3)
db.user.find({},{"username":1}).skip(3).limit(2)


-- sort 方法 按指定字段进排序 ,其中 1 为升序排列，而-1是用于降序排列。
db.user.find({},{"username":1,"classid":1,"age":1,_id:0}).sort({"classid":-1})

db.user.find({},{"username":1,"classid":1,"age":1,_id:0}).sort({"age":-1})

## 6.count()

-- MongoDB 排序 count()方法

//统计数据信息

db.user.count()

## 7.aggregate()

类似:*select by_user, count(\*) from mycol group by by_user*

db.user.aggregate([{$group : {_id : "$classid", num : {$avg : "$age"}}}])


db.user.aggregate([{$group : {_id : "$classid", num_tutorial : {$min : "$age"}}}])

## 8.  索引操作

--查询索引

db.user.getIndexes()

-- 添加普通索引
db.user.ensureIndex({"username":1})


--  分析
db.user.find({"username":'张三'}).explain()


-- 删除索引
db.user.dropIndex({"username":1})


-- 使用索引时的查询
db.user.find({"username":'张三'}).explain()



## 8.备份 数据恢复

--  退出mongo命令行 进行 数据备份
mongodump -d py5 -o /home/yc/data/


-- 删除库
db.dropDatabase()

-- 回复数据库 
mongorestore -d py5 /home/yc/data/py5



**MongoDB 备份(mongodump)与恢复(mongorestore)**

MongoDB数据备份

在Mongodb中我们使用mongodump命令来备份MongoDB数据。该命令可以导出所有数据到指定目录中。

mongodump命令可以通过参数指定导出的数据量级转存的服务器。



**数据恢复**

mongodb使用 mongorestore 命令来恢复备份的数据。

mongorestore命令脚本语法如下：

```
>mongorestore -h <hostname><:port> -d dbname <path>
退出mongo客户端执行
mongorestore -d py /home/yc/data/py4

```

--host <:port>, -h <:port>： MongoDB所在服务器地址，默认为： localhost:27017

--db , -d ：需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2

--drop：恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！

<path>：mongorestore 最后的一个参数，设置备份数据所在位置，例如：c:\data\dump\test。

你不能同时指定 <path> 和 --dir 选项，--dir也可以设置备份目录。

--dir：指定备份的目录 你不能同时指定 <path> 和 --dir 选项。

接下来我们执行以下命令:

```
>mongorestore

```

执行以上命令输出结果如下：

## 9. python  连接MongoDbB 增删改查

1.html 页面

```
<!DOCTYPE html>
<html>
<head>
		<meta charset="utf-8">
	<title>添加留言</title>
</head>
<body>
	<form action="/cgi-bin/add.py" method="post">
		
		用户名:<input type="text" name="username"><br>
		留言内容:
		<br>
			<textarea name="content">请输入留言信息...</textarea>
		<br>
		<input type="submit" name="">
	</form>
</body>
</html>
```
2.add.py 

```
#!/usr/bin/python3
import cgi,cgitb,pymongo,json
cgitb.enable()

print('Content-type:text/html;charset=utf8')
print()



# 接收数据
fs = cgi.FieldStorage()
data = {}  
for key in fs.keys():  
    data[key] = fs[key].value  



# 链接mongo
client = pymongo.MongoClient('127.0.0.1',27017)

# 选择库
db = client.py5


hjs = """
	<script>
	  alert('添加成功');
     location.href = '/cgi-bin/index.py';
	</script>
"""

   
try:
   db.liuyan.insert(data)
   print(hjs)
except:
   print('error')
 


```



3.显示页面  index.py

```
#!/usr/bin/env python3
import cgi,cgitb,pymongo
cgitb.enable()

print('Content-type:text/html;charset=utf8')
print()

# 链接mongo
client = pymongo.MongoClient('127.0.0.1',27017)

# 选择库
db = client.py5


try:
	
	trs = ''
	for row in db.liuyan.find():
		
		trs += """
		<tr>
			<td>{username}</td>
			<td>{content}</td>
			<td>
				<a href="/cgi-bin/del.py?id={id}">删除</a>
				<br>
				<a href="/cgi-bin/update.py?id={id}">修改</a>
			</td>
		</tr>
		""".format(id = row['_id'],username=row['username'],content=row['content'])

except:
	# print("<script>alert('查询留言失败');location.href='/add.html';</script>")
	print("查询留言失败")



html = """
<!DOCTYPE html>
<html>
<head>
		<meta charset="utf-8">
	<title>留言列表</title>
</head>
<body>
	<a href="/add.html">添加留言</a>
	<br>

	<table width="700" border="1">
		<tr>
			<th>用户名</th>
			<th>留言信息</th>
			<th>操作</th>
		</tr>
		{trs}
	</table>
</body>
</html>
""".format(trs = trs)


print(html)
```

 4.修改显示页面

   ```
!/usr/bin/python3

import cgi,cgitb,pymongo

from bson.objectid import ObjectId

cgitb.enable()

print('Content-type:text/html;charset=utf8')

print()

fs=cgi.FieldStorage()

lid=fs['id'].value

print(lid)

client=pymongo.MongoClient("127.0.0.1",27017)

db = client.py5

hjs = ''

for result in db.liuyan.find({"_id":ObjectId(lid)}): 

    hjs = """
    <!DOCTYPE html>
    <html>
    <head>
    	<meta charset="utf-8">
    	<title>修改留言</title>
    </head>
    <body>
    	<form action="/cgi-bin/dbupdate.py" method="post">
    	用户名:<input type="text" name="username" value="%(uname)s"><br>
    		留言内容:
    		<br>
    			<textarea name="content">%(ucontent)s</textarea>
    		<br>
    		<input type="hidden" name="id" value="%(id)s">
    		<input type="submit" name="" value="提交">
    	</form>
    </body>
    </html>
    """%{'uname':result["username"],'ucontent':result["content"],'id':lid}

print(hjs)


   ```
5.修改页面

```
!/usr/bin/python3

import cgi,cgitb,pymongo

from bson.objectid import ObjectId

cgitb.enable()

print('Content-type:text/html;charset=utf8')

print()

fs=cgi.FieldStorage()

data={}

data['id']=ObjectId(fs['id'].value)

data['username']=fs['username'].value

data['content']=fs['content'].value

print(lid)

exit()

client=pymongo.MongoClient("127.0.0.1",27017)

db = client.py5

hjs = """

    	<script>
    	alert('xiugai成功');
    	location.href = '/cgi-bin/index.py';
    	</script>
      """

try:

    db.liuyan.save(data)
    print(hjs)

except:

   print('error')

```


## 10.mongodb 瀑布流  ajax请求

**要导入jquery 还要有把图片放库里 **

html 页面

```
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		
	ul,li,h3,p{
		margin: 0;
		padding: 0;
		list-style:none;
	}

	ul{
		width: 24%;
		height: 500px;
		float: left;
		box-sizing:border-box;
		margin: 0 5px;
	}

	li{
		width: 300px;
		height: 450px;
		margin: 0 auto;
		text-align:center;
		margin-bottom: 20px;
	}

	li div{
		margin-top: -50px;
	}
	


	</style>
</head>
<body>
   <li style="display: none;">
   	<img src="./images/3aa3744cf515f5c0b7fd8b21c4c6edaf.jpg" width="100%" height="100%">
		<div>
			<h3>小清新格子包臀裙</h3>
			<p>155.00</p>
		</div>
   </li>
   <script type="text/javascript" src="/jquery-1.8.3.min.js"></script>
	<script type="text/javascript">
	// 调用函数
	RequestGoods();
	// 定义一个变量 传递过去的参数
	 var p=1;
	 // 定义一个函数 发送ajax get请求goods.py
	  function RequestGoods(){
	  	// 请求的py文件所在路径  第一个p是传递过去的参数  第二个p是上面的变量  
	  	// 之后是回调函数 要求接收json  字典格式
	  	$.get('/cgi-bin/goods.py',{p:p},function(data){
	  		// 遍历py文件给返回来的数据
	  	for (var i = 0; i < data.length; i++) {
	  		// 变量 克隆第一个li
	  		var cli=$('li:first').clone()
	  		// 找到img标签  给他设置拿回来的数据的属性 后面是属性值
	  		cli.find('img').attr('src',data[i].pic);
	  		// 找到h3标签 给他设置拿回来的数据的标题  后面是属性值  
	  		cli.find('h3').html(data[i].title+data[i].id);
	  		// 价格
	  		cli.find('p').html(data[i].price);
	  		// 之后把这个变量给显示到上面
	  		cli.show()
	  		//把遍历的数据给平分  求余4=0
	  		 var inx=i%4;
	  		 //之后找到ul 通过索引 给这个平分的变量 放到ul当中
	  		 $('ul').eq(inx).append(cli)

	  		
	  	};
	  	// 让p自增
	  	p++;
	  	},'json')
	  }
	  // 文档滚动事件
	  $(window).scroll(function(){
	  	// 获取文档高度
	  	var dH=$(document).height();
	  	// 获取可是区域的高度
	  	var wH=$(window).height();
	  	// 获取滚动的高度
	  	var dT=$(document).scrollTop();
	  	// 判断是否触底 如果文档高度=可视的高度+滚动的高度
	  	if(dH==dT+wH){
	  		// 再次发出请求  调用请求
	  		RequestGoods();
	  	}
	  })



	</script>
</body>
</html>
```

请求的py文件

```
#!/usr/bin/python3

import  cgi,cgitb,json,pymongo
cgitb.enable()

print('Content-type:text/html;charset=utf-8')
print()


fs=cgi.FieldStorage()
# 定义一个变量 获取传来的参数p的值
p=fs["p"].value
# mongo 连接数据库的方法
client=pymongo.MongoClient('127.0.0.1',27017)
# 连接数据库

db=client.py5
# 把传来的参数给转换成整型
p=int(p)
# 
end=p*16

start=end-16;
# 找到goods表 查询所有 不要_id字段 跳过start 取16条
res=db.goods.find({},{'_id':0}).skip(start).limit(16)
# 定义一个空数组  

arr=[]
# 遍历 给返回json字典格式
for row in res:
	arr.append(row)

print(json.dumps(arr))
```

# Redis



## 1.数据库操作

进入数据库 **redis-cli**

### 1.1常用操作

keys *  //返回键（key）

keys list*   //返回名以list开头的所有键（key）

exists list1  //判断键名为list1的是否存在   存在返回1， 不存在返回0

del list1 //删除一个键（名为list1）
expire list1 10 //设置键名为list1的过期时间为10秒后

ttl list1 //查看键名为list1的过期时间，若为-1表示以过期 或 永不过期

move age 1 //将键名age的转移到1数据库中。

select 1 //表示进入到1数据库中，默认在0数据库

persist age //移除age的过期时间

flushdb:删除所有的数据 清除当前所在库的所有数据

flushall 清空所有数据
## 2.数据类型

Redis通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Hash), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。



### 2.1String(字符串类型)

set 命令：设置一个键和值，键存在则只覆盖，返回ok
 > set 键  值    例如： >set name zhangsan

 get 命令：获取一个键的值，返回值
 > get 键        例如：>get name

 setnx命令：设置一个不存在的键和值（防止覆盖），
 > setnx 键 值      若键已存在则返回0表示失败

 setex命令：设置一个指定有效期的键和值（单位秒）
 > setex 键 [有效时间] 值  例如: >setex color 10 red
 >   不写有效时间则表示永久有效，等价于set

 setrange命令：替换子字符串 (替换长度由子子串长度决定)
 > setrange 键 位置 子字串   
 >
 > setrange name 4 aa  将name键对应值的第4个位置开始替换  被替换的位置索引是从0开始的

 mset命令：批量设置键和值,成功则返回ok
 > mset 键1 值1 键2 值2 键3 值3 ....

 msetnx命令：批量设置不存在的键和值,成功则返回ok
 > msetnx 键1 值1 键2 值2 键3 值3 ....

 getset命令：获取原值，并设置新值

 getrange命令：获取指定范围的值
 >getrange 键 0 4     //获取指定0到4位置上的值

 mget命令： 批量获取值
 >mget 键1 键2 键3....

 incr命令： 指定键的值做加加操作，返回加后的结果。
 >  键        例如： >incr 键1  就是给这个1的键的值做+1操作   
 >   incrby命令： 设置某个键加上指定值    incrby  键1 给它值加5  就是  incrb 1 5
 >  incrby 键 m    //其中m可以是正整数或负整数  就是可以给键做减操作

 decr命令： 指定键的值做减减操作，返回减后的结果。
 > decr 键        例如： >decr kid   给键做减操作
 >  decrby命令： 设置某个键减上指定值
 > decrby 键 m    //其中m可以是正整数或负整数  

 append命令：给指定key的字符串追加value，返回新字符串值的长度
 >append 键 追加字串

 strlen求长度 >strlen 键名   //返回对应的值。



### 2.2.Hash类型

Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象

hset命令：设置一个哈希表的键和值
>hset hash名 键  值
>如：>hset user:001 name zhangsan
>hget命令： 获取执行哈希名中的键对应值

hsetnx命令：设置一个哈希表中不存在的键和值
>hsetnx hash名 键  值  //成功返回1，失败返回0
>如：>hsetnx user:001 name zhangsan

hmset命令:hmset user:001 username zhangsan age 20 sex 1 批量设置
hmget user:001 username age sex:批量获取值

>hexists user:001 name //是否存在， 若存在返回1

>hlen user:001  //获取某哈希user001名中键的数量

>hdel user:001 name //删除哈希user:001 中name键

>hkeys user:002   //返回哈希名为user:002中的所有键。
>hvals user:002   //返回哈希名为user:002中的所有值。
>hgetall user:002 //返回哈希名为user:002中的所有键和值。


### 2.3 List列表（双向链表结构）

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

list即可以作为“栈”也可以作为"队列"。
操作：
>lpush list1 "world"  //在list1头部压入一个字串
>lpush list1 "hello"  // 在list1头部压入一个字串
>lrange list1 0 -1  //获取list1中内容
>​	      0:表示开头  -1表示结尾。


>rpush list2 "world"  //在list2尾部压入一个字串
>rpush list2 "hello"  // 在list2尾部压入一个字串
>lrange list2 0 -1  //获取list2中内容
>​	      0:表示开头  -1表示结尾。


>linsert list2 before hello there
>在key对应list的特定位置前或后添加字符串

>lset list2 1 "four"
>修改指定索引位置上的值

>lrem list2 2 "hello"  //删除前两个hello值
>lrem list2 -2 "hello" //删除后两个hello值
>lrem list2 0 "hello"  //删除所有hello值

>ltrim mylist8 1 3    //删除此范围外的值

>lpop list2   //从list2的头部删除元素，并返回删除元素
>rpop list2   //从list2的尾部删除元素，并返回删除元素
>rpoplpush list1 list2    //将list1的尾部一个元素移出到list2头部。并返回

>lindex list2 1 //返回list2中索引位置上的元素
>llen list2 //返回list2上长度


### 2.4  Redis 集合(Set)

Redis的Set是string类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

>sadd myset "hello" //向myset中添加一个元素
> 成功返回1，失败(重复)返回0

>smembers myset //获取myset中的所有元素(结果是无序的)

>srem myset "one" //从myset中删除一个one
> 成功返回1，失败(不存在)返回0

>spop myset //随机返回并删除myset中的一个元素
>srandmember myset //随机获取myset中的一个元素，但是不删除

> smove myset1 myset2 zhangsan:将myset1中zhangsan移动到myset2中
> scard myset1 返回myset1的个数
> sismember myset zhangsan:判断张三是否在myset中

>sdiff myset1 myset2 //返回两个集合的差集
>以myset1为标准，获取myset2中不存在的。
>sdiffstore dstset myset1 myset2 ...// 返回所有集合的差集，并保存到dstset中

>sinter myset1 myset2 myset3... // 返回N个集合中的交集
>sinterstore dstset myset1 myset2 ... // 返回N个集合的交集并存储到dstset中

> sunion myset1 myset2 ...//返回所有集合的并集
> sunionstore dstset myset1 myset2// 返回所有集合的并集，并存储到dstset中


### 2.5 Redis 有序集合Sset (sorted set)

Redis 有序集合和集合一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数(score)却可以重复。

> zadd zset 1 one 向zset中添加one，排序为1排序
> zrem zset one:删除zset中one

> zincrby zset 2 one:如果one存在，则顺序增加2，如果one不存在，那么就是2

> zrank zset one:返回one在zset中排名(从小到大的排序)
> zrevrank zset one:返回one在zset中排名(从大到小的排序)

> zrange zset 0 -1 withscores:根据score排序（根据score从小到大排序）
> zrevrange zset 0 -1 withscores:根据score排序（根据score从大到小排序）

> zrangebyscore zset 2 3 withscores:返回集合中score在给定区间的元素（包含2和5）
> zcount zset 2 3:返回集合中给定区间的数量
> zcard zset:返回集合中元素的个数
> zscore zset one:返回one元素的score
> zremrangebyrank zset 3 3:删除集合中排名在给定区间的元素
> zremrangebyscore zset 1 2:将zset中从小到大排序结果的score在1-2之间的删除


## 3.Redis事务

multi   //开启一个事务
set age 10 //暂存指令队列
set age 20
exec    //开始执行（提交事务）
或>discard //清空指令队列（事务回滚）



## 4.Redis主从复制

操作步骤：

 1.先将linux虚拟机关闭，之后克隆一个。

 2.启动两个虚拟机：master（主）和slave（从）

3.  在slave（从）中配置一下ip地址

    \# ifconfig eth0 192.168.128.229

    \# ping 一下看看通不通。

4. 配置从机

    进入：配置文件

    slaveof  192.168.128.228 6379   //配置连接主机的Redis的ip和端口

    masterauth 密码  //配置连接密码



    最后启动slave（从）机的Redis服务。


## 5.Redis乐观锁

Redis Watch 命令用于监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断
在事务前对被操作的属性做一个：

watch age
multi   //开启一个事务(在此期间有其他修改，则此处会失败)
set age 10 //暂存指令队列
set age 20
exec    //开始执行（提交事务）
或>discard //清空指令队列（事务回滚）



## 6.redis 设置密码

### 6.1 临时修改密码

### (redis服务重启后不再生效)

127.0.0.1:6379> CONFIG set requirepass "runoob"
OK
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) "runoob"
### 6.2 配置文件为Redis添加密码

修改配置文件
sudo vim /etc/redis/redis.conf

设置：requirepass redis的密码

requirepass foobared

requirepass abc123

重启服务
sudo service redis restart

登录（两种）
1.# ./redis-cli -a  密码 //连接时指定密码来进行授权
2.redis-cli 进入后发现操作不了时
  auth 密 OK

windows 下设置密码生效

修改配置文件

启动服务 加载配置文件redis-server redis.conf  \(加载一次即可\)

启动客户端



## 7.python  连接redis 增删改查

1.html页面

```
<!DOCTYPE html>

<html>

<head>

    <meta charset="utf-8">
    <title></title>

</head>

<body>

    <form action="/cgi-bin/add.py" method="post"><br>
    	用户名:<input type="text" name="username"><br>
    	密码:<input type="password" name="password"><br>
    	邮箱<input type="text" name="email"><br>
    	年龄:<input type="text" name="age"><br>
    	<br>
    	<input type="submit">
    
    </form>

</body>

</html>

```

2.add.py  注册 增加

```
!/usr/bin/python3

导入redis

import cgi,cgitb,redis

cgitb.enable()

print("Content-Type: text/html;charset=utf-8")#HTML is following

print() #blank line,end of headers

调用cgi包里的方法  来接收传递的参数

fs=cgi.FieldStorage()

定义一个空字典 ,遍历传递过来的值  获取浏览器的值 并且把他赋给字典放到字典当中

data={}

for key in fs.keys():

    data[key]=fs[key].value

执行添加操作

try:

    # python 连接redis       decode_responses=True 为了让redis解析中文          
    r=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
    # 创建一个uid  让uid 自增   自增值等于他的id  而且要给他单独放在一个链表当中也就是下面的uids
    # 每自增一次 就要放一次  因为redis数据库结构很多  这样比较方便好查找
    uid=r.incr('uid')
    
    # hmset命令:hmset user:001 username zhangsan age 20 sex 1,这个命令是哈希表中
    # 浏览器传递过来的是一个字符串
    # 通过自增的id 给用户添加到哈希列表中, 往用户名在数据库里叫user:uid
    res=r.hmset('user:'+str(uid),data)
    # 在list2尾部压入一个字串 (从后插)
    # rpush list2 "world"  
    # 在list2 头部压入一个字符串 (从前插)
    # lpush list2 "hello"
    # 把自增的uid 值 给放到uids 链表当中  uids链表名
    r.rpush('uids',uid)
    # 添加成功, 跳转
    js="""
    	<script>
    	 alert('success')
    	 location.href='/cgi-bin/index.py'
    	</script>
    """
    print(js)

except:

	print('添加失败')

```

3.增加完 进入index

```
!/usr/bin/python3

import cgi,cgitb,redis

cgitb.enable()

print("Content-Type:text/html;charset=utf-8")#HTML is following

print()  # blank line, end of headers  



python 链接redis

r = redis.Redis(host='127.0.0.1', port=6379,decode_responses=True)

获取所以的用户id   通过查询链表 uids

命令行指令 lrange list1 0 -1

uids=r.lrange('uids',0,-1)

trs=''

遍历uids获取用户数据

获取每个id  也就是自增的uid

for row in uids:

    # 命令行下的 hgetall user:002 //返回哈希名为user:002中的所有键和值。
    # 通过id  也就是这个自增的uid  获取用户的信息 给users这个变量
    users=r.hgetall('user:'+row)
    # print(users) 查询到以下信息
    # 1)"password"
    # 2)"123456"
    # 3)"username"
    # 4)"\xe6\9d\8e"
    # 给客户个页面, 把对应的信息放入进去   
    # users['password']就是对应的信息
    # 对应的占位符  {uid} {name} {upass} {uemail} {uage} {uid} 传递过去的参数
    trs+=""" 
    <tr>
    	<td>{uid}</td>
    	<td>{name}</td>
    	<td>{upass}</td>
    	<td>{uemail}</td>
    	<td>{uage}</td>
    <td><a href="/cgi-bin/del.py?id={uid}">删除</a>|<a href="/cgi-bin/update.py?id={uid}">修改</a></td>
    </tr>
    
    """.format(uid=row,name=users['username'],upass=users['password'],uemail=users['email'],uage=users['age'])

把变量加进去 返回给浏览器  给客户

html="""

<!DOCTYPE html>

<html>

<head>

    <meta charset="utf-8">
    <title>用户列表</title>

</head>

<body>

    <a href="/add.html">添加数据</a>
    <table width="500" border="1">
    	<tr>
    		<td>id</td>
    		<td>用户名</td>
    		<td>密码</td>
    		<td>邮箱</td>
    		<td>年龄</td>
    		<td>操作</td>
    	</tr>
    	"""+trs+"""
    </table>

</body>

</html>

"""

print(html)

```

4.删除操作

```
!/usr/bin/env python3

import cgi,cgitb,redis

cgitb.enable()

print("Content-Type:text/html;charset=utf-8") #HTML is fllowing

print() 						#blank line,end of headers

fs=cgi.FieldStorage()

uid=fs['id'].value

try:

    # python 链接redis
    r = redis.Redis(host='127.0.0.1', port=6379,decode_responses=True)
    # 删除用户数据 删除整个user:1 键(哈希)
    r.delete('user:'+uid)
    
    # 删除用户的id  正常命令行的语句是  lrem list2 0
    # 删除用户的id  uids链表名 uid自增值
    r.lrem('uids',uid)
    
    # 删除成功 跳转到操作页面 index.py
    js="""
    		<script>
    		alert('shanchuchenggong');
    		location.href='/cgi-bin/index.py';
    
    		</script>
    
    	"""
    print(js)

except:
	print('error')
```



5.修改 第一个页面

```
!/usr/bin/python3

import cgi,cgitb,redis

cgitb.enable()

print("Content-Type: text/html;charset=utf-8")

print()

fs=cgi.FieldStorage()

用户点击修改 传递过来个id参数 ?id  获取这个参数的值也就是 自增的值  也是id

uid=fs['id'].value

r=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)

通过找到这个自增值 id值 找到用户的信息

res=r.hgetall('user:'+uid)

把这个页面给返回过去

html='''

    <!DOCTYPE html>
    <html>
    <head>
    	<meta charset="utf-8">
    	<title>用户编辑</title>
    </head>
    <body>
    	<form action="/cgi-bin/doupdate.py" method="post">
    		用户名:<input type="text" name="username" value="{uname}"><br>
    		密码:<input type="password" name="password" value="{upass}"><br>
    		邮箱:<input type="text" name="email" value="{uemail}"><br>
    		年龄:<input type="text" name="age" value="{uage}"><br>
    		
    		<br>
    		<input type="hidden" name="id" value="{uid}">
    		<input type="submit">
    
    	</form>
    </body>
    </html>

'''.format(uname=res['username'],upass=res['password'],uemail=res['email'],uage=res['age'],uid=uid)

print(html)

```

6.修改页面

```
!/usr/bin/python3

import cgi,cgitb,redis

cgitb.enable()

print("Content-Type:text/html;charset=utf-8")

print()

用户改完一提交 到了这个程序进行修改的页面

fs=cgi.FieldStorage()

定义一个变量  获取用户输入的信息

inputs={}

遍历他输入的信息

for key in fs.keys():

    # 不要id 只需要修改对应的哈希数据 user:11
    if key!='id':
    	# 获取完用户输入的值 给放到这个input中
    	inputs[key]=fs[key].value

try:

    #  python 连接redis
    r=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
     # 执行修改 只需要修改对应的哈希数据 user:11  inputs 是对应的信息
    res=r.hmset('user:'+fs['id'].value,inputs)
    
    js="""
    <script>
    	alert('gengxin chenggong');
    	location.href='/cgi-bin/index.py';
    
    </script>
    """
    
    print(js)

except:

    print('error')



```


# --------------------------------------

# 数据结构

## 1.目录

```
# anaconda 
- 安装
- 创建虚拟环境命令
   - `conda create -n p05 pyhton=3.6`
   - 新建虚拟环境命令
- pychar配置虚拟环境
    - file-settings-project:xx-python interpreter-右上角local-anaconda位置
    
# 推荐书籍
- 严蔚敏-数据结构
- 裘宗燕 - 数据结构与算法 python语言描述

# 数据结构和算法
- 程序=数据结构+算法
- 数据结构：
    - 抽象逻辑结构
    - 物理存储结构
- 算法：
    - 如何操作数据
- 抽象数据类型（AbstractDataType=ADT)
    - 数据+基本抽象操作
    - list，set，dict
- 案例01

# 算法的衡量
- 考虑数据量
- 逼近函数
- O(n)
- 时间复杂度
    - 最优时间复杂度
    - 最坏时间复杂度
    - 平均时间复杂度
- 时间复杂度的计算方法
    - 恒定的数字，我们忽略掉
    - 顺序结构，时间复杂度按加法计算
    - 循环算一个n
    - 嵌套属于乘法运算
    - 分支结构，取最大值
    - 判断算法，关注数量的最高次项，其余忽略
# 顺序表
- 简单顺序表
- 索引顺序表
    - 部分排序，索引有序，内容可以无序
- 链表顺序表
    - 链表
    - 案例02
- 遍历
    - 从某个节点开始，挨个访问结构体数据
    
- 插入
    - 从头
    - 从尾
    - 中间
        - 顺序
        - 非顺序
        
# queue队列
- 先进先出（FIFO=first in first out)
- 实现了先进先出的一个数据结构叫做队列
- in
- out
- 案例03
# statck 栈
- 一个口
- 先进后出（FILO=First in loast out)
- 用list可以模拟
- 案例04

# 作业：
1. 完整运行链表的案例02，调试并测试
2. 把queue，stack用单项非循环链表实现，不能使用现成的函数或类
    - 代码001
# 排序算法
- 冒泡排序
    - 每次从第一个元素开始
    - 逐步跟其余的未排序的元素比较
    - 如果第一个元素小于比较的元素，则交换位置
    - 否则，被比较的元素为冒泡的元素
    - 重复执行，知道全部元素排序完毕
    - 05
- 选择排序
    - 每次找出最小的数字，并记录数字位置
    - 最小数字跟末位一个元素进行交换
    - 需要查找的数据量减少一个  
- 插入排序：
    - 假定已经排好序的前半部分列表为a，未排序的列表，即后半部分为b
    - 从b中取第一个数据b1
    - 对于a列表，从后向前比较
        - 假如a[x] 大于 b1
            - a[x] 向后移动一位
        - 否则：
            - 退出循环
    - 此时，退出的位置就是需要插入的位置，把b1插入
            
          
 
# 查找算法
- 无序表查找
    - 挨个比对
- 有序表查找
    - 案例06
    - 折半查找
        - 每次取一个中间值，要查找的数据和中间值进行比对，根据对比结果确定是否向前走和向后走
        
# hash
- 一个函数，y = f(x),即把一个值作为输入，返回一个经过换算的值，通常这个值是一个数字
- 碰撞检测
    - 好的算法
    - 大空间
# 树
```

## 2. 百钱买百鸡

```

import time

# 百钱买百鸡

def checken(n):
    for i in range(0, 20):
        for k in range(0,34):
            for m in range(0,n):
                if  i + m + k ==n and 5*i + 3*k + m//3 == n:
                    print(i,k,m)
                else:
                    time.sleep(1)
                    continue



if __name__ == "__main__":

    checken(100)

```



## 2.单项链表

```


class Node(object):
    '''
     一个节点类
     节点是链表中的某一个数据点，代表链表中的一个单位

    '''
    def __init__(self, data):

        '''
        节点分两部分
        1. data：用来盛放数据，可以是任意类型
        2. next： 表示节点在链表中应该指向的下一节点的位置
        初始化的时候节点的next应该赋值为空，表示下面没有了。
        :param data:
        '''
        self.data = data
        self.next = None

    def printNode(self):
        print(self.data, end=" ")

    def printNext(self):
        print(self.next)

class LinkList(object):

    '''
    形容一个链表的类，单向非循环
    '''
    def __init__(self):
        '''
        初始化的时候链表为空
        直接把header赋值为空就可以
        '''
        self.header = None

    def addBefore(self, node):
        '''
        在一个单向非循环链表中插入数据
        一共分为两步：
        1. 要插入的节点的下一个指向原来链表的第一个节点
        2. 原来链表的指向第一个节点的指针（引用）指向要插入的节点
        :param node: 要插入的节点元素
        :return: 无
        '''
        node.next = self.header
        self.header = node

    def addAfter(self, node):
        if self.header==None:
        # if not self.header:
            self.header=node
            return  None
        point=self.header
        while point.next!=None:
            point=point.next
        point.next=node

    def insert(self, node, pos):
        if self.header==None:
            self.header=node
            return
        count=0
        point=self.header
        while point.next:
            count+=1
            if count==pos+1:
                node.next=point.next
                point.next=node
                return
            point=point.next
        point.next=node

    def insertsort(self):
        if self.hearer==None:
            self.header=node
        if self.header.data>node.data:
            node.next=self.header
            self.header=node
            return
        point=self.header
        while p.data<node.data  and   point.next!=None:
            point=point.next
        node.next=point.next
        point.next=node
        return


    def printList(self):
        '''
        1. 用变量point指向第一个元素
        2. 当point不为空的时候
            2.1 打印内容
            2.2 point指向下一个节点
        :return:
        '''
        point = self.header
        while point:
            print(point.data, end = " ")
            point = point.next




if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    nl = LinkList()
    # 代码一测试
    # nl.addBefore(node1)
    # nl.addBefore(node2)
    # nl.addBefore(node3)
    # nl.addBefore(node4)
    # nl.addBefore(node5)
    # nl.addBefore(node6)
    # 代码二测试
    nl.addAfter(node1)
    nl.addAfter(node2,)
    nl.printList()

```



## 3. 链表的插入多种

```


class Node(object):
    '''
     一个节点类
     节点是链表中的某一个数据点，代表链表中的一个单位

    '''
    def __init__(self, data):

        '''
        节点分两部分
        1. data：用来盛放数据，可以是任意类型
        2. next： 表示节点在链表中应该指向的下一节点的位置
        初始化的时候节点的next应该赋值为空，表示下面没有了。
        :param data:
        '''
        self.data = data
        self.next = None

    def printNode(self):
        print(self.data, end=" ")

    def printNext(self):
        print(self.next)

class LinkList(object):

    '''
    形容一个链表的类，单向非循环
    '''
    def __init__(self):
        '''
        初始化的时候链表为空
        直接把header赋值为空就可以
        '''
        self.header = None

    def addBefore(self, node):
        '''
        在一个单向非循环链表中插入数据
        一共分为两步：
        1. 要插入的节点的下一个指向原来链表的第一个节点
        2. 原来链表的指向第一个节点的指针（引用）指向要插入的节点
        :param node: 要插入的节点元素
        :return: 无
        '''
        node.next = self.header
        self.header = node

    def addAfter(self, node):
        '''
         操作步骤：
         0. 如果header为空，则直接添加
         1. point作为一个标记，记录你查找的当前node
         2. 如果node不是最后一个，则往下走
         3. 如果是最后一个，则把要插入的node插入
        :param node:
        :return:
        '''

        # 下面两句话一个效果
        #if self.header == None:
        if not self.header:
            self.header = node
            return None

        point = self.header
        while point.next != None:
            point = point.next

        point.next = node

        return  None


    def insert(self, node, pos):
        '''
        无序链表插入，必须给出位置
        1. 判断链表是否为空
        2. 遍历链表，计数
        3. 根据计数或者链表状态进行插入
        :param node:
        :param pos:
        :return:
        '''

        # 链表为空的情况
        if self.header == None:
            self.header = node
            return

        # 链表不为空
        # count的位置需要仔细考虑
        # 实际使用应该看具体情况
        count = 0
        p = self.header
        while p.next:
            count += 1
            if count == pos + 1:
                #  插入
                node.next = p.next
                p.next = node
                return

            p = p.next

        # 代码如果执行到这里，说明是count位置超过链表长度
        # 此时只能把节点放入队尾
        p.next = node
        return




    def insertSorted(self, node):
        '''
        插入有序表分几种情况处理
        1. 空链表
        2. 第一个元素大于要插入的数据
        3.  其余情况是第三种可能，不用区分

        :param node:
        :return:
        '''

        # 链表为空
        # 此时只需要简单插入就好
        if self.header == None:
            self.header = node
            return

        # 第一个元素大于要插入的数据
        if self.header.data >= node.data:
            node.next = self.header
            self.header = node

        #  此时前提条件是第一个元素小于要插入的数据
        # 首先需要遍历链表找到位置
        # 假定链表是升序
        p = self.header
        while p.data < node.data and p.next != None:
            if p.next.data > node.data:
                node.next = p.next
                p.next = node
                return None

            p = p.next


        # 因为循环内有出口，所以运行到这段代码就可以肯定是没有找到比插入元素大的内容
        p.next = node
        return


    def printList(self):
        '''
        1. 用变量point指向第一个元素
        2. 当point不为空的时候
            2.1 打印内容
            2.2 point指向下一个节点
        :return:
        '''
        point = self.header
        while point:
            print(point.data, end = " ")
            point = point.next


    def delHead(self):
        '''
         1. 需要判断链表是否为空，是，return None
         2. 删除头并返回头部内容
        :return:
        '''

        if not self.header:
            return None

        p = self.header
        self.header = self.header.next
        return p.data

    def delTail(self):
        '''
        0. 为空返回None
        1. 遍历到尾部
        2. 删除后返回末位元素
        :return:
        '''
        if not self.header:
            return  None

        if self.header.next == None:
            p = self.header
            self.header = None
            return p.data

        pPre = None
        p = self.header
        while p.next:
            pPre, p = p, p.next

        pPre.next = None
        return p.data



    def delPos(self, value):
        '''
        1. 空链表, return None
        2. 只有一个元素，且是被删除对象
        2. 遍历链表， 找到则删除，否则就不做操作
        :param pos:
        :return:
        '''

        if not self.header:
            return None

        if self.header.next == None:
            if self.header.data == value:
                self.header = None

            return None


        pPre = None
        p = self.header

        while p.next and p.data != value:
            pPre, p = p, p.next

        if p.data == value:
            pPre.next = p.next
        return None

if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(8)

    nl = LinkList()
    nl.insertSorted(node1)
    nl.insertSorted(node2)
    nl.insertSorted(node3)

    node5 = Node(5)

    nl.insertSorted(node5)
    nl.printList()
    print()
```



## 4 模仿队列类 底层实现

```
# 模仿队列类
class MyQueue(object):

    def __init__(self):
        # 用list来盛放具体数据

        self.q = list()

    def inQ(self, data):
        # 把队列设计成从后追加，从前拿出就可以
        self.q.append(data)
        # 可有可无
        return None

    def outQ(self):
        # 如果长度为空 也就是为0

        if len(self.q) == 0:
            return None
            # 队列是先进先出  所以要给先弹出前面的 所以是0
        return  self.q.pop(0)




if __name__ == "__main__":
    q = MyQueue()

    q.inQ(1)
    q.inQ(2)
    q.inQ(3)
    q.inQ(4)

    print(q.outQ())
    print(q.outQ())
    print(q.outQ())
    print(q.outQ())

```



## 5.模仿栈类    底层实现

```
# 模仿栈类
class MyStack():
    def __init__(self):
        self.s = list()


    def popSt(self):
        '''
        弹栈，即把最顶层数据返回病删除就好
        :return:
        '''
        # 判断 如果长度为0 
        if len(self.s) == 0:
            # 返回个none
            return None
        # 栈是先进后出  所以要给弹出后进来的

        return self.s.pop()


    def pushSt(self,data ):
        '''
        压栈， 把数据放入栈的最顶层，
        :param data:
        :return:
        '''
        self.s.append(data)


if __name__ == "__main__":
    st = MyStack()

    st.pushSt(1)
    st.pushSt(2)
    st.pushSt(3)
    st.pushSt(4)
    st.pushSt(5)
    st.pushSt(6)
    print(st.popSt())
    print(st.popSt())
    print(st.popSt())
    print(st.popSt())
    print(st.popSt())
```



## 6. 代码调试

```
# 分类
- 调试（debug）
    - 语法错误
    - 逻辑错误
- 测试（test）
    - 一般由第三方执行
    - 可以完全不懂代码
 
# 调试
- pdb
- pycharm
    - debug模式，允许用户按照自己的意愿让程序执行
- 断点（breakpoint，bp）：程序执行到断点出自动暂停，等待用户进一步输入
- 跟进(StepInto, F7)/跳过(StepOver, F8)：
- 跳出（StepOut）： 跳出正在执行的函数，即函数直接执行完毕
- ResumeProgram()：继续函数，继续到下一个断点为止
```



## 7.各种排序

```

'''- 冒泡排序
    - 每次从第一个元素开始
    - 逐步跟其余的未排序的元素比较
    - 如果第一个元素小于比较的元素，则交换位置
    - 否则，被比较的元素为冒泡的元素
    - 重复执行，知道全部元素排序完毕
'''

# 冒泡排序
def bubbleSort(al):
    # 取的轮数  大小数字为例
    for n in range(1, len(al)):
        #  一轮中间的次数 取完几次 相当于 少几个数 所以要减去n 
        for i in range(0, len(al)-n):
            # 逐个比较  如果这个数小于将要比较的数  那么给他俩调换个位置
            if al[i] < al[i+1]:
                # 交换两个变量值
                # 等同于：
                # tmp = a[i]
                # a[i] = a[i+1]
                # a[i+1] = tmp
                al[i], al[i+1] = al[i+1], al[i]
            else:
                # 比完了 继续循环  
                continue
    # 都循环完了 之后给这个排序完的al  返回

    return al


# 选择排序  排序完之后把小的给放到后面去  在来小的 直接给他选择到之前小的后面去 这个比上面的要快一些

def selectSort(al):
    # 从总共数据中挑选出最小的数字，一共需要挑选多少次
    for i in range(1, len(al)):
        # 记录最小数的位置
        min = 0
        # 从未排序的数字中选出最小值，记录下最小值的位置就可以
        for n in range(0, len(al)-i+1):
            # 如果最小数的位置的数大于那个被比较刚拿出来的数 
            if al[min] > al[n]:
                # 那么把这个n给赋值成最小位置  
                min = n
        # 每次需要把最小值跟位置上的倒数第一个交换
        # 此时的倒数第一个是未排序数字中的倒数第一个
        # al[len(al) - i] 这个是索引
        al[min], al[len(al) - i] = al[len(al) - i], al[min]
        print(al)

    return al


# 插入排序

def insertSort(al):
    if len(al) <= 1:
        return al

    # 假定第一个数字已经排好顺序
    # 则需要排序的数据从al[1]开始
    for i in range(1, len(al)):
        # 把需要插入的数据保持下来，避免被覆盖
        tmp = al[i]
        # 需要记录需要插入的位置，这个位置不能直接使用for循环中的变量，避免出现意外
        pos = 0
        # 需要检查前面已经拍好顺序的列表，检查从后向前
        for n in range(i, 0, -1):
            # 如果排好顺序的列表内容比需要插入的数据大，则直接向后移动一个位置
            # 否则就结束循环，同时记录下需要插入的位置
            if al[n-1] > tmp:
                al[n] = al[n-1]

            else:
                pos = n
                break
        # 前面已经找到需要插入的位置，
        # 把需要插入的数据放入指定位置即可
        al[pos] = tmp

    return al


if __name__ == "__main__":

    sortFun = insertSort


    l = [9,2,4,5]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)

    l = []
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)



    l = [9]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)

    l = [8,7]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)

    l = [7,8]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)

    l = [3,6,4]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)

    l = [6,6,6,6,6]
    print(l)
    sortFun(l)
    print(l)
    print("*" * 30)
    
```



快速排序

```
# 快速排序
def qucikSort(al,start,end):
    # 递归退出条件
    if start>=end:
        # 如果第一个值大于他或者他俩交叉也就是他俩一样
        # 直接算是排好给返回出去
        return
    # 设置起始位置和终点位置，因为l,h作为标志
    # l是索引 h 也是索引  因为位置会发生变动所以会发生变化 不是固定的
    l=start
    h=end
    #这个mid 从起始位置开始给设置成哨兵的位置
    mid=al[l]
    # 当起点位置小于终点的位置的时候进行循环
    # 循环一次的内容为
    # 1。先从后向前检查数据，如果数据大于mid则继续向前，否则移动数据后停止
    # 2。然后从前后检查数据，如果数据小于mid则向后继续移动，否则移动数据后终止


    while l<h:
        while l<h and  al[h]>=mid:
            # 从后向前
            h-=1
        # 移动数据
        # 因为是从后向前检查,所以要把后面的值通过进行比较给赋值给前面
        al[l]=al[h]
        while l<h  and  al[l]<mid:
            l+=1
        # 从前向后检查数据 如果小于标杆mid  则向后继续移动数据并且把值给赋给它
        al[h]=al[l]
    # 把哨兵位置放入  程序结束
    al[l]=mid
    # 调用块排函数
    qucikSort(al,start,l-1)
    # 因为前面变了  每次都向后移动一个  end  也在开始变化
    qucikSort(al,l+1,end)

```



## 8. 查找

```

# 查找
# 定义了一个函数 里面传的列表   和数据
def  s1(al, data):
    # 遍历这个列表的长度   得到索引  
    for i in range(0, len(al)):
        # 如果 数据等于这个列表里的其中的一个数据  
        if data == al[i]:
            # 那么 我们给他返回 索引值 
            return i
    # 没有 跳出循环  给他个负1  告诉他没有
    return -1


# 通过中间查找 这样会快 
def zheban_01(al, data):
    # 找到中间位置，这个位置可以不太准确
    # 这个mid  把列表除2 取商 商是除多少 这一半就有多少了  mid是位置
  
        

    # 因为列表已经排序，跟进中间位置的值可以推测要查找的值的相对前后位置
    # 如果这个平均的数值大于 这个 数据  因为我们正常是 正序  1,2,3.....
    if al[mid]  > data:
        # 如果通过索引的这个中间值大于输入的这个数据   那么这个数据肯定在中间值的前面  因为是正序
        # 1,2,3,4
        # 0,1,2,3
        # 位置减1 是索引 倒叙所以是到-1 正常是从0-5取到了 四  这个要想取到0所以是-1
        for i in range(mid-1, -1, -1):
            if al[i] == data:
                return i
        # 找不到给他负一
        return -1
    else:
        for i in range(mid, len(al)):
            if al[i] == data:
                return i
        return -2

    return -3

if __name__ == "__main__":

    al = [4,6,8,9,12,23,67,87,764]

    rst = zheban_01(al, 4)
    print(rst)

```



## 9.   树

### 9.1 树的概念
- 每个节点都有另个或者多个子节点
- 没有父节点的节点成为根（节点）
- 每一个非根节点有且只有一个父节点
- 除了根节点，每个子节点可以分为多个不相交的子树

### 9.2 树的术语
- 节点的度： 节点孩子的个数
- 树的度：在所有节点中，最大度数就是树的度
- 叶子或者终端节点： 没孩子的节点
- 父节点或父亲节点： 一个节点是他子节点的父亲节点
- 孩子或者子节点：
- 兄弟节点：同一个父亲节点的所有节点
- 堂兄弟节点： 父亲节点是兄弟节点的节点
- 节点的层次： 从根节点算起，根节点为第一层，根的子节点为第二层，以此类推
- 树的高度或深度：树中节点的最大层次
- 森林：多棵树

### 9.3 树的种类
- 序的含义有两种
    - 访问节点的先后顺序，此为前提
    - 节点按照一定访问顺序的值的大小
- 无序树： 树中任意节点间没有顺序
- 有序树：任意节点，按照一定访问顺序，有顺序或者大小
    - 二叉树： 每个节点最多两个孩子
        - 完全二叉树：对于一棵树，除叶子节点，
        - 平衡二叉树：任何节点的两颗子树高度最多相差1
        - 排序二叉树：有顺序的二叉树
    - B树： 一种对于读写操作进行优化的自平衡的二叉查找树，能搞保持数据有序

- 常见应用场景：
    - xml, html 解析使用树
    - 路由协议实现查找算法
    - mysql索引
    - 文件的目录结构
    - 很多经典AI算法，俗称决策树
### 9.4 二叉树
- 二叉树的每个节点最多有两个子书的树结构，通常左孩子组成的子树成为“左子树”，
   右变孩子组成的子树成为“右子树”

### 9.5 二叉树的节点表示
- 案例02

### 9.6二叉树的遍历
- 深度优先，一般考虑递归访问
    - 先序(Preorder)
    - 中序(Inorder)
    - 后序(Postorder)
- 广度优先 

# 网络编程
- socket编程
- http协议内容
- 了解webserver后端流程和事物处理模块
- 推荐书籍- 图解http协议

## socket编程
- 七层网络模型- 理论模型
    - 物理层
    - 链路
    - 传输层
    - 网络车
    - 会话层
    - 表示层
    - 应用层
- 四层模型
    - 物理层
    - 链路
    - 表示
    - 应用
- 协议
    - 为了保证数据传输，网络连接而产生的一系列规定
    - 协议可能存在漏洞、问题
    - 协议族
        - 一系列协议统称
        - TCP/IP(TransferControlProtocal/Interxxxx)
        - HTTP

- socket
    - 特指网络中，通过特定的端口+地址进行通信
    - 地址：ip地址，四段数字，取值范围0-255
    - 端口： 用来确定计算机中相应应用程序的编号
        - 理论值 0 - 65535
        - 1000以下
        - 建议10000
    - python支持socket编程
        - tcp：安全，面向链路
            - 三次握手
        - udp： 不安全
- udp编程
    - server服务器端：
        - 创建socket
        - 绑定
        - 收数据
        - 反馈
    - client客户端：
        - 创建socket
        - 发送数据
        - 接受对方返回



### UDP编程方式

UDP编程方式 服务器端py文件 需要在命令行先运行  之后直接运行客户端文件

```
# UDP  先导入socket
import  socket
import time
# 1.创建socket  socket 是传输层和应用层之间的桥梁
# 参数2个 family: 协议,AF_INET      代表ipv4 也就是ip地址 里面是4个数字192.168.*.*  4个
# 传输数据的方式，SOCK_DGRAM 代表用udp方式传输
# udp方式不安全　传输数据量少　快　
skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 创建地址
# 地址应该是一个tuple类型,分别为ip和端口35
# 第一个数字为字符串,127.0.0.1代表自己机器
# 第二个数字代表端口,是一个整数,推荐大于10000(用来确定计算机中相应应用程序的编号)理论值 0 - 65535
addr=("127.0.0.1",7852)
#把已经创建的socket注册到相应地址和端口上
skt.bind(addr)
# 一旦绑定好 那么久在我这个服务器上打印
print('已经绑定好的地址')
# recvfrom里面的参数代表每次接受数据的临时空间的大小,不影响接收数据的多少和结果
# 如果没有访问数据,则等待 回信地址就是我接收到了客户端的数据data还有他的地址add_clt
# 这个while 死循环 等这个程序运行完了 让他继续运行等待  也就相当于服务器一直启动着呢
while True:
    (data,add_clt)=skt.recvfrom(100)
    # 打印测试
    print(data.decode())
    # 我给他的数据
    rstMsg="i am fine ,thank  you"
    # 我把我要发送的数据给转成utf-8字符级 要不然出现乱码
    bRstMsg=rstMsg.encode("utf-8")
    # 把反馈的数据发送给用户,同时记录反馈的数量 这里是字节
    count=skt.sendto(bRstMsg,add_clt)
    print('反馈了{0}'.format(count))
```



UDP 客户端py文件

```
import  socket
# 1.创建socket  socket 是传输层和应用层之间的桥梁
# 参数2个 family: 协议,AF_INET      代表ipv4 也就是ip地址 里面是4个数字192.168.*.*  4个
# 传输数据的方式，SOCK_DGRAM 代表用udp方式传输
# udp方式不安全　传输数据量少　快　
skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 客户端的数据
msg=b"Hello world"
# 发送的内容和对面的地址   端口号
skt.sendto(msg,("127.0.0.1",7852))
rstMsg=skt.recvfrom(90)
# 因为接受过来个元祖  我给他解码
ra=rstMsg[0].decode("utf-8")
print(ra)
```





- tcp编程
    - server
        - 创建socket实例
        - 绑定端口
        - 监听对方链接信号
        - 接受对方连接请求
        - 接收刚才建立的链路传输过来的数据
        - 通过刚才建立的链路反馈给对方信息
        - 销毁链路
    - client
        - 创建通信socket
        - 请求对方建立链接链路
        - 通过已经建立的俩路发送数据
        - 通过建立的链路接收数据
        - 关闭链路



### TCP编程方式

TCP编程方式 服务器端py文件 需要在命令行先运行  之后直接运行客户端文件

```
# TCP编程方式
import socket
# 1.创建socket 实例  socket 是传输层和应用层之间的桥梁
# 参数2个 family: 协议,AF_INET      代表ipv4 也就是ip地址 里面是4个数字192.168.*.*  4个
# 传输数据的方式，SOCK_STREAM 代表用TCP方式传输
# TCP方式安全　传输数据量　慢
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 创建地址
# 地址应该是一个tuple类型,分别为ip和端口35
# 第一个数字为字符串,127.0.0.1代表自己机器
# 第二个数字代表端口,是一个整数,推荐大于10000(用来确定计算机中相应应用程序的编号)理论值 0 - 65535
addr=("127.0.0.1",7853)
#把已经创建的socket注册到相应地址和端口上
skt.bind(addr)
# 监听请求
skt.listen()
# 等待并接收对方的连接请求
#in_skt是一个管道, 通过管道来进行接收数据,和发送数据
(in_skt,in_addr)=skt.accept()
# 一旦绑定好 那么久在我这个服务器上打印
print('已经绑定好的地址')
# 利用建立的链接in_skt传输数据  接收
msg=in_skt.recv(100)
# "i love china" 是这打印出来的内容  是那么发送过来的
print(msg)
# 我要给那边回馈的内容
rstMsg="欢迎大爷来玩"
# 给回馈的内容进行编码
in_skt.send(rstMsg.encode("utf-8"))
# 这次服务器服务结束
print("服务结束")
# 关闭管道
in_skt.close()
```



TCP 客户端py文件

```
import socket
skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=("127.0.0.1",7853)
# 连接那个server地址
skt.connect(addr)
clt_skt=skt
# 我要发送的内容
msg="i love china"
# 把握要发送的内容给进行编码给他
clt_skt.send(msg.encode("utf-8"))
# 接受内容
rst=clt_skt.recv(100)
#把握要接收的内容给转下编码
print(rst.decode("utf-8"))
clt_skt.close()

```

# HTTP协议

# 1.1 代码过程

1. socket编程，编写client和server，双方使用tcp通信，传递简单消息
2. socket编程，编写server端，用浏览器代替client，server可以接受所有传入的信息
   - 此时server接收的信息已经包含http协议内容，不过需要解读
   - 解读步骤如下：
     1. 整个decode后读出
     2. 按行读取，以CRLF为行结束标志
     3. 把按行读出的内容用dict格式存储
3. 把程序重构，改写成oop
4. 尝试用http协议反馈
   - 拼装http协议头内容，内容为简单字符串或者无内容
   - 内容为静态页面
5. 增加404或者500错误
   - 404或者500页面先做成html文件，直接读取
   - 侧重点是返回的时机
   - 500错误返回建议使用异常模拟
6. 模板
   - 写好模板
   - 装载模板，即把模板内容以文件方式读出来
   - 调用的时候用数据填充模板
   - 返回
   - 需要注意数据来源
7. 静态资源的概念
   - 静态资源指图片，音频视频等不需要频繁修改的内容


## 1.1.1整个http流程代码

```
# 模拟整个浏览器访问服务器 服务器接受浏览器 并且进行处理 在给予返回的流程
# 用户访问浏览器，浏览器请求服务器，浏览器给发送报文，
import  socket
# 这个类是WebServer这个类的服务器地址和端口号,给他放到这个这个类里,便于把代码交给别人以后好便于修改
# 不至于让代码出现差错
# 用法:  直接在底下的WebServe 实例化对象的时候直接给当参数传入进去就ok了
class ServerContent:
    address="127.0.0.1"
    port=7222

# HTTP协议 服务器给浏览器发送的内容 也就是响应报文
# 到时候需要的化直接从这个类里来进行调用就OK了
class  SocketContent:
    HeadInfo="HTTP/1.1"
    CODE_OK=200
    STATUS_OK="OK"
    Content_length="Content-Length: "
    Content_Type_HTML="text/html"

# 服务器的 Webserver 类 :
class Webserver():
    # 1.初始化所必需的服务器地址,端口  注意这里是一个元组
    # 2.并且创建一个socket的实例 是传输层和应用层之间的桥梁
    # 参数2个 family: 协议,AF_INET      代表ipv4 也就是ip地址 里面是4个数字192.168.*.*  4个
    # 第二个参数是 代表 传输数据的方式，SOCK_STREAM 代表用TCP方式传输
    #3.把已经创建的socket注册到相应地址和端口上
    def __init__(self,address=("127.0.0.1",7852)):
        self.addr=address
        self.skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.skt.bind(self.addr)
    def start(self):
        # 开启监听
        self.skt.listen()
        while True:
            #  和这个接收数据的管道,浏览器的地址
            self.in_skt,self.addr=self.skt.accept()
            # 实例化SocketHandler  得到一个对象  我把管道in_skt当作当前对象需要接收的参数
            # 因为我要做处理 , 全写在一起  代码不整洁
            # 从而实现两者的传输关连！(暂时理解)
            sh=SocketHandler(self.in_skt)
            # 这里是要调用底下的处理事情这个SocketHandler 的方法
            sh.do()
class SocketHandler():
    # skt形参   用来接收我上面实例化对象的实参 也就是in_skt 这个管道
    def __init__(self,skt):
        self.skt=skt
        # 这里初始化一个列表  用来装服务器这边对传递过来的响应报文进行处理，之后给他装入进去
        self.lines=[]
        self.items={}
        self.rsp=""

    # 这个函数是给传递过来的数据/信息进行操作的所有步骤 到最后直接被调用了
    def do(self):
        # 先是对传递过来的Http相应报文进行处理
        self.parseHttp()
        # 完成业务处理
        self.chuli()
        # 发送处理完的结果
        self.sendRsp()
        # 关闭传入的请求
        self.skt.close()


    # 为了让服务器能看明白浏览器传递过来的报文 则需要对它进行处理 底下的是整个处理流程
    def parseHttp(self):
        # 把获取的所有行给放入到列表中 , 这里的getlines 先是调用了getline 获取单行 之后给放入到lines这个列表中
        self.getLines()
        # 打印这个列表
        # print(self.lines)
        # 对列表进行处理
        self.parseLines()
        # print("$"*20)
        # 处理之后测试一下
        # print(self.lines)
        # 测试对比 打印字典
        # print(self.items)
    def getLines(self):
        # 获取单行
        line=self.getLine()
        # 一行一行的来循环,循环之后给加入进去
        while line:
            self.lines.append(line)
            # 加入之后再次调用  获取下一行
            line=self.getLine()
        # 没有了就代表函数结束了 给个返回值  这里不给None也行
        return  None


    # 这里获取单行的时候需要过滤
    def getLine(self):
        # 定义两变量  一个是a 一个是b  拿a去过滤 给他存到b里 如果b是\r a是\n 那就满足了\r\n
        # 那么我就给我定义的这个rst这一行给返回过去
        a=b""
        b=b""
        rst=b""
        
        # 利用skt的recv方法来挨个字节接收 recv(1)这个代表每次只接收一个字节
        a=self.skt.recv(1)
        while a:
            # 过滤掉\r和\n
            if a==b"\n":
                if b==b"\r":
                    # 条件满足  返回一行  继续循环
                    return rst.decode().strip("\r")
            # b最开始是空的  把b加入进去  所以把b写到了底下
            rst+=b
            # 把a给b  此时a为空  再次调用a来接收
            b=a
            a=self.skt.recv(1)
        # 如果都没有的话  为空   空就不进入循环了  直接返回
        # return rst.decode()

    # 之后我对这个列表进行处理,给他转换成字典 转化成字典的原因是给他发送过来的报文给专成字典
    # 之后我们来通过客户的请求方式来判断 他想要做什么  是GET请求啊 还是 想要访问那个url啊
    # HTTP/1.1是他告诉我要给他返回响应报文的时候要给他HTTP/1.1的版本
    def  parseLines(self):
        # 处理成列表长度为0 意思是那边什么都没给我
        if len(self.lines)==0:
            return  None
        # 对原列表进行复制 也就是取片  不想破坏它
        lines=self.lines[:]
        while len(lines):
            line=lines.pop()
            # 把那个列表带冒号和空格的给切割
            tmp=line.split(": ")
            # Host: 127.0.0.1:8209   例如这个   如果是冒号空格按这个切   那么就是到列表的长度为2
            if  len(tmp)==2:
                # tmp[0]是键  ,tmp[1] 是值
                self.items[tmp[0]]=tmp[1]
                # 转完了之后跳过循环,继续判断 因为这是循环的是行 继续下一行
                continue
            # 把空格给切开
            tmp=line.split(" ")
            # 'GET / HTTP/1.1', 例如这个 如果是按空格切割 那么到列表里的长度就是三个
            # 这几个键是我设置的  给他放到字典里
            # 'method': 'GET', 'url': '/favicon.ico', 'http': 'HTTP/1.1'
            if len(tmp)==3:
                # 请求 行  GET /index.html HTTP/1.1
                # GET   url  http
                self.items["method"]=tmp[0]
                self.items["url"]=tmp[1]
                self.items["http"]=tmp[2]
                continue
        """
    # 转完字典之后 我开始进入判断浏览器客户端那边具体想要做什么,我开始处理
    def chuli(self):
        # 如果发送的是GET请求 我上我解析之后的这个字典里来找  'method': 'GET',
        if self.items.get("method",None)=="GET":
            # 字典里的get方法 获取这个url键的值 如果没有我给他个"/" ,这个"/"
            fn=self.items.get("url","/")
            # 浏览器会自动请求这个文件
            if fn=="/favicon.ico":
                msg="吗的烦啊"
                # 调用mksp函数把它给加入到我这个协议下面
                self.mkrsp(msg)
                # 之后给它发送过去
                self.sendRsp()
                # 让这个函数结束 不往下走了
                return  None
            url=fn.lstrip("/")
            if  url=="" or url=="index.html":
                url="index.html"
            if url not in ["test.html","index.html","01.html"]:
                url="404.html"
            # 打开我这个文件 读模式 这必须加这个utf-8读取文件时候
            with open(url,"r",encoding="utf-8")as f:
                msg=f.read()
                self.mkrsp(msg)
                self.sendRsp()
                return  None
        print("EROEROERO...")

        # ico静态文件单独代码
    def chuli(self):
        if self.items.get("method", None) == "GET":
            fn = self.items.get("url", "/")
            if fn == "/favicon.ico":
                import os
                url = os.path.join("./static", "liuying.ico")
                msg = ""
                with open(url, "rb",encoding) as f:
                    msg = f.read()

                rsp = "HTTP/1.1 200 OK"
                rsp += "\r\n"
                rsp += "Date: 20171211"
                rsp += "\r\n"
                rsp += "Content-Type: text/html"
                rsp += "\r\n"
                rsp += "Set-Cookie: ws by liuying"
                rsp += "\r\n"
                rsp += "Content-Length: " + str(len(msg))
                rsp += "\r\n"
                rsp += "\r\n"

                rsp = rsp.encode() + msg
                self.skt.send(rsp)
                return None
        else:
            self.mkRsp("hello")
            self.sendRsp()
            return None

    """


    # 版本二 chuli + loadTpl + mkTpl 这三个函数  来让页面活起来
    def chuli(self):
        if self.items.get("method",None)=="GET":
            # 处理的时候传入实参 给到下面mkTpl的形参
            # 也就是底下mkTpl函数的返回值被msg接收
            msg=self.mkTpl("welcome.html",["彦祖","汉良"])
            self.mkrsp(msg)
            self.sendRsp()

    # 读取模板  把模板内容读到字符串中，准备将相应的数据内容替换掉
    def loadTpl(self,tpl_name):
        # 定义一个字符串
        rst=""
        # 这必须加这个utf-8读取文件时候
        with open(tpl_name,"r",encoding="utf-8") as f:
            # 读完了给放到变量中
            rst=f.read()
        #之后把值给返回出去
        return  rst
    # 读取完了我现在有个字符串了,下一步开始替换
    # 这里定义了一个替换的函数 形参是传入的文件tpl_name 和data数据
    def mkTpl(self,tpl_name,data):
        # 调用上面的读取文件
        tpl=self.loadTpl(tpl_name)
        # 遍历传入进来的数据的索引
        for i in range(0,len(data)):
            # 这个是tmp的结果"{{0}}"
            tmp="{{"+str(i)+"}}"
            # 之后替换字符串  replace  前面是旧的 后面是新的
            tpl=tpl.replace(tmp,data[i])
        # 替换完之后给tpl返回过去
        return tpl




    # 把内容给加到http协议里
    def mkrsp(self,msg):
        # 响应报文
        # 告诉浏览器成功
        self.rsp="HTTP/1.1 200 OK"
        # 加上这个是http协议的格式
        self.rsp+="\r\n"
        self.rsp+="Date: 20171211"
        self.rsp+="\r\n"
        # 告诉浏览器建一个cookie  文件 保存我的信息
        self.rsp+="Set-Cookie: ws by liuying"
        self.rsp+="\r\n"
        # 告诉浏览器我的文件格式
        self.rsp+="Content-Type: text/html"
        # 回车加换行
        self.rsp+="\r\n"
        # 内容长度告诉浏览器
        self.rsp+="Content-length: "+str(len(msg.encode("utf-8")))
        self.rsp+="\r\n"
        self.rsp+="\r\n"
        # 内容主体
        self.rsp+=msg
        return self.rsp
    # 给浏览器发送信息
    def sendRsp(self):
        self.skt.send(self.rsp.encode("utf-8"))


if __name__=="__main__":
    # 实例化对象 把这个服务器的地址和端口给参数传入进去
    ws=Webserver((ServerContent.address,ServerContent.port))
    ws.start()
```


# 1.2服务器功能

- 解析http请求-解析
- http包装反馈内容并返回-返回
- 按照访问url调用相应处理函数-路由
- 模板的操作处理-模板系统
- 数据-数据库db，模型
- 把需要返回的信息组装成一个可以直接返回的字符串-视图view
- 控制流程




# 1.3  解释下http协议

```
HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。

HTTP协议的主要特点可概括如下：

1.支持客户/服务器模式。

2.简单快速：客户向服务器请求服务时，只需传送请求方法和路径。请求方法常用的有GET、HEAD、POST。每种方法规定了客户与服务器联系的类型不同。由于HTTP协议简单，使得HTTP服务器的程序规模小，因而通信速度很快。

3.灵活：HTTP允许传输任意类型的数据对象。正在传输的类型由Content-Type加以标记。

4.无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。

5.无状态：HTTP协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。


```



# 1.4 解释下Http请求头和常见相应状态码

```
Accept:指浏览器或其他客户可以接爱的MIME文件格式。可以根据它判断并返回适当的文件格式。

Accept-Charset：指出浏览器可以接受的字符编码。英文浏览器的默认值是ISO-8859-1.

Accept-Language：指出浏览器可以接受的语言种类，如en或en-us，指英语。

Accept-Encoding：指出浏览器可以接受的编码方式。编码方式不同于文件格式，它是为了压缩文件并加速文件传递速度。浏览器在接收到Web响应之后先解码，然后再检查文件格式。

Cache-Control：设置关于请求被代理服务器存储的相关选项。一般用不到。

Connection：用来告诉服务器是否可以维持固定的HTTP连接。HTTP/1.1使用Keep-Alive为默认值，这样，当浏览器需要多个文件时(比如一个HTML文件和相关的图形文件)，不需要每次都建立连接。

Content-Type：用来表名request的内容类型。可以用HttpServletRequest的getContentType()方法取得。

Cookie：浏览器用这个属性向服务器发送Cookie。Cookie是在浏览器中寄存的小型数据体，它可以记载和服务器相关的用户信息，也可以用来实现会话功能。

 

状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值：

1xx：指示信息--表示请求已接收，继续处理

2xx：成功--表示请求已被成功接收、理解、接受

3xx：重定向--要完成请求必须进行更进一步的操作

4xx：客户端错误--请求有语法错误或请求无法实现

5xx：服务器端错误--服务器未能实现合法的请求

常见状态代码、状态描述、说明：

200 OK     //客户端请求成功

400 Bad Request  //客户端请求有语法错误，不能被服务器所理解

401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用

403 Forbidden  //服务器收到请求，但是拒绝提供服务

404 Not Found  //请求资源不存在，eg：输入了错误的URL

500 Internal Server Error //服务器发生不可预期的错误

503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

eg：HTTP/1.1 200 OK （CRLF）

```



# **---------------------------------**

# Django

## 1. 配置环境

1. bash Anaconda-5.0.1-Linux-x86-64.sh 一路回车 yes

2. conda create -n 虚拟环境名 python=3.6

3. 安装第三方包在虚拟环境中,如装django

   conda install -n 虚拟环境名 django

4. 虚拟环境加入环境变量(不管用时在执行此语句)

   conda search "python$"

5. 创建djanjo项目工程

   django-admin startproject 项目名字 (建议到一个确定的文件夹去建)

6. 进入虚拟环境 source activate 项目名称

7. 退出虚拟环境  source deactivate

8. 删除虚拟环境  conda remove -n 项目名字 -call


## 2. 创建Django项目

**django-admin  startproject  项目名t05**

**manage.py:  建完django 项目 之后在manage.py 点击Edict 将这个 Script partmeters 给改成 runserver**



### 2.1 总路由

//导入url  要是有子路由的时候需要导入include

**from django.conf.urls import url,include**

**同时, 需要在底下的url 写上**

```
#第一个是子路由都带的路径地址,第二个是绑定导入进来的子路由url名字
url(r'^showeast/',include(r)),
```

//必须导入

**from django.contrib import admin**

//从app名是w01 中导入子路由 urls  命名为r

**from w01 import urls as r**



## 3. 创建app应用  

**先输入 python manage.py startapp  app名字 **



### 1. app-views视图

**1. 这里写的是干活函数,逻辑上函数,给页面返回信息**

**2. 需要导入: from django.shortcuts import render**

​		//导入http包装的模块

​		   **from django.http import HttpResponse**



### 2. app-urls子路由

//导入 url 函数

**from django conf.urls import url**

//导入视图 

**from . import views as v**

//子路由里面没有admin



```
urlpatterns = [
     #地址  第二个是调用的视图函数
    url(r'^admin/', admin.site.urls),
    # 这填写的是网页地址 客户访问的   调用我的视图处理函数
    # 当访问这个网址时候，来用视图里的这个函数进行处理
    url(r'^normalmap/',v.normalmap),
```



### 3. 带参数正则匹配的路由,和对应处理的视图



### 3.0 URLS

```
- 项目 vs 应用
  - 项目：一个完整的工程
  - 应用： 一个项目中包含的独立的事物模块
- url匹配规则
  - 从上往下一个一个比对
  - url格式是分级格式，则按照级别一级一级往下比对,主要对应url包含子url的情况
  - 子url一旦被调用，则不会返回到主url
    - /one/two/three/
  - 正则以r开头，注意尖号(^)和美元符号($)
    - /one/two/three 配对 r'^one/
    - /oo/one/two/three 不配对 r'^one/"
    - /one/two/three/ 配对 r'three/$'
    - /oo/one/two/three/oo/ 不配对 r'three/$"
    - 开头不需要有反斜杠
- 正常路由
- 带参数路由
  - 函数withparam
  - 带一半参数
- 子路由
  - 把总的路由细分成几个独立的子路由，在相应app下建立自己的路由文件    

作业

```

#### 3.1 例子1

**urls**

```
  	# 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以?加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号表示出现的次数，此处4表示只能出现四个0-9的数字
  
  url(r'^age/(?P<year>[0-9]{4})/', v.with_param),
```

**views**

```
def with_param(request,year):
    print("HELLO withparameter")
    return  HttpResponse("Hello withparameter{0}".format(year))
```



#### 3.2 例子2

**urls**

```
 //?:代表忽略这page-,?P定义变量  \d代表数字 +代表贪婪
 url(r'^list/(?:page-?P<page_num>\d+)/', v.half_param),
```



**views**

```
def half_param(request, page_num):
    print(page_num)

    return HttpResponse("Hello half_param {0}".format(page_num))
```



#### 3.3 例子3

**urls**

```
 # 定向追踪  我一看你访问的是age 或者是name  那么我就知道你是哪来的了,这个在后面传
 # 就好比我是从微信跳转来的 我是支付宝跳转来的 都是访问不同的路径 最后达成一个页面 只不过输出结果不一样
 url(r'list/name/',v.in_param,{'source':"xdl"}),
 url(r'list/age/',v.in_param,{'source':"other"}),
```



**views**

```

def in_param(request,source):
    print(source)
    return HttpResponse("Hello you from {0}".format(source))
```



#### 3.4 例子4

**urls**

```
 //这个是逆向解析 
 url(r'rkkk/url/', v.r_url, name="revURL"),
```



**views**在使用这个的时候需要导入reverse

**from django.shortcuts import render,reverse **

```
#当我访问v5_2的时候 跳转到v6 因为导入了 from django.http import HttpResponse,Redirect  

url(r'^v5_2/', v.v5_2),
def v5_2(request):
    # 参数使用反向解析  这个v6是下面的name="v6"
    return redirect( reverse("v6") )

url(r'^v6/', v.v6, name="v6"),
def v6(request):
    return HttpResponse("哈哈，这是v6的返回呀")
```


## 4. 反馈

本节专注于返回结果，学习视图模块如何返回正确的结果

HttpResponseBase

所有反馈结果都应该是HttpResponseBase的子类

Response负责封装返回结果并自动进行返回



**正常views 需要导入  from django.shortcuts import render**

​				 **from django.http import HttpResponse**



### 4.1 正常反馈

**urls.py**

url( r'^v1/',v.v1)

**views.py**

def v1(request):

​	return HttpResponse("ok")



### 

### 4.2  返回html页面

**urls.py**

url(r'^v2/',v.v2)

**views.py**

```
def v2(request):
    rst = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1 style="color: red;"> hello world </h1>

        </body>
        </html>
    '''
    return HttpResponse(rst)
```



### 4.3 set_cookie

​	**cookie:键值对的字典**

​	**delete_cookie(键)**

cookie是否每次都要设置？

 	-原则上设置一次就好
​	-但是需要定期更新

  	-最长失效和有效期不能同时用

**ex:**

**urls.py**

url(r'^v3/',v.v3)

**views.py**

**//设置cookie**

def  v3(request):

​	rsp=HttpResponse("COOKIE OK")

​	rsp.set_cookie("one",one)

​	rsp.set_cookie("two",two)

​	rsp.set_cookie("three",three)

​	return rsp

**//给用户返回cookie**

def t03_cookie(request):

​	d=request.COOKIES

​	rsp="""

​		你好,您设置的cookie是:<br>

​		one:%(one)s<br>

​		two:%(two)s<br>

​		three:%(three)s<br>

​		//第一个'one'是你想给顾客看什么  他只是个字符   第二个one是底下的站位键

​		//后面的d['one']是值

​		

​		"""%{'one':d['one'],'two':d['two'],'three':d['three']}

​	return HttpResponse(rsp)



**展示cookie**

**urls.py**

url(r'^show_cooke/',v.show_cookie)

**views.py**

def show_cookie(request):

​	print(type(request.COOKIES))

​	

​	pront(request.COOKIES)



​	

### 4.4  Http404

- 出现错误的时候给用户一个合理反馈
- 当出现错误，处于安全考虑不能给用户一个详细的问题原因，需要用一定格式通知用户
- 操作步骤：
    1. settings里DEBUG=False， 即关掉调试模式
    2. settings里ALLOWED_HOSTS = ["*"], 即允许所有访问
    3. 修改urls
    4. 在views中添加函数并手动引发异常 raise Http404

**ex**:

**urls.py**

url(r'v4/',v.v4)

**views.py**

def v4(request):

raise Http404



### 4.5 HttpResponseRedirect重定向

- 由于业务需要，需要把对方的访问重新定向到下一个资源，属于自动跳转
- 推荐使用反向解析
- 跳转后应该是跳转到路由总入口，相当于从新访问一次



**需要在views.py导入重定向的模块  **

**from django.http import HttpResponseRedirect**



**urls.py**

url(r'^v5_1/',v.v51)

url(r'^v5_2/',v.v52)

url(r^v6/',v.v6,name="v6")

**views.py**

```
def v51(request):

//HttpResponseRedirect需要一个url作为参数，意思是告诉返回跳转到哪里

//硬编码，不太好的编程风格

	return HttpResponseRedirect("/v6")
```



```
//需要先导入reverse
def v52(request):
    # 参数使用反向解析  这个v6跳转到name="v6", 之后带有参数的url再次调用视图 进入v.v6函数   给他返回return的值
    return HttpResponseRedirect( reverse("v6") )
```

```
def v6(request):
    return HttpResponse("哈哈，这是v6的返回呀")
```



### 4.6   request    HttpRequest的实例

- Request介绍
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象Request
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API


- 封装所有访问信息
- 视图的第一个函数应该是它


- 里面信息基本都是只读
- 视图第一个参数应该是HttpRequest的实例
- 属性
    - path: 请求资源路径 一个字符串，表示请求的页面的完整路径，不包含域名
    - method：请求方法 一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
    - encoding： 编码
        - 默认或者没有，一般认为 "utf-8"
        - 这个属性可写 可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
    - GET： get方法所有//携带数据//传入数据 一个类似于字典的对象，包含get请求方式的所有参数
    - POST： post方法所有//携带数据//传入数据  一个类似于字典的对象，包含post请求方式的所有参数
    - FILES：文件，如果对方给我们传入的是文件，则在这个结构中
    - COOKIES： 对方带入的cookie 一个标准的Python字典，包含所有的cookie，键和值都为字符串
    - session： 记录回话凭证，数据等 一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 


- 方法：
    - is_ajax: 判断对方的请求是否为ajax请求

**urls**

//request 对象内容解析

url(r'v7/',v.v7)

**views.py**

def v7(request):

rsp="传入信息如下: \n path::{0} \n encoding:{1} \n method:{2} \n"

rsp=rsp.format(request.path,request.encoding,request.method)

//返回的是看用户发送的什么请求  打印出request给我们传入的数据

return HttpResponse(rsp)



### 4.8GET 

- QueryDict 对象
    - 使用类似于 dict 对象
    - 跟 dict 区别是可以有重复键
    - 典型的GET,POST 是QueryDict类型
    - get方法，可以返回相应的键的值，可以设置缺省值
    - getlist方法： 返回指定键的重复值


- GET: 封装访问访问为GET的时候的参数
    - QueryDict类型的对象
    - 参数以？开头，形式为name=value, 多个参数用&隔开
    - name值可以重复
    - GET.get(k) 值永远取重复键的最后一个值
    - 如果向得到所有重复值，需要使用getlist



//访问的时候url后面跟参数 ?开头 one=1 & two=2

**urls.py**

url(r'^v8/',v.v8)

**views.py**

def   v8 (request):

​	rst="传入的GET的值是:"

​	**//传入的参数长度 一键值对的长度算1** 

​	print(len(request.GET))

​	**//获取传入参数one的值**

​	print(reques.GET["one"])

​	**//传入多个参数键相同,值永远取重复键的最后一个值**

​	**//相当于字典键one :值[1,12,13]**

​	for i  in request.GET["one"]

​		print(i)

​	**//在GET请求中 对其键进行取对应的键和值 没有默认给他hahaha**

​	request.GET.get("one","hahaha")

​	**//把所有参数给遍历出来,之后给返回到页面**

​	for  k, v in request.GET.items():

​		rst+=k

​		rst+="-->"

​		rst+=v

​		rst+=":"

​	return  HttpResponse(rst)



### 4.9POST

- POST属性
    - QueryDict类型
    - 用post过来的所有数据
    - 一般跟form一起使用
    - 在form中可以设置提交方式，可以设置提交地址，空间有name和value属性
    - checkbox会出现多个值
    - name值是开发人员定的
    - 案例v9_get, v9_post

**ex:**

```

// urls.py里的路由 这个url进入form表单
url(r'abc/',v.abc)
//视图里的函数
def  abc(request):
//需要先倒入 from django.shortcuts import render_to_response
	//这里需要注意在外面建立一个模板文件夹,里面专门放html文件
	//并且在settings里面进行设置 ,并关掉 关掉csrf在setting中
	'DIRS': [os.path.join(BASE_DIR, "templates")],
	
	return render_to_response('1.html')
	
//之后出现表单界面
<form method="post" action="/postqingqiu/">
	<input type="text",name="name">	
	<input type="text",name="age">
	<input type="password",name="pwd">
	<input type="submit" value="提交">

<form/>
//填写完信息 之后form表单被提交到了这个路由
//之后这个路有调用这个视图来处理这个form表单所带入的信息并且给他返回一个页面
url(r'postqingqiu/',v.post)
```




## 5. 手动编写试图

- 大致顺序
  - 加载/读入模板/页面
  - 装载环境变量
  - 渲染-render
  - return response
- 案例render的案例 v10
  - 需要一个模板，模板需要设置settings
  - 编写模板
  - 添加url，关于v10
  - 处理视图 v10
  - 用render函数**

### 5.1  render的案例

**首先需要导入  from django.shortcuts import render,reverse,render_to_response**

**把模板里的界面给返回,通过访问路由地址,之后调用视图函数,在视图函数里面使用rander 来返回界面**

**urls.py**

url(r'^v10/',v.v10)

**views.py**

//返回静态页面

def v10(rq):

​	//参数:

​	//request:传入的HttpRequest的实例

​	//template_name: 模板或者页面名称

​	//context:特指除传入的request之外的,我们自己定义的数据

​	**//注意的是这里需要有rq request的参数**

​	return render( rq, "v10_t.html" , context=None)

​	

### 5.2 render 的案例二

**urls.py**

url(r'^v11/',v.v11)

**views.py**	

//返回带数据的页面

def v11(rq):

​	c=dict()

//当访问路由 ,调用视图里的v11 之后这个函数把字典c里的键name的值liuying赋给 传到页面  并且把字典给传入进去

​	c["name"]="liuying"

​	return rander(rq,"v11_t.html",context=c)

​	

**模板里的v11_t.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1> 我是被{{name}}创建的</h1>
</body>
</html>
```



### 5.3  loder 手动装载 load template 案例 

**导入loader : from django.template import  loader,RequestContext**

**urls.py**

url(r'^v12/',v.v12)

**views.py**

def v12(r)

​	//利用loader装载一个模板,手动装载

​	t=loader.get_template('v11_t.html')

​	//创建一个dict类型的环境

​	c=dict()

​	c["name"]="liuying"

​	//利用创建的环境变量内容进行渲染模板

​	tt=t.render(c)

​	return  HttpResponse(tt)

**模板里的v11_t.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1> 我是被{{name}}创建的</h1>
</body>
</html>
```





### 5.4  render_to_response   tmplate 的案例

**导入: fromdjango.shortcuts import render_to_response**

**urls.py**

url('r^v12,v.v12/')

**views.py**

def v12(r):

​	//创建一个dict类型的环境

​	c=dict()

​	c["name"]="liuying"

​	**//这里render_to_response第一个参数不给他request ,他和render  就这里有不同**

​	return render_to_response("v12.html",c,status=400)

**v12.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1> 我是被{{name}}创建的</h1>
</body>
</html>
```





## 6.系统内建视图

- 需要注意错误处理流程
- 远吗可以在 django.views.defaults中查看
- 常用视图，系统内建
- 404
  - defaults.page_not_found
- 400
  - defaults.bad_request
- 其余在源码包中可以看到



### 6.1手动引发异常

**urls.py**

url(r'^v_404/',v.v404)

**views.py**

//模拟404

def v404(request):

​	try:

​		print("这是成功的输出")

​		print("出错的代码标记")

​		//手动引发异常,实际代码不需这么做

​		//抛出个异常 , 里面需要写个异常实例的对象里面需要传入参数 ,这里给了个字符串

​		raise Exception("E by LY")

​	except Exception as  e:

​		print("逮住错误了,先返回一个东西吧,别让用户久等了")

​		#返回错误

​		return  defaults.page_not_found(request,e,template_name="v404.html")

**v404.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1 style="color:red"> 粗错了，粗大错了！！！！！！！！！！</h1>
</body>
</html>
```



## 7. 模板系统 

- 提供页面的动态支持，包括生成和静态页面
- 便于表达，跟前端分离
- 业务逻辑(views)跟显示内容分离(template)
- 模板包含：
  - 静态html代码
  - 动态数据
- django模板语言，检查DTL(DjangoTemplateLang), 在django.template中定义
- 工程设置：
  - settings中有关于模板目录的设置

  - 一般在主目录下建立templates文件夹，下面每个app有一个独立的文件夹，
    放入跟此app相关的所有模板文件

  - 静态文件单独存放，包含 js,css, 图片

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [

    ```
    //需要单独建立JS等文件夹  之后HTML页面jquery路径要指明位置
    os.path.join(BASE_DIR,'static'),
    ```

    ]
- 模板语言包括
  - 变量
  - 标签
  - 过滤器
  - 注释

### 7.1变量

- 表示方法

  ```
  {{name}}
  ```

- 使用的时候，系统自动把变量表示替换成对应环境上下文的dict里边的值



### 7.2标签

- 表示方法

  ```
  {% 标签 %}
  ```

- 作用

  - 控制流程
  - 加载外部信息等



#### 7.2.1 案例v1for

​	//循环逻辑

​	{% for i in .... %}
​	

​	//假如传入的变量为空，则执行这一段代码 

​	{% empty %}

​	//结束循环

​	{% endfor %}

**案例**

**urls.py**

 url(r'^v1_for/', v.v1for),

**views.py**

def v1for(request):

​	c=dict()

​	c["score"]=[1,2,3,4,5]

​	//给渲染个html页面 并且给过参数

​	return render_to_response("v1for.html",content=c)

**v1forhtml**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
////aaa =    {"a":1,"b":2,"c":3}      那边显示的a=1b=2c=3

//c["score"] = [1,2,3,4,5]  我到html遍历for i  in   score   结果输出的是1,2,3,4,5 语法和python 不是很一样 django 里面写好多 没有为什么

	{% for i in score %}
		{{i}}
	{% endfor %}
```



#### 7.2.2  forloop.counter  案例 v2for

- 系统提供{{forloop.counter}}表示当前循环次数
- 访问dict方法，v2for

**urls.py**

 url(r'^v2_for/', v.v2for),

**views.py**

def v2for(request):

​	c=dict()

​	c["score"]=[98,23,36,84,95]

​	c["score"]=None

​	c['hd']={"one":1,"two":2}

​	return render(request,"v2for.html",content=c)



**v2for.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


{%  for k,v in hd.items %}
	//输出结果"one"=1--"two"=2
    {{ k }} -- {{ v }}

{% endfor %}


{% for i in score %}
			  //forloop.counter  系统默认给排序 默认为1
    <h1 style="color: red"> {{ forloop.counter }}   -- {{ i }} </h1>
//如果为空则显示哈哈哈
    {%  empty %}
    hahhahahahah
{%  endfor %}

</body>
</html>
```





#### 7.2.3 案例3 显示传入来的 request的属性,path,method

**urls.py**

 url(r'^v3_for/', v.v3for),

**views.py**

def v3for(request):

​	c=dict()

​	c["name"]="liuyingli"

​	return  render(request,"v3for.html",context=c)

**v3for.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//request对象的属性 因为上面传入了request对象
{{request.path}}
{{request.method}}

{% for k,v in request %}
	{{k}}--{{v}}
{% endfor %}

</body>
</html>

```



#### 7.24  if  和 注释

​	{% if xxxxx %}
​	逻辑
​	{% elif yyyy %}
​	逻辑
​	{% endif %}

---comment注释

​	{% comment %}
​	多行注释
​	{% endcomment %}



**urls.py**

url(r'^v4_if/', v.v4if),

**views.py**

def v4if(r):

​	c=dict()

​	c["name"]="liuying"

​	return  render(r,"v4if.html",content=c)

**v4if.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% comment %}
第一行注释
第二行注释
这不是跳出
真的是注释
{% endcomment %}

//如果后台给个liuying 过去 则显示liuying
{% if name=="liuying" %}
	<h1> liuying</h1>
{% else %}
	<h1> not liuying</h1>
{% endif %}

</body>
</html>
```



## 8. crsf 问题

- crsf问题： 跨站点请求伪造

- 演示跨站请求问题
  - 建立两个页面 csrf1.html 和  csrf2.html
    - csrf1.html 中包含一个表单，表单提交到csrf2的地址
    - csrf2.html中需要从request.POST中提取值填写模板
  - 构造url v5_csrf1,  v5_csrf2
  - 改造views
  - 修改settings
  - 在render中要求传入HttpRequest的实例作为csrf_token数据的来源

- 保护原理
  - 在表单中加入隐藏内容 
  - 在cookie中加入加密内容
  - 两边内容传入服务器后，服务器跟保存token进行比对
  - 如果有问题则拒绝访问

- 取消保护
  - nsettings中注释掉对应中间件

  ```
    - 由于安全原因，需要在设置中安全选项中删除csrf设置
          ```python
            # settings.py
            

              MIDDLEWARE = [
                  'django.middleware.security.SecurityMiddleware',
                  'django.contrib.sessions.middleware.SessionMiddleware',
                  'django.middleware.common.CommonMiddleware',
                    #  下面这句话被注释掉
                  #'django.middleware.csrf.CsrfViewMiddleware',
                  'django.contrib.auth.middleware.AuthenticationMiddleware',
                  'django.contrib.messages.middleware.MessageMiddleware',
                  'django.middleware.clickjacking.XFrameOptionsMiddleware',
              ]
  ```
  ```

  ```

### 8.1 案例 关于form表单提交 恶意大量请求  对服务器请求安全问题

**urls.py**

**//先进入这个路由**

url(r'^v5_csrf1/',v.v5csrf1)

**views.py**

def v5csrf1(r):

​	//如果模板里使用 csrf_token, 要求上下文环境传入HttpRequest实例

​	//return render(r,"csrf1.html",context={})

​			**//返回csrf1.html表单**

​	return render_to_response(r,"csrf1.html",context={})



**csrf1.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//先写个路由调用函数进入form表单,之后在写个路由 这个路由是form表单提交的地址,
//之后这个调用函数给返回另一个页面 , 并且这个返回的页面是隐藏的参数 {%csrf_token%} 如果不加上这个就要注释掉django 如果加这个则不用注释  
并且这里继续往下写的话 把这个地址 在写一个路由  调用 函数 并且给他个返回页面 并且这个页面有{{name}
<form method="POST"  action="/csrf2/">

//这个要写在里面
{%csrf_token%}
    <input name = "name">  <br>
    <input type="submit" value ="提jiao"/>

</form>

</body>
</html>
```

****

**urls.py**

/**表单提交到这个路由**

​    url(r'^csrf2/', v.v5csrf2),



**views.py**

def v5csrf2(r):

​	c["name"]=r.POST["name"]

​	return render_to_response("csrf2.html",context=c)

**csrf2.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{ name }}
</body>
</html>
```



## 9. 模板的继承

- 模板继承可以减少页面内容的重复定义， 实现页面的重用

- 典型应用： 网站的头尾，法律定义，版权定义都在父模板中，其余独立的不同的定义在子模板中

- block标签: 在父模板中预留一些位置/区域，在子模板中进行填充

- extends标签： 继承标签，写在模板文件的第一行

- 定义父模板的一个例子 base.html

  ```
  {% block block_1 %}
  ```

  ```
  {% endblock %}
  ```

- 定义子模板 index.html

  ```
  {% extends "base.html" %}
  写自定义的子模板中的内容
  ```

- 在子模板中使用block填充

  {% block block_1 %}
  子模板中的实际填充内容
  {% endbloc %}   

- 继承案例 v6_inh   



### 9.1 继承案例 //前提都在模板里

//先写一个路由 ,是直接访问的子路由

**urls.py**

   url(r'^v6_inh/', v.v6inh),

**views.py**

def v6inh(r):

​	return  render_to_response("v6_son.html")

//之后建立两个HTML  一个是父类html  一个是子类html 

**//父类html代码如下  文件名:father.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
    //如果写内容的话不能写到这两行代码里面去
   	 	{% block block_title%}
    	{% endblock %}
      </title>
</head>
<body>
		{% block  block_body %}
		{% endblock %}
		
</body>
</html>
    
```



**//子类html代码如下** 

```
//继承父类的名字 
{% extends "father.html" %}

{% block block_title %}
这是子模板的头呀
{% endblock %}

{% block block_body %}
这是子模板的内容啊
{% endblock %}
```



## 10 过滤器

- 每一个操作的输出作为下一个操作的输入或者操作主体，连续执行

- 使用管道符号来应用过滤器(|)

- 通过使用过滤器来改变变量的计算结果

- 可以在if语句中使用过滤器组合运算符   

  ```
  name | upper|lower
  ```

- 过滤器可以传入参数

  ```
  list|join:"..."
  ```

- default:如果前面变量没有提供值，则我们需要提供一个默认值

  ```
  value|default:"nothing"
  ```

- date:根据制定格式对date变量格式化

  ```
  value|date:"Y-m-d"
  ```

### 10.1 案例操作

**urls.py**

url(r'^v7/', v.v7),

**views.py**

def v7 (r):

​	c=dict()

​	c["name"]="liuying"

​	c["riqi"]="20171215"

​	c["v"]=None

​	return  render(r,"v7.html",context=c)

**v7.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//传入过来HTML给变成了大写
{{ name|upper }}

//传入过来HTML 给过滤成小写
{{ name|lower }}

//传入过来以此过滤最后结果是小写
{{ name|upper|lower }}

//这个不好使, 老师没想出来,后续补充
{{ riqi|date:"Y-m-d" }}

//传入过来过滤成没有传入值
{{ v|default:"没有传入值" }}

</body>
</html>
```



## 11. ORM

-ObjectRelationMap:把面向对象思想转换成关系数据库思想，操作上把类对应相应的表格

-解放程序员，程序员只面向对象编程就好

### 11.1 操作步骤

1. 在app下的models.py 中定义class
    - 所有需要使用ORM的class必须是models.Model的子类

    - class中说有的属性的类型，都应该是 models.XXXXX，不能使用python自己的数据类型

    - 数据库迁移：即生成相应的ORM代码，跟数据库相匹配

    - 准备迁移 //转换成sql语句  准备迁移

    - 需要进入虚拟环境下

            python manage.py makemigrations 

    - 迁移 //注入  也就是迁移

            python manage.py migrate(app名)
        ​    

```
class Student(models.Model):
									#verbose_name字段名
    name=models.CharField(max_length=20,verbose_name="nick_name")
    age=models.IntegerField(verbose_name="nianling",default=18)

    mobile=models.CharField(max_length=12,unique=True,verbose_name="dianhua")
    address=models.CharField(max_length=50,verbose_name="dizhi")
    # 可以为空 True
    qq=models.CharField(max_length=13,verbose_name="msn",null=True)
```



### 11.2 字段常用参数

- max_length: 规定数值的最大长度

- blank： 是否允许字段为空，默认是False(后台添加的时候可不可以为空)

  如果为True，则该字段允许为空白，默认值是 False

  - null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
  - blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如 admin 界面下增加 model 一条记录的时候
  - django model字段中null与blank的区别。如果为True，Django将在数据库中存储一个空值NULL。默认为 False。如果为True，则允许该字段为空白。默认为False。注意，该项与null是不同的，null纯粹是与数据库相关的。而blank则与验证相关。如果一个字段设置为blank=True，表单验证时允许输入一个空值。而blank=False，则该项必需输入数据。

- null： 在DB中控制是否保存为NULL，默认是False (数据库里面字段可不可以为空)

  如果为True，Django 将空值以NULL 存储到数据库中，默认值是 False

- default： 默认值

- unique：唯一 如果为 True, 这个字段在表中必须有唯一值  唯一索引：索引列的值必须是唯一的，但允许有空；

  （主键索引。索引列唯一且不能为空；一张表只能有一个主键索引）

- vebose_name: 字段名

- primary_key 若为 True, 则该字段会成为模型的主键字段



### 11.3 对数据库的使用

1. 迁移成功之后启动shell 来对建好的表进行操作

   **python manage.py shell**

       - 启动：　python manage.py shell
       - 一般情况，对ｏｒｍ的操作分为静态函数和非静态函数
       									//Student.objects.all()
           －　静态：在内存中，只有一份内容存在，调用的时候使用类名.静态函数
       -　使用objects属性操作数据库
       -　all:　查询数据库表中所有内容，返回是QuerySet类型
       //Student.objects.filter(name="李燕")
       - filter: 按条件查找
       #查询对象里的所有信息  字典形式返回
       Student.objects.filter（条件）.values.all()
   ​

2. 把类给导入库成为表

   **from jskapp.models import Student**



3. 查看表

   **s=Student.object.all()**

   //结果<QuerySet [<Student: Student object>]>

   **s**

   //出现表里的数据

   **Student.object.all()**

   ​

4. 往表里添加数据

   **s=Student()**

   **s.name="zhangsan"**

   **s.age=34**

   **s.address="北京通州"**

   **s.mobile="987654"**

   **s.qq=295616882**

   **s.save()**



### 11.4 Meta 属性

- 定义表格的元数据，任何不是字段的内容
- 用class Meta来定义
- 常用字段：
    - db_table: 数据库的表名，一般小些，默认就是 AppName_ModelName
    - ordering: 中文问题，可能出现无效的情况


```
 class StudentInfo(models.Model):
            ...
            class Meta():
                ordering = ['name','-age'] 
                //来定义不是字段的内容 一般是表名
                db_table = "studentinfo"


        class Ox(models.Model):
            horn_length = models.IntegerField()

            class Meta:
            	//按照字段来进行排序
                ordering = ["horn_length"]
                verbose_name_plural = "oxen"
```



### 11.5  自定义修改  加了一个str  打印出来的对象换了一个方式  让按照姓名来显示出

def __str__

return  self.name  之后下面就打印出来的对象换了个显示的方式  而不是显示Student object

	__str__
	时机: 使用print(对象)或者str(对象)的时候触发
	返回值: 必须是字符串类型
	作用: print(对象)进行操作,得到字符串

//表

class Student(models.Model):
name=models.CharField(max_length=20,verbose_name="nick_name")
age=models.IntegerField(verbose_name="nianling",default=18)

mobile=models.CharField(max_length=12,unique=True,verbose_name="dianhua")
address=models.CharField(max_length=50,verbose_name="dizhi")

//可以为空 True

qq=models.CharField(max_length=13,verbose_name="msn",null=True)



//通过my_student来查  而不是通过object来

my_student=StudentManager()



//一输入Studen.object.all() 结果自定义返回姓名

<QuerySet [<Student: zhangsan>, <Student: lisi>, <Student: 李燕>, <Student: 玛丽奥>, <Student: 刘纯>]>

def __str__(self):

​	return  self.name



### 11.6 模型的Manager属性(管理器)

```

- 最重要的属性是Manager,是数据库查询操作的接口,用于从数据库获取示例,Manager比较特殊
- 如果没有自定义Manager,则默认名称是objects
- 只能通过模型类访问,不能通过模型实例访问
- 可以自行定义，否则使用默认的objects 
- 修改常见于两种情况
    1. 向管理器类添加额外的方法
    2. 修改管理器返回的原始查询集合，重写 get_queryset()方法
- 用来真正执行模型对数据的访问
```


### 11.7 关系

- 关系分类：
    - 1:1
    - 1:n
    - n:n


- 1:1(OneToOne)
  - 假定一个老师只能在一个教室上课，一个教室也只能有一个老师
  - 使用OneToOneField定义
  - 在单边定义，任何一边没影响
  - 添加 直接把定义好的实例（已经保存）赋值给相应字段
  - 查找利用相应字段直接查找


```
class Teacher(models.Model):
    name=models.CharField(max_length=20,verbose_name="nick_name")
  
    my_classroom=models.OneToOneField("Classroom",default=None,null=True)
```

- 1:n(OneToMany)
  - 假定一个学生只能在一个教室上课， 一个教室可以有很多学生
  - 使用ForeignKey来定义
  - 在多的一边定义
  - 添加，多利用 objectName.relationName.add(object_to_add)


- n:n(ManyToMany)
  - 假定一班学生需要由好几个老师教才能毕业
  - 使用ManyToManyField定义
  - 单边
  - 添加使用add
  - 添加，多利用 objectName.relationName.add(object_to_add)
  - 查找使用 teacher.my_student.all()





### 11.8 查询参数


      - exact: 隐含包括
      >>> Entry.objects.get(headline__exact="Man bites dog")
    - iexact: 大小写不敏感(不区分大小写)
    
       >>> Blog.objects.get(name__iexact="beatles blog")
    
    - contains: 大小写敏感的包含关系
    
      Entry.objects.get(headline__contains='Lennon')
      大体翻译成
      SELECT ... WHERE headline LIKE '%Lennon%';
    	- istartwith
        - iendwith
        - exact: 精确等于
        - iexact: 大小写不敏感
        - contains:包含
        - icontains：大小写不敏感
    
        - gt: 大于
        - get: 大于等于
        - lt: 小鱼
        - lte: 小于等于
        - range: 范围
        - year: 年份
        - isnull:

​        



### 11.9 查询   F&Q

- F查找
  - 用来在表中对不同字段进行比较
  - 使用方式
    - from django.db.models import F
    - Student.objects.filter(mobile__eq =  F("qq")  )
  - 可以对F表达式进行数学操作
- Q查找
  - filter函数中，默认对条件进行逻辑与操作
  - 对不同字段值进行操作后进行逻辑操作，包括与或（&，|）
  - from django.db.models import Q
  - 本质上是弥补条件查找的能力不足

### 11.10 模型的继承

1. 抽象继承， 父类没有实际对应表格，内容全部有子类继承

   - 实现方式：

     ```
     class Person(models.Model):
         name = models.CharField(xxxxx)
         class Meta():
             abstract = True

      class Student(Person):
         ....
     ```

   - 则以上代码，数据库表中不会有Person先关的表格，person的内容例如name等
     都在Student表中体现      

2. 多表继承

   - 每一model都对应自己的一张表，包括父类子类
   - 父类表跟子类表有一个onetoone关系
   - 如果在抽象继承中，删除abstract，则成为多表继承

3. 代理继承

   - 只是原来表格的一个代理，在数据库中真正指向的是父类表格
   - 如果说Student是Person的代理继承，则数据库中只有一个person相关的表，不会出现student相关的实际表格




## - 简单的django 增删改查操作步骤 -

1.进入虚拟环境  source activate  p05

2.创建django项目    django-admin startproject  xiangmu

3.创建app  python  manage.py startapp  app

4.进行setting设置   设置manage.py   给改成runserver 

5.对模板进行设置  在project下建立一个templates文件夹 存放模板

​    之后修改这个模板的路径  在setting里进行设置

```
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, "templates")],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]
```

6.settings - ALLOWD_HOSTS添加ip 给改成 ALLOWED_HOSTS = ['*']

7.之后写一个类的表   

Class  Person(models.Model):

​	name=models.CharField(max_length=20,null=False,verbose_name="XingMing")

​	age=models.IntegerField(default=16)

​	phone=models.CharField(max_length=15,null=True)

​	def __str__(self):

​		return  self.name+self.phone

6. 之后迁移数据库 , python  manage.py  makemigrations  		

   ​			   python   manage.py migrate

7. 之后进入终端  输入python manage.py  shell   (进行添加数据演示  查看是否成功)

    具体操作 :

    from  app.models import  Person


    ​	p=Person()

    ​	p.name="liyanliang"

    ​	p.age=18

    ​	p.phone="123456789"

    ​	p.save()

    ​	Person.objects.all()//查看是添加成功 

8. 路由操作   

  **fron  xiangmu  import   views as v  ,include  **

  **主路由:**  添加默认的访问为空就自动调用这个函数

  ​	 url('r^$',v,index)

  ​	//主路由指明包含子路由的关系   

  ​	//前面加上t10这部分不采取正则 例如 子路由为index  则可以访问/t10/index/

  ​	url(r'^t10/',include("t10.urls"))

 **from  .import  views   as v**

  **子路由:** 

​	什么也不输入自动出的页面   加上index   为了后面的重定向  

​	**url(r'^index/',v.index,name='index')**

​	

​	//当点击添加跳转到这个函数(因为index.html上的连接  继承了menu  里面的a连接)

​	<a href="{% url 'addusers' %}">添加用户</a>  这里的连接url是 addusers  之后通过这个路径来找到逆向解析name=addusers的这个函数 之后函数里面把添的页面给出去

​	**url(r'^add/', v.adduser, name="addusers"),**

​	

​	//添加操作  此时在add.html页面 add.html页面里面有一个form表单  通过post来提交  

​	这里的url提交地址  <form action="{% url 'insertusers' %}" method="post"> 是对应的逆向解析的路由name=insertusers

​	**url(r'insert/',v.insert,name="insertusers"**



9.  设置函数操作

**from  django.shortcuts  import  render,reverse**

**from django.http import  Httpresponse  ,HttpresponseRedirect**

**from  .models import  Person**



def   index  (request):

​	ps=Person.objects.all()

​	//这里html 页面写的内容 {% for stu in stulist %} 底下的stulist必须这么写  

​	c={"stulist":ps}

​	return render (request, "index.html路径 这里需要注意的是要从配置的模板路径位置的紧接着来开始写")



//把添加的页面给出去

def  adduser(r):

​	return  render(r,"add.html的路径")



def insert(r):

​	p=Person()

​	//往django 库里面存名字   //这里用到了get的方法是为了  如国用户没输入的话 那么我们给他一个默认值 获取来的首先是字符串  二期是个字典

​	p.name=r.POST.get("name","NoName")

​	p.age=r.POST.get("age","18")

​	p.phone=r.POST.get("phone","0000")

​	p.save()

​	//这里的是逆向解析 让页面在次跳转到原来执行这个代码的路由中 还出现这个页面

​	return  HttpResponseRedirect(reverse("index"))

​	





## Django里面连接mysql环境设置流程  

**先在虚拟环境命令行 下载pip管理工具pymysql  **

**进入虚拟环境:**source activate p05

**往pip python安装管理包里安装的命令:** pip install pymysql

1. **settings**

```
DATABASES = {
    'default': {
    	//自带的库
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':'django.db.backends.mysql',
        //这部要去库里把库先建好  建成mydb
        'NAME':'mydb',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    //把自带的app注释掉
    #'t10',
    //后加的mysql的app写法  
    't10.apps.T10Config'
]

```

**2. 主init 文件里面写上**

```
import  pymysql
pymysql.install_as_MySQLdb()
```

**3.之后进入虚拟环境迁移**

```
//准备迁移
python manage.py makemigrations
//迁移
python manage.py migrate

```

**4.表什么的都正常建好写好类迁移就ok,建表之前要导入models**

```
from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=20,null=False,verbose_name='XingMing')
    age=models.IntegerField(default=16)
    phone=models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.name+self.phone
```

**5 这个是迁移之后自动生成的apps.py文件 在app里  安装完之后查询一下**

```
from django.apps import AppConfig


class T10Config(AppConfig):
    name = 't10'

```



## 12  案例

### 12.1 关于session 

#### 12.1.1案例用户提交评论 

**urls**

//得到表单

url(r'^get_form/', v.getForm)

**views.py**

def getForm(r):

​	return  render(r, "showcomment.html")

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>填写评论</title>
</head>
<body>
<form action="/post_form/" method="post">
    {% csrf_token %}
    <textarea name="comm" id="comm" cols="50" rows="20">请输入评论内容
    </textarea>
    <br>
    <input type="submit" value="提交">
</form>

</body>
</html>
```



**提交的urls**

  url(r'^post_form/', v.postForm),

**views 函数**

```
def postForm(r):
    '''
    使用session前提是数据库进行迁移，以此来生成相应的数据表，session保存在数据库中
    每次检查session中标志位，看是否有记录，如果标志位被设置，说明已经有过提交记录
    需要注意的是，此处只记录是否提交过，不记录提交内容，所以会出现提交后即使更换提交内容也反馈已经提交

    :param r:
    :return:
    '''
    # 得到提交评论内容
    comm = r.POST.get("comm", "")
    # 得到session中提交记录，key自己定义，value此处为任意值，有值说明已经提交过，而不检查值内容
    # 如果有提交记录，则有has这个键，否则就是没有提交过，此时返回默认值None
    has_comm = r.session.get('has', default=None)
    # 有过提交记录，注意是提交记录
    if has_comm:
       return HttpResponse("您已经评论过了")
    # 如果是第一次提交
    else:
        # 实际应用应该是业务处理，此处用打印评论内容代替
        print(comm)
        # 第一次提交需要把标志提交记录的key设置一个值，此处只要有值就表示有过提交记录
        r.session['has'] = 1
        return HttpResponse("感谢评论，您可以去死了")
```



**html**

### 12.3 关于AJAX

- 使用视图通过上下文向模板中传递数据，需要先加载完成模板的静态页面，再执行模型代码，生成最张的html，返回给浏览器，这个过程将页面与数据集成到了一起，扩展性差
- 改进方案：通过ajax的方式获取数据，通过dom操作将数据呈现到界面上
- 推荐使用框架的ajax相关方法，不要使用XMLHttpRequest对象，因为操作麻烦且不容易查错
- jquery框架中提供了$.ajax、$.get、$.post方法，用于进行异步交互
- 由于csrf的约束，推荐使用$.get

#### 12.3.1 案例

**urls.py**

//访问这个路由 

​    url(r'^getAjax/', v.getAjax, name="getAjax"),

**views.py**

```
//路由调用这个函数 给了个html页面
def getAjax(r):
    return render(r, "district.html")
```

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Web的使用操作</title>
    <style>
        select{margin:10px;}
    </style>
    //这里注意需要配置static静态文件所在路径
    <script type="text/javascript" src="/static/jquery-1.8.3.min.js"></script>
    <script type="text/javascript">
        //jQuery入口程序
        $(function(){
            $.ajax({
            //ajax发送请求 这个是路由的 url逆向解析的路径
                url: "{% url 'district' 0 %}",
                type: 'get',
                data: {},
                dataType:'json',
                //接收传递过来的res传过来的是json格式
                success:function(res){
                	//res.data 把值取了出来 是个列表  列表里面有键和值
                    var data = res.data;
                    for(var i=0;i<data.length;i++){
                        $('<option
      //data[i]索引把每一个json字典给取出来 .id 是我的值              value="'+data[i].id+'">'+data[i].name+'</option>').appendTo('select:last')
                        //$('select:last').append('<option value="'+data[i].id+'">'+data[i].name+'</option>');

                    }
                },
                error:function(){
                    alert("ajax加载失败！");
                }
            });


            //获取最后一个下拉框并添加选中事件
            $("select").live('change',function(){
                //获取选中的id号
                var id = $(this).val();
                $(this).nextAll().remove();
                $.ajax({
                	//这里写死了访问前面的url
                    url: "/district/"+id,
                    type: 'get',
                    data: {},
                    dataType:'json',
                    success:function(res){
                        if(res.data.length<1)
                            return;
                        var data = res.data;
                        var select = $("<select></select>")
                        for(var i=0;i<data.length;i++){
                            $('<option value="'+data[i].id+'">'+data[i].name+'</option>').appendTo(select)
                            //$('select:last').append('<option value="'+data[i].id+'">'+data[i].name+'</option>');
                        }
                        $("select:last").after(select);
                    }
                });
            });

        });
    </script>
</head>
<body>
        <h1>Ajax的城市级联信息操作</h1>

        <br/>

        <select>
            <option>-请选择-</option>
        </select>

</body>
</html>
```



**urls.py**

//这个url是ajax请求的路径

 url(r'^district/([0-9]+)', v.getDistrict, name="district"),

//**views.py**

//需要导入 from django.http import HttpResponse,JsonResponse

```
//did请求时传递过来的参数  
def getDistrict(r, did):

    # 得到所有districe的内容
    dids = District.objects.all()
    list = []
    # 把得到的地区内容按一定格式封装如数据内
    //得到每个对象
    for ob in dids:
    		//这里的id是给起的名 到html那边需要遍历进行取出的
         list.append({"id":ob.myid, "name":ob.name})

    # 返回Json格式数据给请求端
    //html那边遍历data这个键  列表是值  每个字典里面是一个对象的属性
    //[{"id":ob.myid, "name":ob.name}{"id":ob.myid, "name":ob.name}]
    //返回一个json格式
    return JsonResponse({"data":list})
```



### 13.3 关于分页

- Django提供了一些类实现管理数据分页，这些类位于django/core/paginator.py中
##### 13.3.1Paginator 对象
- Paginator(列表,int)：返回分页对象，参数为列表数据，每面数据的条数
- 属性
    - count：对象总数
    - num_pages：页面总数
    - page_range：页码列表，从1开始，例如[1, 2, 3, 4]
- 方法
    - page(num)：下标以1开始，如果提供的页码不存在，抛出InvalidPage异常
- 异常exception
    - InvalidPage：当向page()传入一个无效的页码时抛出
    - PageNotAnInteger：当向page()传入一个不是整数的值时抛出
    - EmptyPage：当向page()提供一个有效值，但是那个页面上没有任何对象时抛出
##### 13.3.2 Page对象
- 创建对象
    - Paginator对象的page()方法返回Page对象，不需要手动构造
- 属性
    - object_list：当前页上所有对象的列表
    - number：当前页的序号，从1开始
    - paginator：当前page对象相关的Paginator对象
- 方法
    - has_next()：如果有下一页返回True
    - has_previous()：如果有上一页返回True
    - has_other_pages()：如果有上一页或下一页返回True
    - next_page_number()：返回下一页的页码，如果下一页不存在，抛出InvalidPage异常
    - previous_page_number()：返回上一页的页码，如果上一页不存在，抛出InvalidPage异常
    - len()：返回当前页面对象的个数
    - 迭代页面对象可以访问当前页面中的每个对象

```
>>> from django.core.paginator import Paginator
>>> objects = ['john', 'paul', 'george', 'ringo']
//分页的数据   每页几个
>>> p = Paginator(objects, 2)
//总共几个数据//所有页面的对象总数。
>>> p.count
4
//分几页
>>> p.num_pages
2
//分的页数列表显示 从1开始，例如[1, 2, 3, 4]。
>>> p.page_range
[1, 2]

>>> page1 = p.page(1)
>>> page1
//第一页俩数据
<Page 1 of 2>
//第一页的数据
>>> page1.object_list
['john', 'paul']

>>> page2 = p.page(2)
>>> page2.object_list
['george', 'ringo']
>>> page2.has_next()
False
>>> page2.has_previous()
True
>>> page2.has_other_pages()
True
```

##### 13.3.3 案例

**urls**

//请求的地址  携带参数pindex   可以是 

  url(r'^pag(?P<pIndex>[0-9]*)/', v.pagTest, name="pagTest"),

**views.py**

```
def pagTest(r, pIndex):

    '''
     使用分页器对内容进行自动分页
    :param r:
    :param pIndex:
    :return:
    '''
    # 得到所有内容
    list1 = Student.objects.all()

    # 对所有内容进行自动分页，每页3个内容
    p = Paginator(list1, 3)

    # 如果是第一次访问，则参数为空，此时自动默认是第一次
    if pIndex=="":
        pIndex = "1"

    pIndex = int(pIndex)

    # 有系统自动返回一个当前页
    list2 = p.page(pIndex)

    # 生成所有页码的列表, 注意是页码
    plist = p.page_range

    return  render(r, "pagTest.html", {'list':list2, 'plist':plist, 'pIndex':pindex })
```

**html**

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
<ul>
//得到每个对象  
{%for stu in list%}
//对象的名字和 对象的年龄
<li>{{stu.name}}--{{stu.age}}</li>
{%endfor%}
</ul>
//进行遍历传过来的页码列表
{%for pindex in plist%}
//如果传递过来的值等于我上面遍历的值
{%if pIndex == pindex%}
//那么就让他显示出来
{{pindex}}&nbsp;&nbsp;
{%else%}
//其他的让连接形式展现
<a href="/pag{{pindex}}/">{{pindex}}</a>&nbsp;&nbsp;
{%endif%}
{%endfor%}
</body>
</html>
```



## 13.中间件

```
## 概述
- 一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出
- 激活-：添加到Django配置文件中的MIDDLEWARE_CLASSES元组中
- 每个-中间件组件是一个独立的Python类，可以定义下面方法中的一个或多个
-   -  init ：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件
-   -  process_request(request)：执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
-   -  process_view(request, view_func, view_args,view_kwargs)：调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
-   -  process_template_response(request,response)：在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
-   -  process_response(request, response)：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
-   -  process_exception(request,response,exception)：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
- 使用-中间件，可以干扰整个处理过程，每次请求中都会执行中间件的这个方法
## 自定义异常
- 与settings.py同级目录下创建myexception.py文件，定义类MyException，实现process_exception方法

        from django.http import HttpResponse
        class MyException():
            def process_exception(request,response, exception):
                return HttpResponse(exception.message)

将类MyException注册到settings.py中间件中

MIDDLEWARE_CLASSES = (
    'test1.myexception.MyException',
    ...
)
```



## 14.  基于类的视图

- 参考资料
  - [官网中文](http://python.usyiyi.cn/translate/django_182/topics/class-based-views/index.html)
- 和基于函数的视图的优势和区别:
  - HTTP方法的methode可以有各自的方法,不需要使用条件分支来解决
  - 可以使用OOP技术(例如Mixin)
- 概述
  - 核心是允许使用不同的实例方法来相应不同的HTTP请求方法,而避开条件分支实现
  - as_view函数昨晚类的可调用入库,该方法创建一个实例并调用dispatch方法,按照请求方法对请求进行分发,如果该
    方法没有定义,则引发HttpResponseNotAllowed
- 类属性使用
  - 在类定义时直接覆盖
- CSDN讲解

```
ListView

在开发一个网站时，我们常常需要获取存储在数据库中的某个 Model 的列表，比如 Blog 要获取文章（Article）列表以显示到首页，通常我们都会写如下的视图函数来满足我们的需求：

def index(request):
    """
    获取 Article 列表以渲染首页模板
    """
    article_list = Article.objects.all() # 获取文章列表
    category_list = Category.objects.all() # 获取分类列表
    context = { 'article_list' : article_list , 'category_list' : category_list }
    return render_to_response('blog/index.html',context)
当然这仅仅是一个最为基本的视图函数的例子，Django 开发者发现，如果项目里有大量的视图都是实现类似于上面这种获取存储在数据库中的某个 Model 的列表的功能的话，会不断地重复书写诸如下面的代码：

article_list = Article.objects.all()
context = { 'article_list' : article_list }
return render_to_response('blog/index.html',context)
就是不断地获取 Model 列表然后渲染模板文件，Django 说写多了开发人员就觉得无聊了，那我们何不把这些逻辑抽象出来放到一个类里？于是 Django 帮我们写好了一个类，专门用于处理上面的情况，这就是 ListView，将上面的视图函数转写成类视图如下：

class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.all()
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
首先看看 get_queryset 方法，它完成的功能和 article_list = Article.objects.all() 这句代码类似，获取某个 Model 的列表（这里是文章列表），同时我们加入了自己的逻辑，即对 article_list 中的各个 article 进行了 markdwon 拓展，假如仅仅只需要获取 article_list ，则甚至可以不用复写 get_queryset 方法，只需指定一个 model 属性，告诉 Django 去获取哪个 model 的列表就可以了，像这样：

class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    model = Article

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
第二个复写的方法是 get_context_data 方法，这个方法是用来给传递到模板文件的上下文对象（context）添加额外的内容的（context 的概念在前面的教程中已有介绍，如果这里不懂的话我再简单解释一下，我们在模板文件中会使用 {{ }} 这样的标签来包裹模板变量，这些变量哪里来的？就是视图函数通过 context 传递到模板的）。我们这里因为首页需要显示分类信息，因此我们把 category_list 通过 get_context_data 方法加入了 context 对象，视图函数再帮我们把 context 传递给模板。return super(IndexView, self).get_context_data(**kwargs) 语句的作用是添加了 category_list 到上下文中，还要把默认的一些上下文变量也返回给视图函数，以便其后续处理。

现在有了 model 列表，context，按照视图函数的逻辑应该是把这些传递给模板了，ListView 通过指定 template_name 属性来指定需要渲染的模板，而 context_object_name 是给 get_queryset 方法返回的 model 列表重新命名的，因为默认返回的 model 列表其名字是 object_list，为了可读性，我们可以通过 context_object_name 来重新指定，例如我们这里指定为 article_list。

return render_to_response('blog/index.html',context) 的功能在 ListView 中 Django 已经默认帮我们做了，翻看其源代码就会知道：

... 省略其他代码
def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
... 省略其他代码
如果你改变渲染模板的一些行为，通过复写 render_to_response 方法即可。

以上方法在类视图调用 as_view() 方法后会被自动调用。

ListView 总结：

ListView 主要用在获取某个 model 列表中
通过 template_name 属性来指定需要渲染的模板，通过 context_object_name 属性来指定获取的 model 列表的名字，否则只能通过默认的 object_list 获取
复写 get_queryset 方法以增加获取 model 列表的其他逻辑
复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问
DetailView

前面的 ListView 用于获取某个 model 的列表，获取的是一系列对象，但获取单个 mdoel 对象也是很常见的，比如 Blog 里点击某篇文章后进入文章的详情页，这里获取的就是点击这篇文章。我们通常会写如下视图函数：

def detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    context = { 'article' : article }
    return render_to_response('blog/detail.html',context)
同样的，如果这种需求多的话，开发人员就需要枯燥而乏味地大量重复写 article = get_object_or_404(Article,pk=article_id) 这样的句子，Django 通过 DetailView 来把这种逻辑抽象出来，把上面的视图函数转成类视图：

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj
model 属性告诉 Django 是获取哪个 model 对应的单个对象，template_name，context_object_name 属性和 ListView 中是一样的作用，pk_url_kwarg 相当于视图函数中的 article_id 参数，已告诉 Django 获取的是 id 为多少的 model 实例。

get_object 方法默认情况下获取 id 为pk_url_kwarg 的对象，如果需要在获取过程中对获取的对象做一些处理，比如对文章做 markdown 拓展，通过复写 get_object 即可实现。

之后的处理就和 ListView 类似了，已经实现了 render_to_response 方法来渲染模板。

以上方法在类视图调用 as_view() 方法后会被自动调用。

DetailView 总结

DetailView主要用在获取某个 model 的单个对象中
通过 template_name 属性来指定需要渲染的模板，通过 context_object_name 属性来指定获取的 model 对象的名字，否则只能通过默认的 object 获取
复写 get_object 方法以增加获取单个 model 对象的其他逻辑
复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问
使用类的通用视图的好处

通过上面的例子你可能并未体会到使用类的通用视图的好处，毕竟我们写的基于函数的视图似乎代码量更短，但这仅仅是因为例子简单而已。同时别忘了，类是可以被继承的，假如我们已经写好了一个基于类的通用视图，要对其拓展功能，只需继承原本这个类视图即可，而如果写的是函数呢？拓展性就没有这么灵活，可能需要使用到装饰器等高级技巧，或甚至不得不重复一段代码到新拓展的视图函数中。但本质上而言，基于类的通用视图依然是一个视图函数，因为最终调用时我们会通过 genericview.as_view() 方法把类视图转换成一般的视图，url 配置是这样的：
```



### 14.1 案例1 采用继承 Listview  把数据获取出来传到页面  基于函数和基于类的区别

**函数中的路由** 

**urls**

url(r'^list_1',v.list_1),

**函数的视图views**

def list_1:

​	stus=Student.objects.all()

​	//html那边遍历的是我的键

​	c={"stus":stus}

​	return  render(r,"list_1.html",c)

**函数的html**

{% for  stu in  stus %}

​	{{stu.name}}--{{stu.age}}--{{stu.phone}}

​	//这里面的br换行只需要加一个就好 ,之后每遍历一次换行一下

​	<br>

{% endfor %}



**类**

**url**

 **url(r'^list_2/',v.Myviews.as_view()),**

**models**

```
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20,default="AAAA")
    age=models.IntegerField(default=18)
    phone=models.CharField(max_length=20,default="8888888")
    def __str__(self):
        return  self.name


```

**//之后python manage.py makemigrations准备迁移**

**//python  manage.py  makegrate migrate**

**python manage.py  shell   进去之后导入学生这个模型 /表   之后添加数据**



**views**

**导入ListView:**  **from  django.views.generic  import   ListView**

**导入模型**  **from  .models import  Student**

**class Myviews(ListView)**

​	//queryset 代表是需要展示的数据

​	**queryset=Student.objects.all()**

​	//传入数据默认的名称是object_list

​	**template_name="list_html"**

```
template_name:模板名称和位置，默认在 template/app_name/modelName_list.html
如果我不给他html文件的话  那么他就默认去我的这个路径去找  找不到的话就报错了
```



**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//这里必须遍历object_list
{% for stu  in object_list %}
    {{stu.name}}--{{stu.age}}--{{stu.phone}}
<br>
{% endfor %}

</body>
</html>
```



### 14.1    案例2   给模板那边改了个名字

**urls.py**

url(r'^list_3/',v.MyListView1.as_view())

**views.py**

class MyListView1(ListView):

​	queryset=Student.objects.all()

​	context_object_name="stus"

​	template_name="list_3.html"

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//这里给变了个名字
{% for  stu  in stus %}
{{stu.name}}--{{stu.age}}--{{stu.phone}}
<br>
{%  endfor  %}
</body>
</html>

```

****

### 

### 14.2  案例3   采用继承TemplateView

from djangp.views.generic import TemplateView

- 返回一个模板内容
- templates_name: 模板的位置和名称

**urls.py**

url(r'^tpl_1/',v.MyTplVIew.as_view()),

**views.py**

//这是个死模板给个死模板

class  MyTplView(TemplateView):

​	template_name="tpl_1.html"

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1 style="color: red">hahahahhahah 好了</h1>
</body>
</html>
```

​	



### 14.3    采用继承DetailView 携带参数访问

- 如果想知道某一个对象的详细信息，需要先知道对象的一些可查询信息
- 默认输入查询信息是pk（主键）
- 在模板中，传入的对象默认名是object
- 需要定义模型
- 查询字段可修改，自定义 



#### 14.3.1 案例1 传递默认参数pk 主键

from  django.views.generic  import   DetailView

**urls **

//通过携带参数来查询对象的信息

//?P携带参数 pk  这个是DetailView 类中需要的参数不能改,+可以1个或者多个

//+可以1个或者多个  限制0-9数字  你可以给1个或者多个   如果是*你给0个或者多个

//这里代表你必须要给我参数  之后我正则来进行匹配  之后成为url 来访问

 url(r'^d_1/(?P<pk>[0-9]+)', v.DView.as_view() ),



**views.py**

class   DView(DetailView):

​	//这里也必须这么写    后面的是模型//也就是表 默认是pk  也就是主键id

​	model=Student

​	template_name="d_1.html"

​	

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
//这也必须写object

{{ object.name }}--{{ object.age }} --{{ object.phone }}


</body>
</html>
```



#### **14.3.2**  案例2 传递不是默认参数

  **urls.py**

//携带name 参数    \w 取字母数字下划线  +是取多个字母 贪婪

​			\W 取非字母数字下划线 +   贪婪 

   url(r'^d_2/(?P<name>\w+)', v.DView_2.as_view() ),

**views.py**

class   Diew_2(DetailView):

​	model=Student

​	template_name="d_1.html"

​	//如果更改查找的名称,需要更改一下内容

​	//这个内容是模型里面定义的name

​	slug_field="name"

​	slug_url_kwarg="name"

/**/装饰函数     具体看百度吧!**

**就是我让他先进入登录页面**

from django.contrib.auth.decorators import  login_required, permission_required 



### 15.  验证码的实现

**urls**

```
from django.conf.urls import url
from django.contrib import admin
from papp import views as v
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^t/', v.t),
    # 1.先访问这个  调用视图函数  给返回个带数据的图片
    url(r'^verifycode/', v.verifycode, name="verifycode"),
    # 2.1 提交判断
    url(r'^verifycodeValid/$', v.verifycodeValid),
]
```



**views**

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def t(r):
    return render(r, "vfc.html")


# 2.1   做判断
def verifycodeValid(request):
    vc = request.POST['vc']
    if vc.upper() == request.session['verifycode']:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')


# 1.1 做带数据的图片 生成数据并存入session  之后给浏览器返回一份
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    #font = ImageFont.truetype('static/msyh.ttf', 23)
    font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
```



**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script type="text/javascript" src="/static/js/jquery-1.12.4.min.js"></script>


    <script type="text/javascript">
        $(function(){
            $('#verifycodeChange').css('cursor','pointer').click(function() {
                // ?
                $('#verifycode').attr('src',$('#verifycode').attr('src')+1)
            });
        });
    </script>

</head>
<body>

<!-- 2.之后输入  提交 找到对应的视图 做判断 -->
<form method='post' action='/verifycodeValid/'>
    {%  csrf_token %}
    <input type="text" name="vc">
    <!-- 3.看不清换一个 提交到这个要数据的图片  重新调用函数-->
    <img id='verifycode' src= "{% url 'verifycode' %}" alt="CheckCode"/>
<span id='verifycodeChange'>看不清，换一个</span>
<br>
<input type="submit" value="提交">
</form>



</body>
</html>
```


## 15. API接口

**我这边把函数写好   ,之后视图也写好  之后可以把命令行的http**

进入虚拟环境  : source activate p05
安装 pip install djangorestframework

### 15.1序列化操作

**需要先安装 su apt-get  install  httpie**﻿

HTTPie （读aych-tee-tee-pie）是一个 HTTP 的命令行客户端。其目标是让 CLI 和 web 服务之间的交互尽可能的人性化。

1.先建立django项目, 建立app 之后运行起来

2.之后在模型中建立两个表

```
class Student(models.Model):
    name=models.CharField(max_length=20,default="NoName")
    age=models.IntegerField(default=18)
    gender=models.IntegerField(default=1)
    address=models.CharField(max_length=200)
    score=models.IntegerField(default=0)
class   Classroom(models.Model):
    name = models.CharField(max_length=20, default="NoName")
    room_id = models.CharField(max_length=20 )
    address = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    stu_ammount = models.IntegerField( default=20)
```

3. python manage.py  shell 进行数据添加  (s=Student()   之后  s.属性=?  s.save())

4. 之后创建一个serializers.py的文件

   ```
   #Serializers 可以把复杂的数据结构例如querysets,模型实例化转为python数据格式
   from  rest_framework  import  serializers

   #把需要给的数据的模型导入
   from .models import  Student,Classroom

   #定义 之后继承serializers的一个方法
   class StudentSerializer(serializers.ModelSerializer):
   	class Meta:
   	 #设置指定的模型
   	 model=Student
   	 #设置让他传递哪个字段的数据 也就是哪个字段的数据是可以给客户端的 通过命令行的请求  这里有一个请求的方式是 http -h 127.0.0.1:8000/student/
   	 fields=('name','score')
   ```

5. url.py

   ```
   from  django.conf.urls import url
   from  api  import  views  as  v  

   urlpatterns=[
   #为这个Student设置了一个接口
     url(r'^student/',v.StudentAPIviews.as_view(),name="student")
   ]
   ```

6. views.py

   **序列化: 把数据库里的querysets对象给转成json **

   **反序列化 : 把json   把通过POST提交的数据给存储到数据库  也就是 json 格式的数据 给转成 querysets 对象**

   ```
   #导入api视图 这里是用来继承的
   from  rest_framework.views   import  APIView

   #导入我写好模型
   from .models import Student ,Classroom 

   #导入我写好的要转的模型 的那个4.文件的类 () 用它来转换
   from  .serializer import StudentSerializer

   #
   from  rest_framework.renderers import  JSONRenderer

   #看什么请求对应调用什么视图函数
   #基于类的视图有一个比较好的好处：
    每个method都有一个独立的函数进行处理,且默认名称等于method的小写名称
   class StudentAPIview(APIView):
   	#序列化 把数据库里的对象给转换成json格式数据
       def  get(self,request):
       	#单个的数据加上条件   很多数不用添加
       	stu=Student.objects.filter(name="liyanliang")
       	print(stu) #打印出来的结果是queryset类型的一个列表
       	
       	print(stu[0]) #打印出来的是一个对象
       	# 这个是单个转换
       	ser=StudentSerializer(stu[0])
       	#许多对象的转换 这里用到我4文件写的那个类
       	ser=StudentSerializer(stu,many=True)
       	print(type(ser.data))#转换之后的数据类型
   		print(ser.data)	#转换出去的数据格式  json格式
   		
   		#把frame类型的一个字符串类型给转成字符串字节
   		byte_data=JSONRenderer().render(data=ser.data)
   		print(byte_data)
   		
   		#之后给对这个字节进行解码  给转成字json格式自符串乐
   		str_data=byte_data.decode()
   		
   		return  Response(ser.data)
   ```


### 15.2 反序列化操作  

把json   把通过POST提交的数据给存储到数据库  也就是 json 格式的数据 给转成 querysets 对象

```
# 这个是反序列化用的 生成一个内存中的bytes串
from django.utils.six import BytesIO

from  rest_framework.parsers import  JSONParser

class StudentAPIview(APIView):
 这是介绍怎么反序列化测试
def get(self,request):
	return  self.get_deser(request)

	
def get_deser(self,request):
	'''
	对于反序列化进行测试
	#先行得到一个bytes串模拟传入数据,然后进行反序列化
	stu=Student.objects.all()
	ser=StudentSerializer(stu) 
	
	byte_data=JSONRenderer().render(ser.data)
	
	#以下尝试对得到的bytes串进行反序列化 
	#既从网络中收到的stream数据后把数据最终转换成对象并存储到数据库中
    #stream代表从网络中接受到的数据流
	stream=BytesIO(byte_data)
	print(type(stream))
	#打印出来的是<_io.BytesIO object at 0x7fade6c71410>
	print(stream)
	
	#接收到的数据需要进行提取,最终提取城json格式
	json_data=JSONParser().parse(stream)
	#打印出的结果{'name': 'liyanliang', 'score': 100}
	print(json_data)
	#打印出的类型<class 'dict'>
	print(type(json_data))
	
	#提取出的json格式数据需要作为参数初始化一个序列化类对象
	ser=StudentSerializer(data=json_data)
	
	#一旦完成合法性检查,则经过检验后的数据将存入validated_data
	print(type(ser.validated_data))
	print(ser.validated_data)
	#数据合法,则可以把整个数据转成object并存入数据库
	ser.save()	
    return  Response("deser")
    
    
    
    #存入数据库测试 
 http --form  POST 127.0.0.1:8000/student/ name="liuliu" score:=40

 def get(self,request):
 	return  self.test_deser(request)
 def test_deser(self,request):
 	d=dict()
 	d["name"]="haha"
 	d["score"]=90
 	ser=StudentSerializer(data=d)
 	if ser.is_valid()
 		ser.save()
 		return  Response("Save ok")
 	else:
 		print("erroror")
 		return Response("haha")
```
### 15.3 总结    

​	bytes 转换成 比特位 \xe6       一个汉字三个字节   也就是三个比特位

​	**反序列化 ** 1.先序列化实例     ser=StudentSerializer(stu) 

 **几种可能**   2.利用实例的属性得到一个字典     ser.data

​			3.把字典给转成流  byte_data=JSONRenderer().render(ser.data)

​			4.用BytesIO 接收流 也就是变成内存了 stream=BytesIO(byte_data)

5.接收到的数据需要进行提取,最终提取城json格式	json_data=JSONParser().parse(stream)

6.提取出的json格式数据需要作为参数初始化一个序列化类对象					    ser=StudentSerializer(data=json_data)

7.一旦完成合法性检查,则经过检验后的数据将存入validated_data  检查  保存











### 15.4 权限管理

- 分成两部分
  - 登录管理
  - 授权管理-权限管理
- permission_classes
- 安全方法
  - 不会对本系统造成更改的方法
  - 包括GET，HEADER，OPTIONS
- 非安全方法
  - CREATE， UPDATE, DELETE
- 系统权限管理步骤
  - 在视图文件导入 permissions包
  - 在视图类中，添加变量permission_classes, 作为元组，并写入相应权限
- 自定义权限管理
  - 创建mypermission文件
  - 导入 permissions 包
  - 创建权限管理类，并作为permission.BasePermission的子类
  - 改写has_permission 或者 has_object_permission函数

**url.py**

```
from django.conf.urls import url

from  api  import  views as v

urlpatterns = [

	命令行下面访问http -b 127.0.1.1:8000/room  进入接口
    url(r'^room/', v.room_test.as_view(), name="room"),
]

```

###  



serilalizer.py

```

//导入frammework这个建立django 上面的工具
from  rest_framework  import   serializers
//导入模型类
from  .models import  Classroom



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # 定义需要序列化的模型名称
        model = Classroom

```



views.py

```
from  rest_framework.response import Response
from rest_framework.views import   APIView
from  rest_framework import  permissions
from  .pp import  IsLiuYing
# 继承API视图
class room_test(APIView):
	#设置权限的类  这里是一个元祖
    permission_classes = (IsLiuYing,)
    //get 就走这个   
    def get(self,request):
        return  Response("ok")
        //post  如果不指明post  那么添加数据也是post 给访问的一个响应
    def post(self,request):
        print(request.POST)
        return Response("POST OK")



```



pp.py

```
//导入权限包
from   rest_framework import  permissions
//设置权限
class  IsLiuYing(permissions.BasePermission):
    def  has_permission(self, request, view):
    //进行获取
        name=request.data.get("name",None)
        //测试传递过来的参数
        print(request.data)
        //进行设置
        if  name!="liuying":
            return  False
        else:
            return  True
```



## 16. django后台操作

1.创建django项目  django-admin  startproject  xiangmu 

  或者 ：在pycharm下安装django直接建立

2.先添加app python manage.py  startapp app1

3.setting.py  

​	1.添加app

​	2.链接mysql

```
DATABASES = {
    'default': {
       'ENGINE':'django.db.backends.mysql',
        'NAME':'py05_django',
        'USER':'root',
        'PASSWORD':'123456',
        'PORT':3306,
        'HOST':'127.0.0.1'
    }
}
```

​	3.主__init__ 下面导入pymysql

​		import pymysql

​		pymysql.install_as_MySQLdb()

4.配置模板

​	'DIRS':[os.path.join(BASEDIR,'templates')]

5.配置静态文件

```
STATIC_URL = '/static/'
# 配置静态文件
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

```

6.改成中文

```
LANGUAGE_CODE = 'zh-hans'
```



7.模型设置

```
from django.db import models

# Create your models here.
#建表
#商品管理一点击 有字段显示商品名称 数量 分类 标签
class Goos(models.Model):
    name=models.CharField(max_length=30,verbose_name='商品名称')
    num=models.IntegerField(default=0,verbose_name='数量')
  	cat=models.ForeignKey('Cat',blank=True,null=True,verbose_name='分类')
  	#多对多 点击标签 出现标签名称  跟地下的Tags表进行多对多的关联
    tag=models.ManyToManyField('Tags',blank=True,null=True,verbose_name='标签')
    def __str__(self):
        return  self.name
    class Meta:
    	#给表起的名 在页面显示
        verbose_name=verbose_name_plural='商品管理'

#分类管理一点击 有字段分类名称
class Cat(models.Model):
    name=models.CharField(max_length=30,verbose_name='分类名称')
    def  __str__(self):
        return  self.name
    class Meta:
   		 #给表起的名 在页面显示 是分类管理
        verbose_name=verbose_name_plural='分类管理'
class Tags(models.Model):
    name=models.CharField(max_length=30,verbose_name='标签名称')
    #让name字段作为页面显示
    def  __str__(self):
        return   self.name

```



创建超级管理员用户  python  manage.py  create superuser

数据库迁移 

​	准备迁移:    python  manage.py  makemigrations 

​	开始迁移： python  manage.py  migrate



# Django2龙哥追加 有机会看看文档吧

## 1.流程

### 1.1  框架比较

**flask**

​	轻量级 所有模块需要组装，开发一些小型应用

**django**

​	好    数据库同步系统

​			makemigrations

​			migrate

​	admin  自带后台

**tornado**

​	高并发框架(web开发框架  出色的web服务器)	

​	异步非阻塞

​	websocket-长链接  新协议

### 1.2 前期节奏

**安装django**

​	pip install django== 版本号

​	进入桌面    cd  Desktop  

**创建项目**

​	自动创建 需要安环境

​	命令行创建



**MVT 模型 视图   模板 	**

**配置setting**

```
							
									
										#当前文件的绝对路径一直到文件了
						#这获取路径上一层也就是去了文件
		 #又获取了上一层目录路径
#获取项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#生成用户名的时候  加密字符串
SECRET_KEY = '^rxmucj=x0n52pj)#nw&kai*_=!4#2^cusw5rt0wb8-&n)b*w9'

#开启调试模式
	#1.视图函数变动，自动重启服务器
	#2.错误详细输出，环境变量
	#3 生产环境中需要关闭
DEBUG = True

#允许访问的域名的或者ip地址
#现在不给*只能自己访问
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shujuzhanshi.apps.ShujuzhanshiConfig',
    #加app 新建需要手动
    'app'
]


#中间件
#帮你处理请求之前进行再进行一层处理，在响应之前再进行一次响应处理
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#总的urls 配置    改项目名字 这也要改
ROOT_URLCONF = 'daxiangmu.urls'


配置模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #模板的配置 项目文件夹    下面templates 组合   就是templates  的路径
        #如果还有别的模板  再写一项  ，后面
        'DIRS': [os.path.join(BASE_DIR, 'templates')，] ,
        
        #这个是如果为True在app下再建一层模板文件夹 它也会去找  
        #如果为False 则不会去找了
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#数据库设置  默认链接sqllite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #库名
        'NAME': 'pachong',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        #端口号整形   默认是3306  不写也是3306  除非你写别的 
        'PORT': 3306,
    }
}

#后台admin的语言
#默认en-us
LANGUAGE_CODE = 'zh-hans'

#修改时区  
#时区里没有北京    只有上海和重庆
默认为UTC
TIME_ZONE = 'Asia/Shanghai'

#时区相关的配置  先不用管
USE_I18N = True

USE_L10N = True

USE_TZ = False

#静态文件的路由(url)地址  
#http://www.baidu.com/static/ 可能这样访问
STATIC_URL = '/static/'


#静态文件路径地址  存储路径
STATICFILES_DIRS = (
#一定要加一个, 是个元祖
 os.path.join(BASE_DIR,'static')，
)
```



**启动**

​		//默认端口号80000

​	**python manage.py  runsever**

​	//改成6000  ip地址也可以修改

​	**python  manage.py runserver 127.0.0.01:6000**





## 2.案例

### 2.1 1对1 表关系页面展示学生和信息

**urls.py**

```
from  django.conf.urls  import url

from django.contrib  import admin
#加载静态图片
from django.views.static  import serve
from home  import  views as v 
from edu import settings
import  os 

urlpatterns=[
	#系统自带后台  前提需要创建一个账户  python manage.py createsuperuser
  url(r'^admin/',admin.site.urls),
  
 #这波操作是为了让轮播图 能有个路由 在新窗口打开 固定写法 
 #upload是里面单独放的从后台上传图片的文件夹
 url(r'^upload/(.*)$',serve,{'document_root':os.path.join(settings.BASE_DIR,'upload')}),
 
 
url(r'^$',v.shituone),

url(r'^student/$',v.student,name='student')

]
```



**models.py**

```
from  django.db import models 
#你现在想上传  banner图  这些都是你需要的字段  而且这些只是模型 迁移之后成了表
class Banner(models.Model):
	'''
	前面的是字段名
	'''
	#启动状态 0,1 是 数据库里存的标识
	status_choice=[(0,'下线'),(1,'上线')]
	#verbose_name  在后台上显示的名字   这些都是字段类型
	status = models.CharField(verbose_name='状态',max_length=30)
	#数据展示的先后排序 整形一般给个默认值
	weight = models.IntegerField(verbose_name='权重:从大到小',default=0)
	#上传图片到的位置
	img=models.ImageField(verbose_name='图片',upload_to='upload/banner/')
	#这里注意 default 数据库为空 但是也存空字符串了其实 blank True 是后台添加的时候可不可以为空 True可以 False不可以
	#null  是数据库 可不可以为空   True可以  False 不可以
	href=models.CharField(verbose_name='图片链接',max_length=300,blank=True)
	
	#auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
	#auto_now_add为添加时的时间 ，更新对象时不会有变动
	date_add = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		#这两个起的名  第一个 是进入django后台 显示的标题  第二个是进去之后每一层都显示的标题  如果写上的话
		verbose_name_plural = verbose_name = '首页Banner'
	def __str__(self):
		return self.name
		
		
#进行表关联 一个学生一个信息
class Student(models.Model):
	#设置字段后台能操作  之后也操作数据库了相当于
	status_choice = [(0,'下线'),(1,'上线')]
	status = models.IntegerField(verbose_name='状态',default=1,choice=status_choice)
	#权重  数字大的在前面    如果为-数字小的在前面 因为--得正啊 
	weight = models.IntegerField(verbose_name='权重:从大到小',default=0)
	name=models.CharField(verbose_name='学生姓名'，max_length=30)
	#里面加的verbose_name 是在后台进行显示的  标签吧算是
	company = models.CharField(verbose_name='公司',max_length=30)
	salary=models.IntegerField(verbose_name='薪水')
	#ImageField字段下面有一个upload的参数   这个参数是图片上传到什么位置
	avatar=models.ImageField(verbose_name='头像','upload_to'='upload/avator/')
	class Meta:
		verbose_name_plural=verbose_name='学生'
	def  __str__(self):
		return   self.name
		
#学生详情表  和这个表进行关联
class  StuDetail(models.Moldel):
	#进行关联后  得到了student对象   onetoone  进行任意一边的关联操作
	student = models.OneToOne(Student)
	#权重
	weight = models.IntegerField(default=0,verbose_name='权重:从大到小')
	#简介   进行编写的字段是  TextField
	industry = models.TextField(verbose_name='简介')
	class Meta:
		verbose_name_plural = verbose_name = '学生详情'
		
	def __str__(self):
		return self.student.name
		
		
		
查询   
```

****views**.py**

```
from django.shortcuts import render

# Create your views here.
from home.models import  Banner,Student,StuDetail
def  shituone(request):
    #把上线的图片查询出来  数越大权重越大  数据展示在前   - 号正好相反 权重大的展示在后

    # banner_list queryset对象集    order_by排序里面传字符串
    banner_list=Banner.objects.filter(status=1).order_by('-weight').all()[:2]
    #学生信息
    stu_list=Student.objects.filter(status=1).order_by('-weight')

    #学生简介信息
    #按权重排完序取第一个
    #这里需要好好看看模板  stu_best.student.avatar.url 这个student是关联的对象  在关联表中.（相当于去去另外一个表中的值)
    # 后面的操作是.avatar  取图片  在.url  取的是路径
    #从小到大 权重的值越小越靠前  加上-号
    stu_best=StuDetail.objects.order_by('weight').all()

    print(stu_best)
    #上传完图片
    return  render(request,'index.html',locals())

def  student(request):
    return render(request,'student.html')
```



**admin.py需要注册**

```
from django.contrib import admin

from home  import  models  
class StudentInline(admin.StackedInline):
	model=StuDetail
	
#这个是在一起显示   需要把刚才写好的StudentInline
class StudentAdmin(admin.ModelAdmin):
	#注意固定写法  列表里的类可以变化
	inlines = [StudentInline]
#这两个需要关联的表  必须一起注册
admin.site.register(Student,StudentAdmin)

#注册以下数据库模型  表结构 要不没法在后台看到
admin.site.register(Banner)
```



###  2.2 1对多外键查询投票

**models.py**

```
from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    # 在创建的时候 自动添加系统时间
    date_pub = models.DateTimeField()

    def __str__(self):
        return self.question_text

    # 判断是否最近发布的投票
    def was_published_recently(self):
        return self.date_pub > timezone.now() - timedelta(minutes=1)

    was_published_recently.admin_order_field = '-date_pub'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否最近一天发起的投票?'


    class Meta:
        verbose_name = verbose_name_plural = '投票主题'

class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey('Question')

    class Meta:
        verbose_name = verbose_name_plural = '投票选项'


    def __str__(self):
        return self.choice_text
```





**视图**

```
from django.shortcuts import render,HttpResponse,Http404,get_object_or_404
# Create your views here.
from . import models

def index(request):
    question_list = models.Question.objects.order_by('-date_pub').all()[:5]
    return render(request,'poll/index.html',locals())

def detail(request, question_id):

    question = get_object_or_404(models.Question,id=question_id)

    return render(request,'poll/detail.html',locals())
    # return HttpResponse("You're looking at question %s." % question_id)
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    question = models.Question.objects.get(id=question_id)

    cid = request.POST.get('cid',None)

    # 投票计数
    if cid is not None:
        choice = models.Choice.objects.get(id=cid)
        choice.votes += 1
        choice.save()
    else:
        message = '你必须选择'
        return render(request,'poll/detail.html',locals())

    return render(request,'poll/results.html',locals())

    # return HttpResponse("You're voting on question %s." % question_id)
```



**模板**

detail.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{ question.question_text }}</h1>
<span style="color: #ff7f13" >{{ message }}</span>
<form action="{% url 'poll:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="cid" value="{{ choice.id }}">{{ choice.choice_text }}
{% endfor %}
<input type="submit" value="投">
</form>
</body>
</html>
```

index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
{% for question in question_list %}
    <li><a href="{% url 'poll:question' question.id %}"> {{ question.question_text }} </a></li>
{% endfor %}
</ul>
</body>
</html>
```

results.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}-----{{ choice.votes }}</li>
{% endfor %}
</ul>
</body>
</html>
```





### **2.2 2瀑布流**

models.py

```
from django.db import models

# Create your models here.

class Banner(models.Model):
    # 启用状态
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(verbose_name='状态',default=1,choices=status_choice)

    name = models.CharField(verbose_name='banner名称',max_length=30)

    # 权重
    weight = models.IntegerField(verbose_name='权重：从大到小',default=0)

    # pip install Pillow
    img = models.ImageField(verbose_name='图片',upload_to='upload/banner/')

    href = models.CharField(verbose_name='图片链接',max_length=300,blank=True)

    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '首页Banner'

    def __str__(self):
        return self.name


class Student(models.Model):
    # 学生是否上线
    status_choice = [(0,'下线'),(1,'上线')]
    status = models.IntegerField(verbose_name='状态',default=1,choices=status_choice)

    # 权重
    weight = models.IntegerField(verbose_name='权重：从大到小',default=0)
    name = models.CharField(verbose_name='学生姓名', max_length=30)

    company = models.CharField(verbose_name='公司',max_length=30)
    salary = models.IntegerField(verbose_name='薪水',default=10000)

    avatar = models.ImageField(verbose_name='头像',upload_to='upload/avatar/',default='upload/avatar/default.jpg')

    class Meta:
        verbose_name_plural = verbose_name = '学生'

    def __str__(self):
        return self.name

class StuDetail(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True)
    # 权重
    weight = models.IntegerField(verbose_name='权重：从大到小',default=0)

    industry = models.TextField(verbose_name='简介',default='', blank=False)

    class Meta:
        verbose_name_plural = verbose_name = '学生详情'

    def __str__(self):
        return self.student.name

```

**admin.py**

```
from django.contrib import admin

# Register your models here.
from home import models

class StudentInline(admin.StackedInline):
    model = models.StuDetail

class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(models.Banner)
admin.site.register(models.Student,StudentAdmin)
```



**view.py**

```
from django.shortcuts import render,HttpResponse

# Create your views here.
from home.models import *
import json

def index(request):
    banner_list = Banner.objects.filter(status=1).order_by('-weight').all()[:5]
    stu_list = Student.objects.filter(status=1).order_by('-weight').all()[:5]

    stu_best = StuDetail.objects.order_by('-weight').first()

    return render(request,'index.html',locals())

def student(request):
    return render(request,'student.html')

def getstu(request):
    # 获取page
    page = request.GET.get('page',None)

    try:
        page = int(page)
        print(page)
        student_list = Student.objects.filter(status=1).order_by('-weight','-id').all()[page * 2: page * 2 + 2]

        stu_divs = getstu_div(request,student_list)
        return HttpResponse(json.dumps(stu_divs))

    except Exception as e:
        print(e)

def getstu_div(request,student_list):
    tmp = '''
        <div class="grid-boxes-in masonry-brick">
            <img class="img-responsive" style="width: 320px;" src="/%s" alt="">
            <div class="grid-boxes-caption">
                <h3><a href="#">%s</a></h3>
                <ul class="list-inline grid-boxes-news">
                    <li><span>公司：</span> <a href="#">%s</a></li>
                    <li><span>薪资：</span>%s/月</li>
                </ul>
                <p>
                    %s……</p>
            </div>
        </div>
    '''
    stu_divs = []
    for stu in student_list:
        # print(stu.studetail)
        try:
            industry = stu.studetail.industry
        except Exception as e:
            industry = ''

        div = tmp % (stu.avatar.url,stu.name,stu.company,stu.salary,industry)
        stu_divs.append(div)

    return stu_divs

def teststu(request):
    s = Student.objects.all()
    for stu in s:
        print(stu.studetail.industry)
    return HttpResponse(s.count())
```

**urls.py**

```

from django.conf.urls import url
from django.contrib import admin
from home import views
from django.views.static import serve
from edu import settings
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^student/$', views.student ,name='student'),
    url(r'^getstu/$', views.getstu ,name='getstu'),
    url(r'^teststu/$', views.teststu ,name='teststu'),
    url(r'^upload/(.*)$', serve,{'document_root': os.path.join(settings.BASE_DIR,'upload')}),
]

```

**templates**

```
{% extends 'base.html' %}
{% load static %}

{% block css %}
    <link href="{% static 'index/app.css' %}" rel="stylesheet">
    <style>
        .sv-error-msg {
            bottom: -15px;
            position: absolute;
            font-size: 8px;
            color: #a94442;
            background: #f2dede;
            border: 1px solid #ebccd1;
            height: 15px;
            line-height: 15px;
            padding: 0 20px;
        }

        .horiz-img-region {
            padding: 10px 0px;
            margin-top: 20px;
        }

        .horiz-img-region .horiz-img-item {
            width: 176px;
            float: left;
            margin: 0 10px;
        }

        .horiz-img-region .horiz-img-item img {
            height: 160px;
            width: 100%;
            display: block;
        }

        .thumbnail .caption {
            height: 51px;
            text-align: center;
            overflow: hidden;
        }

        .thumbnail .caption p {
            margin: 0px;
        }

        .recruit_region {
        }

        .recruit_list {
            color: #555;
            margin: 5px 0px;
            display: block;
            cursor: pointer;

        }

        .recruit_list .title {
            padding-left: 0px;
            display: block;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .recruit_list .salary {
            text-align: right;
        }

        .owl-clients-v1 img {
            width: 120px;
            height: auto;
        }


    </style>
    <link rel="stylesheet" href="{% static 'index/student.css' %}">
{% endblock %}

{% block body %}

    <div class="bg-gray ptb20">
        <div class="wrap">

            <div class="headline-center margin-bottom-60">
                <h2>关于KAMI教育</h2>
                <p>用责任和情怀专注IT教育30年<br>
                    自8月2日上线以来，由优酷、奥飞剧业、雄孩子传媒、有妖气联合出品的《镇魂街》凭借逼真的特效场景搭建、《镇魂街》已累计8亿的网络播放量，</p>
            </div>

            <div class="blog_masonry_3col">
                <div class="container content grid-boxes masonry clearfix"
                     style="position: relative;padding-top: 0;padding-bottom: 0;">
                    <div class="column-flow">


                        <div class="grid-boxes-in masonry-brick">
                            <img class="img-responsive" style="width: 320px;"
                                 src="./index/1.jpg" alt="">
                            <div class="grid-boxes-caption">
                                <h3><a href="#">小美</a></h3>
                                <ul class="list-inline grid-boxes-news">
                                    <li><span>公司：</span> <a href="#">北京其二布莱特科技公司</a></li>
                                    <li><span>薪资：</span>200000/月</li>
                                </ul>
                                <p>
                                    公司一群老油条，懒散惯了！对于领导的工作安排也是拖拖拉拉！这样下去不行啊。于是厂长，把他女婿安排进来，监督他们！老油条不愧老油条，没多久。厂长女婿也被他们拖下水，上了他们的贼船……</p>
                            </div>
                        </div>


                        <div class="grid-boxes-in masonry-brick">
                            <img class="img-responsive" style="width: 320px;"
                                 src="./index/1.jpg" alt="">
                            <div class="grid-boxes-caption">
                                <h3><a href="#">刘涛涛</a></h3>
                                <ul class="list-inline grid-boxes-news">
                                    <li><span>公司：</span> <a href="#">e天天教育有限公司</a></li>
                                    <li><span>薪资：</span>200000/月</li>
                                </ul>
                                <p>整啥哦呢</p>
                            </div>
                        </div>


                    </div>
                    <div class="column-flow">


                        <div class="grid-boxes-in masonry-brick">
                            <img class="img-responsive" style="width: 320px;"
                                 src="./index/1.jpg" alt="">
                            <div class="grid-boxes-caption">
                                <h3><a href="#">小妹儿</a></h3>
                                <ul class="list-inline grid-boxes-news">
                                    <li><span>公司：</span> <a href="#">北京其二布莱特科技公司</a></li>
                                    <li><span>薪资：</span>1999999/月</li>
                                </ul>
                                <p>觉得自己老牛逼了</p>
                            </div>
                        </div>


                        <div class="grid-boxes-in masonry-brick">
                            <img class="img-responsive" style="width: 320px;"
                                 src="./index/1.jpg" alt="">
                            <div class="grid-boxes-caption">
                                <h3><a href="#">Alice</a></h3>
                                <ul class="list-inline grid-boxes-news">
                                    <li><span>公司：</span> <a href="#">中国中央电视台CCAV</a></li>
                                    <li><span>薪资：</span>399999 /月</li>
                                </ul>
                                <p>瞎来了啊</p>
                            </div>
                        </div>


                    </div>
                    <div class="column-flow">


                        <div class="grid-boxes-in masonry-brick">
                            <img class="img-responsive" style="width: 320px;"
                                 src="./index/1.jpg" alt="">
                            <div class="grid-boxes-caption">
                                <h3><a href="#">拉稀</a></h3>
                                <ul class="list-inline grid-boxes-news">
                                    <li><span>公司：</span> <a href="#">北京其二布莱特科技公司</a></li>
                                    <li><span>薪资：</span>1999999/月</li>
                                </ul>
                                <p>拉了一晚上呀</p>
                            </div>
                        </div>


                    </div>

                </div><!--/container-->
            </div>
        </div>
    </div>
{% endblock %}

{% block js %}
    <script type="text/javascript">
        //滚动事件
        var page = 0;
        $(document).scroll(function(){
            var awaybom = $(document).height() - $(window).scrollTop() - $(window).height()
            if (awaybom === 0){ // 判断是否到底部
                //发起ajax请求
                $.get('{% url 'getstu' %}',{'page':page},function(data){
                    //data响应数据
                    data = JSON.parse(data);
                    $(data).each(function(index,value){
                        //把数据加载到页面上
                        var min = 10000; //最小div高度
                        var mindiv = null; // 最小div
                        $('.column-flow').each(function(index_m,value_m){
                            if ($(value_m).height() < min){
                                min = $(value_m).height();
                                mindiv = $(value_m)
                            }
                        });
                        mindiv.append(value)
                    })

                });

                //页数+1
                page++
            }
        })
    </script>
{% endblock %}
```



###  2.3 多对多 视频分类展示

 看硬盘里的文件吧 需要的时候！

# **----------------------------------**



# 爬虫



构建爬虫程序主要步骤

​	1.明确爬取目标，url地址

​	2.构建http请求，发起请求

​	3.处理响应结果（响应头，响应体)

**为什么要做爬虫**

​	

```
都说现在是“大数据时代” 那么数据从何而来 途径有哪些？
		存储 hadoop
    	 获取 爬虫
          分析 数据分析 机器学习 人工智能

	1.企业产生的用户数据：大型互联网公司有海量用户，所有有天然积累数据的优势，table

  中小型公司也开始积累数据

	2.数据购买平台，通过购买获得需要的数据  （贵阳大数据交易所，数据堂，国云数据市场）

	3.数据管理咨询公司：庞大的数据数据采集团队，通过市场调研，问卷调查，专家对话，样本检测(麦肯锡，埃森哲，艾瑞咨询)

 	4.政府/机构公开的数据：中华人民共和国统计局数据联合国数据，纳斯达克

```



**什么是爬虫**

```
	抓取网络数据的应用程序
```



**如何获取网络资源**

​	

```
    1.bs cs

    2.bs结构三大特征
        1.url同一资源定位符
            构成：协议://主机（二级域名）域名:端口/网站路径?key1=value1&key2=value2#
        2.数据呈现都是用html呈现

        3.协议都是http或者https
```



**构建爬虫程序主要步骤**

```
1.明确爬去目标，url地址
2.构建http请求，发起请求
3.处理响应结果（响应头，响应体）
   a.如果是数据则存储（mysql）
        年龄 性别 体重
   b.如果页面理由其它需要提取的url，则执行步骤1
```



**为什么要用python爬虫**

```
1.php，世界上最好的语言，但是天生不是干这个的，对多线程，多进程支持不好，并发能力很弱，爬虫对工具（包）效率要求很高

2.java，它是python爬虫的主要对手，爬虫生态也很健全，java语言很笨重，代码量很大

  java程序重构成本高，任何修改导致代码变动很大，爬虫是经常需改代码的一类程序

3.c \ c++ 能做爬虫，比java还要复杂

4.python，语法优美，代码简介，开发效率高（优点），模块多（包）https://pypi.python.org/pypi，

  强大的爬虫框架scrapy，成熟高效的分布式爬虫

```

**课程主要内容：**

```
1 如何发起请求 urllib request /  requests（安装）
```



**如何解析页面**

```
   响应内容：
        html
        json "[{key : value},{key : value}]"
        img

    正则（re） xpath beautifulsoup4 jsonpath（处理json的）
```



**反反爬虫手段**

```
  1.headers
        1.user-agent  关键请求头
        2.cookie
        3.host
        4.refer

    2.代理ip

    3.突破登陆限制
        1 模拟post提交表单
        2 cookie
    4.突破js数据加载（解析js）  filder抓包软件 浏览器 火狐 谷歌
    	抓取js加载数据的一种方法，找数据接口，爬虫不是看到才能抓到

    5.请求频率
```

**框架开发**

    封装功能 -- scrapy



**5.分布式爬虫 --- scrapy-redis（模块）**



## 1. 模仿浏览器请求

urllib.request 模块提供了最基本的构造 HTTP 请求的方法，利用它可以模拟浏览器的一个请求发起过程



最基本的爬取网页写入文件

```
from urllib  import  request
base_url='http://www.baidu.com'
#发起http请求，返回类文件对象
response=request.urlopen(url=base_url)
#获取响应内容
html=response.read()
#把响应的内容进行解码 
html=html.decode('utf-8')
#文件名baidu.html
with open('baidu.html','w',encoding='utf-8')as f:
	f.write(html)
```



### 1.1案例1 爬取网页

1.只爬取一个网页返回:

```
#导入request模块，parse模块是对url携带的参数进行编码 把汉字给转成编码格式 因为浏览器的请求头是编码的格式
from  urllib import request,parse
#请求的网址
base_url='http://www.baidu.com/s?'
qs={
  #wd是url的参数?wd= 小妹 见图1
  'wd':'小妹'
}
#请求地址需要进行url编码 把汉字给转成编码格式  因为浏览器的请求头是编码格式见图2
qs=parse.urlencode(qs)
#构建请求对象 参数是请求地址url  还有一个参数是请求头 浏览器身份请求头
req=request.Request(base_url+qs)

#发起http请求,返回类文件对象
response=request.urlopen(req)
#获取响应内容 并且进行解码
print(response.read().decode('utf-8))


```

**图片1**

![xiaomei](/xiaomei.png)



**图片2**

![2018-01-04_202726](/2018-01-04_202726.png)

2.根据输入不一样的参数爬取指定的网页

```
from  urllib  import  request,parse

def baidu(wd):
	base_url='http://baidu.com/s'
	qs={
      'wd':wd
	}
	qs=parse.urlencode(qs)
	#构建请求对象 参数是请求的url地址 还有一个参数是请求头 浏览器身份请求头
	req=request.Request(base_url+qs)
	#发起http请求，返回类文件对象
	response=request.urlopen(req)
	print(response.read().decode('utf-8))
//测试代码 这行代码的意思是只能在当前文件下运行才运行下面的代码
//别的模块导入不运行main下面的代码
if__name__=='__main__':
	while True:
		wd=input('请搜索: ')
		if wd=='q':
			break
		else:
			baidu(wd)
	
```

​	

### 1.2案例2  请求头构造

```
from  urllib import request
base_url='http://www.xicidaili.com'
headers={
 #浏览器身份请求头
 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
req=request.Request(url=url_base,header=headers)
html=response.read()
html=html.decode('utf-8')
print(html)
```



### 1.3案例3  爬取百度自行翻译程序

```
from  urllib  import  request,parse
#把json 格式转 字典
import json

def  fanyi(keyword):
	#要请求的url   通过fiddler抓包工具来抓取
	base_url='http://fanyi.baidu.com/sug'
	#构造请求数据也就是参数
	data={
      'kw':keyword
	}
	#看情况
	headers={
      'Content-Length':len(data)
	}
	#构造请求对象 参数是请求地址url  
#需要把data参数进行编码为 因为请求头上的显示为编码格式如果是汉字的话，这里进行编码防止出错					   req=request.Request(url=base_url,data=bytes(data,encoding='utf-8'))
	#发起http请求，返回类文件对象
	response=request.urlopen(req)
	#服务器处理我的请求 给我的响应 对其进行解码 因为是json 解码之后还要给转成字典
	res=response.read().decode('utf-8')
	res=json.loads(res)
	res=res['data']['0']['v']
if__name__=='__main__':
	while True:
		keyword=input('请输入要查询的信息')
		if keyword=='q'
			break
		else:
			fanyi(keyword)
	
	
```



### 1.4 案例4 分页搜索

```
from  urllib import request,parse
import os 
tieba_name=input('请输入贴吧名称: ')
start=input('起始页')
end=input('结束页')
#构建查询参数
qs={
  'kw':tieba_name
}
base_url='https://tieba.baidu.com/f?'+qs
#生成几页到几页
#转成整形因为输入的是字符串   
for  page in  range(int(start),int(end)+1)：
	#因为第一页是从0开始的  
     pn=(page-1)*50
     #计算完在给转成字符串
	fullurl=base_url+'&pn='+str(pn)
	response=request.urlopen(fullurl)
	html=response.read().decode('utf-8')
	with open (tieba_name+'/'+str(page)+'.html','w',encoding='utf-8') as f:
	f.write(html)
```

### 1.5 案例5 忽略https 请求的证书效

```
from  urllib  import request
#忽略https   请求的证书校验 
import   ssl
#写成https 就是有证书验证  为了防止这个报错需要导入import  ssl  
ssl._create_default_https_context=ssl._create_unverified_context
base_url='https://www.12306.cn/mormhweb/'
response=request.urlopen(base_url)
print(response.read().decode('utf-8'))

```



### 1.6 案例 人人网  

#### 1.6.1post

这里爬虫  通过修改请求头里的cookie直接进入网站 没cookie进不去

需要先登陆才能生成cookie

```
from urllib import request,parse
#铺垫 让服务器先设置生成一个cookie 之后为了cookie 管理对象做铺垫
#表单提交的地址
login_url='http://www.renren.com/PLogin.do'
#参数
data={
  'email':'1752570559@qq.com',
  'password':'1234qwer'
  
}
#转换结束 email=1752570559%40qq.com&password=1234qwer


data=parse.urlencode(data)
headers={
#给请求头加上长度 url编码完之后的长出
  'Content-Length':len(data)
}
#b'email=1752570559%40qq.com&password=1234qwer'
#构建请求的时候需要把所携带的参数给进行编码转换成b模式
req=request.Requesst(url=login_url,data=bytes(data,encoding='utf-8'),headers=headers)
#发起http请求  返回类文件对象
response=request.urlopen(req)
print(response.read().decode('utf-8'))
```

#### 1.6.2 session cookie

Cookie 浏览器请求报文 会有cookie 证明他有cookie 

Cookie 里面有sessionID 和 名字 值 服务器对其进行索引

如果用户第一次访问  服务器会创建一个session 并且加上特殊的算法加上其他的内容并且在服务器保存起来  之后把这段sessionid  给到浏览器   通过响应报文 set-cookie 让浏览器保存起来   并且还有名字和值

当用户再次发送请求时，会带着cookie  服务器会通过索引里面的值来进行获取信息



2. 这个是我我登陆过了   之后来修改cookie  进行进入

```
from  urllib  import  request

base_url='http://www.renren.com/440906810'

//这里通过fiddler 来进行抓取的请求头
//通过正则给转成字典格式  这样做比较方便
操作：pycharm 下 view 下面 Toolbar 之后来 采用正则 勾取正则 来对其转换 之后来进行 replace  all
(.*): (.*) 
"$1" : "$2",  

//请求头

headers={
"Host": "www.renren.com",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer": "http://www.renren.com/SysHome.do",
# "Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",

#     通过修改请求报文cookie  直接进入网站

"Cookie": "anonymid=jc0c6dok-7kb3ae; depovince=BJ; _r01_=1; JSESSIONID=abcnoXJzhRhEFaax5Qadw; ick_login=1572dc66-66f1-47cf-b2c0-c56147421534; first_login_flag=1; ln_uact=1752570559@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=83f9db7d-c755-4508-a8b4-e5e1b76e230a%7C13cfe4e0f2468cd238a9520eb2c92717%7C1515061836267%7C1%7C1515061835491; wp_fold=0; jebecookies=bece12aa-c37d-413b-84f8-81dc0133551e|||||; _de=31795CAA550243A1FFFC179CCE3D61136DEBB8C2103DE356; p=712dcb58736efb0cb176db6858b686810; t=2af66ea14d58d0d65926d8484577e8c80; societyguester=2af66ea14d58d0d65926d8484577e8c80; id=440906810; xnsid=3f0556d1; loginfrom=syshome",

}

//构造请求
req=request.Request(url=base_url,headers=headers)
//发送请求
response=request.urlopen(req)
print(response.read().decode('utf-8'))


```



#### 1.6.3  cookie  管理

//有cookie 管理器  没登陆的号也能登陆

```
from  urllib  import   request,parse
#cookie  管理模块
from   http import   cookiejar
#返回存储cookie的一个对象
cookie=cookie.CookieJar()
#返回一个cookie管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#请求管理器  参数可以加多个 可以加多个管理器
#这里给openner做成全局对象
opener=request.build_opener(cokkie_handler)


def login():
	login_url='http://www.renren.com/PLogin.do'
	data={
      'email':'1752570559@qq.com',
      'password':'1234qwer'
	}
	data=parse.urlencode(data)
	headers={
      'Content-Length' : len(data)
	}
	req=request.Request(url=login_url,headers=headers,data=bytes(data,'utf-8'))
	//发送请求
	response=opener.open(req)
	
#看个人首页
def  getHome():
	home_url='http://www.renren.com/440906810'
	#在发请求
	response=opener.open(home_url)
	print(response.read().decode('utf-8))
	
'''
这样做的好处  在后续  有很多页面需要请求
都用opener  去请求就行了    他就都带着cookie  他就帮你管理了
'''
	
if__name__=='__main__':
	#已登陆界面去查看结果  先调用login 
	login()
	#访问首页
	getHome()
	


```



### 1.7豆瓣一次性获取所有数据 js

```

#在浏览器输入chrom://extensions/完成安装json的工具
#在抓包工具中  来抓取js请求的数据   点击js的包
#在底下row的响应行中  来获取响应数据 通过上面的row请求行 的GET  地址来敲回车
#limit语句   后面是两个参数  也可以一个  从多少开始  查询多少条数据
#1个参数的话就是查询多少条

#抓接口 （这里强调一下 如果数据是从请求的网页上的响应看不到，利用抓包工具 请求js获取数据的接口  之后对这个网站进行操作  一般来说使用xpath规则来提取数据)
from  urllib  import  request ,parse
import  json
#&start=20&limit=20
# 这个是一次全部获取从0  写死的
base_url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=550"

response=request.urlopen(base_url)

data=response.read().decode('utf-8')

data=json.loads(data)

with open('F:/shuju.txt','w',encoding='utf-8')as f:
    for  item in  data:
        f.write(str(item))
        


```

假如不能一次获取  ， 则循环遍历

```
with  open('F:/豆瓣/喜剧片.txt','w',encoding='utf-8') as f:
# 遍历请求的次数0-20一次 20-40一次  总共请求多次
    for  i  in range(0,440,20):
    
        fullurl=base_url % i
    #    总共请求多次
        response=request.urlopen(fullurl)
        data=response.read().decode('utf-8')
    #     # 对得到的数据进行转成json格式
        data=json.loads(data)
    #     对请求完的数据进行打印  打印完在请求 知道不满足条件
        for  item in  data:
            f.write(str(item))
            print(item)

```

### 1.8 提取图片 下载图片

```
from  urllib  import  request
import  re
base_url='https://tieba.baidu.com/p/5504076850'
response=request.urlopen(base_url)
html=response.read().decode()

#提取图片链接

#()是分组的意思  匹配组里面的字符   .*是匹配所有 ?拒绝贪婪 遇到"就停止了
pat=re.compile('<img class="BDE_Image" src="(.*?)"')
pic_url=pat.findall(html)

#下载图片
for url  in  pic_url:
	print('downloading...%s'%url)
	#切割成列表‘/’按它切割   之后索引取出来-1 用作文件名
	fname=url.split('/')[-1]
	# 第一个参数是url  第二个参数提取出来的图片保存的位置		    (url,'F:/'+tieba_name+'/'+fname ） 
	request.urlretrieve(url,fname)
```



### 1.9  获取贴吧每页所有图片 

```
from  urllib  import  request,parse
import  re
import os

#整体思路 ：1. 先对要爬取的网站 查看参数 把参数进行拼接 因为输入是可变的
#           2. 获取源代码
#           3. 之后网站有很多页  获取最大页数

def get_detail(urls,tieba_name):
    # 对传递过来的不一样的网站不一样的后缀 进行遍历
    for  url  in  urls:
        #拼凑一下url 发起请求  返回类文件对象
        response=request.urlopen('https://tieba.baidu.com'+url)
        # 打印出来的是请求后的每一个页面
        html=response.read().decode('utf-8')
        #来对图片链接进行提取
        #（.*？） 这个组里都要了  ？拒绝贪婪  遇到"这个拿一个就走  剩下的不要了
        # 如果把?写到外面
        pat=re.compile('<img class="BDE_Image" src="(.*?)"')
        # 用这个正则找到所有请求后的每一个页面所需要的链接
        pic_url=pat.findall(html)
        # 下载图片
        for  url  in pic_url:
            print('图片下载中...%s'%url)
            # 取出图片
            fname=url.split('/')[-1]
            request.urlretrieve(url,'F:/'+tieba_name+'/'+fname)




def getpage():
    tieba_name=input('请输入贴吧名称: ')
    qs={
        'kw':tieba_name
    }
    # 对参数进行编码
    qs=parse.urlencode(qs)
    #拼接请求网址
    base_url="https://tieba.baidu.com/f?"+qs
    response=request.urlopen(base_url)
    #对返回来的html进行编码
    html=response.read().decode('utf-8','ignore')
    # 正则匹配最后一页美女贴吧里的最后一个页
    # .*都要匹配所有
    # ？拒绝贪婪 遇到到pn=(\d+)就停止了
    # \d+匹配数字贪婪  都拿走
    # re.S  防止乱码
    # 定义正则
    last_pat = re.compile(r'next pagination-item.*?pn=(\d+)',re.S)
    # 拿这个正则去匹配这个返回的html
    res = last_pat.search(html)
    # group1  是我正则匹配的数字
    # print(res.group(1))
    # 如果匹配的是不是空
    if  res is  not None:
        # 获取最大页 也就是最后一页
        # 第1页参数pn是0
        # 第2页参数是pn是50
        # 第3页参数pn是100
        # 第最后一页是2354100 /50 +1
        # 因为网页上的是数字  需要进行转换成整型计算  之后进行+1
        max_page=(int(res.group(1))/50)+1
        # 打印测试
        # print('总页数： %d'%max_page)
    else:
        print('总页数获取失败')
    # 获取用户输入的起始页
    start=input('您要下载的起始页是: ')
    end=input('您要下载的结束页是: ')
        #之后根据请求的贴吧名称来建立文件夹
    # 如果不存在，则建立
    if not  os.path.exists('F:/'+tieba_name):
        os.mkdir('F:/'+tieba_name)
    # 遍历用户输入的页数
    for  page in  range(int(start),int(end)+1):
        # 因为第一页的参数是0
        # 第二页的参数是50
        # 以此类推
        pn=(page-1)*50
        #再次发送请求
        fullurl=base_url+'&pn='+str(pn)
        # print('downloading...%s'%fullurl)
        #发起http请求,返回类文件对象
        # 相当于请求了输入的起始到结束的次数
        response=request.urlopen(fullurl)
        #每一页的网站有了
        html=response.read().decode('utf-8')
        #之后进行每一页里面的网站的提取 对里面想要的网站进行正则
        #也就是提取帖子详情 (一定要先点进去看看网页是什么参数 之后看看是什么规则 来找你想要的)
        # /正斜杠不用转义   \d+要数字  贪婪
        detail_pat=re.compile(r'/p/\d+')
        #根据正则匹配的  找到 一页里所有的每一个链接
        res=detail_pat.findall(html)
        # 在这调用函数  分开处理  传进去的参数是贴吧名tieba_name 和正则匹配出来的要处理的帖子res
        get_detail(res,tieba_name)
getpage()

```



## 2. 正则



**正则表达式**

​	**主要功能：**

​		**1.效验功能,账户 密码 电话 邮箱 ip地址**

​	 	**2.在目标字符串中匹配想要的字符**

​	**常用方法**:

​		**search**

​		**match**

​		**findall**

​	**常用规则**

​		**\d：匹配一个数字**

​		**\w:  匹配一个数字字母下划线**

​		**\s: 匹配空格**



​		**\D: 匹配非\d**

​		**\W: 匹配非\w**

​		**\S:匹配非 \s**



​		***：匹配 0-N 个\*号前面的字符**

​		**+：匹配1-N个*号前面的字符**

​		**？:匹配0-N个*号前面的字符**

​		\d*  0个数字  也行   N 个数字也行  

​		\d+  1个数字也行   多个数字也行 

​		



​		**[]：中括号里面的字符都是原字符 (无特殊含义)** 

​		**[^]:非 所有字符都是原字符 （无特殊含义)**

​		**{n}:重复n次 ** 

​				**{m,n}:  或者m到n次** 

​		**()：给正则表达式，给这个规则进行分组**

​	**group 默认是0  想单取出来每组的话加序号  从1开始  不括没有分组**



​	

​		**. 匹配任意字符，但是不能匹配换行**

​	**注意: 写规则的时候，前面尽量加r**



​		**^：必须以规则开始**

​		**$:必须以规则结束**

​			**常用于校验功能**

### 2.1 search

```
导入re模块
import  re
#编译一个规则
s='www.python.org'
pattern=re.compile('py')
#如果匹配到则返回匹配到的内容，否则返回None
res=patten.search(s)
#匹配到了
if  res is not None: 
	#获取匹配内容
	print(res.group())
else:
	print('没匹配到')
	
###如果s改一下,s='www.pythonpy.org',检索的时候第一个遇到了，就返回了，他第二个py则不匹配
###如果再改一下， 改一下规则 pattern=re.compile('pyg') 则匹配不到 
字符串当中必须要有pyg而且是连续的才能匹配的到

```

### 2.2 \d

​	**\d: 匹配一个数字**

​	**\d的范围0-9**

```
import  re
#目标字符串
s='www.pythonpy.org'

#编译规则
pattern=re.compile('\d')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	print(res.group)
else:
	print('没匹配到')


```



### 2.3 \w

​	**\w: 匹配单个数字,字母,下划线**

```
import  re
#目标字符串
s='www.pythonpy.org'

#编译规则
pattern=re.compile('\w')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	print(res.group)
else:
	print('没匹配到')

```

### 2.4 \s

​	**\s :匹配一个空格**

​	

```
import  re
#目标字符串
s='#_www.11pythonpy.org'

#编译规则
#\w匹配单个数字字母下划线   \d匹配一个数字
pattern=re.compile('\w\d')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	#抓到了 结果11
	print(res.group)
else:
	print('没匹配到')
```



### 2.5 \D \W \S

**\D: 匹配非数字**

**\W: 匹配非单个数字，字母，下划线**

**\S:匹配非空格**



```
import  re
#目标字符串
s='#_www.11pythonpy.org'

#编译规则
#\W非数字字母下划线    \D非单个数字
pattern=re.compile('\W\D')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	匹配到了#_
	print(res.group)
else:
	print('没匹配到')
```



### 2.6  \



```
import  re
#目标字符串
#如果匹配\\ 则本身转义   先在前面+r 取消转移   之后正则里面如果匹配\\
则需要写\\\\  或者正则直接写\\+匹配多个 
s='#_www.11pyt\honpy.org'

#编译规则
#目标是为了匹配上面的\ 正则里'\\'这样不行 把上面的 第二个\ 把'给转义了
r'\\'加r 取消转义  在正则里面是\\ 匹配上面一个\ 
pattern=re.compile(r'\\')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	print(res.group())
else:
	print('没匹配到')
```



### 2.7 . 

**. 万能匹配符,匹配任意字符** 



```
import  re
#目标字符串
s=r'#_www.11pyth\\onpy.org'

#编译规则
...匹配3个
.匹配一个
目标里面的.也能抓到
如果单纯的要里面的.
则需要转移 \. 就拿到里面的不是开始的.了
pattern=re.compile('...')

res=pattern.search(s)

#匹配到了
if  res is not None: 
	#获取匹配内容
	print(res.group)
else:
	print('没匹配到')
```



### 2.8 *

```
import re
s=r'ww...112153131pyyt\\hopasd.org

#\d*匹配0个到多个  这个实际是匹配到了 只不过匹配到了空字符串
pattern=re.compile('\d*')
res=pattern.search(s)

```

### 2.9 ？

```
import re
s=r'ww112153131pyyt\\hopasd.org

#\d?匹配0个到多个  这个实际是匹配到了 只不过匹配到了空字符串
#可有可无

#这个可以  结果ww112153131pyyt
pattern=re.compile('ww\d+pyyt')

#这个行 结果 ww112153131pyyt
pattern= re.compile(ww\d*pyyt')

更改一下s=r'wwpyyt\\hopasd.org
#这个行   结果 wwpyyt  这个意思就是\d如果加*有没有数字都行
pattern=re.compile(ww\d*pyt)


res=pattern.search(s)
```



### 3.0[]



```
import  re

s=r'ww321341311321pyt\\honpy.org'

#编译一个规则
#这个抓不到4   只能抓到一个w
pattern=re.compile('[a-z4]')

#这个抓到了4
pattern=re.compile('[4]')

#这个跟单纯的一个.不一样  单纯的1个点匹配任意字符  除换行
#但是这个是匹配的结果是后面的.  在中括号里面的全部还原成原字符 就是没有任何含义的  那么只能去找我原有的.的含义的字符了 

pattern=re.compile('[.]')

#中括号里面的  重复1-N  因为加上了+  结果ww
#'[a-zA-Z\d]+' 结果ww321341311321
pattern=re.compile('[a-zA-Z]'+)

import  re
s=r'_ww1321313215131pyt\\honpy.org'

#非中括号里面的  这里只取了一个_
#如果去掉_ 则取到了\\
pattern=re.compile('[^a-zA-Z\d]+)

```







### 3.1 {}

```
import  re
s=r'_ww1321313215131pyt\\honpy.org'
#固定匹配多少位 这里是匹配2位
pattern  =re.compile('{\d{2}}')

#匹配3，6位   并且尽量多的匹配
pattern=re.compile('{\d{3,6}}')
```



### 3.2 ()

```
import  re
s=r'_ww1321313215131pyt\\honpy.org'

#我要1321313215131pyt\\honpy.torg
#.任意*可有可无 
pattern=re.compile(r'(\d+).org')
res=pattern .search()
#group 默认是0  想单取出来每组的话加序号  从1开始
print(res.group())
```



### 3.3 ^

```
import  re
s=r'www.baidu.com'
pattern=re.compile(r'^w(.*?)m')
res=pattern.search(s)
#结果www.baidu.com
print(res.group())

```



### 3.4 $

**常用于校验功能时候**

```
import  re
s=r'www.baidu.com'

#以m结束
pattern=re.compile(r'^w(.*?)m')
res=pattern.search(s)
#结果www.baidu.com
print(res.group())
```





### 3.5 findall



**1.把符合规则的一串字符都提出来 并且返回个列表  如果不挨着的话**

**2.findall 在分组的情况下会把分组内容提取出来**

**3.如果分成多个组 ，那么则返回来列表里面套元祖**

4. **提取分组里的内容**  



**——**

**与search 做对比 如果匹配到则返回匹配到的内容，否则返回None，另外search 在检索过程中  如果两个部分的一样，那么则找到第一个后面的就不要了**



```
import  re
s='3121asdasd02222asdd'
##返回列表  ['3121','02222']
pat=re.compile(r'\d+')
#返回列表  ['asdasd','asdd']
pat=re.compile(r'[a-z]+')

res=pat.findall(s)

print(res)




```

```
import  re
html="""
<div>
	<ul>
		<li>抽烟</li>
		<li>喝酒</li>
		<li>烫头</li>
		<li>抠脚</li>
	</ul>
</di>
#抓出来的带
[ <li>抽烟</li>,<li>喝酒</li>,<li>烫头</li>,<li>抠脚</li>]
pat=re.compile(r'<li>.*</li>')

#抓出来的不带<li></li>
#findall 把分组内容提取出来  分一组这是   分两组看下面代码块
pat=re.compile(r'<li>(.*)</li>')

res=pat.findall(html)
print(res)
```

```
import  re
分两组
html="""
<div>
	<ul>
		<li>抽烟1</li>
		<li>喝酒</li>
		<li>烫头</li>
		<li>抠脚2</li>
	</ul>
</di>
#分成两组 
pat=re.compile(r'<li>(.*)(\d）</li>')
#这个结果是[('抽烟','1'),('抠脚','2')]
res=pat.findall(html)
print(res)
```

```
import  re
html="""
<div id=1>
	<ul>
		<li>抽烟1</li>
		<li>喝酒</li>
		<li>烫头</li>
		<li>抠脚2</li>
	</ul>
</div>
<div id=2>
	<ul>
		<li>抽烟22222</li>
		<li>喝酒222222</li>
		<li>烫头222222</li>
		<li>抠脚222222</li>
	</ul>
</div>
</div>
"""
要id为2的的
.*匹配所有  ? 要一个</div>拒绝贪婪 re.S  换行也能匹配的到 还有一个re.DOTALL 和他用法一样
pattern=re.compile(r'<div id=2>.*?</div>',re.S)
res=pattern.search(html)

和上面的区别
只不过是分没分组  取没取到外面的内容 并且能打印出来分组的内容
?放在里面和放在外面放在里面遇到括号外面的1个拿走就不要了 拒绝贪婪
pattern=re.compile(r'<div id=2>(.*?)</div>',re.S)
res=pattern.search(html)

？放在外面 所有的都拿走 直到最后一个</div>出现 并且后面没有了，结束
pattern=re.compile(r'<div id=2>(.*)？</div>',re.S)
res=pattern.search(html)
print(res.group())
```

```
import re
html=<div id="d2" adasda><div><span>乱起八糟</span></div></div>
#.*匹配所直到最后一个/div出现
#?拒绝贪婪   只拿一个
pat=re.compile(r'<div.*>.*</div>')

```







## 3.  代理ip  ip被封的解决方案

思路  

1.爬虫有的时候会遇到被禁ip的情况，这个时候你可以找一下代理网站，抓取一下ip，来进行动态的轮询就没问题了，也可以用别人做好的第三方ip代理平台，

2.如果不使用第三方的平台做代理ip，我们就必须得手动抓取ip了，可以google搜索代理ip，可以找到一大堆网站，找几个稳定的代理网站，可以写一个爬虫脚本持续抓取，要是使用量不大的话，也可以手动粘贴抓取，要是土豪一点呢就买一点其实也可以，大概1块钱可以买几千个，还是挺值得的。

### 3.0 post 有 无 验证码

```
from  urllib import   request,parse
from  http import  cookiejar
import   re

#cookie  管理器   对生成的cookie  进行管理
cookie=cookiejar.CookieJar()
cookie_handler=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(cookie_handler)
# 替换request.urlopen()   默认opener
# 这里加入管理器之后  给opener设置为默认 也可以用urlopen
# install_opener(opener) 安装opener作为urlopen()使用的全局URL opener，
# 即意味着以后调用urlopen()时都会使用安装的opener对象。opener通常是build_opener()创建的opener对象。
request.install_opener(opener)

# 为什么不一样
login_url="https://www.douban.com/accounts/login"
# https://www.douban.com/accounts/login
# https://accounts.douban.com/login

#看是否有验证码  先尝试提交
def getLoginpage():
    response=request.urlopen(login_url)
    html=response.read().decode('utf-8')
    if  '验证码' in  html:
        # 调用处理验证码的函数
        dologin(html)
    else:
        # 如果不在  则直接登陆
        login(html)
    #这里给个返回值 是在底下函数调用的时候被变量接收   否则不接收之后打印给None
    #并且这个html是请求的页面  还没用登陆的页面
    return html


# 有验证码的登陆处理
def dologin(html):
    #找到 验证码图片 和
    code_pat=re.compile(r'captcha_image" src="(.*?)"')
    code_res=code_pat.search(html)
    # 如果不为空  证明匹配到了
    if  code_res is not  None:
        #获取验证码图片的链接
        code_url=code_res.group(1)
    else:
        code_url=None
    #找到csrftoken
    token_pat=re.compile(r'captcha-id" value="(.*?)"')
    token_res=token_pat.search(html)
    # 如果token  不为空
    if token_res is  not  None:
        # 则获取token
        token=token_res.group(1)
    else:
        token=None
    #如果两个都有
    if    token  and  code_url:
        #下载验证码图片并输入
        request.urlretrieve(code_url,'code.png')
        code=input('请输入验证码: ')
        data={
            'form_email':'1752570559@qq.com',
            'form_password':'1234qwer',
            'redir':'https://www.douban.com/',
            'captcha-solution':code,
            'captcha-id':token
        }
        data=parse.urlencode(data)
        headers={
            'Content-Length':len(data)
        }
        req=request.Request(url=login_url,data=bytes(data,encoding='utf-8'),headers=headers)
        #发起请求
        response=request.urlopen(req)
        #请求得到页面
        html=response.read().decode('utf-8')
        # 看看是否登陆成功
        check_login(html)
    else:
        print('获取登陆信息失败')

# 没有验证码的处理
#则直接登陆
def  login(html):
    data={
        'form_email' : '1752570559@qq.com',
        'form_password' : '1234qwer',
        'redir' : 'https://www.douban.com/'
    }
    data=parse.urlencode(data)
    headers={
        'Content-Length' : len(data)
    }
    req = request.Request(url=login_url,data=bytes(data, encoding='utf-8'), headers=headers)
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    check_login(html)

#检查是否登陆成功
def   check_login(html):
    if  '个人主页'  in html:
        print('登陆成功,继续操作')
        con='''
        1.修改签名
        2.其他
        '''
        sign=input('输出新的签名')
        # 调用修改签名的函数
        update_sign(sign)

    else:
        print('登陆失败')


# 修改签名
def  update_sign(sign):
    #发起个人首页请求
    home_url='https://www.douban.com/people/96640796/'
    response=request.urlopen(home_url)
    html=response.read().decode('utf-8')
    print(html)
    #正则匹配这个 表单 这个隐藏域value的值
    ck_pat=re.compile(r'name="ck" value="(.*?)"')
    ck_res=ck_pat.search(html)
    if   ck_res is  not None:
        ck=ck_res.group(1)
    else:
        print('获取ck失败')
        exit()
    data={
        # 通过刚刚正则获取来的name="ck" 的 value  值
        'ck': ck,
        'signature' :sign
    }
    # 重新构建请求头
    data=parse.urlencode(data)
    headers={
        'Content-Length' : len(data)
    }
    #请求修改ajax提交的地址
    sign_url='https://www.douban.com/j/people/96640796/edit_signature'
    req=request.Request(url=sign_url,data=bytes(data,encoding='utf-8'),headers=headers)
    response=request.urlopen(req)
    print(response.read().decode('utf-8'))
if __name__ == '__main__':
    # 先调用这个
    html=getLoginpage()


```



### 3.0.1 加代理

```
from  urllib  import  request
#代码上如何使用代理

#构建免费代理
#免费代理

proxy={
    #浏览器上也可以添加代理IP
    #这个是代码上实现添加代理IP
    'http' : 'http://122.72.18.34:80',
    'https' : 'http://122.72.18.34:80'
}

#认证代理
auth_proxy={
    'http' : 'http://alice:123456@120.78.166.84:6666',
    'https' : 'http://alice:123456@120.78.166.84:6666'
}
#传入一个代理
proxy_handler=request.ProxyHandler(auth_proxy)
opener=request.build_opener(proxy_handler)

#测试这个代理好使不好使  百度查看ip
#这里如果不用openner  来发请求的话  容易导致 代理IP 那边 出现编码的问题
response=opener.open('http://www.baidu.com/s?wd=ip')
print(response.read().decode('utf-8'))
```



### 3.0.2随机代理访问西祠

```
from  urllib  import  request
import  re
import   random
import  time
import  os
users=[
    #UserAgent  中文名为用户代理
    #是Http协议中的一部分，属于头域的组成部分，UserAgent也简称UA。它是一个特殊字符串头，
    #是一种向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4..0.1',
    'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
    'Mozilla/4..0(compatible;MSIE7.0;WindowsNT5.1;Trident/4..0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4..0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4..0(compatible;MSIE7.0;WindowsNT5.1)',
]



# 1. 就是构建请求头这里有时候全写  有时候只写一部分  看情况
#2. 还有就是 data  是POST有  GET无吗
# 做成全局的header了
headers={
'Host': 'www.xicidaili.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    # 随机换用户代理
    'User-Agent': random.choice(users),
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.9',
    #有没有都行
    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWZlMzYwNDcwMmQzOWVjNjhhNDlkNjEzYzNhZTBmYzA4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMU0rYTU2ZklYZDhBUmZmQjdiQVdCTWZsMVk2ZTNWQlJFYmxFQUtoQTZsQ1k9BjsARg%3D%3D--e29ba6bc761981be8a8a1f5cec0d868f3d44fc4f; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1515077843,1515206193; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59={:d}'.format(
        int(time.time())),
    'If-None-Match': 'W/"624b22201f030abc4870fdffe68dec79"',
}



#打开函数  做好的随机ip
def  getOpener():
    # 打开爬下来的数据
    with open("quanguo.json",'r',encoding="utf-8")as f :
        strs=f.read()
        #按照文件里的换行符来切割成列表
        lts=strs.split('\n')
        # res=lts.pop()# ????????? 没打印出来结果?
        # print(res)
        #从这个列表里随机出来一个数据 是个字符串
        dict_strs=random.choice(lts)
        # 将字符串转成相应的对象（如list、tuple、dict和string之间的转换）
        #这里将字符串转成字典
        dt=dict(eval(dict_strs))
        #取出IP的值  这里键我给命的名
        ips=dt['IP']
        port=dt['端口号']
        #做成代理ip 之后我们就用这个ip来去爬取我们想爬取的网站了
        proxy={
            'http': 'http://%s:%s'%(ips,port),
            'https': 'http://%s:%s'%(ips,port)

        }
    # print(proxy)
    #代理管理器  把代理的ip给放到管理器中
    proxy_hendler=request.ProxyHandler(proxy)
    opener=request.build_opener(proxy_hendler)
    return  opener



# getpage调用传递过来的参数
def getDetail(url1,daili_dir,name,opener):
    # 每一种url传递过来了  之后在请求进去
    req=request.Request(url=url1,headers=headers)
    res=opener.open(req)
    html=res.read().decode('utf-8','ignore')
    #获取请求后当前代理种类的最大页数
    pat_lastpage=re.compile(r'>(\d+)</a> <a class="next_page"')
    #最大页数找到了
    max_page=pat_lastpage.search(html)
    print("您访问的<<%s>>一共有:%s")%(name,max_page.group(1))
    # 获取用户要下载的的页码范围
    start=int(input('请输入开始页码:\n'))
    end=int(input('请输入结束页码:\n'))
    # 爬取文件 写入文件
    with open(daili_dir+'/'+name+'.txt','w',encoding='utf-8')as fp:
        #开始遍历用户输入的页码,逐步获取页面上的内容
        for i  in range(start,end+1):
            #让他睡眠间隔  在每一次请求之前 让程序睡眠1秒
            time.sleep(1)
            # 组建url
            url2=url1+str(i)
            print('正在下载%s上第%d页上的内容')%(name,i)
            req=request.Request(url=url2,headers=headers)
            res=opener.open(req)
            html=res.read().decode('utf-8','ignore')
            #利用正则获取页面上需要保存的信息
            pat_detail=re.compile(r'<tr class="odd">.*?<img src="(.*?)".*?<td>(.*?)</td>.*?<td>(\d+)</td>.*?<td>\s*<a href=".*?">(.*?)</a>\s*</td>.*?<td class="country">(.*?)</td>.*?<td>(.*?)</td>.*?<td class="country">.*?title="(.*?)".*?</td>.*?title="(.*?)".*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
            detail_info=pat_detail.findall(html)
            # print(detail_info)
            for  a,b,c,l,e,f,g,h,m,n in  detail_info:
                # 构造一个字典
                d=dict()
                d['国家']=a
                d['IP地址']=b
                d['端口'] = c
                d['服务器地址'] = l
                d['是否匿名'] = e
                d['类型'] = f
                d['速度'] = g
                d['连接时间'] = h
                d['存活时间'] = m
                d['验证时间'] = n
                # 把字典给转成字符串
                str_dicts=str(d)
                # 写入操作
                fp.write(str_dicts)
                #每写完一次 进行换行
                fp.write('\n')



# 爬取网站 存储数据
def  getpage(daili_dir='daili_dir'):
    if  not  os.path.exists(daili_dir):
        os.mkdir(daili_dir)
    base_url='http://www.xicidaili.com/'
    # 构建请求
    req=request.Request(url=base_url,headers=headers)
    try:
        # 调用上面的函数  返回值是请求的方法 opener
        opener=getOpener()
        # 发请求
        res=opener.open(req)
        html=res.read().decode('utf-8','ignore')
        # 正则匹配  是每一种代理的链接
        pat = re.compile(r'<li><a class="false" href="(.{4.})">(.*?)</a></li>')
        result=pat.findall(html)
        # result   [('/nn/', '国内高匿代理'), ('/nt/', '国内普通代理'), ('/wn/', '国内HTTPS代理'), ('/wt/', '国内HTTP代理')]
        # 列表里面是元祖  把元祖里面的内容分着并排取出   遍历  如果元祖里面是3个 那么就来三个参数
        for kind,name in  result:

            url1='http://www.xicidaili.com'+kind
            # print("现在正在链接%s,名字是%s"%(url1,name))
            # 调用这个函数  之后把我的这个要请求的url1给传过去 name是他的名字
            getDetail(url1,daili_dir,name,opener)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    # 死循环
    while True:
        try:
            getpage()
        except:
            continue
        time.sleep(2)
        print('$'*30)
```



### 3.0.3 加代理爬西祠代理边爬边写文件 失败还有内容.

```
from  urllib import  request
import  re
import  json
#循环分页 找规则  先占位
base_url='http://www.xicidaili.com/nt/%d'

headers={
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

#认证代理
# 需要在浏览器设置
auth_proxy={
    'http': 'http://alice:123456@127.78.166.84:6666',
    'https': 'http://alice:123456@120.78.166.84:6666',
}
#正常代理ip
#如果用哪个方式就往里面传哪个
proxy={
    'http' : 'http://122.72.18.34:80',
    'https' : 'http://122.72.18.34:80',
}

#传入一个代理
#ProxyHandler(proxies)参数proxies是一个字典，
# 将协议名称（http，ftp）等映射到相应代理服务器的URL。
proxy_handler=request.ProxyHandler(auth_proxy)
#urlopen()函数不支持验证、cookie或者其它HTTP高级功能。
#要支持这些功能，必须使用build_opener()函数创建自定义Opener对象
opener = request.build_opener(proxy_handler)

# ?
opener.handlers=proxy_handler
#f 传进来写文件的参数
def  getProxy(f):
    last=10
    #先循环遍历生成数字 来发分页请求
    for  i in range(1,last+1):
        fullurl=base_url%i
        print(fullurl)
        #发起请求
        req=request.Request(url=fullurl,headers=headers)
        try:
            response=opener.open(req)
            html=response.read().decode('utf-8')
            tr_pat=re.compile(r'<tr.*?>(.*?)</tr>',re.S)
            #findall  把符合正则规则的字符串  都提取出来 并且返回一个列表
            tr_list=tr_pat.findall(html)[1:]
            #之后找到td里面的内容  也就是我想要的数据
            td_pat=re.compile(r'<td>(.*?)</td>',re.S)
            #enumerate  是遍历之后 给前面加索引 也就是计数
            for  index,tr in  enumerate(tr_list):
                td_list=td_pat.findall(tr)
                host=td_list[0]
                port=td_list[1]
                proxy={
                    'host':host,
                    'port':port
                }
                #需要导入json  给转成json 写入json文件
                #手动加个\n换行
                # f.write(json.dumps(proxy),'\n')
                #如果循环变量等于last那么就是最后一页
                # 用索引和长度 来判断是不是最后一条数据
                #每一个对应的索引+1正好是这个对应的数据  如果等于长度  那么他就是最后一条数据
                #因为目的是最后一条数据 换行 不加，
                if i==last and len(tr_list)==index+1:
                    f.write(json.dumps(proxy), '\n')
                else:
                    f.write(json.dumps(proxy), ',\n')
        #抛完异常   程序不会结束  有问题的都走这了
        except Exception as e:
            #打印出异常
            print(e)


if __name__ == '__main__':
    #open函数实例化一个写文件的对象
    f=open('daili.json','w',encoding='utf-8')
    #调用这个爬取西祠代理的函数  并且把写文件的这个对象传入进去
    f.write('[\n')
    getProxy(f)
    #关闭文件
    f.write(']\n')
    f.close()

```



### 3.1封装随机代理ip

给这个文件起个名叫download.py  可以导入直接用

```
from urllib import  request
import  json
import  random
#获取所有代理
def  getProxy():
	'''
	:return:返回值 所有代理组成的列表
	'''
	with open('daili.json','r')as f:
	# [
	{"host": "61.155.164.111", "port": "3128"},
  	   {"host": "122.72.18.34", "port": "80"} 
  	#]
  	 	#把读取的json文件内容:	给转成字典
		data=json.loads(f.read())
		#构建代理列表
		proxies=[]
		#遍历里面的数据 得到的p还是字典
		for p in data:
			#拼接成ip给放到代理列表中
			proxy={
              'http': 'http://'+p['host']+':'+p['port'],
              'https': 'http://'+p['host']+':'+p['port']
			}
			proxies.append(proxy)
		return  proxies
		
#获取一个openner
#并且来控制随机 传入来的是个列表
def getOpener(proxies)：
	'''
	:pram proxies:代理列表参数
	:return:
	'''
	#随机出一个代理ip
	proxy=random.choice(proxies)
	#创建一个代理处理器ProxyHandler(proxy)
	#ProxyHandler是一个类，其参数是一个字典:{'类型':'代理ip:端口号'}/'http': 'http://122.72.18.34:80'
	proxy_handler=request.ProxyHandler(proxy)
	#在这里我们需要定制一个opener 需要来指定代理处理器handler
	opener=request.build_opener(proxy_handler)
	#install_opener用来创建(全局)默认opener,这个表示调用urlopen将使用你安装的opener 可加可不加
	#request.install_opener(opener)
	return opener
	
#下载器
#成功得到响应结果，失败则换代理继续请求
def downloader(opener,req,proxies,timeout=5,retry=2)：
	'''
	:param opener:用来发请求
	:param req:想发请求需要先有请求对象
	:param proxies:代理列表
	:param timeout:超时时间 过了多久 我就等你这个时间 过了这个时间我就不等你了
	:param retry: 重试
	'''
	try:
		#发请求时候传入超时时间 timeout
		response=opener.open(req,timeout=timeout)
		#请求成功 直接给返回  响应内容
		return response.read()
	except Exception as e:
		#查看错误类型
		print(e)
		if retry>0:
			#随机换一个opener 并且得到一个opener
			opener=getOpener(proxies)
			#再次请求第一次retry为2 失败了打印一次异常
			#再调用 这时retry为1>0 进行第二次请求 失败 打印第二次异常
			#再请求 这时1>0进来了 进行第三次请求 之后1变成了0 失败 打印第三次异常
			#0进不来了  所以总共三次异常
		return downloader(opener,req,proxies,timeout=5,retry=retry-1)
		

#测试代码
if __name__=='__main__':
	#先得到了一个代理的列表，通过getProxy()封装的函数
	proxies=getProxy()
	#获取opener 里是控制随机的，把代理列表传入进来
	opener=getOpener(proxies)
	#请求的url
	base_url='http://www.baidu.com/s?wd=ip'
	#这里强调一下  正常的request.Request(url=url2,headers=headers)这个是创建请求头
	#之后我传进来一个url 利用opener.open的方法 直接把url传入进去了
	#如果需要构建请求头的话  在加上req=request.Request(url=url2,headers=headers)
	#这里的req 就是一个单一的请求网址
	res=downloader(opener,base_url,proxies)
	#print(res.decode('utf-8'))
		
```



### 3.2 封装好的随机代理直接导入拿来用爬取哈尔滨天气

导入上面写好的文件

```
from urllib import  request
import download
import  parse
base_url="http://datacenter.mep.gov.cn:8099/ths-report/report!list.action"
def getPage():
	for i in range(1,2+1):
		data={
          #这个多次请求i  因为提交的页数在变化
            'page.pageNo' : i,
            'xmlname' : '1462259560614',
            'CITY' : '哈尔滨',
            'V_DATE' : '2018-01-09',
             'E_DATE' : '2018-01-11'
		}
		#对参数进行编码
		data=parse.urlencode(data)
		#构建请求头
		headers={
          'Content-Length':len(data)
		}
		#构建请求
		req=request.Request(url=base_url,data=data,headers=headers)
		#获取代理列表
		proxies=download.getProxy()
		#制定一个opener 用来指定代理处理器handler
		opener=download.getOpener(proxies)
		#下载器
		html=download.downloader(opener=opener,req=req,proxies=proxies)
		html=html.decode('utf-8')
		#\s+匹配多个空格 要' 就\'
		pat=re.compile(r'id="gisDataJson"\s+value=\'(.*?)\'')
		res=pat.search(html)
		if res is not None:
			data=res.group(1)
			data=json.loads(data)
			for item in data:
				print(item)
if __name__=='__main__':
	getPage()

```



##4. requests模块



```
import  requests
base_url="http://www.baidu.com/"
headers={
  'User-Agent' ：'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
#这个传输参数和request原生不一样
#request 是原生的请求库  这个是第三方的
request.get(url=base_url,params={'wp':'ip'},headers=headers)
#获取响应码
print(response.staus_code)
#获取响应头
print(response.headers)
#设置编码
#这里如果响应的html发的utf-8你就要设置你的解码方式，如果人家是gbk231你拿utf-8就会出现乱码!,所以你要拿gbk来进行编码
response.encoding='utf-8'
#返回str类型 响应文本
print(response.text)
#这个是返回bytes类型  
print(response.content)
```



#### 4.1  案例1.66ip爬取

```
import  requests
import  re
base_url="http://www.66ip.cn/"
#用get 来发请求
response=requests.get(base_url)
response.encodeing='gbk'
#返回字符串文本
html=response.text
table_pat=re.compile(r'bordercolor="#6699ff">(.*?)</table>',re.S)

table_res=table_pat.search(html)

if  table_res is not  None:
	td_pat=re.compile(r'<tr>(.*?)</tr>',re.S)
	#找到以tr开始  以tr结束的中间表格
	tr_res=td_pat.findall(table_res.group(1))
	#遍历取出的是每一个td  之后找到中间内容
	for  td  in  tr_res[1:]:
		#再次正则
		td_pat=re.compile(r'<td>(.*?)</td>',re.S)
		#因为每一次遍历 所以 每一次遍历中  正则就找到td中间的内容了
		td_res=td_pat.findall(td)
		host=td_res[0]
		port=td_res[1]
		print(host,port)
```



#### 4.2 美丽说 图片爬取

```
import  requests
import re
import  json
from urllib  import  request
base_url="http://mce.meilishuo.com/jsonp/get/3?callback=jQuery112407478516471173062_1515804778399&offset=0&frame=1&trace=0&limit=10&endId=0&pid=78492&page=%d&_=1515804778407"

page=1
while True:
	response=requests.get(base_url%page)
	html=response.text
	data_pat=re.compile(r'data":(.*?)"returnCode',re.S)
	res=data_pat.search(html)
	if  res is not None:
		data=res.group(1).strip(',')
		#因为是页面上响应的内容(字符串) 所以要给转一下  字典无序性  随机的
		data=json.loads(data)
		#取出列表里的item字典
		for  item in data['list']:
			#在把这个键的值url链接给放到列表
			list.append(item['image'])
		for  url  in list:
			#取出文件名
			fname=url.split('/')[-1]
			#提取图片
			request.urlretrieve(url,'F:/美丽说'+fname)
	#获取下一页
	page=int(data['nextPage])
	
	#如果为假  不走这个if 继续循环 
	#如果为True  循环停止 
	if  data['isEnd']
		break
			

```



#### 4.3 request_post 查询天气

post请求  携带数据    

```
import  requests
#这用到了我封装好的随机代理
import  download
#导入随机数
import  random
base_url="http://datacenter.mep.gov.cn:8099/ths-report/report!list.action"
#用抓包软件抓取提交时候的数据  字典格式
data={
      'CITY':'北京',
    'V_DATE': '2017-12-01',
    'E_DATE': '2018-01-08',
    'page.pageNo': 1,
    'xmlname': '1462259560614'
}
headers={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

#用随机代理发  得到一个代理列表 
proxies=dowload.Proxy()

#随机出来一个
proxy=random.choice(proxies)

#随机代理发请求
response=requests.get(url=base_url,data=data,headers=headers,proxies=proxy)
print(reponse.text)
```





####  4.4 微博登陆

**1.注意： 如果没有cookie  先网页登陆账号密码生成cookie,//也可以程序输入post提交过去的参数来像 post提交的地址发请求**

​	**如果有cookie  则构建请求头 把cookie 给加入进来 请求已登陆的url **



这里演示第二种    我登陆过了已经

```
import requests 
base_url=""https://weibo.com/u/5060408609/home"
#这里注意正则  

headers={
  '    "Host": "weibo.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "我没写，太特么长了"
}

response=response.get(url=base_url,headers=headers)
#查看状态码
print(response.status_code)
print(response.text)
```



这里我用的第一种  没登陆过  

```
import requests
#构建会话  正常原生urllib  里面request 里面是cookiejar 来管理session
#这里用到的是requests.session()

#实例一个对象
session=requests.sessiion()

def login():
	base_url='http://www.renren.com/PLogin.do'
	data={
       'email': '1752570559@qq.com',
        'password': '1234qwer'
	}
	#post提交登陆路径  并且携带数据 之后生成cookie  来用cookie管理器进行管理
	#这里用的是requests.session()
	session.post(url=base_url,data=data)
	
def getHome():
	#登陆 这时候已经有session 了  直接访登陆后的主页
	response=session.get('http://www.renren.com/440906810')
	print(response.text)
if  __name__=='__main__':
	login()
	getHome()
```



## 5. Jsonpath 和 xpath 模块 

网络数据格式两种 xml和json 

我所理解的是 XML其实就是HTML的一种数据存储结构 而html是用来显示的  xml用来存储 如果解析html则需要解析它的数据结构 在这我们用到了xpath 它是一个工具  xpath在xml文档中查找信息的语言，可用来在Xml文档中对元素和属性进行遍历 在用Xpath模块时，需要先将HTML文件，转换成xml文档，然后用xpath来查找HTML结点或元素 这里就基于正则了   

之后python 中导入from lxml import etree  

注释:加载字符串

html=etree.HTML(html)

加载文件 读取文件

html=etree.parse('html','lxml')

构建xpath规则来提取数据

就是xpath的语法了  提取你想要的内容了

解析模块 

​	jsonpath 安装 :pip install jsonpath

​	xpath  安装: pip install lxml

​	用xpath匹配出来的结果一定是列表



### 5.1 xpath

在用Xpath模块时，需要先将HTML文件，转换成xml文档，然后用xpath来查找HTML结点或元素

#### **1. 什么是XML?**

​	XML 指可扩展标记语言(Extensible Markup Language)

​	XML 是一种标记语言，很类似HTML

​	XML 的设计宗旨是传输数据，而非显示数据

​	XML 的标签需要我们自行定义

​	XML 被设计为具有自我描述性

​	XML 仅仅是纯文本 

​		有能力处理纯文本的软件都可以处理 XML

​	XML 是W3C的推荐标准

​	W3School官方文档：http://www.w3school.com.cn/xml/index.asp





#### 2. XML 和HTML 的主要差异

XML 不是 HTML 的替代。

XML 和 HTML 为不同的目的而设计：

XML 被设计为传输和存储数据和描述数据，其焦点是数据的内容。

HTML 被设计用来显示数据，其焦点是数据的外观。

HTML 旨在显示信息，而 XML 旨在传输信息。



#### 3.XML 的节点关系

1.父（Parent):每个元素以及属性都有一个父

2.子（Children) :每个元素节点可能有零个，一个或多个

3.同胞(sibling):拥有相同的父的节点

4.先辈():某节点的父  ，父的父

5.后代(Descendant):某个节点的子，子的子，等等



#### 4.什么是Xpath?

Xpath(xml path Language) 是一门在xml文档中查找信息的语言，可用来在Xml

文档中对元素和属性进行遍历

w3school官方文档:http://www.w3school.com.cn/xpath/index.asp



Xpath开发工具

也就是说在浏览器上安装这个插件  可以对网页源代码 通过xpath 提取你想要的数据

1.开源的Xpath表示编辑工具XMLaquire(XML)格式文件可用

2.Chrom 插件 xpath  Helper

3.Firefox 插件 xpath Checker



##### 4.1 xpath语法 ！

选取节点:

Xpath使用路径表达式来选取xml文档中的节点或者节点集，这些路径表达式和我们在常规的电脑文件系统中看到的表达式都非常相似

下面列出了最常用的路径表达式

```
表达式     	描述 
Nodename	 选取此节点的所有子节点
/             从根节点选取
//  		从匹配选择的当前节点选择文档中的节点,而不考虑他们的位置

.			选取当前节点
..			选取当前节点的父节点
@			选取属性

eg: 
<? xml version="1.0" encoding="utf-8"?>
<bookstore>
<book>
	<title> Harry potter </title>
	<author> k.Rowling </author>
	<year> 2005</year>
	<price> 29.99</price>
	</book> 
</bookstore>


bookstore  选取bookstore 元素的所有子节点
/bookstore 选取根元素bookstore #假如路径起始于正斜杠
		  则此路径始终代表到某元素的绝对路径

/bookstore/book 选取属于bookstore的子元素的所有book元素
//book     选取所有book子元素，而不管它们在文档中中的位置
bookstore//book 选取属于bookstore元素的后代所有book元素,而不管它们位于bookstore下的什么位置
//@long  选取名为long的所有属性



```



```
谓语（predicates)  在xpath中 索引是从1开始的
//谓语用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中


路径表达式          		结果
/bookstore/book[1]      选取属于bookstore子元素的第一个book元素
/bookstore/book[last()]  选取属于bookstore子元素的最后一个book元素
/bookstore/book[last()-1] 选取属于bookstore子元素的倒数第二个book元素
/bookstore/book[positon()<3] 选取最前面的两个属于bookstore元素的子元素的book元素
//title[@lang]   选取所有拥有名为lang的属性的title元素
//title[@lang='eng'] 选取所有title元素,且这些元素拥有值为eng的lang属性
/bookstore/book[price>35.00] 选取bookstore元素的所有book元素且其中的price 元素的值须大于35.00
/bookstore/book[price>35.00]/title  选取bookstore元素中的book元素的所有title元素,且其中的price元素的值须大于35.00




```

选取未知节点

```
xpath通配符可用来选取未知的xml元素

通配符			描述
*			  匹配任何元素节点
@			  匹配任意属性节点
node() 		   匹配任何类型的节点

路径表达式
/bookstore/*       选取bookstore元素的所有子元素
//*   			  选取文档中所有元素
//title[@*]  	选取所有带有属性的title元素


选取若干路径
通过在路径中使用"|"可以选取若干个路径

路径表达式
//book/title | //book/price  选取book元素的所有title和price元素
//title  |  //price     选取文档中的所有title和price元素
//bookstore/book/title | //price  选取属于bookstore元素的book元素的所有title元素 ，以及文档中的所有price元素
```

 以上这些就是 xpath的语法内容，在运用到python抓取时要先转换为xml



#### 5.  lxml库 在python中用xpath

 	lxml是一个HTML/XML的解析器，主要的功能是如何解析和提取/HTML/XMl中的数据

​	lxml和正则一样，也是用（实现的, 是一款高性能的Python HTML/XML的解析器  我们可以利用之前学习的xpath语法，来快速的定位特定元素以及节点信息

​	lxml python 官方文档：http://lxml.de/index.html

​	需要安装c语言库，可使用pip安装:pip install lxml或者通过 wheel 方式安装 初步使用

​	我们利用它来解析HTML代码		

```
#使用lxml的etree库
from lxml  import  etree

text='''
	<div>
		<ul>
			<li>...</li>
			<li>...</li>
		</ul>
	</div>
	'''
	
#利用etree.HTML ,将字符串解析为HTML文档  
html=etree.HTML(text)

#按字符串序列化HTML文档
#也就是把html给转成了bytes格式
result=etree.tostring(html)

#lxml可以自动修正html代码 ，可不全缺失的标签  还会添加body,html标签


```

​	

```
文件读取
	除了直接读取字符串,lxml还支持从文件里读取内容

<!--hello.html-->
<div>
</div>
利用etree.parse()方法来读取文件
#读取外部文件 hello.html
 html=etree.parse('./hello.html')
 #这个参数是让它好看的输出格式化html
 result=etree.tostring(html,pretty_print=True)
 
 #将字符串解析成html文档
 etree.HTML(html)

 #将html文档,序列化成字符串
 etree.tostring(html,pretty_print=True)

```



代码如下 

```
1.获取所有的<li>标签
from lxml import  etree
html=etree.HTML(html)
html=etree.parse('hello.html) #type:'html.etree.ElementTree'
result=html.Xpath('//li') #type: list列表其中值的类型为Element

2.继续获取<li>标签的所有class 属性
result=html.xpath('//li/@class'）其结果是li class属性的一个列表

3.继续获取<li>标签下href为link1.html的<a>标签
result=html.xpath('//li/a[@href="link1.html"])

4.获取<li>标签下的所有<span>标签
#因为'/'是用来获取子元素的
错误写法:result=html.xpath('//li/span')
result=html.xpath('//li//span')

5.获取<li>标签下的<a>标签里的所有class 
result=html.xpath('//li/a//@class')['blod']

6.获取最后一个<li>的<a>的href
result=html.xpath('//li[last()]/a/@href')

7.获取倒数第二个元素的内容
result=html.xpath('//li[last()-1]/a')
#text方法可以获取元素的内容
print(result[0].text)

8.获取class值为bold的标签名
result=html.xpath('//*[@class='bold'])
#tag方法可以获取标签名
print(result[0].tag)



```

**58房源案例**

```
etree模块可以用xpath方法提取网页数据
from  lxml  import  etree
import   requests
from  urllib  import   request
import   json 

def get_maxpage(f)：
	#访问第一页先
	base_url="http://bj.58.com/chuzu/pn1"
	#发起请求
	response=requests.get(url=baseurl)
	#得到响应文本
	html=response.text
	#提取内容
	#xpath方法提取网页数据  得到html对象
	html=etree.HTML(html)
	#获得最大页数
	maxx_page=html.xpath('//div[@class="pager"]/a[last()-1]/span/text()')[0]
	调用每一页 
	get_urls(max_page,f)
	
def get_urls(max_page,f):
	max_page=int(max_page)
	#对每页进行操作
	for i in  range(1,max_page+1):
		print('这是第{name}页).format(name= i)
		base_url='http://bj.58.com/chuzu/pn{}'.fromat(str(i))
		response=requests.get(url=base_url)
		html=response.text
		#xpath方法提取网页数据  得到html对象
		html=etree.HTML(html)
		#提取详情链接
		url=html.xpath('//ul[@class="listUl"]/li//h2/a/@href')
		#调用详情页操作
		get_details(url,f)
	
	
	
def get_details(urls,f):
	try:
		#对每个详情链接请求
		for  base_url in  urls :
			response=requests.get(url=base_url)
			html=response.text
			#如果响应码不在这个范围  证明失败
			if  response.status_code not  in  range(200,300):
				print('被拒绝了!!sb58')
				#跳过 继续下一个url
				continue
			#在则提取
			html= etree.HTML(html)
			price=html.xpath('//span[@class="c_ff552e"]/b/text()')
			pay_method=html.xpath('//span[@class="c_333"]/text()')
			title=html.xpath('//h1/text()')
			margin_type=html.xpath('//ul[@class="f14"]/li[1]/span[2]/text()')
			house_type=html.xpath('//ul[@class="f14"]/li[2]/span[2]/text()')
			area=html.xpath('//ul[@class="f14"]/li[5]/span/text()')
			addr=html.xpath('//ul[@class="f14"]/li[6]/span[2]/text()')
			phone=html.xpath('//span[@class="house-chat-txt"]/text()')
			pic=html.xpath('//img[@id="smainPic"]/@src')
			
		   #如果 这些数据 都有那么我对这些数据进行取片写入操作
            #否则  我直接跳过
              if price and pay_method and  title and house_type and direction and host and area and addr and phone and pic:
			
                price = price[0]
                pay_method = pay_method[0]
                title = title[0]
                margin_type = margin_type[0]
                house_type = house_type[0]
                direction = direction[0]
                host = host[0]
                area = ''.join(area)
                addr = addr[0]
                phone = phone[0]
                pic = pic[0]
                pic_name=pic.split('/')[-1]
                request.urlretrieve(pic,'./house/{name}.jpg'.format(name=pic_name))
                #给这些数据做成字典 键自己定义 ,值是我刚才弄好的值
                house={
                  'title':title,
                  'price':price,
                  'pay_method':pay_method,
                  'house_type':house_type,
                  'direction':dirction,
                  'host':host,
                  'area':area,
                  'addr':addr,
                  'phone':phone,
                  'pic_name':pic_name,
                }
                #遍历的是键
                for  key in house:
                	#对数据进行处理house[key]=house[key].replace('\xa0','').strip()
                	#得到house字典  给转成json格式  这个参数是防止写入的时候是ASCI码，因为默认序列化的时候是用ascii来编码的
                data=json.dumps(house,ensure_ascii=False)
                #把数据写入
                f.write(data+'\n')
                
          	 else:
             	continue
      except  Exception  as e :
        print(e)
        #只要一运行到它就结束
        # exit()
        
        
if  __name__=="__main__":
	f=open('58house.json','w')
	get_maxpage(f)
	
          	
                	
				
```



### 5.2 jsonpath

Jsonpath 和Xpath 语法比较

```
Xpath   		Jsonpath  	 		描述
/				$					根节点
.				@ 					现行节点
/ 				.or[]				取子节点
..				n/a					取父节点,jsonpath未支持
//				..					就是不管位置，选择所有符合条件的条件
*				* 					匹配所有元素节点

@				n/a 				根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要

[]				[]					迭代器标示(可以在里面做简单的迭代操作，如数组下标，根据内容选值等)

|				[,]					支持迭代器中做多选

[]				?()					支持过滤操作

n/a 			()					支持表达式计算

()				n/a 				分组。JsonPath不支持

```

```
eg: 我们以拉钩网城市json文件为
http://www.lagou.com/lbs/getAllCitySerchlables.json为例 获取所有城市

import  urllib2
import jsonpath
import  json
import  chardet

url='https://www.lagou.com/lbs/getAllCitySearchLabels.json'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
html=response.read()
#把json格式字符串转换成python 对象
jsonobj=json.loads(html)
#从根节点开始,匹配name节点
citylist=jsonpath.jsonpath(jsonobj,'$..name')

fp=open('city.json','w')
#转成json格式写入 默认使用ascii 进行编码
content=json.dumps(citylist,ensure_ascii=False)
fp.write(content.encode('utf-8'))
fp.close()

```

**老师jsonpath演示代码如下**

```
#jsonpath 把json 数据进行提取
import  jsonpath

import   json 
s = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-4.笔记还没做.笔记还没做",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95,
      "author": "J. R. R. Tolkien"
    }
  }
}
'''

#$以.store为根  跟下的所有book  再往下的作者全部都找出来
res=jsonpath.jsonpath(json.loads(s),'$.store.book[*].author)
print(res)

#..和. 
#..前者是只要满足条件我就都要，把满足的当成一个给我拿回来 比如俩store 他们后面都有内容 都给我完整的拿出来
res=jsonpath.jsonpath(json.loads(s),'$..store')
print(res)

#.后者只拿子节点
res=jsonpath.jsonpath(json.loads(s),'$.store')
print(res)

#直接查找store下的 bicycle 下的author 
res=jsonpath.jsonpath(json.loads(s),'$.store.bicycle.author')
print(res)

#把它当作跟    层级取找  
res=jsonpath.jsonpath(json.loads(s),'$..store..bicycle..author)

#..*找所有
res=jsonpath.jsonpath(json.loads(s),'$..*")

```



#### json 模块import  json

json 模块提供了四个功能:dumps dump  loads load 用于**字符串**和**python 数据类型**间进行**转换**

**1.json.loads()**

把json格式字符串解码转换成Python对象，从json到Python的类型转换

```
import json 
#接收到的响应json格式字符串
strlist='[1,2,3,4]'  

strdict='{'city':'北京','name':'大猫'}'

json.loads(strlist) #[1,2,3,4]

json.loads(strdict)#json数据自动按unicode存储 
#{u'city':u'|u5317|u4eac',...}


```



**2.json.dumps()**

实现python类型转化为json字符串 ，返回一个str对象，把一个python对象编码转换成json字符串



```
import json 
liststr=[1,2,3,4]
tuple=(1,2,3,4)
dictstr={"city":"北京","name","大猫"}
json.dumps(liststr)#'[1,2,3,4]'
json.dumps(tuplestr)#'[1,2,3,4]'

注意  json.dumps()序列化时默认使用的ascii编码

#添加参数  ensure_ascii=False,禁用ascii编码，按utf-8编码

#chardet是一个非常优秀的编码识别模块，可以用pipinstall来安装
#chardet.detect()返回字典，其中confidence是检测精确度

#你给转成json 也是按照unicode 来编码的存储的
"{\"city\":\"\u5317\u4eac\",\"name\":\"\u732b\"}"
res=json.dumps(dictstr)

#检测精度  输出结果{'confidence': 1.0, 'encoding': 'ascii', 'language': ''}

a=chardet.detect(res.encode())

```



**3.json.dump()**

将python 内置类型序列化为json对象写入文件

```
import json
liststr=[{"city":"北京"},{"name":"大刘"}]
dictstr={"city":"北京"},{"name":"大刘"}
#这个还有一个打开文件的参数
json.dump(liststr,open("liststr.json","w"),ensure_ascii=False)

dictstr={"city:":"北京"}
json.dump(dictstr,open("liststr.json","w"),ensure_ascii=False)
```



**4.json.load()**

读文件中json格式为字符串元素，转成python类型

```
strlist=json.load(open("liststr.json"))
print(strlist)
#输出结果是这样的
#"{\"city\":\"\u5317\u4eac\",\"name\":\"\u732b\"}"
```



**补充**

1.自定义了一个简单的数据（python的字典,要想python的字典被序列化(写入/暂时理解)到json文件中请使用双引号！双引号！双引号！

data.obj={

"北京市":{

"朝阳区":["三里屯":"望京","国贸"]，

"朝阳区":["三里屯":"望京","国贸"]，

"朝阳区":["三里屯":"望京","国贸"]，

}，

"北京市":{

"朝阳区":["三里屯":"望京","国贸"]，

"朝阳区":["三里屯":"望京","国贸"]，

"朝阳区":["三里屯":"望京","国贸"]，

}

}

2. dumps:序列化一个对象

   sort-keys:根据key排序

   indent:以4个空格缩进，输出阅读

   ensure_ascii:可以序列化默认用ascii码编码 ascii编不了中文，所以改false	s_dumps=json.dumps(data_obj,sort_key=True,indext=4,ensure_ascii=False)

   print(s_dumps)

3. dump  将一个对象序列存入文件

   dump()的第一个参数是要序列化的对象，第二个参数是打开json文件的操作







### 5.3 Beautfulsoup4 

安装: pip   install  Beautifulsoup4

Beautifulsoup也是对html  进行数据提取的一种方法   它基于正则表达式

Beautifulsoup4(美丽的汤) 简称bs4,特点支持css选择器

BeautIfulSoup  官方文档 

http://www.crummy.com/software/BeautifulSoup/bs4/doc/

使用难度

1.re

2.xpath   bs4



```
from  bs4 import   BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="p1"><b>The Dormouse's story</b><b>----2b</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><b>Elsie</b></span></span>--alice</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<div>我是div</div>
"""

#前提是安装了lxml以后，目的是指定解析    否则报错
#输出格式化后的文档， 它会帮你加上html的标签补齐
print(html.prettify())

#获取标签   包括了标签以及标签内容
print(html.title)#<title>The Dormouse's story</title>

#标签名称
print(html.title.name)#title

#只获取标签中的内容
print(html.title.string)#The Dormouse's story

#获取p标签里的b标签中的内容，如果有两个b标签  那么只默认选取第一个
print(html.p.b.string)

#获取单个属性  也就是标签里的属性     结果是属性值   也只获得第一个
print(*html.p['id'])#p1

#获取所有属性，返回字典  获取p标签里面的所有属性  但是只返回第一个p标签中的
print(html.p.attrs)#{'id': 'p1', 'class': ['title']}

#获取指定标签下所有文本，不管它里面还有没有标签了  都把文本取出来
print(html.p.get_text())#The Dormouse's story----2b

#通过属性来查找标签   返回id="link3"的标签
print(html.find(id="link3"))#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#返回列表  找到所有的p标签
p_list=html.find_all('p')
for  p in  p_list:
	#获得所有的标签中的文本  调用bs4的方法
	print(p.get_text())

#用find_all进行筛选
#对所有p标签进行筛选   把class属性是title的 和id 属性是p1的p标签给拿出来.
#并且如果有嵌套也给取了出来
#这里注意的是属性要是字典形式
#返回值列表
print(html.find_all('p',attrs={'class':'title','id':'p1'}))#[<p class="title" id="p1"><b>The Dormouse's story</b><b>----2b</b></p>]

#找到你想要的所有标签   这里需要传入一个列表，返回值也是个列表
res=html.find_all(['p','div'])

#找到所有的a标签
res=html.find_all('a')
for  a in  res :
	#不支持嵌套 如果你a标签里面有两个span 标签  那么则返回none
	print(a.string)
	#这个则找到标签里的所有文本
	print(a.get_text())
	
```



**css选择器的用法**

```
from  bs4 import  BeautifulSoup
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="p1">
  <b class="b1">The Dormouse's story</b><b>----2b</b>
    <span>
        <b class="b1">The Dormouse's story</b><b>----2b</b>
    </span>
</p>

<p class="story1">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><b>Elsie</b></span></span>--alice</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="storky2s">...</p>
<div>我是div</div>

"""

#css选择器的用法 
html=BeautifulSoup(html,'lxml')
#找出来第一个p标签并包括里面的其他标签
print(html.select('p.title'))

#p下的子孙节点查找  并且都给找到  返回列表
print(html.select('p .b1'))

#p下的子孙节点查找 并且都给找到 返回列表
print(html.seleet('p > .b1'))


#这么写的话则是找到p标签下的  所有b标签 别忘记写空格   找到所有p标签下的b标签
print(html.select('p b'))

#id 选择
#通过id属性找到标签   id为p1的p标签   这里没空格! 写空格找不到!
print(html.select('p#p1'))

#或者的关系   两个都给你拿出来   看你要哪个
#找到p标签class="story1"的 标签
print(html.select('p.story1,p.story2'))

#根据属性筛选
#这个根xpath 不一样  在属性之前没有@符号
#找到p标签class="story1"的 标签  并且把里面的标签页都拿了出来  返回列表
print(html.select('p[class="story1"]'))

#选出类以s开头的所有p标签  里面的标签也都有 返回列表
print(html.select('p[class^="s"]'))

#选出以s结尾的所有p标签  里面的标签也都有 返回列表
print(html.select(['p[class$="s"]'))

#模糊查询   选出里面有kd的类的所有p标签   里面的标签也都有   返回列表
print(html.select('p[class*="k"]'))

```



#### 5.3.1 交友案例

​	



#### 5.3.2 兄弟连学员项目

```
import   requests 
from  bs4  import   BeautifulSoup
import  json 
#获取a  链接 
def  getPage():
	base_url="http://www.itxdl.cn/html/php/phparticles/"
	response=requests.get(url=base_url)
	response.encoding="utf-8"
	#得到首页
	html=response.text
	html=BeautifulSoup(html,'lxml')
	#得到a链接
	a_list=html.select('div.php_zuopin_fenlei a')
	#php java  python h5 啊分类的链接
	for  a in a_list:
		a=a.get('href')
		get_detail(a)
		
	#对每一页进行数据抓取
def get_detail(url)
	response=requests.get(url=url)
	response.encoding=“utf-8"
	html=response.text
	html=BeautifulSoup(html,'lxml')
	all_project=html.select('div.php_xueyuanzuopin_liebiao')
	#遍历 得到每个人的项目  提取的标签了
	for   every  in  all_project:
		 project_name=every.select('div.php_xueyuanzuopin_liebiao_left p')[0].text.replace('项目名称：','')
        class_name=every.select('div.php_xueyuanzuopin_liebiao_left p')[1].text.replace('\xa0','')
        group_name=every.select('div.php_xueyuanzuopin_liebiao_left p')[2].text.replace('小组名称：','')
        project_introduce=every.select('div.php_xueyuanzuopin_liebiao_left p')[3].text.replace('项目简介：','')
        project_pic=every.select('div.php_xueyuanzuopin_liebiao_right img')[0].get('src')
         data={
            'project_name':project_name,
            'class_name':class_name,
            'group_name':group_name,
            'project_introduce':project_introduce,
            'project_pic':project_pic,
        }
        json_data.append(data)
        
 if__name__=='__main__':
 	json_data=[]
 	getPage()
 	#调用完之后给转成了json格式
 	final_data=json.dumps(jsondata,indent=4,ensure_ascii=False)
 	#写入文件操作
 	with open('xdl_project.json','w',encoding='utf-8')as f:
 		f.write(final_data)
 		
 	#######到这结束了 这里注意 打开文件写在for循环外面 #####
 	with open('1.txt','w',encoding='utf-8')as f:
    for  i  in range(0,1000):
        f.write('1111'+'\n')
		
```



## 6. 爬取腾讯招聘信息并链接数据库



```
#爬取腾讯招聘信息
import  requests 

#导入美丽的汤来对html进行解析
from  bs4 import  BeautifulSoup

#导入封装好的插入数据库的类
from  Mydb import  Mydb

#引入系统时间魔魁
import  datetime 

#导入正则表达式
import  re

#参数 第一页是0 每一页参数增加10
base_url='http://hr.tencent.com/position.php?start=%d'

#构建请求头
headers={
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def getPage():
	#获取每一页
	for i  in  range(0,2920+1,10):
		fullurl=base_url%i
		#发送请求
		response=requests.get(fullurl,headers=headers)
		#得到响应文本
		html=response.text
		#实例一个html对象来提取内容
		html=BeautifulSoup(html,'lxml')
		#找到table标签的class="tablelist"属性  之后打个空格 层级选择  来选择下面tr 返回列表形式
		tr_list=html.select('table.tablelist tr')[1:-1]
		for tr  in  tr_list:
		#找到其中的a链接  因它在td下面  td > a 固定用法  找到a链接  这里别忘记加空格 
		#取出a链接  得到所有的a链接
			detail_lin=tr.select('td > a')[0].get('href')
			#但是这里因为取出来的是a链接 如果进行访问   所以加上Tencent的域名  来字符串拼接
			detail_link='http://hr.tencent.com/'+detail_link
			#发起详情页请求  调用请求和抓取数据的函数
			parse_detail(detail_link)
#处理详情页	
def parse_detail(url):
	#我先发起请求
	response=requests.get(url,header=headers)
	#简写如下
	html=BeautifulSoup(response.text,'lxml')
	
    #职位标题
    #找到属性为class="h" 的tr标签 并且里面的td也被取出来了
    #返回的是列表对其进行取片[0]
    #并把内容取出来  这里用到的是text方法
    #strip方法 默认切除字符串前后的空格
	posithon_name=html.select('tr[class="h"]')[0].text.strip()
	
	# 反回列表 索引从0开始
    #找到table下面的class="tablelist"  下的tr  因为这些信息都在tr里,返回tr里面的所有内容
	info=html.select('table.tablelist tr')
	
	
    # 工作地点
    #找到第二个tr  下面的第一个td 因为索引是从0开始的 第二个是因为第一个什么职位名称 我不要
    #contents是td下表面的标签 让它按列表返回 输出结果 [<span class="lightblue l2">工作地点：</span>, '深圳']
    #[-1] 把其中的内容取出 也就是地点
	location=info[1].select('td')[0].contents[-1]
	
	#工作类型 第一个tr里面的第二个td
	p_type=info[1].select('td')[1].contents[-1]
	#招聘人数 因为要存入数据库数字  这里把人给去除
	p_number=info[1].select('td')[2].contents[-1].strip('人')
	#工作职责
    #info[2] 第三个tr 下面的li 得到一个列表
	duty_list=info[2].select('li')
	#遍历li  列表倒推式遍历li  并且把li里面的文本取出来 之后进行字符串拼接
    #给弄成字符串形式
    duty_list=[duty.text for duty  in  duty_list]
    #将列表转成了字符串
    duty=''.join(duty_list)
    
    #工作要求
	requirement=info[3].select('li')
	requirement=[reque.text for reque in  requirement]
	requerement=''.join(requirement)
	#系统时间
	crow_time=datetime.datetime.now().striftime('%Y-%m-%d %H:%M:%S')
	
	 #保存数据
	'''
	1.写到这就链接mysql  具体看Mydb.py
	'''
	'''
	1.存入数据库去重问题
	2.请求过的网站  就不请求了 
	3.在数据库里加一个字段  添加唯一索引  unique  betree 是索引的一种算法
	'''
	
	#通过url上面给找到id
    #这个response.url这个方法能找到所请求的url地址
	re_pat=re.compile(r'id=(\d+)')
	url=response.url
	res=re_pat.search(url)
	#每个url都不一样 你只能去找id  否则匹配不到
	url_id=res.group(1)
	
	#导入封装好的 插入数据的类
    #写  sql 语句
	sql= insert into values(position_name,location,p_type,p_number,duty,requirement,url_id,crow_time)values(%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update position_name valies(position_name)'#插入更新语句  如果已经存在 我更新
	data=[position_name,location,p_type,p_number,duty,requerement,url_id,crow_time]
	
	#用导入类里面方法  需要先实力还一个对象  之后来调用这个方法
	mydb.excute(sql,data)
	
	
if __name__=='__main__':
	#导入进来必须要先实例化对象
	mydb=Mydb()
	getPage()
```



Mydb.py

```
import  pymysql
#导入系统时间模块
import  datetime 
'''
1.打开Navicat  链接数据库
2.之后新建表
	建立字段 尽量保持根变量名一样
	id  逐渐自增 无符号  不允许为空
	剩下的看情况   来设置varchar长度
3. 封装往数据库插入数据的函数
4.之后测试
'''
class Mydb():
	def __init__(self)：
		try:
			#链接mysql 主机ip  root 密码 数据库名 字符集
			self.conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf-8')
			self.cursor=self.conn.cursor()
		except Exception  as e :
			print(e)
	def excute(self,sql,data):
		try:
			res=self.cursor.excecute(sql,data)
			self.conn.commit()
		except Exception as  e:
			self.conn.rollback()
			print(e)
if  __name__=='__main__':
	mydb=Mydb()
	#测试一下
	#这个是系统时间的datatime 模块  它下面的datetime.now()方法  来获取插入的时间 striftime  是日期时间格式
	crow_time=datetime.datetime.now().striftime('%Y-%m-%d %H:%M:%S')
	#写好sql语句  insert into 表名(字段) values (值) 对应写好
	sql='insert into py05_position(positon_name,location,p_type,p_number,duty,requirement,duty,requirement,crow_time) values  (%s,%s,%s,%s,%s,%s,%s) '
	#测试data数据
	data=['python全能全知道','anywhere','全职爷',0,'共组职责','都需要',crow_time]
	#调用这个类的插入方法  把sql 语句 和数据传入进去
	mydb.execute(sql,data)
	
```





## 7. 进程和线程

1.请求

​	突破反爬虫

2.解析

​	html json image

3.存储

​	文件 数据库 redis

4.效率问题

​	同时发请求   

​		利用多进程 多线程

​		**老师举的例子:1线程告诉cpu发http请求**

​					**2线程告诉cpu发http请求**

​					**1线程响应继续工作**

​					**2线程响应继续工作**

**进程:**

​	**描述**:进程就是一段执行的程序，每当一个程序执行时。对于操作系统本身来说，就创建了一个进程，而且分配了相应的资源。       一段程序或者脚本的执行。cpu资源分配的最小单位       进程就好比工厂的车间，它代表CPU所能处理的单个任务。任一时刻，CPU总是运行一个进程，其他进程处于非运行状态。

​	**优点:**    提高效率，利用cpu多核优势

​	**进程开启个数:**    理论上是cpu内核的1-2倍

​	**缺点:**    资源消耗非常大，进程过多，cpu切换进程执行也消耗资源，资源共享困难

​	**使用场景:**    cpu密集型应用程序(计算密集型) 如while  循环 for 循环

**线程:**

​	**优点:**提高效率

​	**开启个数:**跟计算硬件有关系,跟应用场景有关系,一般高于可开启进程数

​	**描述**:进程下可以开启多个线程,cpu调度的最小单位

​	**缺点**:开启个数也不是无限的,如果开启过多，造成进程瘫痪

​	**使用场景**:IO(input(response),output(request),)密集型应用程序，爬虫程序是网络IO,长延时操作



### 7.1进程

#### 案例1

```
#导入多进程模块
import  multiprocessing
#定义进程函数
def foo():
	print('hello 进程')

#在windows下如果创建多进程则需要在以下条件成立
if __name__=='__main__':
	#创建一个进程，则需要先定义一个函数
	#target:构建函数对象  也就是说你要处理/运行的函数写到这 来提高效率
	#args:进程函数的参数
	p=multiprocessing.Process(target=foo)
	#启动进程
	p.start()
```



#### 案例2

```
#导入进程模块
import  multiprocessing
import  time 
def foo(num):
	print(time.sleep(3))
	print('hello %d号进程'%num)
	
if __name__=='__main__':
	#循环创建10个进程/多进程
	#启动就用上了  最后都启动了  就速度快起来了  1个人干活，2个人干活。。类推
	#之后 相当于很多人一起干活了
	for  i in range(10):
		#target:进程函数对象 也就是这个进程所处理的函数   对这个函数进行实例化
		#args:是进程处理的函数  这个函数所需要的参数
		p=multiprocessing.Process(target=foo,arg=（i，)
```



#### 案例3 多进程共享数据 

```
#导入多进程模块
import  multiprocessing 
#初始化一个manager对象 为了共享数据
from  multiprocessing  import  Manager

#定义进程函数
def foo(num,ls):
	#把共享数据加入到列表中
	ls.append(num)
	print('hello %d号进程'% num)
	
if __name__=="__main__":
	#创建一个进程：则需要先定义一个函数
	#target:进程函数对象
	#args:进程函数的参数
	m=Manager()#初始化一个manager对象
	ls=m.list()
	#列表的作用是让它阻塞 等运行完进程在执行主进程代码
	process_list=[]
	
	#先创建了10个进程
	#之后这10个进程随机调用这个函数
	#i 是给进程函数传递过去的数据
	for  i  in  range(10):
		p=multiprocessing.Process(target=foo,args=(i,ls))
		#启动一个进程
		p=start()
		#创建一个进程就加入到进程列表中
		process_list.append(p)#进程执行中会阻塞主进程
		
	for p in  process_list:
		#阻塞主进程
		p.join()
		
	print('进程执行完毕,执行我')
	print(ls)
	
```



#### 案例4 进程池

```
import  time
#进程池
from multiprocessing  import Pool
def foo(num):
	print(num)
if __name__=='__main__':
	#创建一个进程池
	#可以同时跑16个进程  也是最大开启进程数了 在这设置
	#循环到100正常是1个个去打印 才完成
	#加了一个16进程的进程池 他们同时去工作  其中哪一个进程处理完了自动接下一个  直到全部完事
	for  i in range(10):
		#创建一个进程
		#用进程处理的函数  foo对象，i是传递过去的函数的参数
		#注意 这里一定要加逗号 传递过去的是一个元祖
		pool.apply_async(func=foo,arg=(i,))
	#进程池中所有进程执行完毕，继续执行
	#关闭进程池，不再接受新的进程
	pool.close()
	#join()方法表示等待进程结束后继续往下运行，通常用于进程间的同步
	pool.join()
	print('执行完毕')
	
```



#### **案例5  腾讯招聘 进程来跑**

```
import  time 
import  requests
from  bs4  import  BeautifulSoup
#从多进程模块中导入进程池
from multiprocessing  import Pool

base_url='http://hr.tencent.com/position.php?start=%d'
headers={
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}
#接收传递的参数
def getPage():
	fullurl=base_url%i
	response=requests.get(url=fullurl,headers=headers)
	html=response.text
	#获取详情页链接地址
	html=BeautifulSoup(html,'lxml')
	#这里根css选择器获取内容很想  先标签名.它的类名  空格层级关系找到tr
	tr_list=html.select('table.tablelist tr')[1:-1]
	for  tr in  tr_list:
		name=tr.select('td a')[0].text
		
if __name__=='__main__':
	pool=Pool(4)
	#请求2页 因为人家网站的参数是0是第一页  10是第二页
	#获取时间戳
	print(time.time())
	for  i  in range(0,10+1,10)：
		#进程池中的func参数表用多少个进程来处理这个函数
		#这里表示用4个进程同时来去请求
		#args参数是我给它传递过去的参数i
		pool.apply_async(func=getPage,args=(i,))
	pool.close()
	pool.join()
	print(time.ctime())
	
```



### 7.2 线程

#### 案例1

```
#导入线程模块
import  threading
import  time
#线程函数
def foo(num):
	print(num)
#线程
t1=threading.Thread(target=foo,args=(1,))
t2=threading.Thread(target=foo,args=(2,))

```



#### 案例2

```
import  threading
import  time
def foo(i):
	print('%d号线程启动'%i)
	print('%d号线程结束'%i)
	
thread_list=[]
for  i  in range(1,10+1)：
	#创建线程
	t=threading.Thread(target=foo,args=(i,))
	#启动线程   线程因为循环越来越多  干活越来越快  谁干完了就接活 密集行应用程序
	t.start()
	#看线程是否存活  执行中 干活呢就是存活呢  没干活就是没存活
	print(t.is_alive())
	thread_list.append(t)
#等待所有线程完毕 在执行下面的代码 
#同步 阻塞 
for  t in  thread_list:
	t.join()
#检测是否存活
for  t  in thread_list:
	print(t.isalive)
```



#### 案例3 自定义线程

```
import  threading
#自定义我的线程
#继承它爸爸
class MyThread(threading.Thread):
	def __init__(self):
	#找到MyThread的父类然后调用init方法
	#底层源码里面已经写好了这个run了
	def run(self):
		print('启动线程')
if __name__=='__main__':
	t=MyThread()
	y.start()
```



#### 案例4 腾讯招聘  线程来跑

```
import  threading
import requests
from bs4 import  BeautifulSoup 
import  time 
class Crawl(threading.Thread)：
	base_url='http://hr.tencent.com/position.php?start=%d'
	headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    
    def  __init__(self,i):
    	'''
    	 这是对继承自父类的属性进行初始化，而且是用的父类的初始化方法来初始化继承的属性
        也就是说，子类继承了父类的所有属性和方法，父类属性自然会用父类的方法来进行初始化。
        当然，如果初始化的逻辑与父类的不同，不使用父类的方法，自己重新初始化也是可以的
      	'''
      	#这里用到了父类的初始化方法   父类的初始化方法中调通了写好的run启动线程的方法
      	super(Crawl,self).__init__()
      	#初始化一个属性i  接收传入进来的参数
      	self.i=i
      #启动线程
     def run(self):
     	#利用线程来处理函数
     	#参数屌用了初始化的参数self.i 
     	self.getPage(self.i)
     	
     def getPage(self,i)：
     	full_url=self.base_url%i
     	#这里的参数一定要指明  因为底层get源代码是形参是收集关键字形参
     	response=requests.get(url=full_url,headers=self.headers)
     	html=response.text
     	#获取详情页链接地址
     	html=BeautifulSoup(html,'lxml')
     	#获取数据操作
     	tr_list=html.select('table.tablelist tr')[1:-1]
     	for  tr  in tr_list:
     		name=tr.select('td a')[0].text
     		print(name)
     		
 if  __name__=='__mian__':
 	print(time.ctime())
 	thread_list=[]
 	for  i  in range(0,100):
 		#生成线程
 		c=Crawl(i)
 		#启动线程
		c.start()
		#把生成的线程给放到列表中
		thread_list.append(c)
		
	for  i  thead_list:
	#遍历每个线程  等线程结束 执行底下的代码
		i.join()
	print(time.ctime())
		
```



#### 案例5 糗事抓取 为线程做铺垫

```
#糗事百科  网页抓取
import  requests
from lxml import etree
base_url='https://www.qiushibaike.com/8hr/page/%d/'

def getPage():
	#遍历每一页
	for page in range(1,13):
	#拼凑url 
	fullurl = baseurl% page
	response = requests.get(url=fullurl)
	html=response.text
	#解析html文本
	html = etree.HTML(html)
	#获取段子div  /div是紧div[@id="content-left"]下面
	#如果是//div子孙节点找  如果是/div 是子节点里找 只在它儿子中找！
	duanzi_div = html.xpath('//div[@id="content-left"]/div')
	
	#循环所有段子  也就是遍历每一个段子 
	for  duanzi  in  duanzi_div:
		#.//从找到的节点下继续在子孙节点中查找
		nick = duanzi.xpath('.//h2/text()')[0]
		#管道府  都找 满足条件的话
		age = duanzi.xpath('.//div[@class="articleGender manIcon"]/text() | .//div[@class="articleGender womenIcon"]/text()[0]')
		if  age :
			#取片操作
			age=age[0]
		else :
		#没有的话  那么我给它个0 放到数据库 我好知道咋回事！
			age=0
			
		#通过标签的类名 我们利用xpath来取出它的类名  来看看它是男是女  之后我们做判断
		#这里不能取片  因为里面有的没有
		gender_cls = duanzi.xpath('.//div[@class="articleGender manIcon"]/@class |.//div[@class="articleGender womenIcon"]/@class')
		
		#如果里面有  那么我来看看它的性别
		if  gender_cls :
			#有的同时  看看如果man字符串在这个标签的属性值里面
			if  'man' in gender_cls[0]:
				#那么给它存个男
				gender='男'
			#如果women 字符串在这个标签的属性值里面
			elif  'women' in  gender_cls[0]:
				#那么给它存个女
				gender='女'
		#如果它没有属性值
		else:
			#那么给它做个标记
			gender='中'
		#内容
		content=duanzi.xpath('.//div[@class="content"]/span/text()')
		#把内容进行字符串拼接处理  并且去掉首尾空格
		content = ''.join(content).strip()
		
         #星星和评论
         starts=duanzi.xpath('.//span[@class="stats-vote"]/i/text()')[0]
         #//子孙下查找  / 子查找  切记 ！！！！
         comments=duanzi.xpath('.//span[@class="stats-comments"]//i/text()')[0]
         #搞成字典格式
         data={
        'nick': nick,
        'age': age,
        'gender': gender,
        'content': content,
        'starts': starts,
        'comments': comments
        }
         #获取图片  把图片的src 属性值给拿出来
         duanzi_img=duanzi.xpath('.//div[@class="thumb"]//img/@src')
         #如果有
		if  duanzi_img:
			duanzi_img=duanzi_img[0]
			#给拼接图片  要不下载不了
			duanzi_img = 'https:' +duanzi_img
			#给起个名
			fname = duanzi_img.split('/')[-1]
			#图片下载操作
			request.urlretrive(duanzi_img,'F:/糗事图片/'+fname)
		else:
			#如果没有图片 那么我给它个空字符串
			duanzi_img=''
		#存储
		f.write(json.dumps(data,ensure_ascii=False)+'\n')
if __name__=='__main__':
	f=open('F:/duanzi.json','w',encoding='utf-8')
	getPage()
	f.close()
			
		
		
	
```



#####  多线程来抓取糗事



```
import threading
from queue import Queue
import requests
import random
import json
#启动采集线程个数，自定义用多少线程来去采集去队列里 也就是说是请求url
concurrent=3

#启动解析线程个数
conparse=3


#解析类对html进行处理
class Parse(threading.Thread):
	#thread_list 传入进来的目的  看看采集线程是否存活 底下解析线程来判断
	def __init__(self,number,data_q,thread_list,f):
		super(Parse,self).__init__()
		#初始化属性 完成我们采集所需要的过程
		self.number=number
		self.data_q=data_q
		self.thread_list=thread_list
		self.f=f
		
	def run(self):
		
		#由于网络原因 采集线程没结束呢  解析就不能让他结束  需要判断
		while True:
			#1.判断 看看线程的运行状态 如果还存活 终止for循环 人家还采集呢
			for t in self.thread_list:
				#也就是说如果我采集线程存活呢
				if t.is_alive():
				break
			#这个判断是如果我上面的for循环都为假都不存货了 我让他往底下走 之后来判断html里的数据是否为空，这样比较完美，就是比如我循环完了 一个满足的都没有  自然就走到了else了
			else:
                #for 全为假走到这了  采集线程也就是全挂了 我来看看这个数据队列 如果为空 采集线程结束任务了,解析
              	if self.data_q.qsize()==0:
                	#定义一个标记变量 目的是
                	self.is_parse=False
              #默认是True  如果for循环为真 证明有存活 我就走这了 继续解析 
              #如果都是假走到else 我看看数据为0不 如果为0 走不到下面了  不解析了 如果不为0它还是TRue 因为初始的时候给设置的默认标识
              #加上这个的目就是判断两个条件  
              if self.is_parse:
                html=self.data_q.get()
                self.parse(html) 
              else :
              #如果self.is_parse 为假  那么就结束循环了
             	break
		print('%d号解析线程结束'%self.number)
	
	
	#封装一个解析函数
	def parse(html):
    	html = etree.HTML(html)
        #获取段子div  /div是紧div[@id="content-left"]下面
        #如果是//div子孙节点找  如果是/div 是子节点里找 只在它儿子中找！
        duanzi_div = html.xpath('//div[@id="content-left"]/div')

        #循环所有段子  也就是遍历每一个段子 
        for  duanzi  in  duanzi_div:
            #.//从找到的节点下继续在子孙节点中查找
            nick = duanzi.xpath('.//h2/text()')[0]
            #管道府  都找 满足条件的话
            age = duanzi.xpath('.//div[@class="articleGender manIcon"]/text() | .//div[@class="articleGender womenIcon"]/text()[0]')
            if  age :
                #取片操作
                age=age[0]
            else :
            #没有的话  那么我给它个0 放到数据库 我好知道咋回事！
                age=0

            #通过标签的类名 我们利用xpath来取出它的类名  来看看它是男是女  之后我们做判断
            #这里不能取片  因为里面有的没有
            gender_cls = duanzi.xpath('.//div[@class="articleGender manIcon"]/@class |.//div[@class="articleGender womenIcon"]/@class')

            #如果里面有  那么我来看看它的性别
            if  gender_cls :
                #有的同时  看看如果man字符串在这个标签的属性值里面
                if  'man' in gender_cls[0]:
                    #那么给它存个男
                    gender='男'
                #如果women 字符串在这个标签的属性值里面
                elif  'women' in  gender_cls[0]:
                    #那么给它存个女
                    gender='女'
            #如果它没有属性值
            else:
                #那么给它做个标记
                gender='中'
            #内容
            content=duanzi.xpath('.//div[@class="content"]/span/text()')
            #把内容进行字符串拼接处理  并且去掉首尾空格
            content = ''.join(content).strip()

             #星星和评论
             starts=duanzi.xpath('.//span[@class="stats-vote"]/i/text()')[0]
             #//子孙下查找  / 子查找  切记 ！！！！
             comments=duanzi.xpath('.//span[@class="stats-comments"]//i/text()')[0]
             #搞成字典格式
             data={
            'nick': nick,
            'age': age,
            'gender': gender,
            'content': content,
            'starts': starts,
            'comments': comments
            }
             #获取图片  把图片的src 属性值给拿出来
             duanzi_img=duanzi.xpath('.//div[@class="thumb"]//img/@src')
             #如果有
            if  duanzi_img:
                duanzi_img=duanzi_img[0]
                #给拼接图片  要不下载不了
                duanzi_img = 'https:' +duanzi_img
                #给起个名
                fname = duanzi_img.split('/')[-1]
                #图片下载操作
                request.urlretrive(duanzi_img,'F:/糗事图片/'+fname)
            else:
                #如果没有图片 那么我给它个空字符串
                duanzi_img=''
            #存储
            self.f.write(json.dumps(data,ensure_ascii=False)+'\n')

#采集类
class Crawl(threading.Thread):
	#代理
	proxies=[
      {'host':'61.155.164.111','port':'3128'},
      {'host':'122.72.18.34','port':'80'}
	]
	def __init__(self,number,task_q,data_q)
		#这里用到了父类的初始化方法  父类的初始化方法中调用了写好的run启动线程的方法
		super(Crawl,self).__init__()
		#这个属性是 测试几号线程子解析
		#这个属性是传进来的请求队列
		self.task_q=task_q
		#这个属性是传进来的数据队列
		self.data_q=data_q
	def run(self):
		while not self.task_q.empty():
			#从队列里拿出url
			fullurl = self.task_q.get()
			#测试看看几号线程在采集url
			print('%d号线程采集%s'%(self.number,fullurl))
			ran_proxy=random.choice(self.proxies)
			proxy={
              'http' :'http://'+ran_proxy['host'] +':'+ran_proxy['port'],
              'https' : 'http://'+ran_proxy['port']+':'+ran_proxy['port']
			}
			response=requests.get(url=fullurl,proxies=proxy)
			#如果成功
			if  200<=response.status_code<=300:
				html=response.text
				#把响应文本html 给加入到数据队列中  为了到时候解析
				self.data_q.put(html)
			else:
				print('响应错误')
		
if __name__=='__main__':
	#生成请求队列  里面装的都是url
	task_q=Queue()
	#生成数据队列  用于存放响应的html
	data_q=Queue()
	
	#生成文件对象
	f=open('duanzi.json','w',encoding='utf-8')
	#这个网址是你想用线程来爬取的
	base_url='https://www.qiushibaike.com/8hr/page/%d/'
	for page in range(1,13+1):
		fullurl=base_url % page
		#把url给放到请求队列中
		task_q.put(fullurl）
		
	#采集线程列表
	thread_list=[]
	for  i in range(concurrent):
		#生成线程实例对象t i+1就是number上面定义的初始化参数 所以说实例的时候对象需要这个参数
		t=Crawl(i+1,task_q,data_q)
		#启动线程
		t.start()
		#把线程给加入到线程列表中
		thread_list.append(t)
	#边采集边解析  启动解析线程
	parse_thread=[]
	for  i  in range(conparse):
		t=Parse(i,data_q,f)
		t.start()
		parse_thread.append(t)

	#等待所采集线程运行完毕
	for t in thread_list:
		#目的是让主进程阻塞 等待采集线程运行完毕  在走下面的主进程
		t.join()
	#等待所有解析线程运行完毕
	for t in parse_thread:
		t.join()
		
		
	f.close()
```





## 8. js  正向工程 selenium自动化测试工具

**反反爬虫**

header 

​	cookie

​	user-agent

​	proxy

​	js逆向工程

**js正向工程**

​	简单，资源占用大

​	工具

​		selenium:自动化测试工具

​		phantomjs(无界面浏览器)

​		chrome(解析最好，但是占用资源)

​		对比按键精灵:

​			实现:自动打怪,自动刷副本

​			原理：提供鼠标和键盘的api接口

​	安装:

​		pip install selenium



###  基础 selenium_demo   phantomjs

```
from selenium import  webdriver

import time 
#实例化一个浏览器  指明这个路径 是安装的Phantomjs.exe
browser=webdriver.PhantomJS(executable_path=r'D:\slelenum\phantomjs.exe)

#发请求 模拟人  不用响应
browser.get('https://www.baidu.com')
#找到id为kw的输入框  并且输入了春运
browser.find_element_by_id（'kw').send_keys('春运')
#点击搜索按钮  也就是通过这个标签的属性
browser.find_element_by_id('su').click()
time.sleep(2)
#得到了页面原代码
html=browser.page_source
#并且截取屏幕
browser.save_screenshot('baidu.png')

```

### 基础 人人PhanjomJS



```
from  selenium  import  webdriver
import  time 

base_url="http://renren.com/"

browser=webdriver.PhantomJS(executable_path=r'D:\slelenum\phantomjs.exe')
browser.get(base_url)
time.sleep(1)

#直接找到属性给发送过去值
browser.find_mlement_by_name('email').send_keys('1752570559@qq.com')

#直接找到属性给发送过去值
browser.find_element_by_name('password').send_keys('1234qwer')

#这里别忘记点登陆  才能进去  否则进不去
browser.find_element_by_id('login').click()

#3秒以后截图
time.sleep(3)

#这里一定要png  不写这个报错
browser.save_screenshot('renren.png')
#退出浏览器
browser.quit()
```



### 基础 selenium_demo Chrome

```
谷歌的操作
from selenium  import  webndriver
import  time 
#指明 插件exe运行文件   路径 实例化浏览器
browser=webdriver.Chrome(executable_path=r'D:\slelenum\chromedriver.exe')

browser.get('https://www.baidu.com')

browser.find_element_by_id('kw').send_keys('春运')

#点击搜索按钮
browser.find_element_by_id('su').click()
time.sleep(5)
#得到网页源代码
html=browser.page_source

browser.save_screenshot('renrenguge.png')
```



### 案例  拉钩PhantomJS

```
from  selenium import  webdriver

from lxml import  etree
import  time
base_url='https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput='

#初始化浏览器
dc={#这个必须要加上phantomjs  如果用crome 浏览器  则不用加请求头  这特么是人家浏览器 chrome的请求头
      'phantomjs.page.customHeaders.User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}

#初始化浏览器 ，参数添加请求头
#如果没有把phantomjs 加入到环境变量  则需要指明路径   这个路径是安装的phantomjs.exe的运行文件目录
browser=webdriver.PhantomJS(desired_capabilites=dc,executable_path=r'D:\slelenum\phantomjs.exe')

def parsePage(html):
	html=etree.HTML(html)
	#得到一页的所有li 总共15个工作详细
	job_li = html.xpath('//ul[@class="item_con_list"]/li')
	for  job in job_li:
		  job_name=job.xpath('.//h3/text()')[0]
        add=job.xpath('.//span[@class="add"]/em/text()')[0]
        date_pub=job.xpath('.//span[@class="format-time"]/text()')[0]
        money=job.xpath('.//div[@class="li_b_l"]/span/text()')[0]
        exp=job.xpath('.//div[@class="li_b_l"]/text()')[2].strip()
        company=job.xpath('.//div[@class="company_name"]/a/text()')[0]
        data={
             'job_name':job_name,
            'add' : add,
            'date_pub' : date_pub,
            'money' : money,
            'exp' : exp,
            'company' : company
        }
        #转成json格式化字符串
        f.write(json.dumps(data,ensure_ascii=False)+'\n')
	
	
def getPage():
	browser.get(base_url)
	time.sleep(0.5)
	html=browser.page_source
	pagePage(html)
	
	while True:
		browser.find_element_by_class_name('pager_next ').click()
		time.sleep(0.2)
		html=browser.page_source
		parsePage(html)
		if 'pager_next_disabled' in html:
			break
if __name__=='__main__':
	f=open('lagou.json','w',encoding='utf-8')
	getPage()
	f.close()

```



### 案例 拉钩 chrome   

```
from  selenium   import   webdriver
import  time
from  lxml  import  etree
import  json

base_url='https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput='

#初始化浏览器  ，参数添加请求头  如果没有把phantomjs 加入到环境变量  则需要指明路径   这个路径是安装的chromedriver.exe 的运行路径

browser=webdriver.Chrome(executable_path=r'D:\slelenum\chromedriver.exe')

def parsePage(html):
	 #提取
    html=etree.HTML(html)
    #得到一页的所有li  总共15个工作详细
    job_li=html.xpath('//ul[@class="item_con_list"]/li')
    #得到每一个job  对每一个li进行数据提取
    for  job  in  job_li:
        #.//就是从已经找好的下面  从h3开始 把它当作了根 之后顺着下面去找 而且可以找任何只要指明属性 它上面不用非得有标签
        # 如果是1个/必须要指定根下的谁谁谁eg://?/?/?
        #xpath  返回的是列表 要对其 进行 取片操作
        job_name=job.xpath('.//h3/text()')[0]
        add=job.xpath('.//span[@class="add"]/em/text()')[0]
        date_pub=job.xpath('.//span[@class="format-time"]/text()')[0]
        money=job.xpath('.//span[@class="money"]/text()')[0]
        exp=job.xpath('.//div[@class="li_b_l"]/text()')[2].strip()
        company=job.xpath('.//div[@class="company_name"]/a/text()')
        data={
            'job_name': job_name,
            'add': add,
            'date_pub': date_pub,
            'money': money,
            'exp': exp,
            'company': company
        }
        #写一次换一次行  json写入文件 默认是ascii码  给改成false
        f.write(json.dumps(data,ensure_ascii=False)+'\n')
	
def getPage():
	browser.get(base_url)
	html=browser.page_source
	parsePage(html)
	while  True :
		#找到下一页按钮
		browser.find_element_by_class_name('pager_next').click()
		#也防止过快   因为这个软件自己操作浏览器呢
		time.sleep(2)
		#继续得到html文本
		html=browser.page_source
		#再次解析页面
		parsePage(html)
		#如果最后一页点不动的表示在这个html页面中，那么我们终止循环
		if 'pager_next_disabled' in html:
			break
if __name__=='__main__':
	f=open('F:/lago.json','w',encoding='utf-8')
	getPage()
	#执行完之后退出这个界面   也就是退出退出浏览器
	browser.quit()
	f.close()
```



### 案例  斗鱼

```
from selenium import webdriver
import  time 
base_url='https://www.douyu.com/directory/all'

#初始化浏览器  参数添加请求头   
browser=webdriver.PhantomJS(executable_path=r'D:\slelenum\phantomjs.exe')

def parsePage(html):
	#提取
    html=etree.HTML(html)
    #得到一页的所有li  总共15个工作详细
    job_li=html.xpath('//ul[@class="item_con_list"]/li')
    #得到每一个job  对每一个li进行数据提取
    for  job  in  job_li:
        #.//就是从已经找好的下面  从h3开始 把它当作了根 之后顺着下面去找 而且可以找任何只要指明属性 它上面不用非得有标签
        # 如果是1个/必须要指定根下的谁谁谁eg://?/?/?
        #xpath  返回的是列表 要对其 进行 取片操作
        job_name=job.xpath('.//h3/text()')[0]
        add=job.xpath('.//span[@class="add"]/em/text()')[0]
        date_pub=job.xpath('.//span[@class="format-time"]/text()')[0]
        money=job.xpath('.//span[@class="money"]/text()')[0]
        exp=job.xpath('.//div[@class="li_b_l"]/text()')[2].strip()
        company=job.xpath('.//div[@class="company_name"]/a/text()')
        data={
            'job_name': job_name,
            'add': add,
            'date_pub': date_pub,
            'money': money,
            'exp': exp,
            'company': company
        }
        #写一次换一次行  json写入文件 默认是ascii码  给改成false
        f.write(json.dumps(data,ensure_ascii=False)+'\n')


def getPage():
	#第一页请求
	browser.get(base_url)
	time.sleep(0.5)
	#因为这个PhantomJS 反应慢 或者是网慢 从而影响了我们页面抓取
	html=browser.source_page
	#解析  我只是把函数拿来调用一下 程序还往下走
	parsePage(html)
	#让它循环  找到下一页
    while True:
        #找到下一页按钮
        browser.find_element_by_class_name('pager_next ').click()
        #也防止过快 因为 这个软件自己操作浏览器呢 --！
        time.sleep(2)
        #继续得到html文本
        html=browser.page_source
        #再次解析页面
        parsePage(html)
        #如果最后一页点不动的表示在这个html页面中，那么我们终止循环
        if  'pager_next_disabled'  in  html:
            break


if __name__ == '__main__':
    f=open('F:/lago.json','w',encoding='utf-8')
    getPage()
    #执行完之后退出这个界面  也就是退出浏览器
    browser.quit()
    f.close()
```





## 9. 瀑布流下载图片  

```
from selenium  import webdriver 
from lxml import etree 
import time 
from urllib import request 

def parserPage(html):
	html=etree.HTML(html)
	##每次调用都取最后一个div  因为一滚动  一加载  他是ajax从后台取出数据  之后前端渲染页面
	#每刷新一次   它就加一个div 
	#取出div  组成列表
	div_list=html.xpath('//div[@class="imgpage"])[-1]
	#找到里面的每个li  取出图片
	li_list=div_list.xpath('.//ul/li//a/img/@data-imgurl')
	for  img_url in li_list:
		fname=img_url.split('/')[-1]
		request.urlretrive(img_url,'F:/足球宝贝/'+fname)
	
def getPage():
	brows=webdriver.Chrom(executable_path='D:\slelenum\chromedriver')
	#这个url是拿filterzhjua抓取的网址
	base_url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1516082305937_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%B6%B3%E7%90%83%E5%AE%9D%E8%B4%9D'
	brows.get(base_url)
	time.sleep(2)
	html=brows.page_source
	parsePage(html)
	
	while True :
		#循环滚动  这里的参数是写js代码
		brows.execute_script('scrollTo(0,document.body.scrollHeight)')
		#睡一会 
		time.sleep(2)
		#得到页面
		html=brows.page_source
		#解析页面  
		paserPage(html)
if __name__=='__main__':
	getPage()
		
```



# **----------------------------------**

# scrapy爬虫框架

## 1.scrapy了解

### 1.1 scrapy安装

Scrapy的安装介绍
Scrapy框架官方网址：http://doc.scrapy.org/en/latest



**windows 安装方式**

⦁	Python 2 / 3
⦁	pio install Twisted-17.9.0-cp35-cp35m-win_amd64.whl
⦁	升级pip版本：pip install --upgrade pip
⦁	通过pip 安装 Scrapy 框架pip install scrapy

**白话**

```
安装scrapy  框架
    1.安装 pywin32-221.win-amd64-py3.5

       #异步网络框架
    2. 先安装Twisted-17.9.0-cp35-cp35m-win_amd64.whl  这个要指明文件所在路径
       目的防止安装pip  install  scrapy报错
       还有一种是利用国内源 pip  install -i  https://pypi.tuna.tsinghua.edu.cn/simple scrapy
    3.直接安装pip  install  scrapy
```



**Linux安装**
⦁	Python 2 / 3
⦁	安装非Python的依赖 sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
⦁	通过pip 安装 Scrapy 框架 sudo pip install scrapy



### 1.2 scrapy框架

⦁	Scrapy是用纯Python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架，用途非常广泛。
⦁	框架的力量，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片，非常之方便。
⦁	Scrapy 使用了 Twisted['twɪstɪd](其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。



### 1.3 scrapy架构

⦁	Scrapy Engine(引擎): 负责Spider、6mPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
⦁	Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队（Queue），当引擎需要时，交还给引擎。
⦁	Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，
⦁	Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，

⦁	Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
⦁	Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。
⦁	Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）



### 1.4 scrapy的运作流程

代码写好，程序开始运行...
⦁	引擎：Hi！Spider, 你要处理哪一个网站？
⦁	Spider：老大要我处理xxxx.com。
⦁	引擎：你把第一个需要处理的URL给我吧。
⦁	Spider：给你，第一个URL是xxxxxxx.com。
⦁	引擎：Hi！调度器，我这有request请求你帮我排序入队一下。
⦁	调度器：好的，正在处理你等一下。
⦁	引擎：Hi！调度器，把你处理好的request请求给我。
⦁	调度器：给你，这是我处理好的request
⦁	引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求
⦁	下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
⦁	引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给def parse()这个函数处理的）
⦁	Spider：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。
⦁	引擎：Hi ！管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。
⦁	管道``调度器：好的，现在就做！
注意！只有当调度器中不存在任何request了，整个程序才会停止，（也就是说，对于下载失败的URL，Scrapy也会重新下载。）







### 1.5  制作 scrapy  步骤

制作 Scrapy 爬虫 一共需要4步：
⦁	新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
⦁	明确目标 （编写items.py）：明确你想要抓取的目标
⦁	制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
⦁	存储内容 （pipelines.py）：设计管道存储爬取内容







## 2. scrapy 代码流程



**1.建立项目 ：进入指定目录下 创建项目**

​			**eg :  cd   F:/  scrapy startproject  项目名**

**2. 建立一个爬虫: 进入到项目的spider目录下  **

​	   //自己起的爬虫名teacher  域名  尽量2级的 就是没有www

​			**eg: scrapy genspider teacher  itxdl.cnm**

**3. 运行一下**

​			**eg:  scrapy  crawl teacher**



### 2.1 案例1 初识scrapy

 **小型代码以项目名为pckj_text为例 最外一层级pckj_text没写**

​	Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，

**爬虫文件：** pckj_text/spiders/teacher.py  

```
import  scrapy
#这里需要导入  保存数据结构的文件自定义的类 好比数据模型
from pckj_text.items import  TeacherItem

#创建了一个爬虫
class TeacherSpider(scrapy.Spider):
	name='teacher'
	
	#首先这里这个二级名是scrapy在我们创建爬虫的时候自动帮我们生成的 尽量别加主域名www
	allowed_domains=['itxdl.cn']
	#第二个我只能在这个网站进行爬取 爬取起始页
	start_urls=['http://www.itxdl.cn/activity/teacher/teacher_lieibiao/']
	
	#得到了响应
	#在这来做响应解析 
	def parse(self,response)
		teacher_list=response.xpath('//div[@class="php_jiangshi_liebiao"]')
		for teacher  in teacher_list:
			#实例化一个数据对象  是数据模型  也是爬虫扒下来的字段 其实类似字典  这个数据对象的类是我在items.py 这个保存数据结构的文件建立的 其实就是个类字典
			item=TeacherItem()
			name = teacher.xpath('.//h1/text()').extract()[0]
             industry = teacher.xpath('.//p/text()').extract()[0]
             img = teacher.xpath('.//img/@src').extract()[0]
             
             #这根item.py的字段要对上  这个字典对象的键--！
             item['name']=name
             item['industry']=industry
             item['img']=img
             #数据一个一个返回到项目管道 不能用return  如果return则一条数据 for 循环里面如果return了那么 它就停止了 这里我们用yield 并且使用它不会终止for 循环 
             yield item
             
             
			
```



**数据结构文件 pckj_text/items.py**



```
import   scrapy
#这里是系统自动生成的一个类 底下的我们照着写就好了
class PckjTextItem(scrapy.Item):
	pass

##这个数据对象的类是我在items.py 这个保存数据结构的文件建立的 其实就是个类字典
class TeacherItem(scrapy,Item):
	#定义item  只需要继承scrapy.item类 并将所有字段定义为 scrapy.Field类型即可
	name=scrapy.Field()
	industry=scrapy.Field()
	img=scrapy.Field()
```



**执行爬虫工作的文件 pckj_text/main.py**

正常我们是在命令行启动的这条命令  来让爬虫工作  写文件里是被封装好了的

```
from scrapy  import  cmdline

#在这运行文件 
cmdline.excute('scrapy crawl teacher'.split())
```



**中间件文件 middleware.py**

 **加代理**

**1.自己写到另起文件mymidddlewares.py 也可以把这个直接写到middleware里 看你setting.py**DOWNLOADER_MIDDLEWARES**怎么设置**

```
 mymiddlewares.py
 from scrapy_03 import  settings
 from base64 import b64encode
 import  random
#免费代理
class RandomProxy(object):
	#当每个request通过下载中间件的时候，该方法被调用
	def process_request(self,request,spider):
		#把我写好的代理给在setting里导入进来的 
		proxy=random.choice(setting.PROXIES)
 		#我们将代理中间件的代理改写如下，表示遇到异常的时候给请求加上代理
 		#返回request,这个样就会重新请求谷歌
 		proxy='http://%s:%d'(proxy['host'],proxy['port'])
 		request.meta['proxy'] = proxy #设置代理
 		
 
 #认证代理
class RandomAuthProxy(object):
	def process_request(self,request,spider):
		proxy=random.choice(setting.AUTH_PROXIES)
		#设置认证信息
		auth = proxy['user']+':'+proxy['pwd']
		
		auth=bytes(auth,encoding="utf-8")
		auth=b64encode(auth)
		request.headers['Proxy-Authorization']=b'Basic' +auth
		#设置代理信息
		proxy='http://%s:%d' %(proxy['host'],proxy['port'])
		request.meta['proxy']=proxy 设置代理
```

**2.加代理setting设置中间件**

```
#自己写的中间件  为了加代理  dowlloader中间件
#通过中间件 来实现ip的伪装
DOWNLOADER_MIDDLEWARES = {
#这里你看看你在哪写到   用哪个代理   设置好就ok
   'scrapy_03.mymiddlewares.RandomProxy': 1,
}


#免费代理
PROXIES = [

    {'host': '123.125.142.40', 'port': 80},
    {'host': '46.4.227.210', 'port': 1080},
    {'host':'206.221.184.58','port':1080},
    {'host': '103.87.16.2', 'port': 80},
    {'host': '185.111.44.73', 'port': 80},
    {'host': '47.206.51.67', 'port': 8080},
    {'host': '60.255.186.169', 'port': 8888}
]


#花钱认证代理
AUTH_PROXIES = [
    {'host':'127.78.166.84','port':6666,'user':'alice','pwd':'123456'}
]

```



**管道文件 pipelines.py**

⦁	Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.

```
import json 
#系统写好的
class PckjTextPipeline(object):
    def process_item(self, item, spider):
        return item
        
#这里接收到已经解析的数据item
#自己的理解它就像是一个漏洞的管道  爬虫把数据之后通过引擎给到管道
#之后 管道里的各个类也就是要数据操作的方式不一样 
#优先级的意思是数据从管道进来了  谁先拿 拿完之后一定要把数据给返回过去
#因为下面还有其他的人要呢 --！
class TeacherPiepeline(object):
	def __init__(self):
		self.f=open('teacher.json','w',encoding='utf-8')
	def process_item(self,item,spider):
	#这里return的含义是数据我用完了 必须给返回 
		return  self.f.write(json.dumps(item),ensure_ascii=False)+'\n')
		#爬虫结束被调用
	def close_spider(self,spider):
		self.f.close()
```



**项目配置文件 settings.py**

```
#不遵守规则   
ROBOTSTXT_OBEY = False
  
 #管道优先级
ITEM_PIPELINES = {
	#这个在运行哪一个爬虫的时候先把别的给注释掉
    #数字越小 优先级越大  也就是数据先到这个这个类
   'pckj_text.pipelines.TeacherPipeline': 1,
}

# 并发量的设置   让队列的url 同时请求
CONCURRENT_REQUESTS = 8 


#下载延迟  在这给设置时间
DOWNLOAD_DELAY = 0
   
   
#自己写的中间件  为了加代理  dowlloader中间件
#通过中间件 来实现ip的伪装
DOWNLOADER_MIDDLEWARES = {
   'scrapy_03.mymiddlewares.RandomProxy': 1,
}


#打开这个不带cookie去请求
#COOKIES_ENABLED = False


#全局给加 请求头 如果自己写 会把它这个给覆盖  它这个不好用
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}



# #指定图片字段 也就是item里面写的别忘记加
# IMAGES_URLS_FIELD = 'images'
# #获取项目路径  dirname  路径部分
# import  os
# Base_dir=os.path.dirname(os.path.dirname(__file__))
# #下载路径
# #images 是我自己建立的文件夹 根配置的进行添加
# IMAGES_STORE = os.path.join(Base_dir,'images')


# ITEM_PIPELINES = {
#     #图片管道
#     # 'scrapy.pipelines.images.ImagesPipeline' : 1, # 图片处理管道 系统自带的
#     # 'scrapy_03.pipelines.YuehuiImagePipeline': 2,#这是自己重写的

#     #爬虫管道
#    'scrapy_03.pipelines.paxiciPipeline': 1,
# }
```



### 2.2 案例2 66ip

**spiders 爬虫文件**

```
import  scrapy

from scrapy_lianxi.items import Item66
class A66ipSpider(scrapy.Spider):
	name='66ip'
	allow_domains=['66ip.cn']
	start_urls=['http://66ip.cn/']
	headers={
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

	}
	
	def parse(self,response):
		#找到了所有tr   tr也就是一行  也就是行 第0个不要 索引从0开始
		ip_tr=response.css('div#main table tr')[1:]
		#遍历每一行
		for tr in ip_tr:
			#这个实例化对象写到for循环里
			item=Item66()
			#css选择器
			#从一行tr中中拿出列td  取出文本
			data=tr.css('td::text')
			ip=data[0]
			port=data[1]
			location=data[2]
			#把数据交给项目管道
ql			item['ip]=ip
			item['port']=port
			item['location']=location
			yield  item
		#如果有这个标志  证明有下一页
		if  '&raquo;'  in  response.text
		#取出下一页   extract ()不加返回的是对象 加上返回的是列表
		#a::attr(href) 取出a标签里的属性href链接
			next_url=response.css('div#PageList a::attr(href)').extract()[-1]
			next_url='http://www.66ip.cn'+next_url
			yield  scrapy.Request(url=next_url,callback=self.parse,headers=self.headers)
			
```



**数据结构文件items文件**

```
class Item66(scrapy.Item)
	ip=scrapy.Field()
	port=scrapy.Field()
	location=scrapy.Field()
	#加个爬虫名  为了知道是从哪个网站爬取下来的数据
	spider_name=scrapy.Field()
```



**pipelines.py做数据存储的文件**

```
import  json
class Pipeline66(object):
	def __init__(self):
		self.f=open('66.json','w',encoding='utf8')
	def process_item(self,item,spider):
		item['spider_name']=spider.name
		self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
		return item
	def close_spider(self,spider)
		self.f.close()
```

**settings.py**

```
#不遵守协议
ROBOTSTXT_OBEY=False

#并发量的设置  让队列的url 同时请求 url队列是一个个调度出来的 异步非堵塞
CONCURRENT_REQUESTS = 8

#下载延迟  在这给设置时间 是你设置的0.5-1.5倍
DOWNLOAD_DELAY = 0

#项目管道 优先级  看先流经谁
ITEM_PIPELINES = {
  'scrapy_lianxi.pipelines.Pipeline66':2
}
```



**运行文件main.py**

```
from  scrapy import  cmdline
cmdline.excute('scrapy crawl 66ip'.split())
```



### 2.3 案例3  腾讯招聘

**爬虫文件 tencent.py**

```
import  scrapy
from scrapy_lianxi.items import TencentItem

class TencentSpider(scrapy.Spider):
	name='tencent' #爬虫名称
	allowed_domains= ['tencent.com']# 有效域
	start_urls=['http://hr.tencent.com]
	
	base_url='http://hr.tencent.com/position.php?&start=%d'
	def parse(self,response)
		#构建所有分页请求
		for i in range(0,2910+1,10)
			fullurl=self.base_url % i 
			yield scrapy.Request(url=fullurl,callback=self.parseList,headers=self.headers)
	#对列表页获取每一条招聘链接
	def parseList(self,response):
		detail_urls=response.css('tr.even a::attr(href),tr.odd a:attr(href)')
		for url in  detailurls:
			fullurl='http://hr.tencent.com/' + url
			yield scrapy.Request(url=fullurl,callback=self.parseDetail,headers=self.headers)
	
	#详情页 数据提取		
	def parseDetail(self,response):
		item = TencentItem()
		title = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
		info = response.xpath('//table//tr[2]/td/text()').extract()
		location = info[0]
		p_type = info[1]
		number = info[2].strip('人')
		duty  = response.xpath('//table//tr[3]//li/text()').extract()
		duty = ''.join(duty)
		
		requirement= response.xpath('//table//tr[4]//li/text()).extract()
		requirement = ''.join(requirement)
		
		item['title'] = title 
		item['location'] = location
		item['p_type'] = p_type
		item['number'] = number
		item ['duty'] = duty
		item['requirement']= requirement
		#交给管道文件
		return  item
```

**数据结构字段items**

```
class TencentItem(scrapy.Item):
	title=scrapy.Field()
	location = scrapy.Field()
	p_type = scrapy.Field()
	number = scrapy.Field()
	duty = scrapy.Field()
	requirement = scrapy.Field()
	
```



**项目管道pipelines**

```
class TencentPipeline(object):
	def __init__(self):
		self.f=open('position.json','w',encoding='utf-8')
	def process_item(self,item,spider):
		self.f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
		return item
	def close_spider(self,spider):
		self.f.close()
```

**settings.py**

```
#不遵守协议
ROBOTSTXT_OBEY=False

#并发量的设置  让队列的url同时请求
CONCURRENT_REQUESTS=8

#下载延迟 在这设置时间
DOWNLOAD_DELAY = 0 

#项目管道 优先级
ITEM_PIPELINES = {
  'scrapy_lianxi.pipelines.TencentPipeline':1
}
```



**main.py**

```
from  scrapy import  cmdline
cmdline.execute('scrapy crawl tencent'.split())
```



### 2.4 案例4 约会.163

**爬虫文件 spider.py**

```
import  scrapy 
from  scrapy_lianxi.items import  YuehuiItem
import  jsonpath
import  re

class YuehuiSpider(scrapy.Spider):
	name='yuehui'
	allowed_domains = ['yuehui.163.com']
	#第一页 这页可以随便写
	start_urls = ['http://yuehui.163.com/searchusers.do']
	#请求头
	#加入队列的url 也就是我请求的url
	#这个因为在响应的时候html文本中没有数据 所以用filder找它的数据接口
	#这里用到的是js加载  通过后台拿数据 前端js文件把它填充到前端页面里
     base_url='	  http://yuehui.163.com/searchusersrcm.doajax=1&ageBegin=29&ageEnd=30&aim=-1&marriage=0&mode=4&order=8&province=0&city=0&district=-1&sex=0&uTag=0&vippage=-1&page=%d&pagesize=81'
	#循环生成请求队列  加入队列
	#scrapy有一个机制 对已发的请求有过滤去重的作用  如果重复则不再发送了 
	#流程:对每一页请求  之后callback函数在向详情页发链接  详情页callback在提取数据
	def parse(self,response):
		for  i in range(1,7):
			fullurl=self.base_url % i 
			#callback回调函数 响应的时候被触发
			yield scrapy.Reques(url=fullurl,callback=self.parsePage,headers=self.headers)
	
	def parsePage(self,response):
		#构建详情页请求 
		#jsonpath.jsonpath()是用jsonpath来进行提取 第一个参数是提取的文本  第二个参数是想按照什么样的规则来进行提取
		#返回列表！因为很多id		
		id_list=jsonpath.jsonpath(json.loads(response.text),'$..id')
		base_url='http://yuehui.163.com/viewuser.do?id=%s':
		for uid in id_list:
			fullurl = baseurl % uid 
			yield scrapy.Request(url=fullurl,callback=self.parseDetail)
			
	def parseDetail(self,response):
		#把响应的url的uid给拿出来  发真心话请求的时候用
		uid = response.url.split('=')[-1]
		item = YuehuiItem()
		#取p标签(p) class为nick(.nick) 并且把内容取出来(::text)
		nick = response.css('p.nick::text').extract()[0]
		#ul标签 class为infolist   下面的li  这里需要空格切记
		#先把所有li给搞出来  这样方便写规则
		info = response.css('ul.infolist li')
		gender = info[0].xpath('.//text()').extract()[0].strip('性别: ')
		married = info[1].xpath('.//text()').extract()[0].strip('婚姻状况: ')
		age = info[2].xpath('.//text()').extract()[0].strip('学  历:')
		location = info[4].xpath('.//span[2]/text()').extract()[0]
		job = info[4].xpath('.//span[4]/text()').extract()
		
		if job :
			job = job[0]
		else :
			job = '无

		height = info[5].xpath('.//text()').extract()[0].strip('身高: cm')
		weight = info[7].xpath('.//text()').extract()[0].strip('体重: 公斤')
		constellation = info[9].xpath('.//text()').extract()[0]
			#获取头像
		        images = response.xpath('//div[@class="prwrap"]/div[@class="portrait portrait-195"]/img/@src').extract()

		
		item['uid'] = uid 
		item['nick'] = nick 
		item["gender"] = gender
         item["married"] = married
         item["age"] = age
         item["degree"] = degree
         item["location"] = location
         item["job"] = job
         item["height"] = height
         item["weight"] = weight
         item["constellation"] = constellation
         #头像
         item['images'] = images  # 需要传入列表
         yield  item
         #也是点击通过filter来抓取的  
         true_url = 'http://yuehui.163.com/getqalist.do?ajax=1&id=%d&page=1&pagesize=1000' % int(uid)
         yield scrapy.Request(url=true_url,callback=self.parseTrue)
     
     def  parseTrue(self,response):
     	#对响应的json格式字符串解码转成python对象
     	data=json.loads(response.text)
     	#把里面的list字典拿出来  里面有很多人问答题
     	data = data[0]['list']
     	#正则匹配uid 通过响应的url来进行匹配 表关联会用到
     	pat=re.compile(r'(\d+)')
     	res=pat.search(response.url)
	    if  res is not None:
        	uid = res.group(1)
        	for true  in data:
        		item=TrueHeart()
        		qid=true['qid']
        		question=true['question']
        		answer=true['answer']
        		
        		item['qid']=qid
        		#通过这个值来在表中设置进行外键关联
        		item['uid']=uid
        		item['question']=question
        		item['answer']=answer
        		yield  item
       

		
```



**items.py**

```
class YuehuiItem(scrapy.Item):
	uid = scrapy.Field()
	nick = scrapy.Field()
	gender = scrapy.Field()
	married = scrapy.Field()
	age = scrapy.Field()
    degree = scrapy.Field()
    location = scrapy.Field()
    job = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    constellation = scrapy.Field()
    
    def get_sql(self):
    	sql='insert into yuehui_user(uid,nick,gender,married,age,degree,location,job,height,weight,constellation) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
         if not self['height']:
         	self['height'] = 0
         if  not self['weight']:
         	self['weight'] = 0
         if not self['age'] :
         	self['age']= 0
         
         data =[
         self['uid'], self['nick'], self['gender'], self['married'], self['age'], self['degree'],
          self['location'], self['job'], self['height'], self['weight'], self['constellation']
                ]

		return sql,data
		

#真心话   
class TrueHeart(scrapy.Item):
	#问题id 
	uid =scrapy.Field()
	
    question = scrapy.Field()
    answer = scrapy.Field()
    def get_sql(self):
    	sql='insert into yuehui_trueheart(uid,question,answer) ' \
              'values(%s,%s,%s)'
        data=[self['uid'],self['question'],self['answer']]
        return  sql, data
```

**pipelines.py**

```
#约会
import  pymysql 
class YuehuiPipeline(object):
	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
		self.cursor = self.conn.cursor()
	def process_item(self,item,spider):
		sql,data = item.get_sql()
		try:
         	self.cursor.excute(sql,data)
         	self.conn.commit()
         exceptt Exception as e :
         	self.conn.rollback()
         return item
     def close_spider(self):
      	self.cursor.close()
      	self.conn.close()
      	
   #真心话
 class TrueHeartPipeline(obj):
 	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
		self.cursor = self.conn.cursor()
	def process_item(self,item,spider):
		sql,data = item.get_sql()
		try:
         	self.cursor.excute(sql,data)
         	self.conn.commit()
         exceptt Exception as e :
         	self.conn.rollback()
         return item
     def close_spider(self):
      	self.cursor.close()
      	self.conn.close()
      	
      	
      	
 #图片操作单独一个pipeline 
 class YuehuiImagePipeline(ImagesPipeline):
 	def  item_completed(self,results,item,info):
 		if results[0][0]:
 			item['image_path'] = results[0][1]['path']
 		else:
 			item['image_path'] = ''
 			#这没写完应该是
 		return  item
         	
         
```



**setting.py**

```
#不遵守协议
ROBOTSTXT_OBEY = False 
#并发量的设置  让队列的url同时请求
CONCURRENT_REQUESTS = 8

#下载延迟 在这给设置时间
DOWNLOAD_DELAY = 0


#项目管道 设置
ITEM_PIPELINES = {
  'scrapy_lianxi.pipelines.YuehuiPipeline':1
  'scrapy_lianxi.pipelines.TrueHeartPipeline':2
  
  图片管道
  scrapy.pipelines.images.ImagesPipeline' : 1, # 图片处理管道 系统自带的
  'scrapy_03.pipelines.YuehuiImagePipeline': 2,#这是自己重写的
  
}

#指定图片字段 也就是item里面写的
IMAGES_URLS_FIELD = 'images'

下载路径
import  os
Base_dir=os.path.dirname(os.path.dirname(__file__))
#images 是我自己建立的文件夹 根配置的进行添加
IMAGES_STORE = os.path.join(Base_dir,'images')

```

**main.py**

```
from  scrapy import  cmdline
cmdline.execute('scrapy crawl yuehui'.split())
```

 

### 2.5 案例5 爬取西祠代理   存库   并且从库里过滤

**爬虫paxici.py**

```
# -*- coding: utf-8 -*-
import scrapy
import  time
from  scrapy_03.items import xiciItem
class PaxiciSpider(scrapy.Spider):
    name = 'paxici'
    allowed_domains = ['xicidaili.com']
    #这里写成百度是为 也就是我第一次发这个请求的时候没加上这个请求头headers
    #系统默认发一次 因为西祠不加请求头 你访问不了 所以改了个baidu
    start_urls = ['http://www.baidu.com']
    base_url='http://www.xicidaili.com/nn/%d'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

    }
    #第一个参数是starturl的响应
    def parse(self, response):
        #scrapy线程机制是先进后出 根栈是的
        #所以我要想让他从第一页开始所以需要倒着循环分页
        for  i  in range(1000,0,-1):
            fullurl=self.base_url % i
            #yield其实是给返回一个生成器
            #生成器是迭代器 你只能遍历它一次  因为生成器没有将所有的值放入内存中，而是实时的生成这些值
            #将实时生成的值及时进行处理  不用非得等到循环结束
            time.sleep(5)
            yield scrapy.Request(url=fullurl,headers=self.headers,callback=self.parsePage)

    #这个响应是上面调用我这个函数的响应
    def  parsePage(self,response):
        #得到tr列表  每一行  目的取出ip和端口号
        tr_list = response.xpath('//table[@id="ip_list"]//tr')[1:]
        for  tr  in  tr_list:
            item=xiciItem()
            #取出td一行每一列  xpath都返回列表
            td_list=tr.xpath('.//td/text()').extract()
            host = td_list[0]
            port = td_list[1]
            #把取回的端口号已字典的形式给返回到项目管道pipelines
            #这里我直接给到pipelines了
            # 如果入库的话 在items下写好sql和data 之后写好方法  到pipeline直接导入来在插入数据库就好啦
            item['host'] = host
            item['port']= port
            yield item


```



**item.py**

```

class xiciItem(scrapy.Item):
    port=scrapy.Field()
    host=scrapy.Field()


```



**pipelines.py**

```

#西祠pipeline
import  pymysql
class paxiciPipeline(object):
    def __init__(self):
        #初始化链接mysql方法作为我这个类属性
        self.conn = pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
        #初始化游标操作数据库的方法作为我这个类的属性
        self.cursor = self.conn.cursor()
    #这个函数名字不能换
    # 这个方法是把item(item是一种数据模型,和django里的model很像，一种表现形式)
    # 这个对象通过爬虫过来的数据的写入数据库操作
    def  process_item(self,item,spider):
        #数据存储操作
        host = item['host']
        port = item['port']
        #sql 语句 注意字段名 ！！
        sql = 'insert into xici(host,port) values(%s,%s)'
        #插入数据库的时候 这个数据是由列表组成的
        data = [host,port]
        try:
        #用到了游标下面的一个excute插入数据的方法
            self.cursor.execute(sql,data)
            #提交操作  属于事物处理 要么同时成功 要么同时失败
            self.conn.commit()
        except Exception as e :
            print(e)
        return  item
    #当某个spider被关闭时，该信号被发送。该信号可以用来释放每个spider在开启时候所占用的资源
    def  close_spider(self,spider):
        #这里就关闭数据库操作了！ 在往深有点深了
        self.cursor.close()
        self.conn.close()


```



**setting.py**

```
 
 ITEM_PIPELINES = {
 'scrapy_03.pipelines.paxiciPipeline': 1,
 }
```

**线程过滤filter.py**

```
import  pymysql
import  threading
import  requests
from lxml import etree
conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
cursor=conn.cursor()
from queue import  Queue
#第一步 从数据库里查出来之后过滤
def  getProxy():
    proxy_q=Queue()
    sql='select * from xici'
    #执行sql语句
    cursor.execute(sql)
    #查询所有数据 返回 结果是个二级元祖
    res=cursor.fetchall()
    #遍历 加入队列
    for  proxy in  res:
        #队列添加数据.put方法 把元祖加入到队列
        # print(proxy)
        proxy_q.put(proxy)
    #打印出来是个队列对象
    # print(proxy_q)
    res=proxy_q.get()
    print(res)
    #return 之后调用之后打印的结果是值
    return  proxy_q

#线程过滤
class ProxyManager(threading.Thread):
    #对属性进行初始化  之后传递进来
    def __init__(self,proxy_q,lock):
        super(ProxyManager, self).__init__()
        #我现在需要这个参数  所以我就给初始化这个属性也就是这个参数 底下实例化我的时候需要给我传递进来
        self.proxy_q = proxy_q
        #lock用到了线程里的一个方法 线程锁  也就是我这个线程在执行的时候我给它锁起来 谁也进不来  等我把活干完了你在干
        self.lock=lock
    def run(self):
        base_url='http://www.baidu.com/s?wd=ip'
        #如果不为空  那么我从队列里取出代理
        while not self.proxy_q .empty():
            proxy=self.proxy_q.get()
            print(proxy)
            proxy_info={
                'http':'http://'+proxy[1]+":"+str(proxy[2])
            }
            try:
                #requests直接加proxies
                response=requests.get(url=base_url,proxies=proxy_info,timeout=10)
                if  not(200 <= response.status_code <= 300):
                    #锁定线程
                    with self.lock:
                        #之后删除代理
                        self.drop_proxy(proxy[1])
                else:
                    html = etree.HTML(response.text)
                    if not html.xpath('//span[@class="c-gap-right"]/text()'):
                        # 删除代理
                        with self.lock:
                            self.drop_proxy(proxy[1])
                    else:
                        print(proxy)
            except Exception as  e :
                print(e)
                with self.lock:
                    self.drop_proxy(proxy[1])

    def drop_proxy(self,host):
        sql='delete from xici where host="%s' % host
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

if __name__ == '__main__':
    proxy_q=getProxy()
    thread_list=[]
    #threading的一个方法
    lock=threading.Lock()
    #创建线程
    for  i  in  range(1):
        t=ProxyManager(proxy_q=proxy_q,lock=lock)
        t.start()
        thread_list.append(t)

    for  t in  thread_list:
        #主线程被阻塞  等其他线程结束  在跑主线程
        t.join()
```



### 2.6  案例6 安居客房源 案例 在爬虫里面给配置setting



```
import  scrapy
import re
import  os 

from scrapy_04.items import HouseItem

Base_dir = os.path.dirname(os.path.dirname(__file__))

class AnjukeSpider(scrapy.Spider):
	name='anjuke'
	allowed_domains=['anjuke.com']
	
	#这里设置起始的网站   底下可以重新写 如果不重新写给它加上 这个第一次请求
	start_urls = ['https://bj.zu.anjuke.com/']
	
	#这是分页请求的url
	base_url = 'https://bj.zu.anjuke.com/fangyuan/p%d/'
	
	#给图片自己加的请求头
	headers={
      太多 没写
	}
	#给这个爬虫单独配置settings 
	custom_settings = {
      #先设置一下请求频率 不能太快 
      	'CONCURRENT_REQUESTS' :1,
      	
	#setting里有这个全局请求头 我这里给自己加一下   它那个少 不好用
		'DEFAULT_REQUEST_HEADERS':{
            "Host": "bj.zu.anjuke.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://beijing.anjuke.com/?pi=PZ-baidu-pc-all-biaoti",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
		},
		
		#我不带着cookie请求
		'COOKIES_ENABLED' :False,
		
		#下载延迟给加上   正常官方文档写的是你写的秒数 0.5到1.5倍
		'DOWNLOAD_DELAY' :1,
		
		#图片字段
		'IMAGES_UR;S_FIELD' : 'image_path',
		
		#图片路径 images是我自己建的文件夹
		'IMAGES_STORE':os.path.join(Base_dir,'images'),
		
		#图片pipelines
		'ITEPIPELINES':{
          'scrapy_04.pipelines.HouseImagePipeline' :1,
		}
			
	}
	
	#构建首次请求    把这个上面的starturl 给注释掉 自己重新写
	#def start_requests(self):
		#base_url='https://bj.zu.anjuke.com/'
	     #yield  scrapy.Request(url=base_url)
	     
	 
	#解析首次请求   之后做循环分页请求
	def parse(self,response):
		for i in range(50,0,-1):
			fullurl=self.base_url%i
			yield scrapy.Request(url=fullurl,callback=self.parsePage)
			
	#解析循环分页请求
	def parsePage(self,response):
		#找到页里面的每一个房源链接，之后返回链接列表
		detail_url = response.xpath('//div@class="zu-itemmod  "/@link).extract()
		for  url detail_url:
			yield scrapy.Request(url=fullurl,callback = self.parseDetail)
	#对详情页进行解析 		
	def parseDetail(self,response):
		hid_pat=re.compile(r'fangyuan/(\d+)')
		res = hid_pat.search(response.url)
		 #获取详情页信息  这里注意的是返回的的是对象 需要extract()之后变成列表之后取片变成字符串
         title = response.xpath('//div[@class="wrapper"]//h3/text()').extract()[0].strip()
         money = response.xpath('//span[@class="f26"]/text()').extract()[0].strip()
         rent_type = response.xpath('//div[@class="litem fl"]/dl[2]/dd[1]/text()').extract()[0].strip()
         house_type = response.xpath('//div[@class="litem fl"]/dl[3]/dd/text()').extract()[0].strip()
         area = response.xpath('//div[@class="ritem fr"]/dl[3]/dd/text()').extract()[0].strip()
         location = response.xpath('//div[@class="litem fl"]/dl[5]/dd/a/text()').extract()[0].strip()
         level = response.xpath('//div[@class="ritem fr"]/dl[5]/dd/text()').extract()[0].strip()
		
		#图片
		images = response.xpath('//div[@class="picCon"]/ul[@class="picMove cf"]/li/a/img/@src').extract()
		
		#过滤图片给数据库存个图片路径长串列表
		image_path = [ for image in images if  '600*450' in image]

         item['hid']=hid
         item['title']=title
         item['monet']=money
         item['rent_type']=rent_type
         item['house_type']=house_type
         item['area']=area
         item['location']=location
         item['level']=level
         item['image_path']=image_path
         
         import uuid  重复的概率亿分之一
         #自己下载图片 这里需要给单独加headers
         #先定义一个很多图片文件名列表从数据库里取好取
         fname_list=[]
         #遍历每个url  
         #for  url in image_path:
         	#给图片处理加上码加上后坠 之后成立图片名
         	#fname=str(uuid.uuid4())+'.jpg'
         	#下载图片拼凑路径
         	#request.urlretrive(url,os.path.join(Basedir,'images/')+fname)
         	#fname_list.append(fname)
         #存进去的是处理好的图片   
         #很多.jpg 并用管道符|链接的字符串  之后你取的时候好取 直接split方法就行 按照管道符切开
        
         #item['image_path']='|'.join(fname_list)
         
         yield item

		   
		
```

**items.py**

```
import scrapy

class HouseItem(scrapy.Item):
	 hid = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    rent_type = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    location = scrapy.Field()
    level = scrapy.Field()
    #image路径字段
    image_path=scrapy.Field()
    
  
```



**middleware.py 给它加个随机代理**

```
class RandomProxy(object):
	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
		self.cursor=self.conn.cursor()
	def process_request(self,request,spider):
		#随机从数据库获取代理
		sql='select * from xici order by rand() limit 1'
		try:
			self.cursor.excute(sql)
			proxy=self.cursor.fetchone()
			proxy='http://%s:%d'%(proxy[1],proxy[2])
		 #设置代理
             request.meta['proxy']=proxy
         except Exception as e :
           	 print(e)

```

**pipelines.py**

```
#图片单独写一个pipeline  在这取出item  通过result 
class  HouseImagePipeline(ImagePipeline):
	def item_completed(self,results,item,info):
		print(results)
		return  item
```

**setting.py**

```
ITEM_PIPELINIES={
   #图片pipeline 
  'scrapy_03.pipelines.HouseImagePipeline'
  #数据pipeline没写呢
}
```

、

### 2.7 百度ip测试随机代理

scrapy genspider baiduip baidu.com

**爬虫文件 baiduip.py**	

```
import  scrapy

class BaiduipSpider(scrapy.Spider):
	name='baiduip'
	allowed_domains = ['baidu.com']
	start_urls = ['http://baidu.com/s?wd=ip']
	
	def parse(self,response):
		print(response.text)
```

**middleware.py**

```
#随机代理  
import pymysql
class RandomProx(object):
	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root,'123456','pachong',charset='utf8')
		self.cursor=self.conn.cursor()
	def process_request(self,request,spider):
		sql='select * from xici order by rand() limit 1'
		try:
			self.cursor.excute(sql)
			proxy=self.cursor.fetchone()
			proxy='http://$s:%d'%(proxy[1],proxy[2])
			request.meta['proxy']=proxy
		except  Exception as  e:
			print(e)
```

**setting.py**

```
DOWNLOADER_MIDDLEWARES = {
#代理中间件设置 
  'scrapy_04.middlewares.RandomProxy':1
}
```

**main.py**

```
from scrapy  import  cmdline 
cmdline.excute('scrapy crawl baiduip'.spilt())

```



### 2.8 文章爬取

**创建爬虫 : scrapy genspider wenzhang cnblogs.com**

```
import  scrapy

class WenzhangSpider(scrapy.Spider):
	name='wenzhang'
	allowed_domains = ['cnblogs.com']
	start_urls =  ['http://www.cnblogs.com/']
	
	base_url = 'https://www.cnblogs.com/p%d/'
	#这个是响应是start url的响应  我不做任何操作
	def parse(self,response):
		for i in  range(10,0,-1):
			fullurl = self.base_url % i
			yield scrapy.Request(url=fullurl,callback=self.Parse)
			
	def parsePage(self,response):
		#抓取整个文章div
		article = response.xpath('//div[@id="post_list"]/div')
		for  everyarticle  in  article :
			#获取链接
			link = everyarticle.xpath('.//div[@class="post_item_body"]/h3/a/@href').extract()[0].strip()
			tile = everyarticle.xpath('.//div[@class="post_item_body"]/h3/a/text()').extract()[0].strip()
			#获取文章id  为了让它到数据库里当主键
			id_pat = re.compile(r'(\d+).html')
			res = id_pat.search(link)
			if  res is  not None:
				aid = res.group(1)
				nick=everyarticle.xpath('.//div[@class="post_item_foot"]/a/text()').extract()[0].strip()
                  date_=everyarticle.xpath('.//div[@class="post_item_foot"]/text()').extract()[1].strip().strip('发布于')
                  tuijian=everyarticle.xpath('.//div[@class="diggit"]/span[@class="diggnum"]/text()').extract()[0].strip()
                  comment=everyarticle.xpath('.//div[@class="post_item_foot"]/span/a/text()').extract()[0].strip()
                  comment=self.getNum(comment)
                  readnum=everyarticle.xpath('.//span[@class="article_view"]/a/text()').extract()[0].strip()
                  readnum=self.getNum(readnum)
                  industry=everyarticle.xpath('.//p[@class="post_item_summary"]/text()').extract()
                  industry=''.join(industry).strip()
                
               	  #给放到item 中
               	  item['title']=title
               	  item["aid"] = aid
                  item["nick"] = nick
                  item["date_"] = date_
                  item["tuijian"] = tuijian
                  item["comment"] = str(comment)
                  item["readnum"] = str(readnum)
                  item["industry"] = industry
                  
                  #对抓取的每一个详情文章链接请求
                  #meta  把数据传过去  通过meta传递给过去item
                  yield  scrapy.Request(url=link,callback=self.parseDetail,meta={'data',item})
                  
     def parseDetail(self,response):
     	from  w3lib.html import  remove_tags
     	item=response.meta['data']
     	return  item
     	
     def getNum(self,value)
     	import re
     	pat = re.compile(r'\d')
     	res = pat.search(value)
     	if  res is not None:
     		res = int(res.group())
     	else:
     		res =0
     		
     	return res 

		
```



**items.py**

```

import scrapy
class articleItem(scrapy.Item):
    aid = scrapy.Field()
    title = scrapy.Field()
    nick = scrapy.Field()
    date_ = scrapy.Field()
    tuijian = scrapy.Field()
    comment = scrapy.Field()
    readnum = scrapy.Field()
    industry = scrapy.Field()
    images=scrapy.Field()
	def get_sql(self):
		sql='insert into yanl(aid,comment,adate,nick,readnum,title,tuijian) values(%s,%s,%s,%s,%s,%s,%s)'
		data = [
        	self['aid'],self['comment'],self['date_'],self['nick'],self['readnum'],self['title'],self['tuijian']
		]
		return  sql ,data
		
		
```

**pipelines.py**

```
import  pymysql 
class articlePipeline(object):
	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root','123456','pachong',charset='utf8')
		self.cursor=self.conn.cursor()
	def process_request(self,item,spider):
		sql,data=get_sql()
		try:
			self.cursor.excute(sql,data)
			self.conn.commit()
		except  Exception as  e :
			print('sql:{}\ndata:{}'.format(sql,data))
			self.conn.rollback()
		return  item
		
	def close_spider(sql,spider):
		self.cursor.close()
		self.conn.close()
```

**settings.py**

```
ITEM_PIPELINES = {

    'scrapy_04.pipelines.articlePipeline': 1,

}
```





## 3. 全站式爬取

**创建spider：**scrapy genspider -t crawl 爬虫名 二级域名

### 3.1  博客园

**spider.py**

```
import scrapy

from scrapy.linkextractors import  LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class BokeyuanSpider(CrawlSpider):
	name='bokeyuan'
	#有效域
	allowed_domains=['cnblog.com']
	#全站爬取的start_url  要给
	start_urls=['http://www.cnblogs.com/']
	
	rules  = (
	Rule(LinkExtractor(allow=r'/cate/(.*?)'),follow=True),
	
	#回掉parse_item  而且要给字符串forse 遇到这个正则就进去并开始解析，True也进但是 不解析  Rule(LinkExtractor(allow=r'https://www.cnblogs.com/(.*?)'),callbackt='parse_item',follow=False),
	)
	
	#这个函数来解析直接（暂时理解，至少不会报错） 和分布式有些区别  分布式可以在回掉里重新发请求 继续再写一层回掉函数 可以忽略第一个响应
	def parse_item(self,response):
		print(response.status)
         print(response.css('title::text').extract()[0])
         
```

**main.py**

```
from scrapy import cmdline 
cmdline.excute('scrapy crawl bokeyuan'.split())
```



### 3.2 拉钩全站式爬取

**spider.py**

```
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider,Rule
#  这个能把数字给转成时间日期格式 2 days, 12:00:00  能和datetime.datetime.now()进行相加减
from datetime import timedelta
import datetime
import  hashlib
from quanzhan.items import  lagouItem
class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/']
	
	#给这个爬虫单设一个settings 比较好管理
	 custom_settings ={
	 	#不带着cookie去发请求
        'COOKIES_ENABLED': False,
        
        #并发数
		'CONCURRENT_REQUESTS' : 2,
        #设置pipeline
        'ITEM_PIPELINES ': {
        'quanzhan.pipelines.lagouPipeline': 1,
        },
		#下载延迟
         'DOWNLOAD_DELAY': 1,
		
		#请求头
        'DEFAULT_REQUEST_HEADERS': {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_ga=GA1.2.1587002519.1516604272; user_trace_token=20180122145755-928bf659-ff41-11e7-a5a8-5254005c3644; LGUID=20180122145755-928bf9dc-ff41-11e7-a5a8-5254005c3644; _gid=GA1.2.61027638.1516604272; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; LGSID=20180122201822-56bf358b-ff6e-11e7-b57c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3806601.html; SEARCH_ID=951b9979f1994fb884b3d7ecb7b2713e; X_HTTP_TOKEN=b311c674f86a8be5a1a15bc2faae3077; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516609588,1516611219,1516613839,1516623669; JSESSIONID=ABAAABAAAFCAAEG8573CBF62464F2A802E12F849F814596; _putrc=E6BDB358BE74D814; login=true; unick=%E6%9D%8E%E5%BD%A6%E8%89%AF; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=f79e87e0fd7cf7f42ff858752941ac6da64729790436efeb; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516623980; LGRID=20180122202624-75f78df8-ff6f-11e7-b58e-525400f775ce"


        }
   }
   
   #写好rule规则
    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+'),  follow=True),
        # xiaoyuan.lagou.com/
        Rule(LinkExtractor(allow=r'jobs/xiaoyu\.lagou\.com'),  follow=True),

        Rule(LinkExtractor(allow=r'jobs/list.*'), follow=True),


        Rule(LinkExtractor(allow=r'jobs/\d+\.html'), callback='parse_item', follow=False),
    )
    
    def parse_item(self,response):
    	item=lagouItem()
        #获取jid  来存数据库 做唯一索引
        jid=response.url
        jid=self.md5(jid)
        title=response.xpath('//div[@class="job-name"]/span/text()').extract()[0]
        salary=response.xpath('//div/dd[@class="job_request"]/p/span[1]/text()').extract()[0]
        city=response.xpath('//div/dd[@class="job_request"]/p/span[2]/text()').extract()[0]
        city=self.quchu_slash(city)
        exp=response.xpath('//div/dd[@class="job_request"]/p/span[3]/text()').extract()[0]
        exp=self.quchu_slash(exp)
        degree=response.xpath('//div/dd[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree=self.quchu_slash(degree)
        tags=response.xpath('//dd[@class="job_request"]/ul/li/text()').extract()[0]

        publish_time=response.xpath('//p[@class="publish_time"]/text()').extract()[0]
        publish_time=self.process_date(publish_time)
        youhuo=response.xpath('//dd[@class="job-advantage"]/p/text()').extract()[0]
        duty=response.xpath('//dd[@class="job_bt"]/div/p//text()').extract()
        duty=''.join(duty)
        workposition=response.xpath('//div[@class="work_addr"]/text()').extract()[-2].split('-')[1].strip('\n').strip('                                                            ')
        company = response.xpath('//h2[@class="fl"]/text()').extract()[0].strip()

        print(title,salary,city,exp,degree,tags,publish_time,youhuo,duty,workposition,company,jid)

        item["jid"] = jid
        item["title"] = title
        item["salary"] = salary
        item["city"] = city
        item["exp"] = exp
        item["degree"] = degree
        item["tags"] = tags
        item["publish_time"] = publish_time
        item["youhuo"] = youhuo
        item["duty"] = duty
        item["workposition"] = workposition
        item["company"] = company

        yield  item
        
    def  quchu_slash(self,value)：
    	return value.strip('/')
    	
    def process_date(self,value):
    	value=value.replace('\xa0','').strip('发布于拉钩网')
    	try:
    		if '天前' in value:
    			days=int(value.strip('天前'))
    			#1 day, 0:00:00  输出结果 来进行和日期时间相加减 
    			days=timedelta(days=days)
    			#datetime.datetime.now()日期时间格式精确到毫秒
    			#拿它和这个timedelta换算出来的来进行相减
    			res = datetime.datetime.now()-days
    			#直接要年月日
    			res = res.strftime('%Y-%m-%d')
    		else:
    			res=value
    		return res
    	except Exception as e:
    		print(e)
    		
      def md5(self,value):
      	md5=hashlib.md5()
      	md5.update(bytes(value,encoding='utf-8'))
      	#32位的哈希加密编码 字符串类型
      	return md5.hexdigest()	
    		
```



**item.py  字段 继承scrapy.Item spider.py 需要导入**

```
class  lagouItem(scrapy.Item):
    jid=scrapy.Field()
    title=scrapy.Field()
    salary=scrapy.Field()
    city=scrapy.Field()
    exp=scrapy.Field()
    degree=scrapy.Field()
    tags=scrapy.Field()
    publish_time=scrapy.Field()
    youhuo=scrapy.Field()
    duty=scrapy.Field()
    workposition=scrapy.Field()
    company=scrapy.Field()
    spider=scrapy.Field()

    def get_sql(self):
        sql='insert into lagou(jid,title,salary,city,exp,degree,tags,publish_time,youhuo,duty,workposition,company) values' \
            '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data=[
            self['jid'],self['title'],self['salary'],self['city'],self['exp'],self['degree'],self['tags'],self['publish_time'],
            self['youhuo'],self['duty'],self['workposition'],self['company']
        ]
```

**pipelines 存储**

```
import  pymysql 
class lagouPipeline(object):
	def __init__(self):
		self.conn=pymysql.connect('127.0.0.1','root','pachong',charset='utf8')
		self.cursor=self.conn.cursor()
		#传spider 是为了关闭爬虫
	def process_item(self,item,spider):
		sql,data=item.get_sql()
		try:
			self.cursor.execute(sql,data)
			print('sql:{}\ndata:{}'.format(sql,data))
			self.conn.commit()
		except Exception as e :
			print('没成功')
			print(e)
			self.conn.rollback()
		return  item
		
	def close_spider(self):
		self.cursor.close()
		self.conn.close()
```

**main.py**

```
from  scrapy import  cmdline

cmdline.execute('scrapy crawl lagou'.split())

```



### 3.3  scrapy renren.py post提交密码登陆

```
import scrapy
class RenrenSpider(scrapy.Spider):
	name='renren'
	allowed_domains = ['renren.com']
	#重写初次请求函数
	def start_requests(self):
		login_url='http://www.renren.com/PLogin.do'
		data={
          'email':'1752570559@qq.com',
          'password':'1234qwer',
		}
		headers={}
		yield scrapy.FormRequest(url=login_url,formdata=data,headers=headers)
		
	def parse(self,response):
		print(response.text)
		
		
```

### 3.4 scrapy  renren1.py带着cookie登陆

```
import scrapy
class RenrenSpider(scrapy.Spider):
	name='renren1'
	allowed_domains=['renren.com']
	#随便给个其实url  之后第一次回掉无所谓  我重新发请求就好阿
	start_urls=['http://www.baidu.com']
	headers={
         "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.renren.com/",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        #这里注意cookie拿出来单写了
        #cookie
	}
	def parse(self,response):
		home_url='http://www.renren.com/440906810'
		yield scrapy.Request(url=home_url,callback=self.parse_home,headers=self.headers,cookie=self.cookie)
	
	def parse_home(self,response):
		print(response.text)
	
	
```

###  3.5 taobao手机页面抓取

```
import  scrapy
import re
import  json 
import  jsonpath
class TaobaoSpider(scrapy.Spider)：
	name='taobao'
	allowed_domains = ['taobao.com']
	#请求淘宝手机列表页
	base_url = 'https://s.taobao.com/search?q=手机&s=%d'
	def parse(self,response):
		for i  in range(0,4752+1,48):
			fullurl=self.baseurl % i 
			yield scrapy.Request(url=fullurl,callback=self.parseList)
			
	def parseList(self,response):
		#由于给返回的源代码没有数据  所以需要正则匹配 需要先网页查看源代码
		#之后再用jsonpath 来提取  忽略换行 re.S
		pat=re.compile(r'g_page_config = (.*?)g_srp_loadCss',re.S)
		res=pat.search(response.text)
		if  res is  not None:
			data=res.group(1).strip(';\n   ')
			#$..从根节点下的所有元素中查找spus sups 节点下的全部
			res = jsonpath.jsonpath(json.loads(data),'$..spus.*')
			#如果有 解析数据
              if res :
              	for  item in res :
              		print(item)
```



### 3.6 设置爬取优先级

```
    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'),follow=True),
        # Rule(LinkExtractor(allow=r'jobs/list_.*'), follow=True),
        #一定要技术这个优先级参数  
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=False,process_request='pr'),
    )


#设置follow链接解析的优先级 正常不是crawl全站(scrapy.Spider)的是在 scrapy.Request的参数来设置priority=
#这里是全站的 看到我想要的了就解析   不用非得等url全请求完再解析  数越大优先级越高 
def pr(self,request):
	request.priority=1
	return  request
```



## 4. scrapy分布式爬虫

**理解：** 分布式爬虫架构实际上就是由一台主机维护所有的爬取队列，每台从机的sheduler(调度器)共享该队列，协同存储提取 。分布式爬虫的多台协作的关键是共享爬取队列。



**队列怎么维护呢？:**1.推荐redis队列 redis是非关系型数据库，用key-value形式存储，结构灵活，他不像关系型数据库必须要由一定的结构才能存储

2.key-value 可以是多种数据，非常灵活

3.另外redis是内存中的数据结构存储系统，处理速度快，性能好

4.提供了队列，集合()多种存储结构，方便队列维护和去重操作.



**怎么样去重？** **如果多台机器不仅往请求队列存，还同时从里面取，那么如何保证每台机子请求和存储的队列是不重复的呢？**

1.借助redis集合

redis 提供集合数据结构，我们知道集合里面的元素是不重复的

首先，在redis中存储每个reques的指纹 ，在向request队列中加入request前首先验证这个request的指纹是否已经加入到集合中，如果已存在，则不添加requests到队列 。如果不存在，则将request添加入列并将指纹加入集合

```
也就是说 留下指纹到集合中  进队列 新的按指纹（验证了没有 则按） 老的录指纹
```

**(请求对象request //一个Request对象表示一个HTTP请求，它通常是在爬虫生成，并由下载执行，从而生成Response。 ），**



//请求对象详解 request object

```
一个Request对象表示一个HTTP请求，它通常是在爬虫生成，并由下载执行，从而生成Response。

参数：

url（string） - 此请求的网址

callback（callable） - 将使用此请求的响应（一旦下载）作为其第一个参数调用的函数。有关更多信息，请参阅下面的将附加数据传递给回调函数。如果请求没有指定回调，parse()将使用spider的 方法。请注意，如果在处理期间引发异常，则会调用errback。

method（string） - 此请求的HTTP方法。默认为'GET'。

meta（dict） - 属性的初始值Request.meta。如果给定，在此参数中传递的dict将被浅复制。

body（str或unicode） - 请求体。如果unicode传递了a，那么它被编码为 str使用传递的编码（默认为utf-8）。如果 body没有给出，则存储一个空字符串。
不管这个参数的类型，存储的最终值将是一个str（不会是unicode或None）。
headers（dict） - 这个请求的头。dict值可以是字符串（对于单值标头）或列表（对于多值标头）。如果 None作为值传递，则不会发送HTTP头。

cookie（dict或list） - 请求cookie。这些可以以两种形式发送。
```



**怎么样防止中断**

```
怎样防止中断？
在爬取的过程中，难免会有某台机子卡掉了，这时怎么办？
在每台从机scrapy启动时都会首先判断当前redis request队列是否为空。
如果不为空，则从队列中取得下一个request执行爬取。
如果为空，则重新开始开始爬取，第一台从机执行爬取想队列中添加request。

```



**怎样实现架构?**

```
要做到：
维护request队列
对台从机调度reuqest
设置去重
链接redis

已经有了比较成熟的库scrapy-redis

scrapy-redis库实现了如上架构，改写了scrapy的调度器，队列等组件
```



**分布式爬虫三种策略**

```
前言：
爬虫是偏IO型的任务，分布式爬虫的实现难度比分布式计算和分布式存储简单得多。 
个人以为分布式爬虫需要考虑的点主要有以下几个：

爬虫任务的统一调度
爬虫任务的统一去重
存储问题
速度问题
足够“健壮”的情况下实现起来越简单/方便越好
最好支持“断点续爬”功能
Python分布式爬虫比较常用的应该是scrapy框架加上Redis内存数据库，中间的调度任务等用scrapy-redis模块实现。 
此处简单介绍一下基于Redis的三种分布式策略，其实它们之间还是很相似的，只是为适应不同的网络或爬虫环境作了一些调整而已（如有错误欢迎留言拍砖）。 

【策略一】
分布式爬虫策略一
Slaver端从Master端拿任务（Request/url/ID）进行数据抓取，在抓取数据的同时也生成新任务，并将任务抛给Master。Master端只有一个Redis数据库，负责对Slaver提交的任务进行去重、加入待爬队列。

优点： scrapy-redis默认使用的就是这种策略，我们实现起来很简单，因为任务调度等工作scrapy-redis都已经帮我们做好了，我们只需要继承RedisSpider、指定redis_key就行了。 
缺点： scrapy-redis调度的任务是Request对象，里面信息量比较大（不仅包含url，还有callback函数、headers等信息），导致的结果就是会降低爬虫速度、而且会占用Redis大量的存储空间。当然我们可以重写方法实现调度url或者用户ID。 

【策略二】
分布式爬虫策略二
这是对策略的一种优化改进：在Master端跑一个程序去生成任务（Request/url/ID）。Master端负责的是生产任务，并把任务去重、加入到待爬队列。Slaver只管从Master端拿任务去爬。

优点： 将生成任务和抓取数据分开，分工明确，减少了Master和Slaver之间的数据交流；Master端生成任务还有一个好处就是：可以很方便地重写判重策略（当数据量大时优化判重的性能和速度还是很重要的）。 
缺点： 像QQ或者新浪微博这种网站，发送一个请求，返回的内容里面可能包含几十个待爬的用户ID，即几十个新爬虫任务。但有些网站一个请求只能得到一两个新任务，并且返回的内容里也包含爬虫要抓取的目标信息，如果将生成任务和抓取任务分开反而会降低爬虫抓取效率。毕竟带宽也是爬虫的一个瓶颈问题，我们要秉着发送尽量少的请求为原则，同时也是为了减轻网站服务器的压力，要做一只有道德的Crawler。所以，视情况而定。 

【策略三】
分布式爬虫策略三
Master中只有一个集合，它只有查询的作用。Slaver在遇到新任务时询问Master此任务是否已爬，如果未爬则加入Slaver自己的待爬队列中，Master把此任务记为已爬。它和策略一比较像，但明显比策略一简单。策略一的简单是因为有scrapy-redis实现了scheduler中间件，它并不适用于非scrapy框架的爬虫。

优点： 实现简单，非scrapy框架的爬虫也适用。Master端压力比较小，Master与Slaver的数据交流也不大。 
缺点： “健壮性”不够，需要另外定时保存待爬队列以实现“断点续爬”功能。各Slaver的待爬任务不通用。 

结语：
如果把Slaver比作工人，把Master比作工头。策略一就是工人遇到新任务都上报给工头，需要干活的时候就去工头那里领任务；策略二就是工头去找新任务，工人只管从工头那里领任务干活；策略三就是工人遇到新任务时询问工头此任务是否有人做了，没有的话工人就将此任务加到自己的“行程表”。 
```

### 

### 4.0 分布式代码自总结思路

```
1.确定目标
2.创建Scrapy.spider类 (命令scrapy genspider 爬虫名 二级域名 **.com)
3.锁定起始url 写上有效域
4.正常爬 parse回掉函数 因为继承是Scrapy.spider 类
5.爬到数据
6.之后改成RedisSpider 来实现分布式  
	start_url需要注释掉  
	之后改写成redis_key  写键  之后程序运行起来   
	命令行push进去一个url  
	并且redis配置   配置调度器等等 链接数据库  pipline进行设置
	
7.CrawlSpider 正常全站爬取 rule规则  回掉必须是parse_item 而且callback是字符串 也能链接redis 
而且全站爬取有个process_request=‘pr’参数,这个参数是设置follow解析的优先级
正常不是crawl全站的是在scrapy.Request的参数来设置(priority=)
def pr(self,request)：
	request.priority=1
	return request 
8. CrawlRedisSpider 全站分布式爬取  回掉必须要写parse_item 而且参数在rule规则里是字符串  这个也要写redis_key 之后不写start_url 然后程序运行起来push进去  配置redis

#总结: 全站CrawlSpider
	  正常分布式RedisSpider
	  全站分布式RedisCrawSpider 
	
#追加一点 第一次push进去的url 对其可以直接进行回掉函数解析
也可以不管它 在自己写baseurl 直接发请求  反正就是走到这个函数了 你干什么随意
	

```



### 4.1 一步步最后实现分布式代码实现

**课堂笔记分布式爬虫升级步骤**

```
分布式爬虫升级步骤
1.redis服务正常开启，正常链接
2.先用scrapy写爬虫项目
3.settings
	#过滤系统设置为scrapy-redis的过滤器
	DUPEFILER_CLASS = "scrapy_redis.dupefilter.PFDoupeFilter"
	#调度器
	SCHEDULER="scrapy_redis.scheduler.Scheduler"
	#是否可以暂停爬虫
	SCHEDULER_PERSIST  = True
	#请求队列模式
	#按优先级调度，priority  数字越大，优先级越高
	SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
	#先进先出队列
	SCHEDULER_QUEUE_CLASS ="scrapy_redis.queue.SpiderQueue"
	#先进后出
	SCHDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
	
	#数据存储到redis中
	ITEM_PIPELINES = {
        'example.pipelines.ExamplePipeline':300
    'scrapy_redis.pipelines.RedisPipeline':999
	}
	
	#redis链接信息
	REDIS_HOST = '127.0.0.1'
     REDIS_PORT = 6379
	
```

**1.fenbu1.py**

//创建项目：scrapy genspider -t crawl fenbu1

```
from scrapy.linkextractors import LinkExtractor

from scrapy.spider import CrawSpider,Rule

class Fenbu1Spider(CrawlSpider):
	name = 'fenbu1'
	allowde_domains = []
	start_urls=['https://www.hao123.com/']
	rules = [
#LinkExtractor 如果填写空 则全站抽取被follow的链接对象   False提取到的所有都拿内容  True则不拿      Rule(LinkExtractor(),callback='parse_directory',follow=False)
	]
	def parse_directory(self,response)
	title=response.css('title::text').extract()[0]
	yield{
      'title':title
	}
#全站链接redis了

#pipeline.py
class FenbushiPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
        


```



**setting.py**

```

# 分布式

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 过滤系统设置为scrapy-redis的过滤器
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"


# 是否可以暂停爬虫
SCHEDULER_PERSIST = True

# 请求队列模式
# 按优先级调度请求,priority 数字越大，优先级越高
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 先进先出队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


# 数据存储到redis中
ITEM_PIPELINES = {
    #分布式3个进阶pipeline
     'fenbushi.pipelines.FenbushiPipeline': 2,
    #拉钩pipeline
    # 'fenbushi.pipelines.lagouPipeline':1,
    #这行代码直接存 redis里了 管道存储
    'scrapy_redis.pipelines.RedisPipeline': 1,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# redis连接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
```

**2.fenbu2.py**

****

```
#rules:是Rule对象的集合，用于匹配目标网站并排除干扰
from scapy.spider import Rule

#LinkExtractors 适用于从网页(scrapy.http.Response)中抽取会被follow的对象
from scrapy.linkextractor  import LinkExtractor

#类爬虫继承了RedisCrawlSpider
#RedisCrawlSpider 能够支持分布式的抓取。因为采用的是crawlSpider,所以需要遵守Rule规则，以及callback不能写parse()方法



class Fenbu2Spider(RedisCrawSpider):
	name='fenbu2'
	#这个是redis的键
	#值的类型是list  命令行里  给这个网址 加入队列lpush mycrawler http://www.hao123.com
	redis_key='redisjian'
	#rules是对象的集合  用于匹配目标网站 因为集合无序性
	rules = (
	Rule(LinkExtractor(),callback='parse_page',follow=True),
	)
	def parse_page(self,response):
		return {
          'name':response.css('title::text').extract_first(),
          'url':response.url
		}
		
		
		
	
	
```

**pipelines 分布式两个pipeline 如果存储爬虫名字的话 一个是Redispipline 一个是 正常Pipeline**

```
from datetime import datetime

class FenbushiPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
        

```

**setting设置**#

```
#别的没写   ，就写了些新的分布式设置
USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#过滤系统设置为scrapy-redis的过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 是否可以暂停爬虫
SCHEDULER_PERSIST = True

# 请求队列模式
# 按优先级调度请求,priority 数字越大，优先级越高
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 请求队列模式
# 按优先级调度请求,priority 数字越大，优先级越高
# 分布式只需 加这个参数就ok  设置优先级   如果全站式 也有priority优先级
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 先进先出队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 数据存储到redis中
ITEM_PIPELINES = {
    #分布式3个进阶pipeline
     'fenbushi.pipelines.FenbushiPipeline': 2,
    #这行代码直接存 redis里了 管道存储
    'scrapy_redis.pipelines.RedisPipeline': 1,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# redis连接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379



```

**3.fenbu3.py**

```
‘’‘
爬虫任务的统一调度，爬虫任务的统一去重，存储问题，速度问题，足够健壮的情况下实现起来越简单/方便越好,最好支持断电续爬功能
'''
from scrapy_redis.spiders import RedisSpider
import  scrapy
class Fenbu3Spider(RedisSpider):
	name='fenbu3'
	#我设置了一个键值对
	#这个在运行的时候需要把两个都push进队列里
	#lpush wo:start_url  http://www.hao123.com
	redis_key='wo:start_urls'
	
	def parse(self,response):
		#得到响应内容  去里面匹配url  组成url列表
		url_list = response.xpath('//a/@href').extract()
		#遍历每一个url 
		for url  in  url_list:
			if 'http' in  url   or  'https' in url :
				print(url)
				#那么我来发请求  在响应的内容用我的回掉函数
				yield scrapy.Request(url=url,callback=self.parsePage)
				
	def  parsePage(self,respose):
		#取出响应内容的  数据
		return {
          'name':response.css('title::text').extract_first()
		}
		

				
```



**setting.py**

```
# 分布式

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 过滤系统设置为scrapy-redis的过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 是否可以暂停爬虫
SCHEDULER_PERSIST = True

# 请求队列模式
# 按优先级调度请求,priority 数字越大，优先级越高
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 先进先出队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


# 数据存储到redis中
ITEM_PIPELINES = {
    #分布式3个进阶pipeline
     'fenbushi.pipelines.FenbushiPipeline': 2,
    #拉钩pipeline
   
    #这行代码直接存 redis里了 管道存储
    'scrapy_redis.pipelines.RedisPipeline': 1,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# redis连接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

```

**pipelines.py**

```
#这个给加了两个字段
from datetime import datetime
class FenbushiPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
```



**main.py有所不同**

```
#这个是fenbu3 的
# import  os
# os.chdir('fenbushi/spiders')
# cmdline.execute('scrapy runspider fenbu3.py'.split())
```



### 4.2 全站分布式拉钩

**spider.py**

```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

#  这个能把数字给转成时间日期格式 2 days, 12:00:00  能和datetime.datetime.now()进行相加减
from datetime import timedelta
import datetime
import  hashlib
# rules: 是Rule对象的集合，用于匹配目标网站并排除干扰
from scrapy.spiders import Rule
from  fenbushi .items import  lagouItem
from scrapy_redis.spiders import RedisCrawlSpider
# from quanzhan.items import  lagouItem
class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # 运行之后  敲这个lpush  lagouwang https://www.lagou.com/
    redis_key='lagouwang'


    custom_settings ={
        'COOKIES_ENABLED': False,

         'DOWNLOAD_DELAY': 1,

        'DEFAULT_REQUEST_HEADERS': {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_ga=GA1.2.1587002519.1516604272; user_trace_token=20180122145755-928bf659-ff41-11e7-a5a8-5254005c3644; LGUID=20180122145755-928bf9dc-ff41-11e7-a5a8-5254005c3644; _gid=GA1.2.61027638.1516604272; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; LGSID=20180122201822-56bf358b-ff6e-11e7-b57c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3806601.html; SEARCH_ID=951b9979f1994fb884b3d7ecb7b2713e; X_HTTP_TOKEN=b311c674f86a8be5a1a15bc2faae3077; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516609588,1516611219,1516613839,1516623669; JSESSIONID=ABAAABAAAFCAAEG8573CBF62464F2A802E12F849F814596; _putrc=E6BDB358BE74D814; login=true; unick=%E6%9D%8E%E5%BD%A6%E8%89%AF; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=f79e87e0fd7cf7f42ff858752941ac6da64729790436efeb; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516623980; LGRID=20180122202624-75f78df8-ff6f-11e7-b58e-525400f775ce"


        }
   }



    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+'),  follow=True),
        # xiaoyuan.lagou.com/
        Rule(LinkExtractor(allow=r'jobs/xiaoyu\.lagou\.com'),  follow=True),

        Rule(LinkExtractor(allow=r'jobs/list.*'), follow=True),

        Rule(LinkExtractor(allow=r'jobs/\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item=lagouItem()
        #获取jid  来存数据库 做唯一索引
        jid=response.url
        jid=self.md5(jid)
        title=response.xpath('//div[@class="job-name"]/span/text()').extract()[0]
        salary=response.xpath('//div/dd[@class="job_request"]/p/span[1]/text()').extract()[0]
        city=response.xpath('//div/dd[@class="job_request"]/p/span[2]/text()').extract()[0]
        city=self.quchu_slash(city)
        exp=response.xpath('//div/dd[@class="job_request"]/p/span[3]/text()').extract()[0]
        exp=self.quchu_slash(exp)
        degree=response.xpath('//div/dd[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree=self.quchu_slash(degree)
        tags=response.xpath('//dd[@class="job_request"]/ul/li/text()').extract()[0]

        publish_time=response.xpath('//p[@class="publish_time"]/text()').extract()[0]
        publish_time=self.process_date(publish_time)
        youhuo=response.xpath('//dd[@class="job-advantage"]/p/text()').extract()[0]
        duty=response.xpath('//dd[@class="job_bt"]/div/p//text()').extract()
        duty=''.join(duty)
        workposition=response.xpath('//div[@class="work_addr"]/text()').extract()[-2].split('-')[1].strip('\n').strip('                                                            ')
        company = response.xpath('//h2[@class="fl"]/text()').extract()[0].strip()

        print(title,salary,city,exp,degree,tags,publish_time,youhuo,duty,workposition,company,jid)

        item["jid"] = jid
        item["title"] = title
        item["salary"] = salary
        item["city"] = city
        item["exp"] = exp
        item["degree"] = degree
        item["tags"] = tags
        item["publish_time"] = publish_time
        item["youhuo"] = youhuo
        item["duty"] = duty
        item["workposition"] = workposition
        item["company"] = company

        yield  item
    def quchu_slash(self,value):
        return  value.strip('/')

    #目的替换发布于拉钩网
    def process_date(self,value):
        #字符串替换
        value=value.replace('\xa0','').strip(' 发布于拉钩网')
        try:
            if  '天前' in  value:
                days=int(value.strip('天前'))
                days=timedelta(days=days)
                #datetime.datetime.now()是带后面的秒数 2018-01-22 18:55:13.303471
                #拿它和这个timedelta来进行相减
                res=datetime.datetime.now()-days
                # 加上striftime  则不带  2018-01-22
                res=res.strftime('%Y-%m-%d')

            else:
                res=value
            return res
        except Exception as e :
            print(e)


    def md5(self,value):
        md5=hashlib.md5()
        md5.update(bytes(value,encoding='utf-8'))
        return  md5.hexdigest()
```

**pipelines**

```
class lagouPipeline(object):
    def process_item(self,item,spider):
        item['craweld']=datetime.utcnow()
        item['spider']=spider.name
        return item
```

**setting.py**

```


# 分布式

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 过滤系统设置为scrapy-redis的过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 是否可以暂停爬虫
SCHEDULER_PERSIST = True

# 请求队列模式
# 按优先级调度请求,priority 数字越大，优先级越高
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 先进先出队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


# 数据存储到redis中
ITEM_PIPELINES = {
    #分布式3个进阶pipeline
     'fenbushi.pipelines.FenbushiPipeline': 2,
    #拉钩pipeline
    # 'fenbushi.pipelines.lagouPipeline':1,
    #这行代码直接存 redis里了 管道存储
    'scrapy_redis.pipelines.RedisPipeline': 1,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# redis连接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

```

## 5. 利用分布式做的项目

### **5.0 第一个不是分布式拉钩网 **

```
import  scrapy
from  scrapy.linkextractors import  LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#  这个能把数字给转成时间日期格式 2 days, 12:00:00  能和datetime.datetime.now()进行相加减
from datetime import timedelta
import datetime

from xiangmu.items import  lagouItem

class  LagouSpider(CrawSpider):
	name='lagou'
	allowed_domains=['lagou.com']
	start_urls = ['http://www.lagou.com']
	
	custom_settings = {
    	'COOKIES_ENABLED': False,
        "CONCURRENT_REQUESTS": "5",
         'DOWNLOAD_DELAY': 0,
        'ITEM_PIPELINES' :{
            # 'xiangmu.pipelines.lagouPipeline': 1,
             'scrapy_redis.pipelines.RedisPipeline': 300,
        },

        'DEFAULT_REQUEST_HEADERS': {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_ga=GA1.2.1587002519.1516604272; user_trace_token=20180122145755-928bf659-ff41-11e7-a5a8-5254005c3644; LGUID=20180122145755-928bf9dc-ff41-11e7-a5a8-5254005c3644; _gid=GA1.2.61027638.1516604272; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; LGSID=20180122201822-56bf358b-ff6e-11e7-b57c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3806601.html; SEARCH_ID=951b9979f1994fb884b3d7ecb7b2713e; X_HTTP_TOKEN=b311c674f86a8be5a1a15bc2faae3077; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516609588,1516611219,1516613839,1516623669; JSESSIONID=ABAAABAAAFCAAEG8573CBF62464F2A802E12F849F814596; _putrc=E6BDB358BE74D814; login=true; unick=%E6%9D%8E%E5%BD%A6%E8%89%AF; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=f79e87e0fd7cf7f42ff858752941ac6da64729790436efeb; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516623980; LGRID=20180122202624-75f78df8-ff6f-11e7-b58e-525400f775ce"


        }
   }


   rulse=(
   Rule(LinkExtractor(allow=r'zhaopin/.*),follow=True),
   Rule(LinkEXtractor(allow=r'gongsi/'),follow=True),
   Rule(LinkEXtractor(allow=r'jobs/xiaoyu\.lagou\.com'),follow=True),
   Rule(LinkExtractor(allow=r'jobs/\d+\.html'), callback='parse_item', follow=False),
   )
   
   def parse_item(self,response):
       item=lagouItem()
       url=response.url
       #职位名
       if  'lagou' in url:
            comefrom='来源于拉钩网'
        else:
            comefrom='未知'
        positionname=response.xpath('//div[@class="job-name"]/span/text()').extract()[0]
        #薪水
        salary=response.xpath('//div/dd[@class="job_request"]/p/span[1]/text()').extract()[0]
        if salary:
            salary=salary.split('-')
            lowsalary=int(salary[0].strip('k'))*1000
            highsalary=int(salary[1].strip('k '))*1000


        else:
            salary='无'
        #职位描述
        positiondescription=response.xpath('//dd[@class="job_bt"]/div/p//text()').extract()
        positiondescription=''.join(positiondescription)

        #职位地点
        positionaddress=response.xpath('//div[@class="work_addr"]/text()').extract()[-2].split('-')[1].strip('\n').strip('                                                            ')
        #发布时间
        published=response.xpath('//p[@class="publish_time"]/text()').extract()[0]
        published=self.process_date(published)


        #学历
        degree=response.xpath('//div/dd[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree=self.quchu_slash(degree)

        #职位诱惑
        treatment=response.xpath('//dd[@class="job-advantage"]/p/text()').extract()[0]

        #公司名
        company = response.xpath('//h2[@class="fl"]/text()').extract()[0].strip()

        #工作城市
        city=response.xpath('//div/dd[@class="job_request"]/p/span[2]/text()').extract()[0]
        city=self.quchu_slash(city)

        #工作经验
        exp=response.xpath('//div/dd[@class="job_request"]/p/span[3]/text()').extract()[0]
        exp=self.quchu_slash(exp)


        #技能标签
        tag=response.xpath('//dd[@class="job_request"]/ul/li/text()').extract()[0]


        item["url"] = url
        item["positionname"] = positionname
        item["lowsalary"] = lowsalary
        item["highsalary"] = highsalary

        item["positiondescription"] = positiondescription
        item["positionaddress"] = positionaddress
        item["published"] = published
        item["degree"] = degree
        item["treatment"] = treatment
        item["company"] = company
        item["city"] = city
        item["exp"] = exp
        item["tag"] = tag
        item['comefrom']=comefrom
        yield  item


    def quchu_slash(self,value):
        return  value.strip('/')

    #目的替换发布于拉钩网
    def process_date(self,value):
        #字符串替换
        value=value.replace('\xa0','').strip(' 发布于拉钩网')
        try:
            if '天前' in value:
                days = int(value.strip('天前'))
                days = timedelta(days=days)
                # datetime.datetime.now()是带后面的秒数 2018-01-22 18:55:13.303471
                # 拿它和这个timedelta来进行相减
                res = datetime.datetime.now() - days
                # 加上striftime  则不带  2018-01-22
                res = res.strftime('%Y-%m-%d')

            else:
                res = value
            return res
        except Exception as e:
            print(e)



       
```



**piplines.py**

```
class  lagouPipeline(object):
    def process_item(self, item, spider):
        return item
```



### 5.1 案例1  zhilian

```
# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule

from scrapy_redis.spiders import RedisCrawlSpider
from  xiangmu.items import  zhilianItem
class ZhilianSpider(RedisCrawlSpider):
    name = 'zhilian'
    redis_key='zhilianwang'
    # allowed_domains = ['zhaopin.com']

    rules = (

        Rule(LinkExtractor(allow=r'//jobs.zhaopin.com/\w+?/'),follow=True),

        Rule(LinkExtractor(allow=r'http://jobs.zhaopin.com/bj\d+?/'),follow=True),

        Rule(LinkExtractor(allow=r'http://jobs.zhaopin.com/sj\d+/'),follow=True),

        Rule(LinkExtractor(allow=(r'http://company.zhaopin.com/.*\d+\.htm', r'.*index\.html')),follow=True),
        Rule(LinkExtractor(allow=(r'http://jobs.zhaopin.com/\d+\.htm')),callback='papa_item',follow=False),

        Rule(LinkExtractor(allow=r'\d+\.htm'),callback='parse_item',follow=False)

    )


    custom_settings = {
        "CONCURRENT_REQUESTS": "30",
        "DOWNLOAD_DELAY": "0",

        "ITEM_PIPELINES": {
            #这个配置上你可以往别的地方进行设置存储
            'xiangmu.pipelines.A51jobPipeline': 1,
            #这个是走redis存储  也是设置的先流经谁  设置权重 要加上 分布式的时候
            'scrapy_redis.pipelines.RedisPipeline': 300,
        },
        "LOG_LEVEL": "DEBUG",
        "SCHEDULER_QUEUE_CLASS": "scrapy_redis.queue.SpiderPriorityQueue",
        "SCHEDULER_PERSIST": "True",
        "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
        "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
        "REDIS_HOST": '127.0.0.1',
        "REDIS_PORT": 6379,

    }


    def parse_item(self, response):
        # pass
        #网页来源

        item=zhilianItem()
        url=response.url
        if 'zhaopin' in  url:
            comefrom='来源于智联'
        else:
            comefrom='未知'

        #公司
        company = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()
        if  company :
            company=company[0]
        else:
            company='无'

        #职位名称
        positionname=response.xpath('//div[@class="fl"]/h1/text() | //div[@class="inner-left fl"]/h1/text() ').extract()
        if positionname:
            positionname=positionname[0]
        else:
            positionname=''

        #薪水
        salary=response.xpath('//div[@class="terminalpage-left"]/ul/li[1]//strong/text()').extract()

        if salary:
            salary=salary[0].strip('元/月\xa0').split('-')
            lowsalary=int(salary[0])
            highsalary=int(salary[1])
        else:
            lowsalary=''
            highsalary=''


        #城市
        city=response.xpath('//div[@class="terminalpage-left"]/ul/li[2]//strong/a/text()').extract()
        if city:
            city=city[0]
        else:
            city=''

        #待遇
        treatment=response.xpath('//div[@class="welfare-tab-box"]/span/text()').extract()
        treatment=','.join(treatment)
        if  treatment:
            treatment=treatment
        else:
            treatment='无'

        #日期
        published=response.xpath('//div[@class="terminalpage-left"]/ul/li[3]//span/text()')
        if published:
            published=published.extract()[1]
        else:
            published=''
        degree=response.xpath('//div[@class="terminalpage-left"]/ul/li[6]//strong/text()').extract()
        if degree:
            degree=degree[0]
        else:
            degree=''

        exp=response.xpath('//div[@class="terminalpage-left"]/ul/li[5]//strong/text()').extract()
        if  exp:
            exp=exp[0]
        else:
            exp=''

        positionaddress=response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract()
        if positionaddress:
            if '\r\n' in positionaddress :
                positionaddress=positionaddress.strip('\r\n').strip(' ')
            else:
                positionaddress=positionaddress[0].strip('\r\n                            ')
        else:
            positionaddress='无'

        positiondescription=response.xpath('//div[@class="tab-inner-cont"]/p/text()').extract()
        positiondescription=''.join(positiondescription).strip(' ').strip('\r\n')
        if  positiondescription:
            positiondescription=positiondescription.strip(' ').strip('\xa0').strip('\r\n')
        else:
            positiondescription='无'
        tag=''
        item['url']=url
        item['comefrom'] = comefrom
        item['company']=company
        item['positionname']=positionname
        item['lowsalary']=lowsalary
        item['highsalary']=highsalary
        item['city']=city
        item['treatment']=treatment
        item['published']=published
        item['degree']=degree
        item['exp']=exp
        item['positionaddress']=positionaddress
        item['positiondescription']=positiondescription
        item['tag']=tag

        yield item

    def papa_item(self,response):
        item=zhilianItem()
        url=response.url
        if 'zhaopin' in url:
            comefrom = '来源于智联'
        else:
            comefrom = '未知'
        company = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()
        if company:
            company = company[0]
        else:
            company = '无'

        positionname=response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        salary = response.xpath('//div[@class="terminalpage-left"]/ul/li[1]//strong/text()').extract()

        if salary:
            salary=salary[0].strip('元/月\xa0').split('-')
            lowsalary=int(salary[0])
            highsalary=int(salary[1])
        else:
            lowsalary=''
            highsalary=''


        #城市
        city=response.xpath('//div[@class="terminalpage-left"]/ul/li[2]//strong/a/text()').extract()
        if city:
            city=city[0]
        else:
            city=''

        #待遇
        treatment=response.xpath('//div[@class="welfare-tab-box"]/span/text()').extract()
        treatment=','.join(treatment)
        if  treatment:
            treatment=treatment
        else:
            treatment='无'

        #日期
        published=response.xpath('//div[@class="terminalpage-left"]/ul/li[3]//span/text()')
        if published:
            published=published.extract()[1]
        else:
            published=''
        degree=response.xpath('//div[@class="terminalpage-left"]/ul/li[6]//strong/text()').extract()
        if degree:
            degree=degree[0]
        else:
            degree=''

        exp=response.xpath('//div[@class="terminalpage-left"]/ul/li[5]//strong/text()').extract()
        if  exp:
            exp=exp[0]
        else:
            exp=''

        positonaddress=response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract()
        if positonaddress:
            if '\r\n' in positonaddress :
                positionaddress=positonaddress.strip('\r\n').strip(' ')
            else:
                positionaddress=positonaddress[0].strip('\r\n                            ')
        else:
            positionaddress='无'

        positiondescription=response.xpath('//div[@class="tab-inner-cont"]/p/text()').extract()
        positiondescription=''.join(positiondescription).strip(' ').strip('\r\n')
        if  positiondescription:
            positiondescription=positiondescription.strip(' ')
        else:
            positiondescription='无'

        tag=''
        item['url'] = url
        item['comefrom']=comefrom
        item['company']=company
        item['positionname']=positionname
        item['lowsalary']=lowsalary
        item['highsalary']=highsalary
        item['city']=city
        item['treatment']=treatment
        item['published']=published
        item['degree']=degree
        item['exp']=exp
        item['positionaddress']=positionaddress
        item['positiondescription']=positiondescription
        item['tag']=tag
        yield item
        
    

```

 **Pipeline.py**


    class zhilianPipeline(object):
    def process_item(self, item, spider):
        return  item
### 5.2 案例2 58同城

```
# -*- coding: utf-8 -*-
import scrapy
import  hashlib
from  xiangmu.items import  A58jobItem
from scrapy_redis.spiders import RedisSpider

class A58tcSpider(RedisSpider):
    name = '58tc'
    allowed_domains = ['tj.58.com']
    #起始这个   之后自动去重了
    # start_urls = ['http://bj.58.com/job/']



    redis_key = '58wangzhan'


    base_url='http://tj.58.com/job/pn%d/'
    custom_settings = {
        #并发量
        "CONCURRENT_REQUESTS": "10",
        "DOWNLOAD_DELAY": "0",

        "ITEM_PIPELINES": {
            # 这个配置上你可以把数据往别的地方进行设置存储
            'xiangmu.pipelines.A58Pipeline': 1,
            # 这个是走redis存储  也是设置的先流经谁  设置权重 要加上 分布式的时候
            'scrapy_redis.pipelines.RedisPipeline': 300,
        },
        "DEFAULT_REQUEST_HEADERS":{
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests" : "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "f=n; userid360_xml=A3201C6040F1166BDD7D200EA254C614; time_create=1519474609926; f=n; id58=c5/njVpVf4Jl/y0HCYCqAg==; 58home=bj; 58tj_uuid=7d6f9206-1490-462e-9b95-d82493657a48; als=0; wmda_uuid=beb94fb7eaf7fbe9032ec897997f392c; wmda_new_uuid=1; commontopbar_myfeet_tooltip=end; xxzl_deviceid=76GZAR3C7yr97vrDR84M7k4RTxxFjvMUNJIpCEcXri4UnaxuLuemCWEGomNvZKf3; Hm_lvt_dcee4f66df28844222ef0479976aabf1=1515553360; wmda_visited_projects=%3B2385390625025%3B1731916484865; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1516882900; jobBottomBar=1; gr_user_id=15ce27c6-5fb0-4ff5-8fc1-ca3414596750; city=bj; ppStore_fingerprint=C123ABE03303734DE1AD673F4E8939EB4F622D64FB5F4966%EF%BC%BF1516889804606; f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; new_uv=2; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253D2J0D1FCFCSOn0Qq6ydiT_PoKJSAvq28WvNo4LGRweLO%2526wd%253D%2526eqid%253Dbdddddfe0004dc22000000035a6a78ea; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; new_session=0; wmda_session_id_1731916484865=1516927219318-468b9a88-e1d4-5e64; sessionid=dab9a8f3-32f3-4f88-98a5-b69474eb88dc; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1516890452,1516890469,1516890470,1516927232; JSESSIONID=011A522D076E1B82F84CCC4B8F38E9E5; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1516930283",
        },

            "LOG_LEVEL": "DEBUG",
            "SCHEDULER_QUEUE_CLASS": "scrapy_redis.queue.SpiderPriorityQueue",
            "SCHEDULER_PERSIST": "True",
            "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
            "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
            "REDIS_HOST": '127.0.0.1',
            "REDIS_PORT": 6379,

    }


    def parse(self, response):
        for  i  in range(1,71):
            fullurl=self.base_url%i
            yield  scrapy.Request(url=fullurl,callback=self.parsePage)

    def parsePage(self,response):
        urllist=response.xpath('//div[@class="job_name clearfix"]/a/@href').extract()
        for url in  urllist:
            yield  scrapy.Request(url=url,callback=self.parsexiangqing,priority=1)


    def parsexiangqing(self,response):
        item=A58jobItem()
        url=response.url
        url = self.md5(url)

        positionname=response.xpath('//div[@class="pos_base_info"]/span[1]/text()').extract()[0]
        salary=response.xpath('//div[@class="pos_base_info"]/span[2]/text()').extract()[0]

        if salary:
            if '-' in  salary:
                lowsalary=int(salary.split('-')[0])
                highsalary=int(salary.split('-')[1])
            else:
                lowsalary=0
                highsalary=0
        else:
            lowsalary = 0
            highsalary = 0

        degree=response.xpath('//div[@class="pos_base_condition"]/span[2]/text()').extract()[0]
        exp=response.xpath('//div[@class="pos_base_condition"]/span[3]/text()').extract()[0].strip()
        city=response.xpath('//div[@class="pos-area"]/span/span[1]/text()').extract()[0]

        positionaddress=response.xpath('//div[@class="pos-area"]/span[2]/text()').extract()[0]
        positiondescription=response.xpath('//div[@class="des"]/text()').extract()
        positiondescription=''.join(positiondescription)
        published=response.xpath('//span[@class="pos_base_num pos_base_update"]/span/text()').extract()[0]
        treatment=response.xpath('//div[@class="pos_welfare"]/span/text()').extract()
        treatment=''.join(treatment)
        company=response.xpath('//div[@class="baseInfo_link"]/a/text()').extract()[0]
        tag=''

        item['url'] = url
        item['company'] = company
        item['positionname'] = positionname
        item['lowsalary'] = lowsalary
        item['highsalary'] = highsalary
        item['city'] = city
        item['treatment'] = treatment
        item['published'] = published
        item['degree'] = degree
        item['exp'] = exp
        item['positionaddress'] = positionaddress
        item['positiondescription'] = positiondescription
        item['tag'] = tag
        yield  item

    def md5(self, value):
        md5 = hashlib.md5()
        md5.update(bytes(value, encoding='utf-8'))
        return md5.hexdigest()
```



**pipelines.py**

```

class A58Pipeline(object):
    def process_item(self,item,spider):
        #给到控制台
        #这是插入到字段的值  把爬虫名给当成来源名字
        item['comefrom']=spider.name
        return  item
```



### 5.3 案例3 赶集网

```
# -*- coding: utf-8 -*-
from scrapy_redis.spiders import  RedisSpider
import  scrapy
import  hashlib
from xiangmu.items import ganjiItem
import  datetime
class GanjiSpider(RedisSpider):
    name = 'ganji'
    allowed_domains = ['bj.ganji.com']
    redis_key='ganji'
    base_url='http://bj.ganji.com/zpbiaoqian/xicheng/o%d/'
    import  datetime
    custom_settings = {
        'ITEM_PIPELINES': {
            'xiangmu.pipelines.ganjiPipeline': 1,
            'scrapy_redis.pipelines.RedisPipeline': 300,
        },
        "CONCURRENT_REQUESTS": "5",
         'DOWNLOAD_DELAY': 0,

        'DEFAULT_REQUEST_HEADERS':{
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "statistics_clientid=me; ganji_xuuid=60c34530-fb6d-4907-9bb1-36f8a4bc58ea.1517186102473; ganji_uuid=3935210944349292626341; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A30902576639%7D; GANJISESSID=sih2oc9tcp64c5fthc7gcq4cfg; xxzl_deviceid=0BsWKQZC2bpFBxXlKElCKSRg%2FPuc%2BeNCmMuPOyElK997HGkVMIDhiCpIQSN%2FrjJg; lg=1; index_zcm_banner=2018-1-29; citydomain=bj; __utma=32156897.1524860060.1517186111.1517186111.1517186111.1; __utmc=32156897; __utmz=32156897.1517186111.1.1.utmcsr=bj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _wap__utmganji_wap_newCaInfo_V2=%7B%22ca_n%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%7D; WantedListPageScreenType=1920; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1517186118; pos_detail_zcm_popup=2018-1-29; bdshare_firstime=1517186136039; simResStatus=%2C908%2C102169%2C; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1517186134,1517187224; gj_footprint=%5B%5B%22%5Cu91c7%5Cu8d2d%5Cu5458%5C%2F%5Cu52a9%5Cu7406%22%2C%22%5C%2Fzpcaigou%5C%2F%22%5D%2C%5B%22%5Cu6536%5Cu94f6%5Cu5458%22%2C%22%5C%2Fzpshouyinyuan%5C%2F%22%5D%2C%5B%22%5Cu6e38%5Cu620f%5Cu6d4b%5Cu8bd5%22%2C%22%5C%2Fzpyouxiceshi%5C%2F%22%5D%5D; zhaopin_lasthistory=zpbaihuolingshou%7Czpcaigou; zhaopin_historyrecords=bj%7Czpcaigou%7C-%2Cbj%7Czpshouyinyuan%7C-%2Cbj%7Czpxiaoshoudaibiao%7C-%2Cbj%7Czpyouxiceshi%7C-%2Cbj%7Czpchanpinzhuanyuan%7C-; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1517187595; __utmt=1; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1517187684; __utmb=32156897.17.10.1517186111; ganji_login_act=1517187694777",
        },

        "LOG_LEVEL": "DEBUG",
        "SCHEDULER_QUEUE_CLASS": "scrapy_redis.queue.SpiderPriorityQueue",
        "SCHEDULER_PERSIST": "True",
        "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
        "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
        "REDIS_HOST": '127.0.0.1',
        "REDIS_PORT": 6379,

    }
    def parse(self, response):
        for  i  in range(0,90):
            fullurl=self.base_url % i
            yield  scrapy.Request(url=fullurl,callback=self.parsePage)

    def parsePage(self,response):
        urls=response.xpath(r'//dl[@class="con-list-zcon new-dl"]/dt/a/@href').extract()

        for  url  in  urls :
            fullurl='http://bj.ganji.com' + url
            yield scrapy.Request(url=fullurl,callback=self.detailPage)
    def detailPage(self,response):
        item=ganjiItem()
        url=response.url
        url=self.md5(url)

        positionname=response.xpath('//ul[@class="clearfix pos-relat"]/li[1]/em/a/text()').extract()[0]

        published=response.xpath('//p[@class="data-sty mb-5"]/span[1]/text()')
        if  published:
            if '-' in published:
                published=published.extract()[0].strip('更新日期:')

            else:
                published=str(datetime.datetime.now().strftime('%Y-%m-%d'))
        else:
            published='没有填写日期'
        salary=response.xpath('//li[@class="fl"][2]/em/text()').extract()[0]
        if  salary:
            if '-' in salary:
                lowsalary=int(salary.split('-')[0])
                highsalary=int(salary.split('-')[1].strip('元'))
            else:
                lowsalary=0
                highsalary=0
        exp=response.xpath('//li[@class="fl"][4]/em/text()').extract()[0]
        positionaddress=response.xpath('//li[@class="fl w-auto"]/em/text()').extract()[0].strip()
        degree=response.xpath('//li[@class="fl"][3]/em/text()').extract()[0]
        treatment=response.xpath('//ul[@class="clearfix"]/li/text()').extract()
        treatment=''.join(treatment).strip('\n').strip(' - ').strip('\n')
        positiondescription=response.xpath('//div[@class="deta-Corp"]/text()').extract()
        positiondescription=''.join(positiondescription).strip('\n').strip(' ').strip('\r').strip(' ').strip('\n')
        tag=''
        company=response.xpath('//span[@class="firm-name"]/a/text()').extract()[0].strip('\n').strip(' ')
        city=response.xpath('//li[@class="fl w-auto"]/em/a/text()').extract()[0]

        item['url'] = url
        item['company'] = company
        item['positionname'] = positionname
        item['lowsalary'] = lowsalary
        item['highsalary'] = highsalary
        item['city'] = city
        item['treatment'] = treatment
        item['published'] = published
        item['degree'] = degree
        item['exp'] = exp
        item['positionaddress'] = positionaddress
        item['positiondescription'] = positiondescription
        item['tag'] = tag

        yield  item



    def md5(self, value):
        md5 = hashlib.md5()
        md5.update(bytes(value, encoding='utf-8'))
        return md5.hexdigest()



```



**pipeline.py**

```


class  ganjiPipeline(object):
    def process_item(self,item,spider):
        item['comefrom']=spider.name
        return  item

```



### 5.4 案例4 51job

```
# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiangmu.items import  A51jobItem
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider

#RedisSpider 必须parse回掉 正常不全站用它 RedisCrowlSpider  parse_item

#全站分布用RedisCrawlSpider

#类里有Redis 不用starturl  用redis_key随便写键
class A51jobSpider(RedisCrawlSpider):
    name = '51job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://www.51job.com/']
    #这只是个键名 值只是要找的url
    redis_key = 'myspider:url'

    custom_settings = {

        "CONCURRENT_REQUESTS": "5",
        "DOWNLOAD_DELAY": "0",

        "ITEM_PIPELINES": {
            'xiangmu.pipelines.A51jobPipeline': 1,
            'scrapy_redis.pipelines.RedisPipeline': 300,
        },
        "LOG_LEVEL": "DEBUG",
        "SCHEDULER_QUEUE_CLASS": "scrapy_redis.queue.SpiderPriorityQueue",
        "SCHEDULER_PERSIST": "True",
        "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
        "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
        "REDIS_HOST": '127.0.0.1',
        "REDIS_PORT": 6379,

    }

    rules = (

        Rule(LinkExtractor(r'http://search.51job.com/list/010000,000000,0000,32,9,99,%2B,2,1.html\?.*&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='),  follow=True),
        Rule(LinkExtractor(
            r'http://search.51job.com/list/010000,000000,0000,03,9,99,%2B,2,1.html\?confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='), follow=True),
        Rule(LinkExtractor(
            r'http://search.51job.com/list/010000,000000,0000,33,9,99,%2B,2,1.html\?confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='),follow=True),
        Rule(LinkExtractor(
            r'http://search.51job.com/list/010000,000000,0000,26,9,99,%2B,2,1.html\?confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='),follow=True),

        Rule(LinkExtractor(r'http://jobs.51job.com/beijing/\d+\.html\?s=01&t=0'), callback='parse_item', follow=False),
        Rule(LinkExtractor(r'http://jobs.51job.com/beijing-\w+/\d+\.html\?s=01&t=0'), callback='parse_item', follow=False),

    )
    def parse_item(self, response):
        item=A51jobItem()
        url=response.url

        if  '51job'in  url:
            comefrom='来源于51job'
        else:
            comefrom='未知'
        positionname=response.xpath(r'//div[@class="in"]//h1/text()').extract()[0]
        salary=response.xpath(r'//div[@class="cn"]/strong/text()').extract()[0]
        if salary:
            if '万/月' in salary:
                lowsalary=float(salary.strip('万/月').split('-')[0])*10000
                highsalary=float(salary.strip('万/月').split('-')[1])*10000
            elif '千/月' in salary:
                lowsalary=float(salary.strip('千/月').split('-')[0])*1000
                highsalary=float(salary.strip('千/月').split('-')[1])*1000

            else:
                lowsalary=''
                highsalary=''
        else:
            lowsalary=''
            highsalary=''

        positiondescription=response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()

        positiondescription=''.join(positiondescription).strip('\r\n\t\t\t\t\t\t')
        positionaddress=response.xpath('//p[@class="fp"]/text()').extract()[-1].strip('\t')

        published=response.xpath('//div[@class="t1"]/span[4]/text()')
        if  published:
            published=published.extract()[0].strip('发布')
        else:
            published=''

        degree=response.xpath('//div[@class="t1"]/span[2]/text()').extract()[0]
        if degree:
            if '招'  in degree:
                degree='学历不限'
            else:
                degree=degree
        else:
            degree='学历不限'

        treatment=response.xpath('//div[@class="jtag inbox"]/p[@class="t2"]/span/text()').extract()
        if  treatment:
            treatment=','.join(treatment)
        else:
            treatment='无'
        company=response.xpath('//p[@class="cname"]/a/text()').extract()[0]

        city=response.xpath('//div[@class="cn"]/span/text()').extract()[0]
        exp=response.xpath('//div[@class="t1"]/span[1]/text()').extract()[0]
        tag=''


        item["url"] = url
        item["positionname"] = positionname
        item["lowsalary"] = lowsalary
        item["highsalary"] = highsalary

        item["positiondescription"] = positiondescription
        item["positionaddress"] = positionaddress
        item["published"] = published
        item["degree"] = degree
        item["treatment"] = treatment
        item["company"] = company
        item["city"] = city
        item["exp"] = exp
        item["tag"] = tag
        item['comefrom'] = comefrom
        yield  item


```

**pipeline.py**

```
class  ganjiPipeline(object):
    def process_item(self,item,spider):
        item['comefrom']=spider.name
        return  item

```

### 5.5将缓存数据从redis转移mysql

```
import json 
import  redis 
import pymysql 

def main():
	#指定redis数据库信息
	rediscli= redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
	#指定mysql数据库
	mysqlcli = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='pachong',charset='utf8')
	#无限循环
	while True:
		source,data=rediscli.blpop(["ganji:item"])#从redis里提取数据
		item = json.loads(data,decode('utf-8'))#把json转字典
		
	try:
		#使用cursor()方法获取操作游标
		cur=mysqlcli.cursor
		#使用execute方法执行SQL  INSERT语句
         sql = 'insert into zhaopin(url,positionname,lowsalary,highsalary,positiondescription,positionaddress,published,degree,treatment,company,city,exp,tag,comefrom) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update lowsalary=values(lowsalary),highsalary=VALUES(highsalary),published=values(published)'
         cur.execute(sql, (item["url"], item["positionname"], item["lowsalary"], item["highsalary"], item["positiondescription"], item["positionaddress"],item["published"],item["degree"], item["treatment"], item["company"], item["city"], item["exp"], item["tag"],item['comefrom']))
         
         #提交sql事务
         mysqlcli.cmmit()
         #关闭本次服务
         cur.close()
         print('插入 %s' % item['positonname'])
      except pymysql.Error  as  e :
          mysqlcli.rollback()
          print("插入错误",str(e))
          
          
if  __name__=='__main__':
	main()

```



## 6. Django将爬取的数据进行展示 有BUG 能力不够了！

**setting.py**

```

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^rxmucj=x0n52pj)#nw&kai*_=!4#2^cusw5rt0wb8-&n)b*w9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shujuzhanshi.apps.ShujuzhanshiConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'daxiangmu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #模板的配置
        'DIRS': [os.path.join(BASE_DIR, 'templates')] ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'daxiangmu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #库名
        'NAME': 'pachong',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#配置静态文件路径 在主dir下面
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```



**模板templates/index.html**

```
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>招聘驿站</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="{% static 'img/sync.ico' %}">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'css/list.css' %}">
</head>
<body>
<!-- 顶部栏 -->
<div class="tops" style="top:0;position: fixed;">
    <div class="logo">
        <span>相逢一醉是前缘，风雨散，飘然何处 !</span>
        <span style="margin-left: 400px;font-size:20px;"><a href="#">首页</a></span>
        <span style="margin-left: 50px;font-size:20px;"><a href="#">搜索招聘</a></span>
        <!-- <span style="margin-left: 250px;font-size:16px;"><a href="#">请登录</a></span><em></em>
        <span style="font-size:16px;"><a href="#">注册</a></span> -->
    </div>
</div>
<br>
<!-- 搜索框 -->
<div class="container">
    <div class="search">
                                                    {#一点击自动跳转到这个index  逆向解析#}
        <form class="navbar-form navbar-left" action="{% url 'index' %}" method="get" role="search">
            <div class="form-group">
                                                                                                            {# kw 让输入的值进行显示 #}
                <input style="width: 300px" type="text" class="form-control" name='kw' placeholder="职业职位" value="{{ kw }}">
                <input style="width: 300px" type="hidden" class="form-control" name='money' placeholder="职业职位" value="{{ money }}">
                <input style="width: 300px" type="hidden" class="form-control" name='degree' placeholder="职业职位" value="{{ degree }}">
                <input style="width: 300px" type="hidden" class="form-control" name='pn' placeholder="职业职位" value="{{ pn }}">

            </div>
            <button type="submit" class="btn btn-default">搜索</button>
        </form>
    </div>
</div>
<div class="container">
    <div class="cls">
        <span>热门搜索：</span>
        <ul>
            {# 1个{%自动跳转逆向解析到路由index  给视图kw参数%}#}

            <li><a href="{% url 'index' %}?kw=&money={{ money }}&degree={{ degree }}&pn={{ pn }}">全部</a></li>
                                    {#  整体相当于都满足了 就这么写联查   前面的money是传递过去的参数名   后面的money是查完了之后给返回来的数据 模板填充     #}
            <li><a href="{% url 'index' %}?kw=销售&money={{ money }}&degree={{ degree }}&pn={{ pn }}">销售</a></li>
            <li><a href="{% url 'index' %}?kw=工程师&money={{ money }}&degree={{ degree }}&pn={{ pn }}">工程师</a></li>
            <li><a href="{% url 'index' %}?kw=人事&money={{ money }}&degree={{ degree }}&pn={{ pn }}">人事</a></li>
            <li><a href="{% url 'index' %}?kw=会计&money={{ money }}}&degree={{ degree }}&pn={{ pn }}">会计</a></li>
            <li><a href="{% url 'index' %}?kw=房地产&money={{ money }}&degree={{ degree }}&pn={{ pn }}">房地产</a></li>
            <li><a href="{% url 'index' %}?kw=平面设计&money={{ money }}&degree={{ degree }}&pn={{ pn }}">平面设计</a></li>
            <li><a href="{% url 'index' %}?kw=web前端&money={{ money }}&degree={{ degree }}&pn={{ pn }}">web前端</a></li>
        </ul>
    </div>
    <div class="cls">
        <span>月薪范围：</span>
        <ul>
            <li><a href="">所有</a></li>
            <li><a href="{% url 'index' %}?money=3-5">3-5k</a></li>
            <li><a href="{% url 'index' %}?money=5-7">5-7k</a></li>
            <li><a href="{% url 'index' %}?money=7-10">7-10k</a></li>
            <li><a href="{% url 'index' %}?money=10-20">10-20k</a></li>
            <li><a href="{% url 'index' %}?money>=20">20k以上</a></li>
        </ul>
    </div>
    <div class="cls">
        <span>工作年限：</span>
        <ul>
            <li><a href="">不限</a></li>
            <li><a href="">1-3年</a></li>
            <li><a href="">3-6年</a></li>
            <li><a href="">6-10年</a></li>
            <li><a href="">10年以上</a></li>
        </ul>
    </div>
    <div class="cls">
        <span>学历要求：</span>
        <ul>
            <li><a href="">所有</a></li>
            <li><a href="">初中</a></li>
            <li><a href="">高中</a></li>
            <li><a href="">中专</a></li>
            <li><a href="">大专</a></li>
            <li><a href="">本科</a></li>
            <li><a href="">研究生</a></li>
        </ul>
    </div>
</div>
<br><br>
<!-- 列表显示 -->
<div class="container">
    <table class="table table-striped active">
        <tr>
            <td class="av">职位名称</td>
            <td class="av">公司名称</td>
            <td class="ck">工作地点</td>
            <td class="ck">薪资范围</td>
            <td class="ck">工作年限</td>
            <td class="ck">发布时间</td>
            <td class="ck">来源</td>
        </tr>


        <!--遍历每一个对象  直接.它的字段就出来值了-->
        {# 传递过来的数据进行填充#}
        {% for job in job_list %}
            <tr>
                {# 点击获取url  a链接 直接跳转 #}
                {#  job.字段}
                <td class="av"><a href="{{ job.url }}">{{ job.positionname }}</a></td>
                <td class="av">{{ job.company }}</td>
                <td class="ck">{{ job.positionaddress }}</td>
                <td class="ck">{{ job.lowsalary }}-{{ job.highsalary}}</td>
                <td class="ck">{{ job.exp }}</td>
                <td class="ck">{{ job.published }}</td>
                <td class="ck">{{ job.comefrom }}</td>

            </tr>
        {% endfor %}
    </table>
</div>
<br>
<!-- 分页 -->
<div class="container">
    <ul class='pagination fenye'>
        <li>
            <a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn=1">首页</a>
        </li>

        <li id='zuojt'>
            {% if job_list.has_previous %}
                <a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn={{ job_list.previous_page_number }}">上一页</a>
            {% endif %}
        </li>

        {% for num in page_numbers %}
            {% if num == pn %}
                <li class="active"><a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn={{ num }}">第{{ num }}页</a></li>
            {% else %}
                <li class=""><a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn={{ num }}">第{{ num }}页</a></li>
            {% endif %}
        {% endfor %}


        <li id='zuojt'>
            {% if job_list.has_next %}
                <a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn={{ job_list.next_page_number }}">下一页</a>
            {% endif %}
        </li>

        <li>
            <a href="{% url 'index' %}?kw={{ kw }}&money={{ money }}&degree={{ degree }}&pn={{ paginator.num_pages }}">尾页</a>
        </li>
    </ul>
</div>


<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="{% static 'js/jquery-1.12.4.min.js' %}"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="{% static 'js/bootstrap.min.js' %}"></script>

</body>
</html>
```

**urls.py**

```
from django.conf.urls import url

#导入子路由
from django.contrib import  admin

from shujuzhanshi import  views


# from django.contrib import
urlpatterns = [
    #后台
    url(r'^admin/',admin.site.urls),
    #这个什么都不输就访问了   ^以什么开始  index 是为了模板点击之后来逆向解析 之后进入视图处理函数
    url(r'^$', views.index,name='index'),
]

```



**views.py**

```
from  django.shortcuts   import render
from .models import *

from django.core.paginator  import Paginator 

def index(request):
	#获取点击传递过来的值      kw 
	kw =request.GET.get('kw','')
	money=request.GET.get('money','')
	
	#查询出来   模糊查询
	#查询出来前5个queryset的pname字段的值
	#jobs = zhaopin.objects.values('pname').all()[:5] 列表里放字典 一个对象一个字典
	#jobs = zhaopin.objects.values_list().all()返回元祖形式 你要是取片的话就1个
	
	degree=request.GET.get('degree','')
	pn=request.GET.get('pn','')
	
	try:
		pn=int(pn)
	except EXxception as e :
		pn=1
		
	#第一套
	#if kw:
		#select字段筛选
		#根据职位进行模糊查询 把queryset对象里的这些值  给拿出来  返回列表 values里面的值是字段
		
	#返回所有变量 以字典形式{'job_list': <QuerySet [{'highsalary': 30000, 'positionname': 'python运维研发工程师(za..) }]}  #这有缩进			  #job_list=zhaopin.objects.filter(positionname_contains=kw).values('positionname','url','positionaddress','lowsalary','highsalary','exp','published','company','comefrom').all()
	    
	   
	 #第一套升级版  直接搜出来  把这些对象的内容
    job_list=zhaopin.objects.values('positionname','url','positionaddress','lowsalary','highsalary','exp','published','company','comefrom').all()

    # where
    if kw:
        job_list = zhaopin.objects.filter(pname__contains=kw).all()


    #如果有money
    if  money:
        #看看它是否在里面
        if '-'in  money:
            lowsalary=money.split('-')[0]
            highsalary=money.split('-')[1]
            #where
            #模糊查询 大于         lt小于   字段加__  因为存的整形  所以整形来查
            job_list=job_list.filter(lowsalary__gte=int(lowsalary)*1000,highsalary__lte=int(highsalary)*1000)

        else:
            job_list=job_list.filter(lowsalary__gte=int(money)*1000)
        # job_list = job_list[:50]
        #给返回去所有函数内部的变量

    if  degree:
        job_list=job_list.filter(degree__contains=degree)


    #limit操作 取出来50条数据
    job_list=job_list[:500]
    #分页  每页5条数据   10页总共
    paginator = Paginator(job_list, 40)
    try:
        #根据输入的页码进行显示那页的数据
        job_list=paginator.page(pn)
    except Exception as e :
        #如果超过页码范围 就显示第一页的数据
        job_list=paginator.page(1)

    #为了控制生成的页码
    #让前面有几页  不管你怎么点
    start = pn-10
    #就是为了让当前点击页的后面有几个
    end = pn +3

    #如果起始页小于1  让它等于1
    if start < 1:
        start = 1
    #如果end  大于 页码总数数
    if end > paginator.num_pages:
        #因为底下的生成页码取不到最后一页
        end = paginator.num_pages + 1

    #生成页码
    page_numbers = range(start,end)

    return render(request,'index.html',locals())

	

```



**models.py**

```
from django,db import models
class zhaopin(models.Model):
	#好比mysql数据库里的字段名
    url=models.CharField(max_length=255)
    positionname=models.CharField(max_length=50)
    lowsalary=models.IntegerField()
    highsalary=models.IntegerField()
    positionaddress=models.CharField(max_length=255)
    positiondescription=models.CharField(max_length=255)
    published=models.CharField(max_length=255)
    degree=models.CharField(max_length=255)
    treatment=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    comefrom=models.CharField(max_length=255)
    exp=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    abc=models.CharField(max_length=1)
    def __str__(self):
        #给对象个名
        return  self.positionname
    #表名
    class Meta:
        db_table='zhaopin'

	
```


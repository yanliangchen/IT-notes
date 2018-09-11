[TOC]



## 1. 为什么要选择Numpy & Pandas?

两个科学运算当中最为重要的两个模块，一个是 numpy,一个是 pandas。任何关于数据分析的模块都少不了它们两个。

应用

数据分析

机器学习

深度学习

为什么使用 numpy & pandas

运算速度快：numpy 和 pandas 都是采用 C 语言编写, pandas 又是基于 numpy, 是 numpy 的升级版本。

消耗资源少：采用的是矩阵运算，会比 python 自带的字典或者列表快好多



## 2. Numpy的安装

Linux :  

​	$  sudo  pip  install  python-numpy

Windows : 下载numpy的不同版本 下载的路径  给安到指定版本  

​        $  python  -m  pip  install   



## 3. Numpy的学习 

NumPy是Python语言的一个扩充程序库。支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。Numpy内部解除了Python的GIL(全局解释器锁),运算效率极好,是大量机器学习框架的基础库!  

**补充 : GIL全局解释器锁**

 同一进程下的多线程共享数据，共享意味着竞争，竞争带来无序，为了数据安全所以需要加锁进行数据保护，GIL本质是一把互斥锁，使并发变为串行，保证同一时间只有一条线程访问解释器级别的数据，这样就保证了解释器级别的数据安全，同时也带来了一些问题，同一进程只有一条线程执行任务，无法利用多核优势，解决方案可以根据任务的类型来处理，如果是I/O密集型，则需要开多线程提高效率，如果是计算密集型则需要多进程。



**参见:https://www.yiibai.com/numpy/numpy_array_from_existing_data.html**

### 3.1 NumPy Ndarray对象

NumPy 中定义的最重要的对象是称为 `ndarray` 的 N 维数组类型。 它描述相同类型的元素集合。 可以使用基于零的索引访问集合中的项目。



1.`ndarray`中的每个元素在内存中使用相同大小的块。 `ndarray`中的每个元素是数据类型对象的对象(称为 `dtype`)。



2.从`ndarray`对象提取的任何元素(通过切片)由一个数组标量类型的 Python 对象表示。 下图显示了`ndarray`，数据类型对象(`dtype`)和数组标量类型之间的关系。

 

![img](http://www.yiibai.com/uploads/images/201704/2404/430090425_51678.jpg)

 

`ndarray`类的实例可以通过本教程后面描述的不同的数组创建例程来构造。 基本的`ndarray`是使用 NumPy 中的数组函数创建的，如下所示：

```
import  numpy  as  np 
a = [[1, 2, 3, 4]]
b = np.array(a)
```

它从任何暴露数组接口的对象，或从返回数组的任何方法创建一个ndarray。

```
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

上面的构造器接受以下参数：

| 1.   | `object` 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。 |
| ---- | ------------------------------------------------------------ |
| 2.   | `dtype` 数组的所需数据类型，可选。                           |
| 3.   | `copy` 可选，默认为`true`，对象是否被复制。                  |
| 4.   | `order` `C`(按行)、`F`(按列)或`A`(任意，默认)。              |
| 5.   | `subok` 默认情况下，返回的数组被强制为基类数组。 如果为`true`，则返回子类。 |
| 6.   | `ndimin` 指定返回数组的最小维数。                            |



#### 3.1.1 示例 1

```

```



#### 3.1.2  示例 2

```
# 多于一个维度
import  numpy  as  np
a = np.array([ [1, 2], [3, 4] ])
print(a)

#输出如下：
[[1, 2]
 [3, 4]]
```



#### 3.1.3 示例 3

```
# 最小维度
import numpy  as  np
a = np.array([1, 2, 3],ndmin = 2)
print(a)

# 输出如下：
[[1, 2, 3, 4, 5]]
```



#### 3.1.4 示例 4

```
#dtype 参数
import  numpy  as  np 
a = np.array([1, 2, 3],dtype = complex)
print(a)

#输出如下:
[1.+0.j , 2.+0.j , 3.+0.j]
```

**ndarray**  对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。 内存块以按行(C 风格)或按列(FORTRAN 或 MatLab 风格)的方式保存元素。





### 3.2 NumPy 数据类型

NumPy 支持比 Python 更多种类的数值类型。 下表显示了 NumPy 中定义的不同标量数据类型。 

 

| 序号 | 数据类型及描述                                             |
| ---- | ---------------------------------------------------------- |
| 1.   | bool_存储为一个字节的布尔值(真或假)                        |
| 2.   | int_默认整数，相当于 C 的long，通常为int32或int64          |
| 3.   | intc相当于 C 的int，通常为int32或int64                     |
| 4.   | intp用于索引的整数，相当于 C 的size_t，通常为int32或int64  |
| 5.   | int8字节(-128 ~ 127)                                       |
| 6.   | int1616 位整数(-32768 ~ 32767)                             |
| 7.   | int3232 位整数(-2147483648 ~ 2147483647)                   |
| 8.   | int6464 位整数(-9223372036854775808 ~ 9223372036854775807) |
| 9.   | uint88 位无符号整数(0 ~ 255)                               |
| 10.  | uint1616 位无符号整数(0 ~ 65535)                           |
| 11.  | uint3232 位无符号整数(0 ~ 4294967295)                      |
| 12.  | uint6464 位无符号整数(0 ~ 18446744073709551615)            |
| 13.  | float_float64的简写                                        |
| 14.  | float16半精度浮点：符号位，5 位指数，10 位尾数             |
| 15.  | float32单精度浮点：符号位，8 位指数，23 位尾数             |
| 16.  | float64双精度浮点：符号位，11 位指数，52 位尾数            |
| 17.  | complex_complex128的简写                                   |
| 18.  | complex64复数，由两个 32 位浮点表示(实部和虚部)            |
| 19.  | complex128复数，由两个 64 位浮点表示(实部和虚部)           |

 

 	NumPy 数字类型是dtype(数据类型)对象的实例，每个对象具有唯一的特征。 这些类型可以是np.bool_，np.float32等。 

#### 3.2.1 数据类型对象（dtype）

数据类型对象描述了对应于数组的固定内存块的解释，取决于以下方面： 

-  			数据类型(整数、浮点或者 Python 对象) 		
	  			数据大小 		
	  			字节序(小端或大端) 		
	  			在结构化类型的情况下，字段的名称，每个字段的数据类型，和每个字段占用的内存块部分。 		
	  			如果数据类型是子序列，它的形状和数据类型。 



字节顺序取决于数据类型的前缀<或>。<意味着编码是小端(最小有效字节存储在最小地址中)。>意味着编码是大端(最大有效字节存储在最小地址中)。 

dtype可有以下语法构造:

```
numpy.dtype(object, align, copy)
参数为： 
Object：被转换为数据类型的对象。 
Align：如果为true，则向字段添加间隔，使其类似 C 的结构体。 
Copy? 生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用。 
```

#### 3.2.2  示例1

```
# 使用数组标量类型  
import numpy as np 
dt = np.dtype(np.int32)  
print dt

#输出如下： 
int32
```

#### 3.2.2 示例2

```
#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。  
import numpy as np 

dt = np.dtype('i4')  
print dt

#输出如下:
int32
```

#### 3.2.3 示例3

```
# 使用端记号  
import numpy as np 
dt = np.dtype('>i4')  
print dt
```

下面的例子展示了结构化数据类型的使用。 这里声明了字段名称和相应的标量数据类型。 



#### 3.2.4 示例4

```
# 首先创建结构化数据类型。  
import numpy as np 
dt = np.dtype([('age',np.int8)])  
print dt


#输出如下： 
[('age', 'i1')]
```



#### 3.2.5 示例5

```
# 现在将其应用于 ndarray 对象  
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt)  
print (a)

#输出如下：
[(10,) (20,) (30,)]
```



#### 3.2.6 示例6

```
#文件名称可用于访问age列的内容
import  numpy  as  np 
#可以理解成你这个数组事存的np.int8类型的 
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
#可以理解成存的映射关系对象
print(a['age'])
输出如下： 
[10 20 30]
```



#### 3.2.7 示例7 

以下示例定义名为 **student** 的结构化数据类型，其中包含字符串字段name，**整数字段**age和**浮点字段**marks。 此dtype应用于ndarray对象。 

```
import numpy as np 
student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])  
print (student)
```

输出如下：

```
[('name', 'S20'), ('age', 'i1'), ('marks', '<f4')])
```



#### 3.2.8 示例8

```

```

输出如下：

```

```

每个内建类型都有一个唯一定义它的字符代码： 

- ​			'b'：布尔值 		
	  			'i'：符号整数 		
	  			'u'：无符号整数 		
	  			'f'：浮点 		
	  			'c'：复数浮点 		
	  			'm'：时间间隔 		
	  			'M'：日期时间 		
	  			'O'：Python 对象 		
	  			'S', 'a'：字节串 		
	  			'U'：Unicode 		
	  			'V'：原始数据(void) 



### 3.3 Numpy 数组属性

#### 3.3.1 ndarray.shape

这一数组属性返回一个包含数组维度的元祖，它也可以用于调整数组大小。

##### 3.3.1.1 示例1

```
import numpy as np 
a = np.array([[1,2,3],[4,5,6]])  
print a.shape

#输出如下:
(2,3)
```



##### 3.3.1.2 示例2

```
# 这会调整数组大小  
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) a.shape =  (3,2)  
print a

#输出如下:
[[1, 2] 
 [3, 4] 
 [5, 6]]
```



##### 3.3.1.3 示例3 

NumPy 也提供了`reshape`函数来调整数组大小。

```
import  numpy  as  np 
a = np.array([1,2,3],[4,5,6])
b = a.reshape(3,2)
print(b)

#输出如下：
[[1, 2] 
 [3, 4] 
 [5, 6]]
```



#### 3.3.2  ndarray.ndim

这一数组属性返回数组的维数。

##### 3.3.2.1 示例1 

```
等间隔数字的数组
import numpy  as  np
a = np.arange(24)
print(a)

#输出结果如下:
[0 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 17 18 19 20 21 22 23]
```

##### 3.3.2.2  示例2

```
#一维数组
import  numpy  as  np
a = np.arange(24)
#现在调整其大小
#现在拥有三个维度   
b = a.reshape(2,4,3)
print(b)
```

```
输出如下:
给输出成2个数组，四行3列  4L,3L
[[[ 0,  1,  2] 
  [ 3,  4,  5] 
  [ 6,  7,  8] 
  [ 9, 10, 11]]  
  
  [[12, 13, 14] 
   [15, 16, 17]
   [18, 19, 20] 
   [21, 22, 23]]]
```



#### 3.3.3 numpy.itemsize

这一数组属性返回数组中每个元素的字节单位长度。

##### 3.3.3.1 示例1 

```
# 数组的 dtype 为 int8(一个字节)
# 不管你写入数组里多少个元素  存的dtype是 int8类型  就是一个字节
import  numpy  as  np 
x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)

#输出如下：
1
```



##### 3.3.3.2  示例2

```
# 数组的 dtype 现在为 float32(四个字节)  
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.float32)  
print x.itemsize

#输出如下:
4
```



#### 3.3.4 numpy.flags 

`ndarray`对象拥有以下属性。这个函数返回了它们的当前值。

| 序号 | 属性及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1.   | `C_CONTIGUOUS (C)` 数组位于单一的、C 风格的连续区段内        |
| 2.   | `F_CONTIGUOUS (F)` 数组位于单一的、Fortran 风格的连续区段内  |
| 3.   | `OWNDATA (O)` 数组的内存从其它对象处借用                     |
| 4.   | `WRITEABLE (W)` 数据区域可写入。 将它设置为`flase`会锁定数据，使其只读 |
| 5.   | `ALIGNED (A)` 数据和任何元素会为硬件适当对齐                 |
| 6.   | `UPDATEIFCOPY (U)` 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新 |



##### 3.3.4.1  示例

下面的例子展示当前的标志.

```
import  numpy  as  np 
x  = np.array([1,2,3,4,5])
print (x.flags)

#输出如下:
  C_CONTIGUOUS : True
  F_CONTIGUOUS : True
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
  UPDATEIFCOPY : False

```



### 3.4  Numpy 数组创建例程

新的`ndarray`对象可以通过任何下列数组创建例程或使用低级`ndarray`构造函数构造。

#### 3.4.1  numpy.empty

它创建指定形状和`dtype`的未初始化数组。 它使用以下构造函数：

```
numpy.empty(shape,dtype = float ,order = 'C')
```

构造器接受下列参数：

| 序号 | 参数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1.   | `Shape` 空数组的形状，整数或整数元组                         |
| 2.   | `Dtype` 所需的输出数组类型，可选                             |
| 3.   | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |



##### 3.4.1.1 示例

下面的代码展示空数组的例子：

```
import  numpy  as  np 
x = np.empty([3,2],dtype = int)
print(x)

#输出如下:
[[22649312    1701344351] 
 [1818321759  1885959276] 
 [16779776    156368896]]
```

**注意**：数组元素为随机值，因为它们未初始化。



#### 3.4.2 numpy.zeros

返回特定大小，以 0 填充的新数组。

```
numpy.zeros(shape,dtype = float, order = 'C')
```

构造器接受下列参数：

| 序号 | 参数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1.   | `Shape` 空数组的形状，整数或整数元组                         |
| 2.   | `Dtype` 所需的输出数组类型，可选                             |
| 3.   | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |



##### 3.4.2.1 示例1

```
# 含有 5 个 0 的数组，默认类型为 float  
import numpy as np 
x = np.zeros(5)  
print x

#输出如下 ：
[0. 0. 0. 0. 0.]
```



##### 3.4.2.2 示例2 

```
import numpy as np 
x = np.zeros((5,), dtype = np.int)  
print x

输出如下:
[0 0 0 0 0]
```



##### 3.4.2.3 示例3

```
# 自定义类型 
import numpy as np 
x = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'i4')])  
print x

输出如下：
[[(0,0)(0,0)]
 [(0,0)(0,0)]]
```



#### 3.4.3 numpy.ones

返回特定大小，以 1 填充的新数组。

```
numpy.ones(shape, dtype = None, order = 'C')
```

构造器接受下列参数：

 

| 序号 | 参数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1.   | `Shape` 空数组的形状，整数或整数元组                         |
| 2.   | `Dtype` 所需的输出数组类型，可选                             |
| 3.   | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |



##### 3.4.3.1 示例1 

```
# 含有 5 个 1 的数组，默认类型为 float  
import numpy as np 
x = np.ones(5)  
print(x)

#输出如下：
[1. 1. 1. 1. 1.]
```





##### 3.4.3.2 示例2 

```
import  numpy  as  np 
x = np.ones([2,2],dtype = int)
print(x)

#输出如下:

[[1 1]
[1 1]]
```





### 3.5  NumPy来自现有数据的数组
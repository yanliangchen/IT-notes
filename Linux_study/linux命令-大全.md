**摘自菜鸟教程 http://www.runoob.com/linux/linux-command-manual.html**



## 1.cat 

### 参数说明：

 

**-n 或 --number**：由 1 开始对所有输出的行数编号。

 

**-b 或 --number-nonblank**：和 -n 相似，只不过对于空白行不编号。

 

**-s 或 --squeeze-blank**：当遇到有连续两行以上的空白行，就代换为一行的空白行。

 

**-v 或 --show-nonprinting**：使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。

 

**-E 或 --show-ends** : 在每行结束处显示 $。

 

**-T 或 --show-tabs**: 将 TAB 字符显示为 ^I。

 

**-e** : 等价于 -vE。

 

 **-A, --show-all**：等价于 -vET。

 **-e：**等价于"-vE"选项；

 **-t：**等价于"-vT"选项；

 

### 实例：

 

把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里：

 

```
cat -n textfile1 > textfile2
```

 

 把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：

 

```
cat -b textfile1 textfile2 >> textfile3
```

 

清空 /etc/test.txt 文档内容：

 

```
cat /dev/null > /etc/test.txt
```

 

cat 也可以用来制作镜像文件。例如要制作软盘的镜像文件，将软盘放好后输入：

 

```
cat /dev/fd0 > OUTFILE
```

 

相反的，如果想把 image file 写到软盘，输入：

 

```
cat IMG_FILE > /dev/fd0
```

 

**注**：

 

- \1. OUTFILE 指输出的镜像文件名。
- \2. IMG_FILE 指镜像文件。
- \3. 若从镜像文件写回 device 时，device 容量需与相当。
- \4. 通常用制作开机磁片。





## 2.chattr(改变文件属性)

Linux chattr命令用于改变文件属性。

这项指令可改变存放在ext2文件系统上的文件或目录属性，这些属性共有以下8种模式：

1. a：让文件或目录仅供附加用途。
2. b：不更新文件或目录的最后存取时间。
3. c：将文件或目录压缩后存放。
4. d：将文件或目录排除在倾倒操作之外。
5. i：不得任意更动文件或目录。
6. s：保密性删除文件或目录。
7. S：即时更新文件或目录。
8. u：预防意外删除。





### 参数：

　　-R  递归处理，将指定目录下的所有文件及子目录一并处理。

　　-v<版本编号>  设置文件或目录版本。

　　-V  显示指令执行过程。

　　+<属性>  开启文件或目录的该项属性。

　　-<属性>  关闭文件或目录的该项属性。

　　=<属性>  指定文件或目录的该项属性。

### 示例：

用chattr命令防止系统中某个关键文件被修改,被删除：

 

```
chattr +i /etc/resolv.conf
```

 

```
lsattr /etc/resolv.conf
```

 会显示如下属性

```
----i-------- /etc/resolv.conf
```

  

让某个文件只能往里面追加数据，但不能删除，适用于各种日志文件：

 

```
chattr +a /var/log/messages
```



如果取消给加的指定指令，则用-参数

```
chattr -i ./textfile2
```





## 3.chgrp命令(改变属组)、

### 参数:

```
参数说明
　　-c或--changes 效果类似"-v"参数，但仅回报更改的部分。
　　-f或--quiet或--silent 　不显示错误信息。
　　-h或--no-dereference 　只对符号连接的文件作修改，而不更动其他任何相关文件。
　　-R或--recursive 　递归处理，将指定目录下的所有文件及子目录一并处理。
　　-v或--verbose 　显示指令执行过程。
　　--help 　在线帮助。
　　--reference=<参考文件或目录> 　把指定文件或目录的所属群组全部设成和参考文件或目录的所属群组相同。
　　--version 　显示版本信息。
```



### 实例：

//把log2012.log给改变成bin属组

```
chgrp -v bin log2012.log
```



//根据指定文件来对该文件进行改变和它一样的属组

```
//改变了a   和c一样
chgrp --reference=c.txt  a.txt
```



## 4.chmod(改变文件权限)

### 参数:

```
其中：
u 表示该文件的拥有者，g 表示与该文件的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。
+ 表示增加权限、- 表示取消权限、= 表示唯一设定权限。
r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行。
其他参数说明：
-c : 若该文件权限确实已经更改，才显示其更改动作
-f : 若该文件权限无法被更改也不要显示错误讯息
-v : 显示权限变更的详细资料
-R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更)
--help : 显示辅助说明
--version : 显示版本
```



### 示例:

//将文件file1.txt设为所有人皆可读取:

```
chmod ugo+r  file1.txt
```



//将文件file1.txt设为所有人皆可读取:

```
chmod a+r file1.txt
```



//将文件file1.txt 和file2.txt设为该文件拥有者，与其所属同一个群体者可写入，但其他以外的人则不可写入:

```
chmod ug+w,o-w file1.txt file2.txt
```



//将ex1.py设定为只有该文件拥有者可以执行:

```
chmod u+x ex1.py
```



// 将目前目录下的所有文件与子目录皆设为任何人读取:

```
chmod -R a+r *
```



//此外chmod也可以用数字来表示权限如 :

 

```
chmod 777 file
```

 

//语法为：

```
chmod abc file

其中a,b,c各为一个数字，分别表示User、Group、及Other的权限。
r=4，w=2，x=1
若要rwx属性则4+2+1=7；
若要rw-属性则4+2=6；
若要r-x属性则4+1=5。
```


//a是赋予权限给所有人 看赋予哪些权限的话后面可以选择

```
chmod a=rwx file
```



//给demo.sh变成可执行文件

```
chmod +x demo.sh
```

若用chmod 4755 filename可使此程序具有root的权限



## 5.awk

AWK是一种处理文本文件的语言，是一个强大的文本分析工具。



### 参数:

```
-F fs or --field-separator fs
指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:。 
-v var=value or --asign var=value
赋值一个用户定义变量。 
-f scripfile or --file scriptfile
从脚本文件中读取awk命令。 
-mf nnn and -mr nnn
对nnn值设置内在限制，-mf选项限制分配给nnn的最大块数目；-mr选项限制记录的最大数目。这两个功能是Bell实验室版awk的扩展功能，在标准awk中不适用。 
-W compact or --compat, -W traditional or --traditional
在兼容模式下运行awk。所以gawk的行为和标准的awk完全一样，所有的awk扩展都被忽略。 
-W copyleft or --copyleft, -W copyright or --copyright
打印简短的版权信息。 
-W help or --help, -W usage or --usage
打印全部awk选项和每个选项的简短说明。 
-W lint or --lint
打印不能向传统unix平台移植的结构的警告。 
-W lint-old or --lint-old
打印关于不能向传统unix平台移植的结构的警告。 
-W posix
打开兼容模式。但有以下限制，不识别：/x、函数关键字、func、换码序列以及当fs是一个空格时，将新行作为一个域分隔符；操作符**和**=不能代替^和^=；fflush无效。 
-W re-interval or --re-inerval
允许间隔正则表达式的使用，参考(grep中的Posix字符类)，如括号表达式[[:alpha:]]。 
-W source program-text or --source program-text
使用program-text作为源代码，可与-f命令混用。 
-W version or --version
打印bug报告信息的版本。
```



### 实例:

//log.txt

```
2 this is a test
3 Are you like awk
This's a test
10 There are orange,apple,mongo
```



#### 1. 选择文本输出，和格式化输出

```
# 每行按空格或TAB分割，输出文本中的1、4项
 $ awk '{print $1,$4}' log.txt
 ---------------------------------------------
 2 a
 3 like
 This's
 10 orange,apple,mongo
 # 格式化输出
 $ awk '{printf "%-8s %-10s\n",$1,$4}' log.txt
 ---------------------------------------------
 2        a
 3        like
 This's
 10       orange,apple,mongo
```



#### 2. 使用','分割

```
 $  awk -F, '{print $1,$2}'   log.txt
 ---------------------------------------------
 2 this is a test
 3 Are you like awk
 This's a test
 10 There are orange apple

#或者使用内建变量
 $ awk 'BEGIN{FS=","} {print $1,$2}'     log.txt
 ---------------------------------------------
 2 this is a test
 3 Are you like awk
 This's a test
 10 There are orange apple

#使用多个分隔符，先使用空格分割，然后对分割结果再使用“，”分割
awk -F '[,]' '{print $1,$2,$5}' log.txt

```



#### 3.设置变量

```
 $ awk -va=1 '{print $1,$1+a}' log.txt
 ---------------------------------------------
 2 3
 3 4
 This's 1
 10 11
 $ awk -va=1 -vb=s '{print $1,$1+a,$1b}' log.txt
 ---------------------------------------------
 2 3 2s
 3 4 3s
 This's 1 This'ss
 10 11 10s
```



#### 4.运算符

| = += -= *= /= %= ^= **= | 赋值                             |
| ----------------------- | -------------------------------- |
| ?:                      | C条件表达式                      |
| \|\|                    | 逻辑或                           |
| &&                      | 逻辑与                           |
| ~ ~!                    | 匹配正则表达式和不匹配正则表达式 |
| < <= > >= != ==         | 关系运算符                       |
| 空格                    | 连接                             |
| + -                     | 加，减                           |
| * / %                   | 乘，除与求余                     |
| + - !                   | 一元加，减和逻辑非               |
| ^ ***                   | 求幂                             |
| ++ --                   | 增加或减少，作为前缀或后缀       |
| $                       | 字段引用                         |
| in                      | 数组成员                         |



##### 4.1.过滤

//过滤第一列大于2的行

``` 
$ awk '$1>2' log.txt
```



//过滤第一列等于2的行

```
$ awk '$1==2 {print $1,$3}' log.txt
#输出
2 is 
```



//过滤第一列大于2并且第二列等于'Are'的行

```
$ awk '$1>2 && $2=="Are" {print $1,$2,$3}' log.txt    #命令
#输出
3 Are you
```



#### 5. 内建变量(文本内容做统计)

| $n          | 当前记录的第n个字段，字段间由FS分隔                        |
| ----------- | ---------------------------------------------------------- |
| $0          | 完整的输入记录                                             |
| ARGC        | 命令行参数的数目                                           |
| ARGIND      | 命令行中当前文件的位置(从0开始算)                          |
| ARGV        | 包含命令行参数的数组                                       |
| CONVFMT     | 数字转换格式(默认值为%.6g)ENVIRON环境变量关联数组          |
| ERRNO       | 最后一个系统错误的描述                                     |
| FIELDWIDTHS | 字段宽度列表(用空格键分隔)                                 |
| FILENAME    | 当前文件名                                                 |
| FNR         | 各文件分别计数的行号                                       |
| FS          | 字段分隔符(默认是任何空格)                                 |
| IGNORECASE  | 如果为真，则进行忽略大小写的匹配                           |
| NF          | 一条记录的字段的数目                                       |
| NR          | 已经读出的记录数，就是行号，从1开始                        |
| OFMT        | 数字的输出格式(默认值是%.6g)                               |
| OFS         | 输出记录分隔符（输出换行符），输出时用指定的符号代替换行符 |
| ORS         | 输出记录分隔符(默认值是一个换行符)                         |
| RLENGTH     | 由match函数所匹配的字符串的长度                            |
| RS          | 记录分隔符(默认是一个换行符)                               |
| RSTART      | 由match函数所匹配的字符串的第一个位置                      |
| SUBSEP      | 数组下标分隔符(默认值是/034)                               |



```
//输出一些文件的内容统计，会有专用的名词
$ awk 'BEGIN{printf "%4s %4s %4s %4s %4s %4s %4s %4s %4s\n","FILENAME","ARGC","FNR","FS","NF","NR","OFS","ORS","RS";printf "---------------------------------------------\n"} {printf "%4s %4s %4s %4s %4s %4s %4s %4s %4s\n",FILENAME,ARGC,FNR,FS,NF,NR,OFS,ORS,RS}'  log.txt
FILENAME ARGC  FNR   FS   NF   NR  OFS  ORS   RS
---------------------------------------------
log.txt    2    1         5    1
log.txt    2    2         5    2
log.txt    2    3         3    3
log.txt    2    4         4    4


$ awk -F\' 'BEGIN{printf "%4s %4s %4s %4s %4s %4s %4s %4s %4s\n","FILENAME","ARGC","FNR","FS","NF","NR","OFS","ORS","RS";printf "---------------------------------------------\n"} {printf "%4s %4s %4s %4s %4s %4s %4s %4s %4s\n",FILENAME,ARGC,FNR,FS,NF,NR,OFS,ORS,RS}'  log.txt
FILENAME ARGC  FNR   FS   NF   NR  OFS  ORS   RS
---------------------------------------------
log.txt    2    1    '    1    1
log.txt    2    2    '    1    2
log.txt    2    3    '    2    3
log.txt    2    4    '    1    4


# 输出顺序号 NR, 匹配文本行号（你想要的一些内容）
$ awk '{print NR,FNR,$1,$2,$3}' log.txt
---------------------------------------------
1 1 2 this is
2 2 3 Are you
3 3 This's a test
4 4 10 There are

# 指定输出分割符（$1和$2为他俩之间,$5如果内容不足5条，那么则只分割出满足条件的行数
$  awk '{print $1,$2,$5}' OFS=" $ "  log.txt
---------------------------------------------
2 $ this $ test
3 $ Are $ awk
This's $ a $
10 $ There $
```



#### 6.使用正则，字符串匹配

```
# 输出第二列包含 "th"，并打印第二列与第四列
$ awk '$2 ~ /th/ {print $2,$4}' log.txt
---------------------------------------------
this a
```



##### 6.1**~ 表示模式开始。//中是模式**

``` 
# 输出包含"re" 的行
$ awk '/re/ ' log.txt
---------------------------------------------
3 Are you like awk
10 There are orange,apple,mongo
```



#### 7. 忽略大小写(过滤出this)

```
$ awk 'BEGIN{IGNORECASE=1} /this/' log.txt
---------------------------------------------
2 this is a test
This's a test
```



#### 8. 模式取反(没有th的第2列和第4列)

```
$ awk '$2 !~ /th/ {print $2,$4}' log.txt
---------------------------------------------
Are like
a
There orange,apple,mongo
$ awk '!/th/ {print $2,$4}' log.txt
---------------------------------------------
Are like
a
There orange,apple,mongo
```



#### 9.awk脚本

```
$ awk '$2 !~ /th/ {print $2,$4}' log.txt
---------------------------------------------
Are like
a
There orange,apple,mongo
$ awk '!/th/ {print $2,$4}' log.txt
---------------------------------------------
Are like
a
There orange,apple,mongo
```



假设有这么一个文件（学生成绩表）： 

```
$ cat score.txt
Marry   2143 78 84 77
Jack    2321 66 78 45
Tom     2122 48 77 71
Mike    2537 87 97 95
Bob     2415 40 57 62
```

**我们的awk脚本如下**

```
$ cat cal.awk
#!/bin/awk -f
#运行前
BEGIN {
    math = 0
    english = 0
    computer = 0
 
    printf "NAME    NO.   MATH  ENGLISH  COMPUTER   TOTAL\n"
    printf "---------------------------------------------\n"
}
#运行中
{
    math+=$3
    english+=$4
    computer+=$5
    printf "%-6s %-6s %4d %8d %8d %8d\n", $1, $2, $3,$4,$5, $3+$4+$5
}
#运行后
END {
    printf "---------------------------------------------\n"
    printf "  TOTAL:%10d %8d %8d \n", math, english, computer
    printf "AVERAGE:%10.2f %8.2f %8.2f\n", math/NR, english/NR, computer/NR
}
```





## 6.chown(指定文件的拥有者改为指定的用户或组)

Linux/Unix 是多人多工操作系统，所有的文件皆有拥有者。利用 chown 将指定文件的拥有者改为指定的用户或组，用户可以是用户名或者用户ID；组可以是组名或者组ID；文件是以空格分开的要改变权限的文件列表，支持通配符。 。

一般来说，这个指令只有是由系统管理者(root)所使用，一般使用者没有权限可以改变别人的文件拥有者，也没有权限可以自己的文件拥有者改设为别人。只有系统管理者(root)才有这样的权限。



### 参数：

```

```



### 示例:

```
//将文件 file1.txt 的拥有者设为 users 群体的使用者 jessie :
chown users:jessie file1.txt
将目前目录下的所有文件与子目录的拥有者皆设为 users 群体的使用者 lamport :
chown -R lamport:users *
```





## 7. cksum命令

Linux cksum命令用于检查文件的CRC是否正确。确保文件从一个系统传输到另一个系统的过程中不被损坏。

CRC是一种排错检查方式，该校验法的标准由CCITT所指定，至少可检测到99.998%的已知错误。

指定文件交由指令"cksum"进行校验后，该指令会返回校验结果供用户核对文件是否正确无误。若不指定任何文件名称或是所给予的文件名为"-"，则指令"cksum"会从标准输入设备中读取数据。



### 参数：

```
--help：在线帮助。
--version：显示版本信息。
文件…:需要进行检查的文件路径
```



### 示例：

```
使用指令"cksum"计算文件"testfile1"的完整性，输入如下命令：
$ cksum testfile1       
以上命令执行后，将输出校验码等相关的信息，具体输出信息如下所示： 
1263453430 78 testfile1         //输出信息 
上面的输出信息中，"1263453430"表示校验码，"78"表示字节数。
```



## 8. grep 

作为linux中最为常用的三大文本（awk，sed，grep）处理工具之一，掌握好其用法是很有必要的。

首先谈一下grep命令的常用格式为：grep  [选项]  ”模式“  [文件]

grep家族总共有三个：grep，egrep，fgrep。



### 参数:

```
-a 或 --text : 不要忽略二进制的数据。 
-A<显示行数> 或 --after-context=<显示行数> : 除了显示符合范本样式的那一列之外，并显示该行之后的内容。 
-b 或 --byte-offset : 在显示符合样式的那一行之前，标示出该行第一个字符的编号。 
-B<显示行数> 或 --before-context=<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前的内容。 
-c 或 --count : 计算符合样式的列数。 
-C<显示行数> 或 --context=<显示行数>或-<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前后的内容。 
-d <动作> 或 --directories=<动作> : 当指定要查找的是目录而非文件时，必须使用这项参数，否则grep指令将回报信息并停止动作。
-e<范本样式> 或 --regexp=<范本样式> : 指定字符串做为查找文件内容的样式。 
-E 或 --extended-regexp : 将样式为延伸的普通表示法来使用。 
-f<规则文件> 或 --file=<规则文件> : 指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式。 
-F 或 --fixed-regexp : 将样式视为固定字符串的列表。 
-G 或 --basic-regexp : 将样式视为普通的表示法来使用。 
-h 或 --no-filename : 在显示符合样式的那一行之前，不标示该行所属的文件名称。 
-H 或 --with-filename : 在显示符合样式的那一行之前，表示该行所属的文件名称。 
-i 或 --ignore-case : 忽略字符大小写的差别。 
-l 或 --file-with-matches : 列出文件内容符合指定的样式的文件名称。 
-L 或 --files-without-match : 列出文件内容不符合指定的样式的文件名称。 
-n 或 --line-number : 在显示符合样式的那一行之前，标示出该行的列数编号。 
-q 或 --quiet或--silent : 不显示任何信息。 
-r 或 --recursive : 此参数的效果和指定"-d recurse"参数相同。 
-s 或 --no-messages : 不显示错误信息。 
-v 或 --revert-match : 显示不包含匹配文本的所有行。 
-V 或 --version : 显示版本信息。 
-w 或 --word-regexp : 只显示全字符合的列。 
-x --line-regexp : 只显示全列符合的列。 
-y : 此参数的效果和指定"-i"参数相同。 
```



### 8.1 过滤文件的内容，返回所有的你要的内容

1.文本内容  

```
$ cat file 
testfile1:This a Linux testfile! #列出testfile1 文件中包含test字符的行  
testfile_2:This is a linux testfile! #列出testfile_2 文件中包含test字符的行  
testfile_2:Linux test #列出testfile_2 文件中包含test字符的行 
```



结果如下所示 

```
$ grep test test* #查找前缀有“test”的文件包含“test”字符串的文件  
testfile1:This a Linux testfile! #列出testfile1 文件中包含test字符的行  
testfile_2:This is a linux testfile! #列出testfile_2 文件中包含test字符的行  
testfile_2:Linux test #列出testfile_2 文件中包含test字符的行 
```



### 8.2 递归查找文件内容，返回文件内容和所在目录

```
$ grep -r update /etc/acpi #以递归的方式查找“etc/acpi”  
#下包含“update”的文件  
/etc/acpi/ac.d/85-anacron.sh:# (Things like the slocate updatedb cause a lot of IO.)  
Rather than  
/etc/acpi/resume.d/85-anacron.sh:# (Things like the slocate updatedb cause a lot of  
IO.) Rather than  
/etc/acpi/events/thinkpad-cmos:action=/usr/sbin/thinkpad-keys--update 


$ grep -i user1 /etc/passwd #忽略大小写
```





### 8.3 grep 多个关键字并列查找

```
egrep -w 'user1|USER1' /etc/passwd #过滤的字符串全部返回
```



### 8.4 统计grep 查找出来的行数

```
//统计所匹配出来的行数的总数
grep -c 'user1' /etc/passwd
```



### 8.5 grep反向查找只显示不匹配的行

```
grep -v  user1 /etc/passwd
```



### 8.6 linux管道符和grep命令的搭建使用

```
//返回结果
cat  文件 | grep -i '要找的内容' 
```



### 8.7 找指定内容返回内容所在的文件的路径

```
//只列出匹配的文件名
grep -l '内容' /root/*

//列出不匹配的文件名
grep -L '内容' /root/*

```



### 8.8  grep '[a-z]'   aa 

```
$ grep '[a-z]' aa // 显示所有包含每个字符串至少有5个连续小写字符的字符串的行。
```



### 8.9 显示所有以d开头的文件中包含test的行。

```
$ grep 'test' d* // 显示所有以d开头的文件中包含test的行。
```





## 10. sed(如果需要操作源文件，则需要加上-i操作)

### 10.1删除操作

```
//删除第2行
$sed '2d' 文件
```

```
//删除example文件的第二行到末尾所有行
$sed '2,$d' example
```

```
//删除example文件的最后一行
$sed '$d' example
```

```
$sed '/test/'d example
```



### 10.2 p输出

| 命令    | 完整示例                  | 说明                                             |
| ------- | ------------------------- | ------------------------------------------------ |
| p       | sed  -n 'p' 1.txt         | 输出1.txt的所有行                                |
| 2p      | sed  -n '2p' 1.txt        | 输出1.txt的第二行                                |
| 2，5p   | sed  -n '2，5p' 1.txt     | 输出1.txt的第二行到第五行                        |
| 2，+5p  | sed  -n '2，+5p' 1.txt    | 输出1.txt的第二行和第二行以后的5行               |
| 1～2p   | sed  -n '1～2p' 1.txt     | 输出第一行，每隔两行输出一行，也就是输出奇数行   |
| 2～2p   | sed  -n '1～2p' 1.txt     | 输出第二行，每隔两行输出一行，也就是输出偶数数行 |
| /正则/p | sed  -n '/^[0-9]/p' 1.txt | 输出1.txt以数字开头的行                          |
| $=      | sed  -n '$=' 1.txt        | 输出1.txt的行数                                  |



### 10.3 s替换

| 命令           | 完整示例                    | 说明                                                         |
| -------------- | --------------------------- | ------------------------------------------------------------ |
| s/old/new/     | sed   's/old/new/' 1.txt    | 删除1.txt中每行的第一个old都替换成new                        |
| s/old/new/2    | sed   's/old/new/' 1.txt    | 删除1.txt中每行的第二个old都替换成new                        |
| s/old/new/g    | sed   's/old/new/g' 1.txt   | 删除1.txt中每行的每一个old都替换成new                        |
| s/old//        | sed   's/old//' 1.txt       | 删除1.txt中每行的第一个old都替换成空也就是把old删除          |
| s/old/&s/      | sed   's/old/&s/' 1.txt     | 删除1.txt中每行的第一个old都替换成olds &代表前面查找的字符串 |
| 4，7s/^/#/     | sed   '4,7s/^/#/' 1.txt     | 删除1.txt中4-7行开头加上#  也就是批量添加注释                |
| 4，7s/^#an/an/ | sed   '4,7s/^#an/an/' 1.txt | 删除1.txt中4-7行以#an开头的行去掉#                           |



### 10.4 i/a/c插入

| 命令   | 完整示例                   | 说明                                 |
| ------ | -------------------------- | ------------------------------------ |
| 行号 i | sed   '2i123' 1.txt        | 在1.txt的第二行前面插入123           |
| 正则 i | sed   '/^[0-9]/i123' 1.txt | 在1.txt中所有数字开头的行前面插入123 |
| a      | 在行后插入                 | 命令格式和i相同                      |
| c      | 替换该行                   | 命令格式和i相同                      |



### 10.5 sed高级应用

| 命令        | 完整示例                         | 说明                                               |
| ----------- | -------------------------------- | -------------------------------------------------- |
| 行号r       | sed  -i  '2r 2.txt' 1.txt        | 在1.txt中第二行后面插入2.txt的内容                 |
| 行号，行号r | sed  -i  '2，5r 2.txt' 1.txt     | 在1.txt中第二行到第五行每行后面插入一遍2.txt的内容 |
| /正则/r     | sed  -i  '/^[0-9]/r 2.txt' 1.txt | 在1.txt中以数字开头的行后每行面插入一遍2.txt的内容 |
| w           | sed   '2w 3.txt' 1.txt           | 在1.txt中第二行导出为3.txt的内容                   |
| w           | sed   '2,5w 3.txt' 1.txt         | 在1.txt中第二行到第五行导出3.txt的内容             |
| /正则/r     | sed  -i  '/^[0-9]/w 2.txt' 1.txt | 在1.txt中以数字开头的行导出为3.txt的内容           |







## 11.  防火墙操作

//查看状态，看电脑上是否已经安装

sysyemctl  status  firewalld

1. `#yum install firewalld  //安装firewalld 防火墙`

2. `#systemctl start firewalld.service   //开启防火墙`

3. `#systemctl stop firewalld.service   //关闭防火墙`

4. `# systemctl enable firewalld.service  //设置开机自动启动`

5. `# systemctl disable firewalld.service   //设置关闭开机制动启动`

6. `#firewall-cmd --reload  //在不改变状态的条件下重新加载防火墙`

7. `启用某个服务`

   `# firewall-cmd --zone=public --add-service=https   //临时`

   `# firewall-cmd --permanent --zone=public --add-service=https  //永久`

8. `开启某个端口`

   `#firewall-cmd --permanent --zone=public --add-port=8080-8081/tcp  //永久`

   `#firewall-cmd  --zone=public --add-port=8080-8081/tcp   //临时`

9. `查看开启的端口和服务`

   `#firewall-cmd --permanent --zone=public --list-services    //服务空格隔开  例如 dhcpv6-client https ss   `

   `#firewall-cmd --permanent --zone=public --list-ports //端口空格隔开  例如  8080-8081/tcp 8388/tcp 80/tcp`

10. `#systemctl restart firewalld.service  //修改配置后需要重启服务使其生效`

11. `firewall-cmd --zone=public --query-port=8080/tcp  //查看服务是否生效（例：添加的端口为8080)`
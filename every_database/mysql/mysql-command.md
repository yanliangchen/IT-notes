**MySQL服务的配置和使用**
修改MySQL管理员的口令：mysqladmin –u root password 密码字符串 
如：mysqldmin –u root password 111111
连接MySQL服务器，使用命令： mysql [-h 主机名或IP地址] [-u 用户名] [-p] 
如：mysql –u root –p
如已有密码需修改root密码用命令: mysqladmin –u root –p password 新密码字符串 
如：mysqladmin –u root –p password 111111

**创建数据库格式为：CREATE DATABASE 数据库名称；**

如：mysql>create database abc; 默认创建数据库保存在/var/lib/mysql中
查看数据库是 mysql>show abc;
选择数据库是 USE 数据库名称; 如：mysql>use abc;
删除数据库是 DROP DATABASE 数据库名称； 如：mysql>drop database abc;

**数据库的创建和删除**

创建表是 CREATE TABLE 表名称(字段1，字段2，…[表级约束]) [TYPE=表类型]；
其中字段(1,2 )格式为:字段名 字段类型 [字段约束]
如创建一个表student，如下：

```
mysql>create table student (
sno varchar(7) not null, 字段不允许为空
sname varchar (20 )not null,
ssex char (1) default ‘t’,
sbirthday date,
sdepa char (20),
primary key (sno) 表的主键
);
```

可用describe命令查看表的结构。

默认表的类型为MYISAM，并在/var/lib/mysql/abc 目录下建立student.frm(表定义文件)，student.MDY(数据文件)，stedent.MYI(索引文件)。
复制表 CREATE TABLE 新表名称 LIKE 原表名称；
如：mysql>create table xtable like student;
删除表 DROP TABLE 表名称1[表名称2…];
如：mysql> drop table xtale;



**修改表 ALTER TABLE 表名称 更改动作1[动作2]；**

动作有ADD(增加) DROP(删除)CHANGE、MODIFY(更改字段名和类型)RENAME

```
增加字段：mysql>alter table student add saddress varchar(25);
更改字段名和字段类型： mysql>alter table student change saddress sremark test;
即使不更改字段类型也要给出字段类型如：
mysql>alter table student change saddress sremark varchar (25);
更改字段类型　：mysql> alter table student modify sremark varchar(25);
删除字段：mysql>alter table student drop sremark；
更改表名称： mysql>alter table student rename to xs；
```



**表中数据的插入、删除和修改**

插入记录： INSERT INTO 表名称（字段名1,字段名2…
VALUES(字段1的值，字段2的值
如：mysql>insert into student (sno,sname,ssex,sbirthday,sdepa)
values(‘0321001’,’Liu Tao’,dagault,19870201,’math’);

查看表 mysql>select * from student;
插入与前面相同的记录，可用insert命令的缩写格式，
如: mysql>insert into student values (‘0321001’, ‘Liu Tao’, default, 19870201, ‘mth’);

如果字段名列表中没有给出表中的某些字段，那么这些字段设置为默认值，
如：mysql>insert into student (sno,sname,sbirthday)
values(‘0321002’,’Wang Jun’,1870112);

一个单独的insert语句中可使用多个valuse字句，插入多条记录，
如：mysql>insert into student values
(‘0322001’, ‘Zhang Liaoyun’, ‘f’ 1971102,’computer’),
(‘0322002’, ‘Li Ming’, ‘t’ 1971105,’computer’);

删除记录： DELETE FROM 表名称 WHERE 条件表达式；
如：mysql>delete from student where sno=’0321002’;

删除student表中sno字段值前4位为‘0322’的记录
如：mysql>delete from student where left (sno,4)=’0322’;

删除所以记录，可以不带where字句
如：mysql>delete from student;

删除所以记录可以用命令truncate 删除表，然后重建表，所以比delete命令快
如：mysql>truncate table student;

修改记录 UPDATE 表名称 SET 字段名1=字段值1
WHERE 条件表达式
如： mysql>update student set sbirthday=1920113, sdepa=’math’ where sno=’0321002’;



**索引的创建与删除**

在创建表的同时创建索引
创建表时，可用INDEX字句或UNIQUE(字段值必须惟一)字句创建索引
如：创建课程表course, 课程编号cno字段为主键，课程名称cname字段创建一个名为can的索引
mysql>create table course(
cno varchar(5) not null,
cname varchar(30) not null,
teacher varchar(20),
primary key (cno),
index can (cname)
);

 

1、创建主键索引   括号里的是字段

alter table table_name add constraint index_name primary key (col1); 

2、创建唯一键索引 

create unique index uk_name on table_name (col2); 

3、创建普通索引 

create index index_name on table_name (col3); 



4 、删除索引 DROP INDEX 索引 ON表名称；
如：mysql>drop index sna on student;

//补充一下知识,温故而知新。

```
1、普通索引
   普通索引（由关键字KEY或INDEX定义的索引）的唯一任务是加快对数据的访问速度。因此，应该只为那些最经常出现在查询条件（WHEREcolumn=）或排序条件（ORDERBYcolumn）中的数据列创建索引。只要有可能，就应该选择一个数据最整齐、最紧凑的数据列（如一个整数类型的数据列）来创建索引。
2、唯一索引
　　普通索引允许被索引的数据列包含重复的值。比如说，因为人有可能同名，所以同一个姓名在同一个“员工个人资料”数据表里可能出现两次或更多次。
如果能确定某个数据列将只包含彼此各不相同的值，在为这个数据列创建索引的时候就应该用关键字UNIQUE把它定义为一个唯一索引。这么做的好处：一是简化了MySQL对这个索引的管理工作，这个索引也因此而变得更有效率；二是MySQL会在有新记录插入数据表时，自动检查新记录的这个字段的值是否已经在某个记录的这个字段里出现过了；如果是，MySQL将拒绝插入那条新记录。也就是说，唯一索引可以保证数据记录的唯一性。事实上，在许多场合，人们创建唯一索引的目的往往不是为了提高访问速度，而只是为了避免数据出现重复。
3.主索引也叫做（聚集索引）（主键：若某一个属性组（注意是组）能唯一标识一条记录，该属性组就是一个主键。主键不能重复，且只能有一个，也不允许为空。定义主键主要是为了维护关系数据库的完整性。）
　　在前面已经反复多次强调过：必须为主键字段创建一个索引，这个索引就是所谓的"主索引"。主索引与唯一索引的唯一区别是：前者在定义时使用的关键字是PRIMARY而不是UNIQUE。 
4.外键索引 （外键: 如果为某个外键字段定义了一个外键约束条件，MySQL就会定义一个内部索引来帮助自己以最有效率的方式去管理和使用外键约束条件。 ）
　　如果为某个外键字段定义了一个外键约束条件，MySQL就会定义一个内部索引来帮助自己以最有效率的方式去管理和使用外键约束条件。 
5.复合索引()
（4）组合索引
  为了形象地对比单列索引和组合索引，为表添加多个字段：
CREATE TABLE mytable( ID INT NOT NULL, username VARCHAR(16) NOT NULL, city VARCHAR(50) NOT NULL, age INT NOT NULL ); 为了进一步榨取MySQL的效率，就要考虑建立组合索引。就是将 name, city, age建到一个索引里：
ALTER TABLE mytable ADD INDEX name_city_age (name(10),city,age); 建表时，usernname长度为 16，这里用 10。这是因为一般情况下名字的长度不会超过10，这样会加速索引查询速度，还会减少索引文件的大小，提高INSERT的更新速度。
如果分别在 usernname，city，age上建立单列索引，让该表有3个单列索引，查询时和上述的组合索引效率也会大不一样，远远低于我们的组合索引。虽然此时有了三个索引，但MySQL只能用到其中的那个它认为似乎是最有效率的单列索引。
建立这样的组合索引，其实是相当于分别建立了下面三组组合索引：
usernname,city,age usernname,city usernname 为什么没有 city，age这样的组合索引呢？这是因为MySQL组合索引“最左前缀”的结果。简单的理解就是只从最左面的开始组合。并不是只要包含这三列的查询都会用到该组合索引，下面的几个SQL就会用到这个组合索引：
SELECT * FROM mytable WHREE username="admin" AND city="郑州" SELECT * FROM mytable WHREE username="admin" 而下面几个则不会用到：
SELECT * FROM mytable WHREE age=20 AND city="郑州" SELECT * FROM mytable WHREE city="郑州"


```



**索引的建立时机，不足，注意事项**

```
1.建立索引的时机
一般来说，在WHERE和JOIN中出现的列需要建立索引，但也不完全如此，因为MySQL只对<，<=，=，>，>=，BETWEEN，IN，以及某些时候的LIKE才会使用索引。例如：
SELECT t.Name FROM mytable t LEFT JOIN mytable m ON t.Name=m.username WHERE m.age=20 AND m.city='郑州' 此时就需要对city和age建立索引，由于mytable表的userame也出现在了JOIN子句中，也有对它建立索引的必要。
刚才提到只有某些时候的LIKE才需建立索引。因为在以通配符%和_开头作查询时，MySQL不会使用索引。例如下句会使用索引：
SELECT * FROM mytable WHERE username like'admin%' 而下句就不会使用：
SELECT * FROM mytable WHEREt Name like'%admin' 因此，在使用LIKE时应注意以上的区别。
2.索引的不足之处
上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：
◆虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。
◆建立索引会占用磁盘空间的索引文件。一般情况这个问题不太严重，但如果你在一个大表上创建了多种组合索引，索引文件的会膨胀很快。
索引只是提高效率的一个因素，如果你的MySQL有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。
3.使用索引的注意事项
使用索引时，有以下一些技巧和注意事项：
◆索引不会包含有NULL值的列
只要列中包含有NULL值都将不会被包含在索引中，复合索引中只要有一列含有NULL值，那么这一列对于此复合索引就是无效的。所以我们在数据库设计时不要让字段的默认值为NULL。
◆使用短索引
对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个CHAR(255)的列，如果在前10个或20个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。
◆索引列排序
MySQL查询只使用一个索引，因此如果where子句中已经使用了索引的话，那么order by中的列是不会使用索引的。因此数据库默认排序可以符合要求的情况下不要使用排序操作；尽量不要包含多个列的排序，如果需要最好给这些列创建复合索引。
◆like语句操作
一般情况下不鼓励使用like操作，如果非使用不可，如何使用也是一个问题。like “%aaa%” 不会使用索引而like “aaa%”可以使用索引。
◆不要在列上进行运算
select * from users where YEAR(adddate)<2007; 将在每个行上进行运算，这将导致索引失效而进行全表扫描，因此我们可以改成
select * from users where adddate<‘2007-01-01’; 
◆不使用NOT IN和<>操作 
```

**创建新用户**

以MySQL管理员连接到数据库服务器： #mysql –u root –p
创建新用户guess并设置密码，同时可以从任何主机连接数据库服务器：
mysql>insert into mysql.user (host,user,password)
values (‘%’,’gusee’,password(‘guest’)); 使用password()函数，密码是加密的
重载MySQL授权表：mysql>flush privileges;
远程客户端连接数据库服务器 ：#mysql –h 192.168.0.50 –u guess –p 开放服务器的TCP断口3306



**查看当前用户可用数据库： show database** 

删除用户 mysql>delete from mysql.user where user=’guest’;

 mysql>flush privileges; 重载MySQL授权表 



更改用户密码
如：更改guset密码为123456
mysql>update mysql.user set password=password(‘123456’)
where user =’guset’;
mysql>flush privileges;
或者是 mysql>set password for guset@’%’=password(‘123456’);



**用户权限的设置** 

赋予权限

 mysql> grant select on dmc_db.*  to test;

 回收权限

 mysql> revoke  select on dmc_db.*  from  test;  //如果权限不存在会报错



 可使用多个权限同时赋予和回收，权限之间使用逗号分隔

 mysql> grant select，update，delete  ，insert  on dmc_db.*  to  test;



在表user、db和host中，所有字段声明为ENUM(‘N’,’Y’),默认是‘N’; 

在表tables_priv和columns_priv中，

权限字段声明为SET类型 修改授权表中的访问权限有两中方法，

一是使用 INSERT、UPDATE和DELETE等DML语句， 

另一中是GRANT和GRVOKE语句 使用GRANT语句授权： 

GRANT 权限列表 [(字段列表)] on 数据库名称.表名称 TO 用户名@域名或IP地址 [INDETIFIED BY ‘密码值’][WITH CRANT OPTION]; 



**授权用户不同级别的访问权限** 

如：新建用户tom,能从子网192.168.16.0访问数据库服务器，可以读取数据库xsxk,并能修改表course 中字段teacher的值 

mysql>grant select on xsxd.* to tom@’192.168.16.%’ indentifiend by ‘123456’;

 mysql>grant update(teacher) on xsxd.course to tom@’192.168.16.%’’ 

注意几点：数据库名称.表名称 用来设置权限运用的级别，有全局的（*.*）,指定数据库的（xsxd.*） 和指定表的（xsxd.student）; 

字段列表 设置权限运用中指定的表中的哪些字段，如update(cname,teacher) 权限列表 指定的权限与权限运行的级别有关，如有写权限（FILE、PROCESS、RELOAD、SHUTDOWN）作为管理权限用于全局级别；对于字段级别只能指定SELECT、INSERT、UPDATE、REFERENCES 



**授予用户管理权限的权利**

如：管理员授予拥护admin可以从本地连接数据库服务器，对数据库xsxk具有完全访问权限，并可以
将拥有的权限赋予其他用户
mysql>grant all on xsxd.* to admin@localhost indentified by ‘123456’ with grant option;
其中with grant option 子句表示拥护拥有的权限可以赋予其他用户。
mysql>qrant select on xsxd.student to bill@localhost; 授予bill用户权限
mysql>show grants for admin@localhost; 查看用户权限
使用REVOKE语句撤权
格式如下：
REVOKE 权限列表[(字段列表)] on数据库名称.表名称
FROM用户名@域名或IP地址
如：撤消用户admin@localhost 对数据库xsxd的创建、删除数据库及表的权限，不撤消用户赋予其它用户的权限
mysql>revoke create,drop on xsxd.* from admin@localhost;
mysql>revoke grant option on xsxd.* from admin@localhost;
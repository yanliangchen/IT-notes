# mysql之触发器 

**触发器**

​    MySQL语句在需要时被执行，存储过程也是如此。但是，如果你想要某条语句（或某些语句）在事件发生时自动执行，怎么办呢？例如：每当增加一个顾客到某个数据库表时，都检查其电话号码格式是否正确，州的缩写是否为大写；每当订购一个产品时，都从库存数量中减去订购的数量；无论何时删除一行，都在某个存档表中保留一个副本。

​    所有这些例子的共同之处是它们都需要在某个表发生更改时自动处理某个动作。这确切地说就是一个触发器。 触发器是MySQL 响应以下任意语句而自动执行任意其他的一条 MySQL语句（或位于BEGIN和 END语句之间的一组语句）

​        1、DELECT

​        2、INSERT

​        3、UPDATE

其他的mysql语句不支持触发器的。

 

**创建触发器**

​    在创建触发器时，需要给出 4条信息：

​        1、唯一的触发器名；

​        2、触发器关联的表

​        3、触发器应该响应的动作（ DELETE、INSERT 或UPDATE）

​        4、触发器何时执行（处理之前或之后）。

​    注意：保持每个数据库的触发器名唯一。

​    触发器用 CREATE TRIGGER语句创建。下面是一个简单的例子：



```
mysql> DELIMITER //
mysql> CREATE TRIGGER newproduct  AFTER  INSERT ON products
    -> FOR EACH ROW
    -> SELECT 'added ' INTO @ee;
    -> //
Query OK, 0 rows affected (0.05 sec)
```



​    CREATE TRIGGER用来创建名为newproduct的新触发器。触发器可在一个操作发生之前或之后执行，这里给出了 AFTER INSERT，所以此触发器将在 INSERT语句成功执行后执行。FOR EACH ROW是触发器的执行间隔，FOR EACH ROW子句通知触发器每隔一行执行一次动作，而不是对整个表执行一次。在这个例子中，文本 added将对每个插入的行显示一次。为了测试这个触发器，使用 INSERT语句添加一行或多行到products中，你将看到对每个成功的插入。

```
mysql> insert into products (prod_id, vend_id, prod_name, prod_price, prod_desc)
    -> values
    -> ('TNT3', 1002, 'liwei', 123.12, 'dudu jiushi ni')
    -> //
Query OK, 1 row affected (0.03 sec)
```

​    在使用select来查询变量ee,看看结果是什么

```
select @ee
//
```

​    结果是：

```
+------+
| @ee  |
+------+
| added     |
+------+
```

​    注意：只有表才支持触发器，视图不支持（临时表也不支持）。

​    触发器按每个表每个事件每次地定义，每个表每个事件每次只允许一个触发器。因此，每个表最多支持 6个触发器（每条INSERT、 UPDATE和DELETE的之前和之后）。单一触发器不能与多个事件或多个表关联，所以，如果你需要一个对 INSERT和UPDATE 操作执行的触发器，则应该定义两个触发器。

​    注意：如果BEFORE触发器失败，则 MySQL将不执行请求的操作。此外，如果 BEFORE触发器或语句本身失败， MySQL将不执行 AFTER触发器（如果有的话）。

 

**删除触发器**

​    现在，删除触发器的语法应该很明显了。为了删除一个触发器，可使用 DROP TRIGGER语句，如下所示：

```
DROP TRIGGER newproduct  
```

​    触发器不能更新或覆盖。为了修改一个触发器，必须先删除它，然后再重新创建。

 

**使用触发器**

​    在有了前面的基础知识后，我们现在来看所支持的每种触发器类型以及它们的差别。

 

**INSERT触发器**

​    INSERT触发器在INSERT 语句执行之前或之后执行。需要知道以下几点：

​        1、在INSERT触发器代码内，可引用一个名为 NEW的虚拟表，访问被插入的行。

​        2、在BEFORE INSERT触发器中， NEW中的值也可以被更新（允许更改被插入的值）；

​        3、对于 AUTO_INCREMENT列，NEW 在INSERT执行之前包含 0，在INSERT执行之后包含新的自动生成值。

​    下面举一个例子（一个实际有用的例子）。 AUTO_INCREMENT列具有MySQL自动赋予的值。第21章建议了几种确定新生成值的方法，但下面是一种更好的方法：

```
mysql> create trigger neworder after insert on orders
    -> for each row select new.order_num into @liwei;
```

​    此代码创建一个名为 neworder的触发器，它按照AFTER INSERTON orders执行。在插入一个新订单到 orders表时，MySQL 生成一个新订单号并保存到 order_num中。触发器利用select 语句的返回结果，从NEW. order_num取得这个值并赋值给变量liwei。此触发器必须按照 AFTER INSERT执行，因为在BEFORE INSERT语句执行之前，新order_num还没有生成。对于 orders的每次插入使用这个触发器将总是返回新的订单号。接着我们插入新的数据看看。

```
mysql> insert into orders(order_date,cust_id)
    -> values (Now(), 10001);
```

​    数据插入完成之后，我们来使用liwei变量来查询新的订单号。

```
mysql> select @liwei;
```

​    结果：



```
+--------+
| @liwei |
+--------+
|  20010 |
+--------+
1 row in set (0.02 sec)
```



​    orders 表包含3 个列。order_date 和 cust_id 必须给出，order_num由MySQL 自动生成，而现在 order_num 输出赋值给一个变量。然后利用这个变量做返回。

通常，将 BEFORE 用于数据验证和净化（目的是保证插入表中的数据确实是需要的数据）。本提示也适用于 UPDATE触发器。

 

**DELETE触发器**

​    DELETE 触发器在DELETE 语句执行之前或之后执行。需要知道以下两点：

​        1、在 DELETE触发器代码内，你可以引用一个名为 OLD 的虚拟表，访问被删除的行；

​        2、OLD 中的值全都是只读的，不能更新。

​    下面的例子演示使用 OLD 保存将要被删除的行到一个存档表中：

```
mysql> create trigger deleteorder before delete on orders
    -> for each row select old.order_num,old.order_date into @liwei,@tx;
```

​    删除一条数据：

```
mysql> delete from orders where order_num = 10002;
Query OK, 1 row affected (0.14 sec)
```

​    我们来看看查询上面声明的两个变量（liwei与tx）

```
mysql> select @liwei;
```

​    输出：

```
+--------+
| @liwei |
+--------+
|  10002 |
+--------+
```

​    或者是如下语句一条数据。



```
create trigger deleteorder before delete on orders
for each row 
 begin
insert into otherorder (order_num, prder, cust_id)
 values
( old.order_num,  old.order_date,  old.cust_id);
```



​    在任意订单被删除前将执行此触发器。它使用一条 INSERT 语句将 OLD中的值（要被删除的订单）保存到一个名为 otherorder的存档表中（为实际使用这个例子，你需要用与 orders 相同的列创建一个名为 otherorder的表）。

​    使用 BEFORE DELETE 触发器的优点（相对于 AFTER DELETE触发器来说）为，如果由于某种原因，订单不能存档， DELETE 本身将被放弃。

​    正如所见，触发器 deleteorder 使用BEGIN 和END 语句标记触发器体。这在此例子中并不是必需的，不过也没有害处。使用 BEGIN END 块的好处是触发器能容纳多条 SQL语句（在 BEGIN END 块中一条挨着一条）。

 

**UPDATE触发器**

​    UPDATE 触发器在UPDATE 语句执行之前或之后执行。需要知道以下几点：

​        1、在 UPDATE触发器代码中，你可以引用一个名为 OLD 的虚拟表访问以前（ UPDATE 语句前）的值，引用一个名为 NEW 的虚拟表访问新更新的值；

​        2、在 BEFORE UPDATE触发器中， NEW 中的值可能也被更新（允许更改将要用于 UPDATE 语句中的值）；

​        3、OLD 中的值全都是只读的，不能更新。

​    下面的例子保证州名缩写总是大写（不管 UPDATE 语句中给出的是大写还是小写）：

```
mysql> create trigger upvendor before update on vendors
    -> for each row set new.vend_state = upper(new.vend_state);
Query OK, 0 rows affected (0.21 sec)
```

​    显然任何数据净化都需要在update语句之前进行。就像这个例子中的一样。每次在更新一行时， NEW.vend_state中的值（将用来更新表行的值）都用 Upper(NEW.vend_state) 替换。

 

**关于触发器的进一步介绍**

​    1、创建触发器可能需要特殊的安全访问权限，但是，触发器的执行是自动的。如果 INSERT 、UPDATE 或 DELETE语句能够执行，则相关的触发器也能执行。

​    2、应该用触发器来保证数据的一致性（大小写、格式等）。在触发器中执行这种类型的处理的优点是它总是进行这种处理，而且是透明地进行，与客户机应用无关。

​    3、触发器的一种非常有意义的使用是创建审计跟踪。使用触发器，把更改（如果需要，甚至还有之前和之后的状态）记录到另一个表非常容易。

​    4、遗憾的是， MySQL 触发器中不支持 CALL语句。这表示不能从触发器内调用存储过程。所需的存储过程代码需要复制到触发器内。

 

​    关于什么时候使用new，old这两个关键字就好像字面意思新旧一样：

​         INSERT 只有NEW
         UPDATE既有NEW又和OLD
         DELETE只有OLD 

​    所以对于INSERT语句,只有NEW是合法的；对于DELETE语句，只有OLD才合法；而UPDATE语句可以在和NEW以及 OLD同时使用。下面是一个UPDATE中同时使用NEW和OLD的例子。

 



```
CREATE TRIGGER tr1  
BEFORE UPDATE ON liwei   
FOR EACH ROW   
BEGIN   
SET @old = OLD.s1;   
SET @new = NEW.s1;   
END; 
```



​    现在如果liwei表中的s1列的值是55，也就是@new的值就是55，那么执行了"UPDATE liwei SET s1 = s1 + 1"之后@old的值会变成55，

 

​    另外按照我在使用trigger和function的时候在mysql的trigger和function中不能出现select * from table形式的查询，因为其会返回一个结果集；而这在mysql的trigger和function中是不可接受的，但是在存储过程中可以。在 trigger和function中可以使用select ... into ...形式的查询。比如在使用trigger的时候没有into 的时候会报这样一种错误：

```
not allowed to return a result set from a trigger
```
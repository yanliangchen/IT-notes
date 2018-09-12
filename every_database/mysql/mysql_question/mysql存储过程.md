# mysql之存储过程		 

**一、存储过程**

​    迄今为止，使用的大多数 SQL语句都是针对一个或多个表的单条语句。并非所有操作都这么简单，经常会有一个完整的操作需要多条语句才能完成。例如，考虑以下的情形。

​        1、 为了处理订单，需要核对以保证库存中有相应的物品。

​        2、 如果库存有物品，这些物品需要预定以便不将它们再卖给别的人，并且要减少可用的物品数量以反映正确的库存量。

​        3、库存中没有的物品需要订购，这需要与供应商进行某种交互。

​        4、 关于哪些物品入库（并且可以立即发货）和哪些物品退订，需要通知相应的客户。

​     这显然不是一个完整的例子，它甚至超出了本书中所用样例表的范围，但足以帮助表达我们的意思了。执行这个处理需要针对许多表的多条MySQL语句。此外，需要执行的具体语句及其次序也不是固定的，它们可能会（和将）根据哪些物品在库存中哪些不在而变化。

​     那么，怎样编写此代码？一种是我们可以单独编写每条语句，并根据结果有条件地执行另外的语句。在每次需要这个处理时（以及每个需要它的应用中）都必须做这些工作。而另一种可以创建存储过程。

​     其实简单来说：存储过程，就是为以后的使用而保存的一条或多条 MySQL语句的集合。可将其视为批文件，虽然它们的作用不仅限于批处理。

 

**二、为什么要使用存储过程**

​       既然我们知道了什么是存储过程，那么为什么要使用它们呢？有许多理由，下面列出一些主要的理由。

​        1、通过把处理封装在容易使用的单元中，简化复杂的操作（正如前面例子所述）。

​        2、 由于不要求反复建立一系列处理步骤，这保证了数据的完整性。如果所有开发人员和应用程序都使用同一（试验和测试）存储过程，则所使用的代码都是相同的。这一点的延伸就是防止错误。需要执行的步骤越多，出错的可能性就越大。防止错误保证了数据的一致性。

​        3、简化对变动的管理。如果表名、列名或业务逻辑（或别的内容）有变化，只需要更改存储过程的代码。使用它的人员甚至不需要知道这些变化。这一点的延伸就是安全性。通过存储过程限制对基础数据的访问减少了数据讹误（无意识的或别的原因所导致的数据讹误）的机会。

​        4、提高性能。因为使用存储过程比使用单独的 SQL语句要快。

​        5、存在一些只能用在单个请求中的 MySQL元素和特性，存储过程可以使用它们来编写功能更强更灵活的代码（在下一章的例子中可以看到。）

​    换句话说，使用存储过程有 3个主要的好处，即简单、安全、高性能。显然，它们都很重要。不过，在将 SQL代码转换为存储过程前，也必须知道它的一些缺陷。

​        1、一般来说，存储过程的编写比基本 SQL语句复杂，编写存储过程需要更高的技能，更丰富的经验。

​        2、你可能没有创建存储过程的安全访问权限。许多数据库管理员限制存储过程的创建权限，允许用户使用存储过程，但不允许他们创建存储过程。

​    尽管有这些缺陷，存储过程还是非常有用的，并且应该尽可能地使用。

 

​    不能编写存储过程？你依然可以使用：MySQL将编写存储过程的安全和访问与执行存储过程的安全和访问区分开来。这是好事情。即使你不能（或不想）编写自己的存储过程，也

仍然可以在适当的时候执行别的存储过程。

 

**三、使用存储过程**

​    使用存储过程需要知道如何执行（运行）它们。存储过程的执行远比其定义更经常遇到，因此，我们将从执行存储过程开始介绍。然后再介绍创建和使用存储过程。

 

​    执行存储过程

​    MySQL称存储过程的执行为调用，因此 MySQL执行存储过程的语句为CALL。 CALL接受存储过程的名字以及需要传递给它的任意参数。请看以下例子：

```
call productpricing ( @ pricelow,
                             @ pricehigh,
                             @ priceaverage
                           );
```

​    其中执行productpricing 的存储过程，他计算并返回产品的最低价格，最高价格，均价。存储过程可以显示结果，也可以不显示结果，接下来会提到。

 

**创建存储过程**

​    正如所述，编写存储过程并不是微不足道的事情。为让你了解这个过程，请看一个例子——一个返回产品平均价格的存储过程。以下是其代码：

```
CREATE PROCEDURE productpricing()
BEGIN
   SELECT AVG(prod_price) AS priceaverage
   FROM products;
END;
```

​    我们稍后介绍第一条和最后一条语句。此存储过程名为productpricing，用CREATE PROCEDURE productpricing() 语句定义。如果存储过程接受参数，它们将在 ()中列举出来。此存储过程没有参数，但后跟的 ()仍然需要。BEGIN和 END语句用来限定存储过程体，过程体本身仅是一个简单的 SELECT语句（使用第12章介绍的 Avg()函数）。

​    在MySQL处理这段代码时，它创建一个新的存储过程 productpricing。没有返回数据，因为这段代码并未调用存储过程，这里只是为以后使用而创建它。

​    这里有一个需要注意的就是：mysql命令行客户机的分隔符

​    如果你使用的是 mysql命令行实用程序，应该仔细阅读此说明。

​    默认的 MySQL语句分隔符为;（正如你已经在迄今为止所使用的MySQL语句中所看到的那样）。 mysql命令行实用程序也使用;作为语句分隔符。如果命令行实用程序要解释存储过程自身内的 ;字符，则它们最终不会成为存储过程的成分，这会使存储过程中的 SQL出现句法错误。解决办法是临时更改命令行实用程序的语句分隔符，如下所示：



```
DELIMITER //
CREATE PROCEDURE productpricing()
BEGIN
   SELECT AVG(prod_price) AS priceaverage
   FROM products;
END //
DELIMITER ;
```



​    其中， DELIMITER //告诉命令行实用程序使用 //作为新的语句结束分隔符，可以看到标志存储过程结束的 END定义为END//而不是END; 。这样，存储过程体内的 ;仍然保持不动，并且正确地传递给数据库引擎。最后，为恢复为原来的语句分隔符，可使用 DELIMITER ;。除\符号外，任何字符都可以用作语句分隔符。如果你使用的是 mysql命令行实用程序，在阅读本章时请记住这里的内容。

 

​    那么，如何使用这个存储过程？如下所示：

```
CALL productpricing();
```

​    结果是：

```
+--------------+
| priceaverage |
+--------------+
|    16.133571 |
+--------------+
```

​    CALL productpricing();执行刚创建的存储过程并显示返回的结果。因为存储过程实际上是一种函数，所以存储过程名后需要有()符号（即使不传递参数也需要）。

 

**删除存储过程**

​    存储过程在创建之后，被保存在服务器上以供使用，直至被删除。删除命令（类似于第 21章所介绍的语句）从服务器中删除存储过程。为删除刚创建的存储过程，可使用以下语句：

```
DROP PROCEDURE productpricing;
```

​    这条语句删除刚创建的存储过程。请注意没有使用后面的 ()，只给出存储过程名。

​    仅当存在时删除 :如果指定的过程不存在，则 DROP PROCEDURE将产生一个错误。当过程存在想删除它时（如果过程不存在也不产生错误）可使用 DROP PROCEDURE IF EXISTS。

 

**使用参数**

​    productpricing只是一个简单的存储过程，它简单地显示 SELECT语句的结果。一般，存储过程并不显示结果，而是把结果返回给你指定的变量。这里所说的变量（ variable）内存中一个特定的位置，用来临时存储数据。

以下是 productpricing的修改版本（如果不先删除此存储过程，则不能再次创建它）：



```
DELIMITER //
CREATE PROCEDURE pricing(
   OUT pl DECIMAL(8, 2),
   OUT ph DECIMAL (8, 2),
   OUT pa DECIMAL (8, 2),
)
BEGIN

   SELECT MIN (prod_price)
   INTO pl
   FROM productes;
   SELECT MAX (prod_price)
   INTO ph
   FROM productes;
   SELECT AVG (prod_price)
   INTO pa
   FROM productes;
  
END //

DELIMITER ;
```



​    此存储过程接受 3个参数：pl 存储产品最低价格， ph存储产品最高价格， pa存储产品平均价格。每个参数必须具有指定的类型，这里使用十进制值。关键字 OUT指出相应的参数用来从存储过程传出一个值（返回给调用者）。 MySQL支持IN （传递给存储过程）、 OUT（从存储过程传出，如这里所用）和 INOUT（对存储过程传入和传出）类型的参数。存储过程的代码位于 BEGIN和END 语句内，如前所见，它们是一系列SELECT语句，用来检索值，然后保存到相应的变量（通过指定 INTO关键字）。

​    注意参数的数据类型：存储过程的参数允许的数据类型与表中使用的数据类型相同。注意，记录集不是允许的类型，因此，不能通过一个参数返回多个行和列。这就是前面的例子为什么要使用 3个参数（和3条SELECT语句）的原因。

​    为调用此修改过的存储过程，必须指定 3个变量名，如下所示：

```
CALL pricing (@pricelow, @pricehigh, @pricevarage );
```

​    由于此存储过程要求 3个参数，因此必须正好传递 3个参数，不多也不少。所以，这条 CALL语句给出3 个参数。它们是存储过程将保存结果的 3个变量的名字。

​    变量名 所有MySQL变量都必须以 @开始。

​    在调用时，这条语句并不显示任何数据。它返回以后可以显示（或在其他处理中使用）的变量。

```
SELECT @pricevarage
```

​    输出：

```
+--------+
| @pricevarage|
+--------+
|  55.00 |
+--------+
```

​     为了获得 3个值，可使用以下语句：

```
SELECT @pricelow, @pricehigh, @pricevarage ;
```

​    你会看到一个输出结果。

​    下面是另外一个例子，这次使用 IN和OUT 参数。ordertotal接受订单号并返回该订单的合计：



```
create procedure ordertotal (
in onumber int,
out ototal decimal (8,2)
)
begin
select sum(item_price * quantity)
from orderitems
where order_num = onumber
into ototal;
end //
```



​    onumber定义为IN ，因为订单号被传入存储过程。 ototal定义为OUT，因为要从存储过程返回合计。 SELECT语句使用这两个参数，WHERE子句使用 onumber选择正确的行，INTO使用 ototal存储计算出来的合计。

​     为调用这个新存储过程，可使用以下语句：

```
call ordertotal(20005, @total);
```

​    必须给 ordertotal传递两个参数；第一个参数为订单号，第二个参数为包含计算出来的合计的变量名。

​    为了显示次合计，可以如下操作：

```
SELECT @total;
```

​    输出：

```
+--------+
| @total |
+--------+
|   192.37|
+--------+
```

​    @total已由ordertotal 的CALL语句填写， SELECT显示它包含的值。

​    为了得到另一个订单的合计显示，需要再次调用存储过程，然后重新显示变量：

```
call ordertotal(20009, @total);
SELECT @total;
```

​    输出：

```
+--------+
| @total |
+--------+
|  38.47 |
+--------+
```

​    以后我们每次要通过订单号，来获得商品的总价都可以使用这个方式。是不是很有用啊。。

**建立智能存储过程**

​        迄今为止使用的所有存储过程基本上都是封装 MySQL简单的SELECT语句。虽然它们全都是有效的存储过程例子，但它们所能完成的工作你直接用这些被封装的语句就能完成（如果说它们还能带来更多的东西。那就是使事情更复杂）。只有在存储过程内包含业务规则和智能处理时，它们的威力才真正显现出来。

​       考虑这个场景。你需要获得与以前一样的订单合计，但需要对合计增加营业税，不过只针对某些顾客（或许是你所在州中那些顾客）。那么，你需要做下面几件事情：

​       1、获得合计（和以前一样）

​       2、把营业税有条件的添加到合计

​       3、返回合计（带或不带税的）

我们输入如下代码：



```
-- Name: ordertotal        //   添加注释
-- Parameters: onumber = order number
--             taxable = 0 if not taxable, 1 if taxtable
--             ototal = order total variable

CREATE     PROCEDURE ordertotal (
IN onumber INT,
IN taxable BOOLEAN,
OUT ototal DECIMAL(8,2)
) COMMENT 'Obtain order total, optionally adding tax'
BEGIN
    --  Declare variable for total       
    DECLARE total DECIMAL(8.2);      //   声明变量     
    --  Declare tax percentage
    DECLARE taxrate INT DEFAULT 6;
   
    -- Get the order total
    SELECT SUM(item_price * quantity)
    FROM orderitems
    WHERE order_num = onumber
    INTO total
   
    -- Is this taxable?
    IF taxable THEN
        --  Yes, so add taxrate to the total
        SELECT total + (total / 100 * taxrate) INTO total;
    END IF;
        --  And finally, save to out variable
        SELECT total INTO ototal;
END; 
```



​    此存储过程有很大的变动。首先，增加了注释（前面放置 --）。在存储过程复杂性增加时，这样做特别重要。添加了另外一个参数 taxable，它是一个布尔值（如果要增加税则为真，否则为假）。在存储过程体中，用 DECLARE语句定义了两个局部变量。 DECLARE要求指定变量名和数据类型，它也支持可选的默认值（这个例子中的 taxrate的默认被设置为 6%）。SELECT 语句变，因此其结果存储到 total（局部变量）而不是 ototal。IF 语句检查taxable是否为真，如果为真，则用另一SELECT语句增加营业税到局部变量 total。最后，用另一SELECT语句将total（它增加或许不增加营业税）保存到 ototal。

​    注意：COMMENT关键字 ，本例子中的存储过程在 CREATE PROCEDURE语句中包含了一个 COMMENT值。它不是必需的，但如果给出，将在SHOW PROCEDURE STATUS的结果中显示。

​    这显然是一个更高级，功能更强的存储过程。为试验它，请用以下两条语句：

​    第一条：

```
call ordertotal(20009, 0，@total);
SELECT @total;
```

​    输出：

```
+--------+
| @total |
+--------+
|  38.47 |
+--------+
```

​    第二条：

```
call ordertotal(20009, 1，@total);
SELECT @total;
```

​    输出：

```
+--------+
| @total |
+--------+
|  36.21 |
+--------+
```

​    BOOLEAN值指定为1 表示真，指定为 0表示假（实际上，非零值都考虑为真，只有 0被视为假）。通过给中间的参数指定 0或1 ，可以有条件地将营业税加到订单合计上。

这个例子给出了 MySQL的IF 语句的基本用法。 IF语句还支持 ELSEIF和ELSE 子句（前者还使用 THEN子句，后者不使用）。在以后章节中我们将会看到 IF的其他用法（以及其他流控制语句）。

 

​    检查存储过程

​    为显示用来创建一个存储过程的 CREATE语句，使用SHOW CREATE PROCEDURE语句：

```
show create procedure ordertotal;
```

​    为了获得包括何时、由谁创建等详细信息的存储过程列表，使用 SHOW PROCEDURE STATUS。

​    注意：限制过程状态结果，SHOW PROCEDURE STATUS列出所有存储过程。为限制其输出，可使用 LIKE指定一个过滤模式，例如：

```
SHOW PROCEDURE STATUS like 'ordertotal';
```
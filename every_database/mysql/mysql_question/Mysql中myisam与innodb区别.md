### 1.MySQL中myisam与innodb的区别

（1）不同之处;

1>.InnoDB支持事物，而MyISAM不支持事物

 

2>.InnoDB支持行级锁，而MyISAM支持表级锁

 

3>.InnoDB支持MVCC, 而MyISAM不支持

 

4>.InnoDB支持外键，而MyISAM不支持

 

5>.InnoDB不支持全文索引，而MyISAM支持。

 

  (2)、innodb引擎的4大特性

 

插入缓冲(insert buffer),二次写(double write),自适应哈希索引(ahi),预读(read ahead)

 

(3)、2者selectcount(*)哪个更快，为什么

 

myisam更快，因为myisam内部维护了一个计数器，可以直接调取。
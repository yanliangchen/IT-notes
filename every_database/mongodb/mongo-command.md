

**显示现有的数据库。**

showdbs;



**显示当前使用的数据库**

db;



**切换当前使用的数据库**

use leyue;



**创建数据库**

//没有则创建

use dbtest;

db.集合名称.insert({"name":"wang wu"}) 创建数据库:MongoDB没有专门创建数据库的语句,可以使用“use” 来使用某个数据库,如果要使用 的数据库不存在,那么将会创建一个,会在真正向该库加入文档后,保存成为文件。 



**创建集合**

  创建集合:在MongoDB中不用创建集合,因为没有固定的结构,直接使用db.集合名称.命令 来操作就可 以了。如果非要显示创建集合的话,用:db.createCollecion(“集合名称”);



**显示集合**

show collections ；





**insert 可以插入一个用{} 多条数据用[]**

db.userdatas.insert([ {"name":'lisan',"age":23},{"name":"wang wu","age":33} ])



**删除文档 db.集合.remove()**

db.userdatas.remove({"name":"lisan"})



**查看数据库 文档状态 可以看到文档的个数大小 等等信息**

数据库： db.stats() 

文档：db.集合.stats



**查看集合所有的文档**

db.集合名称.find(); 

db.userdatas.find() 



**文档替换 db.集合名称.update(条件,新的文档);只会修改符合条件的第一个文档。**

​    

```
db.test.update({"age":12},{"address":"北京","name":"老王"})1
```

  

**$set :指定一个字段的值,如果字段不存在,会创建一个.**

  

```
db.test.update({"name":"u1"},{"$set":{"name":"u2"}},0,1)1
```

  

**$unset :删掉某个字段**

  

```
db.test.update({"name":"u1"},{"$unset":{"address":1}},0,1)1
```

​    

**$push:向已有数组的末尾加入一个元素,要是没有就新建一个数组。**

  

```
db.test.update({"name":"u1"},{"$push":{"score":2}},0,1)1
```

​    

**each:通过一次each:通过一次push来操作多个值**

​    

```
db.test.update({"name":"u1"},{"$push":{"score":{"$each":[4,5,6]}}})1
```

  

**save方法**

  

如果文档存在就更新,不存在就新建,主要根据”_id”来判断。

​    

```
    db.test.save({"name":"li si"})
```
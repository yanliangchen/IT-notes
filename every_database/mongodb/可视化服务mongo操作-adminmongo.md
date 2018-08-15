**Mongodb可视化服务mongo-admin**



github地址：<https://github.com/mrvautin/adminMongo>

 

安装方法：

 

1、把git仓库克隆到本地

 

```
git clone https://github.com/mrvautin/adminMongo
```

 

2、进入仓库

 

```
cd adminMongo
```

 

3、安装

 //下载npm

```
yum -y  install  npm
```



```
npm install
```

 

4、启动

 

```
npm start
```

 

//注意  这个服务默认是泡在0.0.0.0段上的，如果是公网，则需要访问公网地址

5、访问地址 http://127.0.0.1:1234



6、 之后就是连接 

 //Connectionname 随便起

//Connectionstring  mongodb://127.0.0.1:27017 连接

//之后可以建库 建集合(建表) 里面放入json格式的数据 ，之后做能往里面进行数据查询，集合形式查询文档，添加文档。

 

[![adminMongo connections screen](https://raw.githubusercontent.com/mrvautin/mrvautin.github.io/master/images/adminMongo/adminMongo_connections.png)](https://raw.githubusercontent.com/mrvautin/mrvautin.github.io/master/images/adminMongo/adminMongo_connections.png)
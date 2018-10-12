1、安装zip、unzip应用。

 

```
yum install zip unzip
```

 

![img](data:image/png;base64,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)

 

2、压缩和解压文件

　

```
　以下命令均在/home目录下操作

　　　　cd /home #进入/home目录

　　a、把/home目录下面的mydata目录压缩为mydata.zip

　　　　zip -r mydata.zip mydata #压缩mydata目录

　　b、把/home目录下面的mydata.zip解压到mydatabak目录里面

　　　　unzip mydata.zip -d mydatabak

　　c、把/home目录下面的abc文件夹和123.txt压缩成为abc123.zip

　　　　zip -r abc123.zip abc 123.txt

　　d、把/home目录下面的wwwroot.zip直接解压到/home目录里面

　　　　unzip wwwroot.zip

　　e、把/home目录下面的abc12.zip、abc23.zip、abc34.zip同时解压到/home目录里面

　　　　unzip abc*.zip

　　f、查看把/home目录下面的wwwroot.zip里面的内容

　　　　unzip -v wwwroot.zip

　　g、验证/home目录下面的wwwroot.zip是否完整

　　　　unzip -t wwwroot.zip

　　h、把/home目录下面wwwroot.zip里面的所有文件解压到第一级目录

　　　　unzip -j wwwroot.zip

```


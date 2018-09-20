# docker-compose搭建django+mysql开发环境

使用docker来搭建开发环境不仅能够跟我们主机的已有的各种软件配置隔离，而且也能够很方便地分发给别人，从而使团队能够在统一的开发环境下快速开始开发、测试和部署。本文采用Docker的docker-compose来搭建python2.7+django1.7.5+mysql的web开发环境。



摘自：https://blog.csdn.net/yhcvb/article/details/45696961 （并对中间的坑进行了完善）



## 0、安装docker 

​	

```
看https://github.com/yanliangchen/IT-notes/blob/master/docker/centos7安装docker(没问题%EF%BC%8C亲测).md
```



## 1、项目目录

  

创建工程目录mysite

​    

```
yhc@yhc-E540:~/workspaces/docker$ mkdir mysite && cd mysite
```

  

创建以下2个目录（这里为方便放置各个文件，可以根据需要自己组织，后面配置文件做相应修改即可）

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ mkdir db mysite
```

​    

## 2、配置文件

  

## （1）Dockerfile

  

Dockerfile包含创建镜像所需要的全部指令。在项目根目录下创建`Dockerfile`文件，其内容如下：

​    

```
FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
ADD ./mysite/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```

  

第1行的`FROM`指令表示新的镜像将基于python:2.7的镜像来构建 
 第2行的`ENV`为环境变量（PYTHONUNBUFFERED见[这里](https://docs.python.org/2/using/cmdline.html)） 
 第3行的`RUN`指令表示在镜像内新建/code目录 
 第4行指定指定RUN、CMD与ENTRYPOINT命令的工作目录 
 第5行是将`./mysite/requirements.txt`文件添加到刚才新建的code目录中 
 第6行运行`pip`安装所需的软件





## （2）docker-compose.yml

  

之前的Dockerfile定义了一个应用，而使用compose，可以在一个文件里，定义多容器的应用。该YAML配置语言，用于描述和组装多容器的分布式应用。在项目根目录创建`docker-compose.yml`文件，其内容如下：

​    

```
db:
  image: mysql
  expose:
    - "3306"
  volumes:
    - ./db:/var/lib/mysql
  environment:
    - MYSQL_DATABASE=mysitedb
    - MYSQL_ROOT_PASSWORD=11111111  

web:
  build: .
  command: python ./mysite/manage.py runserver 0.0.0.0:8000
  volumes:
    - .:/code
  ports:
    - "8000:8000"
  links:
    - db
```

  

db标签： 
     images表示使用mysql镜像 
     expose表示暴露端口3306，但不发布到宿主机上 
     volume表示挂载宿主机的路径作为卷，冒号左边为宿主机路径，右边为镜像内路径 
     environment为环境变量，每个容器都有自己定义的环境变量，具体查看[镜像手册](https://github.com/docker-library/docs)中的mysql

  

web标签： 
     build指定建立Dockerfile路径 
     command将覆盖默认的命令 
     ports指定主机开放的端口 
     links指向其他容器中的服务



##  （3）requirements.txt

  

在子目录mysite下`requirements.txt`文件，该文件内容如下:

​    

```
django==1.7.5
MySQL-python
```



## 3、构建镜像

  

在项目根目录执行以下命令

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose build
db uses an image, skipping
Building web...
Step 0 : FROM python:2.7
 ---> d833e0b23482
Step 1 : ENV PYTHONUNBUFFERED 1
 ---> Using cache
 ---> df633fc1ab0e
Step 2 : RUN mkdir /code
 ---> Using cache
 ---> 49bb20e37bfc
Step 3 : WORKDIR /code
 ---> Using cache
 ---> f84fca46a343
Step 4 : ADD ./mysite/requirements.txt /code/
 ---> e8f756bed13e
Removing intermediate container 91e677d50cd4
Step 5 : RUN pip install -r requirements.txt
 ---> Running in 7eb86e071025
Collecting django==1.7.5 (from -r requirements.txt (line 1))
  Downloading Django-1.7.5-py2.py3-none-any.whl (7.4MB)
Collecting MySQL-python (from -r requirements.txt (line 2))
  Downloading MySQL-python-1.2.5.zip (108kB)
Installing collected packages: django, MySQL-python
  Running setup.py install for MySQL-python
Successfully installed MySQL-python-1.2.5 django-1.7.5
 ---> 3e5c9b891397
Removing intermediate container 7eb86e071025
Step 6 : ADD . /code/
 ---> 251dea7e2af2
Removing intermediate container b4b0c2b08538
Successfully built 251dea7e2af2
```



如果提示-bash: docker-compose: command not found

```
#利用pip方式进行安装
$ yum -y install epel-release
$ yum -y install python-pip
$ pip install docker-compose

#重新执行docker-compose build 命令


#中间 还有报错 可能缺少像gcc的这种依赖
参考：https://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet
```



如果本地没有python和mysql镜像的话下载需要多等待一些时间。完成之后就构建好了python+django+mysql的镜像。





## 4、创建django工程

  

执行以下命令

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose run web django-admin.py startproject mysite ./mysite

Starting dockermysite_db_1...
```

  

完成之后就在子目录mysite下创建了一个新的django工程 
 因为在镜像内是以root权限创建的，所以宿主机中对工程文件无法进行更改，这里修改一下权限

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ sudo chmod -R 777 mysite/
```

  

修改`setttings.py`文件中数据库配置

​    

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysitedb',
        'USER': 'root',
        'PASSWORD': '11111111',
        'HOST': 'db',
        'PORT': 3306,
    }
}
```





## 5、运行

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose up
```

```
#如果这里出现 
```



## 6、打包镜像

  

（1）查看镜像

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
mysite_web          latest              251dea7e2af2        8 minutes ago       783 MB
python              2.7                 d833e0b23482        13 days ago         747.9 MB
postgres            latest              b733b00eb1ae        13 days ago         213.9 MB
mysql               latest              56f320bd6adc        3 weeks ago         282.9 MB123456
```

  

（2）打包

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker save -o docker-mysite-image.tar.gz mysite_web
yhc@yhc-E540:~/workspaces/docker/mysite$ ls
db  docker-compose.yml  Dockerfile  docker-mysite-image.tar.gz  mysite
```

  

最后目录如下所示

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ tree
.
├── db
│   ├── auto.cnf
│   ├── ibdata1
│   ├── ib_logfile0
│   ├── ib_logfile1
│   ├── mysitedb [error opening dir]
│   ├── mysql [error opening dir]
│   └── performance_schema [error opening dir]
├── docker-compose.yml
├── Dockerfile
├── docker-mysite-image.tar.gz
└── mysite
    ├── manage.py
    ├── mysite
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── settings.py
    │   ├── settings.pyc
    │   ├── urls.py
    │   ├── urls.pyc
    │   ├── wsgi.py
    │   └── wsgi.pyc
    └── requirements.txt

6 directories, 17 files
```





## 7、加载镜像

  

镜像打包好后就可以分发给别的其他的开发人员，只需要加载镜像即可。 
 这里在本机进行测试镜像的加载，首先将原来的镜像删除了

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker rmi -f mysite_web
Untagged: mysite_web:latest
Deleted: 251dea7e2af26522b9e74612163972cb0aca2ec071e7b1696d815097db105770
Deleted: 3e5c9b8913971f90b4c94e8b0e04ed4dc2a09da6261fe0a9b3dffa7b0392ce92
Deleted: e8f756bed13e2172a8f522b93728f6aca75795bec0bb032ba154003f4a15b44012345
```

  

运行看看

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose up
Recreating mysite_db_1...
Recreating mysite_web_1...
No such image: mysite_web:latest (tag: latest)1234
```

  

发现无法运行了 
 接下来加载镜像

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker load -i docker-mysite-image.tar.gz
```

  

再次运行

​    

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose up
```

  

```
#如果出现django连接不上mysql的可以先试试sqllite3 这个没问题 
#但是我搭建的过程中遇到一个mysql报错 ，
参考 : https://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet 

ps : 我没有找到容器拉的mysql服务的所在目录的执行文件，暂时没有解决这个问题
```



## 8、其他

  

还可以运行python shell，命令如下：

  

```
yhc@yhc-E540:~/workspaces/docker/mysite$ docker-compose run web mysite/manage.py shell
```
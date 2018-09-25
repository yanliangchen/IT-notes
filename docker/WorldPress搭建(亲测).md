### Docker-WorldPress-Nginx  

参考github:  https://github.com/eugeneware/docker-wordpress-nginx

我是拿docker跑的 ，因为是博客嘛 ，不要搞的那么麻烦 

1 . 前提条件:

​	环境  ：centos 7 

​	docker环境 : 我这里用的是	 Docker version 18.06.1-ce, build e68fc7

​	docker安装过程: 参见我自己的github 也是学习docker过程中记录下来的 （亲测,没问题）

​	参考github :https://github.com/yanliangchen/IT-notes/tree/master/docker

2 . 安装worldpress 

​	docker-wordpress-nginx  

 

A Dockerfile that installs the latest wordpress, nginx, php-apc and php-fpm.

 

NB: A big thanks to [jbfink](https://github.com/jbfink/docker-wordpress) who did most of the hard work on the wordpress parts!

 

You can check out his [Apache version here](https://github.com/jbfink/docker-wordpress).

 

### Installation

 

The easiest way to get this docker image installed is to pull the latest version from the Docker registry:

 

```
$ docker pull eugeneware/docker-wordpress-nginx
```

 

If you'd like to build the image yourself then:

 

```
$ git clone https://github.com/eugeneware/docker-wordpress-nginx.git
$ cd docker-wordpress-nginx
$ sudo docker build -t="eugeneware/docker-wordpress-nginx" .
```

 

### Usage

 

To spawn a new instance of wordpress on port 80.  The -p 80:80 maps the internal docker port 80 to the outside port 80 of the host machine.

 

//我这里用的是9000 因为没有开公网ip 没有备案  只需要把映射到后台worldpress 前面的这个80进行修改就好了  

```
$ sudo docker run -p 80:80 --name docker-wordpress-nginx -d eugeneware/docker-wordpress-nginx
```

 

Start your newly created docker.

 

```
$ sudo docker start docker-wordpress-nginx
```

 

After starting the docker-wordpress-nginx check to see if it started and the port mapping is correct.  This will also report the port mapping between the docker container and the host machine.

 

```
$ sudo docker ps

0.0.0.0:80 -> 80/tcp docker-wordpress-nginx
```

 

You can the visit the following URL in a browser on your host machine to get started:

 

//我访问的公网ip +9000  

```
http://127.0.0.1:80
```

​    



//到这就可以写文章啦 ~  后续 我会给大家一个域名 ，共同成长  ~~  hhh 


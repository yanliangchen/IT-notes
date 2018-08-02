### **1. 单台机器安装nginx**

​	//安装yum源 eple

​	$sudo yum install epel-release

​	//安装nginx

​	$sudo yum install  nginx 

​	 // 启动Nginx

​	$sudo systemctl start nginx

​	//需要先安装防火墙firewall库（路过知识点升华）

​	

```
# 安装firewalld
yum install firewalld firewall-config
systemctl start  firewalld # 启动
systemctl status firewalld # 或者 firewall-cmd --state 查看状态
systemctl disable firewalld # 停止
systemctl stop firewalld  # 禁用

# 关闭服务的方法
# 你也可以关闭目前还不熟悉的FirewallD防火墙，而使用iptables，命令如下：

systemctl stop firewalld
systemctl disable firewalld
yum install iptables-services
systemctl start iptables
systemctl enable iptables
```

​	//如果您正在运行防火墙，请运行以下命令可以允许HTTP和HTTPS通信//云主机自行开启http https端口(需要认证)

​	$sudo  firewall-cmd --permanent --zone=public --add-service=http 

​	$sudo  firewall-cmd --permanent --zone=public --add-service=https

​	$sudo firewall-cmd --reload 

​	//我这里的云主机是80端口没备案的，所以我要给nginx服务换一个端口

```
 vim   /etc/nginx/nginx.conf
 给里面默认的端口改成没有被用的端口

```

​	// 停掉服务（重启服务）

```
1. 可以使用
$netstat -lnpt //查看服务 
$ps -ef | grep nginx  //查看nginx服务
$kill -9  进程号//(因为nginx默认是帮你做好的一个nginx负载，有一台master主,4台worker从,所以你需要进行4次操作)
$ nginx -c  /etc/nginx/nginx.conf //之后进行重启操作命令 

2. 也可以进入到nginx的目录
$进入nginx可执行目录sbin下，输入命令
$cd /usr/local/nginx/sbin
$./nginx -s reload 

//查看重启并有是否成功效果加上-c参数
$ nginx -t -c  /etc/nginx/nginx.conf
```

​	





### 2. 反向代理，负载均衡（3台机器实现）

实现一台前端负载均衡服务器访问到后端其他的Web服务（）

**先决条件**



 1. **3台机器的服务都能正常访问** 

 2. **前端负载均衡配置文件 /etc/nginx/nginx.conf**

    ```
      //这里注意一下 
     events {
      // IO多路复用得模型 epoll是最高效的
    	
        use epoll;
        //worker_connections 每个worker进程最大的request数量      这个值可以加两个0  102400
    
        worker_connections  1024;
    }
    
    
    http {
        include       mime.types;
        default_type  application/octet-stream;
    
        #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
        #                  '$status $body_bytes_sent "$http_referer" '
        #                  '"$http_user_agent" "$http_x_forwarded_for"';
    
        #access_log  logs/access.log  main;
    
        sendfile        on;
        #tcp_nopush     on;
    
        #keepalive_timeout  0;
        keepalive_timeout  65;
    
        #gzip  on;
    
        upstream webapp {
        	
            keepalive 2;
            //后端的服务，这里最好是内网  暂时不太懂网络
            server 114.67.22.221:8000;
            server 114.67.22.213:8000;
        }
    
        server {
            listen       80;
            server_name  localhost;
    
            #charset koi8-r;
    
            #access_log  logs/host.access.log  main;
    
            location / {
                proxy_pass http://webapp;
                #root   html;
                #index  index.html index.htm;
            }
    
            #error_page  404              /404.html;
    
            # redirect server error pages to the static page /50x.html
            #
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
                                                      
    ```

//这是我加入进来的

```
http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    upstream webapp {
        //高可用 nginx
        keepalive 2;
        //后端服务器的ip和端口
        server 114.67.22.221:8000;
        server 114.67.22.213:8000;
    }
	//这个是提醒一下要修改的http包含这个 
    server {
        listen       80;
        server_name  localhost;



 server {
       //本地前端服务监听的80端口
        listen       80;
        //这个是本地的ip地址
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            proxy_pass http://webapp;
            #root   html;
            #index  index.html index.htm;
        }
```



### 
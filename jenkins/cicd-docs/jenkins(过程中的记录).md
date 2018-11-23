### 1. 搭建完 启动

1. vim /etc/sysconfig/jenkins

2. 改下JENKINS_LISTEN_ADDRESS="172.34.0.5"  （回环网卡eth0地址）

3. 关闭防火墙

  systemctl stop firewalld
  systemctl disbale firewalld 

### 2. 备份恢复更新sh脚本设置2点定时启动

```
# 每天两点进行备份
crontab -e   (0 2 * * * bash /opt/jenkins_backup/jenkins_toolbox.sh backup )  
```

### 3. jenkins基础之上配置nginx (yum安装)

```
 $ yum -y install epel-release 
 $ yum  -y  install  nginx 
 $ cd /etc/nginx/conf.d
 
 $ vim  jenkins.conf
 
 # 文件里就这些配置(这是http)
 upstream jenkins_server {
   # 内网地址   8080 jenkins服务
    server 172.34.0.5:8080 fail_timeout=0;
}

server {
    listen 80;
    server_name jenkins.example.com;
    #  这个日志目录必须要有 否则报错
    access_log      /var/log/nginx/jenkins/access.log;
    error_log       /var/log/nginx/jenkins/error.log;

    location / {
        proxy_set_header        Host $host:$server_port;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
        proxy_pass              http://jenkins_server;
    }
}




#https配置（有1个就行了  文件名随便起，不影响的）
upstream app_server {
    server 172.34.0.5:8080 fail_timeout=0;
}

server {
    listen 80;
    server_name jenkins.example.com;
    return 301 https://$host/$request_uri;
}

server {
    listen 443 ssl;
    server_name jenkins.example.com;

    access_log      /var/log/nginx/jenkins/access.log;
    error_log       /var/log/nginx/jenkins/error.log;

    location / {
        proxy_set_header        Host $host:$server_port;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
        proxy_redirect http:// https://;
        proxy_pass              http://app_server;
    }
}
 

```


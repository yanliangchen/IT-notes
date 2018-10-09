安装
+++++++

+------------------+----------------------------------------------+
|       组件       |                     作用                     |
+------------------+----------------------------------------------+
|      nginx       |               静态 Web 服务器                |
+------------------+----------------------------------------------+
|   gitlab-shell   | 用于处理 Git 命令和修改 authorized keys 列表 |
+------------------+----------------------------------------------+
| gitlab-workhorse |            轻量级的反向代理服务器            |
+------------------+----------------------------------------------+
|    logrotate     |               日志文件管理工具               |
+------------------+----------------------------------------------+
|    postgresql    |                    数据库                    |
+------------------+----------------------------------------------+
|      redis       |                  缓存数据库                  |
+------------------+----------------------------------------------+
|     sidekiq      |      用于在后台执行队列任务（异步执行）      |
+------------------+----------------------------------------------+
|     unicorn      |  Gitlab Rails 应用是托管在这个服务器上面的   |
+------------------+----------------------------------------------+

RHEL/CentOS
"""""""""""""""

1. 安装并配置必要的依赖项

    在 CentOS7/RHEL 系统中，下面的命令将会在系统防火墙中开放 HTTP/HTTPS 和 SSH 端口

    .. code-block:: bash

        sudo yum install -y curl policycoreutils-python openssh-server
        sudo systemctl enable sshd
        sudo systemctl start sshd
        sudo firewall-cmd --permanent --add-service=http
        sudo firewall-cmd --permanent --add-service=https
        sudo systemctl reload firewalld

    接下来，安装Postfix以发送通知电子邮件。如果要使用其他解决方案发送电子邮件，请跳过此步骤并在安装GitLab后配置外部SMTP服务器。

    .. code-block:: bash

        sudo yum install postfix
        sudo systemctl enable postfix
        sudo systemctl start postfix

2. 添加 GitLab 软件包存储库并安装软件包

    新建 ``/etc/yum.repos.d/gitlab-ce.repo`` , 内容为：

    .. code-block:: bash

        cat << "EOF" > /etc/yum.repos.d/gitlab-ce.repo 
        [gitlab-ce]
        name=Gitlab CE Repository
        baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
        gpgcheck=0
        enabled=1
        EOF

    .. code-block:: bash

        sudo yum makecache
        sudo yum install -y gitlab-ce

3. 浏览主机并登陆

    首次访问时，您将被重定向到密码重置屏幕。提供初始管理员帐户的密码，您将被重定向回登录屏幕。使用默认帐户的用户名 ``root`` 登录。

Ubuntu
"""""""""

1. 安装并配置必要的依赖项

    .. code-block:: bash

        sudo apt-get update
        sudo apt-get install -y curl openssh-server ca-certificates

    接下来，安装Postfix以发送通知电子邮件。如果要使用其他解决方案发送电子邮件，请跳过此步骤并在安装GitLab后配置外部SMTP服务器。

    .. code-block:: bash

        sudo apt-get install -y postfix

    在Postfix安装期间，可能会出现配置屏幕。选择 “Internet Site” 并按Enter键。使用服务器的外部DNS作为“邮件名称”，然后按Enter键。如果出现其他屏幕，请继续按Enter键接受默认值。

2. 添加GitLab软件包存储库并安装软件包

    首先信任 GitLab 的 GPG 公钥:

    .. code-block:: bash

        curl https://packages.gitlab.com/gpg.key 2> /dev/null | sudo apt-key add - &>/dev/null

    再选择你的 Debian/Ubuntu 版本，文本框中内容写进 ``/etc/apt/sources.list.d/gitlab-ce.list``

    .. code-block:: bash

        sudo cat << EOF > /etc/apt/sources.list.d/gitlab-ce.list
        deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu xenial main
        EOF

    安装 gitlab-ce ：

    .. code-block:: bash

        sudo apt-get update
        sudo apt-get install gitlab-ce

3. 浏览主机并登陆

    首次访问时，您将被重定向到密码重置屏幕。提供初始管理员帐户的密码，您将被重定向回登录屏幕。使用默认帐户的用户名 ``root`` 登录。


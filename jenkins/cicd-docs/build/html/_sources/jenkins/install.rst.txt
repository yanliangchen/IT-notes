安装
+++++++

Debian/Ubuntu
""""""""""""""""""

Jenkins 使用 java 开发，所以在部署 jenkins 之前，需要安装 jdk

.. code-block:: bash

    sudo apt-get install openjdk-8-jre

最新版本可在apt存储库中找到，较旧但稳定的LTS版本在此apt存储库中。

.. code-block:: bash

    wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins

CentOS/RHEL
"""""""""""""""""

Jenkins 使用 java 开发，所以在部署 jenkins 之前，需要安装 jdk

.. code-block:: bash

    su -c "yum install java-1.8.0-openjdk"

最新版本可以在 rpm 存储库中找到，较旧但稳定的 LTS 版本在此 RPM 存储库中。

.. code-block:: bash

    sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
    sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
    sudo yum install jenkins


启动
"""""""""""""""

当 Jenkins 安装完成之后，启动脚本路径为 ``/etc/init.d/jenkins``，示例如下：


* 启动

    .. code-block:: none

        $ sudo /etc/init.d/jenkins start

* 关闭

    .. code-block:: none

        $ sudo /etc/init.d/jenkins stop

* 重启

    .. code-block:: none

        $ sudo /etc/init.d/jenkins restart

* 查看帮助

    .. code-block:: none

        $ sudo /etc/init.d/jenkins help


如果你的系统已经支持 systemd，使用 systemctl 命令管理 jenkins 更佳。

* 启动

    .. code-block:: none

        $ sudo systemctl start jenkins

* 关闭

    .. code-block:: none

        $ sudo systemctl stop jenkins

* 重启

    .. code-block:: none

        $ sudo systemctl restart jenkins

* 开机启动

    .. code-block:: none

        $ sudo syetemctl enable jenkins
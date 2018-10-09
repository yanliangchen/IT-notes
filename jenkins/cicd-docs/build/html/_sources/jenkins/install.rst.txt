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


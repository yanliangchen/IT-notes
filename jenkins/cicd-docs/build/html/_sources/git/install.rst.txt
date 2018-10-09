环境安装
+++++++++++++++

源码包安装
""""""""""""""

RHEL/CentOS
''''''''''''''''''

类 RHEL 系统默认安装的版本是较旧的 1.8 版本，推荐使用 2.7 版本。

1. 安装依赖

    .. code-block:: bash

        yum upgrade -y
        yum install libcurl-devel \
        expat-devel \
        gettext-devel \
        openssl-devel \
        zlib-devel \
        gcc \
        perl-ExtUtils-MakeMaker \
        bash-completion \
        unzip

2. 获取源码包

    注意不要使用 git 1.8 版本，推荐使用 2.7 版本

    .. code-block:: bash

        wget https://github.com/git/git/archive/v2.7.4.zip
        unzip v2.7.4.zip
        cd git-2.7.4

3. 编译

    .. code-block:: bash

        make prefix=/usr/local/git all
        make prefix=/usr/local/git install
        rm -rf /usr/bin/git
        ln -s /usr/local/git/bin/git /usr/bin/git

4. 检查

    .. code-block:: bash

        git --version


Debian/Ubuntu
'''''''''''''''''''
Ubuntu 发行版 apt repo 中 git 二进制安装包版本就是 2.7 

1. 安装依赖

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade -y
        sudo apt -y install \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        gettext \
        libz-dev \
        libssl-dev \
        unzip \
        make \
        gcc \
        perl

2. 获取源码包

    注意不要使用 git 1.8 版本，推荐使用 2.7 版本

    .. code-block:: bash

        wget https://github.com/git/git/archive/v2.7.4.zip
        unzip v2.7.4.zip
        cd git-2.7.4

3. 编译

    .. code-block:: bash

        sudo make prefix=/usr/local/git all
        sudo make prefix=/usr/local/git install
        sudo rm -rf /usr/bin/git
        sudo ln -s /usr/local/git/bin/git /usr/bin/git

4. 检查

    .. code-block:: bash

        git --version


二进制包安装
"""""""""""""""

RHEL/CentOS
''''''''''''''''

添加额外的 git repo，安装指定版本的 git

1. 添加 repo 源

    .. code-block:: bash

        cat > /etc/yum.repos.d/WANdisco-git.repo << EOF
        [WANdisco-git]
        name=WANdisco Replicated Git
        baseurl=http://opensource.wandisco.com/replication/rhel/\$releasever/git/\$basearch
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-WANdisco
        EOF
        curl -s http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco > RPM-GPG-KEY-WANdisco
        rpm --import RPM-GPG-KEY-WANdisco
        rm -f RPM-GPG-KEY-WANdisco

2. 安装 git

    .. code-block:: bash

        yum install git-<version>



Debian/Ubuntu
''''''''''''''''''

使用 apt 包管理器直接安装

1. 添加 PPA 源

.. code-block:: bash

    sudo add-apt-repository ppa:git-core/ppa
    sudo apt-get update

2. 安装 git

.. code-block:: bash

    sudo apt -y install git
    git --versio
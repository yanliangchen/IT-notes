备份管理
++++++++++

对 gitlab 进行备份将会创建一个包含所有库和附件的文档文件。对备份的恢复只能恢复到与备份时的 gitlab 相同的版本。将 gitlab 迁移到另一台服务器上的最佳方法就是通过备份和还原。

gitlab 提供了一个简单的命令来备份整个 gitlab，并且能灵活的满足需求。

配置文件
""""""""""""

.. code-block:: ruby

    ### Backup Settings
    ###! Docs: https://docs.gitlab.com/omnibus/settings/backups.html

    # gitlab_rails['manage_backup_path'] = true
    # gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"

    ###! Docs: https://docs.gitlab.com/ce/raketasks/backup_restore.html#backup-archive-permissions
    # gitlab_rails['backup_archive_permissions'] = 0644

    # gitlab_rails['backup_pg_schema'] = 'public'

    ###! The duration in seconds to keep backups before they are allowed to be deleted
    # gitlab_rails['backup_keep_time'] = 604800

    # gitlab_rails['backup_upload_connection'] = {
    #   'provider' => 'AWS',
    #   'region' => 'eu-west-1',
    #   'aws_access_key_id' => 'AKIAKIAKI',
    #   'aws_secret_access_key' => 'secret123'
    # }
    # gitlab_rails['backup_upload_remote_directory'] = 'my.s3.bucket'
    # gitlab_rails['backup_multipart_chunk_size'] = 104857600

    ###! **Turns on AWS Server-Side Encryption with Amazon S3-Managed Keys for
    ###!   backups**
    # gitlab_rails['backup_encryption'] = 'AES256'

    ###! **Specifies Amazon S3 storage class to use for backups. Valid values
    ###!   include 'STANDARD', 'STANDARD_IA', and 'REDUCED_REDUNDANCY'**
    # gitlab_rails['backup_storage_class'] = 'STANDARD'

+------------------------------------------------+----------------------------------+
|                     关键字                     |               含义               |
+------------------------------------------------+----------------------------------+
|     ``gitlab_rails['manage_backup_path']``     |         管理备份文件路径         |
+------------------------------------------------+----------------------------------+
|        ``gitlab_rails['backup_path']``         |         定义备份文件路径         |
+------------------------------------------------+----------------------------------+
| ``gitlab_rails['backup_archive_permissions']`` |         指定备份文件权限         |
+------------------------------------------------+----------------------------------+
|      ``gitlab_rails['backup_pg_schema']``      | 指定备份 postgresql 数据库表名称 |
+------------------------------------------------+----------------------------------+
|      ``gitlab_rails['backup_keep_time']``      |         备份文件保存时间         |
+------------------------------------------------+----------------------------------+

备份文件还支持上传到云端，支持 AWS、google、openstack swift 和 rackspace。

配置文件修改完成之后，请重新执行下面的命令使配置文件生效。

.. code-block:: bash

    sudo gitlab-ctl reconfigure

备份时间戳
"""""""""""""""

从 gitlab 9.2 版本开始，时间戳格式由 ``EPOCH_YYYY_MM_DD`` 更改为 ``EPOCH_YYYY_MM_DD_Gitlab-version``。

备份文件将保存在 gitlab.yml 文件中定义的 backup_path 中，文件名为 ``TIMESTAMP_gitlab_backup.tar`` ，TIMESTAMP 为备份时的时间戳。

1. 使用二进制软件包安装

    .. code-block:: bash

        sudo gitlab-rake gitlab:backup:create

2. 在 docker 中运行的 gitlab 

    .. code-block:: bash

        docker exec -c <container name> gitlab-rake gitlab:backup:create

备份策略选项
""""""""""""""

该选项对 gitlab 8.17 及以上版本有效。

默认的备份策略是使用 linux 的 tar/gzip 命令。这在大多数情况下是没有问题的，但是当数据在打包过程中发生变化时，将会有错误抛出 ``file changed as we read it`` ，这会导致备份进程失败。

为了解决这个问题，8.17 引入了一个名为 copy 的备份策略，就是在调用 tar、gzip 时将数据拷贝到一个临时位置。不过也引入了另外一个问题，将额外占用一倍的磁盘空间。

要使用复制策略而不是默认流策略，可以指定：

.. code-block:: bash

    sudo gitlab-rake gitlab:backup:create STRATEGY=copy

排除特定目录
"""""""""""""

通过加环境变量选择跳过要备份的内容。可用的选项有：

+--------------+---------------------------+
|     选项     |            内容           |
+--------------+---------------------------+
|      db      |           数据库          |
+--------------+---------------------------+
|   uploads    |            附件           |
+--------------+---------------------------+
| repositories |   Git repositories 数据   |
+--------------+---------------------------+
|    builds    |     CI job output logs    |
+--------------+---------------------------+
|  artifacts   |      CI job artifacts     |
+--------------+---------------------------+
|     lfs      |        LFS objects        |
+--------------+---------------------------+
|   registry   | Container Registry images |
+--------------+---------------------------+
|    pages     |       Pages content       |
+--------------+---------------------------+

指定多个选项使用逗号分隔

.. code-block:: bash

    sudo gitlab-rake gitlab:backup:create SKIP=db,uploads

使用 crontab 定时备份
""""""""""""""""""""""""""

.. code-block:: bash

    0 2 * * * /opt/gitlab/bin/gitlab-rake gitlab:backup:create CRON=1

环境变量 ``CRON=1`` 的作用是如果没有任何错误发生时，避免备份脚本的所有进度输出。将以将 /etc/gitlab 备份到安全的地方。如果要还原 gitlab 应用程序，还需要还原 gitlab-secrets.json 。如果没有，那么使用双重身份验证的 Gitlab 用户将无法访问 Gitlab 服务器，而存储在 Gitlab 中的“安全变量”将被丢失。

所有配置都存储在 ``/etc/gitlab`` 中，只需要备份此目录

.. code-block:: bash

    sudo sh -c 'umask 0077; tar -cf $(date "+etc-gitlab-%s.tar")  /etc/gitlab'

使用 crontab 

.. code-block:: bash

    0 2 * * *  umask 0077; tar cfz /secret/gitlab/backups/$(date "+etc-gitlab-\%s.tgz")  /etc/gitlab

服务器的 SSH 主机密钥存储在 ``/etc/ssh/`` 目录中，如果必须执行完整的服务器还原，请确保备份和还原这些密钥，以避免中间人攻击的警告。

恢复备份
""""""""""""

只能还原到与备份文件相同的 gitlab 版本。

首先有安装与备份文件相同的 gitlab，执行 ``gitlab-ctl reconfigure``。如果 gitlab 没有运行，需要执行 ``gitlab-ctl start``。并确保备份文件位于 ``gitlab_rails['backup_path']``

.. code-block:: bash

    sudo gitlab-ctl stop unicorn
    sudo gitlab-ctl stop sidekiq
    sudo gitlab-ctl status
    sudo gitlab-rake gitlab:backup:restore BACKUP=1493107454_2017_04_25_9.1.0 
    sudo gitlab-ctl start 
    sudo gitlab-rake gitlab:check SANITIZE=true
邮件配置
+++++++++++

邮件是 Gitlab 不可或缺的一个部分，它提供了代码提交提醒，用户密码找回等功能。Gitlab 也提供了几种邮件配置方案，有 sendmail，postfix 和 smtp 。这里只介绍 smtp，其中 sendmail 太过于古老，现在几乎被 postfix 替代了，而 postfix 配置没有 smtp 方便。

修改配置文件
""""""""""""""

.. code-block:: ruby

    # gitlab_rails['time_zone'] = 'UTC'
    
    ### Email Settings
    # gitlab_rails['gitlab_email_enabled'] = true
    # gitlab_rails['gitlab_email_from'] = 'example@example.com'
    # gitlab_rails['gitlab_email_display_name'] = 'Example'
    # gitlab_rails['gitlab_email_reply_to'] = 'noreply@example.com'
    # gitlab_rails['gitlab_email_subject_suffix'] = ''

    ### GitLab email server settings
    ###! Docs: https://docs.gitlab.com/omnibus/settings/smtp.html
    ###! **Use smtp instead of sendmail/postfix.**

    # gitlab_rails['smtp_enable'] = true
    # gitlab_rails['smtp_address'] = "smtp.server"
    # gitlab_rails['smtp_port'] = 465
    # gitlab_rails['smtp_user_name'] = "smtp user"
    # gitlab_rails['smtp_password'] = "smtp password"
    # gitlab_rails['smtp_domain'] = "example.com"
    # gitlab_rails['smtp_authentication'] = "login"
    # gitlab_rails['smtp_enable_starttls_auto'] = true
    # gitlab_rails['smtp_tls'] = false

+-------------------------------------------------+-------------------+
|                      关键字                     |        含义       |
+-------------------------------------------------+-------------------+
|          ``gitlab_rails['time_zone']``          |      时区设置     |
+-------------------------------------------------+-------------------+
|     ``gitlab_rails['gitlab_email_enabled']``    |    开启邮件服务   |
+-------------------------------------------------+-------------------+
|      ``gitlab_rails['gitlab_email_from']``      |  发送邮件来源地址 |
+-------------------------------------------------+-------------------+
|  ``gitlab_rails['gitlab_email_display_name']``  |   邮件显示用户名  |
+-------------------------------------------------+-------------------+
|    ``gitlab_rails['gitlab_email_reply_to']``    |    邮件回复地址   |
+-------------------------------------------------+-------------------+
| ``gitlab_rails['gitlab_email_subject_suffix']`` |    邮件主体后缀   |
+-------------------------------------------------+-------------------+
|         ``gitlab_rails['smtp_enable']``         |   开启 smtp 服务  |
+-------------------------------------------------+-------------------+
|         ``gitlab_rails['smtp_address']``        |  smtp 服务器地址  |
+-------------------------------------------------+-------------------+
|          ``gitlab_rails['smtp_port']``          |   smtp 服务端口   |
+-------------------------------------------------+-------------------+
|        ``gitlab_rails['smtp_user_name']``       | smtp 账户用户名称 |
+-------------------------------------------------+-------------------+
|        ``gitlab_rails['smtp_password']``        |   smtp 账户密码   |
+-------------------------------------------------+-------------------+
|         ``gitlab_rails['smtp_domain']``         |    smtp 服务域    |
+-------------------------------------------------+-------------------+
|     ``gitlab_rails['smtp_authentication']``     |   smtp 认证方式   |
+-------------------------------------------------+-------------------+
|  ``gitlab_rails['smtp_enable_starttls_auto']``  |  开启自动tls认证  |
+-------------------------------------------------+-------------------+
|           ``gitlab_rails['smtp_tls']``          |      tls 认证     |
+-------------------------------------------------+-------------------+

修改完成后，重新加载配置文件并重启

.. code-block:: bash

    sudo gitlab-ctl reconfigure
    sudo gitlab-ctl restart

.. attention:: 

    126邮箱和163邮箱都没有TLS加密设置，所以默认只能使用 25 端口。
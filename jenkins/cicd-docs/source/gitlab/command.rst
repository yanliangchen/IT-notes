命令
+++++++++

状态查询
"""""""""""""""""

通过命令可以查看各服务组件的运行状态

.. code-block:: bash

    gitlab-ctl status
    run: alertmanager: (pid 12966) 4279s; run: log: (pid 12980) 4279s
    run: gitaly: (pid 12895) 4281s; run: log: (pid 12978) 4279s
    run: gitlab-monitor: (pid 12928) 4280s; run: log: (pid 12936) 4280s
    run: gitlab-workhorse: (pid 12877) 4281s; run: log: (pid 12950) 4280s
    run: logrotate: (pid 20523) 726s; run: log: (pid 12952) 4280s
    run: nginx: (pid 12398) 4332s; run: log: (pid 12951) 4280s
    run: node-exporter: (pid 12620) 4314s; run: log: (pid 12924) 4280s
    run: postgres-exporter: (pid 12987) 4279s; run: log: (pid 13069) 4278s
    run: postgresql: (pid 12125) 4372s; run: log: (pid 12864) 4281s
    run: prometheus: (pid 12943) 4280s; run: log: (pid 12961) 4279s
    run: redis: (pid 12050) 4378s; run: log: (pid 12863) 4281s
    run: redis-exporter: (pid 12705) 4302s; run: log: (pid 13068) 4279s
    run: sidekiq: (pid 12371) 4334s; run: log: (pid 12931) 4280s
    run: unicorn: (pid 12328) 4340s; run: log: (pid 12930) 4280s

也可以指定查看某个服务

.. code-block:: bash

    gitlab-ctl status nginx
    run: nginx: (pid 12398) 4463s; run: log: (pid 12951) 4411s

查看日志
""""""""""""""""""

如果想查看某个服务的日志，可以使用如下命令

.. code-block:: bash

    gitlab-ctl tail nginx
    ==> /var/log/gitlab/nginx/current <==

    ==> /var/log/gitlab/nginx/error.log <==

    ==> /var/log/gitlab/nginx/gitlab_access.log <==
    192.168.47.1 - - [27/Sep/2018:11:59:37 +0800] "POST /profile/preferences HTTP/1.1" 200 585 "http://192.168.47.132/profile/preferences" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:11:59:42 +0800] "POST /profile/preferences HTTP/1.1" 200 585 "http://192.168.47.132/profile/preferences" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:11:59:43 +0800] "GET /profile/keys HTTP/1.1" 200 7587 "http://192.168.47.132/profile/preferences" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:11:59:43 +0800] "GET /assets/webpack/pages.profiles.keys.963cb5f3.chunk.js HTTP/1.1" 200 803 "http://192.168.47.132/profile/keys" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:11:59:45 +0800] "GET /profile/chat_names HTTP/1.1" 200 6725 "http://192.168.47.132/profile/keys" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:11:59:47 +0800] "GET / HTTP/1.1" 200 7539 "http://192.168.47.132/profile/chat_names" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:12:01:58 +0800] "GET /projects/new HTTP/1.1" 200 13013 "http://192.168.47.132/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:12:01:58 +0800] "GET /assets/webpack/commons~pages.projects~pages.projects.activity~pages.projects.artifacts.browse~pages.projects.artifa~1485fd35.d346ca1a.chunk.js HTTP/1.1" 200 7340 "http://192.168.47.132/projects/new" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:12:01:58 +0800] "GET /assets/webpack/pages.projects.new.0fa98a30.chunk.js HTTP/1.1" 200 1667 "http://192.168.47.132/projects/new" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    192.168.47.1 - - [27/Sep/2018:12:02:11 +0800] "GET /import/github/new HTTP/1.1" 200 6206 "http://192.168.47.132/projects/new" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

    ==> /var/log/gitlab/nginx/gitlab_error.log <==

    ==> /var/log/gitlab/nginx/access.log <==

也可以前往服务组件的日志目录进行查看：

.. code-block:: bash

    ll /var/log/gitlab/
    total 0
    drwx------ 2 gitlab-prometheus root        82 Sep 27 11:01 alertmanager
    drwx------ 2 git               root        82 Sep 27 11:01 gitaly
    drwx------ 2 git               root        82 Sep 27 11:01 gitlab-monitor
    drwx------ 2 git               root       216 Sep 27 11:00 gitlab-rails
    drwx------ 2 git               root        30 Sep 27 10:59 gitlab-shell
    drwx------ 2 git               root        82 Sep 27 11:01 gitlab-workhorse
    drwx------ 2 root              root        47 Sep 27 11:00 logrotate
    drwxr-x--- 2 root              gitlab-www 131 Sep 27 11:00 nginx
    drwx------ 2 gitlab-prometheus root        82 Sep 27 11:01 node-exporter
    drwx------ 2 gitlab-psql       root        82 Sep 27 11:01 postgres-exporter
    drwx------ 2 gitlab-psql       root        82 Sep 27 11:01 postgresql
    drwx------ 2 gitlab-prometheus root        82 Sep 27 11:01 prometheus
    drwxr-xr-x 2 root              root        28 Sep 27 10:59 reconfigure
    drwx------ 2 gitlab-redis      root        82 Sep 27 11:01 redis
    drwx------ 2 gitlab-redis      root        82 Sep 27 11:01 redis-exporter
    drwx------ 2 git               root        82 Sep 27 11:01 sidekiq
    drwx------ 2 git               root       134 Sep 27 11:01 unicorn

启动服务
""""""""""""""

可以启动指定的服务，也可以启动全部服务

.. code-block:: bash

    gitlab-ctl start
    gitlab-ctl start nginx

关闭服务
""""""""""""""

可以关闭指定的服务，也可以关闭全部服务

.. code-block:: bash

    gitlab-ctl stop
    gitlab-ctl stop nginx

重启服务
""""""""""""""

可以重启指定的服务，也可以重启全部服务

.. code-block:: bash

    gitlab-ctl restart
    gitlab-ctl restart nginx

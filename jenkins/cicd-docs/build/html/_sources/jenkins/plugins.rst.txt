插件
+++++++++++

默认 plugins
""""""""""""""""

1. `Folders plugins <https://go.cloudbees.com/docs/cloudbees-documentation/cje-user-guide/index.html#folder>`_

    该插件允许用户创建“文件夹”来组织作业。用户可以定义自定义分类（例如，按项目类型，组织类型）。文件夹是可嵌套的，您可以在文件夹中定义视图。

2. `OWASP Markup Formatter plugin <https://wiki.jenkins.io/display/JENKINS/OWASP+Markup+Formatter+Plugin>`_

    使用策略定义在用户提交的文本中允许有限的HTML标记。
    
3. `build timeout plugin <https://wiki.jenkins.io/display/JENKINS/Build-timeout+Plugin>`_

    此插件允许您在构建时间过长时自动中止构建。一旦达到超时，Jenkins就像一只无形的手点击了“中止构建”按钮。

4. `Credentials Binding Plugin <https://wiki.jenkins.io/display/JENKINS/Credentials+Binding+Plugin>`_

    允许将凭据绑定到环境变量，以便从其他构建步骤中使用。

5. `Timestamper <https://wiki.jenkins.io/display/JENKINS/Timestamper>`_

    将时间戳添加到控制台输出

6. `Workspace Cleanup Plugin <https://wiki.jenkins.io/display/JENKINS/Workspace+Cleanup+Plugin>`_

    用于删除构建工作区的插件。

7. `Ant Plugin <https://wiki.jenkins.io/display/JENKINS/Ant+Plugin>`_

    这个插件为Jenkins添加了Apache Ant支持。这个功能曾经是核心的一部分，但是从Jenkins 1.431开始，它被分成了单独的插件。

8. `Gradle Plugin <https://wiki.jenkins.io/display/JENKINS/Gradle+Plugin>`_

    此插件可以调用Gradle构建脚本作为主构建步骤。

9. `Pipeline <https://wiki.jenkins.io/display/JENKINS/Pipeline+Plugin>`_

    一套插件，可让您协调自动化，简单或复杂。有关更多详细信息和文档，请参阅Jenkins网站。

10. `Github Organization Folder Plugin <https://wiki.jenkins.io/display/JENKINS/GitHub+Organization+Folder+Plugin>`_

    过时的插件。升级到1.6后可能会被删除。

11. `Pipeline: Stage View Plugin <https://wiki.jenkins.io/display/JENKINS/Pipeline+Stage+View+Plugin>`_

    管道状态查看插件

12. `Git plugin <https://wiki.jenkins.io/display/JENKINS/Git+Plugin>`_

    这个插件允许使用Git作为构建SCM，包括几个提供者的存储库浏览器。需要最近的Git运行时（最低1.7.9，建议1.8.x）。与Git运行时的交互是通过使用Git Client插件来执行的，该插件仅在官方git客户端上进行测试。使用外来设施需要您自担风险。

13. `Subversion Plugin <https://wiki.jenkins.io/display/JENKINS/Subversion+Plugin>`_

    这个插件将Subversion支持（通过SVNKit）添加到Jenkins。这个插件捆绑在jenkins.war中。

14. `SSH Slaves plugin <https://wiki.jenkins.io/display/JENKINS/SSH+Slaves+plugin>`_

    此插件允许您通过SSH管理在 ``*nix`` 机器上运行的代理程序。

15. `Matrix Authorization Strategy Plugin <https://jenkins.io/doc/book/managing/security/#authorization>`_

    提供基于矩阵的安全授权策略（全局和每个项目）。

16. `PAM Authentication plugin <https://wiki.jenkins.io/display/JENKINS/PAM+Authentication+Plugin>`_

    为Jenkins添加Unix可插入身份验证模块（PAM）支持。

17. `LDAP Plugin <https://wiki.jenkins.io/display/JENKINS/LDAP+Plugin>`_

    这个插件是Jenkins核心的一部分，直到1.468。之后，它被拆分为可单独更新的插件。但是，出于向后兼容的目的，后续核心版本仍然捆绑它。如果你根本不使用这个插件，你可以简单地禁用它。

18. `Email Extension Plugin <https://wiki.jenkins.io/display/JENKINS/Email-ext+plugin>`_

    此插件允许您配置电子邮件通知的各个方面。您可以自定义何时发送电子邮件，谁应该接收电子邮件以及电子邮件所说的内容。

19. `Mailer Plugin <https://wiki.jenkins.io/display/JENKINS/Mailer>`_

    此插件允许您配置构建结果的电子邮件通知。这是原始核心电子邮件组件的突破。


常用 plugins
""""""""""""""""

1. `SSH plugin <https://wiki.jenkins.io/display/JENKINS/SSH+plugin>`_

    这个插件源自非常酷的SCP插件。您可以使用SSH插件通过ssh在远程计算机上运行shell命令。

2. `Gitlab Plugin <https://wiki.jenkins.io/display/JENKINS/GitLab+Plugin>`_

    这个插件是一个构建触发器，允许GitLab在推送代码或创建合并请求时触发Jenkins构建。基于每个作业完成配置。

3. `Pipeline <https://wiki.jenkins.io/display/JENKINS/Pipeline+Plugin>`_

    一套插件，可让您协调自动化，简单或复杂。有关更多详细信息和文档，请参阅Jenkins网站。

4. `Git plugin <https://wiki.jenkins.io/display/JENKINS/Git+Plugin>`_

    这个插件允许使用Git作为构建SCM，包括几个提供者的存储库浏览器。需要最近的Git运行时（最低1.7.9，建议1.8.x）。与Git运行时的交互是通过使用Git Client插件来执行的，该插件仅在官方git客户端上进行测试。使用外来设施需要您自担风险。

5. `Git Parameter Plugin <https://wiki.jenkins.io/display/JENKINS/Git+Parameter+Plugin>`_

    添加从项目中配置的git存储库中选择分支，标签或修订的功能。

6. `Deploy Plugin <https://wiki.jenkins.io/display/JENKINS/Deploy+Plugin>`_

    此插件接受war / ear文件，并在构建结束时将其部署到正在运行的远程应用程序服务器。实施基于Cargo。当前支持的容器列表包括：

        * Tomcat 4.x/5.x/6.x/7.x
        * JBoss 3.x/4.x
        * Glassfish 2.x/3.x

7. `Maven integration plugin <https://plugins.jenkins.io/maven-plugin>`_

    

8. `Role-based Authorization Strategy <https://wiki.jenkins.io/display/JENKINS/Role+Strategy+Plugin>`_

    添加新的基于角色的策略来管理用户的权限。

9. `Html reports <https://wiki.jenkins.io/display/JENKINS/HTML+Publisher+Plugin>`_

    这个插件发布 HTML 报告

10. `performance plugin <https://wiki.jenkins.io/display/JENKINS/Performance+Plugin>`_

    此插件允许您从流行的测试工具中捕获报告。 Jenkins将生成具有性能和稳健性趋势报告的图表。 它包括根据报告的错误百分比将最终构建状态设置为良好，不稳定或失败的功能。

11. `Cobertura <https://wiki.jenkins.io/display/JENKINS/Cobertura+Plugin>`_

    此插件允许您从Cobertura捕获代码覆盖率报告，Jenkins将生成覆盖率的趋势报告。

12. `SonarQube <https://wiki.jenkins.io/display/JENKINS/SonarQube+plugin>`_

    该插件可轻松集成SonarQube™，这是一种用于连续检查代码质量的开源平台。

13. `Blue Ocean <https://wiki.jenkins.io/display/JENKINS/Blue+Ocean+Plugin>`_

    Blue Ocean是一个重新思考Jenkins用户体验的新项目。 Blue Ocean专为Jenkins Pipeline设计并与Freestyle工作兼容，通过以下主要功能减少了团队中每个成员的混乱并提高了清晰度：

        * CD管道的复杂可视化，允许快速和直观地理解软件管道状态。
        * 管道编辑器，通过引导用户通过直观和可视的过程来创建管道，使自动化CD管道变得平易近人。
        * Jenkins UI的个性化，以满足DevOps团队每个成员的基于角色的需求。
        * 在需要干预和/或出现问题时精确定位。Blue Ocean UI 显示了需要注意的地方，便于异常处理和提高生产力。
        * 分支和拉取请求的本机集成可在与 GitHub 和 Bitbucket 中的其他代码协作代码时实现最大的开发人员生产力。

插件管理
""""""""""""""

Jenkins 通过大量插件提供附加功能，管理 Jenkins 插件主要是安装和配置。这里主要介绍 jenkins 插件的安装，具体配置需要参考具体 Jenkins 插件的说明。

Jenkins 提供了 Update Center，可以从 Update Center 在线下载安装 Jenkins 插件。

管理 Jenkins 插件的方法主要有两种。一种是通过 Jenkins 的 Web 界面，另一种是通过 Jenkins CLI。

通过 web 界面管理插件
'''''''''''''''''''''''''''''''

Jenkins 界面 --> System Manager --> Manager Plugins --> Available

.. image:: /images/jenkins/web插件管理页面.png

在 Jenkins 里面点击安装后，报了如下的错误：

.. image:: /images/jenkins/安装插件报错.png

错误的原因是国内的网络不能访问国外的网站，遇到这种情况我们就需要手动进行安装，具体的步骤如下：

1. 进入 `Jenkins Plugins <https://mirrors.tuna.tsinghua.edu.cn/jenkins/plugins/>`_ 搜索需要的插件，如下图所示：

    .. image:: /images/jenkins/清华大学jenkins插件.png

2. 找到需要下载的插件，进行下载

    .. image:: /images/jenkins/git_plugin.png

3. 选择你要下载的版本

    .. image:: /images/jenkins/git_plugin_version.png

4. 下载完成后，进入 jenkins 页面，点击 Systme Manager --> Manager Plugins --> Available

    .. image:: /images/jenkins/上传插件.png

5. 点击 update 按钮安装插件，之后会跳转页面

    .. image:: /images/jenkins/安装插件.png

通过 Jenkins CLI 的 install-plugin 命令管理插件
'''''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: bash

    java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin <SOURCE> ... [-deploy] [-name alias_name] [-restart]

参数说明

* SOURCE 是插件文件或插件的URL；
* -deploy 直接部署插件，无需推迟到 Jenkins 服务器重启的时候再部署插件
* -name 给插件命名别名
* -restart 安装插件后重启 jenkins 服务器

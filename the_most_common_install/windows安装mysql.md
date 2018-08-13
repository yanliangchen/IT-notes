**一、下载mysql（已成功）**  

参考： https://www.jb51.net/article/92158.htm  

ps :为了下次找起来不方便，特此记录。

 

\1. 在浏览器里打开mysql的官网http://www.mysql.com/

 

\2. 进入页面顶部的"Downloads"

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003287.png)](https://files.jb51.net/file_images/article/201609/2016090715003287.png)

 

\3. 打开页面底部的“Community(GPL) Downloads”

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003288.png)](https://files.jb51.net/file_images/article/201609/2016090715003288.png)

 

\4. 在页面中间的位置找到我们windows上要用的下载页面“MySQL on Windows(Installer & Tools)”

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003389.png)](https://files.jb51.net/file_images/article/201609/2016090715003389.png)

 

\5. 选择第一项"MySQL Installer”

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003390.png)](https://files.jb51.net/file_images/article/201609/2016090715003390.png)

 

\6. 页面底端找到下载入口“Windows (x86,
 32-bit), MSI Installer”，点击Download按钮开始下载，共381.4M

 

注意：MSI格式是指windows的安装程序，下载后直接双击就能进入安装向导的那种，区别于对文件进行解压的安装方式；

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003391.png)](https://files.jb51.net/file_images/article/201609/2016090715003391.png)

 

\7. 这个页面告诉询问你是否登录，告诉你登录之后有哪些好处，我们不登录，点击页面底部的“No thanks, just start my download.”按钮进入下载页面

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003392.png)](https://files.jb51.net/file_images/article/201609/2016090715003392.png)

 

\8. 开始下载，等待下载完成（由于直接下载速度太慢，之后我用迅雷下载完成的）

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003393.png)](https://files.jb51.net/file_images/article/201609/2016090715003393.png)

 

\9. 下载完成

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003394.png)](https://files.jb51.net/file_images/article/201609/2016090715003394.png)

 

**二、安装mysql**

 

**![img](https://files.jb51.net/file_images/article/201609/2016090715003395.png)**

 

\1. 双击下载好的mysql安装文件“mysql-installer-community-5.7.14.0.msi”打开安装程序，打开后需要稍等一下

 

![img](https://files.jb51.net/file_images/article/201609/2016090715003396.png)

 

\2. 选择安装类型（根据个人需要）

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003397.png)](https://files.jb51.net/file_images/article/201609/2016090715003397.png)

 

\3. 我只需要安装mysql server，所以选择最后一项“Custom”，选择Custom之后左边的安装流程和右边的描述文字会改变，然后点击"Next"按钮继续

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003398.png)](https://files.jb51.net/file_images/article/201609/2016090715003398.png)

 

\4. 在这里我们需要从安装程序提供的可安装的产品（Products）中选择我们需要的mysql server

 

[![img](https://files.jb51.net/file_images/article/201609/2016090715003399.png)](https://files.jb51.net/file_images/article/201609/2016090715003399.png)

 

我们展开Available Products里的第一项“MySQL Servers”，依次展开其子结点，直到其终端结点，我的操作是64位的，所以选中“MySQL Server 5.7.14 - X64”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150034100.png)](https://files.jb51.net/file_images/article/201609/20160907150034100.png)

 

然后点击绿色的向右箭头，将当前Product移动需要安装的列表，然后在右边展开“MySQL Server 5.7.14 - X64”项，取消“Development Components”的勾选（因为我们只需要安装mysql server），之后点击“Next”按钮进入下一步

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150034101.png)](https://files.jb51.net/file_images/article/201609/20160907150034101.png)

 

\5. 点击“Execute”（执行）开始安装，安装过程中会显示安装的Progress（进度），等待安装完成后Status会显示Complete，mysql图标前会出现一个绿色的勾，然后点击“Next”按钮进入产品配置界面

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150034102.png)](https://files.jb51.net/file_images/article/201609/20160907150034102.png)

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044103.png)](https://files.jb51.net/file_images/article/201609/20160907150044103.png)

 

\6. 点击“Next”按钮进入MySQL Server 的配置

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044104.png)](https://files.jb51.net/file_images/article/201609/20160907150044104.png)

 

Config Type选择“Development Machine”，选择此项将使用较小的内容来运行我们的mysql server，对应小型软件、学习是完全够用的。之后“Next”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044105.png)](https://files.jb51.net/file_images/article/201609/20160907150044105.png)

 

在Root Account Password设置数据库root账号的密码，我填的是123456所以程序提醒我密码强度为弱，我们需要牢记这个密码，然后点击“Next”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044106.png)](https://files.jb51.net/file_images/article/201609/20160907150044106.png)

 

这里可以设置mysql server的名称和是否开机启动，我把名称改为了“MySQLZzz1”，取消了开机启动，其它的没改，点击“Next”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044107.png)](https://files.jb51.net/file_images/article/201609/20160907150044107.png)

 

点击“Next”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044108.png)](https://files.jb51.net/file_images/article/201609/20160907150044108.png)

 

此界面将之前设置的配置内容应用到我们的mysql server，点击“Execute”，等待完成就可以了

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044109.png)](https://files.jb51.net/file_images/article/201609/20160907150044109.png)

 

配置完成，点击“Finish”完成配置环节

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150044110.png)](https://files.jb51.net/file_images/article/201609/20160907150044110.png)

 

\7. 配置完成后将回到安装程序，我们点击“Next”继续

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150045111.png)](https://files.jb51.net/file_images/article/201609/20160907150045111.png)

 

提示我们安装完成，点击“Finish”

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150045112.png)](https://files.jb51.net/file_images/article/201609/20160907150045112.png)

 

\8. 在上一步点击“Finish”之后电脑是如此的平静，让人不知道接下来干什么！按以往安装软件的经验这个时候电脑应该要自动启动刚刚安装好的软件的。所以我在进程里找了一下，确实没有发现类似mysql的进程，那么我们进入下一步。

 

**三、配置mysql环境变量（非必要）**

 

说明：给mysql配置环境变量后我们就可以在cmd里运行mysql（开启、停止等操作）

 

\1. 和其实环境变量的配置方法一样，我们打开环境变量配置窗口（组合键win+Pause -> 更改设置 -> 系统属性里选择“高级” -> 环境变量）

 

\2. 选中系统变量中的“path”，在path值开头处输入mysql安装目录下的bin文件夹所在路径：C:\Program Files\MySQL\MySQL Server 5.7\bin，保存退出

 

注意：mysql server安装的默认路径为：C:\Program Files\MySQL\MySQL Server 5.7

 

\3. 测试是否配置成功：打开cmd，输入“mysql -u root -p”回车，然后输入mysql安装时设置的root账号的密码（123456），若提示“Welcome to the MySQL monitor.”说明配置成功了。

 

**四、启动mysql**

 

是的，到现在我们还没有启动我们的mysql！那么要怎么启动呢？

 

（基于已配置环境变量的情况）

 

\1. 以管理员的身份运行cmd，输入“net start mysqlzzz1”（MySQLZzz1是配置mysql server时填写的服务器名称，cmd里不区分大小写也可以使用）

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150052113.png)](https://files.jb51.net/file_images/article/201609/20160907150052113.png)

 

\2. 提示启动成功后我们便可以在任务管理器的进程里看到“mysqld.exe”的进程了。

 

附：

 

若执行命令时提示：服务名无效。请键入 NET HELPMSG 2185 以获得更多的帮助。

 

**解决办法：** 在 mysql bin目录下 以管理员的权限 执行 mysqld -install命令

 

**附卸载mysql服务的方法。**

 

1、以管理员的权限 net stop mysql ，关闭mysql服务

 

2、以管理员的权限 mysqld -remove ，卸载mysql服务

 

**五、测试是否安装成功**

 

我们使用MySQL管理软件（Navicat for MySQL）进行连接测试，确保mysql已经可以使用：

 

\1. 打开Navicat for MySQL

 

![img](https://files.jb51.net/file_images/article/201609/20160907150052114.png)

 

\2. 新建一个连接，填写连接信息：

 

连接名称：用于区分不同的连接，自己命名即可

 

主机名：localhost

 

端口：3306

 

用户名：root

 

密码：123456（之前配置mysql的时候填写的密码）

 

![img](https://files.jb51.net/file_images/article/201609/20160907150052115.png)

 

\3. 点击“连接测试”按钮，弹出连接成功对话框即表示mysql server已开启

 

![img](https://files.jb51.net/file_images/article/201609/20160907150052116.png)

 

\4. 之后就是Navicat for MySQL软件的使用

 

[![img](https://files.jb51.net/file_images/article/201609/20160907150052117.png)](https://files.jb51.net/file_images/article/201609/20160907150052117.png)

 

另：

 

我们也可以在cmd里，再次输入“net start mysqlzzz1”，若提示“请求的服务已经启动。”表示mysql server已正常启动；

 

至此，mysql server在windows 10 64位上就安装完成了。
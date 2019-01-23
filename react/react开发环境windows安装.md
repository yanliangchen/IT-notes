最近在学习react相关的知识，刚刚起步，一路遇坑不断。自己做个笔记，方便日后总结，也供相同趣味的小伙伴一起交流探讨。

学习时主要参考官网的教程：<https://facebook.github.io/react/docs/hello-world.html>    和部分网上的博客。

### 1.安装node。

去官网（<https://nodejs.org/en/download/>）下载最新的稳定版本，我安装的版本是6.11.2。（ps：尽量下载稳定版的，因为我刚弄的时候下载的是最新的版本，然后又一次跑一个命令一直卡在那里不动，后来重新安装了以后才好）。下载安装完以后在cmd界面输入 node -v 可以直接查看版本。

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918134455290-1684596170.png)

安装node时会自带一个npm的包管理工具，我们可以在命令行通过 npm -v 查看：

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918134722321-1362891758.png)

国内使用npm很慢，我们可以使用淘宝的镜像来代替原有的，在命令行输入： npm config set registry https://registry.npm.taobao.org  即可设置。

当我们安装好node以后，会自动将node设置系统的环境变量，将npm设置为系统的用户变量，可以在系统环境变量中查看。

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918135957868-911856528.png)      ![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918140048790-1217617678.png)

我们通过npm install -g 安装的模块，都在用户变量（上左图）对应的路径中，比如这里示例下载一个 yarn 工具。

 ![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918140645103-758953285.png)

可以在日志信息中看到，刚刚安装的yarn在 {User}/AppData/Roaming/npm 文件夹中（ps：AppData是隐藏的文件夹）：

### 2.安装create-react-app

安装create-react-app有利于我们快速创建一个react应用，安装命令： npm install -g create-react-app 。安装过程可能会比较慢，因为要下载很多模块及相应的依赖，如果一直卡的话建议检查一下网络设置或者改成淘宝的镜像。

### 3.创建并运行项目

在cmd中切换至工作空间，输入 create-react-app demo01 创建一个react项目，创建过程比较慢，理由同上。

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918141833306-221171202.png)

这里是因为我上一步安装了yarn，所以成功的提示可能与你有所不同。这里我根据提示使用  yarn start 命令启动项目，没有安装yarn的可以输入  npm start

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918142251915-1128236439.png) or  ![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918142349634-746958986.png)

都可以看到成功的启动了项目：

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918142439446-2135356485.png)

下载我们根据页面的提示修改一下src/App.js里面的文件并保存，体验一把乐趣（虽然没什么乐趣）。修改的部分如下：

```
<p className="App-intro">
    开始React之坑的学习
</p>
```

保存后可以看到浏览器实时的改变了：

![img](https://images2017.cnblogs.com/blog/1242154/201709/1242154-20170918142834900-1477115155.png)

至此，一个朴素的react工程就创建成功了。



### 4.可以直接pycharm

前提摘要是要安装node
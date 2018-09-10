## sphinx+github+Read the Docs

**教你快速搭建一个博客，并通过多人协作提交github修改共同编写文档，之后通过Read the Docs 来帮你发布构建**

摘自：https://mp.weixin.qq.com/s/nmEEg1c2cXg0242KjkpsTw    

ps : 我这里用的是centos7，方便修改，我直接沾过来啦~

![img](https://mmbiz.qpic.cn/mmbiz_jpg/UFM3uMlAXxOf1busc8gJY8wnTpxEBTldWEPu0IlJtpCNBYByXSicEVPULZVogC9piaXXzjnVZlpEJkwDCA1JQz1A/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

本文来源：python编程时光，欢迎大家关注

10个优秀的程序员里，有9个人都有写博客的习惯。这是非常好的习惯，它使得知识得以提炼，转输出为输入，在提升自己的同时，还能利用互联网易传播的特性，将知识分享给每一个热爱学习的人。这是值得每个程序员，投入时间和精力去坚持做下去的事。

博客既然是自己的一个知识宝库，那么索引将变得极为重要。通过自己的探索，小明发现了一个能够很好地满足这个需求的 Python 框架 **Sphinx**。

实现的大体的思路如下：

- Markdown：书写文档
- Pandoc：格式转化
- Sphinx：生成网页
- GitHub：托管项目
- ReadtheDocs：发布网页

接下来，就来看看到底是如何实现的？

# 01 成品展示 

以我的博客(mings-blog.rtfd.io)为例，先给大家展示一下。

这是首页。显示了你所有的文章索引。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxMeDwdo76GxKPOwcl5iavS5spnRHM9N5RIpEibeiaKxltOJo2f4iaiatLMBsH7Xwduh0LI3n7DdiaG8BF8g/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这是我的导航栏。是不是结构很清晰，很方便索引。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxMeDwdo76GxKPOwcl5iavS5smOkeXicGZakVa8eibI3IiaqyTaRu39a3Ba6Ae2RAH4pdBWMFX9ib0TghpA/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

点击文章后，还可以很方便查看标题，跳转。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxMeDwdo76GxKPOwcl5iavS5sOuSIWricbDnkYhtcJiaOiazwcJVltSW4qYXGjZDwRa869VRhpicQuc1z6Q/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

体验下搜索功能，速度很快。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTH7xVR42AOV9UhmrXHCLAdPEDqVa7QsYGjpJ6bpvHlnBzUB737adI2DQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

看完这些你是不是也很想拥有这样一个博客呢？

只要你认真往下看，30分钟搭建这样一个博客不在话下。

# 02 安装Sphinx 

安装之前，请确认下Python版本。我这里使用的是Python 2.7.14，其他版本请自行尝试（Py3有点不一样，不想踩坑的，请跟我一样使用 Py2）。

安装Python工具包

```
1.安装依赖
sudo yum install openssl-devel -y 
sudo yum install zlib-devel -y
yum  -y  install  wget

2.安装setuptools

wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26 

tar -zxvf setuptools-19.6.tar.gz 
cd setuptools-19.6
sudo python setup.py build 
sudo python setup.py install

3.安装pip

wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb 

tar -zxvf pip-8.0.2.tar.gz 
cd pip-8.0.2 
python setup.py build 
sudo python setup.py install
```



```
# pip 更新
$ pip install  --upgrade  pip
$ pip install sphinx sphinx-autobuild sphinx_rtd_theme
```

初始化

```
# 先创建一个工程目录:
/opt/mkdocs
$sphinx-quickstart
```

执行这个命令`sphinx-quickstart`的时候，会让你输入配置。除了这几个个性化配置，其他的都可以按照默认的来。

```
> Project name: MING's BLOG>
> Author name(s): MING> 
> Project release []:
> 1.0> Project language [en]: zh_CN
```

完了后，就可以看见创建的工程文件。

```
F:\mkdocs
(mkdocs) λ ls -l
total 5
-rw-r--r-- 1 wangbm 1049089 610 Jun 23 16:57 Makefile
drwxr-xr-x 1 wangbm 1049089   0 Jun 23 16:57 build/
-rw-r--r-- 1 wangbm 1049089 817 Jun 23 16:57 make.bat
drwxr-xr-x 1 wangbm 1049089   0 Jun 23 16:57 source/

F:\mkdocs
(mkdocs) λ tree
卷 文档 的文件夹 PATH 列表
卷序列号为 0002-B4B9
F:.
├─build
└─source
    ├─_static
    └─_templates
```

解释下这些文件/夹：

- build：文件夹，当你执行make html的时候，生成的html静态文件都存放在这里。
- source：文件夹：你的文档源文件全部应全部放在source根目录下。
- Makefile：编译文件。完全不用管。
- make.bat：bat脚本。你也不用管。

# 03 配置及扩展 

Sphinx 的配置文件是 `source\conifg.py`

由于修改的内容比较多而杂，为了使这个搭建过程，更加顺畅。

小明已经给你精心准备了一份配置文件。你只要克隆下来就好了。

关于配置文件，我做了哪些事：

- 配置主题
- 支持LaTeX
- 支持中文检索

以上配置文件，所有的配置文件  都在这篇文档的当前目录下的压缩包，自行克隆

由于扩展模块会用到一些第三方依赖包，需要你去包装它。requirements.txt 同样我也给你准备好了，在压缩包里有。

你只要执行这个命令，即可安装。

```
$ pip install -r requirements.txt -i https://pypi.douban.com/simple/
#这里报错
  compilation terminated.
  error: command 'gcc' failed with exit status 1

$ 安装gcc依赖
$ yum  -y  install  gcc
$ sudo yum install python-devel
#到这 就能 执行了  pip install -r requirements.txt -i https://pypi.douban.com/simple/  
#但是网上还有别的依赖 我暂时先不安装了 如果报错 查看一下吧
```



# 04 撰写文章

万事俱备，接下来要写文档了。

在source目录下，新增文件 how_to_be_a_rich_man.rst（至于什么是rst格式呢，请自行搜索引擎噢）

文件内容如下

```
第一章 如何成为有钱人
======================

1.1 财富继承法
---------------------

有个有钱的老爸。


1.2 财富共享法
---------------------

有个有钱的老婆。
```

写好文档后，千万记得要把这个文档写进，目录排版里面。

排版配置文件是 `source\index.rst`，千万要注意中间的空行不可忽略。

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   how_to_be_a_rich_man
```

然后删除这几行

```
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

然后执行`make html` 生成html静态文件。

```
/opt/mkdocs
(mkdocs) $ make html
Running Sphinx v1.7.4
loading translations [zh_CN]... done
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 2 source files that are out of date
updating environment: [extensions changed] 2 added, 0 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded.

The HTML pages are in build\html.
```



```
'''
因为我这里是 我没有进行niginx  或者 apache 对我的页面进行配置 没办法提供web服务 所以这里我就没办法在页面上进行观看文档了 如果这个时候你已经出现上面的页面，那么我们接着往下走，直接让github和Read the  docs进行关联 最后你就可以 通过对你的文章进行修改 提交到github上 之后在read the  docs 进行一个触发 最后就可以看到你所提交的文档了.
'''
```



**好，以下是托管项目的操作步骤 **



执行完了后，你可以发现原先的build，不再是空文件夹了。

我们点进去 build\html\，打开index.html

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTH6OhZREcibTMhmbQicmz2385ktGBzqaoXt6xuhA4MeqrqkXx6NAiaxANPg/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

点击 我们刚写的暴富指南。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTHqbgWDNic4DFbEpTicIKgiaLib0BfHA0mcfn91lJ2OfbgWjxIogzJXDibjEw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

##  

# 05 托管项目 

看到网页的那一刻是不是相当激动。

不过别激动，这只是本地的，我们需要将其发布在线上。

这里我将工程文件，托管在`GitHub`上，然后由`Read the Docs`发布。

在托管之前呢，我们需要准备工作。在mkdocs根目录下，添加文件`.gitignore`（聪明的你，肯定知道这是什么），内容如下

`build/.idea/*.pyc`

接下来，在你的GitHub上新建一个仓库。然后把mkdocs这个目录下的所有文件都提交上去。步骤很简单，这里就不细讲,因为我的github上面有git的详细操作，如果git没有掌握，那么就学习下git先。

# 06 发布上线

托管完成后，我们要发布它，让别人可以访问。

你需要先去 `Read the Docs` 注册下帐号。

关联一下GitHub

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTHNicicLSFpyIibMFwRjBDhlY3zsJuLdsXSYMqhpD1ViaZiaL8M6F2o8Vqvdw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

 

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTHKZkVqe7PsMouxZQbA6JLPMvTwWQKnk9YVZJYDibLzGRUDU1xZiabOK8A/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

导入代码库。填好与你对应的信息。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTH8AMPRDCWdhtX9cWrVMTMAGz9L4ZMjibeAwG3ficeNZZgIma6REBIbgQA/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

 

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTHz6tmp4JgxB48QdjfIcIvATDElTpTJTo2YAibfWQsvpwe4BeseIFqvtw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

构建网页后。右下方，你可以看见你的在线地址。

![img](https://mmbiz.qpic.cn/mmbiz_png/UFM3uMlAXxOUM1o7Siado4CX2iaGlMibeTHCk3EA0OdX5MPSiaMhvJqZ4lCPLM3zkJ7BlANmmibQGp3IEPzj0HB8x7g/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这里要提醒一下的是，Sphinx的文档格式，默认是 rst 格式，如果你习惯了使用Markdown来写文章，可以使用 Pandoc 这个神器转换一下。

这里给出转换命令。

`pandoc -V mainfont="SimSun" -f markdown -t rst hello.md -o hello.rst`

或者你也可以在Sphinx上添加支持Markdown渲染的扩展模块及配置。也很简单，但是，我发现使用 md 文件，在网站上的导航无法实现跳转。

到这里，属于你的个人博客就搭建好了，快去试一下吧。

最后，感谢阅读。整个项目的源码和模块包我都放在我自己公众号后台，感兴趣的可以在后台回复「**sphinx**」领取。





# 07 总结

至此，搭建完成，结合了小编的公众号，之后踩了不是特别多的坑，嗯，这里的话，其实以后就按照这个rst的格式来进行书写就好了，陆续我会增加一些自己所学的rst格式或者工具，定期的分享给大家。
# PyCharm 使用Github管理Django项目]

不管是对于教程代码免费分享的需要，还是项目开发过程中的版本管理，Github都是我们首选的开源代码仓库，如果你没有私有仓库，并且不用保护代码，那么将项目上传到Github上是最佳的选择。

关于如何使用Git软件请自行学习，或许以后有空我也会写点教程。如何在PyCharm中配合Github，则在站点的博客中有一篇《[PyCharm 在PyCharm中使用GitHub](https://www.cnblogs.com/wcwnina/p/9112255.html)》，可供大家参考。

## 一、 创建requirement.txt文件

**requirement.txt**`（自命名）`文件是一个项目的**依赖库文件**，可以通过下面的方式自动生成：

进入虚拟环境，切换到项目根目录下，使用pip工具的 **freeze**（冻结）参数。

```
(mysite_env) F:\Django_course\mysite>pip freeze > requirement.txt
```

打开`requirement.txt`文件，其内容如下：

```
Django==1.11.7
django-simple-captcha==0.5.5
olefile==0.44
Pillow==4.3.0
pytz==2017.3
six==1.11.0
```

他人如果拷贝了我们的代码，要安装第三方库依赖的话，只需要：

```
pip install -r requirement.txt
```

就可以一次性安装好所有的库了。

## 二、创建.gitignore文件

在项目代码中，有一些文件是不能上传的，比如密码文件、数据库文件、核心配置文件等等，还有一些是不用上传的，比如临时文件。为了让git自动忽略这些文件，我们需要创建一个忽略名单。

在项目根目录下新建一个`.gitignore`文件，这里可能需要你在Pycharm下安装ignore插件，如下图所示：

![43.png-162kB](http://static.zybuluo.com/feixuelove1009/sesbyfupnop42neufjcddiil/43.png)

我这里是已经安装好了，新安装的话，要在搜索栏里搜索到插件后再安装。

在`.gitignore`文件里写入下面的内容：

```
.idea
settings.py
db.sqlite3
mysite/__pycache__/
```

这些文件将不会上传到Github中，也不会进行版本管理。

## 三、特殊文件处理

对于settings.py文件有个问题，如果没有这个文件是无法运行Django项目的，但是settings中又可能包含很多关键的不可泄露的部分，比如SECRET_KEY：

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b(&6i_$g2%8vh)ruu$)a9pkw+s-e&qj_e_#=@gnbo^48#gp_8a'
```

还有数据库的IP/port、用户名和密码，邮件发送端的用户名和密码，这些都是绝对不能泄露的。

那怎么办呢？简单！复制settings文件，并重命名为settings.example.py文件，放在同一目录里，把敏感信息、密码等修改或删除。使用者看到这个文件名，自然会明白它的作用。

## 四、添加说明文件和许可文件

通常我们要给Github的仓库添加说明文件和许可文件。

在项目根目录下创建一个`README.md`文件，这是markdown格式的。在文件里写入项目说明，使用方法，注意事项等等所有你认为需要说明的东西。

对于许可文件`LICENSE`，如果你暂时不想公开授权，或者不知道用哪种授权，可以暂时不提供。

下面是一个APACHE2.0授权的范例：

```
   mysite - User login and register system

   Copyright 2017- www.liujiangblog.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## 五、上传代码

在上传过程中，确认文件列表的时候，一定要注意查看没有保密文件被上传。

![44.png-58.4kB](http://static.zybuluo.com/feixuelove1009/kt1ef1vogwsctud4ohxr7mrs/44.png)

等待一会，项目文件上传完毕后，进入Github的仓库页面，如下所示：

![img](https://images2018.cnblogs.com/blog/1202586/201806/1202586-20180609180420797-1734223189.png)

 

点击进入详细页面：

![img](https://images2018.cnblogs.com/blog/1202586/201806/1202586-20180609180122073-1295608454.png)

 

现在，所有人都可以通过下面的方式，下载和使用本项目的源代码了：

```
git clone https://github.com/*******_project_1
```

## 六、使用Github仓库中的源码

如果你不是从教程的开始一步步地实现整个项目，而是直接使用从Github上copy下来的整个源码，那么你可能需要做一些额外的工作，比如：

- 创建虚拟环境
- 使用pip安装第三方依赖
- 修改settings.example.py文件为settings.py
- 运行migrate命令，创建数据库和数据表
- 运行python manage.py runserver启动服务器

而在Pycharm中运行服务器的话，可能还需要做一些额外的工作，比如：

- 配置解释器
- 配置启动参数

因为你本地Pycharm的配置情况，可能会发生不同的问题，需要根据实际情况实际处理，下面给两张配置图，供大家参考：

![47.png-91.5kB](http://static.zybuluo.com/feixuelove1009/enqnleo3mo0wp9eak6bswtrb/47.png)

![48.png-73.6kB](http://static.zybuluo.com/feixuelove1009/rckdsjzq2cp4ogeo5gtn7nti/48.png)

以上内容，都经过实际测试，如果你依然不能顺利启动服务器，请详细检查Pycharm的配置。

 

　　至此，转载请注明出处。

*[参考出处：http://www.liujiangblog.com/course/django/115，有改动]*
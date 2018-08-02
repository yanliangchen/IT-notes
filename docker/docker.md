# 一  .Docker 官方文档总结 

**官方文档  ：https://docs.docker.com/install/**

### 1.1 **版本 **

​	1.社区版(CE)非常适合希望开始使用Docker并尝试使用基于容器的应用的个人开发人员和小团队。

​	2.企业版(EE)）专为企业开发和IT团队而设计，他们可以在生产规模上构建，发布和运行关键业务应用程序。1



### 1.2 CE社区版安装Linux(ubuntu)

​	

 **一 . 安装Docker CE，您需要这些Ubuntu版本的64位版本：**

- Artful 17.10（Docker CE 17.11 Edge及更高版本）
- Xenial 16.04（LTS）
- Trusty 14.04（LTS）

  ​

  **二 . 卸载旧版本**

老版本的Docker被称为`docker`或`docker-engine`。如果这些已安装，请将其卸载：

```
$ sudo apt-get remove docker docker-engine docker.io
```



  **三 . 安装Docker CE**

  您可以根据您的需要以不同的方式安装Docker CE：

- 大多数用户 [设置Docker的存储库](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)并从中进行安装，以便安装和升级任务。这是推荐的方法。
- 有些用户下载DEB软件包并 [手动安装，](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-from-a-package)并完全手动管理升级。这对于在无法访问互联网的空隙系统上安装Docker等情况很有用。
- 在测试和开发环境中，一些用户选择使用自动 [便利脚本](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-convenience-script)来安装Docker。



  **四 .使用存储库进行安装**

​	首次在新主机上安装Docker CE之前，需要设置Docker存储库。之后，您可以从存储库安装和更新Docker。

1. 更新`apt`包裹索引：

   ```
   $ sudo apt-get update

   ```

2. 安装软件包以允许`apt`通过HTTPS使用存储库：

   ```
   $ sudo apt-get install \
       apt-transport-https \
       ca-certificates \
       curl \
       software-properties-common

   ```

3. 添加Docker的官方GPG密钥：

   ```
   $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

   ```

   `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`通过搜索指纹的最后8个字符，确认您现在拥有带指纹的密钥 。

   ```
   $ sudo apt-key fingerprint 0EBFCD88

   pub   4096R/0EBFCD88 2017-02-22
         Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
   uid                  Docker Release (CE deb) <docker@docker.com>
   sub   4096R/F273FCD8 2017-02-22

   ```

4. 使用以下命令设置**稳定的**存储库。即使您想从**边缘**或**测试**存储库安装构建，也总是需要**稳定的**存储 库。要添加**边缘**或 **测试**存储库，请在下面的命令中添加单词或（或两者）后面的单词。****************`edge``test``stable`

   > **注意**：下面的`lsb_release -cs`子命令返回您的Ubuntu发行版的名称，例如`xenial`。有时候，在像Linux Mint这样的发行版中，您可能需要更改`$(lsb_release -cs)` 为您的父级Ubuntu发行版。例如，如果您正在使用 `Linux Mint Rafaela`，您可以使用`trusty`。

   - [x86_64 / amd64]() （这里用的是64)
   - [armhf]()
   - [IBM Power（ppc64le）]()
   - [IBM Z（s390x）]()

   ```
   $ sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"
   ```



**五.安装DOCKER CE**

1. ****更新`apt`软件包索引。

   ```
   $ sudo apt-get update

   ```

2. 安装*最新版本*的Docker CE，或者转到下一步安装特定版本：  （这里2和3(是安装特定的版本) 进行选择 ）

   ```
   $ sudo apt-get install docker-ce

   ```

   > 有多个Docker存储库？
   >
   > 如果启用了多个Docker存储库，则安装或更新时未指定版本`apt-get install`或 `apt-get update`命令始终会安装尽可能高的版本，这可能不适合您的稳定性需求。

3. 要安装*特定版本*的Docker CE，请列出回购站中的可用版本，然后选择并安装：

   一个。列出您的回购中可用的版本：

   ```
   $ apt-cache madison docker-ce

   docker-ce | 18.03.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages

   ```

   湾 例如，通过其全限定包名称（它是包名称（`docker-ce`）“=”版本字符串（第二列））来 安装特定版本`docker-ce=18.03.0~ce-0~ubuntu`。

   ```
   $ sudo apt-get install docker-ce=<VERSION>

   ```

   Docker守护进程自动启动。

4. 通过运行`hello-world` 映像验证是否正确安装了Docker CE 。

   ```
   $ sudo docker run hello-world
   ```

   该命令下载测试图像并将其运行到容器中。当容器运行时，它会打印一条信息消息并退出。

5. docker 已正常运行 添加用户到docker组

   5.1 创建`docker`组。

   ```
   $ sudo groupadd docker

   ```

   5.2  将您的用户添加到`docker`组中。

   ```
   $ sudo usermod -aG docker $USER    //注释: 比如ubuntu用户  sudo  usermod -aG  docker  ubuntu

   ```

   5.3  注销并重新登录，以便重新评估您的组成员资格。

   如果在虚拟机上进行测试，则可能需要重新启动虚拟机才能使更改生效。

   在桌面Linux环境（如X Windows）上，完全退出会话并重新登录。

   ​

   5.4  验证您可以不使用运行`docker`命令`sudo`。

   ```
   $ docker run hello-world
   ```



 6.  开机是否启动设置

     ```
     $ sudo systemctl enable docker

     ```

     要禁用此行为，请`disable`改为使用。

     ```
     $ sudo systemctl disable docker
     ```



### 1.3 卸载Docker CE

1. 卸载Docker CE软件包：

   ```
   $ sudo apt-get purge docker-ce

   ```

2. 不会自动删除主机上的图像，容器，卷或自定义配置文件。删除所有图像，容器和卷：

   ```
   $ sudo rm -rf /var/lib/docker
   ```







# 开始使用Docker



## 2. 设置docker环境

### 2.1 Docker的概念

Docker是开发人员和系统管理员 使用容器**开发，部署和运行**应用程序的平台。使用Linux容器来部署应用程序称为*集装箱化*。容器不是新的，但它们用于轻松部署应用程序。

集装箱化越来越受欢迎，因为集装箱是：

- 灵活：即使是最复杂的应用程序也可以装箱。
- 轻量级：容器利用并共享主机内核。
- 可互换：您可以即时部署更新和升级。
- 便携式：您可以在本地构建，部署到云中并在任何地方运行。
- 可扩展性：您可以增加和自动分发容器副本。
- 可堆叠：您可以垂直堆叠服务并即时堆叠服务。



### 2.2 图像和容器

通过运行图像启动容器。一个**图像**是一个可执行的包，其中包括运行应用程序所需的所有内容-的代码，运行时，库，环境变量，和配置文件。

甲**容器**是图像的运行时实例-当被执行时（即，与状态的图像，或者用户进程）在存储器中什么图像变得。您可以使用该命令查看正在运行的容器的列表`docker ps`，就像在Linux中一样。

### 2.3 容器和虚拟机

一个**容器**中运行*原生* Linux和共享主机与其它容器的内核。它运行一个独立的进程，不占用任何其他可执行文件的内存，使其轻量化。

相比之下，**虚拟机**（VM）运行一个完整的“客户”操作系统，通过虚拟机管理程序*虚拟*访问主机资源。一般来说，虚拟机提供的环境比大多数应用程序需要的资源更多。



### 2.4 测试Docker版本

1. 运行`docker --version`并确保您拥有受支持的Docker版本：

   ```
   docker --version

   Docker version 17.12.0-ce, build c97c6d6

   ```

2. 运行`docker info`或（`docker version`不`--`）查看关于docker安装的更多详细信息：

   ```
   docker info

   Containers: 0
    Running: 0
    Paused: 0
    Stopped: 0
   Images: 0
   Server Version: 17.12.0-ce
   Storage Driver: overlay2
   ...
   ```



### 2.5测试Docker安装

1. 通过运行简单的Docker镜像[hello-world来](https://hub.docker.com/_/hello-world/)测试您的安装是否工作正常 ：

   ```
   docker run hello-world

   Unable to find image 'hello-world:latest' locally
   latest: Pulling from library/hello-world
   ca4f61b1923c: Pull complete
   Digest: sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7
   Status: Downloaded newer image for hello-world:latest

   Hello from Docker!
   This message shows that your installation appears to be working correctly.
   ...

   ```

2. 列出`hello-world`下载到您的机器的图像：

   ```
   docker image ls

   ```

3. 列出`hello-world`显示消息后退出的容器（由图像衍生）。如果它仍在运行，则不需要该`--all`选项：

   ```
   docker container ls --all

   CONTAINER ID     IMAGE           COMMAND      CREATED            STATUS
   54f4984ed6a8     hello-world     "/hello"     20 seconds ago     Exited (0) 19 seconds ago
   ```



### 2.6 回顾

```
## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
```



## 3.容器 (构建一个图像并将其作为一个容器运行)

**让您的环境快速测试运行，以确保您全部设置完毕：**

```
docker run hello-world
```

### **3.1介绍**

现在是开始以Docker方式构建应用程序的时候了。我们从这种应用程序的层次结构的底部开始，这是一个容器，我们将在此页面上介绍。在这个层次上面是一个服务，它定义了容器在生产中的行为方式，如[第3部分所述](https://docs.docker.com/get-started/part3/)。最后，在顶层是堆栈，定义了[第5部分中](https://docs.docker.com/get-started/part5/)涵盖的所有服务的交互。

- 堆
- 服务
- **容器**（你在这里）



### 3.2您的新开发环境

过去，如果您要开始编写Python应用程序，您的第一个业务就是将Python运行时安装到您的机器上。但是，这会造成您的计算机上的环境需要完美适合您的应用程序按预期运行，并且还需要与您的生产环境相匹配。

使用Docker，您可以将一个可移植的Python运行时作为一个映像获取，无需安装。然后，您的构建可以将基础Python图像与应用程序代码一起包括在内，确保您的应用程序，依赖项和运行时都一起旅行。

这些便携式图像是由称为a的东西定义的`Dockerfile`。



### 3.3定义一个容器`Dockerfile`

`Dockerfile`定义您的容器内环境中发生了什么。访问网络接口和磁盘驱动器等资源是在此环境中虚拟化的，与系统的其余部分隔离，因此您需要将端口映射到外部世界，并明确要将哪些文件“复制”到那个环境。但是，在完成这些之后，您可以期望在其中定义的应用程序的构建`Dockerfile`在其运行的任何位置都完全相同。



#### 3.3.1Dockerfile

****创建一个空目录。将目录（`cd`）更改为新目录，创建一个名为的文件`Dockerfile`，将以下内容复制并粘贴到该文件中并保存。注意解释新Dockerfile中每条语句的注释。

```
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

```

这`Dockerfile`是指我们还没有创建的几个文件，即 `app.py`和`requirements.txt`。接下来创建这些。

**应用程序本身**

****再创建两个文件，`requirements.txt`然后`app.py`将它们放在同一个文件夹中`Dockerfile`。这完成了我们的应用程序，您可以看到它非常简单。当上述`Dockerfile`被内置到的图像，`app.py`并且 `requirements.txt`是因为存在`Dockerfile`的`ADD`命令，并从输出`app.py`是通过HTTP得益于访问`EXPOSE` 命令。

**requirements.txt**

```
Flask
Redis

```

**app.py**

```
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

```

现在我们看到`pip install -r requirements.txt`为Python安装Flask和Redis库，并且该应用程序输出环境变量`NAME`以及调用的输出`socket.gethostname()`。最后，因为Redis没有运行（因为我们只安装了Python库，而不是Redis本身），所以我们应该期望在这里使用它的尝试失败并产生错误消息。

> **注意**：在容器中访问主机的名称将检索容器ID，这与正在运行的可执行文件的进程ID相似。

而已！您`requirements.txt`的系统中不需要Python或其他任何东西，也不需要在系统上安装或运行此映像。看起来你并没有真正用Python和Flask建立一个环境，但是你已经拥有了。



**构建应用程序**

我们准备构建应用程序。确保您仍然处于新目录的顶层。以下是`ls`应该显示的内容：

```
$ ls
Dockerfile		app.py			requirements.txt

```

现在运行build命令。这会创建一个Docker镜像，我们将使用`-t`它来标记，因此它有一个友好的名称。

```
docker build -t friendlyhello .

```

你的建筑图像在哪里？它在你的机器的本地Docker镜像注册表中：

```
$ docker image ls

REPOSITORY            TAG                 IMAGE ID
friendlyhello         latest              326387cea398

```



**运行应用程序**

****运行应用程序，使用以下命令将计算机的端口4000映射到容器的已发布端口80 `-p`：

```
docker run -p 4000:80 friendlyhello

```

您应该看到Python正在为您的应用提供服务的消息`http://0.0.0.0:80`。但是该消息来自容器内部，它不知道你将该容器的端口80映射到4000，从而制作正确的URL `http://localhost:4000`。

在网页浏览器中转到该网址以查看网页上显示的显示内容。

![浏览器中的Hello World](https://docs.docker.com/get-started/images/app-in-browser.png)

> **注意**：如果您在Windows 7上使用Docker Toolbox，请使用Docker Machine IP而不是`localhost`。例如，http://192.168.99.100:4000/。要查找IP地址，请使用该命令`docker-machine ip`。

您也可以`curl`在shell中使用该命令来查看相同的内容。

```
$ curl http://localhost:4000

<h3>Hello World!</h3><b>Hostname:</b> 8fc990912a14<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>

```

这个端口重新映射`4000:80`是为了展示你`EXPOSE`内部`Dockerfile`和你`publish`使用的 内容之间的区别`docker run -p`。在后面的步骤中，我们只需将主机上的端口80映射到容器中的端口80并使用即可`http://localhost`。



现在让我们以分离模式在后台运行应用程序：

```
docker run -d -p 4000:80 friendlyhello
```



**停止应用程序**

您可以获取应用的长容器ID，然后将其踢回到您的终端。您的容器正在后台运行。您还可以看到带有缩写的容器ID `docker container ls`（并且在运行命令时可以互换使用）：

```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED
1fa4ab2cf395        friendlyhello       "python app.py"     28 seconds ago

```

注意`CONTAINER ID`匹配的内容`http://localhost:4000`。

现在`docker container stop`用来结束这个过程，使用`CONTAINER ID`如下所示：

```
docker container stop 1fa4ab2cf395
```











#### 3.3.2 分享您的image



##### **1. 先注册一个docker账户**

      		1.  **用户**名：liyanliang	
        2.  密码:renyisi886
           3. 邮箱：18518274668@163.com



##### **2. 创建一个存储库**



##### **3. 使用您的Docker ID登录**

如果您没有Docker帐户，请在[cloud.docker.com](https://cloud.docker.com/)注册一个帐户 。记下你的用户名。

登录到本地计算机上的Docker公共注册表。

```
$ docker login
```



##### **4. 标记图像**

****将本地映像与注册表中的存储库相关联的符号是 `username/repository:tag`。该标签是可选的，但建议使用，因为它是注册管理机构用于为Docker镜像提供版本的机制。为该上下文提供存储库并标记有意义的名称，例如 `get-started:part2`。这将图像放入`get-started`存储库并标记为`part2`。

现在，把它放在一起来标记图像。`docker tag image`使用您的用户名，存储库和标签名称运行，以便将图像上传到您想要的目的地。该命令的语法是：

```
docker tag image username/repository:tag

```

例如：

```
docker tag friendlyhello john/get-started:part2

```

运行[docker图像ls](https://docs.docker.com/engine/reference/commandline/image_ls/)以查看新标记的图像。

```
$ docker image ls

REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
friendlyhello            latest              d9e555c53008        3 minutes ago       195MB
john/get-started         part2               d9e555c53008        3 minutes ago       195MB
python                   2.7-slim            1c7128a655f6        5 days ago          183MB
...

```



##### **5.发布图像**

将您的标记图像上传到存储库：

```
docker push username/repository:tag

```

完成后，此上传的结果将公开发布。如果您登录到[Docker Hub](https://hub.docker.com/)，则可以通过其pull命令在那里看到新映像。





##### **6.从远程存储库中提取并运行图像**

从现在开始，您可以使用`docker run`此命令在任何机器上使用并运行您的应用程序：

```
docker run -p 4000:80 username/repository:tag
```







## 4.   服务

#### **4.1 先决条件（前提）**

- [安装Docker版本1.13或更高版本](https://docs.docker.com/engine/installation/)。
- 获取[Docker撰写](https://docs.docker.com/compose/overview/)。在[Docker for Mac](https://docs.docker.com/docker-for-mac/)和[Docker for Windows中，](https://docs.docker.com/docker-for-windows/)它已预先安装，所以你很好用。在Linux系统上，您需要[直接安装它](https://github.com/docker/compose/releases)。在*没有Hyper-V的* Windows 10系统之前 ，使用[Docker Toolbox](https://docs.docker.com/toolbox/overview/)。
- 阅读[第1部分中](https://docs.docker.com/get-started/)的方向。
- 学习如何在[第2部分中](https://docs.docker.com/get-started/part2/)创建容器。
- 确保您已将发布的`friendlyhello`图像 [推送到注册表中](https://docs.docker.com/get-started/part2/#share-your-image)。我们在这里使用该共享图像。
- 确保你的图像作为一个部署的容器。运行此命令，在您的信息开槽`username`，`repo`和`tag`：`docker run -p 80:80 username/repo:tag`，然后访问`http://localhost/`。
- ​

#### 4.2 介绍

在第3部分中，我们扩展了我们的应用并实现了负载平衡。要做到这一点，我们必须在分布式应用程序的层次结构中升级一级： **服务**。

- 堆

- **服务**（你在这里）

- 容器（[第2部分](https://docs.docker.com/get-started/part2/)涵盖）

  ​

#### 4.3 关于服务

在分布式应用程序中，应用程序的不同部分被称为“服务”。例如，如果您想象一个视频共享站点，它可能包含一个用于将应用程序数据存储在数据库中的服务，一个用于在后台进行视频转码的服务用户上传的东西，前端的服务等等。

服务实际上只是“生产中的容器”。服务只运行一个映像，但它编码图像运行的方式 - 应该使用哪个端口，容器应运行多少个副本，以便服务具有所需的容量，以及等等。缩放服务会更改运行该软件的容器实例的数量，从而为流程中的服务分配更多计算资源。

幸运的是，使用Docker平台定义，运行和扩展服务非常简单 - 只需编写一个`docker-compose.yml`文件即可。

##### 1. 你的第一个docker-compose.yml文件

一个`docker-compose.yml`文件是一个YAML文件，它定义了Docker容器在生产中的行为方式。

`docker-compose.yml`

将该文件保存为`docker-compose.yml`您想要的任何位置。确保您已将 [第2部分中](https://docs.docker.com/get-started/part2/)创建[的图像推](https://docs.docker.com/get-started/part2/#share-your-image)送到注册表中，并通过替换 图像详细信息来更新此图像。`.yml``username/repo:tag`

```
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:

```

该`docker-compose.yml`文件告诉Docker执行以下操作：

- 从注册表中拉出[我们在步骤2中上传的图像](https://docs.docker.com/get-started/part2/)。
- 运行该图像的5个实例作为所调用的服务`web`，限制每个实例使用最多10％的CPU（跨所有核心）和50MB的RAM。
- 如果一个失败，立即重启容器。
- 将主机上的端口80映射到`web`端口80。
- `web`通过称为负载平衡的网络指示容器共享端口80 `webnet`。（在内部，容器本身`web`在临时端口上发布到 80端口。）
- `webnet`使用默认设置定义网络（这是一个负载平衡覆盖网络）。

##### 2. 运行新的负载平衡应用程序

在我们可以使用该`docker stack deploy`命令之前，我们首先运行：

```
docker swarm init

```

> **注意**：我们在[第4部分讨论](https://docs.docker.com/get-started/part4/)了该命令的含义。如果你没有运行，`docker swarm init`你会得到一个错误，“这个节点不是一个群管理器。”

现在我们来运行它。你需要给你的应用一个名字。在这里，它被设置为 `getstartedlab`：

```
docker stack deploy -c docker-compose.yml getstartedlab

```

我们的单个服务堆栈在一台主机上运行了5个部署映像的容器实例。让我们来调查。

在我们的应用程序中获取一项服务的服务ID：

```
docker service ls

```

查找服务的输出`web`，并在您的应用程序名称前加上。如果您将其命名为与此示例中所示的相同，则名称为 `getstartedlab_web`。还列出了服务ID以及副本数量，映像名称和端口暴露量。

在服务中运行的单个容器称为**任务**。任务会获得数值增加的唯一ID，直到`replicas`您定义 的数量`docker-compose.yml`。列出您的服务的任务：

```
docker service ps getstartedlab_web

```

如果您只列出系统中的所有容器，但也不会显示服务过滤的任务，也会显示任务：

```
docker container ls -q

```

您可以`curl -4 http://localhost`连续运行多次，也可以在浏览器中转到该网址并点击几次刷新。

![浏览器中的Hello World](https://docs.docker.com/get-started/images/app80-in-browser.png)

无论哪种方式，容器ID都会发生变化，从而显示负载平衡; 在每个请求中，以循环方式选择5个任务中的一个来响应。容器ID与前一个命令（`docker container ls -q`）的输出相匹配。

> 运行Windows 10？
>
> Windows 10 PowerShell应该已经`curl`可用了，但是如果没有的话，你可以抓取一个像[Git BASH](https://git-for-windows.github.io/)这样的Linux终端仿真器 ，或者下载非常相似的[wget for Windows](http://gnuwin32.sourceforge.net/packages/wget.htm)。

> 响应时间慢？
>
> 根据您的环境的网络配置，容器可能需要长达30秒才能响应HTTP请求。这并不代表Docker或群集性能，而是我们稍后在本教程中讨论的未满足的Redis依赖项。就目前而言，访客柜台并不是出于同样的原因; 我们还没有添加服务来保存数据。



##### 3. 扩展应用程序

您可以通过更改其中的`replicas`值`docker-compose.yml`，保存更改并重新运行该`docker stack deploy`命令来缩放应用程序：

```
docker stack deploy -c docker-compose.yml getstartedlab

```

Docker执行一个就地更新，不需要先撕下堆栈或杀死任何容器。

现在，重新运行`docker container ls -q`以查看重新配置的已部署实例。如果您扩大了副本，则会启动更多任务，从而启动更多容器。



##### 4. 取下应用程序和群

- 将应用删除`docker stack rm`：

  ```
  docker stack rm getstartedlab

  ```

- 强制取下这个程序的leader  (docker  swarm  init  是生成leader)

  ```
  docker swarm leave --force

  ```

用Docker站起来并扩展您的应用程序非常简单。您已经朝着学习如何在生产中运行容器迈出了一大步。接下来，您将学习如何将这个应用程序作为Docker机器群集上的真正群体运行。









## **5.** docker集群（没搞定)



# 二.菜鸟教程docker(补充)

### **1.docker  容器使用命令**



#### 1.0运行一个web应用

前面我们运行的容器并没有一些什么特别的用处。

接下来让我们尝试使用 docker 构建一个 web 应用程序。

我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用。

```
runoob@runoob:~# docker pull training/webapp  # 载入镜像
runoob@runoob:~# docker run -d -P training/webapp python app.py
```



#### 

#### **1.1 查看网络端口的快捷方式**

​		上面我们创建的web应用**容器ID为:7a38a1ad55c6** **名字为：determined_swanson**

​		1.**docker  ps 能查看docker容器id **

​		2.**runoob@runoob:~$ docker port 7a38a1ad55c6**     

​		**runoob@runoob:~$ docker port determined_swanson**

​		结果：5000/tcp -> 0.0.0.0:5000





#### 1.2 查看WEB应用程序日志

```
runoob@runoob:~$ docker logs -f 7a38a1ad55c6
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
192.168.239.1 - - [09/May/2016 16:30:37] "GET / HTTP/1.1" 200 -
192.168.239.1 - - [09/May/2016 16:30:37] "GET /favicon.ico HTTP/1.1" 404 -
```



#### 1.3  查看WEB应用程序容器的进程

```
runoob@runoob:~$ docker top determined_swanson
```



#### 1.4 检查WEB应用程序

```
使用 docker inspect 来查看Docker的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

runoob@runoob:~$ docker inspect determined_swanson
[
    {
        "Id": "7a38a1ad55c6914b360b565819604733db751d86afd2575236a70a2519527361",
        "Created": "2016-05-09T16:20:45.427996598Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
......
```



#### 1.5 停止WEB应用容器

```
runoob@runoob:~$ docker stop determined_swanson   
determined_swanson
```



#### 1.6重启WEB应用程序

```
runoob@runoob:~$ docker start determined_swanson
determined_swanson
```



#### **1.7 移除WEB应用容器**

```
runoob@runoob:~$ docker rm determined_swanson  
determined_swanson

删除容器时，容器必须是停止状态，否则会报如下错误
runoob@runoob:~$ docker rm determined_swanson
Error response from daemon: You cannot remove a running container 7a38a1ad55c6914b360b565819604733db751d86afd2575236a70a2519527361. Stop the container before attempting removal or use -f
```





### 2.Docker镜像使用(容器里面有镜像)

#### 2.0 **Docker 镜像使用**

当运行容器时，使用的镜像如果在本地中不存在，docker 就会自动从 docker 镜像仓库中下载，默认是从 Docker Hub 公共镜像源下载。



#### 2.1 列出镜像列表

```
runoob@runoob:~$ docker images           
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
php                 5.6                 f40e9e0f10c8        9 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        4 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
training/webapp     latest              6fae60ef3446        11 months ago       348.8 MB


//各个选项说明
REPOSITORY：表示镜像的仓库源

TAG：镜像的标签

IMAGE ID：镜像ID

CREATED：镜像创建时间

SIZE：镜像大小


```

**可以下载不同版本的镜像往容器里 从仓库源 ，容器里可以是有服务，可以是有系统**

```
同一仓库源可以有多个 TAG，代表这个仓库源的不同个版本，如ubuntu仓库源里，有15.10、14.04等多个不同的版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。

所以，我们如果要使用版本为15.10的ubuntu系统镜像来运行容器时，命令如下：

runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash 
root@d77ccb2e5cca:/#
如果要使用版本为14.04的ubuntu系统镜像来运行容器时，命令如下：

runoob@runoob:~$ docker run -t -i ubuntu:14.04 /bin/bash 
root@39e968165990:/# 
```



#### 2.2 获取一个新的镜像

```
当我们在本地主机上使用一个不存在的镜像时 Docker 就会自动下载这个镜像。如果我们想预先下载这个镜像，我们可以使用 docker pull 命令来下载它。

Crunoob@runoob:~$ docker pull ubuntu:13.10
13.10: Pulling from library/ubuntu
6599cadaf950: Pull complete 
23eda618d451: Pull complete 
f0be3084efe9: Pull complete 
52de432f084b: Pull complete 
a3ed95caeb02: Pull complete 
Digest: sha256:15b79a6654811c8d992ebacdfbd5152fcf3d165e374e264076aa435214a947a3
Status: Downloaded newer image for ubuntu:13.10
下载完成后，我们可以直接使用这个镜像来运行容器。
```



#### 2.3 查找镜像 

```
我们可以从 Docker Hub 网站来搜索镜像，Docker Hub 网址为： https://hub.docker.com/
我们也可以使用 docker search 命令来搜索镜像。比如我们需要一个httpd的镜像来作为我们的web服务。我们可以通过 docker search 命令搜索 httpd 来寻找适合我们的镜像。

runoob@runoob:~$  docker search httpd


//注释

NAME:镜像仓库源的名称

DESCRIPTION:镜像的描述

OFFICIAL:是否docker官方发布
```



#### 2.4 拖取镜像

```
我们决定使用上图中的httpd 官方版本的镜像，使用命令 docker pull 来下载镜像。

runoob@runoob:~$ docker pull httpd
Using default tag: latest
latest: Pulling from library/httpd
8b87079b7a06: Pulling fs layer 
a3ed95caeb02: Download complete 
0d62ec9c6a76: Download complete 
a329d50397b9: Download complete 
ea7c1f032b5c: Waiting 
be44112b72c7: Waiting
下载完成后，我们就可以使用这个镜像了。

runoob@runoob:~$ docker run httpd
```



#### 2.5 创建镜像

```
当我们从docker镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。

1.从已经创建的容器中更新镜像，并且提交这个镜像
2.使用 Dockerfile 指令来创建一个新的镜像
```



#### 2.6更新镜像

```
更新镜像之前，我们需要使用镜像来创建一个容器。
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash
root@e218edb10161:/# 
```



 1. 在运行的容器内使用 apt-get update 命令进行更新。

  ​ **1.1   然后我们使用docker ps查看到该容器信息，接下来就使用docker attach进入该容器**

  ​	**$ sudo docker attach e218edb10161** 

  ​	 **$ sudo docker exec -it 775c7c9ee1e1 /bin/bash** 

2.在完成操作之后，输入 exit命令来退出这个容器。

此时ID为e218edb10161的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit来提交容器副本。

```
runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8



//
各个参数说明：

-m:提交的描述信息

-a:指定镜像作者

e218edb10161：容器ID

runoob/ubuntu:v2:指定要创建的目标镜像名
```



3. 我们可以使用 **docker images** 命令来查看我们的新镜像 **runoob/ubuntu:v2**：

```
runoob@runoob:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/ubuntu       v2                  70bf1840fd7c        15 seconds ago      158.5 MB
ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
php                 5.6                 f40e9e0f10c8        9 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        4 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
training/webapp     latest              6fae60ef3446        12 months ago       348.8 MB
```

   

4.使用我们的新镜像 **runoob/ubuntu** 来启动一个容器

```
runoob@runoob:~$ docker run -t -i runoob/ubuntu:v2 /bin/bash                            
root@1a9fbdeb5da3:/#
```



#### 2.7构建镜像

我们使用命令 **docker build** ， 从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。

```
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7
MAINTAINER      Fisher "fisher@sudops.com"

RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd runoob
RUN     /bin/echo 'runoob:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
EXPOSE  22
EXPOSE  80
CMD     /usr/sbin/sshd -D
```

每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。

第一条FROM，指定使用哪个镜像源

RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。

然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。

```
runoob@runoob:~$ docker build -t runoob/centos:6.7 .
Sending build context to Docker daemon 17.92 kB
Step 1 : FROM centos:6.7
 ---&gt; d95b5ca17cc3
Step 2 : MAINTAINER Fisher "fisher@sudops.com"
 ---&gt; Using cache
 ---&gt; 0c92299c6f03
Step 3 : RUN /bin/echo 'root:123456' |chpasswd
 ---&gt; Using cache
 ---&gt; 0397ce2fbd0a
Step 4 : RUN useradd runoob
......
```

参数说明：

- **-t** ：指定要创建的目标镜像名
- **.** ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径

使用docker images 查看创建的镜像已经在列表中存在,镜像ID为860c279d2fec

```
runoob@runoob:~$ docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
runoob/centos       6.7                 860c279d2fec        About a minute ago   190.6 MB
runoob/ubuntu       v2                  70bf1840fd7c        17 hours ago         158.5 MB
ubuntu              14.04               90d5884b1ee0        6 days ago           188 MB
php                 5.6                 f40e9e0f10c8        10 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago          182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago          324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago          194.4 MB
ubuntu              15.10               4e3b13c8a266        5 weeks ago          136.3 MB
hello-world         latest              690ed74de00f        6 months ago         960 B
centos              6.7                 d95b5ca17cc3        6 months ago         190.6 MB
training/webapp     latest              6fae60ef3446        12 months ago        348.8 MB
```

我们可以使用新的镜像来创建容器

```
runoob@runoob:~$ docker run -t -i runoob/centos:6.7  /bin/bash
[root@41c28d18b5fb /]# id runoob
uid=500(runoob) gid=500(runoob) groups=500(runoob)
```

从上面看到新镜像已经包含我们创建的用户runoob

------





#### 2.8设置镜像标签

我们可以使用 docker tag 命令，为镜像添加一个新的标签。

```
runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev
```

docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。

使用 docker images 命令可以看到，ID为860c279d2fec的镜像多一个标签。

```
runoob@runoob:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/centos       6.7                 860c279d2fec        5 hours ago         190.6 MB
runoob/centos       dev                 860c279d2fec        5 hours ago         190.6 MB
runoob/ubuntu       v2                  70bf1840fd7c        22 hours ago        158.5 MB
ubuntu              14.04               90d5884b1ee0        6 days ago          188 MB
php                 5.6                 f40e9e0f10c8        10 days ago         444.8 MB
nginx               latest              6f8d099c3adc        13 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        5 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
centos              6.7                 d95b5ca17cc3        6 months ago        190.6 MB
training/webapp     latest              6fae60ef3446        12 months ago       348.8 MB
```





### 3.Docker容器链接（待续)

#### 3.0 Docker 容器连接

前面我们实现了通过网络端口来访问运行在docker容器内的服务。下面我们来实现通过端口连接到一个docker容器



#### 3.1 网络端口映射

我们创建了一个 python 应用的容器。

```
runoob@runoob:~$ docker run -d -p training/webapp  python app.py
```

另外，我们可以指定容器绑定的网络地址，比如绑定127.0.0.1.

我们使用**-P**参数创建一个容器，使用**docker  ps** 来看端口5000绑定主机端口32768

```
runoob@runoob:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
fce072cc88ce        training/webapp     "python app.py"     4 minutes ago       Up 4 minutes        0.0.0.0:32768->5000/tcp   grave_hopper
```

我们也可以使用 **-p** 标识来指定容器端口绑定到主机端口。

两种方式的区别是：

- **-P :**是容器内部端口随机映射到主机的高端口。
- **-p : **是容器内部端口绑定到指定的主机端口。

```
runoob@runoob:~$ docker run -d -p 5000:5000 training/webapp python app.py
33e4523d30aaf0258915c368e66e03b49535de0ef20317d3f639d40222ba6bc0
```



```
runoob@runoob:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                     NAMES
33e4523d30aa        training/webapp     "python app.py"     About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp    berserk_bartik
fce072cc88ce        training/webapp     "python app.py"     8 minutes ago        Up 8 minutes        0.0.0.0:32768->5000/tcp   grave_hopper
```

另外，我们可以指定容器绑定的网络地址，比如绑定127.0.0.1。

```
runoob@runoob:~$ docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
95c6ceef88ca3e71eaf303c2833fd6701d8d1b2572b5613b5a932dfdfe8a857c
runoob@runoob:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                NAMES
95c6ceef88ca        training/webapp     "python app.py"     6 seconds ago       Up 6 seconds        5000/tcp, 127.0.0.1:5001->5000/tcp   adoring_stonebraker
33e4523d30aa        training/webapp     "python app.py"     3 minutes ago       Up 3 minutes        0.0.0.0:5000->5000/tcp               berserk_bartik
fce072cc88ce        training/webapp     "python app.py"     10 minutes ago      Up 10 minutes       0.0.0.0:32768->5000/tcp              grave_hopper
```

这样我们就可以通过访问127.0.0.1:5001来访问容器的5000端口。

上面的例子中，默认都是绑定 tcp 端口，**如果要绑定 UDP 端口**，可以在端口后面加上 **/udp**。

```
runoob@runoob:~$ docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
6779686f06f6204579c1d655dd8b2b31e8e809b245a97b2d3a8e35abe9dcd22a
runoob@runoob:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                NAMES
6779686f06f6        training/webapp     "python app.py"     4 seconds ago       Up 2 seconds        5000/tcp, 127.0.0.1:5000->5000/udp   drunk_visvesvaraya
95c6ceef88ca        training/webapp     "python app.py"     2 minutes ago       Up 2 minutes        5000/tcp, 127.0.0.1:5001->5000/tcp   adoring_stonebraker
33e4523d30aa        training/webapp     "python app.py"     5 minutes ago       Up 5 minutes        0.0.0.0:5000->5000/tcp               berserk_bartik
fce072cc88ce        training/webapp     "python app.py"     12 minutes ago      Up 12 minutes       0.0.0.0:32768->5000/tcp              grave_hopper
```

**docker port** 命令可以让我们快捷地查看端口的绑定情况。

```
runoob@runoob:~$ docker port adoring_stonebraker 5000
127.0.0.1:5001
```



#### 3.2 Docker容器连接

端口映射并不是唯一把 docker 连接到另一个容器的方法。

docker有一个连接系统允许将多个容器连接在一起，共享连接信息。

docker连接会创建一个父子关系，其中父容器可以看到子容器的信息。

------

#### 3.3 容器命名

当我们创建一个容器的时候，docker会自动对它进行命名。另外，我们也可以使用--name标识来命名容器，例如：

```
runoob@runoob:~$  docker run -d -P --name runoob training/webapp python app.py
43780a6eabaaf14e590b6e849235c75f3012995403f97749775e38436db9a441
```

我们可以使用 **docker ps** 命令来查看容器名称。

```
runoob@runoob:~$ docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
43780a6eabaa        training/webapp     "python app.py"     3 minutes ago       Up 3 minutes        0.0.0.0:32769->5000/tcp   runoob
```





### 4.  Docker 安装 Nginx  

#### 4.0 容器只运行单个应用的好处

```
从技术角度讲，你可以在Docker容器中运行多个进程。你可以将数据库，前端，后端，ssh，supervisor都运行在同一个Docker容器中。但是，这会让你非常痛苦:

非常长的构建时间(修改前端之后，整个后端也需要重新构建)
非常大的镜像大小
多个应用的日志难以处理(不能直接使用stdout，否则多个应用的日志会混合到一起)
横向扩展时非常浪费资源(不同的应用需要运行的容器数并不相同)
僵尸进程问题 - 你需要选择合适的init进程
因此，我建议大家为每个应用构建单独的Docker镜像，然后使用 Docker Compose 运行多个Docker容器
```



#### 4.0.0  中间镜像Dockerfile文件及编写镜像的步骤

总结自：http://www.jb51.net/article/115327.htm

##### 4.0.0.1 一,将多个RUN指令合并为一个

```
一 .将多个RUN指令合并为一个
0.Docker镜像是分层的，
1. Dockerfile中的每个指令都会创建一个新的镜像层。
2.镜像层将被缓存和复用
3.当Dockerfile的指令修改了，复制的文件变化了，或者构建镜像时指定的变量不同了，对应的镜像层缓存就会失效
某一层的镜像缓存失效之后，它之后的镜像层缓存都会失效
4.镜像层是不可变的，如果我们再某一层中添加一个文件，然后在下一层中删除它，则镜像中依然会包含该文件(只是这个文件在Docker容器中不可见了)。
5.Docker镜像类似于洋葱。它们都有很多层。为了修改内层，则需要将外面的层都删掉。记住这一点的话，其他内容就很好理解了。
///
现在，我们将所有的RUN指令合并为一个。同时把apt-get upgrade删除，因为它会使得镜像构建非常不确定(我们只需要依赖基础镜像的更新就好了) 记住一点，我们只能将变化频率一样的指令合并在一起。将node.js安装与npm模块安装放在一起的话，则每次修改源代码，都需要重新安装node.js，这显然不合适。
```



##### 4.0.0.2 二，基础镜像的标签不要用latest

```
当镜像没有指定标签时，将默认使用latest 标签。因此， FROM ubuntu 指令等同于FROM ubuntu:latest。当时，当镜像更新时，latest标签会指向不同的镜像，这时构建镜像有可能失败。如果你的确需要使用最新版的基础镜像，可以使用latest标签，否则的话，最好指定确定的镜像标签。

示例Dockerfile应该使用16.04作为标签。
```



##### 4.0.0.3 三，每个RUN指令后删除多余文件

```
假设我们更新了apt-get源，下载，解压并安装了一些软件包，它们都保存在/var/lib/apt/lists/目录中。但是，运行应用时Docker镜像中并不需要这些文件。我们最好将它们删除，因为它会使Docker镜像变大。

示例Dockerfile中，我们可以删除/var/lib/apt/lists/目录中的文件(它们是由apt-get update生成的)。
```



##### 4.0.0.4 四，选择合适的基础镜像（alpine版本最好)

```
在示例中，我们选择了ubuntu作为基础镜像。但是我们只需要运行node程序，有必要使用一个通用的基础镜像吗？node镜像应该是更好的选择。
```

```
更好的选择是alpine版本的node镜像。alpine是一个极小化的Linux发行版，只有4MB，这让它非常适合作为基础镜像。
```



##### 4.0.0.5 五，设置WORKDIR 和CMD

```
WORKDIR指令可以设置默认目录，也就是运行RUN / CMD / ENTRYPOINT指令的地方。
CMD指令可以设置容器创建是执行的默认命令。另外，你应该讲命令写在一个数组中，数组中每个元素为命令的每个单词。

//egg
FROM node:7-alpine
 
WORKDIR /app
ADD . /app
RUN npm install
 
CMD ["npm", "start"] 
```



##### 4.0.0.6 六，使用ENTRYPOINT 

```
NTRYPOINT指令并不是必须的，因为它会增加复杂度。ENTRYPOINT是一个脚本，它会默认执行，并且将指定的命令错误其参数。它通常用于构建可执行的Docker镜像。entrypoint.sh如下:
#!/usr/bin/env sh
# $0 is a script name, 
# $1, $2, $3 etc are passed arguments
# $1 is our command
CMD=$1
 
case "$CMD" in 
 "dev" )
  npm install
  export NODE_ENV=development
  exec npm run dev
  ;;
 
 "start" )
  # we can modify files here, using ENV variables passed in 
  # "docker create" command. It can't be done during build process.
  echo "db: $DATABASE_ADDRESS" >> /app/config.yml
  export NODE_ENV=production
  exec npm start
  ;;
 
  * )
  # Run custom command. Thanks to this line we can still use 
  # "docker run our_image /bin/bash" and it will work
  exec $CMD ${@:2}
  ;;
esac 
```



##### 4.0.0.7 七，在entrypoint脚本中使用exec

```
在前文的entrypoint脚本中，我使用了exec命令运行node应用。不使用exec的话，我们则不能顺利地关闭容器，因为SIGTERM信号会被bash脚本进程吞没。exec命令启动的进程可以取代脚本进程，因此所有的信号都会正常工作。
```



##### 4.0.0.8 八，COPY与ADD优先使用前者

```
COPY指令非常简单，仅用于将文件拷贝到镜像中。ADD相对来讲复杂一些，可以用于下载远程文件以及解压压缩包(参考官方文档)。
```



##### 4.0.0.9 九，合理调整COPY与RUN的顺序

```
我们应该把变化最少的部分放在Dockerfile的前面，这样可以充分利用镜像缓存。

示例中，源代码会经常变化，则每次构建镜像时都需要重新安装NPM模块，这显然不是我们希望看到的。因此我们可以先拷贝package.json，然后安装NPM模块，最后才拷贝其余的源代码。这样的话，即使源代码变化，也不需要重新安装NPM模块（安装 node.js的工具）。
```



##### 4.0.0.10  十，设置环境变量，映射端口和数据

```
运行Docker容器时很可能需要一些环境变量。在Dockerfile设置默认的环境变量是一种很好的方式。另外，我们应该在Dockerfile中设置映射端口和数据卷。示例如下:

ENV指令指定的环境变量在容器中可以使用。如果你只是需要指定构建镜像时的变量，你可以使用ARG指令。
```



##### 4.0.0.11 十一 ，使用LABEL设置镜像元数据

```
使用LABEL设置镜像元数据
使用LABEL指令，可以为镜像设置元数据，例如镜像创建者或者镜像说明。旧版的Dockerfile语法使用MAINTAINER指令指定镜像创建者，但是它已经被弃用了。有时，一些外部程序需要用到镜像的元数据，例如nvidia-docker需要用到com.nvidia.volumes.needed。示例如下:
FROM node:7-alpine 
LABEL maintainer "jakub.skalecki@example.com"
```



##### 4.0.0.12  十二 ，添加HEALTHCHECK

```
1 . 运行容器时，可以指定--restart always选项。这样的话，容器崩溃时，Docker守护进程(docker daemon)会重启容器
2 . 对于需要长时间运行的容器，这个选项非常有用。
3 . 但是，如果容器的确在运行，但是不可(陷入死循环，配置错误)用怎么办？使用HEALTHCHECK指令可以让Docker周期性的检查容器的健康状况。我们只需要指定一个命令，如果一切正常的话返回0，否则返回1。
```



#### 4.1 **方法1，通过Dockerfile构建** 

**创建Dockerfile**

 1  . 首先，创建目录nigix,用于存放后面的相关东西 

```
runoob@runoob:~$ mkdir -p ~/nginx/www ~/nginx/logs ~/nginx/conf
```

www目录将映射为nginx容器配置的虚拟目录

logs目录将映射为nginx容器的日志目录

conf目录里的配置文件映射为nginx容器的配置文件

进入创建的nginx目录，创建Dockerfile 


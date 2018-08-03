# 一、Kubernetes系列之介绍篇

 摘自：https://blog.csdn.net/real_myth/article/details/78719244

**•Kubernetes介绍**

1.背景介绍

　　云计算飞速发展

　　　　- IaaS

　　　　- PaaS

　　　　- SaaS

　　Docker技术突飞猛进

　　　　- 一次构建，到处运行

　　　　- 容器的快速轻量

　　　　- 完整的生态环境

2.什么是kubernetes

　　首先，他是一个全新的基于容器技术的分布式架构领先方案。Kubernetes(k8s)是Google开源的容器集群管理系统（谷歌内部:Borg）。在Docker技术的基础上，为容器化的应用提供部署运行、资源调度、服务发现和动态伸缩等一系列完整功能，提高了大规模容器集群管理的便捷性。

　　Kubernetes是一个完备的分布式系统支撑平台，具有完备的集群管理能力，多扩多层次的安全防护和准入机制、多租户应用支撑能力、透明的服务注册和发现机制、內建智能负载均衡器、强大的故障发现和自我修复能力、服务滚动升级和在线扩容能力、可扩展的资源自动调度机制以及多粒度的资源配额管理能力。同时Kubernetes提供完善的管理工具，涵盖了包括开发、部署测试、运维监控在内的各个环节。

Kubernetes中，Service是分布式集群架构的核心，一个Service对象拥有如下关键特征：

- 拥有一个唯一指定的名字
- 拥有一个虚拟IP（Cluster IP、Service IP、或VIP）和端口号
- 能够体统某种远程服务能力
- 被映射到了提供这种服务能力的一组容器应用上

　　Service的服务进程目前都是基于Socket通信方式对外提供服务，比如Redis、Memcache、MySQL、Web Server，或者是实现了某个具体业务的一个特定的TCP Server进程，虽然一个Service通常由多个相关的服务进程来提供服务，每个服务进程都有一个独立的Endpoint（IP+Port）访问点，但Kubernetes能够让我们通过服务连接到指定的Service上。有了Kubernetes内奸的透明负载均衡和故障恢复机制，不管后端有多少服务进程，也不管某个服务进程是否会由于发生故障而重新部署到其他机器，都不会影响我们队服务的正常调用，更重要的是这个Service本身一旦创建就不会发生变化，意味着在Kubernetes集群中，我们不用为了服务的IP地址的变化问题而头疼了。

　　容器提供了强大的隔离功能，所有有必要把为Service提供服务的这组进程放入容器中进行隔离。为此，Kubernetes设计了Pod对象，将每个服务进程包装到相对应的Pod中，使其成为Pod中运行的一个容器。为了建立Service与Pod间的关联管理，Kubernetes给每个Pod贴上一个标签Label，比如运行MySQL的Pod贴上name=mysql标签，给运行PHP的Pod贴上name=php标签，然后给相应的Service定义标签选择器Label Selector，这样就能巧妙的解决了Service于Pod的关联问题。

　　在集群管理方面，Kubernetes将集群中的机器划分为一个Master节点和一群工作节点Node，其中，在Master节点运行着集群管理相关的一组进程kube-apiserver、kube-controller-manager和kube-scheduler，这些进程实现了整个集群的资源管理、Pod调度、弹性伸缩、安全控制、系统监控和纠错等管理能力，并且都是全自动完成的。Node作为集群中的工作节点，运行真正的应用程序，在Node上Kubernetes管理的最小运行单元是Pod。Node上运行着Kubernetes的kubelet、kube-proxy服务进程，这些服务进程负责Pod的创建、启动、监控、重启、销毁以及实现软件模式的负载均衡器。

　　在Kubernetes集群中，它解决了传统IT系统中服务扩容和升级的两大难题。你只需为需要扩容的Service关联的Pod创建一个Replication Controller简称（RC），则该Service的扩容及后续的升级等问题将迎刃而解。在一个RC定义文件中包括以下3个关键信息。

- 目标Pod的定义
- 目标Pod需要运行的副本数量（Replicas）
- 要监控的目标Pod标签（Label）

　　在创建好RC后，Kubernetes会通过RC中定义的的Label筛选出对应Pod实例并实时监控其状态和数量，如果实例数量少于定义的副本数量，则会根据RC中定义的Pod模板来创建一个新的Pod，然后将新Pod调度到合适的Node上启动运行，知道Pod实例的数量达到预定目标，这个过程完全是自动化。

　　

　Kubernetes优势:

　　　　- 容器编排

　　　　- 轻量级

　　　　- 开源

　　　　- 弹性伸缩

　　　　- 负载均衡

**•Kubernetes的核心概念**

1.Master

　　k8s集群的管理节点，负责管理集群，提供集群的资源数据访问入口。拥有Etcd存储服务（可选），运行Api Server进程，Controller Manager服务进程及Scheduler服务进程，关联工作节点Node。Kubernetes API server提供HTTP Rest接口的关键服务进程，是Kubernetes里所有资源的增、删、改、查等操作的唯一入口。也是集群控制的入口进程；Kubernetes Controller Manager是Kubernetes所有资源对象的自动化控制中心；Kubernetes  Schedule是负责资源调度（Pod调度）的进程

 

2.Node

　　Node是Kubernetes集群架构中运行Pod的服务节点（亦叫agent或minion）。Node是Kubernetes集群操作的单元，用来承载被分配Pod的运行，是Pod运行的宿主机。关联Master管理节点，拥有名称和IP、系统资源信息。运行docker eninge服务，守护进程kunelet及负载均衡器kube-proxy.

- 每个Node节点都运行着以下一组关键进程
- kubelet：负责对Pod对于的容器的创建、启停等任务
- kube-proxy：实现Kubernetes Service的通信与负载均衡机制的重要组件
- Docker Engine（Docker）：Docker引擎，负责本机容器的创建和管理工作

　　Node节点可以在运行期间动态增加到Kubernetes集群中，默认情况下，kubelet会想master注册自己，这也是Kubernetes推荐的Node管理方式，kubelet进程会定时向Master汇报自身情报，如操作系统、Docker版本、CPU和内存，以及有哪些Pod在运行等等，这样Master可以获知每个Node节点的资源使用情况，冰实现高效均衡的资源调度策略。、

 

3.Pod

　　运行于Node节点上，若干相关容器的组合。Pod内包含的容器运行在同一宿主机上，使用相同的网络命名空间、IP地址和端口，能够通过localhost进行通。Pod是Kurbernetes进行创建、调度和管理的最小单位，它提供了比容器更高层次的抽象，使得部署和管理更加灵活。一个Pod可以包含一个容器或者多个相关容器。

　　Pod其实有两种类型：普通Pod和静态Pod，后者比较特殊，它并不存在Kubernetes的etcd存储中，而是存放在某个具体的Node上的一个具体文件中，并且只在此Node上启动。普通Pod一旦被创建，就会被放入etcd存储中，随后会被Kubernetes Master调度到摸个具体的Node上进行绑定，随后该Pod被对应的Node上的kubelet进程实例化成一组相关的Docker容器冰启动起来，在。在默认情况下，当Pod里的某个容器停止时，Kubernetes会自动检测到这个问起并且重启这个Pod（重启Pod里的所有容器），如果Pod所在的Node宕机，则会将这个Node上的所有Pod重新调度到其他节点上。

 

4.Replication Controller

　　Replication Controller用来管理Pod的副本，保证集群中存在指定数量的Pod副本。集群中副本的数量大于指定数量，则会停止指定数量之外的多余容器数量，反之，则会启动少于指定数量个数的容器，保证数量不变。Replication Controller是实现弹性伸缩、动态扩容和滚动升级的核心。

 

5.Service

外部系统访问Service的问题

　　首先需要弄明白Kubernetes的三种IP这个问题

　　　　Node IP：Node节点的IP地址

　　　　Pod IP： Pod的IP地址

　　　　Cluster IP：Service的IP地址

　　首先,Node IP是Kubernetes集群中节点的物理网卡IP地址，所有属于这个网络的服务器之间都能通过这个网络直接通信。这也表明Kubernetes集群之外的节点访问Kubernetes集群之内的某个节点或者TCP/IP服务的时候，必须通过Node IP进行通信

　　其次，Pod IP是每个Pod的IP地址，他是Docker Engine根据docker0网桥的IP地址段进行分配的，通常是一个虚拟的二层网络。

　　最后Cluster IP是一个虚拟的IP，但更像是一个伪造的IP网络，原因有以下几点

- Cluster IP仅仅作用于Kubernetes Service这个对象，并由Kubernetes管理和分配P地址
- Cluster IP无法被ping，他没有一个“实体网络对象”来响应
- Cluster IP只能结合Service Port组成一个具体的通信端口，单独的Cluster IP不具备通信的基础，并且他们属于Kubernetes集群这样一个封闭的空间。

Kubernetes集群之内，Node IP网、Pod IP网于Cluster IP网之间的通信，采用的是Kubernetes自己设计的一种编程方式的特殊路由规则。

 

6.Label

　Kubernetes中的任意API对象都是通过Label进行标识，Label的实质是一系列的Key/Value键值对，其中key于value由用户自己指定。Label可以附加在各种资源对象上，如Node、Pod、Service、RC等，一个资源对象可以定义任意数量的Label，同一个Label也可以被添加到任意数量的资源对象上去。Label是Replication Controller和Service运行的基础，二者通过Label来进行关联Node上运行的Pod。

我们可以通过给指定的资源对象捆绑一个或者多个不同的Label来实现多维度的资源分组管理功能，以便于灵活、方便的进行资源分配、调度、配置等管理工作。

一些常用的Label如下：

- 版本标签："release":"stable","release":"canary"......
- 环境标签："environment":"dev","environment":"qa","environment":"production"
- 架构标签："tier":"frontend","tier":"backend","tier":"middleware"
- 分区标签："partition":"customerA","partition":"customerB"
- 质量管控标签："track":"daily","track":"weekly"

　　Label相当于我们熟悉的标签，给某个资源对象定义一个Label就相当于给它大了一个标签，随后可以通过Label Selector（标签选择器）查询和筛选拥有某些Label的资源对象，Kubernetes通过这种方式实现了类似SQL的简单又通用的对象查询机制。

 

　　Label Selector在Kubernetes中重要使用场景如下:

- - 　　kube-Controller进程通过资源对象RC上定义Label Selector来筛选要监控的Pod副本的数量，从而实现副本数量始终符合预期设定的全自动控制流程
  - 　　kube-proxy进程通过Service的Label Selector来选择对应的Pod，自动建立起每个Service岛对应Pod的请求转发路由表，从而实现Service的智能负载均衡
  - 　　通过对某些Node定义特定的Label，并且在Pod定义文件中使用Nodeselector这种标签调度策略，kuber-scheduler进程可以实现Pod”定向调度“的特性

 

•**Kubernetes架构和组件**

![img](http://images2015.cnblogs.com/blog/1087716/201704/1087716-20170411111532391-899038129.png)

 

　　- 服务分组，小集群，多集群

　　- 服务分组，大集群，单集群

 

**•Kubernetes 组件:**

　　Kubernetes Master控制组件，调度管理整个系统（集群），包含如下组件:

　　1.Kubernetes API Server

　　　　作为Kubernetes系统的入口，其封装了核心对象的增删改查操作，以RESTful API接口方式提供给外部客户和内部组件调用。维护的REST对象持久化到Etcd中存储。

　　2.Kubernetes Scheduler

　　　　为新建立的Pod进行节点(node)选择(即分配机器)，负责集群的资源调度。组件抽离，可以方便替换成其他调度器。

　　3.Kubernetes Controller

　　　　负责执行各种控制器，目前已经提供了很多控制器来保证Kubernetes的正常运行。

　　4. Replication Controller

　　　　管理维护Replication Controller，关联Replication Controller和Pod，保证Replication Controller定义的副本数量与实际运行Pod数量一致。

　　5. Node Controller

　　　　管理维护Node，定期检查Node的健康状态，标识出(失效|未失效)的Node节点。

　　6. Namespace Controller

　　　　管理维护Namespace，定期清理无效的Namespace，包括Namesapce下的API对象，比如Pod、Service等。

　　7. Service Controller

　　　　管理维护Service，提供负载以及服务代理。

　　8.EndPoints Controller

　　　　管理维护Endpoints，关联Service和Pod，创建Endpoints为Service的后端，当Pod发生变化时，实时更新Endpoints。

　　9. Service Account Controller

　　　　管理维护Service Account，为每个Namespace创建默认的Service Account，同时为Service Account创建Service Account Secret。

　　10. Persistent Volume Controller

　　　　管理维护Persistent Volume和Persistent Volume Claim，为新的Persistent Volume Claim分配Persistent Volume进行绑定，为释放的Persistent Volume执行清理回收。

　　11. Daemon Set Controller

　　　　管理维护Daemon Set，负责创建Daemon Pod，保证指定的Node上正常的运行Daemon Pod。

　　12. Deployment Controller

　　　　管理维护Deployment，关联Deployment和Replication Controller，保证运行指定数量的Pod。当Deployment更新时，控制实现Replication Controller和　Pod的更新。

　　13.Job Controller

　　　　管理维护Job，为Jod创建一次性任务Pod，保证完成Job指定完成的任务数目

　　14. Pod Autoscaler Controller

　　　　实现Pod的自动伸缩，定时获取监控数据，进行策略匹配，当满足条件时执行Pod的伸缩动作。

 

**•Kubernetes Node运行节点，运行管理业务容器，包含如下组件:**

　　1.Kubelet

　　　　负责管控容器，Kubelet会从Kubernetes API Server接收Pod的创建请求，启动和停止容器，监控容器运行状态并汇报给Kubernetes API Server。

　　2.Kubernetes Proxy

　　　　负责为Pod创建代理服务，Kubernetes Proxy会从Kubernetes API Server获取所有的Service信息，并根据Service的信息创建代理服务，实现Service到Pod的请求路由和转发，从而实现Kubernetes层级的虚拟转发网络。

　　3.Docker

　　　　Node上需要运行容器服务

# [二、基于kubernetes构建Docker集群环境实战](http://www.cnblogs.com/xhyan/p/6655731.html)

kubernetes是google公司基于docker所做的一个分布式集群，有以下主件组成

　　etcd: 高可用存储共享配置和服务发现，作为与minion机器上的flannel配套使用，作用是使每台 minion上运行的docker拥有不同的ip段，最终目的是使不同minion上正在运行的docker containner都有一个与别的任意一个containner（别的minion上运行的docker containner）不一样的IP地址。

　　flannel: 网络结构支持

　　kube-apiserver: 不论通过kubectl还是使用remote api 直接控制，都要经过apiserver

　　kube-controller-manager: 对replication controller, endpoints controller, namespace controller, and serviceaccounts controller的循环控制，与kube-apiserver交互，保证这些controller工作

　　kube-scheduler: Kubernetes scheduler的作用就是根据特定的调度算法将pod调度到指定的工作节点（minion）上，这一过程也叫绑定（bind)

　　kubelet: Kubelet运行在Kubernetes Minion Node上. 它是container agent的逻辑继任者

　　kube-proxy: kube-proxy是kubernetes 里运行在minion节点上的一个组件, 它起的作用是一个服务代理的角色

 

**图为GIT+Jenkins+Kubernetes+Docker+Etcd+confd+Nginx+Glusterfs架构**：

**如下：**

 

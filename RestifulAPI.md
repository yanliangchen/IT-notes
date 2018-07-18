# 我的理解 RESTful Api 架构

2016年02月19日 09:00:08

阅读数：1317

## 一些常见的误解

不要以为 RESTful Api  就是设计得像便于 SEO 的伪静态，例如一个 Api 的 URL 类似于 <http://xxx.com/blog/1> ，我们可以通过浏览器访问该 URL 而读取文章，但是这并不代表着它就是 RESTful Api 。

也不要认为URL 里有 queryString 就不是 RESTful Api ，例如 <http://xxx.com/users/?page=10&page_size=30>

更不要认为 HTTP + JSON 就是 RESTful ApI 了。

## REST 和 HTTP/1.1 

Roy Fielding （Apache HTTP 服务器的核心开发者，Apache 软件基金会的合作创始人，HTTP/1.1 协议专家组的负责人）总结了一套理论框架，然后使用这套理论框架中的指导原则，来指导HTTP/1.1协议的设计方向。后来他在其的博士学位论文 Architectural Styles and the Design of Network-based Software Architectures 中更为系统、严谨地阐述了这套理论框架，并且使用这套理论框架推导出了一种新的架构风格，并且为这种架构风格取了一个令人轻松愉快的名字 REST。

想必通过这个你已经明白了 REST 和 HTTP/1.1 的密不可分的关系了吧。HTTP/1.1 的很多特性就是 REST 的特性，比如连接的无状态性。还有后面说的 REST 五大特性都和 HTTP/1.1 协议密不可分。

## RESTful Api 与 SOAP Web API 在 URL 形式上的对比

### 从设计一个删除评论的 api 说起 

我们可以这样设计成类似于：

<http://mengkang.net/?method=comment.del&id=x> ①

<http://mengkang.net/comment/del/id/x> ②

或者其他形式的 url。

而 RESTful Api 则是：

[DELETE] [http://mengkang.net/comments/1](http://mengkang.net/comment/1) ③

我们对比可以发现①和② URL 中，都有`del`的动作指示。

> SOAP Web API采用RPC风格，它采用面向功能的架构，所以我们在设计SOAP Web API的时候首相考虑的是应高提供怎样的功能（或者操作）。
>
> 而 RESTful Api 是面向资源的架构。是查询、新增、修改、删除，都该资源无关。

所以我们在③ URL 中没有看到`del`的关键字，对比②和③最为明显。

## 进一步认识 RESTful Api 

我们知道 URL 全称为“统一资源定位符（Uniform Resource Locator）”，用于描述 Web 资源所在的位置。RESTful Api 是以 HTTP 协议为强烈依托的，将类似于①和②这种以功能为主导的URL风格舍弃，还原 URL 的本质，它的宗旨就是一个 URL 就应该是一个资源，不能包含任何动作。

`PUT`和`PATCH`的功能都可以代表更新，但略有不同，`PUT`大多时候表示更新该资源的全部信息，而`PATCH`则更新部分信息。

`PUT`和`POST`又一些功能的重叠，都可以是新建一个资源，`POST`时，新建资源的地址是由服务器返回给客户端的。也就是说客户端在发送`POST`请求资源之前还无法预知该资源的地址，这在我们的 Api 开发中非常常见，新建一个帖子，新建一条评论，都如此。

而资源的地址是客户端预先知道的情况则比较少。也有人如此设计而使用`PUT`，比如需要对 github 上的某人的项目 star ，则可能会设计成：<http://github.com/xxx/zhoumengkang/projectname/star> 这里把“对这个项目已经点赞过”看成了一个资源，那么就可以用`PUT`，因为要删除这个资源时，还是访问这个 URL。

关于这些功能上有交集的地方，可能后面会有一些更加标准的规范或者协议吧。

最后说下`HEAD`和`OPTIONS`，`HEAD`请求的是资源的元数据，比如一张照片，的元数据则可能包含了，照片拍摄的设备，地点，时间等。服务器一般将对应资源的元数据置于响应的报头集合返回给客户端，这样的响应一般不具有主体部分。`OPTIONS`则是发送一种“探测”请求以确定针对某个目标地址的请求必须具有怎样的约束（比如应该采用怎样的HTTP方法以及自定义的请求报头），然后根据其约束发送真正的请求。

关于过滤筛选，排序和 token 等 query string 是支持使用，和唯一资源的概念并不冲突。

## 我所理解的无状态性和唯一资源对 Api Url 的设计指导

举一个实际的例子，用户黑名单的 CURD。我们可是设计成

如上的 api 设计中，首先如上的 url 设计中，通过授权码中获取登录用户 uid。则是有状态的了，其次因为所有的用户访问的资源都是同一个地址，这与唯一资源的概念是相违背的。如果是无状态的，那么就与唯一资源的概念相吻合了。（这只是 restful 所建议的，实际是否需要完全遵守视情况而定）

## REST的五大特性

1. 资源（Resource）
2. 资源的表述（Representation）
3. 状态转移（State Transfer）
4. 统一接口（Uniform Interface）
5. 超文本驱动（Hypertext Driven）

资源的概念是 RESTful 里面最重要的一个概念，很容易被我们忽视和误解，所以就重点阐述了这一特性。

而其他特性，我们日常开发应该都是遵守的，就不再展开说了，需要了解的可以看我的这篇笔记 [REST的五个特性](http://mengkang.net/623.html) 。



## REST 状态码

理论上来说我们应该以 Http response status code 作为客户端的标准，而不是在 Http body 体里面定义。这样客户端的能够更快速的获取服务端的响应状态码。

但是由于国内某些网络商会劫持状态码非`200`的请求，跳转到他们的广告地址。所以大家还是考虑国内的实际情况。

## REST 架构风格约束

1. 客户-服务器（Client-Server）通信只能由客户端单方面发起，表现为请求-响应的形式。
2. 无状态（Stateless）通信的会话状态（Session State）应该全部由客户端负责维护。
3. 缓存（Cache）响应内容可以在通信链的某处被缓存，以改善网络效率。
4. 统一接口（Uniform Interface）通信链的组件之间通过统一的接口相互通信，以提高交互的可见性。
5. 分层系统（Layered System）通过限制组件的行为（即，每个组件只能“看到”与其交互的紧邻层），将架构分解为若干等级的层。

文字比较学院派，仔细一想，想必也发现我们实际工作都已经遵守这五条架构风格了。

短短的一篇文章无法涵盖所有内容，这里推荐下 [Github Api](https://developer.github.com/v3/)， 可以作为大家设计 RSETful Api 的最佳范例。





s







# [REST的五个关键词](javascript:;)

[周梦康](https://mengkang.net/about.me) 发表于 2016-01-05 分类于 [tips](https://mengkang.net/tips.html) [3600 次浏览](https://mengkang.net/623.html) 标签 : [REST](https://mengkang.net/tag-86.html)

要深入理解REST，需要理解REST的五个关键词：

1. 资源（Resource）
2. 资源的表述（Representation）
3. 状态转移（State Transfer）
4. 统一接口（Uniform Interface）
5. 超文本驱动（Hypertext Driven）

### 资源

关于资源的理解在<http://mengkang.net/620.html>里已经说了很多了。

### 资源的表述

实际是资源暴露出来的展现形式，拿[GET]访问的请求来说就是通过浏览器访问某个地址之后所得到的内容。

### 状态转移

我所理解的，将客户端对资源操作的状态通过 Api 的请求转移到服务端。比如客户端需要删除某个资源，请求完，服务器端该资源的状态也是删除的了。

### 统一接口

REST要求，必须通过统一的接口来对资源执行各种操作。对于每个资源只能执行一组有限的操作。以HTTP/1.1协议为例，HTTP/1.1协议定义了一个操作资源的统一接口，主要包括以下内容：

1. 7个HTTP方法：GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS
2. HTTP头信息（可自定义）
3. HTTP响应状态代码（可自定义）
4. 一套标准的内容协商机制（即接口内容输出之后，各个字段各个对象如何解析的定义）
5. 一套标准的缓存机制
6. 一套标准的客户端身份认证机制

### 超文本驱动

就像网页里的超链接，得到当前接口的返回内容，app 布局上对应的各个按钮下一步可能会请求 api 需要在当前 api 予以给出。

举个例子 <https://developer.github.com/v3/git/commits/#get-a-commit> 返回的内容为

里面的`parents`节点里有一个`url`字段，而对应的客户端上有一个查看其父节点的按钮，点击那个按钮，就会向这个`url`对应的`api`发送请求了。

下一步操作的执行，不是客户端需要自身关心的，而是`api`返回的文档内容驱动的。

个人觉得，这些标准实际在我们开发的时候无形中就实现并遵守了，就想数据库设计范式一样，不遵守，没法玩了。




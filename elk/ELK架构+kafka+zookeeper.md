# ELK日志分析框架从搭建踩坑到实例教学

  	摘自：http://www.360zhijia.com/360anquanke/330910.html

![ELK日志分析框架从搭建踩坑到实例教学](https://p1.ssl.qhimg.com/t01547ae7e29edf5e8a.jpg)

Elk是elasticsearch+logstash+kibana的简称，是一个开源的日志分析的框架，在这三个组件中，这三个组件的作用如下：

- elasticsearch是存储，可以理解为数据库，把数据存起来并建立索引，方便用户的查询。
- Kibana是展示用的组件，负责将数据进行可视化呈现。同时有控制台，可以直接对es进行操作，
- Logstash是这个elk的核心组件，是日志的过滤器。它负责将日志进行格式化，然后传给elasticsearch进行存储。同时logstash也有一些组件，可以进行一些数据分析的工作。

这三个组件之间的逻辑关系是logstash-elasticsearch-kibana，但是在实际操作中并没有那么简单。因为还有一些问题需要考虑：

- 日志怎么实时读取？
- 为了避免大并发的情况下造成的信息丢失，需要使用cache，cache怎么设置？
- 怎么实现集群化部署？集群化部署的话，负载均衡的问题怎么考虑？

因此，一个完整的elk的架构应该是这个样子的：

![ELK日志分析框架从搭建踩坑到实例教学](https://p4.ssl.qhimg.com/t01f934bbe9b829ac57.png)

图1 elk架构图1

- Filebeat负责从web服务器上实时抓取数据，当log文件发生变化时，将文件内容吐给kafka。
- Kafka是消息队列，主要作用是在filebeat和logstash之间做缓存，避免因写入logstash的数据量过大，导致数据丢失。同样的解决方案还有redis。activemq，ribbitmq也是消息队列，但是因为filebeat没有相对应的输出格式，因此在这个方案中不做考虑。
- Zookeeper是kafka的分发系统，他负责维护整个kafka集群的负载均衡，在部署的时候，每个kafka节点上都要单独安装zookeeper，同时要保证zookeeper之间能够互相通信（2181端口）。
- Logstash是日志处理器，也是整个elk系统的核心。负责来自kafka的日志处理，然后把处理过的日志吐给elasticsearch。需要注意的是，经logstash处理过的日志都是json格式的。同时logstash还有众多插件，在这个里面需要用到的logstash-input-kafka就是插件之一。还有一些有趣的函数，例如geoip，可以根据ip找出ip的所在的位置。
- Elasticsearch可以理解为是一个存储，它将logstash传来的数据存储起来、建立索引，由于elasticsearch建立的是全文索引，这点有区别于同类产品splunk，所以在查询数据的准确度和速度上都有所提高，适合于大数据检索，但是做大数据检索时，需要集群化部署，典型的用空间换时间的做法。
- Kibana是一个图形化展示的工具，能够根据elasticsearch中存储的数据进行可视化展示。同时在高版本的kibana中，还提供了开发者工具，可以直接写elastcsearch的查询语句，并进行查询，可以看作是elasticsearch的一个可视化用户端。

接下来是一些概念。

- 生产者（producer）和消费者（consumer）：这组概念是消息队列的一组概念，主要指的的是消息的生产者和消息的接收者。在消息队列中，生产者产生消息，吐到消息队列中，消费者从消息队列中抽取消息。在点对点的消息队列模式中，可以有多个生产者，但是只能有一个消费者；在topic的消息队列模式中，可以有多个消费者���Kafka是topic模式的消息队列，这也就为未来的logstash集群化提供了可行性。
- 集群（cluster）：集群就是将多个提供相同服务的服务器整合起来，统一提供服务，不再各自为政。但是。集群化并不是仅仅能够内部互访互通这么简单，集群的负载，任务分发，统一管理都是集群化需要考虑的问题。
- 索引（index）：索引简单理解就是一个目录，有了这个东西之后，可以大大提高检索效率。Elasticsearch的主要作用在于对全文建立了索引，并且配合这个索引，有极快的检索速度，也是所有关系型数据库的核心。
- 输入（input），输出（output）和过滤（filter）：logstash的一组概念，指的是logstash的输入源，输出地以及对数据的处理方式。在logstash上至少需要指定出输入和输出，这样logstash就会把原文作为message字段统一写入elasticsearch，如果不想这样，就要添加过滤，对message字段进行筛选，处理。
- 点对点模式（queue）和发布/订阅模式（topic）：queue模式是一种传统的消息队列模式，消息不再队列中存储，这也就表示消息不可重复消费，topic模式是生产者将消息生产到topic中，可以有多个消费者来共同消费这个topic中的消息，表示消息可以重复消费。如下图所示：

![ELK日志分析框架从搭建踩坑到实例教学](https://p4.ssl.qhimg.com/t018a7c64e6d52b9555.png)

图2 点对点模式

![ELK日志分析框架从搭建踩坑到实例教学](https://p0.ssl.qhimg.com/t01e19687ec275cec6d.png)
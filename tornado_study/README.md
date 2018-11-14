### 1. tornado安装

  **python  -m  pip  install  tornado**

### 2. image目录

**1 . http请求流程，**

**2. tornado,django,flask三种框架的区别，**

**3. tornado高性能 : epoll机制**

​	

```
简单理解：
ioloop封装了epoll

epoll返回可处理的socket 

把所有socket都放入到epoll里 

不用挨个循环判断 看哪个可以处理了 

如果需要更好了解需要看看epoll和select的机制，后续陆续学习
```


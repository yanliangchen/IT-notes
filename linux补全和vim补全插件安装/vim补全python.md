

### **Python攻克之路-vim实现python的补全功能** 



```

环境：CentOS7.4 Python3.6
1. 更新系统安装包
[root@node2 ~]# yum update
　　
2. 安装python包

[root@node2 ~]# pip install pep8 flake8 pyflakes isort yapf
PyFlakes：静态检查Python代码逻辑错误的工具
pep8： 静态检查PEP 8编码风格的工具
isort：在python中是一个使import 列表更美观的工具包
YAPF (Yet Another Python Formatter)是Google开源的一个用来格式化Python代码的工具. 支持2种代码规范

3. 下载.vimrc文件
[root@node2 ~]# wget https://raw.githubusercontent.com/fisadev/fisa-vim-config/master/.vimrc
　　
4. install plugin
[root@node2 ~]# vim .vimrc #会自动安装加载
```

![img](https://images2018.cnblogs.com/blog/1142788/201804/1142788-20180430084904013-680236054.png)
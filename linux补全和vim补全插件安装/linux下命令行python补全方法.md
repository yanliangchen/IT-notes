很多时候，在linux下编写python时，

 

都懒得去vi一个新文件，直接就新开一个终端，

 

进入python命令行模式，然后就可以写一些测试代码。 

 

不过最悲剧的就是，刚开始使用的时候，每个字母都要自己写，

 

不能像linux普通终端那样用tab来自动完成。 

 

于是，在网上搜索了一番，终于还是被我找到了，特此记录一下。

 

 首先，在宿主目录~下，

 

新建一个.pythonstartup.py文件（linux debian类的系统用“.”号开始表示隐藏文件），然后在该文件写入以下代码：

 

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
  
import readline, rlcompleter; 
readline.parse_and_bind("tab: complete"); # 启用Tab补全
 
def igtk():
   globals()['gtk'] = __import__('gtk');
   globals()['thread'] = __import__('thread');
   gtk.gdk.threads_init();
   thread.start_new_thread(gtk.main, ());
   pass;
```

 

 

 保存之后，我们需要将该文件添加到环境变量中，这里采用修改~/.bashrc文件来添加环境变量。

 

 用vi打开~/.bashrc文件，在文件末尾添加如下代码： 

 

```
export PYTHONSTARTUP=~/.pythonstartup.py
```

```
source  ~/.bashrc
```

现在终端上进入python命令模式后，就可以用tab来自动完成了
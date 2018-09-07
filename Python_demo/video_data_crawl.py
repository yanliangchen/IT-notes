


'''
下载流式文件，requests库中请求的stream设为True就可以啦，[文档在此](http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow)。

先找一个视频地址试验一下：

'''
# -*- coding: utf-8 -*-
import requests
 
def download_file(url, path):
    #stream=True请求连接不会被关闭,除非读取所有数据或者调用Response.close
    with requests.get(url, stream=True) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
 

'''
看样子是没有实现上下文需要的__exit__方法。既然只是为了保证要让r最后close以释放连接池，那就使用contextlib的closing特性好了：
'''

# -*- coding: utf-8 -*-
import requests
from contextlib import closing
 
def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)




'''
程序正常运行了，不过我盯着这文件，怎么大小不见变啊，到底是完成了多少了呢？还是要让下好的内容及时存进硬盘，还能省点内存是不是：
'''

# -*- coding: utf-8 -*-
import requests
from contextlib import closing
import os
 
def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())


'''
文件以肉眼可见的速度在增大，真心疼我的硬盘，还是最后一次写入硬盘吧，程序中记个数就好了

'''

def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            n = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                loaded = n*1024.0/content_size
                f.write(chunk)
                print '已下载{0:%}'.format(loaded)
                n += 1

'''
结果就很直观了：

已下载2.579129%
已下载2.581255%
已下载2.583382%
已下载2.585508%
'''

'''
心怀远大理想的我怎么会只满足于这一个呢，写个类一起使用吧：
'''
# -*- coding: utf-8 -*-
import requests
from contextlib import closing
import time
 
def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024*10
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            p = ProgressData(size = content_size, unit='Kb', block=chunk_size)
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                p.output()
 
 
class ProgressData(object):
 
    def __init__(self, block,size, unit, file_name='', ):
        self.file_name = file_name
        self.block = block/1000.0
        self.size = size/1000.0
        self.unit = unit
        self.count = 0
        self.start = time.time()
    def output(self):
        self.end = time.time()
        self.count += 1
        speed = self.block/(self.end-self.start) if (self.end-self.start)>0 else 0
        self.start = time.time()
        loaded = self.count*self.block
        progress = round(loaded/self.size, 4)
        if loaded >= self.size:
            print u'%s下载完成\r\n'%self.file_name
        else:
            print u'{0}下载进度{1:.2f}{2}/{3:.2f}{4} 下载速度{5:.2%} {6:.2f}{7}/s'.\
                  format(self.file_name, loaded, self.unit,\
                  self.size, self.unit, progress, speed, self.unit)
            print '%50s'%('/'*int((1-progress)*50))

'''
运行：

下载开始
下载进度10.24Kb/120174.05Kb 0.01% 下载速度4.75Kb/s
/////////////////////////////////////////////////
下载进度20.48Kb/120174.05Kb 0.02% 下载速度32.93Kb/s
/////////////////////////////////////////////////
'''

'''
看上去舒服多了。

下面要做的就是多线程同时下载了，主线程生产url放入队列，下载线程获取url：
'''
# -*- coding: utf-8 -*-
import requests
from contextlib import closing
import time
import Queue
import hashlib
import threading
import os
 
 
def download_file(url, path):
    #一直保持连接 closing   正常的with语句  如果操作数据库，网络请求他会自动关闭
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024*10
        #r.headers 获得响应文本
        content_size = int(r.headers['content-length'])
        if os.path.exists(path) and os.path.getsize(path)>=content_size:
            print '已下载'
            return
        print '下载开始'
        with open(path, "wb") as f:
            p = ProgressData(size = content_size, unit='Kb', block=chunk_size, file_name=path)
            #分块进行来写入
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                p.output()
 
 
class ProgressData(object):
 
    def __init__(self, block,size, unit, file_name='', ):
        self.file_name = file_name
        self.block = block/1000.0
        self.size = size/1000.0
        self.unit = unit
        self.count = 0
        self.start = time.time()
    def output(self):
        self.end = time.time()
        self.count += 1
        speed = self.block/(self.end-self.start) if (self.end-self.start)>0 else 0
        self.start = time.time()
        loaded = self.count*self.block
        progress = round(loaded/self.size, 4)
        if loaded >= self.size:
            print u'%s下载完成\r\n'%self.file_name
        else:
            print u'{0}下载进度{1:.2f}{2}/{3:.2f}{4} {5:.2%} 下载速度{6:.2f}{7}/s'.\
                  format(self.file_name, loaded, self.unit,\
                  self.size, self.unit, progress, speed, self.unit)
            print '%50s'%('/'*int((1-progress)*50))
 
 
queue = Queue.Queue()
 
 
def run():
    while True:
        #设置timeout的谜底是为了防止url不可访问，或者相应速度太慢造成的时间浪费
        #你还可以通过这个  就知道最长需要多久可以爬完
        url = queue.get(timeout=100)
        if url is None:
            print u'全下完啦'
            break
        #补习：MD5加密后的值是128bit的，按4位二进制组合成一个十六进制，所以最后出来的十六进制字符串是32个，比如d3379f609e1aa88da2f50018d4fa218f。
        h = hashlib.md5()
        h.update(url)
        name = h.hexdigest()
        path = 'e:/download/' + name + '.mp4'
        download_file(url, path)
 
 
def get_url():
    queue.put(None)
 
 
if __name__ == '__main__':
    get_url()
    for i in xrange(4):
        t = threading.Thread(target=run)
        #守护线程
        #在thread.start()之前设置，否则会跑出一个IllegalThreadStateException异常。你不能把正在运行的常规线程设置为守护线程。 
        #在Daemon线程中产生的新线程也是Daemon的。
        #守护线程应该永远不去访问固有资源，如文件、数据库，因为它会在任何时候甚至在一个操作的中间发生中断。
        t.daemon = True
        t.start()


if __name__ == '__main__':
    url = '就在原帖...'
    path = '想存哪都行'
    download_file(url, path)



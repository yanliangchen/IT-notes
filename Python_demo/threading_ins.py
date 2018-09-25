# encoding: utf-8
__author__ = 'liyanliang'
import time
import threading
def loop():
    """
    新线程执行的代码
    :return:
    """
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

if __name__ == '__main__':
    # 多线程实例 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
    print time.ctime()
    print 'thread %s is running...' % threading.current_thread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name
    print time.ctime()
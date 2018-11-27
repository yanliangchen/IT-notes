#!encoding=utf-8
import  time
# 同步的一个代码
# 一.解决异步(非阻塞)
#  1.可以用多线程
#  2.tornado里面是单进程,单线程

# 线程帮执行
import  threading
def  long_io(callback):
    def fun(cb):
        print('开始执行长延时操作')
        time.sleep(5)
        print('结束执行长延时操作')
        resp = 'Long_IO_RESPONSE'
        cb(resp)
    t = threading.Thread(target=fun,args=(callback,))
    t.start()
# 回调函数
def on_finish(resp):
    print('开始执行回调函数')
    print('长延时操作的结果是：%s' % resp)
    print('结束执行回调函数')

def req_a():
    print('开始处理请求a')
    #longio结束时 回调函数onfinsh
    long_io(on_finish)
    print('离开处理请求a')


def req_b():
    print('开始处理请求b')
    time.sleep(2)
    print('结束处理请求b')

if __name__ == '__main__':
    req_a()
    req_b()
#!encoding=utf-8
import  time
# 同步的一个代码
# 一.解决异步(非阻塞)
#  1.可以用多线程，协程方式
#  2.tornado里面是单进程,单线程
def req_a():
    print('开始处理请求a')
    # 回调函数异步.py实现 : a耗时操作找第三方(线程)去执行了,之后直接处理b 等a耗时完成再来执行a
    time.sleep(5)
    print('结束处理请求a')


def req_b():
    print('开始处理请求b')
    print('结束处理请求b')

if __name__ == '__main__':
    req_a()
    req_b()
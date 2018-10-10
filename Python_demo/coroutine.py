import time
'''
协程（摘自廖雪峰老师）：https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328689835ecd883d910145dfa8227b539725e5ed000
'''

'''
看这个需要先了解生成器方法  
参见收录文章  ： http://codingpy.com/article/python-generator-notes-by-kissg/

在这里体现 ：
generator其实有第2种调用方法(恢复执行)，即通过send(value)方法将value作为yield表达式的当前值，
你可以用该值再对其他变量进行赋值，这一段代码就很好理解了。当我们调用send(value)方法时，
generator正由于yield的缘故被暂停了。
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)



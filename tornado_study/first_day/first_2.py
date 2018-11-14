#!encoding=utf8
import  tornado.web
import  tornado.ioloop
import  tornado.httpserver # 建立tornado   webserver

class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler)
        ]
    )
    # 返回内置的服务器  相当于nginx
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(80)
    '''
    这里补充 : 
        1 .正常tornado服务器上面有启动多进程的写法需要传递参数,这里的数字
    最好是CPU核数的1倍到2倍（不推荐，而且这个在windows上出bug实现不了）
        2 .最好去linux上手动多启动几个进程，之后用nginx去配置负载把哪个请求交给哪个
    进程服务去处理
    '''
    # http_server.start(num_processes= )
    # tornado.ioloop.IOloop创建实例
    # current()获取当前的示例
    # start()方法  循环问epoll 只把可操作socket发过来了  之后到路由映射表
    tornado.ioloop.IOLoop.current().start()


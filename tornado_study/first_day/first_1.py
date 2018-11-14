#!encoding=utf-8
import  tornado.ioloop
import  tornado.web

class IndexHandler(tornado.web.RequestHandler): # Request 是tornado请求处理基类
    def get(self, *args, **kwargs): # 处理get类型请求
        self.write('index ok') # 响应内容

class TornadoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('tornado  ok')
if __name__ == '__main__':
    #建一个APP
    app = tornado.web.Application( # 路由映射表
        [
            (r'/',IndexHandler),
            (r'/tornado',TornadoHandler),

        ],
        debug = True  # 调试模式显示

    ) # p1: handler处理器   p2..pn
    app.listen(80) # app绑定到8080端口
    tornado.ioloop.IOLoop.current().start() # 创建IOLOOP实例，启动监听端口

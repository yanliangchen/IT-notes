# coding:utf-8
import  tornado.web
import  tornado.httpserver
import  tornado.ioloop
import  config
# 数据格式规范
import  json

class  ErrHandler(tornado.web.RequestHandler):
    '''
    待状态码返回之后给出文字提示接口
    '''
    def get(self, *args, **kwargs):
        self.write('ok')
        self.send_error(404,title=u'今天吃什么',content=u'你错了')
        # 再往下写，就报错了.
        # self.write('buxingle')
    def  write_error(self, status_code, **kwargs):
        self.write(str(status_code))
        self.write(kwargs['content'])
        self.write(kwargs['title'])

class  IndexHandler(tornado.web.RequestHandler):
    #通用参数接口(tornado给我们提供的，获取参数)，初始化接口
    #接口调用顺序
    def initialize(self,**info):
        print('is init')
        self.a = info['a']
        self.b = info['b']
    #获取请求头，prepare里面做了
    def prepare(self):
        content_type = self.request.headers.get('User-Agent')# 获取request请求的headers
        print(content_type)
    def  get(self, *args, **kwargs):
        self.write('<br>')
        self.write(str(self.a)+"<br>")
        self.write(str(self.b)+"<br>")

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/error',ErrHandler),
            # 默认传递参数 a =1 b = 2
            (r'/',IndexHandler,dict(a=1,b=2))
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()

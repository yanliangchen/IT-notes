#!encoding=utf8
#目的:传递参数 get请求
import  tornado.web
import  tornado.ioloop
import  tornado.httpserver # 建立tornado   webserver
import  tornado.options
import  config
from  tornado.web import  url

class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index page ok')
class  TornadoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('tornado_page')

class GetHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs): # get接口
        a = self.get_query_argument('a',default=None)# 获取get请求类型  查询参数a的值
        b = self.get_query_argument('b',default=None)# 获取get请求类型  查询参数b的值
        a_list = self.get_arguments('a')
        self.write('get ok')

    def post(self, *args, **kwargs):
        self.get_body_argument('name')



if __name__ == '__main__':
    tornado.options.parse_command_line() # 从命令行接受参数

    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            url(r'/tornado',TornadoHandler,name='tornado'), # 给路由起别名
            url(r'/get',GetHandler,name='get')
        ]
        ,
        #相当于直接传字典了 **args
        **config.settings # app配置项
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()


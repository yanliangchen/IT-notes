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
        self.render('reg.html')

    # post请求接口
    def post(self, *args, **kwargs): # post接口
        #获取查询参数  GET  POST 通用方式获取参数
        a = self.get_argument('a')
        b = self.get_argument('b')
        c = self.get_argument('c')
        print(a,b,c)
        # 获取表单提交的属性信息
        username = self.get_body_argument('username',default=None)
        password   =self.get_body_argument('password',default=None)
        gender = self.get_body_argument('gender',default=None)
        interest =  self.get_body_arguments('interest') # 接受多值

        print(username,password)
        if  username and  password:
            if  username == 'dachui' and  password == '123':
                self.write('登陆成功<br>')
                res = self.write(' '.join(interest))
            else:
                self.write('登陆失败')
        else:
            self.write('用户名，密码不能为空')

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


#!encoding=utf-8
import  tornado.web
import  tornado.ioloop
import  config
import  tornado.httpserver
import  time
class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_cookie('malatid')
        print(a)
        if  a is  None :
            self.set_cookie('malatid','bcd')
            self.write('ok')
        else:
            res = self.get_cookie('malatid')
            self.write(res)

class  ClickCountHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie('count')
        if  count is  None: # 首次登陆
            count ='1'
            self.set_cookie('count','1')
        else: # 以前登陆过，去累加次数
            count = int(count)+1
            count = str(count)
            self.set_cookie('count',count)
        self.write('您第%s次登陆'% count)


class   ClearHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('count')


class  SignHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 设置安全cookie
        self.set_secure_cookie('alice','18')
        #  获取安全cookie
        age = self.get_secure_cookie('alice')
        self.write(age)

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/click',ClickCountHandler),
            (r'/clear',ClearHandler),
            (r'/sign', SignHandler),

        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
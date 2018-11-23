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


        # 设置cookie

        # 获取cookie

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler)
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
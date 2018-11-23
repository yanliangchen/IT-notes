import  tornado.web
import  tornado.ioloop
import  os
from  third_day  import  config
import  tornado.httpserver
from   tornado.web import  StaticFileHandler

def add(price1,price2):
    return  int(price1)+int(price2)

class FuncHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('fuc.html',price = '1000',add=add)


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/func', FuncHandler),
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
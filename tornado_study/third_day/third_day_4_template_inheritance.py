import  tornado.web
import  tornado.ioloop
import  os
import  config
import  tornado.httpserver
from   tornado.web import  StaticFileHandler

class BaseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('reg.html')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/base',BaseHandler),
            # 这个必须得写  否则直接访问静态资源了  因为后面要根来处理这个路 由  指定具体静态资源在什么位置上
            (r'/stc/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir,'static')})
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
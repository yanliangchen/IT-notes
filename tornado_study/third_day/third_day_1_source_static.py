import  tornado.web
import  tornado.ioloop
from  third_day import  config
import  tornado.httpserver
import  os
from   tornado.web import  StaticFileHandler

class   IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index page  ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            # (r'/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir,'static/html')})
            (r'/d/(.*)',StaticFileHandler,{'path':os.path.join(config.Base_dir, 'static/html'), 'default_filename': 'static.html'})
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()

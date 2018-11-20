
import  tornado.web
import  tornado.ioloop
import  config
import  tornado.httpserver
class  IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self): # 执行0
        print('set_default_header')

    def initialize(self): #  执行1
        print('init ok')

    def prepare(self):  # 执行2
        print('prepare ok')

    # get出错，重新执行set_default_headers
    def get(self, *args, **kwargs): # 执行3
        print('get ok')
        self.write('get ok')
        self.send_ error(500)

    # 调用send_error的时候它就被调用了
    def write_error(self, status_code, **kwargs):
        print('write error ok ')

    def on_finish(self):  # 执行4
        print('finish ok')
    # 输出信息 接口调用顺序
    '''
    ERROR:tornado.access:500 GET / (127.0.0.1) 1.00ms
    set_default_header
    init ok
    prepare ok
    get ok
    set_default_header
    write error ok 
    finish ok
    '''
if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
        ]
        ,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
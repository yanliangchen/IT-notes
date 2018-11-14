#!encoding=utf8
# 目的：把端口指定到配置文件
import  tornado.web
import  tornado.ioloop
import  tornado.httpserver # 建立tornado   webserver
import  tornado.options

tornado.options.define('port',8000,type=int) #启动参数
tornado.options.define('subject',[],type=str,multiple=True ) # 启动参数

class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')


if __name__ == '__main__':
    tornado.options.parse_command_line() # 从命令行接受参数
    tornado.options.parse_config_file('config')
    print(tornado.options.options.subject)
    app = tornado.web.Application(
        [
            (r'/',IndexHandler)
        ]
        ,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()

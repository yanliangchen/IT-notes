#!encoding=utf8
# 目的：把配置信息写到config.py 当前代码不需要进行指定
import  tornado.web
import  tornado.ioloop
import  tornado.httpserver # 建立tornado   webserver
import  tornado.options
import  config

class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index page ok')


if __name__ == '__main__':
    tornado.options.parse_command_line() # 从命令行接受参数

    app = tornado.web.Application(
        [
            (r'/',IndexHandler)
        ]
        ,
        #相当于直接传字典了 **args
        **config.settings # app配置项
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()


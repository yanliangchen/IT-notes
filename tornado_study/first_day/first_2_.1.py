#!encoding=utf8
# 目的 : 执行py文件后面根端口号参数，或者是其他参数
import  tornado.web
import  tornado.ioloop
import  tornado.httpserver # 建立tornado   webserver
import  tornado.options

# python  first_2_.1.py  --port=7999   默认8000
tornado.options.define('port',8000,type=int) #启动参数

#multiple允许传多个值之后给封装到列表里
#$ python   first_2_.1.py  --port=8080 --subject=python,tornado,django
tornado.options.define('subject',[],type=str,multiple=True ) # 启动参数
class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')


if __name__ == '__main__':
    tornado.options.parse_command_line() # 从命令行接受参数
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

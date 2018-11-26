#!encoding=utf-8
import  tornado.web
import  tornado.ioloop
import  config
import  tornado.httpserver
import  os
import  torndb
from  tornado.web import StaticFileHandler
class  IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pass

class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/", IndexHandler),
            (r"/add", CityAddHandler),
            (r"/select", SelectHandler),
            # 这里的路由配置数据库图片的路径时候要注意，最好指向都改成一样的,否则出现问题
            (r"/uoloads/(.*)", StaticFileHandler,{'path':os.path.join(config.Base_dir,'uoloads')}),
        ]
        settings = config.settings
        #  https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
        #  如果运行报错，则需要安装按照这个连接 安装mysqlclient
        self.db =torndb.Connection( # 返回数据库操作对象
            host="127.0.0.1",
            database="test",
            user="root",
            password="123456"
        )
        super(Application,self).__init__(handler,**settings)

class CityAddHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        try:
            sql = 'insert   into  class(caption) values("%s")' % "卡鲁"
            #返回res
            res = self.application.db.execute(sql)

        except Exception as e :
            print(str(e))
            res = str(e)
        self.write(str(res))

class  SelectHandler(tornado.web.RequestHandler):
    def  get(self, *args, **kwargs):
        try:
            sql = 'select  * from xi_city'
            rows = self.application.db.query(sql) # [{id:1},title:'云顶山庄',{}]
            self.render('select.html',rows = rows)
        except Exception as e :
            res = e
        self.write('ok')
if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
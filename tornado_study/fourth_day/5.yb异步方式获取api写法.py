#!encoding=utf-8
import  tornado.web
import  tornado.ioloop
import  config
import  tornado.httpserver
from  tornado.web  import  asynchronous
import   tornado.httpclient
import  json
class IndexHandler(tornado.web.RequestHandler):
    @asynchronous
    def get(self, *args, **kwargs):
        ip = self.get_query_argument('ip',None)
        print(ip)
        if  ip  is  not  None:
            client = tornado.httpclient.AsyncHTTPClient() # 建立异步客户端
            client.fetch('http://www.ip138.com/ips138.asp?ip=%s&action=2 '%ip,callback=self.on_response)
        else:
            self.write('输入错误')
    # 回调函数
    def on_response(self,response):
        data = response.body
        data = json.loads(data)
        id = data.get("id")
        subLemmaId = data.get("subLemmaId")
        self.write('%s %s' %(id,subLemmaId))
        vip = self.get_cookie('vip')
        if  vip is not  None:
            self.finish()
        else:
            import  time
            time.sleep(5)
            self.finish()

class IPHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('ip.html')

class VIPHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('vip','super')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/vip',VIPHandler),
            (r'/ip',IPHandler)
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
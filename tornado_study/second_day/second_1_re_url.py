# coding:utf-8
import  tornado.web
import  tornado.httpserver
import  tornado.ioloop
import  config
# 数据格式规范
import  json
class IndexHandler(tornado.web.RequestHandler):
    #通用接口
    # 还可以自定义响应报文
    # 中间如果没看到的话可能出现304（缓存，not modify ）状态码
    def set_default_headers(self): # 全局header
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def get(self,*args,**kwargs):
        stu_info = {
            'name':'你好',
            'age':6,
        }
        # 给回浏览器json格式字符串,响应码为text/html
        self.write(json.dumps(stu_info))
        # 手动指定响应码
        self.set_status(500)
        # 重定向302
        # 400 请求错误 (详细参见那个word)
class  SubjectHandler(tornado.web.RequestHandler):
    # 这两个参数能把写的路由给传递过来
    def get(self,a,b,*args,**kwargs):
        print(a,b)
        # write输出缓冲区   写一次加入一次缓冲区
        self.write('subject  ok')
        self.write('index')

class Err404Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)
        # 第一次给做成文字
        # self.write('这个页面不在这个地球上了')
        # 第二次给 render页面
        self.render('404.html')
if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            # 路由 组1：(.+)匹配任意字符1-n个
            (r'/subject/(.+)/([0-9A-Za-z]+)',SubjectHandler),
            # 自定义404页面
            (r'.*',Err404Handler)
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()

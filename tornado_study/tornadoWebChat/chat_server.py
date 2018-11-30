#coding:utf8
import tornado.web
import tornado.ioloop
import config
import tornado.httpserver
from tornado.websocket import WebSocketHandler
import datetime

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class ChatHandler(WebSocketHandler):
    # 当前台和服务器建立连接时触发
    users = set() #用户列表
    def open(self, *args, **kwargs):
        # 用户添加到用户列表
        self.users.add(self)  # self 就是WebSoketHandler的实例 （self相当于websocket连接）
        for user in self.users:
            ip = self.request.remote_ip # 获取请求来源IP
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = u'[%s]-[%s]-进入洗头城：' % (ip,now)
            user.write_message(message)

    # 当前台有数据发送过来的时候触发
    def on_message(self, message):
        for user in self.users:
            ip = self.request.remote_ip
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.write_message('[%s]-[%s]:%s' % (ip,now,message))

    # 当连接断开的时候触发
    def on_close(self):
        self.users.remove(self) # 从用户列表中删除断开连接的用户
        for user in self.users:
            ip = self.request.remote_ip # 获取请求来源IP
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = u'[%s]-[%s]-离开洗头城：' % (ip,now)
            user.write_message(message)


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/chat',ChatHandler)
        ],
        **config.settings
    )
    chat_server = tornado.httpserver.HTTPServer(app)
    chat_server.listen(config.port,'0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
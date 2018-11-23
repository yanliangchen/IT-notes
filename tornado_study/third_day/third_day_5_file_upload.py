# coding:utf8
# 文件上传
import  tornado.web
import  tornado.ioloop
import  config
import  tornado.httpserver

import   uuid

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('reg.html')

    def post(self, *args, **kwargs):
        image_file = self.request.files.get('avatar')
        print(image_file)
        if  image_file:
            for file  in  image_file:
                fname = str(uuid.uuid4())+'.'+file['filename'].split('.')[-1]
                ftype = file['content_type']
                if  ftype == 'image/jpeg' or  file  == 'image/gif':
                    # 文件上传工作
                    # with  不用关闭文件了
                    with  open('upload/'+fname,'wb') as f :
                        f.write(file['body'])

                else:
                    self.write('文件类型不符合')
        self.write('upload ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/base',IndexHandler),
        ],
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.port)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
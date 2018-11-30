#coding:utf8
import os

Base_dir = os.path.dirname(__file__)

port=8090

settings = {
    'debug' : True,  # 开启调试模式
    'template_path' : os.path.join(Base_dir,'templates'),  # 配置模板路径
    'static_path' : os.path.join(Base_dir,'static'),  # 静态资源路径
    'cookie_secret' : 'Y78vnCf+St2BJrCdoOq076OpYB8pQkoIsIYxDa9VPRM=', # 安全cookie混淆字符串
    'xsrf_cookies' : True
}
#!encoding=utf-8
import   os
# 获取当前文件的整个全的绝对路径  print(os.path.dirname(__file__))
# 上级路径 print(os.path.dirname(os.path.dirname(__file__)))
Base_dir = os.path.dirname(__file__)

port=8080
subject=['python','tornado','django']

settings = {
    'debug':True,
    'template_path': os.path.join(Base_dir,'templates'),# 配置模板路径
    'static_path': os.path.join(Base_dir,'static'),# 静态资源路径
    # cookie安全   安全cookie  混淆字符串
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI='
}


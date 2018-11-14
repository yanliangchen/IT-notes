#!encoding=utf-8
import   os
# 获取当前文件的整个全的绝对路径  print(os.path.dirname(__file__))
# 上级路径 print(os.path.dirname(os.path.dirname(__file__)))
Base_dir = os.path.dirname(__file__)

port=8000
subject=['python','tornado','django']

settings = {
    'debug':True,
    'template_path': os.path.join(Base_dir,'templates')
}


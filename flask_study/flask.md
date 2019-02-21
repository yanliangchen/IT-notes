# Flask 快速后台开发框架

# 1.入门

## 1.1 demo

```

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def  index():
    return  'Hello word2 '

@app.route('/user/<username>')
def  show_user_profile(username):
    return  'User %s'% username

@app.route('/path/<int:post_id>')
def  show_post(post_id):
    return 'Post %d'%post_id

@app.route('/path/<path:subpath>')
def  show_subpath(subpath):
    return 'Subpath %s'% subpath

@app.route('/projects/')
def  projects():
    return 'The project page'

@app.route('/about')
def  about():
    return  'The about page'


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)
```



# 2 . demo  one  文件上传

**入口文件：app.py**

```

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
@app.route('/index')
def  yemian():
    return render_template('upload.html')

@app.route('/chongdingxiang')
def  hanshu():
    return   '重定向成功'
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        print(basepath)
        upload_path = os.path.join(basepath, 'static\\uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        print(upload_path)
        f.save(upload_path)
        #重定向的是函数名
        return redirect(url_for('hanshu'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

```



**upload.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>文件上传示例</h1>
    <form action="/upload" enctype='multipart/form-data' method='POST'>
        <input type="file" name="file">
        <input type="submit" value="上传">
    </form>
</body>
</html>
```



# 3 .demo two 表单post 

```
#表单
from flask import Flask
app = Flask(__name__)
def do_the_login():
    return  '提交成功'
def  show_the_login_form():
    return   '不是post'
@app.route('/index')
def index():
    return  render_template('hello.html')

@app.route('/hello', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('验证函数')
        return do_the_login()
    else:
        print('给到页面')
        return show_the_login_form()

```

**hello.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <form id="login" name="login" method ="post"  action="/hello">

        <p>用户名：<input id="txtUserName" name="txtUserName" type="text" /></p>  <!--用户名文本框-->
        <p>密　码：<input id="txtPWD" name="txtPWD" type="text" /></p>                     <!--密码文本框-->
        <p><input id="subLogin"  name ="subLogin" type="submit" value="提交" /></p><!--提交按钮-->

    </form>
</head>
<body>

</body>
</html>
```

# 4. about  给用户401等页码

```
from flask import Flask,abort

app=Flask(__name__)

@app.route('/index')
def hanshu():
    abort(401)

if __name__ == '__main__':
    app.run(debug=True)
```

# 5. errorhandler 自定义异常

**errorhandler : 抓住所有请求异常，抛自定义页面 ，也可以给json格式**

json 格式

```

from flask import jsonify

from flask import Flask,render_template
app=Flask(__name__)

@app.errorhandler(404)
def error_404(error):
    """这个handler可以catch住所有abort(404)以及找不到对应router的处理请求"""
    response = dict(status=0, message="404 Not Found")
    return jsonify(response)
    
@app.route('/index')
def  index():
    return 'ok'
```



页面格式

```
@app.errorhandler(404)
def error_404(error):
    """这个handler可以catch住所有abort(404)以及找不到对应router的处理请求"""
    return  render_template('page_not_found.html')
```



# 6. cookie 

**设置cookie**

```

from flask import request,Flask,render_template
from flask import make_response
app = Flask(__name__)
import  datetime
@app.route('/set_cookie')
def set_cookie():
    response=make_response('Hello World')
    outdate=datetime.datetime.today() + datetime.timedelta(days=30)
    response.set_cookie('Name','Hyman',outdate)
    return response
```



**获得设置好的cookie**

```

from flask import request,Flask,render_template
from flask import make_response
app = Flask(__name__)

# 获得cookie 通过键
@app.route('/get_cookie')
def get_cookie():
    name=request.cookies.get('Name')
    return name

```



**删除cookie**

```
from flask import request,Flask,render_template
from flask import make_response
app = Flask(__name__)
@app.route('/del_cookie2')
def del_cookie2():
    response=make_response('delete cookie2')
    response.delete_cookie('Name')
    return response
```



**cookie  测试 demo **

```
from flask import request,Flask,render_template
from flask import make_response
app = Flask(__name__)


@app.route('/shezhicookie')
def abc():
    #返回页面设置cookie
    resp = make_response(render_template('page_not_found.html'))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/yanzhengcookie')
def  cookie_get_page():
    if request.cookies.get('username') ==  'the username':
        print(request.cookies.get('username'))
        return '您又cookie  我直接给您的页面'
    else:
        return  '您还没有设置cookie  谢谢! '



@app.route('/del_cookie2')
def del_cookie2():
    response=make_response('delete cookie2')
    response.delete_cookie('username')
    return response
```



# 7. 重定向urlfor 函数所在路由



```

from flask import redirect, url_for
@app.route('/login')
def  login():
    return '您好，您重新定向的login页面,谢谢'
@app.route('/')
def index():
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)

```


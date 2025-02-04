# 导入Flask类

from flask import Flask
from flask import render_template

# Flask类接收一个参数__name__
app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    mstr = 'Hello Tom辅导编程'
    mint = 10
    return render_template('index.html', my_str=mstr, my_int=mint)


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

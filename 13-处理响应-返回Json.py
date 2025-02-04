# 导入Flask类
import json

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify

# Flask类接收一个参数__name__
app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    mstr = 'Hello Tom辅导编程'
    mint = 10
    return render_template('index.html', my_str=mstr, my_int=mint)


@app.route('/demo2')
def demo2():
    return redirect('http://edu.tompeixun.com')


@app.route('/demo3')
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": "tom"
    }
    return jsonify(json_dict)


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

# 导入Flask类

from flask import Flask, make_response, request

# Flask类接收一个参数__name__


app = Flask(__name__)


@app.route('/cookie')
def set_cookie():
    response = make_response('hello world')
    response.set_cookie('username', 'tompeixun', max_age=3600)
    return response


@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('hello world')
    response.delete_cookie('username')
    return response


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

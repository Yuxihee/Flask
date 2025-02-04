# 导入Flask类

from flask import Flask, make_response, request
from flask import session

# Flask类接收一个参数__name__
app = Flask(__name__)
app.config.from_pyfile('setting.py')

@app.route('/set_session')
def set_session():
    session['username'] = 'tompeixun'
    return 'set session ok'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

# 导入Flask类
import json

from flask import Flask

# Flask类接收一个参数__name__
app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})


@app.route('/users/<user_id>')
def user_info(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)


@app.route('/users2/<int:user_id>')
def user_info2(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)


@app.route('/users3/<int(min=1):user_id>')
def user_info3(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

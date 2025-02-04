from flask import Flask


class DefaultConfig(object):
    """默认配置"""
    SECRET_KEY = '123456'


app = Flask(__name__)

app.config.from_object(DefaultConfig)


@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run()
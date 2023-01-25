from flask import Flask
from apis import hello, articles

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here' #Digest認証用にランダムな値を作成する
app.register_blueprint(hello.api)
app.register_blueprint(articles.api)
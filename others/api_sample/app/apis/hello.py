from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPDigestAuth #HTTP"Digest"Auth

api = Blueprint('hello',__name__,url_prefix='/api/hello')

auth = HTTPDigestAuth()

#"id":"パスワード"
id_list = {
    "aws": "password1",
    "ec2": "password2"
}

#入力されたidに該当するパスワードを
#比較のために取得する
@auth.get_password
def get_pw(id):
    if id in id_list:
        return id_list.get(id)
    return None

@api.route('')
@auth.login_required #ここで認証が行われる

def get():
    name = request.args.get('name', 'World')
    return jsonify({'message': 'Hello ' + name + '!'}), 200
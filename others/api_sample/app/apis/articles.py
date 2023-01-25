from flask import Blueprint, jsonify, request
from models import articles
api = Blueprint('article',
                __name__,
                url_prefix='/api/articles')
@api.route('')
def get_all():
    data = articles.get()
    return jsonify(data), 200
@api.route('/<id>')
def get_by_id(id):
    data = articles.get(id)
    if len(data) > 0:
        return jsonify(data), 200
    else:
        return jsonify({'errors': [{'message': 'NOT FOUND'}]}), 404
@api.route('', methods=['POST'])
def post():
    data = articles.post(
        str(request.form['title']),
        str(request.form['link'])
    )
    return jsonify(data), 201
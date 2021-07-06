from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response
from flask import Flask, jsonify, request
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET',''])
def ping_pong():
    return jsonify('pong!')

@app.route('/books',methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'sucesso'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Livro adicionado!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Livro Atualizado!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Livro Deletado!'
    return jsonify(response_object)
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
        else:
            pass
    return False


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'A Arte de E-nganar',
        'author': 'William L. Mitnick',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Tecnicas de Invasão',
        'author': 'Bruno Fraga',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'As Armas da Persuasão',
        'author': 'Robert Cialdini',
        'read': True
    }
]



if __name__ == '__main__':
    app.run()
    
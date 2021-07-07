from book import *

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    Book.delete_book(id)
    response = Response("Livro removido!", status=200, mimetype='application/json')
    return response


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()  # getting data from client
    Book.add_book(request_data["title"], request_data["author"],
                    request_data["read"])
    response = Response("Book added", 201, mimetype='application/json')
    return response

@app.route('/books', methods=['GET'])
def get_books():
    response_object = {'status': 'sucesso'}
    response_object['books'] = Book.get_all_Book()
    return jsonify(response_object)


@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return_value = Book.get_book(id)
    return jsonify(return_value)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    request_data = request.get_json()
    Book.update_book(id, request_data['title'], request_data['author'],  request_data['read'])
    response = Response("Book Updated", status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()
    
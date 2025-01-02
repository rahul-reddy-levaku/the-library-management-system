from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
books = []
members = []

# Helper functions
def locate_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def locate_member(member_id):
    return next((member for member in members if member['id'] == member_id), None)

# Routes for Books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if not data or 'id' not in data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Invalid book data'}), 400

    if locate_book(data['id']):
        return jsonify({'error': 'Book with this ID already exists'}), 400

    books.append(data)
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = locate_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = locate_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.json
    if not data:
        return jsonify({'error': 'Invalid book data'}), 400

    book.update(data)
    return jsonify({'message': 'Book updated successfully'}), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = locate_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    books.remove(book)
    return jsonify({'message': 'Book deleted successfully'}), 200

# Routes for Members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'error': 'Invalid member data'}), 400

    if locate_member(data['id']):
        return jsonify({'error': 'Member with this ID already exists'}), 400

    members.append(data)
    return jsonify({'message': 'Member added successfully'}), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = locate_member(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = locate_member(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    data = request.json
    if not data:
        return jsonify({'error': 'Invalid member data'}), 400

    member.update(data)
    return jsonify({'message': 'Member updated successfully'}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = locate_member(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    members.remove(member)
    return jsonify({'message': 'Member deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

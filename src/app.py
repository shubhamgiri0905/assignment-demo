from flask import Flask, request, jsonify, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookdb"
mongo = PyMongo(app)

# Routes
@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not 'name' in data or not 'img' in data or not 'summary' in data:
        abort(400, description="Missing required fields")

    book_id = mongo.db.books.insert_one(data).inserted_id
    new_book = mongo.db.books.find_one({"_id": book_id})
    return jsonify({'id': str(new_book['_id']), 'name': new_book['name'], 'img': new_book['img'], 'summary': new_book['summary']}), 201

@app.route('/api/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    result = [{'id': str(book['_id']), 'name': book['name'], 'img': book['img'], 'summary': book['summary']} for book in books]
    return jsonify(result), 200

@app.route('/api/books/<id>', methods=['GET'])
def get_book(id):
    book = mongo.db.books.find_one_or_404({"_id": ObjectId(id)})
    return jsonify({'id': str(book['_id']), 'name': book['name'], 'img': book['img'], 'summary': book['summary']}), 200

@app.route('/api/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = mongo.db.books.find_one_or_404({"_id": ObjectId(id)})

    updated_data = {}
    if 'name' in data:
        updated_data['name'] = data['name']
    if 'img' in data:
        updated_data['img'] = data['img']
    if 'summary' in data:
        updated_data['summary'] = data['summary']

    mongo.db.books.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
    updated_book = mongo.db.books.find_one({"_id": ObjectId(id)})
    return jsonify({'id': str(updated_book['_id']), 'name': updated_book['name'], 'img': updated_book['img'], 'summary': updated_book['summary']}), 200

@app.route('/api/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = mongo.db.books.find_one_or_404({"_id": ObjectId(id)})
    mongo.db.books.delete_one({"_id": ObjectId(id)})
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

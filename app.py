from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Dados de exemplo (em uma aplicação real, seria um banco de dados)
users = [
    {'id': 1, 'name': 'João Silva', 'email': 'joao@example.com'},
    {'id': 2, 'name': 'Maria Santos', 'email': 'maria@example.com'}
]

products = [
    {'id': 1, 'name': 'Produto A', 'price': 29.99, 'category': 'Eletrônicos'},
    {'id': 2, 'name': 'Produto B', 'price': 49.99, 'category': 'Livros'}
]

@app.route('/')
def hello_world():
    return '<h1>Hello World from Flask!</h1>'

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'API is running',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users, 'count': len(users)})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products, 'count': len(products)})

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'received': data,
        'timestamp': datetime.utcnow().isoformat(),
        'method': 'POST'
    })

if __name__ == '__main__':
    app.run(debug=True)

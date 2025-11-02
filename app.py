from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World from Flask!</h1>'

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'API is running'})

if __name__ == '__main__':
    app.run(debug=True)

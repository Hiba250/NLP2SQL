from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    q = data.get('question', '')
    return jsonify({'sql': 'SELECT * FROM employees', 'confidence': 0.85, 'engine': 'transformer'})

@app.route('/status')
def status():
    return jsonify({'model_loaded': False})

@app.route('/')
def index():
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
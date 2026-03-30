from flask import Flask, request, jsonify
import os
app = Flask(__name__)
MODEL_PATH = os.environ.get('NL2SQL_MODEL_PATH', 'checkpoints/best_model')
engine = None

@app.route('/status')
def status():
    return jsonify({'engine': 'transformer', 'model_loaded': engine is not None, 'model_path': MODEL_PATH if engine else None})

@app.route('/')
def index():
    return 'NLP2SQL'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    q = data.get('question', '')
    return jsonify({'sql': 'SELECT * FROM employees -- ' + q, 'confidence': 0.85})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
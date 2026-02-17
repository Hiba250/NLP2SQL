from flask import Flask, request, jsonify
app = Flask(__name__)
engine = None

@app.route('/status')
def status():
    return jsonify({'model_loaded': engine is not None, 'engine': 'transformer'})

@app.route('/')
def index():
    return 'NLP2SQL'

@app.route('/generate', methods=['POST'])
def generate():
    return jsonify({'sql': '--placeholder'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
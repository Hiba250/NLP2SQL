from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'NLP2SQL'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question', '')
    return jsonify({'sql': 'SELECT * FROM table -- ' + question})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
app = Flask(__name__)
SCHEMAS = {'employees': {'table': 'employees', 'columns': ['id','name','salary']}, 'products': {'table': 'products', 'columns': ['id','name','price']}}

@app.route('/')
def index():
    return 'NLP2SQL'

@app.route('/generate', methods=['POST'])
def generate():
    return jsonify({'sql': 'SELECT * FROM employees'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
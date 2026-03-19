from flask import Flask, request, jsonify
app = Flask(__name__)
SCHEMAS = {'employees': {'table': 'employees', 'columns': ['id','name','salary']}, 'products': {'table': 'products', 'columns': ['id','name','price']}}

def detect_table(text):
    for k, v in SCHEMAS.items():
        if k in text.lower():
            return v
    return SCHEMAS['employees']

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    q = data.get('question', '')
    hint = data.get('table', None)
    schema = SCHEMAS[hint] if hint and hint in SCHEMAS else detect_table(q)
    return jsonify({'sql': 'SELECT * FROM ' + schema['table'], 'schema': schema})

@app.route('/')
def index():
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
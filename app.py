from flask import Flask, request, jsonify
import os
app = Flask(__name__)
engine = None
MODEL_PATH = os.environ.get('NL2SQL_MODEL_PATH', 'checkpoints/best_model')
try:
    from model.transformer_engine import TransformerNL2SQLEngine
    if os.path.exists(MODEL_PATH):
        engine = TransformerNL2SQLEngine(MODEL_PATH)
except Exception as e:
    print('Engine load failed: ' + str(e))

@app.route('/status')
def status():
    return jsonify({'model_loaded': engine is not None})

@app.route('/')
def index():
    return 'NLP2SQL'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    q = data.get('question', '')
    if engine is None:
        return jsonify({'sql': '-- Model not loaded'})
    res = engine.generate_sql(q, 'employees', ['id','name','salary'])
    return jsonify({'sql': res})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
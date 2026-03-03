from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/examples')
def examples():
    return jsonify([{'question': 'Show all employees in Engineering', 'category': 'Basic'}, {'question': 'Count orders with status Shipped', 'category': 'Count'}, {'question': 'Average salary by department', 'category': 'GroupBy'}])

@app.route('/')
def index():
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
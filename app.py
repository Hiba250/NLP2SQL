from flask import Flask, jsonify
app = Flask(__name__)
SCHEMAS = {'employees': {'table': 'employees', 'columns': ['id','name','age','salary','department']}, 'products': {'table': 'products', 'columns': ['id','name','price','category']}, 'orders': {'table': 'orders', 'columns': ['id','customer_name','product_id','total_amount','status']}, 'students': {'table': 'students', 'columns': ['id','name','age','grade','gpa','major']}}

@app.route('/')
def index():
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True)
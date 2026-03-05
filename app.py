from flask import Flask, jsonify
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('Index page hit')
    return 'NLP2SQL'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
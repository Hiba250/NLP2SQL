"""
NL2SQL - Natural Language to SQL Query Generator
Flask web app powered by a fine-tuned T5 Transformer model.
"""

from flask import Flask, render_template, request, jsonify
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# ─────────────────────────────────────────────
# Sample Database Schema for Demo
# ─────────────────────────────────────────────
SAMPLE_SCHEMAS = {
    "employees": {
        "table": "employees",
        "columns": ["id", "name", "age", "department", "salary", "hire_date", "manager_id", "email", "city"],
        "description": "Employee records"
    },
    "products": {
        "table": "products",
        "columns": ["id", "name", "category", "price", "stock", "rating", "brand", "created_date"],
        "description": "Product catalog"
    },
    "orders": {
        "table": "orders",
        "columns": ["id", "customer_name", "product_id", "quantity", "total_amount", "order_date", "status", "shipping_city"],
        "description": "Customer orders"
    },
    "students": {
        "table": "students",
        "columns": ["id", "name", "age", "grade", "gpa", "major", "enrollment_date", "email"],
        "description": "Student records"
    }
}


def detect_table(text):
    """Detect which table the query refers to."""
    text_lower = text.lower()
    for key, schema in SAMPLE_SCHEMAS.items():
        if key in text_lower or key.rstrip('s') in text_lower:
            return schema
    return SAMPLE_SCHEMAS["employees"]


# ─────────────────────────────────────────────
# Load Transformer Engine
# ─────────────────────────────────────────────
MODEL_PATH = os.environ.get("NL2SQL_MODEL_PATH", "checkpoints/best_model")
engine = None

try:
    if os.path.exists(MODEL_PATH):
        from model.transformer_engine import TransformerNL2SQLEngine
        engine = TransformerNL2SQLEngine(MODEL_PATH)
        logger.info(f"Transformer engine loaded from: {MODEL_PATH}")
    else:
        logger.warning(f"No model found at {MODEL_PATH}. Train a model first:")
        logger.warning(f"  python -m model.train --data_dir data/spider --epochs 5 --batch_size 32")
except ImportError:
    logger.warning("PyTorch/Transformers not installed. Run: pip install -r requirements.txt")
except Exception as e:
    logger.warning(f"Failed to load Transformer engine: {e}")


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────
@app.route('/')
def index():
    return render_template(
        'index.html',
        model_loaded=engine is not None,
    )


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question', '')

    if not question.strip():
        return jsonify({"sql": "", "explanation": "Please enter a question.", "confidence": 0})

    if engine is None:
        return jsonify({
            "sql": "-- Model not loaded",
            "explanation": "No trained model found. Run: <strong>python -m model.train --data_dir data/spider --epochs 5</strong>",
            "confidence": 0,
            "schema": {},
            "engine": "transformer",
        })

    schema = detect_table(question)
    table_hint = data.get('table', None)
    if table_hint and table_hint in SAMPLE_SCHEMAS:
        schema = SAMPLE_SCHEMAS[table_hint]

    result = engine.generate_sql(
        question=question,
        table_name=schema["table"],
        columns=schema["columns"],
    )
    return jsonify(result)


@app.route('/status')
def status():
    return jsonify({
        "engine": "transformer",
        "model_loaded": engine is not None,
        "model_path": MODEL_PATH if engine else None,
    })


@app.route('/examples')
def examples():
    return jsonify([
        {"question": "Show all employees in the Engineering department", "category": "Basic Select"},
        {"question": "How many products are there in each category?", "category": "Aggregation"},
        {"question": "Find employees with salary greater than 80000", "category": "Filtering"},
        {"question": "Show top 5 products by price descending", "category": "Sorting"},
        {"question": "What is the average salary by department?", "category": "Group By"},
        {"question": "Count total orders with status Shipped", "category": "Count"},
        {"question": "Show students with gpa greater than 3.5 in Computer Science major", "category": "Multi-filter"},
        {"question": "Find the maximum price of products in Electronics category", "category": "Max"},
        {"question": "List all orders with total amount above 500 sorted by order date descending", "category": "Complex"},
        {"question": "Show the minimum age of employees by department", "category": "Min + Group"},
    ])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
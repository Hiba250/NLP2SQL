# NL2SQL — Natural Language to SQL Query Generator

> Convert plain English questions into SQL queries using a fine-tuned **T5 Transformer** model trained on the **Spider dataset**.

---

## 📌 Overview

NL2SQL is a deep learning–powered Flask web application that translates natural language questions into valid SQL queries. It uses a fine-tuned sequence-to-sequence T5 model (or CodeT5) and supports multiple real-world database schemas out of the box.

---

## 🚀 Features

- 🧠 **T5 / CodeT5 model** — state-of-the-art text-to-SQL generation
- 🔍 **Multi-table schema detection** — automatically detects which table your question targets
- ⚡ **Beam search decoding** — higher quality SQL output
- 🎯 **Confidence scoring** — each query comes with a confidence estimate
- 📊 **Training graphs** — loss curves, LR schedule, and training summary
- 🧩 **FP16 mixed precision** — faster GPU training
- 🔄 **Dynamic padding** — efficient batching for faster training
- 🌐 **REST API** — `/generate`, `/status`, `/examples` endpoints
- 🖥️ **Modern Web UI** — dark-themed with example query buttons

---

## 🗂️ Project Structure

```
NLP2SQL/
├── app.py                        # Flask web application
├── requirements.txt              # Python dependencies
├── templates/
│   └── index.html                # Web UI (dark theme)
├── model/
│   ├── __init__.py
│   ├── transformer_engine.py     # T5 inference engine
│   ├── data_preprocessor.py      # Spider dataset loader
│   └── train.py                  # Training script
├── checkpoints/                  # Saved models (after training)
│   ├── best_model/
│   ├── final_model/
│   ├── history.json
│   ├── loss_curve.png
│   ├── lr_schedule.png
│   └── training_summary.json
└── data/
    └── spider/                   # Spider dataset files
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hiba250/NLP2SQL.git
cd NLP2SQL
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Dataset — Spider

Download the Spider dataset from [https://yale-lily.github.io/spider](https://yale-lily.github.io/spider) and extract it to `data/spider/`.

**Expected structure:**

```
data/spider/
├── tables.json
├── train_spider.json
└── dev.json
```

---

## 🏋️ Training

### Quick start (CPU-friendly)

```bash
python -m model.train --data_dir data/spider --model t5-small --epochs 5 --batch_size 8
```

### GPU training (recommended)

```bash
python -m model.train --data_dir data/spider --model t5-base --epochs 15 --batch_size 16 --fp16
```

### Best accuracy (code-specialized model)

```bash
python -m model.train --data_dir data/spider --model codeT5-base --epochs 15 --batch_size 8 --fp16
```

### All Training Options

| Argument | Description | Default |
|---|---|---|
| `--data_dir` | Path to Spider folder | *(required)* |
| `--model` | `t5-small` \| `t5-base` \| `codeT5-base` \| `flan-t5-base` | `t5-small` |
| `--epochs` | Number of training epochs | `10` |
| `--batch_size` | Batch size | `16` |
| `--lr` | Learning rate | `3e-4` |
| `--max_input_len` | Max input token length | `192` |
| `--max_target_len` | Max output token length | `96` |
| `--grad_accum` | Gradient accumulation steps | `1` |
| `--eval_every` | Validate every N epochs | `2` |
| `--fp16` | Enable FP16 mixed precision | `False` |
| `--resume` | Resume from checkpoint path | `None` |
| `--checkpoint_dir` | Output directory for models | `checkpoints` |

### Speed Tips

| Setting | Faster ⚡ | Slower but Better 🎯 |
|---|---|---|
| `--model` | `t5-small` (60M params) | `codeT5-base` (220M params) |
| `--batch_size` | `32` or `64` | `8` |
| `--max_input_len` | `128` | `512` |
| `--epochs` | `5` | `15` |

---

## 🖥️ Running the Web App

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

You can also specify a custom model path:

```bash
NL2SQL_MODEL_PATH=checkpoints/best_model python app.py
```

---

## 🔌 REST API

### `POST /generate`

Convert a natural language question to SQL.

**Request:**
```json
{
  "question": "Show all employees in the Engineering department",
  "table": "employees"
}
```

**Response:**
```json
{
  "sql": "SELECT * FROM employees WHERE department = 'Engineering'",
  "confidence": 0.92,
  "engine": "transformer",
  "schema": { "table": "employees", "columns": ["id", "name", "department", "salary"] }
}
```

---

### `GET /status`

Check if the model is loaded.

```json
{
  "engine": "transformer",
  "model_loaded": true,
  "model_path": "checkpoints/best_model"
}
```

---

### `GET /examples`

Get a list of example queries.

```json
[
  { "question": "Show all employees in the Engineering department", "category": "Basic Select" },
  { "question": "How many products are there in each category?",    "category": "Aggregation" },
  { "question": "Find employees with salary greater than 80000",    "category": "Filtering" }
]
```

---

## 🗄️ Supported Schemas

| Table | Columns |
|---|---|
| `employees` | id, name, age, department, salary, hire_date, manager_id, email, city |
| `products` | id, name, category, price, stock, rating, brand, created_date |
| `orders` | id, customer_name, product_id, quantity, total_amount, order_date, status, shipping_city |
| `students` | id, name, age, grade, gpa, major, enrollment_date, email |

---

## 📈 Training Outputs

After training, `checkpoints/` will contain:

| File | Description |
|---|---|
| `best_model/` | Model weights with lowest validation loss |
| `final_model/` | Model weights after last epoch |
| `history.json` | Per-epoch train & val loss |
| `loss_curve.png` | Train vs. validation loss curve |
| `lr_schedule.png` | Learning rate warmup + decay graph |
| `training_summary.json` | Total time, best loss, hyperparameters |

---

## 🛠️ Tech Stack

- **Model:** HuggingFace Transformers (T5 / CodeT5)
- **Backend:** Flask (Python)
- **Training:** PyTorch + mixed precision (FP16)
- **Dataset:** Spider (Yale NLP Group)
- **Frontend:** Vanilla HTML/CSS/JS (dark theme)

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Spider Dataset — Yale NLP](https://yale-lily.github.io/spider)
- [HuggingFace Transformers](https://huggingface.co/transformers)
- [Salesforce CodeT5](https://github.com/salesforce/CodeT5)
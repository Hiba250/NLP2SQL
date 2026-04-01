# NL2SQL - Text-to-SQL with Spider + T5

v1.0 - Production-ready Flask web app that converts natural language to SQL using a fine-tuned T5 Transformer trained on the Spider dataset.

## Quick Start

  pip install -r requirements.txt
  python -m model.train --data_dir data/spider --model t5-small --epochs 5
  python app.py

Open http://localhost:5000

## Features
- T5 / CodeT5 model support
- Beam search decoding
- FP16 mixed precision training
- Dynamic padding for fast batching
- Loss and LR curve graphs
- Multi-table schema detection
- REST API: /generate /status /examples
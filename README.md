# NL2SQL - Text-to-SQL with Spider + T5

## Setup

pip install -r requirements.txt

## Train

python -m model.train --data_dir data/spider --model t5-small --epochs 5

## Speed Tips
- Use t5-small for fastest training
- Increase --batch_size for GPU
- Use --fp16 for mixed precision

## Run

python app.py
Open http://localhost:5000
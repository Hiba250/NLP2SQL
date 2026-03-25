# NL2SQL — Text-to-SQL with Spider + T5

Flask web app that converts natural language to SQL queries using a fine-tuned T5 Transformer model trained on the Spider dataset.

## Setup

```bash
pip install -r requirements.txt
```

## Train on Spider

Download Spider dataset from https://yale-lily.github.io/spider and extract to `data/spider/`.

Expected structure:
```
data/spider/
├── tables.json
├── train_spider.json
└── dev.json
```

### Training Commands

```bash
# Fast training (t5-small)
python -m model.train --data_dir data/spider --model t5-small --epochs 5 --batch_size 32

# Standard training (t5-base, better accuracy)
python -m model.train --data_dir data/spider --model t5-base --epochs 15 --batch_size 16

# Best accuracy (codeT5-base, code-specialized)
python -m model.train --data_dir data/spider --model codeT5-base --epochs 15 --batch_size 8
```

### Speed Tips

| Setting | Faster | Slower but better |
|---|---|---|
| `--model` | `t5-small` (60M) | `codeT5-base` (220M) |
| `--batch_size` | `32` or `64` | `8` |
| `--max_input_len` | `192` (default) | `512` |
| `--max_target_len` | `96` (default) | `256` |
| `--eval_every` | `5` | `1` |
| `--epochs` | `5` | `15` |

**Automatic speed optimizations:**
- Pre-tokenizes all data once before training
- Dynamic padding (pads to longest in batch, not global max)
- Validation uses loss only (no slow autoregressive decoding)
- TF32 on Ampere GPUs, FP16 mixed precision on CUDA
- `torch.compile` on Linux (skipped on Windows)

**On CPU:** Use `t5-small` with `--batch_size 8 --epochs 5 --max_input_len 128 --max_target_len 64`

### All Training Options

```
--data_dir       Path to Spider folder (required)
--model          t5-small | t5-base | codeT5-base | codeT5-large | flan-t5-base
--resume         Resume from checkpoint path
--epochs         Number of epochs (default: 10)
--batch_size     Batch size (default: 16)
--lr             Learning rate (default: 3e-4)
--max_input_len  Max input tokens (default: 192)
--max_target_len Max output tokens (default: 96)
--grad_accum     Gradient accumulation steps (default: 1)
--eval_every     Validate every N epochs (default: 2)
--checkpoint_dir Output directory (default: checkpoints)
```

### Training Outputs

After training, `checkpoints/` will contain:
- `best_model/` — Model with lowest validation loss
- `final_model/` — Model after last epoch
- `history.json` — Training metrics
- `loss_curve.png` — Train vs Val loss per epoch
- `step_loss.png` — Step-level loss (smoothed)
- `lr_schedule.png` — Learning rate warmup + decay
- `training_summary.png` — Time per epoch + summary card

## Run the Web App

```bash
# Start (loads model from checkpoints/best_model)
python app.py

# Or specify model path
NL2SQL_MODEL_PATH=checkpoints/best_model python app.py
```

Open http://localhost:5000

## Project Structure

```
├── app.py                       # Flask app (Transformer only)
├── templates/index.html         # Web UI
├── model/
│   ├── data_preprocessor.py     # Spider dataset loader
│   ├── transformer_engine.py    # T5 inference engine
│   └── train.py                 # Training script + graph generation
├── requirements.txt
└── checkpoints/                 # Saved models (after training)
```
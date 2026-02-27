import argparse, os

def save_best(model, path):
    os.makedirs(path, exist_ok=True)
    if hasattr(model, 'save_pretrained'):
        model.save_pretrained(path)
    print('Saved best model to ' + path)

def train(args):
    print('Training with checkpointing')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--checkpoint_dir', default='checkpoints')
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    train(args)
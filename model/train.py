import argparse, os, json

def save_history(history, path):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, 'history.json'), 'w') as f:
        json.dump(history, f, indent=2)
    print('Saved history.json')

def train(args):
    history = {'train_loss': [], 'val_loss': []}
    save_history(history, args.checkpoint_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--checkpoint_dir', default='checkpoints')
    args = parser.parse_args()
    train(args)
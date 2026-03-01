import argparse, os, json

def plot_loss(history, out_dir):
    try:
        import matplotlib.pyplot as plt
        plt.plot(history['train_loss'], label='Train')
        plt.plot(history['val_loss'], label='Val')
        plt.legend()
        plt.savefig(os.path.join(out_dir, 'loss_curve.png'))
        plt.close()
    except ImportError:
        pass

def train(args):
    history = {'train_loss': [0.8, 0.6, 0.4], 'val_loss': [0.9, 0.7, 0.5]}
    plot_loss(history, args.checkpoint_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--checkpoint_dir', default='checkpoints')
    args = parser.parse_args()
    train(args)
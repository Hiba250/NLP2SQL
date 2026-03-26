import argparse, os

def plot_lr(lr_history, out_dir):
    try:
        import matplotlib.pyplot as plt
        plt.plot(lr_history, label='LR')
        plt.xlabel('Step')
        plt.ylabel('LR')
        plt.legend()
        plt.savefig(os.path.join(out_dir, 'lr_schedule.png'))
        plt.close()
    except ImportError:
        pass

def train(args):
    lr_steps = [3e-4 * (i / 10) for i in range(10)]
    plot_lr(lr_steps, args.checkpoint_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--checkpoint_dir', default='checkpoints')
    args = parser.parse_args()
    train(args)
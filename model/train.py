import argparse

def train(args):
    print('grad_accum=' + str(args.grad_accum))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--grad_accum', type=int, default=1)
    args = parser.parse_args()
    train(args)
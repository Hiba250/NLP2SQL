import argparse

def train(args):
    print('bs=' + str(args.batch_size) + ' lr=' + str(args.lr))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--model', default='t5-small')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=3e-4)
    args = parser.parse_args()
    train(args)
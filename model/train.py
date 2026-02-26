import argparse

def train(args):
    if args.fp16:
        print('FP16 enabled')
    print('LR=' + str(args.lr))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--fp16', action='store_true')
    args = parser.parse_args()
    train(args)
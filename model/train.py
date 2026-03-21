import argparse

def train(args):
    start_epoch = 0
    if args.resume:
        print('Resuming from ' + args.resume)
        start_epoch = 3
    for epoch in range(start_epoch, args.epochs):
        print('Epoch ' + str(epoch))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--resume', default=None)
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    train(args)
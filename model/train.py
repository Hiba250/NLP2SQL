import argparse

def train(args):
    for epoch in range(args.epochs):
        if epoch % args.eval_every == 0:
            print('Eval at epoch ' + str(epoch))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--eval_every', type=int, default=2)
    args = parser.parse_args()
    train(args)
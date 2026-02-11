import argparse

def train(args):
    print('Training...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', required=True)
    parser.add_argument('--model', default='t5-small')
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    train(args)
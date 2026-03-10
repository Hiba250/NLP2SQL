import argparse

def train(args):
    print('max_input=' + str(args.max_input_len) + ' max_target=' + str(args.max_target_len))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--max_input_len', type=int, default=192)
    parser.add_argument('--max_target_len', type=int, default=96)
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    train(args)
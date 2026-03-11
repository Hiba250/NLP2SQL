import argparse

class DynamicPadCollator:
    def __init__(self, tokenizer):
        self.tok = tokenizer
    def __call__(self, batch):
        return self.tok.pad(batch, padding=True, return_tensors='pt')

def train(args):
    print('Dynamic padding collator ready')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    args = parser.parse_args()
    train(args)
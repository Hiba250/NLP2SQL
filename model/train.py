import argparse

def get_scheduler(optimizer, warmup_steps, total_steps):
    from transformers import get_cosine_schedule_with_warmup
    return get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)

def train(args):
    print('Scheduler: cosine with warmup')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--lr', type=float, default=3e-4)
    args = parser.parse_args()
    train(args)
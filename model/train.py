import argparse

def train(args):
    step_losses = []
    for step in range(100):
        loss = 1.0 / (step + 1)
        if step % 10 == 0:
            print('Step ' + str(step) + ': loss=' + str(round(loss, 4)))
        step_losses.append(loss)
    print('Done training')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir')
    args = parser.parse_args()
    train(args)
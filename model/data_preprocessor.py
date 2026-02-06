import json

def load_spider(data_dir):
    with open(f'{data_dir}/train_spider.json') as f:
        return json.load(f)
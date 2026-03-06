import json, os

def load_tables(data_dir):
    with open(os.path.join(data_dir, 'tables.json')) as f:
        return json.load(f)

def load_spider(data_dir):
    tables = load_tables(data_dir)
    with open(os.path.join(data_dir, 'train_spider.json')) as f:
        train = json.load(f)
    return train, tables
from transformers import T5ForConditionalGeneration, T5Tokenizer

class TransformerNL2SQLEngine:
    def __init__(self, model_path):
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
        self.model.eval()

    def generate_sql(self, question, table_name, columns):
        schema = 'Table: ' + table_name + ' | Cols: ' + ', '.join(columns)
        inp = 'translate English to SQL: ' + question + ' ' + schema
        ids = self.tokenizer(inp, return_tensors='pt').input_ids
        out = self.model.generate(ids, max_new_tokens=96)
        return self.tokenizer.decode(out[0], skip_special_tokens=True)
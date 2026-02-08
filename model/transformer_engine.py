from transformers import T5ForConditionalGeneration, T5Tokenizer

class TransformerNL2SQLEngine:
    def __init__(self, model_path):
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
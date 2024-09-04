from transformers import AutoTokenizer

def get_tokenizer(id):
    tokenizer = AutoTokenizer.from_pretrained(id)
    return tokenizer
def get_tokenization(tokenizer, text):
    ids=tokenizer.encode(text)
    string_tokens = tokenizer.convert_ids_to_tokens(ids)
    return string_tokens
def get_vocab_size(tokenizer):
    return len(tokenizer.get_vocab())
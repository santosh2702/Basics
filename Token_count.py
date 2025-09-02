from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "Machine learning is powerful."
tokens = tokenizer.tokenize(text)
print(len(tokens))

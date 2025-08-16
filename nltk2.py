def filter_short_words(text, min_length=3):
    words = text.split()
    return [word for word in words if len(word) >= min_length]
    
text ="AI is cool and fun"
print(filter_short_words(text))


import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
text = "I love playing football."
tokens = word_tokenize(text)
print(tokens)

# ['I', 'love', 'playing', 'football']


import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Hello there! How are you? I'm learning NLP."
print(sent_tokenize(text))
print(word_tokenize(text))

['Hello there!', 'How are you?', "I'm learning NLP."]
['Hello', 'there', '!', 'How', 'are', 'you', '?', 'I' ''m', 'learning', 'NLP', '.']



import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "The cats are running faster than the dogs."

tokens = word_tokenize(text)

filtered = [w for w in tokens if w.lower() not in stopwords.words("english")]

ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered]

Print("Original:", tokens)
print("After stopwords:", filtered)
print("After stemming:", stemmed)






















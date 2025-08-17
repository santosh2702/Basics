sent_tokenize	-> ‘I am in pain'
word_tokenize		-> ‘I’, ‘am’,  ‘in’ , ’pain’

nltk.corpus.stopwords      -> remove —-> and, is , the

Stemming - reduces the word from -> running to run (to the root) PorterStemmer, SnowballStemmer
Lemmatization -> (smarter reduction based on grammar) -> WordNetLemmatizer
Case normalisation (lowercasing text) 
Removing punctuation / special characters
Linguistic Analysis——-
POS ->  nltk.pos_tag	(identifies nouns, verbs, adjectives, etc.)
Named Entity Recognition (NER) -> extract people, places, organizations.
Chunking/Chinking -> grouping words into meaningful phrases
Syntax trees -> parsing sentences into grammar trees

Corpora & Lexical Resources———
WordNet -> synonyms, antonyms, hypernyms
Stopwords lists for multiple languages.

Text classification————
Building classifiers for:
Spam detection (spam/ham emails)
Sentiment analysis (position/negative reviews)
Topic classification (sports, politics, tech)
Algorithms ————
Naive Bayes (nltk.NaiveBayesClassifier)
Decision trees
Custom features extractors (e.g.., bag-of-words, TF-IDF)

Information Extraction
Concordance
Collections
Frequency distribution
N-grams

From nltk.stem import PorterStemmer, WordNetLemmatizer
Ps = PorterStemmer()
print(ps.stem(“running”))
Lemmatise = wordNetLemmatizer()
print(lemmatise.lemmatize(running, post=“v”))

POS Tagging——-
From nltk import pos_tag
Tokens = word_tokenize(“I am learning NLP using NLTK”)
print(pos_tag(tokens))
#	[(‘I’, ‘PRP’),  (‘am’, ‘VBP’),  (‘learning’, ‘VBG’), ……]

From nltk import ne_chunk
Nltk.download(‘maxent_ne_chunker’);
nltk.download(‘words’)
sentence = “Barack obama was the 44th President of the United States.”
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)
tree = ne_chunk(tags)
Print(tree)

From nltk.probability import FreqDist
words = word_tokenize(“cat dog cat fish dog cat”)
fdist = FreqDist(words)
print(fdist.most _common(2))
fdist.plot(5)

From nltk.corpus import wordnet
Syns = wordnet.synsets(“good”)
print(syns[0].definition())
print(syns[0].examples())

For lemma in syns[0].lemmas();
print(“Synonym:”, lemma.name())
If lemma.antonyms():
print(“Antonym:”, lemma.anonyms()[0].name())

From nltk.classify import NaiveBayesClassifier
Train = [({‘word’: ‘good}, ‘pos’),
	({‘word’: ‘bad’}, ‘neg’)]
Classifier = NavieBayesClassifier.train(train)
print(classifier.classify({‘word’: ‘good’}))






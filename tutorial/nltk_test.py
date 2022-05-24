import nltk
from nltk.stem.porter import *

sent = "McDonald's became the symbol of glasnost in action 30 years ago when it opened its first restaurant in Moscow. But after temporarily shutting down more than 800 restaurants following the invasion of Ukraine, McDonald's has decided to leave Russia altogether."
#print(sent)

words = nltk.word_tokenize(sent)
#print(words)

tags = nltk.pos_tag(words)
print(tags)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in words]
#print(' '.join(stemmed))

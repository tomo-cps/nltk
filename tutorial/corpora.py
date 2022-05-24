#from nltk.book import *
#from nltk.corpus import brown

#a = brown.categories()
#print(a)
#output
#['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

#reviews_words = brown.words(categories = 'reviews')
#print(reviews_words)
#output
#['It', 'is', 'not', 'news', 'that', 'Nathan', ...]

#b= len(reviews_words)
#print(b)


from nltk.corpus import twitter_samples
a = twitter_samples.fileids()
print(a)

text = twitter_samples.strings(
    'tweets.20150430-223406.json')

b = len(text)
print(b)

c = text[:3]
print(c)

d = twitter_samples.tokenized('tweets.20150430-223406.json')[0]
print(d)


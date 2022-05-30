import nltk
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter


def get_wordnet_pos(tag):
#    if tag.startswith('J'):
#        return wordnet.ADJ
#    elif tag.startswith('V'):
#        return wordnet.VERB
    if tag.startswith('N'):
        return wordnet.NOUN
#    elif tag.startswith('R'):
#        return wordnet.ADV
    else:
        return None

lines = pd.read_csv('/Users/okawatomoaki/Documents/nltk/output.csv')

#print(lines)
counts=[]
#print(lines["name"])

#print(lines[["name","comment"])

#print(lines.shape)
#for line in lines['comment'].tolist():

for line in lines['comment']:
    tokens = word_tokenize(line)
    tagged_sent = pos_tag(tokens)
    wordnet_pos_nn=[ (x,y)  for (x,y) in tagged_sent if y in ('NN')]
               
    wnl = WordNetLemmatizer()
    lemmas_sent = [] 
    for tag in wordnet_pos_nn:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lem = wnl.lemmatize(tag[0],pos=wordnet_pos)
        lemmas_sent.append(lem)
    counts.append(dict(Counter(lemmas_sent)))
#print(counts)
#print(1111111111111111111111111111111111)
#print(len(counts[0]))



for d in counts:
    x = list(range(1,len(d)+1))
    print(x)
    plt.bar(x, d.values(), tick_label=list(d.keys()))
    plt.show()


'''
a = counts[0].items()
a = sorted(a)
x, y =zip(*a)

plt.plot(x, y)
plt.show()
'''






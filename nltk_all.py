import nltk
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import collections

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

#fig = plt.figure(figsize = (10,30))
lines = pd.read_csv('/Users/okawatomoaki/Documents/nltk/scrapy_data.csv')

for n,i in enumerate(range(0,61,20)):
    lines_split = lines[i:i+20]
    counts_i = []
    lemmas_sent_i = []
    for line in lines_split['comment'].tolist():
        tokens = word_tokenize(line)
        tagged_sent = pos_tag(tokens)
        
        wordnet_pos_nn = [(x,y) for (x,y) in tagged_sent if y in ('NN')]
        wnl = WordNetLemmatizer()
        for tag in wordnet_pos_nn:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
            #print(wordnet_pos)
            lem = wnl.lemmatize(tag[0],pos=wordnet_pos)
            lemmas_sent_i.append(lem)
    counts_i.append(Counter(lemmas_sent_i))
    counts_limited_i = counts_i[0].most_common(5)
    c = dict(counts_limited_i)
    x = list(range(1,len(counts_limited_i)+1))
    plt.subplot(4,2,n+1)
    plt.bar(x, c.values(), tick_label=list(c.keys()))
plt.show()



'''
        for n in counts_i:
            All_i += n
            x = list(range(1,len(All_i)+1))
            plt.bar(x, All_i.values(), tick_label=list(All_i.keys()))
            plt.show()
''' 
'''
a = counts[0].items()
a = sorted(a)
x, y =zip(*a)

plt.plot(x, y)
plt.show()
'''

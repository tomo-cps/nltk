import nltk
import csv

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

filename = '/Users/okawatomoaki/Documents/nltk/nltk.csv'
with open(filename,'r',encoding = 'utf-8') as f:
    lines = f.readlines()
    counts=[]
    
    for line in lines:
        tokens = word_tokenize(line)
        
        tagged_sent = pos_tag(tokens)

        wnl = WordNetLemmatizer()
        lemmas_sent = []
        for tag in tagged_sent:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
            lem = wnl.lemmatize(tag[0], pos=wordnet_pos)
            lemmas_sent.append(lem)
        counts.append(dict(Counter(lemmas_sent)))
        print(lemmas_sent)
print(counts)
                  
    












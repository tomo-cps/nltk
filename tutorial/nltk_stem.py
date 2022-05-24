import nltk
import csv

from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *

stemmer = PorterStemmer()
for word in ['does\'nt','going','does','done','went','big','giant','better','rocks','corpo\
ra','Japanese','Japan','fortunately']:
    b = [stemer.stem(word) for 
    print(b)

filename = '/Users/okawatomoaki/Documents/nltk/nltk.csv'
with open(filename,'r',encoding = 'utf-8') as f_list:
    for f_line in f_list:
        word_token = word_tokenize(f_line)
       # print(word_token)                        

import os
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import string
import re
from collections import Counter
import json
import nltk
import pandas as pd

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag, map_tag

from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import math


def createTokens(content):
    content=content.decode('utf-8','ignore').lower()
    tok=wordpunct_tokenize(content)
    tok.sort()
    tokens=[]
    for word in tok:
        word=word.encode('utf-8','ignore')
        if word not in stop:
            if re.match('[a-z]{2}',word ):
                word = unicode(word, 'utf-8')
                tokens.append(word)
                #print word#.encode('utf-8','ignore')#.encode('cp850','replace').decode('cp850')
    return tokens


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('ADJ'):
        return 'a'
    elif treebank_tag.startswith('V'):
        return 'v'
    elif treebank_tag.startswith('NO'):
        return 'n'
    elif treebank_tag.startswith('ADV'):
        return 'r'
    else:
        return ''


def lem(tokens):
    posTagged=nltk.pos_tag(tokens);
    lmtzr=WordNetLemmatizer()
    array=[]
    simplified = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
    for i in simplified:
        if (get_wordnet_pos(i[1])):
            array.append(lmtzr.lemmatize(i[0],pos=(get_wordnet_pos(i[1]))))
        else:
            array.append(i[0])
    #print(array)
    return array

def createVocabulary(content):
    #tokenize
    tokens=createTokens(content)
    #print "Tokens Created"

    tokens=lem(tokens)
    return tokens
   
   


#setting stop words
stop=set(stopwords.words('english'))

#opening file
d=pd.read_csv('SampleForNaive.csv')
Id = list(d.id.unique())
data = d['data'].tolist()
category = d['class'].tolist()
vocabulary=[]
for content in data:
    newTokens=createVocabulary(content)
    for word in newTokens:
        if word not in vocabulary:
            if len(word) > 3:
                if "xxx" not in word:
                    word = word.encode("utf-8")
                    vocabulary.append(word)
#print Id
#print vocabulary









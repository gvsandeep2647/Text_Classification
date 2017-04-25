import pandas as pd
from vocabcreater import vocabulary
from math import log,sqrt
from nltk.tokenize import wordpunct_tokenize

ultradata = []
ultraCategories = []
tf_data = {}
idf_data = {}

def make_unique(l):
	'''
		Making the list a set to eliminate all the duplicates and then converting it back to list
	'''
	l = set(l)
	l = list(l)
	return l

def index1(l,d,k):
	'''
		Creates an inverted index.
		It basically returns a dictionary with each key as a word
		Each key then has a value as a dictionary with doc id as key and a list of positional occurences as value
	'''
	occurences = {}
	for word in l:
		d = {}
		for i in xrange(len(data)):
			temp2 = wordpunct_tokenize(data[i])
			#print temp2
			count = 0
			for word2 in temp2:
				if word2 == word:
					count = count + 1
			#print temp
			if count:
				d[i] = count 
		if d:
			occurences[word] = d
	#print occurences
	return occurences

def calc_tf_idf(tf,idf,org,N):
	for key,val in org.iteritems():
		raw_tf = {}
		
		if len(val.keys()) > 0:
			idf[key] = (log((float(N)/len(val.keys())),10))
		else:
			idf[key] = 0.0
		for doc_key,doc_val in val.iteritems():
			if doc_val>0:
				raw_tf[doc_key] = 1 + log(doc_val,10)
			else:
				raw_tf[doc_key] = 0
		tf[key] = raw_tf
	#print tf

def normalize_doc():
	for i in xrange(len(data)):
		temp =[]
		temp2 = wordpunct_tokenize(data[i])
		l=0.0
		for word in temp2:
			if word not in temp:
				temp.append(word)
		
		for word in temp:
			if word in tf_data:
				if i in tf_data[word]:
					l = l + pow(tf_data[word][i],2)
			
		l = sqrt(l)
		for word in temp:
			if word in tf_data:
				if i in tf_data[word]:
					tf_data[word][i] /= l
			

ultralist = pd.read_csv('SampleForNaive.csv')
vocablength=len(vocabulary) #no. of words in vocabulary
Id = list(ultralist.id.unique())
data = ultralist['data'].tolist()
category = ultralist['class'].tolist()

ultradata = vocabulary

dictdata = {}
dictdata = index1(ultradata,dictdata,1)

ultraCategories = make_unique(ultraCategories)
calc_tf_idf(tf_data,idf_data,dictdata,len(data))
normalize_doc()
print tf_data


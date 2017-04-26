import pandas as pd
from vocabcreater import vocabulary,vocabularyfortest
from math import log,sqrt
from nltk.tokenize import wordpunct_tokenize

ultradata = []
ultraCategories = []
tf_data = {}
idf_data = {}
tf_idf_data = {}

def make_unique(l):
	'''
		Making the list a set to eliminate all the duplicates and then converting it back to list
	'''
	l = set(l)
	l = list(l)
	return l

def index1(l,d,data,k):
	'''
		Creates an inverted index.
		It basically returns a dictionary with each key as a word
		Each key then has a value as a dictionary with doc id as key and a list of positional occurences as value
	'''
	occurences = {}
	for word in l:
		d = {}
		for i in range(1,len(data)):
			temp2 = wordpunct_tokenize(data[i])
			#print temp2
			count = 0
			for word2 in temp2:
				if word2 == word:
					#print word
					count = count + 1
			#print temp
			if count:
				d[category[i]] = count 
		if d:
			occurences[word] = d
	
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
				
		
			
		tf[key] = sum(raw_tf.values())
			
			
	

def normalize_doc(data):
	for i in range(1,len(data)):
		temp =[]
		temp2 = wordpunct_tokenize(data[i])
		l=0.0
		for word in temp2:
			if word not in temp:
				temp.append(word)
		
		for word in temp:
			if word in tf_data:
				l = l + pow(tf_data[word],2)
			
		l = sqrt(l)
		for word in temp:
			if word in tf_data:
				tf_data[word] /= l
		'''
			tf-idf score
		'''
		for key in tf_data.keys():
			tf_idf_data[key] = tf_data[key] * idf_data[key]
	
			

ultralist = pd.read_csv('SampleForNaive.csv')
vocablength=len(vocabulary) #no. of words in vocabulary
Id = list(ultralist.id.unique())
data = ultralist['data'].tolist()
category = ultralist['class'].tolist()

ultradata = vocabulary

dictdata = {}
dictdata = index1(ultradata,dictdata,data,1)
#print dictdata
calc_tf_idf(tf_data,idf_data,dictdata,len(data))

normalize_doc(data)
#print data[0]

'''
	associate terms in data with tfidf scores
'''
docvector = {}
for i in xrange(len(data)):
	temp = wordpunct_tokenize(data[i])
	docvector[i] = {}
	docvector[i]['class it belongs to'] = category[i]
	for word in temp:
		if word in tf_idf_data:
			docvector[i][word] = tf_idf_data[word]
#print docvector
'''
	for test file
	
'''
test_tf = {}
test_idf = {}

testlist = pd.read_csv('test.csv')
data1 = testlist['data'].tolist()
category = testlist['category'].tolist()

testdata = {}

#testdata = index1(vocabularyfortest,testdata,data1,1)
#print testdata
'''
	k = 3
'''

for i in xrange(len(data1)):
	temp = wordpunct_tokenize(data1[i])
	#score = 0.0
	temp = make_unique(temp)
	closest_doc = {'score':0.0 , 'docno':0}
	
	for key,val in docvector.iteritems():
		score = 0.0
		for doc_key,doc_val in val.iteritems():
			for words in temp:
				if doc_key == words:
					score += doc_val
		if score > closest_doc['score']:
			#print score
			closest_doc['score'] = score
			closest_doc['docno'] = key
	print "doc " + str(i) + " classified as " + str(docvector[closest_doc['docno']]['class it belongs to'])
			
			
	






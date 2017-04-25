import pandas as pd
from vocabcreater import vocabulary

ultradata = []
ultraCategories = []

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
		for i in xrange(len(ultralist)):
			temp = [j for j,val in enumerate(data[i][k]) if val==word]
			if temp :
				d[i] = temp
		occurences[word] = d
	
	return occurences


ultralist = pd.read_csv('SampleForNaive.csv')
vocablength=len(vocabulary) #no. of words in vocabulary
Id = list(ultralist.id.unique())
data = ultralist['data'].tolist()
category = ultralist['class'].tolist()
#print data[0]
#print category
#print category
ultradata = make_unique(vocabulary)
dictdata = {}
dictdata = index1(ultradata,dictdata,1)
print dictdata
ultraCategories = make_unique(ultraCategories)
#print vocabulary


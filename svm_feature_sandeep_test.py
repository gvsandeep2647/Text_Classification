import sys
import re
import time
import operator
import numpy as np
from utility_functions import *
from stemming import *
from scipy import sparse
from nltk.corpus import stopwords 
from collections import Counter
from math import log, pow, sqrt
import numpy as np
from sklearn import svm
from sklearn.svm import SVC
import progressbar
from sklearn.decomposition import TruncatedSVD
from keras.models import Sequential
from keras.layers import Dense

PS = PorterStemmer()
DATA_FILE = sys.argv[1]

PRETFIDF = {}
VOCABULARY = {}
MATRIX = []
CATEGORY = []
SUBCATEGORY = []
line_num = 0


def genMatrix(data):
	
	global VOCABULARY,line_num
	global CATEGORY,SUBCATEGORY
	matrix = [None]*line_num
	with open(data,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		example = 0
		for row in reader:
			example = example + 1
			vector = [0]*len(VOCABULARY)
			for item in normalizer(row[2].split()):
				if item in VOCABULARY:
					vector[int(VOCABULARY[item])] = 1
			vector.append(int(row[5]))
			MATRIX.append(vector)
			CATEGORY.append(int(row[3]))
			SUBCATEGORY.append(int(row[4]))

def normalizer(l):
	stop = set(stopwords.words('english'))
	pattern = re.compile('\W')
	l = [item for item in l if item.isalpha()]
	l = [i for i in l if i not in stop]
	l = [i for i in l if len(i)>4]
	for i in range(0,len(l)):
		l[i] = re.sub(pattern,'',l[i].lower())
		l[i] = PS.stem(l[i],0,len(l[i])-1)

	return l

def indexing():

	global VOCABULARY,DATA_FILE,PRETFIDF,line_num
	with open(DATA_FILE,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
		for row in reader:
			line_num = line_num + 1
			bar.update(line_num)
			for word in normalizer(row[2].split()):
				if word in PRETFIDF:
					if {line_num:normalizer(row[2].split()).count(word)} not in PRETFIDF[word]:
						PRETFIDF[word].append({line_num:normalizer(row[2].split()).count(word)})
				else:
					PRETFIDF[word] = []
					PRETFIDF[word].append({line_num:normalizer(row[2].split()).count(word)})
	calc_tf_idf()

def calc_tf_idf():
	global PRETFIDF,line_num
	weights = {}	
	for key in PRETFIDF:
		weights[key] = log(float(line_num)/len(PRETFIDF[key]),10)
		temp = 0
		for val in PRETFIDF[key]:
			for k in val:
				temp = temp + 1 + log(k,10)
		weights[key] = weights[key] * temp 

	weights = [(k, v) for k, v in weights.iteritems()]
	weights.sort(key=operator.itemgetter(1))
	make_vocabulary(weights)


def make_vocabulary(wieghts):
	global VOCABULARY
	wieghts = wieghts[(int)(0.8*len(wieghts)):len(wieghts)]
	count  = 0
	for k in wieghts:
		VOCABULARY[k[0]] = count
		count = count + 1

start_time = time.time()
indexing()

genMatrix(DATA_FILE)

TRAIN = MATRIX[0:(int)(0.7*len(MATRIX))]
TEST = MATRIX[(int)(0.7*len(MATRIX)):]

TRAIN_CATEG = CATEGORY[0:(int)(0.7*len(CATEGORY))]
TEST_CATEG = CATEGORY[(int)(0.7*len(CATEGORY)):]

TRAIN_SUBCATEG = SUBCATEGORY[0:(int)(0.7*len(SUBCATEGORY))]
TEST_SUBCATEG = SUBCATEGORY[(int)(0.7*len(SUBCATEGORY)):]

clf = SVC()
clf.fit(np.array(TRAIN),np.array(TRAIN_CATEG))

total = 0 
correct = 0

res_categ = clf.predict(TEST)
for i in xrange(len(res_categ)):
	total = total + 1
	if res_categ[i] == TEST_CATEG[i]:
		correct = correct + 1
print "Accuracy in Categories: ", ((float)(correct)/total)*100 ," %"


clf.fit(np.array(TRAIN),np.array(TRAIN_SUBCATEG))
total = 0 
correct = 0

res_subcateg = clf.predict(TEST)
for i in xrange(len(res_subcateg)):
	total = total + 1
	if res_subcateg[i] == TEST_SUBCATEG[i]:
		correct = correct + 1


clf.fit(np.array(TRAIN),np.array(TRAIN_SUBCATEG))
total = 0 
correct = 0

res_subcateg = clf.predict(TEST)
for i in xrange(len(res_subcateg)):
	total = total + 1
	if res_subcateg[i] == TEST_SUBCATEG[i]:
		correct = correct + 1

print "Accuracy in Sub - Categories: ", ((float)(correct)/total)*100 ," %"

clf = svm.SVR()
clf.fit(np.array(TRAIN),np.array(TRAIN_CATEG))

total = 0 
correct = 0

res_categ = clf.predict(TEST)
for i in xrange(len(res_categ)):
	total = total + 1
	if res_categ[i] == TEST_CATEG[i]:
		correct = correct + 1
print "Accuracy in Categories: ", ((float)(correct)/total)*100 ," %"

numpy.random.seed(7)
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print "\n\n**** REDUCING DIMESIONS TO HALF ****\n\n"


clf = SVC()

MATRIX = np.array(MATRIX)
n_components = (int)(MATRIX.shape[1]*0.5)
pca = TruncatedSVD(n_components)
MATRIX = pca.fit_transform(MATRIX)

TRAIN = MATRIX[0:(int)(0.7*len(MATRIX))]
TEST = MATRIX[(int)(0.7*len(MATRIX)):]

clf.fit(np.array(TRAIN),np.array(TRAIN_CATEG))

total = 0 
correct = 0

res_categ = clf.predict(TEST)
for i in xrange(len(res_categ)):
	total = total + 1
	if res_categ[i] == TEST_CATEG[i]:
		correct = correct + 1
print "(Dim) Accuracy in Categories: ", ((float)(correct)/total)*100 ," %"


clf.fit(np.array(TRAIN),np.array(TRAIN_SUBCATEG))
total = 0 
correct = 0

res_subcateg = clf.predict(TEST)
for i in xrange(len(res_subcateg)):
	total = total + 1
	if res_subcateg[i] == TEST_SUBCATEG[i]:
		correct = correct + 1


print "(Dim) Accuracy in Sub - Categories: ", ((float)(correct)/total)*100 ," %"


print "--- %s seconds ---" % (time.time() - start_time)
import sys
import re
import time
import numpy as np
from utility_functions import *
from stemming import *
from scipy import sparse
from nltk.corpus import stopwords 
from collections import Counter

PS = PorterStemmer()
DATA_FILE = sys.argv[1]
TRAIN_FILE = sys.argv[2]
TEST_FILE = sys.argv[3]

PRETFIDF = {}
VOCABULARY = []
MATRIX = []

def genMatrix(data):
	num_lines = sum(1 for line in open(data)) # To count the number of lines
	global VOCABULARY
	matrix = [None]*num_lines
	with open(data,'rb') as readfile:
		with open("binary_"+data,'w') as writefile:
			reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
			writer = csv.writer(writefile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
			line_num = 0
			for row in reader:
				vector = [False]*len(VOCABULARY)
				for item in normalizer(row[0].split()):
					vector[int(VOCABULARY[item])] = True
				writer.writerow(vector)
				line_num = line_num + 1

def normalizer(l):
	stop = set(stopwords.words('english'))
	pattern = re.compile('\W')
	l = [item for item in l if item.isalpha()]
	l = [i for i in l if i not in stop]
	for i in range(0,len(l)):
		l[i] = re.sub(pattern,'',l[i].lower())
		l[i] = PS.stem(l[i],0,len(l[i])-1)

	return l

def genVocabulary():

	global VOCABULARY,DATA_FILE
	vocabulary = []
	with open(DATA_FILE,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			vocabulary.extend(normalizer(row[2].split()))

	VOCABULARY = list(set(vocabulary))

def indexing():

	global VOCABULARY,DATA_FILE,PRETFIDF
	with open(DATA_FILE,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		line_num = 0
		for row in reader:
			line_num = line_num + 1
			print line_num
			for word in normalizer(row[2].split()):
				if word in PRETFIDF:
					if {line_num:normalizer(row[2].split()).count(word)} not in PRETFIDF[word]:
						PRETFIDF[word].append({line_num:normalizer(row[2].split()).count(word)})
				else:
					PRETFIDF[word] = []
					PRETFIDF[word].append({line_num:normalizer(row[2].split()).count(word)})

start_time = time.time()
# genVocabulary()
indexing()
print PRETFIDF
# genMatrix(DATA_FILE)
print "--- %s seconds ---" % (time.time() - start_time)
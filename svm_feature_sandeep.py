import sys
import re
import time
import numpy as np
from utility_functions import *
from stemming import *
from scipy import sparse
from nltk.corpus import stopwords 

PS = PorterStemmer()
DATA_FILE = sys.argv[1]
TRAIN_FILE = sys.argv[2]
TEST_FILE = sys.argv[3]

VOCABULARY = {}
MATRIX = []

def genMatrix(data):
	num_lines = sum(1 for line in open(data)) # To count the number of lines
	global VOCABULARY
	matrix = [None]*num_lines
	with open(data,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		line_num = 0
		for row in reader:
			vector = [0]*len(VOCABULARY)
			for item in normalizer(row[0].split()):
				vector[int(VOCABULARY[item])] = 1
			matrix[line_num] = vector
			line_num = line_num + 1

	matrix = sparse.csr_matrix(np.array(matrix))
	return matrix

def normalizer(l):
	stop = set(stopwords.words('english'))
	pattern = re.compile('\W')
	l = [item for item in l if item.isalpha()]
	l = [i for i in l if i not in stop]
	for i in range(0,len(l)):
		l[i] = re.sub(pattern,'',l[i].lower())
		l[i] = PS.stem(l[i],0,len(l[i])-1)

	return l

def genVocabulary(data):

	global VOCABULARY
	vocabulary = []
	with open(data,'rb') as readfile:
		reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			vocabulary.extend(normalizer(row[2].split()))

	vocab = list(set(vocabulary))
	vocabulary = {}
	for i in xrange(len(vocab)):
		vocabulary[vocab[i]] = i
	VOCABULARY = vocabulary

start_time = time.time()
genTrainAndTest(DATA_FILE,TRAIN_FILE,TEST_FILE)
genVocabulary(DATA_FILE)

print "--- %s minutes ---" % (time.time() - start_time)
MATRIX = genMatrix(TRAIN_FILE)
print MATRIX.getnnz()
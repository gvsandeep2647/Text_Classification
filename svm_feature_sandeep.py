import sys
import re
from utility_functions import *
from stemming import *
from nltk.corpus import stopwords 

PS = PorterStemmer()
DATA_FILE = sys.argv[1]
TRAIN_FILE = sys.argv[2]
TEST_FILE = sys.argv[3]

VOCABULARY = {}

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


genTrainAndTest(DATA_FILE,TRAIN_FILE,TEST_FILE)
genVocabulary(DATA_FILE)
genVectors()
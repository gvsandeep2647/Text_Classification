import sys
from utility_functions import *

DATA_FILE = sys.argv[1]
TRAIN_FILE = sys.argv[2]
TEST_FILE = sys.argv[3]

genTrainAndTest(DATA_FILE,TRAIN_FILE,TEST_FILE)
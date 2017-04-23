import pandas as pd
from vocabcreater import vocabulary

d = pd.read_csv('SampleForNaive.csv')
vocablength=len(vocabulary) #no. of words in vocabulary
Id = list(d.id.unique())
data = d['data'].tolist()
category = d['class'].tolist()
print data[0]
print category

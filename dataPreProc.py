"""
  
  Aim : To implement NLP and AI techniues to classify conversations into categories and sub-categories
  
  Instructor : Dr. Anand N.
  
  Contributors : G V Sandeep 2014A7PS106H
                 Kushagra Agrawal 2014AAPS334H
				 Ayush Beria 2014A7PSxxxH
				 Rajat Jain 2014A7PSxxxH

  Course No : CS F407 Artificial Intelligence

  Working of dataPreProc.py:

"""

import csv 

with open('sample.csv','rb') as readfile:
	'''
		To iterate through the data and find anamolies if they exist such as :
		1. Missing Data
		2. Data Fields which do not follow the desired Format etc.
		3. The final data which will not comprise of all these anamolies will be stored in final_data array and this data will be used for further proceedings.

	'''
	reader = csv.reader(readfile, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
	line_num = 0
	clean = 1
	for row in reader:
		line_num = line_num + 1
		data_row = []
		
		''' Ensuring all the File IDs are integers '''
		try:
			data_row.append(int(row[0]))
		except:
			clean = 0
			print "Error In Converting File ID to Integer in line number: ",line_num
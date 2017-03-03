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
final_data = []
with open('sample.csv','rb') as readfile:
	'''
		To iterate through the data and find anamolies if they exist such as :
		1. Missing Data
		2. Data Fields which do not follow the desired Format etc.
		3. The final data which will not comprise of all these anamolies will be stored in final_data array and this data will be used for further proceedings.

	'''
	reader = csv.reader(readfile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
	line_num = 0

	for row in reader:
		clean = 1 # to check whether the row currently under consideration is free of anamolies or not
		line_num = line_num + 1
		data_row = []

		''' Ensuring all the File IDs are integers '''
		try:
			data_row.append(int(row[0]))
		except:
			clean = 0
			print "Error In Converting File ID to Integer in line number: ",line_num

		''' Pre Processing on Summary ''' 
		try:
			summary = row[1]
			data_row.append(summary)
		except:
			clean = 0
			print "Error In the Summary in line number: ",line_num
		
		''' Pre Processing on Call Data '''
		try:
			call_data = row[2]
			data_row.append(call_data)
		except:
			clean = 0
			print "Error In the Call Data in line number: ",line_num

		''' Pre Processing on Categories. Assigning All the Possible Categories with a number '''
		try:
			categories = row[3]
			data_row.append(categories)
		except:
			clean = 0
			print "Error In the Categories in line number: ",line_num

		''' Pre Processing on Sub Categories. Assigning All the Possible Sub Categories with a number '''
		try:
			sub_categories = row[4]
			data_row.append(sub_categories)
		except:
			clean = 0
			print "Error In the Sub_categories in line number: ",line_num

		''' Pre Processing on Previous Appointment '''
		try:
			prev_appt = row[5]
			data_row.append(prev_appt)
		except:
			clean = 0
			print "Error In the Previous Appt in line number: ",line_num

		''' Pre Processing on transaction ID. Eliminating Underscores and making it one digit. Do we really need this data? '''
		try:
			trans_id = int(row[6].replace("_",""))
			data_row.append(trans_id)
		except:
			clean = 0
			print "Error In the Transaction ID in line number: ",line_num

		
		''' If no anamolies have been found in the data, add it to the final data to be considered ''' 
		if clean == 1:	
			final_data.append(data_row)


''' The final data with no anamolies'''
print final_data
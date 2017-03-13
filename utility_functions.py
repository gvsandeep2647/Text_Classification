import csv
import numpy as np
def getNumPrevAppt(prev_appt):
	
	'''
	Assigns numeric value to the field : "Previous Appointment"
	'''

	if prev_appt == "NO":
		return 0
	elif prev_appt == "YES":
		return 1
	else:
		return -1
	
def getNumCategory(category):
	
	'''
	Assign numeric value to the field : "Category"	
	'''
	category = category.upper()
	if category == "APPOINTMENTS":
		return 1
	elif category == "ASK_A_DOCTOR":
		return 2
	elif category == "JUNK":
		return 3
	elif category == "LAB":
		return 4
	elif category == "MISCELLANEOUS":
		return 5
	elif category == "PRESCRIPTION":
		return 6
	else:
		return -1

def getNumSubCategory(sub_categories):

	'''
	Assign numeric value to the field : "Sub Category"	
	'''
	sub_categories = sub_categories.upper()
	if sub_categories == "CANCELLATION":
		return 1
	elif sub_categories == "CHANGE OF HOSPITAL":
		return 2
	elif sub_categories == "CHANGE OF PHARMACY":
		return 3
	elif sub_categories == "CHANGE OF PROVIDER":
		return 4
	elif sub_categories == "FOLLOW UP ON PREVIOUS REQUEST":
		return 5
	elif sub_categories == "JUNK":
		return 6
	elif sub_categories == "LAB RESULTS":
		return 7
	elif sub_categories == "MEDICATION RELATED":
		return 8
	elif sub_categories == "NEW APPOINTMENT":
		return 9
	elif sub_categories == "OTHERS":
		return 10
	elif sub_categories == "PRIOR AUTHORIZATION":
		return 11
	elif sub_categories == "PROVIDER":
		return 12
	elif sub_categories == "QUERIES FROM INSURANCE FIRM":
		return 13
	elif sub_categories == "QUERIES FROM PHARMACY":
		return 14
	elif sub_categories == "QUERY ON CURRENT APPOINTMENT":
		return 15
	elif sub_categories == "REFILL":
		return 16
	elif sub_categories == "RESCHEDULING":
		return 17
	elif sub_categories == "RUNNING LATE TO APPOINTMENT":
		return 18
	elif sub_categories == "SHARING OF HEALTH RECORDS (FAX, E-MAIL, ETC.)":
		return 19
	elif sub_categories == "SHARING OF LAB RECORDS (FAX, E-MAIL, ETC.)":
		return 20
	elif sub_categories == "SYMPTOMS":
		return 21
	else:
		return -1

def sanitize(call_data):
	call_data = call_data.split()
	
	''' 
	Removing Empty Elements and all the unnecessary elements. *Debatable*
	Storing the cleaned string back into a file specfied at the compile time

	''' 

	call_data = [x for x in call_data if x != '']	
	call_data = [x for x in call_data if "\\" not in x ]
	call_data = ' '.join(call_data)
	return call_data

def genTrainAndTest(data_file,train_file,test_file):
	
	'''
	This function takes as an input the following three files: 
	1. data_file : which contains the data
	2. train_file : The file which shall contain the training data and only relevant fields
	3. test_file : The file which shall contain the test data and only relevant fields

	Approximately 70% of data is choosen as the training data. This data is selected randomly
	The Remaining data is treated as test_data
	'''
	
	with open(data_file,'rb') as dataFile:
		with open(train_file,'w') as trainFile:
			with open(test_file,'w') as testFile:
				reader  = csv.reader(dataFile, skipinitialspace=False,delimiter=',',quoting=csv.QUOTE_MINIMAL)
				writer1 = csv.writer(trainFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
				writer2 = csv.writer(testFile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
				flag = 0
				for row in reader:
					data_row = []
					data_row.append(row[2])
					data_row.append(row[3])
					data_row.append(row[4])
					data_row.append(row[5])
					if int(np.random.choice([0,1],1,p=[0.3,0.7])) == 1:
						writer1.writerow(data_row)
					else:
						writer2.writerow(data_row)
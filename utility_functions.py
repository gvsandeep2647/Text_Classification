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

	if sub_categories == "CANCELLATION":
		return 1
	elif sub_categories == "CHANGE OF HOSPITAL":
		# Some one please complete this
'''
employee deatail and bank details inheritance concept
'''

class Employee:
	'''employee table details link name suranem,panNO,contactNo'''
	def __init__(self,name,surname,panNo,contactNo):
		self.name=name
		self.surname=surname
		self.panNo=panNo
		self.conatctNo=contactNo
	def fullName(self):
		return self.name+self.surname
	


class Bank:
	'''Bank Details'''
	def __init__(self,panNo,accountNo,ammount):
		self.panNo=panNo
		self.accountNo=accountNo
		self.ammount=ammount


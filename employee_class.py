'''
 class and instance
'''

'''
class ClassName:
	'class documentation'
	class_suite



The class has a documentation string, which can be accessed via ClassName.__doc__.
The class_suite consists of all the component statements defining class members, data attributes and functions.

'''

######### employee class #######

class Bank:
	'bank interset rate calculate'
	
	def __init__(self,accountNo):
		self.acc=accountNo
	
	def display(self):
		print ("bank account %d" % self.acc)

	def calculate(self,ammount,interest,year):
			PI=ammount*interest*year
			return PI/100

emp1=Bank(12344)
emp2=Bank(1564645)
emp3=Bank(45455)
emp1.display()
emp2.display() 
emp3.display()  
print(emp3.calculate(10000,4,2))
print(Bank.__doc__)
print(Bank.__name__)
print(Bank.__module__)
print(Bank.__dict__)

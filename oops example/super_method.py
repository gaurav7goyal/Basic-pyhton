'''

super method overriding in python

'''

class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age
	def __str__(self):
		return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):
	
	def __init__(self, first, last, age, empno):
		super().__init__(first,last,age)
		self.empno = empno
	def __str__(self):
		return super().__str__()+ ", \t" + str(self.empno)
	
	
def main():
	x = Person("Ashwin", "Pajankar", 31)
	print(x)
	y = Employee("James", "Bond", 32,1001)
	print(y)


if __name__ == "__main__":
	main()

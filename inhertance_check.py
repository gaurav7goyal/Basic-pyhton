'''
	Inhertance check for subclass
'''


class Person:
	pass

class Employee:
	pass

class student(Person):
	pass

def main():
	print(issubclass(Employee, Person))
	print(issubclass(student, Person))	

if __name__ == "__main__":
	main()

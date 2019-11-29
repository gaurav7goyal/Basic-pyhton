'''
access modifiers in python
 if you do not want a method or a class variable to be accessed from outside, you can mention that
in the docstrings of the class.
The other way to let others know not to access a variable or a method
made for internal use is to prefix the variable by underscore.
'''

class A:
	def __init__(self):
		self.a = "Public"
		self._b = "Internal use"
		self.__c = "Name Mangling in action"

def main():
	x = A()
	print(x.a)
	print(x._b)
	#print(x.__c)
	
	print(x._A__c)

if __name__ == "__main__":
	main()


"""
 File "access_modifier.py", line 19, in main
    print(x.__c)
AttributeError: 'A' object has no attribute '__c'

break point in python
import pdb
pdb.set_trace()
"""

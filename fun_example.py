'''
purpose:- pyhton method



def add_number(a,b):
	print("add fun result {}".format(a+b))


for i in range(1,10,2):
	add_number(i,i)



#######map fun########

def squre(number):
	return number**2

lista=[1,2,3,4,5,6]

for i in map(squre,lista):
	print(i)
'''
#######Fillter fun########

def divide(number):
	return number%2==0

listb=[2,4,6,8,2,3,7]

for i in filter(divide,listb):
	print(i)

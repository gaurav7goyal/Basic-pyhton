'''
argumet function
*args
**keyword
'''

'''
######default argument###########
def default_argument(number,name="Hey"):
	print(number+' --------- ' +name)

def input_number():
	number=input('enter the number')
	default_argument(number)
	default_argument(number,"hlo")

input_number()
'''

'''
########## *args argument############
def list_argument(num,*args,name="list"):
	print(num)
	print('---argument---'+name)
	for i in args:
		print(i)
		print('------number----'+ name)

list_argument(10)
list_argument(1,2,3,4)
'''
########## **keyword argument############
def dic_argument(num,*args,**keyword):
	print(num)
	for i in args:
		print(i)
	for item,value in keyword.items():
		print ("%s == %s" %(item, value)) 

dic_argument(10)
dic_argument(1,2,3,4)
dic_argument(1,a='one',b='two')


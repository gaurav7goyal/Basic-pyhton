"""
############range###############3
for i in range(2,21,2):
	index=1
	print("2*{}={}".format(index,i))
	index=index+1
###############word string format##########
print('\n\n')
words='asdfgjh'
index=0
for latter in words:
	#print(latter)
	print("at index{} latter is {}".format(index,latter))
	index=index+1

###########enumerate fun###########3
print('\n\n')
for a in enumerate(words):
	print(a)

############zip fun two list##########33

list1=[1,2,3]
list2=['a','b','c']

print('\n\n')
for i in zip(list1,list2):
	print(i)

#########input#################
"""
name = input()
sa='ddd'
print(name)
print("{}".format(name))


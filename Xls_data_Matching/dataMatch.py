import pandas as pd
import re

A = pd.read_csv('address.csv')
B = pd.read_csv('number.csv')

print(A.columns)
print(B.columns)


addess_name=A['name'].tolist()
addess_address=A['address'].tolist()
number_name=B['name'].tolist()
number_number=B['number'].tolist()

addess_dict = dict(zip(addess_name, addess_address))
number_dict = dict(zip(number_name, number_number))

print(addess_dict)
print(number_dict)



filename = 'outputData.csv'
f = open(filename, 'w')


headers = 'Name, Address, Number\n'
f.write(headers)

for name, address in addess_dict.items():
	if name in number_dict:
		print(name,address,number_dict[name])
		f.write(name + ',' +address + ',' + str(number_dict[name]) + '\n')

f.close()

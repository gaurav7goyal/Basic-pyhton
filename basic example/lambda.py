'''
lambda fun
'''


def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)

for i in range(1,4):
	number=int(input('input number'))
	print(f(number))



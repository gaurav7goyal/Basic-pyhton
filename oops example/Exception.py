'''
Exception in python
'''


def main():
	try:
		a = 1/0
		print("DEBUG:This line will not be executed...")
	
	except ZeroDivisionError as err:
		print("Error: {0}".format(err))
	
	except TypeError as err:
		print("Error: {0}".format(err))

	except Exception as err:
		print("Error: {0}".format(err))

	print("This line will be executed...")


if __name__ == "__main__":
	main()

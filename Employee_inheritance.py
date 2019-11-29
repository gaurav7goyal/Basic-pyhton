import data

class Detail:
	'''  valid check and input for employee and bank class '''
	def employeedatainput(self):
		'''employee data input'''		
		name=input("enter your name:-\t")
		surname=input("enter your surname:-\t")
		panNo=input("enter your pan no:-\t")
		contactNO=input("enter your mob no:-\t")
		e1=data.Employee(name,surname,panNo,contactNO)
		print(e1.name)

	
	def bankdataInput(self):
		'''Bank details data input'''
		panNo=input("enter your panNO:-\t")
		Account=input("enter your AccountNO:-\t")
		Ammt=input("enter your ammount:-\t")
		data.Bank(panNo,Account,Ammt)
		


	

def main():
		d1=Detail()
		d1.employeedatainput()
		d1.bankdataInput()


if __name__ == "__main__":
	main()

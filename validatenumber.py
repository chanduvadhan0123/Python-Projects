class NumberCheck:
	def __init__(self):
		self.number = "";

	def validateNum(self,num):
		if num.isnumeric():
	
			if len(num)!=10:
				print("phone number should be 10 digits")
				print()
				number=input("enter mobile number : ")
				self.validateNum(number)
			else:
				print("valid mobile number")
		else:
			print("enter valid number")
			print()
			number=input("enter mobile number : ")
			self.validateNum(number)

class Checking(NumberCheck):
	def checkingNum():
		num=input("enter number :")
		NumberCheck().validateNum(num)

	checkingNum()





		



		

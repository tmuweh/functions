
def addition(num1, num2):
	"""add two numbers """
	try:
		sum = int(num1) + int(num2)
	except Exception as e:
		#do nothing but move on
		pass
	else:
		print("Sum is " + str(sum))


while True:
	print("Enter q at anytime to quit to quit!")
	num1 = input("Enter a number: ")
	if num1 == 'q':
		break
	num2 = input("Enter another number: ")
	if num2 == 'q':
		break
	addition(num1, num2)
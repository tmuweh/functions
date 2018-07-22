
def addition(num1, num2):
	"""add two numbers """
	try:
		sum = int(num1) + int(num2)
	except TypeError:
		print("You cannot sum strings")
	else:
		print("Sum is " + str(sum))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

addition(num1, num2)
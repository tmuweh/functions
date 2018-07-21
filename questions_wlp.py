filename = 'responnses.txt'

while True:
	print("Enter 'quit' or 'Q' at anytime to exit!\n")

	answer = input("Why do you like Programming? ")

	if answer == 'quit' or answer == 'Q':
		print('Thank You and Bye!')
		break
	with open(filename, 'a') as file_object:
		file_object.write('\n ' + answer)



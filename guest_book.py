file_name = 'guest_book.txt'

while True:
	print("Enter q or Q at anytime to quit!")
	guest_name = input('Enter your name please: ')
	if guest_name == 'q' or guest_name == 'Q':
		break
	with open(file_name, 'a') as file_object:

		file_object.write('\n=> ' + guest_name.title())
		print("Välkomen " + guest_name.title())

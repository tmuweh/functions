filename = 'occurance.txt'

with open(filename, 'r') as file_object:

	content = file_object.read()

	word = input("Enter a swedish word to count in file: ")
	print(word.lower() + " appears " + str(content.lower().count(word.lower())) + " times!")

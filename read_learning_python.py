filename = 'learning_python.txt'

with open(filename) as file_object:
	file_content = file_object.read()
	print(file_content.rstrip())
print('\n')
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
	print('\n')
with open(filename) as file_object:

	lines = file_object.readlines()
	print('\n')
for line in lines:
	print(line.rstrip())
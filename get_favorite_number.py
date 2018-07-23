import json

filename = 'favorite_number.json'

try:
	with open(filename, 'r') as file_object:
		print("I know your favorite_number! It's "+ json.load(file_object))

except Exception as e:
	raise e
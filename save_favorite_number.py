import json

filename = "favorite_number.json"

with open(filename, 'w') as file_object:

	favorite = input("Enter favorite number: ")
	json.dump(favorite, file_object)
	
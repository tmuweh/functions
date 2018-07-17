def city_country(city , country):
	
	formated_string = "\"" + city.title() + ", " + country.title() + "\""

	return formated_string

print(city_country(city = "Buea", country = "Ambazonia"))
print(city_country(city = "Douala", country = "Cameroun")) 
print(city_country(city = "Paris", country = "France"))
print(city_country(city = "Kumba", country = "Ambazonia"))
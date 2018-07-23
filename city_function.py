
def city_country(city, country, poplulation=''):
	"""print string on city and country with comma separation"""
	if poplulation:
		single_string = city.title() + ", " + country.title() + " - population " + str(poplulation)
	else:	
		single_string = city.title() + ", " + country.title()
	return single_string


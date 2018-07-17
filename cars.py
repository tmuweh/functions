
def make_car(manufacturer, model_name, **properties):

	car_info = {'manufacturer': manufacturer, 'model_name': model_name}

	for key, value in properties.items():
		car_info[key] = value

	return car_info

print(make_car(manufacturer ='volvo', model_name = 'v60', color ='white', fuel= 'diesel', tow_package = True))


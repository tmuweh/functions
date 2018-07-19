
class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		

	def describe_restaurant(self):
		"""prints information about restaurant"""
		print("Name: " + self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)

	def open_restaurant(self):
		"""display information whether restaurant is open"""
		print(self.restaurant_name + " is open now")
		

umea = Restaurant("Saint David", "African")
umea.describe_restaurant()
umea.open_restaurant()


stockholm = Restaurant("Erriksson", "Western")
stockholm.describe_restaurant()
stockholm.open_restaurant()

uppsala = Restaurant("ThaiRestaurant", "ASian")
uppsala.describe_restaurant()
uppsala.open_restaurant()





class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		

	def describe_restaurant(self):
		"""prints information about restaurant"""
		print("Name: " + self.restaurant_name)
		

	def open_restaurant(self):
		"""display information whether restaurant is open"""
		print("Cuisine Type: " + self.cuisine_type)
		



class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		

	def describe_restaurant(self):
		"""prints information about restaurant"""
		print("Name: " + self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)

	def open_restaurant(self):
		"""display information whether restaurant is open"""
		print(self.restaurant_name + " is open now")
	def set_number_served(self, number_served):
		"""sets a new number serve for restaurant class"""
		self.number_served = number_served
	def increment_number_sesrved(self, increment):
		"""increments number_served by increment"""
		self.number_served += increment

restaurant = Restaurant("restau", "general")
restaurant.set_number_served(40)
print(restaurant.number_served)
restaurant.increment_number_sesrved(10)
print(restaurant.number_served)




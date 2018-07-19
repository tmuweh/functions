from restaurant import Restaurant

class IceScreamStand(Restaurant):
	"""icescreenstand for a specific restaurant"""

	def __init__(self, restaurant_name, cuisine_type, flavour):
		super(IceScreamStand, self).__init__(restaurant_name, cuisine_type)
		self.flavour = flavour

	def display_flavour(self):
		"""print flavour of icescream"""
		
		print("Flavour: "+ self.flavour)


icescream = IceScreamStand("canabina", "snack", flavour = "chokolad")

icescream.display_flavour()
icescream.describe_restaurant()

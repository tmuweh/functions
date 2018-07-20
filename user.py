
class User(object):		
	"""stores a user profile and describe user"""
	def __init__(self, firs_name, last_name, **properties):
		self.profile = {}
		self.firs_name = firs_name
		self.last_name = last_name
		self.login_attempts = 0

		for key, value in properties.items():
			self.profile[key] = value


	def describe_user(self):
		"""prints a summary of the user's profile"""
		print("Name: " + self.firs_name.title() + " " + self.last_name.title())

		for key, value in self.profile.items():
			print(key.title() + ": " + value.title())

	def greet_user(self):
		"""prints personalized greeting for the user"""
		print("Welcome " + self.firs_name + "!")
		print("\n")

	def increment_login_attempts(self):
		"""increment login attempts"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""reset login attempts to 0"""
		self.login_attempts = 0

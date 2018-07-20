from user import User

class Privileges():
	"""docstring for privilege"""
	def __init__(self, *privileges):
		self.privileges = []
		for privilege in privileges:
			self.privileges.append(privilege)
	def show_privileges(self):
		for privilege in self.privileges:
			print("\n- " + privilege)

	
class Admin(User, Privileges):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super(Admin, self).__init__(first_name, last_name)
		self.privileges = Privileges("can add post", "can delete post", "can add user", "can remove user/privileges")

	
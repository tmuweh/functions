from user import User

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name, *privileges):
		super(Admin, self).__init__(first_name, last_name)
		self.privileges = []
		for privilege in privileges:
			self.privileges.append(privilege)

	def show_privileges(self):

		for privilege in self.privileges:
			print("\n- " + privilege)


user1 = Admin("anselm", "Muweh", "can add post", "can delete post", "can add user", "can remove user/privileges")

user1.describe_user()
user1.show_privileges()
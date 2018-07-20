from random import randint

class Die(object):
	"""docstring for Die"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		side = randint(1, self.sides)
		print("side: " + str(side))

die6 = Die(6)
die10 = Die(10)
die20 = Die(20)

x = 0
while x < 10:
	die6.roll_die()
	die10.roll_die()
	die20.roll_die()
	x += 1
	print("\n")


	

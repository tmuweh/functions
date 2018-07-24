import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	"""docstring for TestEmployee"""

	def setUp(self):

		self.empl = Employee("Tangue", "Muweh", 100000)

	def test_give_default_raise(self):
		
		self.empl.give_raise() #default value in function  is 5000
		self.assertEqual(self.empl.annual_salary, 105000)
	def test_give_custom_raise(self):

		self.empl.give_raise(10000)
		self.assertEqual(self.empl.annual_salary, 110000)

unittest.main()


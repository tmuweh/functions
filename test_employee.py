import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	"""docstring for TestEmployee"""
	def test_give_default_raise(self):
		empl = Employee("Tangue", "Muweh", 100000)
		empl.give_raise() #default value in function  is 5000
		self.assertEqual(empl.annual_salary, 105000)
	def test_give_custom_raise(self):
		empl = Employee("Tangue", "Muweh", 200000)
		empl.give_raise(10000)
		self.assertEqual(empl.annual_salary, 210000)

unittest.main()


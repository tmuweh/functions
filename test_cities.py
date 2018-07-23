import unittest 

from city_function import city_country

class TestCityCountry(unittest.TestCase):
	
	def test_city_country(self):
		""" Can "Buea, Ambazonia" work?"""
		single_string = city_country("buea", "ambazonia")
		self.assertEqual(single_string, "Buea, Ambazonia")

	def test_city_country_population(self):
		"""Can "Buea, Ambazonia - population =5000000" work?"""
		single_string = city_country("buea", "Ambazonia", 5000000)
		self.assertEqual(single_string, 'Buea, Ambazonia - population 5000000')

unittest.main()


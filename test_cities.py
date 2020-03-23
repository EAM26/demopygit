import unittest
from city_functions import show_location

class CitiesCountriesTest(unittest.TestCase):
    def test_city_country(self):
        location = show_location('santiago', 'chile')
        self.assertEqual(location, "Santiago, Chile")


    def test_city_country_population(self):
        location = show_location('santiago', 'chile', 50000)
        self.assertEqual(location, "Santiago, Chile - 50000")


if __name__ == '__main__':
    unittest.main()
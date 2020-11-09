import unittest
from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = get_formatted_city('kyiv', 'ukraine')
        self.assertEqual(formatted_city, 'Kyiv, Ukraine')

    def test_city_country_populaton(self):
        formatted_city = get_formatted_city('kyiv', 'ukraine', '3000000')
        self.assertEqual(formatted_city, 'Kyiv, Ukraine - Population 3000000')

if __name__ == '__main__':
    unittest.main()

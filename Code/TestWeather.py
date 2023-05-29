import unittest
from unittest.mock import patch
from io import StringIO
import Weather

class TestWeatherModule(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Spain', 'December'])  # Mock user input
    def test_countryChoice(self, mock_input, mock_stdout):
        # Call the function you want to test
        Weather.countryChoice()
        
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIn Spain the season is Winter"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['December'])  # Mock user input
    def test_countryOutput(self, mock_input, mock_stdout):
        # Call the function you want to test
        Weather.output('country6', "Meteorological")
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "In Sri Lanka the season is Monsoon"
        self.assertEqual(output, expected_output)
    def test_weatherDict(self):
        # Verify the keys in the cityDict
        self.assertIn("country1", Weather.countryDict)
        self.assertIn("country2", Weather.countryDict)
        self.assertIn("country3", Weather.countryDict)
        self.assertIn("country4", Weather.countryDict)
        self.assertIn("country5", Weather.countryDict)
        self.assertIn("country6", Weather.countryDict)

        # Verify the values for specific keys
        self.assertEqual(Weather.countryDict["country1"]["name"], "Australia")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["December"], "Summer")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["January"], "Summer")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["February"], "Summer")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["March"], "Autumn")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["April"], "Autumn")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["May"], "Autumn")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["June"], "Winter")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["July"], "Winter")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["August"], "Winter")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["September"], "Spring")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["October"], "Spring")
        self.assertEqual(Weather.countryDict["country1"]["Meteorological"]["November"], "Spring")

        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["December"], "Birak")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["January"], "Birak")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["February"], "Bunuru")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["March"], "Bunuru")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["April"], "Djeran")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["May"], "Djeran")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["June"], "Makuru")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["July"], "Makuru")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["August"], "Dijilba")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["September"], "Dijilba")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["October"], "Kambarang")
        self.assertEqual(Weather.countryDict["country1"]["Noongar"]["November"], "Kambarang")

if __name__ == '__main__':
    unittest.main()

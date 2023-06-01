import unittest
from unittest.mock import patch
from io import StringIO
import Season

class TestSeasonModule(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Spain', 'December', 'y', 'n'])  # Mock user input
    def test_countryChoice(self, mock_input, mock_stdout):
        # Call the function you want to test
        Season.countryChoice()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIn Spain the season is Winter"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Australia', 'Noongar', 'December', 'n', 'n'])  # Mock user input
    def test_AustraliaCountry(self, mock_input, mock_stdout):
        # Call the function you want to test
        Season.countryChoice()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nWhich season system would you like to use: \nMeteorological\nNoongar\nThe current season in Australia is Birak\nOkay bye"
        self.assertEqual(output, expected_output)


    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Perth', 'n'])  # Mock user input
    def test_InvalidCountry(self, mock_input, mock_stdout):
        # Call the function you want to test
        Season.countryChoice()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIncorrect Country"
        self.assertEqual(output, expected_output) 

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Sri Lanka','Halloween','n'])  # Mock user input
    def test_InvalidMonth(self, mock_input, mock_stdout):
        # Call the function you want to test
        Season.countryChoice()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nInvalid month"
        self.assertEqual(output, expected_output) 
      
    
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['December', 'y', 'n'])  # Mock user input
    def test_countryOutput(self, mock_input, mock_stdout):
        # Call the function you want to test
        Season.output('country6', "Meteorological")
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "In Sri Lanka the season is Monsoon"
        self.assertEqual(output, expected_output)
    def test_SeasonDict(self):
        # Verify the keys in the cityDict
        self.assertIn("country1", Season.countryDict)
        self.assertIn("country2", Season.countryDict)
        self.assertIn("country3", Season.countryDict)
        self.assertIn("country4", Season.countryDict)
        self.assertIn("country5", Season.countryDict)
        self.assertIn("country6", Season.countryDict)

        # Verify the values for specific keys
        self.assertEqual(Season.countryDict["country1"]["name"], "Australia")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["December"], "Summer")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["January"], "Summer")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["February"], "Summer")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["March"], "Autumn")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["April"], "Autumn")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["May"], "Autumn")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["June"], "Winter")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["July"], "Winter")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["August"], "Winter")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["September"], "Spring")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["October"], "Spring")
        self.assertEqual(Season.countryDict["country1"]["Meteorological"]["November"], "Spring")

        self.assertEqual(Season.countryDict["country1"]["Noongar"]["December"], "Birak")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["January"], "Birak")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["February"], "Bunuru")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["March"], "Bunuru")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["April"], "Djeran")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["May"], "Djeran")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["June"], "Makuru")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["July"], "Makuru")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["August"], "Dijilba")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["September"], "Dijilba")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["October"], "Kambarang")
        self.assertEqual(Season.countryDict["country1"]["Noongar"]["November"], "Kambarang")

if __name__ == '__main__':
    unittest.main()

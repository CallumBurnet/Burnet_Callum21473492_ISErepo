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
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nSri Lanka\nIn Spain the season is Winter"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['December'])  # Mock user input
    def test_countryOutput(self, mock_input, mock_stdout):
        # Call the function you want to test
        Weather.output('country5', "Meteorological")
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "In Sri Lanka the season is Monsoon"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from io import StringIO
import Temp
import Weather

class TestTemperatureModule(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Perth', 'morning'])  # Mock user input
    def test_cityChoice(self, mock_input, mock_stdout):
        # Call the function you want to test
        Temp.cityChoice()
        
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        
        # Assert the expected output
        expected_output = "Which City are you selecting: \nPerth\nAdelaide\nWould you like the morning or afternoon temperature?\nThe morning temperature of Perth is 18.2"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['morning'])  # Mock user input
    def test_Cityoutput(self, mock_input, mock_stdout):
        # Call the function you want to test
        Temp.Cityoutput('city1')
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Would you like the morning or afternoon temperature?\nThe morning temperature of Perth is 18.2"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

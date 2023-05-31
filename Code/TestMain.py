import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMainModule(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Incorrect input', 'n'])  # Mock user input
    def test_MainIncorrect(self, mock_input, mock_stdout):
        # Call the function you want to test
        main.mainLoop()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Bye"
        self.assertEqual(output, expected_output)
                
                # Assert the expected output
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Find the Season of a Country', 'n', 'n'])  # Mock user input
    def test_MainSeason(self, mock_input, mock_stdout):
        # Call the function you want to test
        main.mainLoop()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIncorrect Country"
        self.assertEqual(output, expected_output)
                
                # Assert the expected output 
    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements
    @patch('builtins.input', side_effect=['Find the Temperature of a city', 'n', 'n'])  # Mock user input 
    def test_MainTemperature(self, mock_input, mock_stdout):
        # Call the function you want to test
        main.mainLoop()
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Which City are you selecting: \nPerth\nAdelaide"
        self.assertEqual(output, expected_output)
                
                # Assert the expected output          
if __name__ == '__main__':
    unittest.main()

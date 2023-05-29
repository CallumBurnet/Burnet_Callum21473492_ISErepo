import unittest
from unittest.mock import patch
from io import StringIO
import Temp

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
    def test_Cityoutput_normal(self, mock_input, mock_stdout):
        # Call the function you want to test
        Temp.Cityoutput('city1')
        # Get the printed output
        output = mock_stdout.getvalue().strip()
        # Assert the expected output
        expected_output = "Would you like the morning or afternoon temperature?\nThe morning temperature of Perth is 18.2"
        self.assertEqual(output, expected_output)

    def test_cityDict(self):
        # Verify the keys in the cityDict
        self.assertIn("city1", Temp.cityDict)
        self.assertIn("city2", Temp.cityDict)

        # Verify the values for specific keys
        self.assertEqual(Temp.cityDict["city1"]["name"], "Perth")
        self.assertEqual(Temp.cityDict["city1"]["Min"], 0.7)
        self.assertEqual(Temp.cityDict["city1"]["Max"], 46.0)
        self.assertEqual(Temp.cityDict["city1"]["Morning Temperature"], 18.2)
        self.assertEqual(Temp.cityDict["city1"]["Afternoon Temperature"], 23.0)

        self.assertEqual(Temp.cityDict["city2"]["name"], "Adelaide")
        self.assertEqual(Temp.cityDict["city2"]["Min"], -1.0)
        self.assertEqual(Temp.cityDict["city2"]["Max"], 49.0)
        self.assertEqual(Temp.cityDict["city2"]["Morning Temperature"], 16.5)
        self.assertEqual(Temp.cityDict["city2"]["Afternoon Temperature"], 21.0)

if __name__ == '__main__':
    unittest.main()

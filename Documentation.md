# Cover Page
    > ISE Final Project
    > Callum Burnet
    > 21473492
    > Wednesday 8am
# Introduction
This project is to validate the core concepts learnt in Introduction to Software engineering such as:
> Modularity
> Version control
> Black box testing
> White box testing
> Ethics
Through a simple yet effect small project to test all of these concepts.
# Module Description
## Temperature file
    1. cityChoice()
    2. cityOutput()
## Weather file
    1. countryChoice()
    2. output()
# Modularity

# Black box test cases
## Equivalence partitioning
> Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.
> The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.
Test cases are designed to cover each partition at least once, rather than testing every possible input individually.
> It helps identify representative values that are likely to uncover defects.Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.
> The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.
> Test cases are designed to cover each partition at least once, rather than testing every possible input individually.
It helps identify representative values that are likely to uncover defects.

CODE
```Python
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
```
## Boundary value analysis
> Boundary value analysis is a testing technique that focuses on testing the boundaries or limits of input values.
> The idea behind boundary value analysis is that errors often occur at the edges or boundaries of input ranges, rather than in the middle.
> Test cases are designed to test values at the lower and upper boundaries of valid and invalid ranges, as well as just inside and just outside the boundaries.
> The goal is to uncover errors that are more likely to occur near the boundaries and ensure the system handles them correctly.
> Test cases are typically derived from the minimum and maximum valid input values, as well as values immediately above and below those limits.
# White box test cases

# Test implementation & execution
# Version control
# Ethics
# Discussion

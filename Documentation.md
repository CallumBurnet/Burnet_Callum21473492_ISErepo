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
- Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.
- The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.
Test cases are designed to cover each partition at least once, rather than testing every possible input individually.
- It helps identify representative values that are likely to uncover defects.Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.
- The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.
- Test cases are designed to cover each partition at least once, rather than testing every possible input individually.
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
    - Boundary value analysis is a testing technique that focuses on testing the boundaries or limits of input values.
    - The idea behind boundary value analysis is that errors often occur at the edges or boundaries of input ranges, rather than in the middle.
    - Test cases are designed to test values at the lower and upper boundaries of valid and invalid ranges, as well as just inside and just outside the boundaries.
    - The goal is to uncover errors that are more likely to occur near the boundaries and ensure the system handles them correctly.
    - Test cases are typically derived from the minimum and maximum valid input values, as well as values immediately above and below those limits.

# White box test cases
    - White box testing is a software testing technique that focuses on the internal structure and implementation details of the system under test. It involves testing the code's internal paths, branches, and logic to ensure that all possible execution paths are tested
    - Understanding the Internal Structure: White box testers have access to the internal workings of the system, including the source code, algorithms, and data structures. They analyze the code and its implementation details to identify potential areas of concern and develop test cases accordingly.

    - Coverage Criteria: White box testing aims to achieve thorough coverage of the code by exercising all possible paths, branches, and conditions. Common coverage criteria used in white box testing include statement coverage, branch coverage, path coverage, and condition coverage.

    - Testing Techniques: Various testing techniques are used in white box testing, including path testing, control flow testing, data flow testing, and mutation testing. These techniques help testers design test cases that target specific paths or conditions within the code.

    - Test Case Design: Test cases in white box testing are often based on the internal structure of the code. Testers focus on exercising different branches, loops, and conditional statements, as well as testing edge cases and boundary conditions. Test cases may be derived from the code itself, code reviews, or analysis of requirements and specifications.

    - Debugging and Error Localization: White box testing can help identify and localize errors within the code. By examining the internal paths and variables, testers can pinpoint the exact location where an error occurs, making it easier for developers to debug and fix the issue.

    -Code Optimization: White box testing can also highlight areas of the code that can be optimized for better performance, efficiency, or maintainability. By analyzing the code during testing, potential improvements or optimizations may be identified.
```python
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
```
# Test implementation & execution
# Version control
Version Control is utilised in the project as a method of change management, and project ease of access. Many times during the development of the project I switched between PC and laptop, cloning the remote repository was much easier than manually saving and sending between devices.
 
# Ethics
## User Privacy

## Data Accuracy
## Transparency and informed Consent
## Non-Discriminant
## Accessibility Design
## Responsible Use of Data
# Discussion

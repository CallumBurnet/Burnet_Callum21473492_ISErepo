# Cover Page

    > ISE Final Project

    > Callum Burnet

    > 21473492

    > Wednesday 8am

# Introduction

This project is to validate the core concepts learnt in Introduction to Software engineering such as:

>Modules

>Modularity

>Black Box Testing

>White Box Testing

>Version control

> Ethics


# Module Description

## Temperature file functions

1. cityChoice()

2. cityOutput()

## Season file functions

1. countryChoice()

2. output()

# Modularity
Modules are extremely important in computer science for a variety of reasons such as coupling, cohesion, and redundancy. In this project
  

# Black box test cases

## Equivalence partitioning

>Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.

>The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.

Test cases are designed to cover each partition at least once, rather than testing every possible input individually.

>It helps identify representative values that are likely to uncover defects.Equivalence partitioning is a testing technique that divides the input data into groups or partitions based on the assumption that if one input in a partition is valid (or invalid), the others in the same partition will exhibit similar behavior.

>The goal of equivalence partitioning is to reduce the number of test cases while ensuring adequate coverage of different input conditions.

>Test cases are designed to cover each partition at least once, rather than testing every possible input individually.

### Design 
### Main Function

|Category|Test Data|Result|
|----------|----------|-------|
|Invalid Choice|firstChoice = "incorrect input", choice = 'n'|"Bye"|
|Valid Choice - Season| FirstChoice = "Find the Season of a Country"| "Which country would you like the season for"|
|Valid Choice - Temperature|FirstChoice = "Find the Temperature of a city"|"Which City are you selecting"|



#### Season Functionality

| Category | Test Data |  Result |
|-----------|------------|---------|
|Valid Country, Valid Month| Country = "Spain", month = "December"| In Spain the season is Winter|
|Valid Country, Valid Season, Valid Month| Country = "Australia", Season = Noongar, month = December | In Australia the season is Birak|
|Invalid Country, Valid Month| Country = "Perth", Month = "December"| Invalid input try again|
| Valid Country, Invalid Month| Country = "Sri Lanka", Month = "Halloween"| Invalid input try again|

#### Temperature Functionality

| Category | Test Data | Result |
|----------|----------|---------|
|Valid City, Valid time of day, Valid time|city = "Perth", tempChoice = "morning", Currtemperature =  18.2 |"The Current temperature of Perth is equal to the average temperature"|
|Valid City, Invalid time |city = "Perth", tempChoice = "morninggggg"|"incorrect input please try again"|
|Invalid City, Valid time| city = "Randomcity", tempChoice = "morning"|"incorrect input please try again"|
|Invalid City, Invalid time| city = "Randomcity", tempChoice = "time"| "incorrect input please try again"|


## Boundary value analysis

- Boundary value analysis is a testing technique that focuses on testing the boundaries or limits of input values.

- The idea behind boundary value analysis is that errors often occur at the edges or boundaries of input ranges, rather than in the middle.

- Test cases are designed to test values at the lower and upper boundaries of valid and invalid ranges, as well as just inside and just outside the boundaries.

- The goal is to uncover errors that are more likely to occur near the boundaries and ensure the system handles them correctly.

- Test cases are typically derived from the minimum and maximum valid input values, as well as values immediately above and below those limits.
### Design

| Boundary | Test Data | Expected Result|
|------------|------------|-----------------|
|Between invalid and valid, Morning Perth| Currtemperature = -21, Currtemperature = -20 | = "The morning temperature of Perth is less than average", = "Invalid temperature"|
| Perth Morning Between 5 less than average and 4 less than average | Currtemperature = 13.2, Currtemperature = 14.2 | = "The difference of temperature is greater than 5 degrees lower, The morning temperature of Perth is less than average temperature", "The morning temperature of Perth is less than average temperature"|
| Perth Morning Between 4 more than average and 5 more than average | Currtemperature = 22.2, Currtemperature = 23.2 | = "The difference of temperature is greater than 5 degrees more, The morning temperature of Perth is more than average temperature", "The morning temperature of Perth is more than average temperature"|
|Between valid and invalid, Afternoon Perth| Currtemperature = 59, Currtemperature = 60 | = "The afternoon temperature of Perth is more than average", = "Invalid temperature"|

# White box test cases

>White box testing is a software testing technique that focuses on the internal structure and implementation details of the system under test. It involves testing the code's internal paths, branches, and logic to ensure that all possible execution paths are tested

>Understanding the Internal Structure: White box testers have access to the internal workings of the system, including the source code, algorithms, and data structures. They analyze the code and its implementation details to identify potential areas of concern and develop test cases accordingly.

>Coverage Criteria: White box testing aims to achieve thorough coverage of the code by exercising all possible paths, branches, and conditions. Common coverage criteria used in white box testing include statement coverage, branch coverage, path coverage, and condition coverage.

>Testing Techniques: Various testing techniques are used in white box testing, including path testing, control flow testing, data flow testing, and mutation testing. These techniques help testers design test cases that target specific paths or conditions within the code.

>Test Case Design: Test cases in white box testing are often based on the internal structure of the code. Testers focus on exercising different branches, loops, and conditional statements, as well as testing edge cases and boundary conditions. Test cases may be derived from the code itself, code reviews, or analysis of requirements and specifications.

>Debugging and Error Localization: White box testing can help identify and localize errors within the code. By examining the internal paths and variables, testers can pinpoint the exact location where an error occurs, making it easier for developers to debug and fix the issue.

>Code Optimization: White box testing can also highlight areas of the code that can be optimized for better performance, efficiency, or maintainability. By analyzing the code during testing, potential improvements or optimizations may be identified.



- Season function

- For the weather function i will be white box testing and asserting the values of the dictionaries, as the code is quite simple all of the functionalities can be tested in black box testing as pathways don't need to be understood, the only pathway that doesn't get tested in the values of the dictionary

| Statement | Assertion |Boolean |
|-------------------------|-------------------------------|------|
|Valid Dictionary Keys|country1 == Dict | = TRUE |
| Country Season is valid | *Season* == Dict(country1)(*month*) | = TRUE |



- Temperature function

- For the Temperature function i will be white box testing and asserting the values of the dictionaries, as the code is quite simple all of the functionalities can be tested in black box testing as pathways don't need to be understood, the only pathway that doesn't get tested in the values of the dictionary

|Statement | Assertion |Boolean |
|-------------------------|-------------------------------|------|
|Valid Dictionary Keys|  "city" == Dict | = TRUE|
| City name is valid | "Perth" == Dict(city1)(name) | = TRUE |
|City min is valid| 0.7 == Dict(city1)(Min)|  = TRUE|
|City Max is valid | 46.0 == Dict(city1)(Max)| = TRUE|
|City Morning Average is valid |18.2 == Dict(city1)("Morning Temperature")| = TRUE
|City Afternoon Average is valid |23.0 == Dict(city1)("Morning Temperature")| = TRUE|
# Test implementation & execution

## Black Box implementation
### Main Function
```python
class TestMainModule(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Incorrect input', 'n'])  # Mock user input

    def test_MainIncorrect(self, mock_input, mock_stdout):

        # Call the function you want to test

        main.mainLoop()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Bye"

        self.assertEqual(output, expected_output)

                # Assert the expected output

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Find the Season of a Country', 'n', 'n'])  # Mock user input

    def test_MainSeason(self, mock_input, mock_stdout):

        # Call the function you want to test

        main.mainLoop()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIncorrect Country"

        self.assertEqual(output, expected_output)

                # Assert the expected output

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Find the Temperature of a city', 'n', 'n'])  # Mock user input

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
	
```
### Temperature Function
```python
class TestTemperatureModule(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Perth', 'morning', '18.2'])  # Mock user input

    def test_cityEqual(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.cityChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which City are you selecting: \nPerth\nAdelaide\nIs it the morning or afternoon?\nThe current temperature of Perth is equal to the average temperature"

        self.assertEqual(output, expected_output)

  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Perth', 'morninggggg','n'])  # Mock user input

    def test_TimeInvalid(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.cityChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which City are you selecting: \nPerth\nAdelaide\nIs it the morning or afternoon?\nincorrect input"

        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Australia','n'])  # Mock user input

    def test_InvalidCity(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.cityChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which City are you selecting: \nPerth\nAdelaide"

        self.assertEqual(output, expected_output)

  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Australia','n'])  # Mock user input

    def test_InvalidBoth(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.cityChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which City are you selecting: \nPerth\nAdelaide"

        self.assertEqual(output, expected_output)

  
  
  
  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['morning','18.0'])  # Mock user input

    def test_Cityoutput_normal(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.Cityoutput('city1')

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Is it the morning or afternoon?\nThe morning temperature of Perth is less than the average temperature"

        self.assertEqual(output, expected_output)

  


```
### Season  Function
```python
class TestSeasonModule(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Spain', 'December', 'y'])  # Mock user input

    def test_countryChoice(self, mock_input, mock_stdout):

        # Call the function you want to test

        Season.countryChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIn Spain the season is Winter"

        self.assertEqual(output, expected_output)

  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Australia', 'Noongar', 'December', 'n'])  # Mock user input

    def test_AustraliaCountry(self, mock_input, mock_stdout):

        # Call the function you want to test

        Season.countryChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nWhich season system would you like to use: \nMeteorological\nNoongar\nThe current season in Australia is Birak\nOkay bye"

        self.assertEqual(output, expected_output)

  
  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Perth', 'n'])  # Mock user input

    def test_InvalidCountry(self, mock_input, mock_stdout):

        # Call the function you want to test

        Season.countryChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nIncorrect Country"

        self.assertEqual(output, expected_output)

  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['Sri Lanka','Halloween','n'])  # Mock user input

    def test_InvalidMonth(self, mock_input, mock_stdout):

        # Call the function you want to test

        Season.countryChoice()

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Which Country would you like the season for: \nCurrent choices are:\nAustralia\nSpain\nJapan\nMauritius\nMalaysia\nSri Lanka\nInvalid month"

        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['December', 'y'])  # Mock user input

    def test_countryOutput(self, mock_input, mock_stdout):

        # Call the function you want to test

        Season.output('country6', "Meteorological")

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "In Sri Lanka the season is Monsoon"

        self.assertEqual(output, expected_output)
```


## White Box implementation
###  Temperature Functionality
```python
@patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['morning','0.6'])  # Mock user input

    def test_Cityoutput_LowerBoundFail(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.Cityoutput('city1')

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Is it the morning or afternoon?\nInvalid temperature"

        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['morning','0.7'])  # Mock user input

    def test_Cityoutput_LowerBoundPass(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.Cityoutput('city1')

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Is it the morning or afternoon?\nThe difference of temperature is greater than 5 degrees lower than average\nThe morning temperature of Perth is less than the average temperature"

        self.assertEqual(output, expected_output)

  

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['afternoon','46.1'])  # Mock user input

    def test_Cityoutput_UpperBoundFail(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.Cityoutput('city1')

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Is it the morning or afternoon?\nInvalid temperature"

        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Mock sys.stdout to capture print statements

    @patch('builtins.input', side_effect=['afternoon','46.0'])  # Mock user input

    def test_Cityoutput_UpperBoundPass(self, mock_input, mock_stdout):

        # Call the function you want to test

        Temp.Cityoutput('city1')

        # Get the printed output

        output = mock_stdout.getvalue().strip()

        # Assert the expected output

        expected_output = "Is it the morning or afternoon?\nThe difference of temperature is greater than 5 degrees higher than average\nThe afternoon temperature of Perth is more than the average temperature"

        self.assertEqual(output, expected_output)
```
``
### Validation of Dictionaries - Semi Whitebox
>As you need to know the structure of the dictionary (code) to assert the dictionary
#### Temperature dictionary
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
#### Season Dictionary
```python
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
```
# Version control

- Version Control is utilised in the project as a method of change management, and project ease of access. Many times during the development of the project I switched between PC and laptop, cloning the remote repository was much easier than manually saving and sending between devices.
> Here is a history of the changes in version control made throughout the project

# Ethics

## User Privacy

- Safeguard the privacy and confidentiality of user data

- We must ensure trhat any personal information collected during the process is handled and securely and in compliance with relevant privacy laws and regulation

## Data Accuracy

- We should strive to provide accurate and up-to-date information to users.

## Transparency and informed Consent

- Users should be aware of when data is being collected from the user. This process should be as transparent as possible

## Non-Discriminant

- Ensure that the software program does not discriminate against users based on their race, ethnicity, gender, religion, nationality, or any other protected

## Accessibility Design

- Design function for the disabled, such as input loops

## Responsible Use of Data

- Stress the responsibility placed on the development of responsible use of data

# Discussion
- The Project overall went really well key take aways were:
	- Important of error handling
		- Error handling's important was really amplified in this project, as unittests would not function if errors were not handled correctly. This lead to more time fixing all errors in the code than the logical code itself 
	- Unittesting and Mocking inputs
		-Using the mocking inputs aspect of Unit Testing original was hard, as I had no knowledge of patch or even the idea of mocking user inputs. But as functions get more complex you can no longer just plug inputs as parameters in the project.  This lead to mocking the user inputs within functions.
	- Modularity issues
		- This project I was more conscious of declaring global variables as this can make the project have a higher complexity, as if the code were to be reused it losses modularity, as the global variable is required. it is much easier to use parameters and return values in the project.
	- 
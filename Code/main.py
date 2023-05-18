#Main module for Project which will call all modules
import Weather
import Temp
firstChoice = input("Would you like to: \n Find the Temperature of a city \n Find the Season of a Country \n")
if(firstChoice == "Find the Temperature of a city"):
    Weather.countryChoice()
if(firstChoice == "Find the Season of a Country"):
    Temp.cityChoice()
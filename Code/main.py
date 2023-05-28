#Main module for Project which will call all modules
#Main module for Project which will call all modules
import Weather
import Temp

def mainLoop():
    firstChoice = input("Would you like to: \n Find the Temperature of a city \n Find the Season of a Country \n Exit \n")
    if(firstChoice == "Find the Temperature of a city"):
        Temp.cityChoice()

    elif(firstChoice == "Find the Season of a Country"):
        Weather.countryChoice()
    elif(firstChoice == "Exit"):
        print("Bye")
    else:
        print("Incorret choice please try")
        mainLoop()

    


mainLoop()


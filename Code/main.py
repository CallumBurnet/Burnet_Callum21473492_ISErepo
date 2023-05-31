#Main module for Project which will call all modules
#Main module for Project which will call all modules
import Season
import Temp
import unittest

def mainLoop():
    firstChoice = input("Would you like to: \n Find the Temperature of a city \n Find the Season of a Country \n Exit \n")
    if(firstChoice == "Find the Temperature of a city"):
        Temp.cityChoice()

    elif(firstChoice == "Find the Season of a Country"):
        Season.countryChoice()
    elif(firstChoice == "Exit"):
        print("Bye")
    else:
        choice = input("Incorret input would you like to try again Y/N: ").lower()
        if(choice == 'y'):
            mainLoop()
        elif(choice == 'n'):
            print("Bye")
        else:
            print("incorrect input try again")
            mainLoop()



if __name__ == '__main__':
    mainLoop()


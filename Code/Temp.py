#This file will be for the Temperature Module

cityDict = {
    "city1": {
        "name": "Perth",
        "Min": 0.7,
        "Max": 46.0,
        "Morning Temperature": 18.2,
        "Afternoon Temperature": 23.0
    },
    "city2":{
        "name": "Adelaide",
        "Min": -1.0,
        "Max": 49.0,
        "Morning Temperature": 16.5,
        "Afternoon Temperature": 21.0
    }
}

def cityChoice():
    cityValid = False
    print("Which City are you selecting: ")
    for i in range(1, len(cityDict)+1):
        print(cityDict["city"+str(i)]["name"])
    
    choice = input("")
    for i in range(1, len(cityDict)+1):
        if(choice == cityDict["city"+ str(i)]["name"]):
            city = "city" + str(i)
            cityValid = True
            Cityoutput(city)

    if(cityValid != True):
        choice = input("Incorrect input would you like to try again Y/N: ").lower()
        if(choice == "y"):
            cityChoice()
    
    
def Cityoutput(city):
    print("Is it the morning or afternoon?")
    tempChoice = input("")
    tempChoice = tempChoice.lower()
            
    if(tempChoice == "morning"):
        cityTemp = cityDict[str(city)]["Morning Temperature"]
        currTemperature = input("What is the temperature: ")
        try:
            currTemperature = float(currTemperature)
            if(currTemperature >= cityDict[str(city)]["Min"] and currTemperature <= cityDict[str(city)]["Max"]):

                if(currTemperature == cityTemp):
                    print("The current temperature of "+ cityDict[city]["name"] + " is equal to the average temperature")
                elif(currTemperature < cityTemp):
                    if((cityTemp - currTemperature) >= 5):
                        print("The difference of temperature is greater than 5 degrees lower than average")
                    print("The morning temperature of " + cityDict[city]["name"] + " is less than the average temperature")
                elif(currTemperature > cityTemp):
                    if((currTemperature - cityTemp) >= 5):
                        print("The difference of temperature is greater than 5 degrees greater than average")
                    print("The morning temperature of " + cityDict[city]["name"] + " is more than the average temperature")
            else:
                print("Invalid temperature")

        except ValueError:
            print("Invalid Temperature please try again")
            cityChoice()
        
    elif(tempChoice == "afternoon"):
        cityTemp = cityDict[str(city)]["Afternoon Temperature"]
        currTemperature = input("What is the temperature: ")
        try:
            currTemperature =  float(currTemperature)
            if(currTemperature >= cityDict[str(city)]["Min"] and currTemperature <= cityDict[str(city)]["Max"]):
                if(currTemperature == cityTemp):
                    print("The current temperature of "+ cityDict[city]["name"] + " is equal to the average temperature")
                elif(currTemperature < cityTemp):
                    if((cityTemp - currTemperature) >= 5):
                        print("The difference of temperature is greater than 5 degrees lower than average")
                    print("The afternoon temperature of " + cityDict[city]["name"] + " is less than the average temperature")
                elif(currTemperature > cityTemp):
                    if((currTemperature - cityTemp) >= 5):
                        print("The difference of temperature is greater than 5 degrees higher than average")
                    print("The afternoon temperature of " + cityDict[city]["name"] + " is more than the average temperature")
            else:
                print("Invalid temperature")
        except ValueError:
            print("incorrect temperature please try again")
            cityChoice()

    else:
        print('incorrect input')
        tempChoice = input("Would you like to try again Y/N").lower()
        if(tempChoice == 'y'):
            Cityoutput(city)


        
    

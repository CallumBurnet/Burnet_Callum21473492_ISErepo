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
    print("Which City are you selecting: ")
    for i in range(1, len(cityDict)+1):
        print(cityDict["city"+str(i)]["name"])
    
    choice = input("")
    for i in range(1, len(cityDict)+1):
        if(choice == cityDict["city"+ str(i)]["name"]):
            city = "city" + str(i)
            Cityoutput(city)
        else:
            print("Not a valid country")
    
def Cityoutput(city):
    print("Is it the morning or afternoon?")
    tempChoice = input("")
    tempChoice = tempChoice.lower()
            
    if(tempChoice == "morning"):
        cityTemp = cityDict[str(city)]["Morning Temperature"]
        currTemperature = input("What is the temperature: ")
        if type(currTemperature) == float:
            currTemperature = float(currTemperature)
            if(currTemperature == cityTemp):
                print("The Current temperature of "+ cityDict[city]["name"] + "is equal to the average temperature: ")
            elif(currTemperature < cityTemp):
                if((cityTemp - currTemperature) >= 5):
                    print("The difference of temperature is greater than 5 degrees lower")
                print("The morning temperature of " + cityDict[city]["name"] + " is less than the average temperature")
            elif(currTemperature > cityTemp):
                if((currTemperature - cityTemp) >= 5):
                    print("The difference of temperature is greater than 5 degrees lower")
                print("The morning temperature of " + cityDict[city]["name"] + " is more than the average temperature")
        else:
            print("incorrect input type try again")
            cityChoice()
        
    elif(tempChoice == "afternoon"):
        cityTemp = cityDict[str(city)]["Afternoon Temperature"]
        currTemperature = input("What is the temperature: ")
        if type(currTemperature) == float:
            currTemperature = float(currTemperature)
            if(currTemperature == cityTemp):
                print("The Current temperature of "+ cityDict[city]["name"] + "is equal to the average temperature")
            elif(currTemperature < cityTemp):
                if((cityTemp - currTemperature) >= 5):
                    print("The difference of temperature is greater than 5 degrees lower")
                print("The afternoon temperature of " + cityDict[city]["name"] + " is less than the average temperature")
            elif(currTemperature > cityTemp):
                if((currTemperature - cityTemp) >= 5):
                    print("The difference of temperature is greater than 5 degrees lower")
                print("The afternooon temperature of " + cityDict[city]["name"] + " is more than the average temperature")
        else:
            print("incorrect input type try again")
            cityChoice()

    else:
        print('incorrect input please try again')
        cityChoice()


        
    

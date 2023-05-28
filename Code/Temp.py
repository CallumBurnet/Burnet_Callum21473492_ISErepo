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
            cityname = cityDict["city"+ str(i)]["name"]
            print("Would you like the morning or afternoon temperature?")
            tempChoice = input("")
            tempChoice = tempChoice.lower()
            
            if(tempChoice == "morning"):
              cityTemp = str(cityDict["city"+ str(i)]["Morning Temperature"])
              print("The morning temperature of " + cityname + " is " + cityTemp)
            elif(tempChoice == "afternoon"):
                cityTemp = str(cityDict["city"+ str(i)]["Afternoon Temperature"])
                print("The afternoon temperature of " + cityname + " is " + cityTemp)

            else:
                print('incorrect input please try again')
                cityChoice()


    

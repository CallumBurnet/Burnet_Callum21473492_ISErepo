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
    print(cityDict["city1"]["name"])
    print(cityDict["city2"]["name"])
    choice = input("")
    for i in range(1, len(cityDict)):
        if(choice == cityDict["city"+ str(i)]):
            city = cityDict["city"+ str(i)]
            


    

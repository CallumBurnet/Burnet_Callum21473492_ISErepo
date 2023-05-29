from PIL import Image
import os
countryDict = {
     "country1": {
         "name": "Australia",
         "Meteorological":{
            "December": "Summer",
            "January": "Summer",
            "February": "Summer",
         
            "March": "Autumn",
            "April": "Autumn",
            "May": "Autumn",

            "June": "Winter",
            "July": "Winter",
            "August": "Winter",

            "September": "Spring",
            "October": "Spring",
            "November": "Spring"
        },
        "Noongar":{
            "December": "Birak",
            "January": "Birak",
            "February": "Bunuru",
         
            "March": "Bunuru",
            "April": "Djeran",
            "May": "Djeran",

            "June": "Makuru",
            "July": "Makuru",
            "August": "Dijilba",

            "September": "Dijilba",
            "October": "Kambarang",
            "November": "Kambarang"
        }
        },
        "country2": {
            "name": "Spain",
            "December": "Winter",
            "January": "Winter",
            "February": "Winter",
         
            "March": "Spring",
            "April": "Spring",
            "May": "Spring",

            "June": "Summer",
            "July": "Summer",
            "August": "Summer",

            "September": "Autumn",
            "October": "Autumn",
            "November": "Autumn"
        },
         "country3": {
            "name": "Japan",
            "December": "Winter",
            "January": "Winter",
            "February": "Winter",
         
            "March": "Spring",
            "April": "Spring",
            "May": "Spring",

            "June": "Summer",
            "July": "Summer",
            "August": "Summer",

            "September": "Autumn",
            "October": "Autumn",
            "November": "Autumn"
        },
          "country4": {
            "name": "Mauritius",
            "December": "Summer",
            "January": "Summer",
            "February": "Summer",
         
            "March": "Autumn",
            "April": "Autumn",
            "May": "Autumn",

            "June": "Winter",
            "July": "Winter",
            "August": "Winter",

            "September": "Spring",
            "October": "Spring",
            "November": "Spring",
        },
        "country5": {
            "name": "Malaysia",
            "December": "Northeast Monsoon",
            "January": "Northeast Monsoon",
            "February": "Northeast Monsoon",
         
            "March": "Inter-monsoon",
            "April": "Inter-monsoon",
            "May": "Inter-monsoon",

            "June": "Southeast Monsoon",
            "July": "Southeast Monsoon",
            "August": "Southeast Monsoon",

            "September": "Inter-monsoon",
            "October": "Inter-monsoon",
            "November": "Inter-monsoon",
        },
        "country6": {
            "name": "Sri Lanka",
            "December": "Monsoon",
            "January": "Monsoon",
            "February": "Monsoon",
         
            "March": "Inter-monsoon",
            "April": "Inter-monsoon",
            "May": "Inter-monsoon",

            "June": "Monsoon",
            "July": "Monsoon",
            "August": "Monsoon",

            "September": "Inter-monsoon",
            "October": "Inter-monsoon",
            "November": "Inter-monsoon",
        },
}
def countryChoice():
    validCountryIn = False
    seasonChoice =  "Meteorological"
    print("Which Country would you like the season for: ")
    print("Current choices are:")
    for i in range(1, len(countryDict)+1):
        print(countryDict["country" + str(i)]["name"])
    countryInput = input("Country:")
    countryKey = ""
    for i in range(1, len(countryDict)+1):
        if(countryInput == countryDict["country" +str(i)]["name"]):
            countryKey = "country" + str(i)
            validCountryIn = True
    if(validCountryIn == True and countryInput == "Australia"):
        print("Which season system would you like to use: ")
        print("Meteorological")
        print("Noongar")
        seasonChoice = input("")
        if(seasonChoice == "Meteorological" or "Noongar"):
            output(countryKey, seasonChoice)
        else:
            print("Incorrect Seasonal System please try again")
            countryChoice()

    if(validCountryIn == True and countryInput != "Australia"):
        output(countryKey, seasonChoice)
    else:
        print("incorrect input try again")
        countryChoice()


def output(countryKey, seasonChoice):
    validMonthIn = False
    monthInput = input("Month: ")
    if(monthInput == "January" or monthInput == "February" or monthInput == "March" or monthInput == "April" or monthInput == "May" or monthInput == "June" or monthInput == "July" or monthInput == "August" or monthInput == "September" or monthInput == "October" or monthInput == "November" or monthInput == "December"):
       validMonthIn = True
    else:
        print("Fail at month")
        output(countryKey, seasonChoice)
    if(countryDict[countryKey]["name"] == "Australia" and validMonthIn == True):
        if(seasonChoice == "Meteorological"):
            Weather = countryDict[countryKey][seasonChoice][monthInput]
            imageChoice = input("Would you like to see the image of " + Weather + " Y/N")
            imageChoice = imageChoice.upper()
            if(imageChoice == "Y"):
                file = Weather.lower()
                showImages(file)
            elif(imageChoice == "N"):
                print("Okay bye")
            else: 
                print("Incorrect input")
                output(countryKey, monthInput)
                
            
            
        elif(seasonChoice == "Noongar"):
            Weather = countryDict[countryKey][seasonChoice][monthInput]
            Weather = Weather.lower()
            showImages(Weather)
    else:
        if(validMonthIn == True):
            Weather = countryDict[countryKey][monthInput]
            print("In " + countryDict[countryKey]["name"] + " the season is " + Weather)
            Weather = Weather.lower()
            showImages(Weather)
        else: 
            print("Invalid month please try again")
            output(countryKey, seasonChoice)

         



def showImages(Weather):
     # Get the current directory of the script
    currentDir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the "Documents" folder
    documentsDir = os.path.join(currentDir, "../Documents")
    os.chdir(documentsDir)
    filename = Weather + ".png"
    image_path = os.path.join(documentsDir, filename)
    image = Image.open(image_path)
    image.show()

from PIL import Image
import os
def countryChoice():
    print("Which City would you like the city for: \n")
    print("Current choices are:")





def Image():
     # Get the current directory of the script
    currentDir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the "Documents" folder
    documentsDir = os.path.join(currentDir, "../Documents")
    os.chdir(documentsDir)
    filename = "autumn.png"
    image_path = os.path.join(documentsDir, filename)
    with Image.open(image_path) as image:
        image.show()

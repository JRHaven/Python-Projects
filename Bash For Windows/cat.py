# Cat is a basic script to show the contents of a file

# Only need one library
import os

# Main Function. First check if the file exists
def show(file):
    if(os.path.exists(file) == False):
        print("cat: " + file + " file not found")
    else:
         show = open(file)
         print(show.read())
         show.close()

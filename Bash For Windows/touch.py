# touch is a script that creates a new empty file

# Our only library
import os

# Main function
def write(filename):
    new = open(filename, "w")
    new.write("")
    new.close()

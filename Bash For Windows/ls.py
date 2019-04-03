# ls is a basic script that either outputs the files in a directory or returns a list of files in the current
# directory

# Libraries
from os import walk
import os
import glob
import systemvariables

# Function that prints out all files 1 by 1 virtically without any other characters on the screen
def show():
    dir_list = os.listdir(os.getcwd())
    i = 0
    for dirs in dir_list:
        print(dir_list[i])
        i += 1
        
# Function that returns a list of everything in the current directory
def list():
    theList = os.listdir(os.getcwd())
    return theList

# Function that prints out all of the variables, unlike the echo script that only prints out 1 requested
# variable
def vars():
    print("usrsession:", systemvariables.usrsession)
    print("HOME:", systemvariables.HOME)
    print("ROOT:", systemvariables.ROOT)
    print("exepath:", systemvariables.exepath)
    print("USRDOCS:", systemvariables.USRDOCS)

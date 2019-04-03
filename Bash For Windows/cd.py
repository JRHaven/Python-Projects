# cd is a basic script that deciphers tildas and slashes then goes into desired directory

# Libraries
import os
import systemvariables

# Main Function
def go(path):
    if(path == "~"):
        os.chdir(systemvariables.HOME)
    elif(path == "/"):
        os.chdir(systemvariables.ROOT)
    else:
        if(path == ""):
            go("~")
        else:
            os.chdir(path)

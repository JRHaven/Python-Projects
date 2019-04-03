import os
import systemvariables
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

# username sets the username and password

# Libraries
import os
import systemvariables

# Main Function
def get(path):
    os.chdir(path)
    if(os.path.exists("../../Settings/ivhzadgz.bws") == True):
        username = input("What do you want your user name to be? # ")
        namefile = open("Settings/ivhzadgzzoneth.bws", "w")
        namefile.write(username)
        namefile.close
        password = input("What Password?                         # ")
        passfile = open("Settings/kvnnadgzzoneth.bws", "w")
        passfile.write(password)
        passfile.close
    username = input("What do you want your user name to be? # ")
    namefile = open("Settings/ivhzadgz.bws", "w")
    namefile.write(username)
    namefile.close
    password = input("What Password?                         # ")
    passfile = open("Settings/kvnnadgz.bws", "w")
    passfile.write(password)
    passfile.close

# usrmgr is a script responsable for the login prompt, the not-yet implemented multiple user function and
# welcoming the user into Bash For Windows. Despite not being the first script executed, this is the first
# time the user interacts with Bash For Windows.

# Libraries
import os
import repair
import bash
import systemvariables

# Login Prompt
def logon():
    os.chdir(systemvariables.exepath)
    os.chdir("../../")
    incorrect = True
    if(os.path.exists("Settings/ivhzadgzzoneth.bws") == True):
        while(incorrect == True):
            user = open("Settings/ivhzadgzzoneth.bws", "r")
            userguess = input("Type a user name # ")
            if(userguess == user.read()):
                incorrect = False
                systemvariables.usrsession = userguess
            else:
               print("Incorrect Username.")
        incorrect = True
        while(incorrect == True):
            password = open("Settings/kvnnadgzzoneth.bws", "r")
            passguess = input("password # ")
            if(passguess == password.read()):
               incorrect = False
            else:
               print("Incorrect Password.")
        password.close()
    else:
        while(incorrect == True):
            user = open("Settings/ivhzadgz.bws", "r")
            userguess = input("Type a user name # ")
            if(userguess == user.read()):
               incorrect = False
            else:
               print("Incorrect Username.")
        incorrect = True
        while(incorrect == True):
            password = open("Settings/kvnnadgz.bws", "r")
            passguess = input("password # ")
            if(passguess == password.read()):
                incorrect = False
                systemvariables.usrsession = userguess
            else:
                print("Incorrect Password.")
        password.close()
    print("Welcome to Bash(the Bourne Again Shell) for Windows!")
    user.close()
    bash.run()
    
# Function for checking a password based on username provided
def checkpassword():
    session = systemvariables.usrsession
    user = ""
    if(os.path.exists("Settings/ivhzadgzzoneth.bws") == True):
        potentialusr1 = open("Settings/ivhzadgzzoneth.bws" + "r")
        if(session == potentialusr1.read()):
            user = "Settings/ivhzadgzzoneth.bws"
    potentialusr2 = open("Settings/ivhzadgz.bws", "r")
    if(session == potentialusr2.read()):
        user = "Settings/ivhzadgzzoneth.bws"
    else:
        user = "No User"
    if(user != "No User"):
        if(user == "Settings/ivhzadgzzoneth.bws"):
            while(incorrect == True):
                password = open("Settings/kvnnadgzzoneth.bws", "r")
                passguess = input("password # ")
                if(passguess == password.read()):
                    incorrect = False
                else:
                   print("Incorrect Password.")
        else:
            while(incorrect == True):
                password = open("Settings/kvnnadgz.bws", "r")
                passguess = input("password # ")
                if(passguess == password.read()):
                    incorrect = False
                else:
                    print("Incorrect Password.")
    else:
        logon()

# Repair is a script that tries to solve any problems that comes up

# Libraries
import os
import username
import systemvariables

# Repair for anything missing in the base folder
def baserepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash")
    os.mkdir("Bash/Users")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Repair for anything missing in the base of the user folder
def baseusrrepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Like the function we just had, but only repairs in the user's personal folder
def baseusrfilerepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Repair for anything missing in the settings folder
def settingsrepair():
    print("Solving Problems...")
    os.chdir(systemvariables.exepath + "/../..")
    os.mkdir("Settings")
    username.get(os.getcwd())
    os.chdir(systemvariables.exepath + "/../..")

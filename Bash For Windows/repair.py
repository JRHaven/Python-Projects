import os
import username
import systemvariables
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
def baseusrrepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
def baseusrfilerepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
def settingsrepair():
    print("Solving Problems...")
    os.chdir(systemvariables.exepath + "/../..")
    os.mkdir("Settings")
    username.get(os.getcwd())
    os.chdir(systemvariables.exepath + "/../..")

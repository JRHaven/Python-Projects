import platform
import bash
import os
import os.path
import username
import usrmgr
import usrmgr2
import repair
import systemvariables
#print(os.getcwd())
#print(os.path.dirname(os.path.realpath(__file__)))
systemvariables.exepath = os.path.dirname(os.path.realpath(__file__))
if(platform.system() != "Windows"):
    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
    os.system("bash")
    exit()
os.chdir(systemvariables.exepath + "/../..")
#print(os.getcwd())
usrmgr2.usrcheck(os.getcwd())
username = open("Settings/ivhzadgz.bws" , "r")
if(os.path.exists("Bash") == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baserepair()
        bre
    else:
        print("Abort.")
elif(os.path.exists("Bash/Users") == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baseusrrepair()
    else:
        print("Abort.")
elif(os.path.exists("Bash/Users/" + username.read()) == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baseusrfilerepair()
    else:
        print("Abort.")
usrmgr.logon()

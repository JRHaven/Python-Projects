# Startup is the file that starts off Bash For Windows. You can only run Bash for Windows with this script.

# Import libraries
import platform
import bash
import os
import os.path
import username
import usrmgr
import usrmgr2
import repair
import systemvariables

# The commented out lines are for me to use for debugging purposes only.
#print(os.getcwd())
#print(os.path.dirname(os.path.realpath(__file__)))

# Set a system variable
systemvariables.exepath = os.path.dirname(os.path.realpath(__file__))

# Check to make sure we are running on Windows and if not start bash
if(platform.system() != "Windows"):
    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
    os.system("bash")
    exit()
    
# Move to the root of the file structure
os.chdir(systemvariables.exepath + "/../..")
#print(os.getcwd())

# Tell the login prompt what folder we are in
usrmgr2.usrcheck(os.getcwd())
username = open("Settings/ivhzadgz.bws" , "r")

# See if any folders are deleted and if they are attempt to fix it using the repair script
if(os.path.exists("Bash") == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baserepair()
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
        
# Call the login prompt
usrmgr.logon()

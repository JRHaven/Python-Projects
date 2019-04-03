import os
import repair
import bash
import usrmgr
def usrcheck(path):
    if(os.path.exists("Settings") == False):
        choice = input("Unfortunatly, Bash for Windows could not find settings. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
        if((choice == "y") or (choice == "Y")):
            repair.settingsrepair()
        else:
            print("Abort.")
    elif((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        choice = input("Unfortunatly, Bash for Windows could not find user settings. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
        if((choice == "y") or (choice == "Y")):
            repair.usersettingsrepair()
        else:
            print("Abort.")
            logon()
    else:
        usrmgr.logon()

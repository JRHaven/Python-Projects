import os
import systemvariables
import urllib
def install(go):
    print("\nMoving to Downloads Directory...")
    os.chdir(systemvariables.HOME + "\\" + systemvariables.usrsession + "\\Downloads")
    #print(os.getcwd())
    print("Getting Executable from selected source...")
    file = input("What do you want to name this new file? ")
    urllib.request.urlretrieve(go, file)
    confirm = input("Do you want to execute this file[Y,n]? ")
    if((confirm == "Y") or (confirm == "y")):
        os.system(file)
    else:
        print("The file was downloaded into the Downloads folder.")

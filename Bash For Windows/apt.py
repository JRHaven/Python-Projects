# Apt tries to get a file from the internet but does not work yet

# Libraries
import os
import systemvariables
import urllib

# Main function
def install(go):
    print("\nMoving to Downloads Directory...")
    os.chdir(systemvariables.HOME + "\\" + systemvariables.usrsession + "\\Downloads")
    # Commented out lines are for debugging purposes only
    #print(os.getcwd())
    print("Getting Executable from selected source...")
    file = input("What do you want to name this new file? ")
    
    # Attempt to retrieve the file
    urllib.request.urlretrieve(go, file)
    
    # Ask the user if they want to execute the downloaded file
    confirm = input("Do you want to execute this file[Y,n]? ")
    if((confirm == "Y") or (confirm == "y")):
        os.system(file)
    else:
        print("The file was downloaded into the Downloads folder.")

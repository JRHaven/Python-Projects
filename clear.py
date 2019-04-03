import platform
import os
def cs():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

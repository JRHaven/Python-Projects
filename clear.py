# clear makes it easier to clear the screen based on what platform one is on

# We need 2 libraries
import platform, os

# The library that makes it happen. If we are running Windows, run cls for
# the command prompt. If we are running Mac or Linux, which uses bash for the
# most part, run the clear command
def cs():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

# Code is used often, so I created a library for it. If the requested file exists, return True. If not, return False

# Uses the ls library to get list of all the files in the directory to look through
import ls

# Main function
def check(filename):
    directory = ls.list()
    if(any(filename in s for s in directory)):
       return True
    else:
       return False

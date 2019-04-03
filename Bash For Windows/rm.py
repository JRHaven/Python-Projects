# rm is a basic script that removes a file

# Libraries
import os
import ls

# Main Function. First get a listing of the directory from the ls script
def remove(file):
    directory = ls.list()
    
    # If it exists, remove it. If not, display a message
    if(any(file in s for s in directory)):
        os.remove(file)
    else:
        print("rm: The file", file, "does not exist so not deleting!")

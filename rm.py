import os
import ls
def remove(file):
    directory = ls.list()
    if(any(file in s for s in directory)):
        os.remove(file)
    else:
        print("rm: The file", file, "does not exist so not deleting!")

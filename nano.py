import os
import touch
import ls
def write(filename):
    theList = ls.list()
    if(any(filename in s for s in theList)):
        os.system("notepad " + filename)
    else:
        touch.write(filename)
        os.system("notepad " + filename)

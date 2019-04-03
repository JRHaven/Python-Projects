# nano is a basic script that opens a file in notepad. The nano script does NOT try to imitate the real GNU Nano
# text editor.

# Libraries
import os
import touch
import ls

# Main Function. First get a listing of the directory using the ls script
def write(filename):
    theList = ls.list()
    
    # Find out if there is a file called the same as the input text. If not, create the file using the touch
    # script before opening notepad
    if(any(filename in s for s in theList)):
        os.system("notepad " + filename)
    else:
        touch.write(filename)
        os.system("notepad " + filename)

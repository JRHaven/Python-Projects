'''
This file is under the MIT License.
Copyright 2026 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



 ---------------
  Documentation
 ---------------
 
Because there is no help doc for this program, here's some hastily written documentation!

This is a modification of my other study script that will shuffle between multiple results!
Like the other script, it uses set files to do its thing.

setFile.txt
-----------
Word 1:1;Word 1:2;Word 1:3;Word 1:4
Word 2:1;Word 2:2;Word 2:3;Word 2:4
Word 3:1;Word 3:2;Word 3:3;Word 3:4

Fairly basic here, each "flashcard" is on its own line, with the words
seperated by a semicolon (and no spaces!)

A study session is hardcoded to 10 sets (as this is a quick and dirty script I wrote in
an hour for myself), regardless of how many sets there are in the set file. Once it is
finished, the user presses enter and the program quits. A KeyboardInterrupt will peacefully
quit the program at any time.

study.py will NOT run without any arguments provided. The only argument should be the
set file. So to run the program on setFile.txt, the following command should be run:
$ python study.py setFile.txt
'''

from time import sleep
from random import randint
from sys import argv
import os

studySet = {}

# Argument handlage
def argHandler(args):
    if(len(args) > 1):
        # Return first valid path found in arguments. If none is found,
        # return error
        for i in args:
            # Don't run on ourselves!
            if(os.path.exists(i) and os.path.basename(__file__) not in i):
                return i

        return -1
    else:
        return -1

# Function that will import all our set data from the file into the handy dandy dictionary
# we established before
def importSet(filePath):
    studySet = []
    with open(filePath, 'r') as setFile:
        setFileConts = setFile.read()
        setFile.close()
    
    # For each line that has a ':' character, extrapolate based on that ':' character
    for i in setFileConts.split("\n"):
        if(";" in i):
            studySet += [i.split(";")]

    # return
    return studySet


def main():
    # Handle args with previous function
    filePath = argHandler(argv)
    if(filePath == -1):
        print("Either no path or invalid path entered.\nTry putting in the path to a valid set file as an argument!")
        return 1
    
    studySet = importSet(filePath)
    # Have all this in a try to deal with keyboard interrupts
    try:
        # Use randint() to generate a random study word index ya know what im sayin
        index = randint(0, len(studySet) - 1)

        # Use while loop to make it easier to manipulate how manny times this loops
        i = 0
        while(i < 10):
            os.system("clear")
            # Get selection
            selInd = randint(0, len(studySet[index]) - 1)
            print("\n\n\n           " + studySet[index][selInd] + "\n\n")

            # Get throw away input. The user will press enter to reveal answer.
            input("Press enter to reveal...")

            print("\n", end="")
            for word in studySet[index]:
                if(not word == studySet[index][selInd]):
                    print(word)

            # The user will press enter to continue to next item. If they type 'r', do
            # this same question again
            if(input("...") != "r"):
                # Use randint() to generate a random study word index ya know what im sayin
                index = randint(0, len(studySet) - 1)
                i += 1
        
        input("Press enter again to quit...")
        
        return 0
    except KeyboardInterrupt:
        print("\n")
        return 0

if(__name__ == "__main__"):
    exit(main())

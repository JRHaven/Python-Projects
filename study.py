'''
This file is under the MIT License.
Copyright 2024 Jeremiah Haven

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

This program is effectively a poor-man's Quizlet flashcards program with your own provided
flashcards, and relies on "set files". These files are config-file-esk but still somewhat
intuitive to put together. Here's an example:

setFile.txt
-----------
Question 1:Answer 1
Question 2:Answer 2
Question 3:Answer 3

Fairly basic here, each "flashcard" is on its own line, with the question and answer
seperated by a colon (and no spaces!)

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
    studySet = {}
    with open(filePath, 'r') as setFile:
        setFileConts = setFile.read()
        setFile.close()
    
    # For each line that has a ':' character, extrapolate based on that ':' character
    for i in setFileConts.split("\n"):
        if(":" in i):
            setItemEntry = i.split(":")
            studySet[setItemEntry[0]] = setItemEntry[1]

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
            print("\n\n\n           " + list(studySet.items())[index][0] + "\n\n")

            # Get throw away input. The user will press enter to reveal answer.
            input("Press enter to reveal...")

            print("\n" + list(studySet.items())[index][1])

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

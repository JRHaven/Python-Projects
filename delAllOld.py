#
# Deletes all files and directories in given directory that are older than 1 hr.
# Pefect for temp directories. Doesn't continuously run though, should probably
# be put in a crontab if that is the implementation you want.
#

# This script is under the MIT License.
#
# Copyright 2023 Jeremiah Havenn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
# associated documentation files (the "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial 
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os, time, sys, shutil

# Variable that will be set with what directory we will be working in
dir = ""

# Help screen
def help():
    print("""\
delAllOld: A program that pernamently deletes all files that are older than 1 hour!
Perfect for cleaning out a temp directory.

Basic usage:
--help  -h:     Show this help page
[Directory]:    Tells delAllOld which directory to delete files and
                directories from\
""")

# Argument Interpretation function
def args():
    # Use global variable dir
    global dir

    # Extrapolate directory. The directory should be given by an argument.
    # First check if there were any arguments passed to the script
    if(len(sys.argv) <= 1):
        # There were no arguments (other than the program being called itself)
        print("No argument was given. Please give the directory to delete as an argument.\n\nUse --help or -h \
more detailed information.")
        return 1
    
    # At the moment, the script only has 2 valid arguments: -h (or --help), and the actual directory.
    # I don't know if this script will ever have move arguments than that, but to futureproof, I will
    # do the following:
    #
    # Check if there is ever a help argument (-h or --help). If there is, do nothing other than print
    # the help screen using the help() function. If there is not a help argument, cycle through and find
    # a valid directory in the arguments. If we get to the end of the argument array, no valid directory
    # was found. Display error message and quit with an exit response of 1.
    if("-h" in sys.argv or "--help" in sys.argv):
        help()
        # Exit the function, but it should end entire script, not continuing on or treated as an error.
        return 2
    
    # Create directory variable
    dir = ""
    for i in sys.argv:
        if(os.path.isdir(i)):
            dir = i
            break
    
    # Check if there was a directory found
    if(dir == ""):
        print("No valid directory was supplied. Try again with a valid directory.")
        return 1
    
    # At this point, the function has run successfully
    return 0

# Function to get arrays of all files and directories that are more than 1 hr old
def getFilesToDelete():
    # Array
    allFiles = []

    # Gets last modified dates, as seconds from last epoch. Simply find difference between
    # that time and now (converting to int, we don't need to worry about decimals), and see
    # if the difference is more than 3600 (the amt of seconds in an hour).
    for i in os.listdir("."):
        # Skip . and ..
        if(i == "." or i == ".."):
            continue
        if(int(time.time()) - int(os.path.getmtime(i)) > 3600):
            allFiles.append(i)
    
    # If our array is empty, skip the rest. There's no need for it.
    if(len(allFiles) == 0):
        return ([], [])
    
    # Now split files and directories into different arrays. Deleting is different depending
    # on if it is a file or a directory, so this will be insanely helpful later.
    files = []
    dirs = []

    for i in allFiles:
        if(os.path.isdir(i)):
            dirs.append(i)
        else:
            files.append(i)
    
    # Return the 2 arrays packaged into one. Files is before Dirs. Should be unpacked into
    # two variables when the function is called.
    return(files, dirs)

# Main function for protection against importation
def main():
    # Use global variable dir
    global dir

    # Handle arguments. Will return a value of 1 if it encountered error, pass that
    # as main exit code
    argCode = args()
    if(argCode == 1):
        return 1
    elif(argCode == 2):
        return 0
    
    # Change into correct directory
    os.chdir(dir)

    # Build a list of files and directories to be deleted. This will be returned as (filesArr, dirsArr).
    # We will make use of Python's variable unpacking feature to accomplish this.
    files, dirs = getFilesToDelete()

    # Finally, delete! Files will use the os.remove() function, dirs will use os.rmdir().
    for i in files:
        os.remove(i)
    for i in dirs:
        shutil.rmtree(i)

    return 0

if(__name__ == "__main__"):
    exit(main())
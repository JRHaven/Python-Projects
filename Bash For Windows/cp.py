# cp is a basic script that copies a file

# Libraries
import filechk
import os

# Main Function. First checks if the file wanted exists
def copy(srcfile, dstfile):
    if(filechk.check(srcfile) == True):
        # Read the file, copy the contents to a new file, then changes the name and/or moves it to new directory
        source = open(srcfile, "r")
        copy = open(srcfile + " - copy", "w")
        copy.write(source.read())
        copy.close()
        source.close()
        copiedfile = srcfile + " - copy"
        os.rename(copiedfile, dstfile)
    else:
        print("cp: The file", srcfile, "does not exist so not copying!")
        

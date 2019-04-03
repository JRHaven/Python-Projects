import filechk
import os
def copy(srcfile, dstfile):
    if(filechk.check(srcfile) == True):
        source = open(srcfile, "r")
        copy = open(srcfile + " - copy", "w")
        copy.write(source.read())
        copy.close()
        source.close()
        copiedfile = srcfile + " - copy"
        os.rename(copiedfile, dstfile)
    else:
        print("cp: The file", srcfile, "does not exist so not copying!")
        

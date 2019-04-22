'''
This file is under the MIT License.

Copyright 2019 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
# theZipper is one of my proudest scripts made with Python. It simply zips up a folder.

# Libraries
import os
import zipfile
import tarfile
import platform
from time import sleep

# Define a clear function for cleaner code
def clear():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
        
# Zip a folder using .zip format
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            
# Zip a folder using the .tar.gz format
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
# Clear the screen then set some variables
clear()
zipmethod = ""
fol = ""

# Function to find which format to use based on platform
def find_platform():
    if(platform.system() == "Windows"):
        zipmethod = ".zip"
        return zipmethod
    elif(platform.system() == "Mac OS X"):
        zipmethod = input("Which format do you want to use? (type " + '"' +
                          ".zip" + '"' + " for compatibility with OS X and Linux,"
                          + "or " +'"' + ".tar.gz" + '"' + " for compatibility accross"
                          + "all platforms.) # ")
        return zipmethod
    else:
        zipmethod = input("Which format do you want to use? (type " + '"' +
                          ".zip" + '"' + " for compatibility with OS X and Linux,"
                          + "or " +'"' + ".tar.gz" + '"' + " for compatibility accross"
                          + "all platforms.) # ")
        return zipmethod

# Make the progress bar work better
def update_bar(lastdialogue):
    clear()
    print("theZipper is now zipping files...")
    print("")
    print(lastdialogue)
    
# Main function
def zipfol():
    lastdialogue = "0%... [                ] "
    
    # Go up a directory
    if(zipmethod == ".zip"):
        if(platform.system() == "Windows"):
            os.chdir(fol + "\..")
        else:
            os.chdir(fol + "/..")
        
        # Start zipping using a progress bar
        lastdialogue = "25%... [||||            ]"
        update_bar(lastdialogue)
        zipf = zipfile.ZipFile(zipnam + ".zip", 'w', zipfile.ZIP_DEFLATED)
        lastdialogue = "50%... [||||||||        ]"
        update_bar(lastdialogue)
        zipdir(folnam, zipf)
        lastdialogue = "75%... [||||||||||||    ]"
        update_bar(lastdialogue)
        zipf.close()
        lastdialogue = "100%... [||||||||||||||||]"
        update_bar(lastdialogue)
    else:
        if(platform.system() == "Windows"):
            os.chdir(fol + "\..")
        else:
            os.chdir(fol + "/..")
        lastdialogue = "50%... [|||||||||       ]"
        update_bar(lastdialogue)
        make_tarfile(zipnam + ".tar.gz", folnam)
        lastdialogue = "100%... [||||||||||||||||]"
        update_bar(lastdialogue)
        
# Execution ouside of the functions
print("Welcome to theZipper Zip Wizard!")
print("")
print("")
zipmethod = find_platform()

# Commented lines are for debugging purposes only
#print(platform.system())
#print(zipmethod)
clear()
print("theZipper Zip Wizard")
print("")
print("")
print("Create a directory then put all zipped files in there.")
sleep(5)
fol = input("Please copy and paste the full file path here. # ")
folnam = input("The folder name here.                          # ")
clear()
print("theZipper Zip Wizard")
print("")
print("")
zipnam = input("What is the name of your zip. Exclude file ending. # ")
clear()
print("theZipper is now zipping files...")
print("")
print("0%... ")
zipfol()
sleep(3)
print("")
print("")
print("")
print("All Done.")
exit()

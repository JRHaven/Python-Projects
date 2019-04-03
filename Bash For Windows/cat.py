import os
def show(file):
    if(os.path.exists(file) == False):
        print("cat: " + file + " file not found")
    else:
         show = open(file)
         print(show.read())
         show.close()

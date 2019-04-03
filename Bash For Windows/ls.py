from os import walk
import os
import glob
import systemvariables
def show():
    dir_list = os.listdir(os.getcwd())
    i = 0
    for dirs in dir_list:
        print(dir_list[i])
        i += 1
def list():
    theList = os.listdir(os.getcwd())
    return theList
def vars():
    print("usrsession:", systemvariables.usrsession)
    print("HOME:", systemvariables.HOME)
    print("ROOT:", systemvariables.ROOT)
    print("exepath:", systemvariables.exepath)
    print("USRDOCS:", systemvariables.USRDOCS)

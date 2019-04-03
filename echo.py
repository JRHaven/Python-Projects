import systemvariables
def reg(string):
    stringprt = string
    ifvar = False
    #print(stringprt.find("$", 0, 1))
    if(stringprt.find("$", 0, 1) == 0):
       ifvar = True
    else:
       ifvar = False
    if(ifvar == True):
        newstr = stringprt[1:]
        #print(newstr)
        if(((((newstr == "usrsession") or (newstr == "HOME")) or (newstr == "exepath")) or (newstr == "USRDOCS")) or (newstr == "ROOT")):
            #print("yes")
            if(newstr == "usrsession"):
                print(systemvariables.usrsession)
            elif(newstr == "HOME"):
                print(systemvariables.HOME)
            elif(newstr == "exepath"):
                print(systemvariables.exepath)
            elif(newstr == "USRDOCS"):
                print(systemvariables.USRDOCS)
            else:
                print(systemvariables.ROOT)
        else:
            print(string)
    else:
        print(string)

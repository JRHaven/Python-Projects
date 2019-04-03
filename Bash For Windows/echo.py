# echo is a basic script the either echos text given or outputs a variable

# Import the system variables (to output if asked to)
import systemvariables

# Main Function. Commented lines are for debugging purposes only. First set a couple of variables
def reg(string):
    stringprt = string
    ifvar = False
    #print(stringprt.find("$", 0, 1))
    
    # See if the first character of a string is a dollar sign, the symbol that declares the want of a
    # system variable
    if(stringprt.find("$", 0, 1) == 0):
       ifvar = True
    else:
       ifvar = False
    
    # If there is a dollar sign, find out what variable we want and print it out. If not, print out
    # inputted text
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

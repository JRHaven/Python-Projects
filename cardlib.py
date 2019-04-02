from sys import stdout
import clear, random
from time import sleep
def drawcrd(num, suite, amt):
    if((amt > 0) and (amt < 5)):
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("+-----------+ ")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            if(num[i-1] == "10"):
                stdout.write("|" + num[i-1] + "         | ")
            else:
                stdout.write("|" + num[i-1] + "          | ")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("|" + suite[i-1] + "          | ")
        stdout.write("\n")
        i = 0
    if((amt > 4) and (amt < 15)):
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("+---")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            if(num[i-1] == "10"):
                stdout.write("|" + num[i-1] + " ")
            else:
                stdout.write("|" + num[i-1] + "  ")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("|" + suite[i-1] + "  ")
        stdout.write("\n")
        i = 0
    if(amt > 14):
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("+--")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            if(num[i-1] == "10"):
                stdout.write("|" + num[i-1] + "")
            else:
                stdout.write("|" + num[i-1] + " ")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("|" + suite[i-1] + " ")
        stdout.write("\n")
        i = 0
def deal(maxcrds, nums, suites, speed):
    for i in range (1, maxcrds+1):
        clear.cs()
        drawcrd(nums, suites, i)
        sleep(speed)
def selection(amt):
        stdout.write("               ")
        if((amt > 0) and (amt < 5)):
           for i in range(1, amt+1):
               stdout.write("-------------")
           i = 0
           for i in range(1, amt):
               stdout.write("-")
           stdout.write("\n")
           stdout.write("                     ")
           i = 0
           for i in range(1, amt+1):
               stdout.write(str(i) + "             ")
           stdout.write("\n")
        if((amt > 4) and (amt < 15)):
           for i in range(1, amt+1):
               stdout.write("---")
           i = 0
           for i in range(1, amt+1):
               stdout.write("-")
           stdout.write("\n")
           stdout.write("                  ")
           i = 0
           for i in range(1, amt+1):
               if(i >= 10):
                   stdout.write(str(i) + "  ")
               else:
                   stdout.write(str(i) + "   ")
           stdout.write("\n")
        if(amt > 14):
           for i in range(1, amt+1):
               stdout.write("--")
           i = 0
           for i in range(1, amt+1):
               stdout.write("-")
           stdout.write("\n")
           stdout.write("               ")
           i = 0
           for i in range(1, amt+1):
               if(i >= 10):
                   stdout.write(str(i) + " ")
               else:
                   stdout.write(str(i) + "  ")
           stdout.write("\n")
def randomnums(amt):
    nums = []
    for i in range(1, amt+1):
        nums.append(str(random.randint(1, 10)))
    i = 0
    for i in range(1, amt+1):
        if(nums[i-1] == "1"):
            nums[i-1] = "A"
    i = 0
    for i in range(1, amt+1):
        if(random.randint(1, 11) == 11):
            thing = random.randint(1, 3)
            if(thing == 1):
                nums[i-1] = "J"
            elif(thing == 2):
                nums[i-1] = "Q"
            elif(thing == 3):
                nums[i-1] = "K"
    return nums
def randomnum():
    num = "A"
    num = str(random.randint(1, 10))
    if(num == "1"):
        num = "A"
    if(random.randint(1, 11) == 11):
        thing = random.randint(1, 3)
        if(thing == 1):
            num = "J"
        elif(thing == 2):
            num = "Q"
        elif(thing == 3):
            num = "K"
    return num
def randomsuites(amt):
    suites = []
    for i in range(1, amt+1):
        suites.append(random.randint(1, 4))
    i = 0
    for i in range(1, amt+1):
        if(suites[i-1] == 1):
            suites[i-1] = "H"
        elif(suites[i-1] == 2):
            suites[i-1] = "D"
        elif(suites[i-1] == 3):
            suites[i-1] = "C"
        elif(suites[i-1] == 4):
            suites[i-1] = "S"
    return suites
def randomsuite():
    suite = 1
    suite = random.randint(1, 4)
    i = 0
    if(suite == 1):
        suite = "H"
    elif(suite == 2):
        suite = "D"
    elif(suite == 3):
        suite = "C"
    elif(suite == 4):
        suite = "S"
    return suite

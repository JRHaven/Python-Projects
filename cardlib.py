# Cardlib: a library that shows ascci cards in a terminal

# The libraries we will need. The clear library is one that I made.
from sys import stdout
import clear, random
from time import sleep

# Display cards
def drawcrd(num, suite, amt):
    # If the amount of cards requested is less than 5, show full card with
    # one space in between each
    if((amt > 0) and (amt < 5)):
        stdout.write("               ")
        for i in range(1, amt+1):
            stdout.write("+-----------+ ")
        stdout.write("\n")
        i = 0
        stdout.write("               ")
        for i in range(1, amt+1):
            
            # Leave enough space for a 10 to fit and not ruin the display
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
        
    # If the amount of cards requested is between 5 and 14, show the number
    # and suite, one space, then start the next card
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
    
    # If there is 15 or more cards requested to show, collapse the cards asm
    # much as possible
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

# Show an animation for dealing
def deal(maxcrds, nums, suites, speed):
    for i in range (1, maxcrds+1):
        clear.cs()
        drawcrd(nums, suites, i)
        sleep(speed)

# Show an interface for choosing a card. Shows a list of numbers under the
# cards
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
        
# Generates a list of random numbers A-K then returns them to the script that
# imports the library. Does NOT act like a deck of cards. Does not keep track
# of what was taken and that there can only be up to 4 of a certin number.
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

# Generates 1 random number A-K and returns a string
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

# Like the randomnums library this returns a list of suites, using
# the first letter of it (e.g. Spades = S)
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

# Like randomnum but returns a suite
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

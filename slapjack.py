# Fun Game of Slap Jack!

'''
Copyright 2020-2023 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to 
deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
'''

import cardlib, keyboard, os
from clear import cs
from time import sleep
from random import randint

# The Game
def slapJack():
    # We must be run as root!
    if not os.geteuid() == 0:
        print("\nOnly root can run this script\n")
        exit(1)
    
    # Make sure there is indeed a jack that we can slap!
    while(True):
        # Use cardlib to create a set of 52 different random numbers, Jacks, Kings, and Queens
        deckCrdNums = cardlib.randomnums(52)

        # We have not discovered a Jack Yet.
        jacks = False

        # Record the number of Jacks
        numJacks = 0

        # Go through the numbers. If there is a jack, set a boolian, then add to the number
        # of Jacks
        for i in deckCrdNums:
            if(i == "J"):
                jacks = True
                numJacks += 1
        # If we found a Jack, don't try to generate a new set of numbers. If we didn't find
        # a Jack, do the whole thing over with a new set of random numbers.
        if(jacks == True):
            # If we have less then 3 Jacks, go through and randomly assign new jacks
            if(numJacks < 3):
                j = 0
                for i in deckCrdNums:
                    j += 1
                    if(j == 52):
                        break
                    if(i != "J"):
                        if(randint(1,18) == 1):
                            deckCrdNums[j] = "J"
                numJacks = 0
                for i in deckCrdNums:
                    if(i == "J"):
                        jacks = True
                        numJacks += 1
            break

    # Message and Difficulty selection
    print("Welcome to Slap Jack! To play this game, if a Jack appears, simply press the\n\
J button on your keyboard to \"Slap\" it! If you sucessfully slap a jack,\nyou will be\
awarded a point! What difficulty do you want?\n\nB: Beginner\nI: Intermediate\nA: Advanced\n\
E: Expert\nC: Custon\n\nThe difficulty you chose will determine the amount of time you see \
each card.\n")
    diff = input()

    # Set delay based on difficulty. If none entered, default to beginner difficulty.
    delay = 0
    if((diff == "b") or (diff == "B")):
        delay = 100
    elif((diff == "i") or (diff == "I")):
        delay = 70
    elif((diff == "a") or (diff == "A")):
        delay = 50
    elif((diff == "e") or (diff == "E")):
        delay = 30
    elif((diff == "c") or (diff == "C")):
        # Set a custom delay
        while(True):
            try:
                delay = int(input("Choose the number of Miliseconds between each card: "))
            except ValueError:
                print("That was not a real number. Try Again.")
                continue
            break
    else:
        print("No known difficulty was entered. Difficulty set to Beginner.")
        delay = 100
        sleep(3)
    score = 0

    # Main Game
    for i in deckCrdNums:
        # Clears the Screen
        cs()

        # Do a fancy display of the card using cardlib's built-in output generator thingy.
        # Input to it the current number, a random suite (suites don't matter in this game),
        # and the amount of cards to display, which is 1.
        cardlib.drawcrd([i], [cardlib.randomsuite()], 1)

        # Detection loop
        for j in range(1, (delay * 10)):
            # If the user hit the j key on their keyboard, do the following:
            if(keyboard.is_pressed("j")):
                # If a Jack is being shown, award a point
                if(i == "J"):
                    score += 1
                    cs()
                    print("Correct! Score", score)
                else: # If there isn't a Jack being shown, tell the user
                    cs()
                    print("Oops! Not a Jack!")
                
                # Regardless, wait 3 seconds before continuing, then go strait onto the
                # next card.
                sleep(3)
                break
            else:
                sleep(0.001)
    
    # Once the game is over, clear the screen and output a message based on what
    # score the player had, then exit peacfully.
    cs()
    if(score < 1):
        print("That was embarassing! You didn't slap a single Jack!\nBetter luck next time!")
    elif(score == 1):
        print("The Jacks must have been quick! Congratulations on slapping\nthe Jack you slapped!")
    else:
        print("Congratulations! You slapped", score, "Jacks! Nice!")
    exit(0)

# If the user hits Ctrl + C while playing, end the game.
try:
    slapJack()
except KeyboardInterrupt:
    cs()
    print("Thanks for Playing!")
    exit(0)

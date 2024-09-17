'''
Copyright 2024 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from random import randint

# Alphabet string constants to refrence
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SYMBOLS = "~`!@#$%^&*()-=_+[]\\{}|;\':\",./<>?"

# If this script is being used to generate passwords, use the following, more
# password friendly SYMBOLS constant by uncommenting it!
#SYMBOLS = "!@#&*=+:;,.?"

# Returns a random letter from ALPHABET constant
def randAlph():
    return ALPHABET[randint(0, len(ALPHABET)-1)]

# Returns a random symbol from SYMBOLS constant
def randSym():
    return SYMBOLS[randint(0, len(SYMBOLS)-1)]

def main():
    # Settings. Change these to your liking. Also feel free to use
    # random amounts
    numAlph = randint(5,8)
    numNums = randint(0,3)
    numSyms = 3

    # -----------------------
    #  END OF CONFIGURATIONS
    # -----------------------

    # Total chars constant - PLEASE NO TOUCHY TOUCHY!!!
    TOT_CHARS = numAlph + numNums + numSyms

    # Generator with result string
    result = ""
    for i in range(0, TOT_CHARS):
        # Use an infinate loop to ensure that we pick a mode that hasn't been
        # used yet
        while(True):
            mode = randint(0, 2)
            if(mode == 0 and numAlph > 0):
                result += randAlph()
                numAlph -= 1
                break
            elif(mode == 1 and numNums > 0):
                result += str(randint(0,9))
                numNums -= 1
                break
            elif(mode == 2 and numSyms > 0):
                result += randSym()
                numSyms -= 1
                break

    print("String with", TOT_CHARS, "chars:")
    print(result)
    
    return 0

if(__name__ == "__main__"):
    exit(main())

'''
Copyright 2019-2020 Jeremiah Haven

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
import os

# The string we will use to cipher and deciper info
alphabet = "a`~b8c$d+=.:|e#fgh!i0jk'l?mn/\^&()*o1,pq%[]{}rs-t@uvw4x_yz 2395670"

# Length of the string above
alphLen = len(alphabet) - 1

# Various Variables
reverse = ""
text = ""
buffer = ""
newText = ""
cipher = True
cipherInput = ""
outputFile = ""

# If we recieve keyboard interrupt, exit peacefully
try:
    # Keep asking for the file until they enter a file that exists
    while(True):
        file = input("Which File to cipher? ")
        if(os.path.exists(file) == True):
            break
        else:
            print("That doesn't exist.")
    
    # Cipher or Decipher
    cipherInput = input("Do you need to cipher or decipher the file? [C,d] ")
    if((cipherInput == "d") or (cipherInput == "D")):
        cipher = False
    outputFile = input("What is the file name of the output file? ")

    # Clear the screen. Only works in Unix or GNU/Linux based systems
    os.system("clear")

    # Start ciphering info if told to do so
    if(cipher == True):
        print("Ciphering file", file)

        # Get contents of input file into variable
        theFile = open(file, "r")
        text = str(theFile.read())
        theFile.close()

        # Make all the text lowercase
        text = text.lower()

        # Reverse Text
        for i in text:
            buffer = reverse
            reverse = i + buffer
        buffer = ""
        i = ""
        for i in reverse:
            j = i
            buffer = buffer + j
        reverse = buffer

        # Reset Variables
        buffer = ""
        j = ""
        k = []
        l = 0
        m = 0

        # Figure out string indexes of all characters
        for i in reverse:
            k.append(0)
            for j in alphabet:
                if(i == j):
                    k[l] = m
                    break
                m += 1
            l += 1
            m = 0
        l = 0
        m = 0
        n = 0

        # Cipher the data by shifting values by the same amount
        for m in k:
            n = k[l]
            n += 16
            while(n > alphLen):
                n -= alphLen
            k[l] = n
            l += 1
        l = 0
        m = 0
        n = 0

        # Reassign list of indexes to text
        for n in k:
            m = k[l]
            newText = newText + alphabet[m]
            l += 1

        # Write Finished Product to file
        theFile = open(outputFile, "w")
        theFile.write(newText)
        theFile.close()
        print("...Done!")
        exit(0)
    else:
        # Almost exact thing, but in a different order
        print("Deciphering file", file)
        theFile = open(file, "r")
        text = str(theFile.read())
        theFile.close()
        buffer = ""
        i = ""
        l = 0
        m = 0
        n = 0
        
        # Reverse
        for i in text:
            if(i == "\n"):
                continue
            j = i
            buffer = buffer + j
        text = buffer
        i = ""
        buffer = ""
        for i in text:
            buffer = reverse
            reverse = i + buffer
        text = reverse

        # Create array of indexes
        k = []
        l = 0
        m = 0
        for i in text:
            k.append(0)
            for j in alphabet:
                if(i == j):
                    k[l] = m
                    break
                m += 1
            l += 1
            m = 0
        l = 0
        m = 0
        n = 0

        # Shift values back to decipher text string
        for m in k:
            n = k[l]
            n -= 16
            while(n < 0):
                n += alphLen
            k[l] = n
            l += 1
        l = 0
        m = 0
        n = 0

        # Assign values to sting
        for n in k:
            m = k[l]
            newText = newText + alphabet[m]
            l += 1

        # Output to ew text
        theFile = open(outputFile, "w")
        theFile.write(newText)
        theFile.close()
        print("...Done!")
        exit(0)
except KeyboardInterrupt:
    # Exit Peacefully
    exit(0)

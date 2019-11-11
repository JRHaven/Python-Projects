'''
This script is under the MIT License.

Copyright 2019 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

// Use the gtts library to create the audio file
from gtts import gTTS

// Use the os library so that we can interact with the file
import os

// Get an input of the file from the user
file = input("Read from file: ")

// View the contents of the file with a variable
contents = open(file)

// Store the text of the file in this variable
say = contents.read()

// It takes a while for the audio file to be created. Infrom the end user
print("\nGenerating speech. Be patient. This could take a while...\n")

// Start generating the file. I assume that this is the english language
tts = gTTS(text=say, lang='en')

// File to save to
tts.save("text.mp3")

// Make sure the vlc media player isn't already running
os.system("killall cvlc")

// Play the file with the command line front of the vlc media player. Modify this file if
// you cannot use this command
os.system("mpv text.mp3")

// Delete the file
os.remove("text.mp3")

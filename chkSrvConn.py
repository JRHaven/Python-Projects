#!/usr/bin/python3

'''
Copyright 2025 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
'''

# chkSrvConn: Check if the Raspberry Pi Server is active
#
# Checks file containing the Pi's IP and pings it. If ping succeeds, execute script
# given in argument.

from sys import argv
from os import environ, system, path
from platform import system as platSys      # Use "as" keyword to avoid conflict from system module from os library
from re import match

def getScript():
    # Ensure we don't include python path or the command itself in our array
    args = []
    if((argv[0] == "python") or (argv[0] == "python3")):
        args = argv[2:]
    else:
        args = argv[1:]
    
    # Grab valid path. Checking that it's a script isn't necessary; sh will take
    # care of that
    for i in args:
        if(path.exists(i)):
            return i
    
    # No valid path found
    print("ERROR: No valid path to script found! There\'s nothing to do.")
    exit(1)

def getIPFile():
    # Constant for our file path. Detect KeyError if HOME variable doesn't exist for
    # whatever reason.
    try:
        IP_FILE_PATH = environ["HOME"] + "/srvip"
    except KeyError:
        print("ERROR: Couldn't find home path. Make sure that $HOME is set and try again.")
        exit(1)
    
    if(path.exists(IP_FILE_PATH)):
        return IP_FILE_PATH
    else:
        print("ERROR: Couldn't find server IP file.\nEnsure the server's IP address is at",
            IP_FILE_PATH, "and try again.")
        exit(1)

def getIPAddr(ipFilePath):
    # Grap IP file contents
    with open(ipFilePath, "r") as ipFile:
        ip = ipFile.read().strip()
        ipFile.close()

    # Check that it is a valid IP with regex pattern
    PATTERN = r"^(([0-9]{1}\.)|([0-9]{2}\.)|([0-1]{1}[0-9]{1}[0-9]{1}\.)|(2[0-5]{1}[0-5]{1}\.)|(2[0-4][0-9]\.)){3}(([0-9]{1})|([0-9]{2})|([0-1]{1}[0-9]{1}[0-9]{1})|(2[0-5]{1}[0-5]{1})|(2[0-4][0-9]))$"
    if(match(PATTERN, ip)):
        return ip
    else:
        print("ERROR: Invalid IP address!\nBe sure to follow the 255.255.255.255 ipv4 format. Ensure that the IP is the\nonly thing in the file.")
        exit(1)

def main():
    if(platSys() == "Linux"):
        scriptPath = getScript()
        ip = getIPAddr(getIPFile())
        
        # If a ping succeeds, run the script and return a 0 exit code
        if(system(f"ping {ip} -c 1 >> /dev/null") == 0):
            system(f"/bin/bash {scriptPath}")
            return 0
        else:
            # return a 1 exit code
            return 1
    else:
        print("ERROR: This script must run on Linux!")
        return 1

if(__name__ == "__main__"):
    exit(main())
#!/usr/bin/python3
'''
Copyright 2023 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os, time, platform, math

# Few Global Constants
SYSTEM_HOME = "/home/" + os.environ['USER'] + "/"
LAST_RUN_FILE = SYSTEM_HOME + ".pyLastRun"
LOCAL_TIME = time.localtime()
DAY = LOCAL_TIME.tm_mday
MON = LOCAL_TIME.tm_mon
YEAR = LOCAL_TIME.tm_year

def osChk():
    if(platform.system() != "Linux"):
        return False
    
    return True

def writeTimeStamp():
    with open(LAST_RUN_FILE, "w") as wFile:
        wFile.write(str(DAY) + ',' + str(MON) + ',' + str(YEAR))
        wFile.close()

# Function (look at all em arguments) to check things
def originalCheck(cWeek, lastYr, lastMon, lastWeek, lastDay, tYear, tMon, tWeek, tDay, modified=False, newMon=0, newDay=0):
    if(modified):
        mon = newMon
        day = newDay
    else:
        mon = MON
        day = DAY
    
    if(((YEAR - lastYr) >= tYear) and (tYear > 0)):
        return True
    if(((mon - lastMon) >= tMon) and (tMon > 0)):
        return True
    if(((cWeek - lastWeek) >= tWeek) and (tWeek > 0)):
        return True
    if(((day - lastDay) >= tDay) and (tDay > 0)):
        return True
    
    return False

def main():
    # ------- SET TARGET TIME -------
    # Target days, weeks, months, years
    # Example for 2 weeks:
    tDay = 0
    tWeek = 0
    tMon = 2
    tYear = 0

    # Ensure we are running Linux - that's the system this is designed to use
    if(not osChk()):
        print("ERROR: This system isn't running Linux! This cannot work on Windows, Mac, or Unix.")
        print("Quit!")
        return 1

    # Check if lastrun is availible. If not, create it! Initialize with our current values
    if(not os.path.exists(LAST_RUN_FILE)):
        writeTimeStamp()
        print("First run detected and initial timestamp has been written!")
        print("The timestamp has been written to", LAST_RUN_FILE, ". Delete this file if\nyou wish to reset things. Do not \
modify this file in any way - it will break this program!")
        return 0

    # Read the values stored in the file
    runFile = open(LAST_RUN_FILE, "r")
    runFileConts = runFile.read()
    runFile.close()

    # Process those values
    # We are expecting that the file hasn't been tampered with in this case.
    vals = runFileConts.split(",")

    # We do want to make sure these can be integers. If not, there has defelintly been tampering.
    try:
        lastDay = int(vals[0])
    except ValueError:
        print("ERROR: Could not convert day to int! Using today's date instead.")
        lastDay = DAY
    
    # Get weeks based on dividing days by 7 and rounding to the floor
    lastWeek = math.floor(lastDay / 7)
    # Also find current week
    cWeek = math.floor(DAY / 7)

    # Do the same for months and years that we did for days
    try:
        lastMon = int(vals[1])
    except ValueError:
        print("ERROR: Could not convert month to int! Using today's date instead.")
        lastMon = MON
    
    try:
        lastYr = int(vals[2])
    except ValueError:
        print("ERROR: Could not convert year to int! Using today's date instead.")
        lastYr = YEAR
    

    # Now compare! Create a cool variable to tell us if the task needs to be done!
    trigger = originalCheck(cWeek, lastYr, lastMon, lastWeek, lastDay, tYear, tMon, tWeek, tDay)
    
    # Couple extra checks. When it is the next year, month, the method above won't always be accurate.
    # Create a variable so that we don't have to recheck if we don't have to
    modified = False
    newMon = MON
    newDay = DAY
    if(YEAR > lastYr):
        # For all these, simply increment our current values the proper amount (to equal)
        newMon = MON + 12
        modified = True
    if(MON > lastMon):
        # Just using 4 here, as it is generally accurate. The week values are all approximate anyway.
        newWeek = cWeek + 4
        # Using 30 as a general number that *should* work the majority of the time
        newDay = DAY + 30
        modified = True
    
    if(modified):
        trigger = originalCheck(newWeek, lastYr, lastMon, lastWeek, lastDay, tYear, tMon, tWeek, tDay, True, newMon, newDay)

    # Finally, if our trigger has been triggered, give a cool display! Also need to reset our timestamp.
    if(trigger):
        print("!!!!! ALARM ALARM ALARM !!!!!")
        print("The scheduled thing! Do it!")
        writeTimeStamp()
    else:
        print("Not quite")

    return 0

if(__name__ == "__main__"):
    exit(main())
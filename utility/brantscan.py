from pathlib import *
from glob import *
from getopt import *
import os
import sys
import re

readable = r'.*(.txt|.nut)'
properties = r'.properties.(.*?)(\/|\)|\s|=)'
prefstring = r'(\[CREATURE:.*? MAN.*?\])'

# credit to stack overflow user monkut for the get_size method
def findlines(filepath, regex):
    validlines = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not(os.path.islink(fp)):
                try:
                    if(not re.match(readable, fp)):
                        continue
                    file = open(fp, "r", encoding="utf-8")
                    lines = file.readlines()
                    file.close()
                    # validlines.append([f])
                    for line in lines:
                        results = re.findall(regex, line)
                        if(results != []):
                            if(results not in validlines):
                                validlines.append(results) 
                except:
                    continue
    return validlines

found_dir = "NODIR"
dirspecified = False

if(len(sys.argv) > 0):
    for x in range(0, len(sys.argv)):
        if(sys.argv[x] == "-h"):
            print("Usage: scanfor.py [-h] -i <directory>\n-i is the directory flag\n-h is the help flag.")
            sys.exit(2)
        elif(sys.argv[x] == "-i"):
            if(x == len(sys.argv) - 1):
                print("Usage: scanfor.py [-h] -i <directory>")
                sys.exit(2)
            found_dir = sys.argv[x+1] 
            dirspecified = True
if(not dirspecified):
    print("Run scanfor.py -h for how to use this. No directory specified.")
    sys.exit(1)

#term = input("What term are you searching for:")

if(not os.path.isdir(found_dir)):
    print("Invalid directory")
    sys.exit(2)

masterlist = []
dirs = glob(found_dir + "/*/")
for x in range(0, len(dirs)):
    foundlines = findlines(dirs[x], prefstring)
    cleanedlist = []
    for entry in foundlines:
        for item in entry:
            if item not in cleanedlist:
                cleanedlist.append(item)
    print(dirs[x][len(found_dir):] + " : " + str(cleanedlist))
    for item in cleanedlist:
        print(item)
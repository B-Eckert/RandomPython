# Deletes annoying spaces from PDF formatting for ease of copying.
from functools import reduce
import os
import re


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'basefile/base_kamino_file.txt'), "r", encoding="utf-8")
base = file.read()
basecopy = base[:]
file.close()
clone_name = r"CT-\d\d\d\d"

def formatCloneNumber(x):
    if(x >= 1000):
        return str(x)
    elif(x >= 100):
        return "0" + str(x)
    elif(x >= 10):
        return "00" + str(x)
    else:
        return "000" + str(x)
for x in range(2, 99):
    basecopy += re.sub(clone_name, "CT-" + formatCloneNumber(x), base)
file = open(os.path.join(__location__, 'basefile/kamino_2.bin'), "w", encoding="utf-8")
file.write(basecopy)
file.close()
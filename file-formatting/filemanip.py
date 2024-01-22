# Deletes annoying spaces from PDF formatting for ease of copying.
from functools import reduce
import os

USE_EQUALS_FOR_NEWLINE = True
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'format.txt'), "r", encoding="utf-8")
n = file.readlines()
file.close()
def cat(a, b):
    a = a.replace("\n", "").replace("\t", "")
    b = b.replace("\n", "").replace("\t", "")
    return a + " " + b
vals = reduce(cat, n)
vals = vals.replace("   ", " ").replace("  ", " ")
if(USE_EQUALS_FOR_NEWLINE):
    vals = vals.replace("=", "\n")
print(vals)
file = open(os.path.join(__location__, 'format.txt'), "w", encoding="utf-8")
file.write(vals)
file.close()
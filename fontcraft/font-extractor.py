import os
import re
import sys
import codecs
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'unicode/mathematical.bold.script.txt'), "r", encoding="utf-8", errors="ignore")
n = file.readlines()
file.close()
"""
    Takes a text file in this folder with entries from the unicode database website and turns it into a dictionary indexed by the character
    the unicode character represents. Used for converting into different unicode fonts like fraktur, bold serif, etc.
"""

def wordToNumString(word):
    if(word == 'ONE'):
        return '1'
    elif(word == 'TWO'):
        return '2'
    elif(word == 'THREE'):
        return '3'
    elif(word == 'FOUR'):
        return '4'
    elif(word == 'FIVE'):
        return '5'
    elif(word == 'SIX'):
        return '6'
    elif(word == 'SEVEN'):
        return '7'
    elif(word == 'EIGHT'):
        return '8'
    elif(word == 'NINE'):
        return '9'
    elif(word == 'ZERO'):
        return '0'
    

#regex = r'(.*?);.*?(CAPITAL|SMALL|DIGIT|SIGN).*?([A-Z]|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|ZERO);(.*).*'
regex = r'(.*?);.*?(CAPITAL|SMALL|DIGIT|SIGN|HIEROGLYPH).*? (.*?);(.*).*'

tuples = []
pictographic = False
for line in n:
    matchObj = re.match(regex, line)
    symbol = matchObj.group(3)
    if matchObj.group(2) == 'SMALL':
        symbol = symbol.lower()
    elif(matchObj.group(2) == 'DIGIT'):
        symbol = wordToNumString(symbol)
    elif(matchObj.group(2) == 'SIGN' or matchObj.group(2) == 'HIEROGLYPH'):
        pictographic = True
    tuples.append((matchObj.group(1), symbol))
#print(tuples)
newFontDict = {}
for tuple in tuples:
    newFontDict[tuple[1]] = chr(int(tuple[0], 16))
print("Your font dictionary:")
print(newFontDict)
if pictographic:
    signList = []
    for tuple in tuples:
        signList += chr(int(tuple[0], 16))
    print("Your list of signs in this pictographic list:")
    print(signList)
import os
import re
# Used to turn the export file for the elite table into a list and then format that list properly.
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'events-meaningless.txt'), "r", encoding="utf-8", errors="ignore")
n = file.readlines()
file.close()
text = ""
patrol = r'.*[pP]atrol.*'
bandits = r'.*([Ll]ooters|[Bb]andit|[Rr]aiders).*'
for line in n:
    if not(re.match(patrol, line) or re.match(bandits, line)): #or re.match(bandits, line)
        text += line
print(text)
file = open(os.path.join(__location__, 'events-meaningful.txt'), "w", encoding="utf-8", errors="ignore")
file.write(text)
file.close()
import os
import re
# Used to turn the export file for the elite table into a list and then format that list properly.
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'dwarftext.txt'), "r", encoding="utf-8", errors="ignore")
n = file.readlines()
file.close()
text = ""
silver = r"\[color=silver\](.*?)\[\/color=silver\]"
for y in re.findall(silver, n):
    print(y)
    if (len(y[0]) > 40): #or re.match(bandits, line)
        text += y + "\n"
print(text)
file = open(os.path.join(__location__, 'extracted-info.txt'), "w", encoding="utf-8", errors="ignore")
file.write(text)
file.close()

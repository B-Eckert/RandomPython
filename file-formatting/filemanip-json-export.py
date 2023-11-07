import os
import re
# Used to turn the export file for the elite table into a list and then format that list properly.
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'file.json'), "r", encoding="utf-8", errors="ignore")
n = str(file.readlines())
file.close()
taglist = []
regex = r'("name":) "(.*?)"'
result = re.findall(regex, n)
for r in result:
    taglist.append(r[1])
for x in range(0, taglist.__len__()):
    taglist[x] = taglist[x].replace("\\", "")
    print(str(x) + ": " + taglist[x] + "\n")
print(taglist)
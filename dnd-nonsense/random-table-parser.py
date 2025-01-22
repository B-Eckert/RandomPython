import re
import os
import secrets


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

randomTableContent = open(__location__ + "/random-tables/random-tables-from-knave.txt",  "r", encoding="utf-8", errors="ignore").read()

tables = dict()
entries = re.findall(r"(([\w ]*)=(\n(\d+ ?[A-Za-z()-. ]+) ?(\d+ ?[A-Za-z()-. ]+))*)", randomTableContent)
for entry in entries:
    tableName = re.match(r"([A-Za-z()-. ]+)=", entry[0]).group(1).title()
    items = re.findall(r"(\d+) ?([A-Za-z()-. ]+)", entry[0])
    tables[tableName] = []
    print("Including table " + tableName + "...")
    for item in items:
        tables[tableName].append(item[1])

option = 0
while(option != -1):
    print("Choose a table to choose from or -1 for none...")
    index = 1
    keylist = []
    for key in tables.keys():
        print(str(index) + ") " + str(key))
        keylist.append(str(key))
        index += 1
    option = int(input())
    if(option != -1):
        print("Rolling on tablename: " + keylist[option-1])
        index = secrets.randbelow(len(tables[keylist[option-1]]))
        print(str(index+1) + ". " + tables[keylist[option-1]][index])
        input()
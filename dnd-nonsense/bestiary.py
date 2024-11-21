import json
import os
import d20
import re
from termcolor import colored

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Bestiary:   
    def __init__(self, books=[]):
        self.bookDict = {}
        self.masterMonsterList = []
        for titl in books:
            jsonContent = ""
            try:
                print("Book " + titl.upper() + " is loading...")
                jsonContent = open(__location__ + "/bestiary-jsons/bestiary-" + titl + ".json", "r", encoding="utf-8", errors="ignore").read()
            except:
                print("Book " + titl.upper() + " failed loading.")
            if(jsonContent != ""):
                self.bookDict[titl] = json.loads(jsonContent)
                self.masterMonsterList.extend(self.bookDict[titl]["monster"])
    def colorRoll(self, roll, color, props=[], total=True):
        return colored(str(d20.roll(roll).total) if total else str(d20.roll(roll)), color, attrs=props)
    def abilityExtract(self, ability, name=""):
        if(name != ""):
            print(colored(self.abilityExtract(name), attrs=["bold"]))
        def matchProcess(regex, string, function):
            matches = re.findall(regex, string)
            for m in matches:
                string = function(m, string)
            return string
        # Roll Info
        rollRegex = r"({@dice (.*?)})"
        def rollProcess(m, string):
            return string.replace(m[0], self.colorRoll(m[1], "green"))
        ability = matchProcess(rollRegex, ability, rollProcess)

        # Roll Info
        dmgRegex = r"({@damage (.*?)})"
        def dmgProcess(m, string):
            return string.replace(m[0], self.colorRoll(m[1], "red", total=False))
        ability = matchProcess(dmgRegex, ability, dmgProcess)
        
        # hit info
        hitRegex = r"({@hit ([0-9]*)})"
        def hitProcess(m, string):
            return string.replace(m[0], "+" + m[1] + " (" + self.colorRoll("d20+"+ m[1], "green") + ") to hit.")
        ability = matchProcess(hitRegex, ability, hitProcess)
        # on hit info
        onhitRegex = r"({@h})"
        def onhitProcess(m, string):
            return string.replace(m, "on hit ")
        ability = matchProcess(onhitRegex, ability, onhitProcess)
        
        # ranged/melee attack
        attackRegex = r"({@atk (mw|rw|mw,rw)})"
        def attackProcess(m, string):
            attackFlavor = ""
            if(m[1] == "mw"):
                attackFlavor = "Melee Attack:"
            elif(m[1] == "rw"):
                attackFlavor = "Ranged Attack:"
            elif(m[1] == "mw,rw"):
                attackFlavor = "Melee/Ranged Attack:"
            return string.replace(m[0], attackFlavor)
        ability = matchProcess(attackRegex, ability, attackProcess)
        
        # creature name
        creatureRegex = r"({@creature (.*?)})"
        def creatureProcess(m, string):
            return string.replace(m[0], colored(m[1].title(), "blue", attrs=["bold"]))
        ability = matchProcess(creatureRegex, ability, creatureProcess)
        
        # save dc
        dcRegex = r"({@dc ([0-9]*)})"
        def dcProcess(m, string):
            return string.replace(m[0], colored("DC " + m[1], "blue"))
        ability = matchProcess(dcRegex, ability, dcProcess)
        
        
        # recharge
        rechRegex = r"({@recharge ([0-9]*)})"
        def rechProcess(m, string):
            return string.replace(m[0], colored("(Recharge " + m[1] + ")", "light_magenta"))
        ability = matchProcess(rechRegex, ability, rechProcess)
        
        # condition
        conditionRegex = r"({@condition (.*?)})"
        def conditionProcess(m, string):
            return string.replace(m[0], colored(m[1].title(), "light_magenta"))
        ability = matchProcess(conditionRegex, ability, conditionProcess)
        
        # condition
        spellRegex = r"({@spell (.*?)})"
        def spellProcess(m, string):
            return string.replace(m[0], colored(m[1].title(), "cyan"))
        ability = matchProcess(spellRegex, ability, spellProcess)
        
        
        return ability
    def bestiarySearch(self, name):
        for entry in self.masterMonsterList:
            if(entry["name"] == name):
                return entry
    def useEconomy(self, entry, actionName, actionEconomy=""):
        actionKey = ""
        if(actionEconomy.upper() == "A"):
            actionKey = "action"
        elif(actionEconomy.upper() == "B"):
            actionKey = "bonus"
        elif(actionEconomy.upper() == "R"):
            actionKey = "reaction"
        elif(actionEconomy.upper() == "T"):
            actionKey = "trait"
        else:
            actionKey = "all"
        actions = []
        if(actionKey == "all"):
            if("action" in entry):
                actions.extend(entry["action"])
            if("bonus" in entry):
                actions.extend(entry["bonus"])
            if("reaction" in entry):
                actions.extend(entry["reaction"])
            if("trait" in entry):
                actions.extend(entry["trait"])
        else:
            if(actionKey in entry):
                actions = entry[actionKey]
        for econ in actions:
            if(econ["name"] == actionName):
                return self.abilityExtract(econ["entries"][0], econ["name"])
        return colored("No such ability found.", "red", attrs=["bold"])
                

b = Bestiary(["mm", "mtf", "vgm"])
monster = b.bestiarySearch("Mind Flayer")
print(b.useEconomy(monster, "Mind Blast {@recharge 5}"))
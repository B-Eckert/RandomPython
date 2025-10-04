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
            if(entry["name"].lower() == name.lower()):
                return entry
        return None
    def gatherActions(self, entry, actionEconomy=""):
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
        return actions
        
    def useEconomy(self, entry, actionName, actionEconomy=""):
        actions = self.gatherActions(entry, actionEconomy)
        for econ in actions:
            if(econ["name"] == actionName):
                return self.abilityExtract(econ["entries"][0], econ["name"])
        return colored("No such ability found.", "red", attrs=["bold"])
    
    def printUsageMenu(self, entry):
        usageOption = r"[ABRT]\d+"
        print(entry["name"], "\n------------------")
        traits = self.gatherActions(entry, "T")
        if(not len(traits) == 0):
            print("Traits\n------")
            for x in range(0, len(traits)):
                print(str(x+1) + ") " + traits[x]["name"])
            print("")
        actions = self.gatherActions(entry, "A")
        if(not len(actions) == 0):
            print("Actions\n-------")
            for x in range(0, len(actions)):
                print(str(x+1) + ") " + actions[x]["name"])
            print("")
        bonusActions = self.gatherActions(entry, "B")
        if(not len(bonusActions) == 0):
            print("Bonus Actions\n-------------")
            for x in range(0, len(bonusActions)):
                print(str(x+1) + ") " + bonusActions[x]["name"])
            print("")
        reactions = self.gatherActions(entry, "R")
        if(not len(reactions) == 0):
            print("Reactions\n---------")
            for x in range(0, len(reactions)):
                print(str(x+1) + ") " + reactions[x]["name"])
            print("")
    def selectFromUsageMenu(self, entry, input):
        usageOption = r"([ABRT])(\d+)"
        match = re.match(usageOption, input)
        if(match):
            actions = self.gatherActions(match.group(1))
            if(int(match.group(2)) > 0):
                pass                
        

b = Bestiary(["mm", "mtf", "vgm", "mme1", "mme2", "mme3"])
# monster = b.bestiarySearch("Mind Flayer")
monster = b.bestiarySearch("Maurezhi Lord")
searchRunning = False
# print(b.useEconomy(monster, "Mind Blast {@recharge 5}"))
b.printUsageMenu(monster)
while(searchRunning):
    # search loop
    creature = input("What is the creature you are looking for (Q to quit, I for index): ")    
    if(creature.lower() == "q"):
        searchRunning = False
    elif(creature.lower() == "i"):
        # run index functionality
        pass
    monster = b.bestiarySearch(creature)
    if(not b.bestiarySearch(creature)):
        print("That is not a valid creature, please search again.")
    else:
        actionsRunning = True
        while(actionsRunning):
            pass
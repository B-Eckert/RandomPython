import random
import math
from datetime import datetime

# TODO: Link the survival list and the other stuff to the World so you can algorithmically do the hunts.
# TODO: 
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
randomizer.seed(seed)
# CONSTANTS
mutationFactor = 5
speciesSensitivity = 2
breedMax = 4

statMax = 3
# New Gene Set:

# SPECIES SET
# Possible Allelles:
# Settings:
# Eats: Carnivore (0), Omnivore (1), Herbivore (2)
#   0 - Needs to fight to eat
#   1 - Can fight to eat if plants are low
#   2 - Must eat plants to eat
# 
# Plant food amt will be a set value.
# Stats: Stat total determines how much food a creature needs to survive a round.
# Combative Ability: Low (0), Medium (1), High (2) // When two animals fight, they roll contested combat checks, 1d3+COMBATIVE. Whoever rolls higher wins. Creatures are worth 
#                                               // their stat total amount of food.
# Scavenging: Low (0), Medium (1), High (2) // Ability to acquire food from the wilderness. Herbivores get 2*1d3+SCAV food. Omnivores get 1*1d3+SCAV food. Carn get 0.5*1d3+SCAV.
# Stealth: Low (0), Medium (1), High (2) // Ability to hide. Low-stealth creatures will be attacked by carnivores before high-stealth creatures.
#                                          // At start of 'hunting' phase, 1d3+stealth is rolled to determine stealth.
# Breeding: Low (0), Medium (1), High (2) // How many offspring they create. 2+breeding offspring are created when a pairing happens.
# Resourcefulness: Low (0), Medium (1), High (2) // Determines eating phase. Roll 1d3+RES to see what eating phasae they eat in. Also determines carnivores detecting stealth.

def speciesDict(settings, stats):
    return ({
        "Eats":settings[0]
    },
    {
        "Combative":stats[0],
        "Scavenging":stats[1],
        "Stealth":stats[2],
        "Breeding":stats[3],
        "Resourcefulness":stats[4]
    })

# Phases:
# 1: Breeding - New generation is born from the old. Pairings are made between animals of the same species. Species must be same to breed!
# 2-3: Scavenging phase 1/2
# Hunting Phase - Stealth is rolled and the carnivores hunt for other animals. Carnivores can eat animals in their perception bracket and randomly pick one.
# 3-4: Scavenging phase 3/4
# 5: Hunting Phase II - Stealth is rolled and the carnivores who are still hungry hunt for other animals.
# 6: Scavenging phase 5
# 7: Culling & mass death

# In this scenario we're setting up, all stats can vary between 1-20 (including brd, meaning that they can have at most 20 children)
class EcosystemSpecies:
    def __init__(self, settings, stats, name, parent):
        self.settings = settings
        self.stats = stats # stats will be a dictionary I think, iterate through keys.
        self.name = name
        self.pref = "a"
        self.parent = parent
    def incEvolutionPrefix(self):
        ordinator = ord(self.pref)+1
        if ordinator == 123:
            ordinator = 65
        if ordinator == 91:
            ordinator = 97
        self.pref = chr(ordinator)
    def histrionicString(self):
        if self.parent == None:
            return [self.name, self.name + ":" + str(self.stats) + ":" + str(self.settings)]
        return [self.parent.histrionicString()[0] + "->" + self.name, self.parent.histrionicString()[1] + "->" + self.name + ":" + str(self.stats) + ":" + str(self.settings)]
class EcosystemCreature:
    def __init__(self, settings, stats, parent, template):
        self.settings = settings
        self.stats = stats
        self.parent = parent
        self.template = template
        self.hunger = self.statTotal()+1
        self.sex = randomizer.randrange(0, 2) # 0 or 1, 1 = pp 0 = pp receptacle
    def determineNewSpecies(self):
        if self.template != None:
            difference = 0
            for x in self.stats:
                diff = self.stats[x] - self.template.stats[x]
                if diff < 0:
                    diff *= -1
                difference += diff
            if difference >= speciesSensitivity or self.settings['Eats'] != self.template.settings['Eats']:
                temp = EcosystemSpecies(self.settings, self.stats, self.template.name + self.template.pref, self.template)
                self.template.incEvolutionPrefix()
                self.template = temp
    def statTotal(self):
        sum = 0
        for x in self.stats:
            sum += self.stats[x]
        return sum
    def carcassValue(self):
        return self.statTotal()/(3-self.settings['Eats'])
    def satisfied(self):
        if self.hunger <= 0:
            return True
        return False
    def feed(self, num):
        
        self.hunger -= num
        if self.hunger <= 0:
            remainder = self.hunger * -1
            self.hunger = 0
            return remainder
        return 0
    def eatScav(self):
        scavCoef = 0
        if self.settings["Eats"] == 0:
            scavCoef = 0.25
        elif self.settings["Eats"] == 1:
            scavCoef = 0.5
        elif self.settings["Eats"] == 2:
            scavCoef = 1
        return self.scavNum()*scavCoef # how much food they want to eat
    def mutate(stats):
        newStats = {
            "Combative": stats["Combative"],
            "Scavenging": stats["Scavenging"],
            "Stealth": stats["Stealth"],
            "Breeding": stats["Breeding"],
            "Resourcefulness": stats["Resourcefulness"]
        }
        choice = random.choice(list(newStats.keys()))
        alter = randomizer.randrange(-1, 2)
        newStats[choice] += alter
        if newStats[choice] < 0:
            newStats[choice] = 0
        if newStats[choice] > statMax:
            newStats[choice] = statMax
        return newStats
    def fightNum(self):
        return randomizer.randrange(1, 4)+self.stats["Combative"]-self.settings['Eats']/2
    def stealthNum(self):
        return randomizer.randrange(1, 4)+self.stats["Stealth"]+self.settings['Eats']
    def resourceNum(self):
        return randomizer.randrange(1,4)+self.stats["Resourcefulness"]
    def scavNum(self):
        return randomizer.randrange(1,4)+self.stats["Scavenging"]
    def breedNum(self):
        return 1+self.stats["Breeding"]+self.settings['Eats']
    def children(self):
        kidList = []
        for x in range(self.breedNum()):
            randomTypeChange = randomizer.randrange(1, 101)
            settings = self.settings
            """            
            if(randomTypeChange > 90):
                newEats = settings['Eats'] + randomizer.randrange(-1, 2)
                if(newEats < 0):
                    newEats = 0
                elif(newEats > 2):
                    newEats = 2
                settings = {
                    'Eats':newEats
                }
            """
            child = EcosystemCreature(settings, EcosystemCreature.mutate(self.stats), self, self.template)
            child.determineNewSpecies()
            kidList.append(child)
        return kidList
    def printStats(self):
        return ("Species: " + self.template.name+"\nStats: " + str(self.stats)+"\nSettings: " + str(self.settings))
    def __str__(self):
        return self.printStats()
# 1: int, 2: pwr, 3: def, 4: mbl, 5: hp, 6: stl, 7: brd, 8: sz
# Rules:
# o Power can be at most 2x size
# o HP can be at most 5x size
# o Stealth can be at most 100-size
# [0,0,0,0,0]
# [1,1,1,1,1]

creatureList = []
for x in range(0, 6):
    dicts = speciesDict([0], [1,1,1,1,1])
    carnivoreSpawnling = EcosystemSpecies(dicts[0], dicts[1], "C", None)
    creatureList.append(EcosystemCreature(carnivoreSpawnling.settings, carnivoreSpawnling.stats, None, carnivoreSpawnling))
for x in range(0, 6):
    dicts = speciesDict([1], [1,1,1,1,1])
    omnivoreSpawnling = EcosystemSpecies(dicts[0], dicts[1], "O", None)
    creatureList.append(EcosystemCreature(omnivoreSpawnling.settings, omnivoreSpawnling.stats, None, omnivoreSpawnling))

for x in range(0, 6):
    dicts = speciesDict([2], [1,1,1,1,1])
    herbivoreSpawnling = EcosystemSpecies(dicts[0], dicts[1], "H", None)
    creatureList.append(EcosystemCreature(herbivoreSpawnling.settings, herbivoreSpawnling.stats, None, herbivoreSpawnling))

# SIMULATION CONSTANTS
time = 20
dumpy = ""
highestNumber = statMax + 3
defaultForage = 500
class World:
    def __init__(self, popcap):
        self.forage = 0
        self.popcap = popcap
        self.carcass = 0
        self.creatureList = []
        self.survivalList = []
    def feedingCapF(self, value):
        if(value > self.forage):
            self.forage = 0
            return self.forage
        else:
            self.forage -= value
            return value
    def feedingCapC(self, value):
        if(value > self.carcass):
            self.carcass = 0
            return self.carcass
        else:
            self.carcass -= value
            return value
    def carns(self, x):
        if(x.settings["Eats"] == 0):
            return True
        return False
    def huntingPhase(self):
        retStr = ""
        stealthList = blankCategories(highestNumber+2)
    # filter to carnivores
        
        carnivores = list(filter(self.carns, self.survivalList))
        # you cant eat someone of the same species so you cant eat yourself so its whatever
        for x in self.survivalList:
            stealthList[x.stealthNum()-1].append(x)
        neg = 0
        for x in range(0, carnivores.__len__()):
            if not carnivores[x-neg].satisfied():
                brackets = carnivores[x-neg].resourceNum()
                preyList = []
                for j in range(0, brackets):
                    preyList.extend(stealthList[j])
                def diffSpecies(y):
                    if carnivores[x-neg].template.name == y.template.name:
                        return False
                    if y in carnivores:
                        return False
                    return True
                preyList = list(filter(diffSpecies, preyList))
                if(preyList.__len__() == 0):
                    continue
                prey = random.choice(preyList)
                if(prey.settings['Eats'] == 0):
                    prey = random.choice(preyList)
                if(prey.fightNum() > carnivores[x-neg].fightNum()):
                    print(prey.template.name + " killed " + carnivores[x-neg].template.name + " in a hunt.")
                    retStr += prey.template.name + " killed " + carnivores[x-neg].template.name + " in a hunt\n"
                    # prey wins and kills carnivore
                    self.carcass += carnivores[x-neg].carcassValue()
                    ind = self.survivalList.index(carnivores[x-neg])
                    self.survivalList.remove(carnivores[x-neg])
                    for s in range(0, stealthList.__len__()):
                        if carnivores[x-neg] in stealthList[s]:
                            ind = stealthList[s].index(carnivores[x-neg])
                            stealthList[s].pop(ind)
                    carnivores.pop(x-neg)
                    neg += 1
                    
                else:
                    # carnivore wins and kills prey (meets beats)
                    print(carnivores[x-neg].template.name + " killed " + prey.template.name + " in a hunt.")
                    retStr +=  carnivores[x-neg].template.name + " killed " + prey.template.name + " in a hunt\n"
                    value = prey.carcassValue()
                    self.carcass += carnivores[x-neg].feed(value)
                    ind = self.survivalList.index(prey)
                    self.survivalList.pop(ind)
                    if prey in carnivores:
                        ind = carnivores.index(prey)
                        carnivores.pop(ind)
                        if(ind < x-neg):
                            neg += 1
                    for s in range(0, stealthList.__len__()):
                        if prey in stealthList[s]:
                            ind = stealthList[s].index(prey)
                            stealthList[s].pop(ind)
        return retStr
world = World(100)
world.creatureList = creatureList
# Phases:
# 1: Breeding - New generation is born from the old. Pairings are made between animals of the same species. Species must be same to breed!
# 2-3: Scavenging phase 1/2
# Hunting Phase - Stealth is rolled and the carnivores hunt for other animals. Carnivores can eat animals in their perception bracket and randomly pick one.
# 3-4: Scavenging phase 3/4
# 5: Hunting Phase II - Stealth is rolled and the carnivores who are still hungry hunt for other animals.
# 6: Scavenging phase 5

def invertIf(value):
    if(value < 0):
        value *= -1
        return value
    else:
        return 0
def feedingPhase(creature, world):
    if not creature.satisfied():
        scav = creature.eatScav()
        if(creature.settings['Eats'] == 2):
            edible = world.feedingCapF(scav)
            feedReturn = creature.feed(edible)
            world.forage += feedReturn
            # world.forage += creature.feed(world.feedingCapF(scav))
        elif(creature.settings['Eats'] == 1):
            if(world.forage >= world.carcass):
                edible = world.feedingCapF(scav)
                feedReturn = creature.feed(edible)
                world.forage += feedReturn
            else:
                edible = world.feedingCapC(scav)
                feedReturn = creature.feed(edible)
                world.carcass += feedReturn
        else:
            edible = world.feedingCapC(scav)
            feedReturn = creature.feed(edible)
            world.carcass += feedReturn
def blankCategories(number):
    n = []
    for x in range(0, number):
        n.append([])
    return n
for round in range(1, time+1):
    print("==========================[ROUND " + str(round) + "]===========================")
    dumpy += "==========================[ROUND " + str(round) + "]===========================\n"
    world.forage = defaultForage
    world.carcass = 0
    # Phase 1: Breeding
    world.survivalList = []
    for x in world.creatureList:
        for kid in x.children():
            world.survivalList.append(kid)
    # Phase 1a: Scavenging Initiative
    # survivalList = sorted(survivalList, key = lambda x : x.resourceNum())
    scavList = blankCategories(highestNumber)
    for x in world.survivalList:
        scavList[x.resourceNum()-1].append(x)
    # Phase 2: Scavenging phase 1/2
    for x in scavList[4]:
        feedingPhase(x, world)
    for x in scavList[4] + scavList[3]:
        feedingPhase(x, world)
    # Phase 3: Hunting Phase
    print("================1st Hunt================\n")
    dumpy += "================1st Hunt================\n"
    dumpy += world.huntingPhase()
        # filter out the species from the stealth brackets they can do and then kill fight, removing the victor from the survival list + stealth bracket and feeding the victor
    # Scavenging Phase 3/4
    for x in scavList[4] + scavList[3] + scavList[2]:
        feedingPhase(x, world)
    for x in scavList[4] + scavList[3] + scavList[2] + scavList[1]:
        feedingPhase(x, world)
    # Hunting Phase II
    print("================2nd Hunt================\n")
    dumpy += "================2nd Hunt================\n"
    dumpy += world.huntingPhase()
    # Scavenging Phase 5
    world.forage /= 2
    for x in scavList[4] + scavList[3] + scavList[2] + scavList[1] + scavList[0]:
        feedingPhase(x, world)
    # Final Phase: Starvation and Culling
    neg = 0
    for x in range(0, world.survivalList.__len__()):
        if not world.survivalList[x-neg].satisfied():
            print(world.survivalList[x-neg].template.name + " starved to death.")
            dumpy += world.survivalList[x-neg].template.name + " starved to death\n"
            world.survivalList.pop(x-neg)
            neg += 1
    """     
    if world.survivalList.__len__() > world.popcap:
        while world.survivalList.__len__() > world.popcap:
            thanos = random.choice(world.survivalList)
            print(thanos.template.name + " was snapped by Thanos")
            dumpy += thanos.template.name + " was snapped by Thanos\n"
            world.survivalList.remove(thanos)
    """
    world.creatureList = world.survivalList
    for x in world.creatureList:
        print(x.template.name + " survived.")
        dumpy += x.template.name + " survived.\n"
    print("Final food total: " + str(world.forage) + "," + str(world.carcass))
    print("Final pop total: " + str(world.creatureList.__len__()))
"""
for round in range(1, time+1):
    world.survivalList = []
    for x in creatureList:
        for kid in x.children():
            world.survivalList.append(kid)
    world.survivalList = sorted(world.survivalList, key = lambda x: x.evoStr(round))
    # For the cull index, we want the number of creatures on this island to stay around a certain number.
    # So basically if we have more than that number, we cut off at that number. Otherwise, 20%.
    cullIndex = int(world.survivalList.__len__() * 0.8)
    if world.survivalList.__len__() - cullIndex < world.survivalList.__len__() - popSize:
        cullIndex = popSize
    # Printing nonsense
    world.survivalList = world.survivalList[-1*cullIndex:]
    print("\nGeneration", round, "Ten Most Powerful (Pop:", world.survivalList.__len__(), ")")
    dumpy += "\nGeneration " + str(round) + " Ten Most Powerful (Pop: " + str(world.survivalList.__len__()) + ")\n"
    for x in world.survivalList[-10:]:
        print(x.printStats())
        dumpy += x.printStats() + "\n"
        print("Strength:", x.evoStr(round))
        dumpy += "Strength: " + str(x.evoStr(round)) + "\n"
    creatureList = world.survivalList
"""
dumpy += "===============================\nFinal Surviving Species\n"
for x in world.creatureList:
    dumpy += x.printStats() + "\n"
if(world.creatureList.__len__() > 0):
    dumpy += "=======================\nGeneology of Random\n"
    print(world.creatureList[-1].template.histrionicString()[0], "\n" + world.creatureList[-1].template.histrionicString()[1])
    dumpy += world.creatureList[-1].template.histrionicString()[0] + "\n" + world.creatureList[-1].template.histrionicString()[1]
file = open("dumpy.txt", "w")
file.write(dumpy)
file.close()
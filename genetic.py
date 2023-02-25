import random
from datetime import datetime
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
randomizer.seed(seed)
# CONSTANTS
mutationFactor = 6
speciesSensitivity = 15
breedMax = 4
intelligenceHandicap = 10
# In this scenario we're setting up, all stats can vary between 1-20 (including brd, meaning that they can have at most 20 children)
class SpeciesTemplate:
    def __init__(self, statList, name, parent):
        self.stats = statList
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
            return [self.name, self.name + ":" + str(self.stats)]
        return [self.parent.histrionicString()[0] + "->" + self.name, self.parent.histrionicString()[1] + "->" + self.name + ":" + str(self.stats)]

class Creature:
    def __init__(self, statList, parent, template):
        self.stats = statList
        self.parent = parent
        self.template = template
    def determineNewSpecies(self):
        if self.template != None:
            difference = 0
            for x in range(self.stats.__len__()):
                diff = self.stats[x] - self.template.stats[x]
                if diff < 0:
                    diff *= -1
                difference += diff
            if difference >= speciesSensitivity*mutationFactor:
                temp = SpeciesTemplate(self.stats, self.template.name + self.template.pref, self.template)
                self.template.incEvolutionPrefix()
                self.template = temp
    def mutate(stats):
        newStats = []
        for stat in stats:
            newStat = stat + randomizer.randrange(-1*mutationFactor, mutationFactor+1)
            if newStat <= 0:
                newStat = 1
            newStats.append(newStat)
        # Rules for evolution
        # 10 is the ideal size for smart people
        if newStats[0] > newStats[7]*3:
            newStats[0] = newStats[7]*3
        if newStats[0] <= 10 and newStats[0] > newStats[7]*4:
            newStats[0] = newStats[7]*4
        elif newStats[0] > 10 and newStats[0] > 400/newStats[7]:
            newStats[0] = int(400/newStats[7])
        if newStats[1] > newStats[7]*4:
            newStats[1] = newStats[7]*4
        if newStats[2] > newStats[7]*3:
            newStats[2] = newStats[7]*3
        if newStats[3] > 100/newStats[7]:
            newStats[3] = int(100/newStats[7])
        if newStats[4] > newStats[7]*5:
            newStats[4] = newStats[7]*5
        if newStats[5] > 100/newStats[7]:
            newStats[5] = int(100/newStats[7])
        if newStats[6] > breedMax:
            newStats[6] = breedMax
        # Rules for evolution done.
        return newStats
    def evoStr(self, roundNum):
        # This takes all these numbers and calculates it into an "Evolutionary Strength"
        # This will determine how strongly things are weighted against each other in order to determine if a creature survives a wave or not.
        # Weakest 20% of creatures will die off every cycle.
        strength = 0
        # 1: Intelligence - int * roundNum/10
        strength += self.stats[0] * (roundNum/intelligenceHandicap)
        # 2: Power - Power is multiplied by a tenth of the size
        strength += self.stats[1]*(self.stats[7]/10)
        # 3/4: Defense/Mobility - def / mbl depending on which is bigger.
        if self.stats[2] > self.stats[3]:
            strength += self.stats[2]
        else:
            strength += self.stats[3]
        # 5: HP - HP/3 is added directly. Harder to grow.
        strength += (self.stats[4]/3)*(self.stats[2]/8)
        # 6: Stealth - (mbl/8) * stealth - Stealth busted, needs a rework
        strength += ((self.stats[3]/15)*(self.stats[5]/2))
        # 7: Breeding - Doesn't matter
        # 8: Size - Divides the whole number. The game is getting big numbers and also being as efficient as possible.
        if self.stats[7]/9 > 1:
            strength /= (self.stats[7]/9)
        return int(strength)
    def children(self):
        kidList = []
        for x in range(randomizer.randrange(1, self.stats[6]+1)):
            child = Creature(Creature.mutate(self.stats), self, self.template)
            child.determineNewSpecies()
            kidList.append(child)
        return kidList
    def printStats(self):
        return ("Species: " + self.template.name+"\nStats: " + str(self.stats))

# 1: int, 2: pwr, 3: def, 4: mbl, 5: hp, 6: stl, 7: brd, 8: sz
# Rules:
# o Power can be at most 2x size
# o HP can be at most 5x size
# o Stealth can be at most 100-size
spawnling = SpeciesTemplate([1, 1, 1, 1, 1, 1, 2, 1], "S", None)
creatureList = []
for x in range(0, 11):
    creatureList.append(Creature(spawnling.stats, None, spawnling))

# SIMULATION CONSTANTS
time = 200
popSize = 1000
dumpy = ""

for round in range(1, time+1):
    survivalList = []
    for x in creatureList:
        for kid in x.children():
            survivalList.append(kid)
    survivalList = sorted(survivalList, key = lambda x: x.evoStr(round))
    # For the cull index, we want the number of creatures on this island to stay around a certain number.
    # So basically if we have more than that number, we cut off at that number. Otherwise, 20%.
    cullIndex = int(survivalList.__len__() * 0.8)
    if survivalList.__len__() - cullIndex < survivalList.__len__() - popSize:
        cullIndex = popSize
    # Printing nonsense
    survivalList = survivalList[-1*cullIndex:]
    print("\nGeneration", round, "Ten Most Powerful (Pop:", survivalList.__len__(), ")")
    dumpy += "\nGeneration " + str(round) + " Ten Most Powerful (Pop: " + str(survivalList.__len__()) + ")\n"
    for x in survivalList[-10:]:
        print(x.printStats())
        dumpy += x.printStats() + "\n"
        print("Strength:", x.evoStr(round))
        dumpy += "Strength: " + str(x.evoStr(round)) + "\n"
    creatureList = survivalList
dumpy += "===============================\nFinal Surviving Species\n"
for x in survivalList:
    dumpy += x.printStats() + "\n"
    dumpy += "Strength: " + str(x.evoStr(round)) + "\n"
dumpy += "=======================\nGeneology of Strongest\n"
print(survivalList[-1].template.histrionicString()[0], "\n" + survivalList[-1].template.histrionicString()[1])
dumpy += survivalList[-1].template.histrionicString()[0] + "\n" + survivalList[-1].template.histrionicString()[1]

file = open("dumpy.txt", "w")
file.write(dumpy)
file.close()
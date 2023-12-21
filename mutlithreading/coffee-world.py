import threading
import time
from typing import List
import sys
"""
The class that directs coffee machine logic.
"""
class CoffeeMachine:
    def __init__(self, name, grains=60, water=100): # The "grains" is how much weariness a cup of this coffee will restore. A cup of coffee consumes 10 water.
        self.name = name
        self.grains = grains
        self.water = water
        self.waterLock = threading.Lock()
        self.waterCheckLock = threading.Lock()
        self.beingUsed = False
        self.usedLock = threading.Lock()
    def oneCup(self, callback):
        with self.usedLock:
            self.beingUsed = True
        with self.waterLock:
            print("Coffee is being made at machine", self.name, "\b...")
            time.sleep(2)
            with self.waterCheckLock:
                self.water -= 10
                if(self.water <= 0):
                    print("[OUT OF WATER:", self.name, "\b]")
            print("Coffee is done at machine", self.name, "\b.")
        with self.usedLock:
            self.beingUsed = False
        callback(self.grains)
    def isUsed(self):
        with self.waterCheckLock:
            if(self.water <= 0):
                return True
        with self.usedLock:
            return self.beingUsed
    
""" 
The class that directs coffee drinker logic.
"""
class CoffeeDrinker:
    def __init__(self, name, initWeariness=50, coffeePoint=30, wearinessDecay=10):
        self.name = name
        self.weariness = initWeariness
        self.wearinessLock = threading.Lock()
        self.wearinessDecay = wearinessDecay # Every tick weariness will be reduced.
        self.coffeePoint = coffeePoint # The point at whence they go to get coffee
    def readyForCoffee(self):
        if(self.weariness <= self.coffeePoint):
            print(self.name, "is ready for coffee.")
        return self.weariness <= self.coffeePoint
    def coffeeTick(self):
        print(self.name, "is at", self.weariness, "weariness.")
        self.weariness -= self.wearinessDecay
    def caffienate(self, value):
        print(self.name, "is caffeinated for", value)
        with self.wearinessLock:
            self.weariness += value


"""
The class that directs the world logic.
"""
class World:
    def __init__(self, drinkers:List[CoffeeDrinker], machines:List[CoffeeMachine]):
        self.drinkers = drinkers
        self.machines = machines
    def validCoffeeMachine(self):
        for index in range(self.machines.__len__()):
            if(not self.machines[index].isUsed()):
                return (True, index)
        return (False, 0)
    def engageCoffeeThread(self, index, callback):
        return threading.Thread(target=self.machines[index].oneCup, args=[callback], daemon=True)
    def drinkerThread(self, drinker: CoffeeDrinker):
        while(drinker.weariness > 0):
            time.sleep(1)
            drinker.coffeeTick()
            if(drinker.readyForCoffee()):
                cofMach = self.validCoffeeMachine()
                if(cofMach[0]):
                    machineThread = self.engageCoffeeThread(cofMach[1], drinker.caffienate)
                    machineThread.start()
        print("Coffee drinker", drinker.name, "died.")
    def startThreads(self):
        for drinker in drinkers:
            print("Drinker " + drinker.name + " initialized...")
            threading.Thread(target=self.drinkerThread, args=[drinker], daemon=True).start()
        #print("Did the loop finish?")
        time.sleep(60)
        sys.exit(0)

# Each thread will be "Directed" by one coffee drinker who drinks from the same coffee machine. They will have to wait for each other's coffee to be ready.
# Very dramatically, if they don't get their coffee by the time their weariness decays to 0, they die.


drinkers = [CoffeeDrinker("Brant Eckert"), 
            CoffeeDrinker("Patrick", initWeariness=100, wearinessDecay=5, coffeePoint=20), 
            CoffeeDrinker("Charles", initWeariness=100, coffeePoint=40, wearinessDecay=15),
            CoffeeDrinker("Jenna", initWeariness=50, coffeePoint=70, wearinessDecay=15)]
machines = [CoffeeMachine("My Beloved [Strong]"), CoffeeMachine("My Dear [Weak]", grains=30)]
world = World(drinkers, machines)

world.startThreads()

import random
from datetime import datetime
class Dice:
    def __init__(self):
        self.rand = random.Random()
        seed = datetime.now().microsecond * datetime.now().second
        self.rand.seed(seed)
    def r(self, face, modifier=0):
        return self.rand.randrange(1, face+1)+modifier
    def roll(self, face, number = 1, advantage = 0, modifier = 0):
        sum = 0
        for x in range(0, number):
            rolls = [self.r(face)]
            if(advantage == 0):
                sum += rolls[0]
            elif(advantage > 0):
                adv = advantage
                while adv != 1:
                    rolls.append(self.r(face))
                    adv -= 1
                sum += max(rolls)
            elif(advantage < 0):
                adv = advantage
                while adv != -1:
                    rolls.append(self.r(face))
                    adv += 1
                sum += min(rolls)
        return sum + modifier
    # These rolls are for context highlighting, roll and r are if we only care about the output value and nothing else.
    def rollA(self, face, advantage, modifier=0):
        rolls = [self.r(face), self.r(face)]
        if advantage == True:
            return [rolls, max(rolls)+modifier]
        else:
            return [rolls, min(rolls)+modifier]
    def rollM(self, number, face, modifier = 0):
        set = []
        for x in range(0, number):
            set.append(self.r(face))
        return [set, sum(set)+modifier] # returns the set of numbers, then the actual number in the second field. roll[1] is what you want.
    
dice = Dice()

print(dice.roll(8, 3))

# Just gonna leave this as is and use the D20 library for further mutability w/ strings
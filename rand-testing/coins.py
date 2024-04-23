import random
from datetime import datetime
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)

def coin():
    return randomizer.randrange(0, 2)
def manycoin(n):
    result = [0, 0]
    for x in range(n):
        co = coin()
        if(co == 0):
            result[0] += 1
        else:
            result[1] += 1
    return result

print('Number of Coins')
num = int(input())
res = manycoin(num)
print(str(res[0]) + " (" + str((res[0]/num)*100) + "%) Tails, " + str(res[1]) + " (" + str((res[1]/num)*100) + "%) Heads.")

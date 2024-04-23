import random
from datetime import datetime
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)

def dice(num, face):
    summ = 0
    for i in range(num):
        summ += randomizer.randrange(1, face+1)
    return summ

print('Dice face.')
face = int(input())
print('Dice number')
num = int(input())
avg = int((face/2)+1)
print('Con Bonus')
con = int(input())

total = 0
for i in range(num):
    d = dice(1, face)
    if i == 0:
        total += face+con
    elif d > avg:
        total += d+con
    else:
        total += avg+con

print("HP Total: ", total)

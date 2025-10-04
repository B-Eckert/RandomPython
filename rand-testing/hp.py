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
print('Take average if roll under average? (y/n)')
avgInput = input()
if(avgInput.lower() == 'y'):
    avg = int((face/2)+1)
else:
    avg = 0

connector = "+"
hpLog = "("

total = 0
for i in range(num):
    d = dice(1, face)
    if i == 0:
        total += face+con
        hpLog += str(face) + connector
    elif d > avg:
        total += d+con
        hpLog += str(d) + connector
    else:
        total += avg+con
        hpLog += str(avg) + connector

if(num > 1):
    hpLog = hpLog[:(-1 * len(connector))] + ") + " + str(con*num) + " = " + str(total)
else:
    hpLog += " ) + 0 = 0"
print("HP Total: " + str(total))
print("HP Log: " + hpLog)

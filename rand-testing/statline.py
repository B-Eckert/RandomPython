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
    for y in range(num):
        del y
        summ += randomizer.randrange(1, face+1)
    return summ

def fourdsixkeephighest():
    z = []
    for y in range(4):
        del y
        z.append(dice(1, 6))
    z.remove(min(z))
    summ = 0
    for y in z:
        summ += y
    return summ

iters = 0
enough = False
while enough is False:
    total = 0
    for i in range(6):
        x.append(fourdsixkeephighest())
        total += x[i]
    if(total >= threshhold):
        print("It took ", iters, " tries.")
        enough = True
    else:
        print("Bad Sum: ", total)
        if(total < 60):
            print("=============")
            for i in range(6):
                print("Bad Number ", i+1, ": ", x[i])
            print("=============")
        iters+=1
        x.clear()
x.sort(reverse=True)
for i in range(6):
    print("Number ", i+1, ": ", x[i])
print("=============")
print("Sum: ", total)

print("Extras [d20]:", dice(1,20), dice(1,20))
print("Extras [4d6kh3]: ", fourdsixkeephighest(), fourdsixkeephighest())
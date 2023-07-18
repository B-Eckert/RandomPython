import random
from datetime import datetime
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)

def dice(num, face):
    sum = 0
    for i in range(num):
        sum += randomizer.randrange(1, face+1)
    return sum

def fourdsixkeephighest():
    z = []
    for i in range(4):
        z.append(dice(1, 6))
    z.remove(min(z))
    sum = 0
    for i in z:
        sum += i
    return sum

iters = 0
enough = False
while enough == False:
    sum = 0
    for i in range(6):
        x.append(fourdsixkeephighest())
        sum += x[i]
    if(sum >= threshhold):
        print("It took ", iters, " tries.")
        enough = True
    else:
        print("Bad Sum: ", sum)
        if(sum < 60):
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
print("Sum: ", sum)

print("Extras [d20]:", dice(1,20), dice(1,20))
print("Extras [4d6kh3]: ", fourdsixkeephighest(), fourdsixkeephighest())
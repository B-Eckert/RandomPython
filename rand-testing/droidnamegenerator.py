import random
from datetime import datetime
threshhold = 72
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)

affixes = [[
    "OOM", "OOM", "OOM", "RB"
],
    ["SRB"],
    ["XRB"],
    ["TX"],
    ["SDF"],
    ["DXE"]
]

option = 0
while(option != -1):
    print("-1 to quit")
    print("Choose which type of battle droid to generate a name for.\n1: B1\n2: B2\n3: BX\n4: Tactical Droid\n5: Dwarf Spider Droid\n6: Destroyer Droid")
    option = int(input())
    if(option != -1):
        option -= 1
        number = int(input("How many: "))
        for x in range(0, number):
            name = affixes[option][randomizer.randrange(0, len(affixes[option]))]
            name += "-" + str(randomizer.randrange(1, 1000))
            print(name)
        input()

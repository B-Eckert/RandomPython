z = [1,2,3]
for x in range(0, z.__len__()-1):
    for y in range(x+1, z.__len__()):
        print(z[x], ":",z[y])
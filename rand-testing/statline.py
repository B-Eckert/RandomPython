import secrets
threshhold = 72
midness_range = 4
midness_acceptable_max = 17
x = []

def dice(num, face):
    summ = 0
    for y in range(num):
        del y
        summ += secrets.randbelow(face)+1
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

def midstatline(statline):
    # I define a "mid" statline as a statline where all the numbers are only 2-4 points distant
    if(max(statline) - min(statline) < midness_range and max(statline) < midness_acceptable_max):
        return True
    return False

iters = 0
enough = False
while enough is False:
    total = 0
    for i in range(6):
        x.append(fourdsixkeephighest())
        total += x[i]
    if(total >= threshhold and not midstatline(x)):
        print("It took ", iters, " tries.")
        enough = True
    elif(midstatline(x) and total >= threshhold):
        print("Statline was mid. Biggest number was:", max(x), "| Smallest number was:", min(x),"| Total was:", total)
        iters += 1
        x.clear()
    else:
        print("Bad Sum: ", total)
        if(total < 60):
            print("===============")
            for i in range(6):
                print("Bad Number ", i+1, ": ", x[i])
            print("===============")
        iters+=1
        x.clear()
x.sort(reverse=True)
for i in range(6):
    print("Number ", i+1, ": ", x[i])
print("===============")
print("Sum: ", total)

print("Extras [d20]:", dice(1,20), dice(1,20))
print("Extras [4d6kh3]: ", fourdsixkeephighest(), fourdsixkeephighest())
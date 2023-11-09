def scientific(x):
    exponent = 0
    original = x
    if(x == 0):
        exponent = 0
    elif(x < 1):
        while(x < 1):
            x*=10
            exponent -= 1
        return [x, exponent]
    else:
        while(x >= 10):
            x/=10
            exponent+=1
    return [x, exponent, original]
def writeScientific(sciPair):
    if(sciPair[1] > -1 & sciPair[1] <= 3):
        return str(sciPair[2])
    else:
        return str(sciPair[0])+"x10^"+str(sciPair[1])

def wrtSci(x):
    return writeScientific(scientific(x))

writeScientific(scientific(100))


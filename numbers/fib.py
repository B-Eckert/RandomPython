import scientific as sci
# If a fibonacci number's index divides another fibonacci number's index, then the fibonacci numbers are divisible.
fibNums = [1, 1]
for i in range(2,10000):
    fibNums.append(fibNums[i-1]+fibNums[i-2])
for i in range(2, fibNums.__len__()):
    for j in range(i+1, fibNums.__len__()):
        if((j+1) % (i+1) == 0):
            if(fibNums[j] % fibNums[i] == 0):
                # print("It holds. Indices ", j+1, ":", i+1, ":", int((j+1)/(i+1))," result in ", sci.wrtSci(fibNums[j]), " and ", sci.wrtSci(fibNums[i]), " which divide to ", sci.wrtSci(int(fibNums[j]/fibNums[i])))
                pass
                if(int(fibNums[j]//fibNums[i])-fibNums[j-i] in fibNums):
                    # print("Is in.")
                    pass
            else:
                print("It does not hold. Indices ", j+1, ":", i+1, ":", int((j+1)/(i+1)), "result in ", fibNums[j], " and ", fibNums[i], " which divide to ", sci.wrtSci(float(fibNums[j])/float(fibNums[i])))
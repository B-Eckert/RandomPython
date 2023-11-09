def commasFunction(number):
    numstr = str(number)
    if(numstr.__len__() <= 3):
        print(number)
    else:
        commastr = ""
        while(numstr.__len__() > 3):
            commastr = "," + numstr[-3:] + commastr
            numstr = numstr[0:-3]
        commastr = numstr + commastr
        return commastr

num = 0
while(num != -1):
    print("Enter the number to add commas to or -1 to exit.")
    num = int(input())
    if(num != -1):
        print(commasFunction(num))

def fib(initial, previous, numberOfThem):
    if(numberOfThem != 0):
        if(initial == 0):
            print(0)
            numberOfThem -= 1
        if(initial == 0 and previous == 1):
            print(1)
            numberOfThem -= 1
        print(initial+previous)
        return fib(previous, initial+previous, numberOfThem-1)
fib(0, 1, 100)
points = 70
stats = [8,8,8,8,8]
cost = [1,1,1,1,1]

option = 0
increasePoints = int(input("How many ASIs do you have? "))
points += 5 * increasePoints
while(option != -1):
    print("========[-1 to quit, *10 to revert]=========")
    print("Point Total:", points, "\n1: Body:", stats[0], "\n2: Quik:", stats[1], "\n3: Perc:", stats[2], "\n4: Mind:", stats[3],"\n5: Pers:", stats[4])
    option = int(input("What do you want to increase? "))
    if(option != -1):
        if(option >= 1 and option <= 5):
            option -= 1
            points -= cost[option]
            cost[option] += 1
            stats[option] += 1
        elif(option >= 10 and option <= 50):
            option = int(option/10) - 1
            cost[option] -= 1
            stats[option] -= 1
            points += cost[option]
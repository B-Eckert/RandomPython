import threading
import math
from typing import List
import secrets
import re

# Notes: Each 'actor' will be betting with their own pool of roulette strategies on a fair game. Their roulette strategies will range in complexity, but they will basically each have a function Bet which returns a list of tuples of bet type [NUMBER, NUMBER-NUMBER, NUMBER-NUMBER-NUMBER-NUMBER, NUMBER-NUMBER-NUMBER-NUMBER-NUMBER-NUMBER, EVENS, ODDS, RED, BLACK, ROW1, ROW2, ROW3, 1_12, 13_24, 25_36] and value in % willing max

# There are 38 possibilities, 

# The game will end when they have lost all their money or if they hit a certain configurable threshhold of gains, like 10x their initial money.

betterRisk = .2
board = [
            [num for num in list(range(1, 37)) if num % 3 == 1],
            [num for num in list(range(1, 37)) if num % 3 == 2],
            [num for num in list(range(1, 37)) if num % 3 == 0]
        ]

class RollResult:
    def __init__(self, number="00", column=-1, isRed=False, isBlack=False, isEven=False, isOdd=False):
        self.number = number
        self.column = column
        self.isRed = isRed
        self.isBlack = isBlack
        self.isEven = isEven
        self.isOdd = isOdd
    def __str__(self):
        return self.number
        
class Better:
    def __init__(self, name, startChips=100, winMult=1.60):
        self.startChips = startChips
        self.chipPool = startChips
        self.chipPoolLock = threading.Lock()
        self.winMult = winMult
        self.winLossRecord = []
        self.name = name
        self.winner = 0
        self.winRound = -1
        self.loseRound = -1
    def __str__(self):
        return self.name + ":\n========\n" + str(self.startChips) + "->" + str(self.chipPool) + "\n========\n" + str(self.winLossRecord)
    def bettingStrategy(self):
        # The most basic betting strategy is 50/50 Odds or Evens and then putting 10% of your money in on it
        loss = 0
        with self.chipPoolLock:
            loss = int(math.ceil(self.chipPool * betterRisk))
            self.chipPool -= loss
        if(secrets.randbelow(100) % 2 == 0):
            return [("ODD", loss)]        
        return [("EVEN", loss)]
    def payout(self, amount):
        with self.chipPoolLock:
            self.chipPool += amount

# The Color and Parity better will bet 50/50 randomly on Black/Red and Odd/Even
class ColorAndParityBetter(Better):
    def bettingStrategy(self):
        loss = 0
        betList = []
        with self.chipPoolLock:
            loss = int(math.ceil(self.chipPool * betterRisk))
            self.chipPool -= loss
        if(loss == 1):
            if(secrets.randbelow(100) % 2 == 0):
                return [("ODD", loss)]
            return [("EVEN", loss)]
        minorLoss = int(loss/2)
        if(secrets.randbelow(100) % 2 == 0):
            betList.append(("ODD", minorLoss))
        else:
            betList.append(("EVEN", minorLoss))
        
        if(secrets.randbelow(100) % 2 == 0):
            betList.append(("RED", loss - minorLoss))
        else:
            betList.append(("BLACK", loss - minorLoss))
        return betList
    
#Single row better bets on 1 row at a time
class SingleRowBetter(Better):
    def bettingStrategy(self):
        loss = 0
        with self.chipPoolLock:
            loss = int(math.ceil(self.chipPool * betterRisk))
            self.chipPool -= loss

        row = secrets.randbelow(100) % 3 + 1
        return [("ROW " + str(row), loss)]
# The 'Twin Row Better' takes on a higher risk for a higher reward, betting smaller units evenly spread out across specific numbers for a big payday.
# If the 'Twin Row Better' has less than 8 chips, they will fall back to the ODD/EVEN RED/BLACK strategy.
class TwinRowBetter(Better):
    def bettingStrategy(self):
        rowNumberFactor = 6 # const
        loss = 0
        betList = []
        with self.chipPoolLock:
            loss = int(math.ceil(self.chipPool * betterRisk))
            self.chipPool -= loss
        if(loss == 1):
            if(secrets.randbelow(100) % 2 == 0):
                return [("ODD", loss)]
            return [("EVEN", loss)]
        if(loss < rowNumberFactor):
            minorLoss = int(loss/2)
            if(secrets.randbelow(100) % 2 == 0):
                betList.append(("ODD", minorLoss))
            else:
                betList.append(("EVEN", minorLoss))
            
            if(secrets.randbelow(100) % 2 == 0):
                betList.append(("RED", loss - minorLoss))
            else:
                betList.append(("BLACK", loss - minorLoss))
        else:
            shift = secrets.randbelow(2) # 0 for 1/2, 1 for 2/3
            # we will be using 8 chips every time up/down for that sweet 42% odds and 17x payout (per chip, a little over 2x)
            # we have 12 possible slots for l/r twins so we have a variance of 4 that we can possibly have for our up/down offset.
            updown = secrets.randbelow(12 - rowNumberFactor) # 0-3 0->7, 3->11 perf
            
            incrementalBets = int(loss/rowNumberFactor)
            extraHeap = loss - (incrementalBets * rowNumberFactor) # at most 7
            
            for y in range(updown, updown+rowNumberFactor):
                pair = str(board[shift][y]) + "-" + str(board[shift+1][y])
                specificBet = incrementalBets
                if(extraHeap != 0):
                    specificBet += 1
                    extraHeap -= 1
                betList.append((pair, specificBet))
                    
        return betList
            
class SpecificBlackOrRedBetter(Better):
    def bettingStrategy(self):
        loss = 0
        betList = []
        with self.chipPoolLock:
            if(self.chipPool > 10):
                loss = 10
            else:
                loss = self.chipPool/2
            self.chipPool -= loss
        if(loss == 1):
            if(secrets.randbelow(100) % 2 == 0):
                return [("ODD", loss)]
            return [("EVEN", loss)]
        if(loss < 10):
            minorLoss = int(loss/2)
            if(secrets.randbelow(100) % 2 == 0):
                betList.append(("ODD", minorLoss))
            else:
                betList.append(("EVEN", minorLoss))
            
            if(secrets.randbelow(100) % 2 == 0):
                betList.append(("RED", loss - minorLoss))
            else:
                betList.append(("BLACK", loss - minorLoss))
        else:
            # we will be using 8 chips every time up/down for that sweet 42% odds and 17x payout (per chip, a little over 2x)
            # we have 12 possible slots for l/r twins so we have a variance of 4 that we can possibly have for our up/down offset.
            halfBet = int(loss/2)
            fifthBet = int((loss-halfBet)/5)
            extraHeap = loss - halfBet - (fifthBet*5) # at most 5 i think
            with self.chipPoolLock:
                self.chipPool += extraHeap
            betList.append(("RED", halfBet))
            betList.append(("8-11", fifthBet))
            betList.append(("10-13", fifthBet))
            betList.append(("17-20", fifthBet))
            betList.append(("26-29", fifthBet))
            betList.append(("28-31", fifthBet))
        return betList

class Table:
    def __init__(self, betters:List[Better]):
        self.betters = betters
        self.redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.round = 1
        # column 1 is X % 3 = 1, col 2 is x % 3 = 2, col 3 is x % 3 = 0
        # because there are 12 numbers, there are 11 edges for 2 or vertices for 4 in each row
        # there are a total of 33 edges or 22 vertices for each 2/4 combo
        
    def rollNumber(self):
        result = secrets.randbelow(38) # 0 is 0, 37 is 00
        number = "NAN"
        isBlack = False
        isRed = False
        isEven = False
        isOdd = False
        column = -1
        if(result in (0, 37)):
            if(result == 0):
                number = "0"
            else:
                number = "00"
        else:
            isRed = result in self.redNumbers
            isBlack = not isRed
            isEven = (result % 2) == 0
            isOdd = (result % 2) == 1
            column = ((result-1) % 3) + 1
            number = str(result)
        return RollResult(number, column, isRed, isBlack, isEven, isOdd)
    
    def betPayout(self, betType, betValue, result=RollResult()):
        number = re.compile(r"(\d+)")
        numbers = re.compile(r"(\d+-)+\d+")
        rangep = re.compile(r"(\d+)_(\d+)")
        odds = re.compile(r"(odds|ODDS|odd|ODD)")
        evens = re.compile(r"(evens|EVENS|even|EVEN)")
        black = re.compile(r"(black|BLACK)")
        red = re.compile(r"(red|RED)")
        rowX = re.compile(r"(row|ROW) ?(\d)")
        
        if(number.fullmatch(betType)):
            if(result.number == betType):
                return betValue * 35
        elif(numbers.fullmatch(betType)):
            matchList = re.findall(r"\d+", betType)
            if(result.number in matchList):
                if(len(matchList) == 2):
                    return 17*betValue
                elif(len(matchList) == 4):
                    return 8*betValue
                elif(len(matchList) == 6):
                    return 5*betValue
                elif(len(matchList) == 3):
                    return 11*betValue
                else:
                    print("[Bet Match] Non-standard length: " + str(len(matchList)))
                    return betValue
        elif(rangep.fullmatch(betType)):
            matchObj = rangep.fullmatch(betType)
            if(int(result.number) >= int(matchObj.group(1)) and int(result.number) <= int(matchObj.group(2))):
                return 2*betValue
        elif(odds.fullmatch(betType) and int(result.isOdd)):
            return 2*betValue
        elif(evens.fullmatch(betType) and int(result.isEven)):
            return 2*betValue
        elif(red.fullmatch(betType) and int(result.isRed)):
            return 2*betValue
        elif(black.fullmatch(betType) and int(result.isBlack)):
            return 2*betValue
        elif(rowX.fullmatch(betType)):
            matchObj = rowX.fullmatch(betType)
            if(result.column == int(matchObj.group(2))):
                return 2*betValue
        return 0
    def playHand(self):
        # unorthodox; predecided what the roll would be.
        spinner = self.rollNumber()
        # print("Spinner will land on: " + str(spinner.number) + " colored " + ("black" if spinner.isBlack else "red"))
        for better in self.betters:
            startingMoney = better.chipPool
            bets = better.bettingStrategy()
            for bet in bets:
                better.payout(self.betPayout(bet[0], bet[1], spinner))
            endingMoney = better.chipPool
            better.winLossRecord.append(str(startingMoney) + " -> " + str(endingMoney) + " : " + str(bets))
            if(better.chipPool == 0):
                # print(better.name + " has lost all their chips at round " + str(self.round))
                better.winner = -1
                better.loseRound = self.round
                self.betters.remove(better)
            if(better.chipPool >= better.startChips * better.winMult):
                # print(better.name + " has multiplied their starting money at round " + str(self.round))
                better.winner = 1
                better.winRound = self.round
                self.betters.remove(better)
        self.round += 1
        

successes = [0, 0, 0, 0, 0]
persists = [0, 0, 0, 0, 0]
losses = [0, 0, 0, 0, 0]
averageDurationsLoss = [0, 0, 0, 0, 0]
averageDurationsWin = [0, 0, 0, 0, 0]
runGames = 0
totalGames = 1000.0
numberOfHands = 1500 

for repetitions in range(0, int(totalGames)):
    eckertFamily = [Better("Mom"), ColorAndParityBetter("Hunter"), TwinRowBetter("Brant"), SingleRowBetter("Ethan"), SpecificBlackOrRedBetter("Dad")]
    eckertFamilySatDown = eckertFamily.copy()
    eckertFamilyTable = Table(eckertFamilySatDown)
    for x in range(0, numberOfHands):
        eckertFamilyTable.playHand()
    index = 0
    runGames += 1
    for member in eckertFamily:
        if(member.winner == 1):
            successes[index] += 1
            if(averageDurationsWin[index] == 0):
                averageDurationsWin[index] = member.winRound
            else:
                averageDurationsWin[index] = ((averageDurationsWin[index] * (runGames - 1)) + member.winRound)/runGames
        elif(member.winner == 0):
            persists[index] += 1
        else:
            losses[index] += 1
            if(averageDurationsLoss[index] == 0):
                averageDurationsLoss[index] = member.loseRound
            else:
                averageDurationsLoss[index] = ((averageDurationsWin[index] * (runGames - 1)) + member.loseRound)/runGames
        index += 1

#for better in eckertFamily:
#    print(str(better))

print("Percentages are displayed in Win/Persist (End the game without any gain)/Loss")
print("Settings are as folows, Total Games: " + str(int(totalGames)) + " | Number of Hands in a Game: " + str(int(numberOfHands)) + " | Amount of Money Willing to Bet: " + str(betterRisk * 100) + "%\n=================================================================")
for x in range(0, len(eckertFamily)):
    print(eckertFamily[x].name + " had the following success in percentages: " + str((round(successes[x]/totalGames, 4)) * 100) + "%/" + str((round(persists[x]/totalGames, 4)) * 100) + "%/" + str((round(losses[x]/totalGames, 4)) * 100) + "%")
    print(eckertFamily[x].name + " also has the following durations: Average Win Round - " + str(round(averageDurationsWin[x], 2)) + " / Average Loss Round - " + str(round(averageDurationsLoss[x], 2)))
    print("=============================================================================================")
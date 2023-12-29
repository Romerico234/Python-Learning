from random import shuffle

def roll(die: str):
    if die.lower()== "a":
        return diceA()
    if die.lower() == "b":
        return diceB()
    if die.lower() == "c":
        return diceC()

def play(die1: str, die2: str, times: int):
    die1_win = 0
    die2_win = 0
    tie = 0
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if result1 > result2:
            die1_win += 1
        elif result2 > result1:
            die2_win += 1
        else:
            tie += 1
    return (die1_win, die2_win, tie)


def diceA():
    sides = [3,3,3,3,3,6]
    shuffle(sides)
    return sides[0]

def diceB():
    sides = [2,2,2,5,5,5]
    shuffle(sides)
    return sides[0]

def diceC():
    sides = [1,4,4,4,4,4]
    shuffle(sides)
    return sides[0]

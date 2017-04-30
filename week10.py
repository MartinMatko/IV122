import random
import week2
import re

def showDoor(choice):
    return {
        0: 1,
        1: 2,
        2: 1
    }.get(choice)


def applyStrategy(strategy, choice, shown):
    third = [x for x in list(range(3)) if x != choice and x!= shown][0]
    return {
        'switch': third,
        'stay': choice,
        'random': [choice, third][random.randint(0, 1)]
    }.get(strategy)


def montyHallProblem(strategy, n=100000):
    prices = ['car', 'goat', 'goat']
    wins = 0
    for i in range(n):
        choice = random.randint(0, 2)
        shown = showDoor(choice)
        choice = applyStrategy(strategy, choice, shown)
        if prices[choice] == 'car':
            wins += 1
    print('With ' + str(n) + ' iterations and ' + strategy + ' strategy player had won in ' + str(
        wins / n * 100) + '% of games.')


def analyzeNumbers():
    set = ['1', '2', '3', '4', '5', '6']
    variationsWithRepetition6 = week2.calculation(set, 6, week2.Type.variationWithRepetition)
    variationsWithRepetition2 = week2.calculation(set, 2, week2.Type.variationWithRepetition)
    for i in range(1, 8):
        file = open('random/random' + str(i) + ".txt")
        file = file.read().replace(" ", "") #now we have only numbers as one long string
        length = len(file)
        print('Sequence: ' + str(i) + ' of length ' + str(length))
        countingNumbers(file)
        overlappingVariations(file, variationsWithRepetition2, False)
        overlappingVariations(file, variationsWithRepetition2, True, 200)
        overlappingVariations(file, variationsWithRepetition6, True, 10)

def countingNumbers(file):
    for i in range(1, 7):
        positions = [0]
        sum = 0
        for j in range(len(file)):
            if str(i) == file[j]:
                positions.append(j)
        occurences = len(positions)
        for j in range(occurences-1):
            sum += positions[j+1] - positions[j]
        print(str(i) + ' is in sequence ' + str(occurences))
        print(str(i) + ' has average interval of occuring ' + str(sum/occurences))
        print(positions)


def overlappingVariations(file, variations, lookingForExisting, max=0):
    for variation in variations:
        variationString = ''.join(variation)
        numberOfVariations = file.count(variationString)
        # finding all permutations which are not generated or are generated at least 1.5 times more then they should
        if lookingForExisting:
            if numberOfVariations > max:
                print(variationString + ' was generated ' + str(numberOfVariations))
        else:
            if numberOfVariations == 0:
                print(variationString + ' was generated ' + str(numberOfVariations))




#montyHallProblem('switch')

analyzeNumbers()
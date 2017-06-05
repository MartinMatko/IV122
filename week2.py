import random
import time
from enum import Enum

import numpy as np
from PIL import Image, ImageDraw

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)

set = ['A', 'B', 'C', 'D']


class Type(Enum):
    permutation = 1
    variation = 2
    variationWithRepetition = 3
    combination = 4
    combinationWithRepetition = 5


def calculation(set, k, type):
    if k == 1:
        return [[x] for x in set]
    result = []
    tempSet = set[:]
    for x in set:
        remainingElements = tempSet[:]
        if not (type == Type.variationWithRepetition or type == Type.combinationWithRepetition):
            remainingElements.remove(x)
        recursiveCalculations = calculation(remainingElements, k - 1, type)
        for y in recursiveCalculations:
            result.append([x] + y)
        if type == Type.combination or type == Type.combinationWithRepetition:
            tempSet.remove(x)
    return result


# print(calculation(set, 2, Type.combinationWithRepetition))

def combNumber(n, k, cache=None):
    if k == 0 or n == k:
        return 1
    if cache is None:
        cache = np.zeros((k, n))
    if cache[n - 1][k - 1] == 0:
        cache[n - 1][k - 1] = combNumber(n - 1, k - 1, cache) + combNumber(n - 1, k, cache)
    return cache[n - 1][k - 1]


def pascalTriangle(n, d):
    sizeOfSquare = size / n
    cache = [[0 for x in range(n)] for y in range(n)]
    colors = [[], [], []]
    for i in range(d):
        colors[0].append(random.randint(0, 255))
        colors[1].append(random.randint(0, 255))
        colors[2].append(random.randint(0, 255))
    for y in range(0, n):
        for x in range(0, y + 1):
            remainder = combNumber(y, x, cache) % d
            colorOfSquare = (colors[0][remainder], colors[1][remainder], colors[2][remainder])
            draw.rectangle([size / 2 - x * sizeOfSquare + ((y - 1) * sizeOfSquare) / 2, y * sizeOfSquare,
                            size / 2 - x * sizeOfSquare + \
                            sizeOfSquare + ((y - 1) * sizeOfSquare) / 2, y * sizeOfSquare + sizeOfSquare],
                           colorOfSquare)
    image.save("images2\\pascal" + str(n) + "n" + str(d) + "d.png")


# pascalTriangle(256, 8)

def exponentialWholeNumbers(x, n):
    temp = 2
    result = x
    while temp * 2 <= n:
        result = result * result
        temp *= 2
    for i in range(int(n - temp / 2)):
        result = result * x
    return result


# exponentialWholeNumbers(2, 10)

def rootBisectionMethod(x, n):
    up = x
    down = 0
    difference = 1
    half = (up - down) / 2
    while (abs(difference) > 0.01):
        half = (up - down) / 2 + down
        difference = exponentialWholeNumbers(half, n) - x
        if (difference <= 0):
            down = half
        else:
            up = half
    return half


def powerWithFractions(number, numerator, denominator):
    result = exponentialWholeNumbers(number, numerator)
    result = rootBisectionMethod(result, denominator)
    print(result)


# powerWithFractions(2, 2, 3)

timeMax = 1


def monteCarlo():
    start = time.time()
    inside = 0
    total = 0
    while time.time() - start < timeMax:
        x = random.random()
        y = random.random()
        total += 1
        if abs(np.sqrt(x ** 2 + y ** 2)) < 1:
            inside += 1
    print((4 * inside) / total)


def leibniz():
    start = time.time()
    result = 1
    denominator = -3
    counter = 1
    while time.time() - start < timeMax:
        result = result + (1 / denominator)
        if counter % 2 == 1:
            denominator = -1 * denominator + 2
        else:
            denominator = -1 * denominator - 2
        counter += 1
    print(result * 4)


def archimedes():
    x = 4
    y = 2 * np.math.sqrt(2)
    start = time.time()
    while time.time() - start < timeMax:
        xnew = 2 * x * y / (x + y)
        y = np.math.sqrt(xnew * y)
        x = xnew
    print((x + y) / 2)


def wallis():
    result = 2
    i = 3
    start = time.time()
    while time.time() - start < timeMax:
        result = result * ((i - 1) / i) * ((i + 1) / i)
        i += 2
    print(result * 2)

# monteCarlo()
# leibniz()
# archimedes()
# wallis()
# image.show()

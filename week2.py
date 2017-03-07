from enum import Enum

from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plot
from random import randint
from PIL.ImageQt import rgb
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.misc.comb

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

#print(calculation(set, 2, Type.combinationWithRepetition))

def combNumber(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combNumber(n - 1, k - 1) + combNumber(n - 1, k)


def comb_number(n, k, cache=None):
    if k == 0 or k == n:
        return 1
    if cache is None:
        cache = [[0 for _ in range(k)] for _ in range(n)]
    if cache[n - 1][k - 1] == 0:
        cache[n - 1][k - 1] = comb_number(n - 1, k - 1, cache) + comb_number(n - 1, k, cache)
    return cache[n - 1][k - 1]


def pascal(n, d):
    sizeOfSquare = size / (n*2)
    cache = [[0 for _ in range(n)] for _ in range(n)]
    colors = [[], [], []]
    for i in range(d):
        colors[0].append(randint(0, 255))
        colors[1].append(randint(0, 255))
        colors[2].append(randint(0, 255))
    for y in range(0, n):
        for x in range(0, y + 1):
            colorOfSquare = (colors[0][comb_number(y, x, cache) % d], colors[1][comb_number(y, x, cache) % d], colors[2][comb_number(y, x, cache) % d])
            draw.rectangle([size/2 - x * sizeOfSquare, y * sizeOfSquare *2, size/2 - x * sizeOfSquare + sizeOfSquare, y * sizeOfSquare *2 + sizeOfSquare *2], colorOfSquare)


pascal(30, 5)

image.show()

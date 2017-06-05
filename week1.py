import math

import matplotlib.pyplot as plot
import numpy as np
from PIL import Image, ImageDraw

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def bitmap():
    for x in range(size):
        for y in range(size):
            image.putpixel((x, y), (x, 0, y))


def scalar():
    for (x, y) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        for z in range(0, int(size / 2), 10):
            draw.line((z - 2 * x * z + x * size, size / 2, size / 2, size / 2 - z + 2 * y * z), fill=10)


def scalar1():
    for (x, y) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        z = 1
        while z < size // 2:
            z **= 100 / 99
            draw.line((z - 2 * x * z + x * size, size / 2, size / 2, size / 2 - z + 2 * y * z), fill=10)


def ulam(k, conditionMethod):
    number = 1
    x = int(size / 2 - 1)
    y = int(size / 2 - 1)
    for i in range(1, int(size - 1)):
        for j in range(1, i):
            number += 1
            if conditionMethod(number, k):
                image.putpixel((x, y), (0, 0, 0))
            if i % 2 == 1:
                x += 1
            else:
                x -= 1
        for j in range(1, i):
            number += 1
            if conditionMethod(number, k):
                image.putpixel((x, y), (0, 0, 0))
            if i % 2 == 1:
                y -= 1
            else:
                y += 1


def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def isDividable(n, k):
    return n % k == 0


def collatz(n):
    numberOfSteps = 0
    while n != 1:
        numberOfSteps += 1
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            print(1)
    return numberOfSteps


def collatzNumberOfSteps():
    for i in range(1, 8000):
        numberOfSteps = 0
        n = i
        while n != 1:
            numberOfSteps += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        plot.plot(i, numberOfSteps, 'ko')
    plot.show()


def collatzMaxNumber():
    for i in range(1, 1000):
        maxNumber = 0
        n = i
        while n != 1:
            if n > maxNumber:
                maxNumber = n
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        plot.plot(i, maxNumber, 'ko')
    plot.show()


def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)


def nsdNumberOfStepsModulo(a, b, steps=1):
    if b == 0:
        return steps
    else:
        return nsdNumberOfStepsModulo(b, a % b, steps + 1)


def nsdNumberOfStepsMinus(a, b):
    steps = 0
    while a != b:
        steps += 1
        if a > b:
            c = a
            a = a - b
            b = c
        else:
            c = a
            a = b - a
            b = c

    return steps


def nsd3dPlot():
    fig = plot.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(1, 100):
        for j in range(1, 100):
            ax.scatter(i, j, nsd(i, j), color='b')
    plot.show()


def nsdPlot(n, function):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = function(i, j)
    plot.pcolor(matrix)
    plot.colorbar()
    plot.show()


# bitmap()
# scalar()
# ulam()
ulam(13, isDividable)
# collatzNumberOfSteps()
# collatzMaxNumber()
# nsd3dPlot()
# nsdPlot(300, nsdNumberOfStepsModulo)
# nsdPlot(300, nsdNumberOfStepsMinus)


image.show()

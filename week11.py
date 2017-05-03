import random
import numpy as np
import matplotlib.pyplot as plot


def loadData(filename):
    lines = open(filename + '.txt').read().split('\n')
    x = []
    y = []
    for line in lines:
        record = line.split(' ')
        x.append(float(record[0]))
        y.append(float(record[1]))
    return np.array(x, dtype=float), np.array(y, dtype=float)


def generateData(n, a, b, variance):
    x = np.arange(n)
    delta = np.random.uniform(-variance, variance, size=(n,))
    # delta = np.random.normal(0, variance, size=(n,))
    y = a * x + b + delta
    return x, y


def getLineFromFormula(x, y):
    sumXX, sumXY, sumX, sumY = 0, 0, 0, 0
    n = len(x)
    for i in range(n):
        sumXX += x[i] ** 2
        sumXY += x[i] * y[i]
        sumX += x[i]
        sumY += y[i]
    a = (n * sumXY - sumX * sumY) / (n * sumXX - sumX ** 2)
    b = (sumY - a * sumX) / n
    return a, b


def analyse(filename):
    x, y = loadData(filename)
    # x, y = generateData(100, 1/5, 20, 10)
    a, b = getLineFromFormula(x, y)
    plot.scatter(x, y)
    plot.plot(x, a * x + b, color="red")
    plot.title(str(a) + 'x + ' + str(b))
    plot.show()


def kMeans(filename, k):
    x, y = loadData(filename)
    #TODO

#analyse('faithful')
kMeans('faithful', 2)

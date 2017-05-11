import math

import matplotlib.pyplot as plot
import numpy as np


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


def getDistance(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))


def kMeans(filename, n):
    x, y = loadData(filename)
    means = {}
    cm = plot.get_cmap('gist_rainbow')
    minX, maxX, minY, maxY = min(x), max(x), min(y), max(y)
    for i in range(n):
        means[i] = {'x': np.random.randint(minX, maxX),
                    'y': np.random.randint(minY, maxY),
                    'pointsX': [],
                    'pointsY': [],
                    'color': cm(1. * i / n)}

    for i in range(20):
        for mean in means.values():
            mean['pointsX'].clear()
            mean['pointsY'].clear()

        # assigning points to mean
        for j in range(len(x)):
            shortestDistance = max(maxX, maxY)
            for k in range(len(means.values())):
                centreX, centreY = means[k]['x'], means[k]['y']
                distance = math.sqrt((x[j] - centreX) ** 2 + (y[j] - centreY) ** 2)
                if distance < shortestDistance:
                    shortestDistance = distance
                    mean = means[k]
            mean['pointsX'].append(x[j])
            mean['pointsY'].append(y[j])

        # finding new mean of cluster
        for mean in means.values():
            mean['x'] = sum(mean['pointsX']) / len(mean['pointsX'])
            mean['y'] = sum(mean['pointsY']) / len(mean['pointsY'])

    for mean in means.values():
        plot.scatter(mean['pointsX'], mean['pointsY'], color=mean['color'])
        plot.scatter(mean['x'], mean['y'], color=(0, 0, 0))
    plot.show()


# analyse('faithful')
kMeans('faithful', 4)

import random
from PIL import Image, ImageFont
from math import log, cos, sin, pi

from Geometry import *

size = 500
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def isPointInsideOfMaze(movedX, movedY, graphSize):
    return 0 <= movedX < graphSize and 0 <= movedY < graphSize

def drawBorders(graph, graphSize):
    sizeOfTile = size // math.sqrt(len(graph))
    for i in range(graphSize):
        for j in range(graphSize):
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                movedX = i + direction[0]
                movedY = j + direction[1]
                if isPointInsideOfMaze(movedX, movedY, graphSize) and (str(movedX) + ',' + str(movedY)) not in graph[str(i) + ',' + str(j)]:
                    draw.line((i * sizeOfTile, j * sizeOfTile, movedX * sizeOfTile, movedY * sizeOfTile), fill=10)
    image.save('C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images13\\maze.png')
    image.show()

def initialiseMaze(size):
    graph = {}
    for i in range(size):
        for j in range(size):
            graph[str(i) + ',' + str(j)] = set()
            # for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            #     movedX = i + direction[0]
            #     movedY = j + direction[1]
            #     if isPointInsideOfMaze(movedX, movedY, size):
            #         graph[str(i) + ',' + str(j)].add(str(movedX) + ',' + str(movedY))
    return graph

def generateEdges(graph, graphSize):

    vertex = '0,0'
    x0, y0 = vertex.split(',')
    x1, y1 = -1, -1
    complexity = 100
    while complexity > 0:
        while not isPointInsideOfMaze(x1, y1, graphSize):
            randomJump = 1
            direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            x1 = int(x0) + randomJump * direction[0]
            y1 = int(y0) + randomJump * direction[1]
        nextVertex = str(x1) + ',' + str(y1)
        graph[vertex].add(nextVertex)
        vertex = nextVertex
        x0, y0 = vertex.split(',')
        x1, y1 = -1, -1
        complexity -= 1
    return graph


def generateMaze(graphSize):
    graph = initialiseMaze(graphSize)
    generateEdges(graph, graphSize)
    drawBorders(graph, graphSize)


generateMaze(10)

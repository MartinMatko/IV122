from PIL import Image, ImageFont

from Geometry import *

size = 500
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def mazeToGraph():
    lines = open('numberMaze.txt').read().split('\n')
    graph = {}
    graphSize = len(lines)
    for i in range(graphSize):
        rows = lines[i].split(' ')
        for j in range(graphSize):
            position = int(rows[j])
            graph[str(i) + ',' + str(j)] = set()
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                movedX = i + direction[0] * position
                movedY = j + direction[1] * position
                if isPointInsideOfMaze(movedX, movedY, graphSize):
                    graph[str(i) + ',' + str(j)].add(str(movedX) + ',' + str(movedY))
    return graph, graphSize


def solve(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start] - set(path):
        newPaths = solve(graph, node, end, path)
        for newPath in newPaths:
            paths.append(newPath)
    return paths


def drawTiles(graphSize):
    sizeOfTile = size // graphSize
    for i in range(graphSize):
        draw.line((0, i * sizeOfTile, size, i * sizeOfTile), fill=10)
        draw.line((i * sizeOfTile, 0, i * sizeOfTile, size), fill=10)


def drawNumbers():
    lines = open('numberMaze.txt').read().split('\n')
    graphSize = len(lines)
    sizeOfTile = size // graphSize
    verdana_font = ImageFont.truetype("verdana.ttf", sizeOfTile // 2, encoding="unic")
    for i in range(graphSize):
        positions = lines[i].split(' ')
        for j in range(graphSize):
            draw.text((i * sizeOfTile, j * sizeOfTile), positions[j], font=verdana_font, fill="#000000")


def drawPath(path, graphSize):
    sizeOfTile = size // graphSize
    for i in range(len(path) - 1):
        vertex1 = path[i].split(',')
        vertex2 = path[i + 1].split(',')
        x1 = int(vertex1[0]) * sizeOfTile + sizeOfTile // 2
        y1 = int(vertex1[1]) * sizeOfTile + sizeOfTile // 2
        x2 = int(vertex2[0]) * sizeOfTile + sizeOfTile // 2
        y2 = int(vertex2[1]) * sizeOfTile + sizeOfTile // 2
        draw.line((x1, y1, x2, y2), fill=(0, 50, 200), width=5)


def drawMaze():
    graph, graphSize = mazeToGraph()
    # maze entry is in top left corner and exit in bottom right corner
    paths = solve(graph, '0,0', str(graphSize - 1) + ',' + str(graphSize - 1))
    print(paths)
    drawTiles(graphSize)
    drawNumbers()
    drawPath(min(paths, key=len), graphSize)
    image.save('C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images12\\numberMaze.png')
    image.show()


def isPointInsideOfMaze(movedX, movedY, graphSize):
    return 0 <= movedX < graphSize and 0 <= movedY < graphSize


def lampsToGraph():
    lines = open('lamps.txt').read().split('\n')
    graph = {}
    graphSize = len(lines)
    lamps = []
    for i in range(graphSize):
        rows = lines[i].split(' ')
        for j in range(graphSize):
            graph[str(i) + ',' + str(j)] = set()
            # f=free place o=obstacle l=lamp
            if rows[j] == 'l':
                lamps.append(str(i) + ',' + str(j))
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                movedX = i + direction[0]
                movedY = j + direction[1]
                if isPointInsideOfMaze(movedX, movedY, graphSize) and (rows[j] == 'l' or rows[j] == 'f'):
                    graph[str(i) + ',' + str(j)].add(str(movedX) + ',' + str(movedY))
    return graph, graphSize, lamps


def drawLamps():
    graph, graphSize, lamps = lampsToGraph()
    paths = []
    # TODO paths = ...
    print(paths)
    drawTiles(graphSize)
    drawPath(min(paths, key=len), graphSize)
    image.save('C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images12\\lamps.png')
    image.show()


#drawMaze()
drawLamps()

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


def drawBorders(graphSize):
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
            draw.text((j * sizeOfTile, i * sizeOfTile), positions[j], font=verdana_font, fill="#000000")


def drawPath(path, graphSize):
    sizeOfTile = size // graphSize
    for i in range(len(path) - 1):
        vertex1 = path[i].split(',')
        vertex2 = path[i + 1].split(',')
        y1 = int(vertex1[0]) * sizeOfTile + sizeOfTile // 2
        x1 = int(vertex1[1]) * sizeOfTile + sizeOfTile // 2
        y2 = int(vertex2[0]) * sizeOfTile + sizeOfTile // 2
        x2 = int(vertex2[1]) * sizeOfTile + sizeOfTile // 2
        draw.line((x1, y1, x2, y2), fill=(0, 50, 200), width=5)


def drawMaze():
    graph, graphSize = mazeToGraph()
    # maze entry is in top left corner and exit in bottom right corner
    paths = solve(graph, '0,0', str(graphSize - 1) + ',' + str(graphSize - 1))
    print(paths)
    drawBorders(graphSize)
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
    matrix = [[0 for x in range(graphSize)] for y in range(graphSize)]
    for i in range(graphSize):
        rows = lines[i].split(' ')
        for j in range(graphSize):
            matrix[i][j] = rows[j]

    for i in range(graphSize):
        for j in range(graphSize):
            graph[str(i) + ',' + str(j)] = set()
            # f=free space o=obstacle l=lamp
            if matrix[i][j] == 'l':
                lamps.append({'vertex': str(i) + ',' + str(j),
                              'paths': {},
                              'distances': {}})
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                movedX = i + direction[0]
                movedY = j + direction[1]
                if isPointInsideOfMaze(movedX, movedY, graphSize) and matrix[movedX][movedY] != 'o' and matrix[i][
                    j] != 'o':
                    graph[str(i) + ',' + str(j)].add(str(movedX) + ',' + str(movedY))
    return graph, graphSize, lamps


def dijsktra(graph, initial):
    costOfPath = {initial: 0}
    path = {}
    vertices = set(graph.keys())
    while vertices:
        minVertex = None
        for node in vertices:
            if node in costOfPath:
                if minVertex is None:
                    minVertex = node
                elif costOfPath[node] < costOfPath[minVertex]:
                    minVertex = node
        if minVertex is None:
            break
        vertices.remove(minVertex)
        currentWeight = costOfPath[minVertex]
        for edge in graph[minVertex]:
            weight = currentWeight + 1
            if edge not in costOfPath or weight < costOfPath[edge]:
                costOfPath[edge] = weight
                path[edge] = minVertex
    return costOfPath, path


def findBestIntersection(lamps, graphSize):
    pathCostSums = {}
    for i in range(graphSize):
        for j in range(graphSize):
            pathCostSums[str(i) + ',' + str(j)] = 0
    for lamp in lamps:
        for vertex in lamp['distances'].keys():
            pathCostSums[vertex] += lamp['distances'][vertex]
    minPathCost = 10000
    bestIntersection = ''
    for vertex in pathCostSums.keys():
        if 0 < pathCostSums[vertex] < minPathCost:
            minPathCost = pathCostSums[vertex]
            bestIntersection = vertex
    return bestIntersection


def drawTiles():
    lines = open('lamps.txt').read().split('\n')
    graphSize = len(lines)
    sizeOfTile = size // graphSize
    nextTileX = 0
    nextTileY = 0
    for i in range(graphSize):
        objects = lines[i].split(' ')
        for j in range(graphSize):
            color = (255, 255, 255)
            if objects[j] == 'o':
                color = (128, 128, 128)
            if objects[j] == 'l':
                color = (255, 255, 0)
            draw.rectangle((nextTileX, nextTileY, nextTileX + sizeOfTile, nextTileY + sizeOfTile), fill=color)
            nextTileX += sizeOfTile
        nextTileX = 0
        nextTileY += sizeOfTile


def getPathsFromDictionary(lamps, intersection):
    paths = []
    for lamp in lamps:
        path = []
        currentVertex = intersection
        while currentVertex != lamp['vertex']:
            path.append(currentVertex)
            currentVertex = lamp['paths'][currentVertex]
        path.append(currentVertex)
        paths.append(path)
    return paths


def drawLamps():
    graph, graphSize, lamps = lampsToGraph()
    for lamp in lamps:
        lamp['distances'], lamp['paths'] = dijsktra(graph, lamp['vertex'])
    intersection = findBestIntersection(lamps, graphSize)
    paths = getPathsFromDictionary(lamps, intersection)
    drawTiles()
    drawBorders(graphSize)
    for path in paths:
        drawPath(path, graphSize)
    image.save('C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images12\\lamps.png')
    image.show()


#drawMaze()
drawLamps()

from random import randint

from PIL import Image

from Geometry import *

size = 1000
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)
middle = size // 2


def generateLines(length, count):
    lines = []
    for i in range(count):
        x1 = randint(length, size - length)
        y1 = randint(length, size - length)
        angle = math.radians(randint(0, 360))
        x2 = x1 + math.sin(angle) * length
        y2 = y1 + math.cos(angle) * length
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
    return lines


def drawLines(lines):
    for line in lines:
        draw.line((line.p1.x, line.p1.y, line.p2.x, line.p2.y), fill=(0, 0, 0))


def draw_intersects(lines):
    for first in lines:
        for second in lines:
            intersect = first.intersect(second)
            r = 5
            if intersect is not None:
                x = intersect.x
                y = intersect.y
                draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def linesWithIntersects(length, count):
    lines = generateLines(length, count)
    drawLines(lines)
    draw_intersects(lines)
    image.save("images5\\linesWithIntersects.png")


def generateAndDrawPoints(numberOfPoints):
    points = []
    r = 5
    for i in range(numberOfPoints):
        x = randint(0, size)
        y = randint(0, size)
        points.append(Point(x, y))
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))
    return points


def triangulation(density, sort):
    points = generateAndDrawPoints(density)
    chosen = []
    lines = []
    for point1 in points:
        for point2 in points:
            if point1 != point2:
                lines.append(Line(point1, point2))
    if sort:
        lines.sort(key=lambda x: x.length())
    for line in lines:
        intersected = False
        for selectedLine in chosen:
            if line.intersect(selectedLine) is not None:
                intersected = True
                break
        if not intersected:
            chosen.append(line)
    drawLines(chosen)
    image.save("images5\\triangulationSortedUniform.png")


def findLeftMostPoint(points):
    result = points[0]
    for point in points:
        if point.x < result.x and point.y < result.y:
            result = point
    return result


def isLeftOfLine(point, line):
    return ((line.p2.x - line.p1.x) * (point.y - line.p1.y) - (line.p2.y - line.p1.y) * (point.x - line.p1.x)) > 0


def convexHull(points):
    pointOnHull = findLeftMostPoint(points)
    pointsOnHull = []
    endPoint = points[0]
    while len(pointsOnHull) == 0 or pointsOnHull[0] != endPoint:  # we finish when we close convex hull
        pointsOnHull.append(pointOnHull)
        for point in points:
            if (endPoint == pointOnHull) or (
                    isLeftOfLine(point, Line(pointOnHull, endPoint))):  # we search for leftMost point
                endPoint = point
        draw.line((pointOnHull.x, pointOnHull.y, endPoint.x, endPoint.y), fill=10)
        pointOnHull = endPoint
    return [x for x in points if x not in pointsOnHull]  # returns points which are not in convex hull


def layeredConvexHull(density):
    points = generateAndDrawPoints(density)
    while len(points) > 1:
        points = convexHull(points)
    image.save("images5\\convexHull.png")


# linesWithIntersects(200, 50)
# triangulationBasic(30)
# triangulation(30, False)
# triangulation(30, True)
layeredConvexHull(50)

image.show()

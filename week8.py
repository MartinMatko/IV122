from PIL import Image, ImageDraw
import math
import numpy as np
import copy

from Geometry import Polygon, Point, PolygonGroup

size = 1000
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def rotation(angle):
    cos = math.cos(math.radians(-angle))
    sin = math.sin(math.radians(-angle))
    matrix = np.matrix([[cos, -sin, 0],
                        [sin, cos, 0],
                        [0, 0, 1]])
    return matrix


def scaling(x, y):
    matrix = np.matrix([[x, 0, 0],
                        [0, y, 0],
                        [0, 0, 1]])
    return matrix


def translation(x, y):
    matrix = np.matrix([[1, 0, x],
                        [0, 1, y],
                        [0, 0, 1]])
    return matrix


def shear(k):
    matrix = np.matrix([[1, k, 0],
                        [0, 1, 0],
                        [0, 0, 1]])
    return matrix


def combine(transformations):
    result = transformations[0]
    for i in range(1, len(transformations)):
        result = np.dot(result, transformations[i])
    return result


def square(size):
    square = Polygon(
        [Point(-size, size), Point(size, size), Point(size, -size), Point(-size, -size), Point(-size, size)])
    return square.applyTransformation(rotation(90))


def squares():
    polygon = square(20)
    transformations = combine([rotation(20), scaling(1.1, 1.1), translation(5, 10)])
    polygon.repeatTransformation(10, transformations, image, size)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images8\\squares.png")


def tail():
    polygon = square(50)
    transformations = combine([shear(1.3), rotation(10), scaling(0.9, 0.9), translation(-50, 50)])
    polygon.repeatTransformation(25, transformations, image, size)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images8\\tail.png")


def fan():
    polygon = square(200)
    transformations = combine(rotation(10), scaling(1.1, 0.8))
    polygon.repeatTransformation(50, transformations, image, size)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images8\\fan.png")


def mergeGroups(groups):
    merged = PolygonGroup()
    for group in groups:
        for polygon in group.polygons:
            merged.polygons.append(polygon)
    return merged


def mrcm(n, polygon, transformations):
    group = PolygonGroup([polygon])
    for i in range(n):
        groups = []
        for transformation in transformations:
            oldPolygons = copy.deepcopy(group.polygons)
            newGroup = PolygonGroup(oldPolygons)
            newGroup.applyTransformation(transformation)
            groups.append(newGroup)
        group = mergeGroups(groups)
    for polygon in group.polygons:
        polygon.draw(image, size)


def sierpinskyTriangle(size, angle):
    transformations = [combine([translation(0, size // 2), scaling(0.5, 0.5)]),
                       combine([rotation(angle), translation(0, size // 2), scaling(0.5, 0.5)]),
                       combine([rotation(-angle), translation(0, size // 2), scaling(0.5, 0.5)])]
    mrcm(7, square(size), transformations)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images8\\sierpinskyTriangle" + str(angle) + ".png")


def star(size):
    transformations = [np.matrix([[0.255, 0.0, 0.3726],
                                  [0.0, 0.255, 0.6714],
                                  [0, 0, 1]]),
                       np.matrix([[0.255, 0.0, 0.1146],
                                  [0.0, 0.255, 0.2232],
                                  [0, 0, 1]]),
                       np.matrix([[0.255, 0.0, 0.6306],
                                  [0.0, 0.255, 0.2232],
                                  [0, 0, 1]]),
                       np.matrix([[0.370, -0.642, 0.6356],
                                  [0.642, 0.370, -0.0061],
                                  [0, 0, 1]])]
    mrcm(5, square(size), transformations)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images8\\star.png")


# squares()
# tail()
# fan()

# sierpinskyTriangle(500, 150)
star(500)
image.show()

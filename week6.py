import random
from math import cos, pi, sin

from PIL import Image

from Geometry import *
from Lsystem import Lsystem

size = 500
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def chaosGame(n, r, iterations):
    points = []
    radius = size // 2 - 10
    # https://stackoverflow.com/questions/876853/generating-color-ranges-in-python
    colors = []
    for i in range(n):
        h = '%06X' % random.randint(0, 0xFFFFFF)
        colors.append(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))

    for i in range(n):
        x = size // 2 + radius * cos(2 * pi * i / n)
        y = size // 2 + radius * sin(2 * pi * i / n)
        points.append(Point(x, y))
    x = random.randint(0, size - 10)
    y = random.randint(0, size - 10)
    point = Point(x, y)
    indefOfPrevousChosenPoint = 1
    for i in range(iterations):
        indexOfChosenPoint = random.randint(0, n - 1)
        while (indefOfPrevousChosenPoint == indexOfChosenPoint):
            # while(abs(indefOfPrevousChosenPoint - indexOfChosenPoint) == 1 or abs(indefOfPrevousChosenPoint - indexOfChosenPoint) == 4 ):
            indexOfChosenPoint = random.randint(0, n - 1)
        chosenOne = points[indexOfChosenPoint]
        point.x = int((chosenOne.x + point.x) * r)
        point.y = int((chosenOne.y + point.y) * r)
        if i > 100:
            image.putpixel((point.x, point.y), colors[indexOfChosenPoint])
        indefOfPrevousChosenPoint = indexOfChosenPoint
    image.save("images6\\chaosGamePenta" + str(n) + ".png")


def feigenbaum(x0, zoom=((2.4, 4), (0, 1))):
    zoomR = zoom[0][1] - zoom[0][0]
    zoomX = zoom[1][1] - zoom[1][0]

    for i in range(size):
        r = zoom[0][0] + i * zoomR / size
        for x in calculate(x0, r):
            j = x / (zoomX / size)
            image.putpixel((int(i), int(j)), (0, 0, 0))
    image.save("images6\\feigenbaum" + str(zoom) + ".png")


def calculate(x, r):
    result = []
    xn = x
    for i in range(500):
        xn = r * xn * (1 - xn)
        if i >= 100:
            result.append(xn)
    return result


koch = Lsystem("F--F--F", {"F": "F+F--F+F"},
               {"F": "forward(3)",
                "+": "right(60)",
                "-": "left(60)"})

tree = Lsystem("A", {"A": "F[+A]-A",
                     "F": "FF"},
               {"A": "forward(5)",
                "F": "forward(5)",
                "+": "right(45)",
                "[": "push()",
                "]": "pop()",
                "-": "left(45)"})

branch = Lsystem("A", {"A": "F-[[A]+A]+F[+FA]-A",
                       "F": "FF"},
                 {"A": "forward(1)",
                  "F": "forward(1)",
                  "+": "right(25)",
                  "[": "push()",
                  "]": "pop()",
                  "-": "left(25)"})

krishna = Lsystem("-X--X", {"X": "XFX--XFX"},
                  {"F": "forward(4)",
                   "-": "left(45)"})

root = Lsystem("F", {"F": "―FF[+F][-F]"},
               {"F": "forward(1)",
                "+": "right(45)",
                "[": "push()",
                "]": "pop()",
                "-": "left(45)"})

chaosGame(5, 1 / 2, 1000000)
# root.draw(7, "images6\\root")
# feigenbaum(1/2)
image.show()

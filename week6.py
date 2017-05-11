import random

from PIL import Image

from Geometry import *

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)

def chaosGame(n, r):
    points = []
    angle = (n - 2) * np.math.pi / n
    for i in range(n):
        x = 2 * size // 2 * math.cos(angle) * i
        y = 2 * size // 2 * math.sin(angle) * i
        points.append(Point(x, y))
    x = random.randint(0, size - 10)
    y = random.randint(0, size - 10)
    point = Point(x, y)
    for i in range(10000):
        chosenOne = points[random.randint(0, n - 1)]
        point.x = int((chosenOne.x + point.x) * r)
        point.y = int((chosenOne.y + point.y) * r)
        if i > 100:
            image.putpixel((point.x, point.y), (0, 0, 0))


chaosGame(3, 1 / 2)
image.show()

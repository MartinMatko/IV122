from math import tan, sqrt

from Turtle import *

t = Turtle()
size = 500
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)


def drawRegularPolygon(n):
    for i in range(n):
        t.right(360 / n)
        t.forward(100)
    t.draw("images3\\polygon")


def drawStar(n, size=300):
    angle = 180 - (180 / n)
    t.penup()
    t.forward(size // 2)
    t.pendown()
    for i in range(n):
        t.right(angle)
        t.forward(size)
    t.draw("images3\\star")


def drawPentagram(size=150):
    for i in range(5):  # polygon
        t.right(360 / 5)
        t.forward(size)
    t.left(180 / 5)
    length = 2 * sin(radians((180 - 360 / 5) / 2)) * size
    angle = 180 - (180 / 5)

    for i in range(5):  # star
        t.right(angle)
        t.forward(length)
    t.draw("images3\\pentagram")


def drawNestedSquares(n=50, angle=45, size=200):
    for i in range(n):
        for j in range(4):
            t.forward(size)
            t.right(90)
        difference = size * tan(radians(angle)) / (1 + tan(radians(angle)))
        size = sqrt((size - difference) ** 2 + difference ** 2)
        t.forward(difference)
        t.right(angle)
    t.draw("images3\\squares")


def drawMeshedCircle(density=15, radius=200):
    #vykreslene absolutnymi poziciami je vhodnejsie v tomto pripade
    for i in range(-radius, radius, density):
        y = math.sqrt(radius ** 2 - i ** 2)
        point1 = Point(i, y)
        point2 = Point(i, -y)
        horizontalLine = Line(point1, point2)
        horizontalLine.drawLine(image, 500)

        point1 = Point(y, i)
        point2 = Point(-y, i)
        verticalLine = Line(point1, point2)
        verticalLine.drawLine(image, 500)
    image.show()
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images3\\meshedCircle.png")

def drawTriangles(depth):
    t.left(30)
    _drawTriangles(depth, 5)
    t.draw("images3\\triangles")

def _drawTriangles(depth, size):
    if depth == 0:
        return
    else:
        for j in range(3):
            t.forward(size)
            t.right(360 / 3)
        t.penup()
        t.right(210)
        t.forward(20)
        t.left(210)
        t.pendown()
        size += 2 * 20 * math.sin(radians(60))
        _drawTriangles(depth - 1, size)


# drawRegularPolygon(6)
# drawStar(13)
# drawPentagramRelative()
# drawsTheSquares(150,10,t,75)
# drawNestedSquares(50, 89, 200)
# drawMeshedCircle(10, 200)
drawTriangles(30)

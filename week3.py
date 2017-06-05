from math import tan, sqrt, degrees, sin
from random import randint, uniform

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
    # vykreslene absolutnymi poziciami je vhodnejsie v tomto pripade
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
    image.save("images3\\meshedCircle.png")


def drawTriangles(density):
    step = (200 * sin(radians(30))) / density
    t.left(30)
    for i in range(density):
        length = 200 - (i * (step / sin(radians(30))))
        for j in range(3):
            t.forward(length)
            t.right(360 / 3)
        t.penup()
        t.right(30)
        t.forward(step)
        t.left(30)
        t.pendown()
    t.draw("images3\\triangles")


def drawDiamond(size, density):
    for i in range(density):
        for j in range(density):
            t.right(360 // density)
            t.forward(size)
        t.right(360 // density)
    t.draw("images3\\diamond")


def tree(n):
    t.penup()
    t.forward(200)
    t.right(180)
    t.pendown()
    _tree(150, n)
    t.draw("images3\\tree")


def _tree(length, n):
    if n == 0:
        return
    t.forward(length)
    angle = 20 + randint(0, 40)  # uhol medzi vetvami
    ratio = uniform(0.5, 0.7)  # pomer dlzky vetiev k ich rodicom
    t.left(angle)
    _tree(length * ratio, n - 1)
    t.right(2 * angle)
    _tree(length * ratio, n - 1)
    t.left(angle)
    t.back(length)


def snowflake(depth):
    for i in range(3):
        _snowflake(200, depth)
        t.right(120)
    t.draw("images3\\snowflake")


def _snowflake(lengthSide, depth):
    if depth == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    _snowflake(lengthSide, depth - 1)
    t.left(60)
    _snowflake(lengthSide, depth - 1)
    t.right(120)
    _snowflake(lengthSide, depth - 1)
    t.left(60)
    _snowflake(lengthSide, depth - 1)


def hilbert(depth):
    t.penup()
    t.right(180)
    t.forward(size // 2)
    t.right(90)
    t.forward(size // 2)
    t.right(90)
    t.pendown()
    _hilbert(depth, 90)
    t.draw("images3\\hilbert90")


def _hilbert(level, angle):
    if level == 0:
        return
    t.right(angle)
    _hilbert(level - 1, -angle)
    t.forward(10)
    t.left(angle)
    _hilbert(level - 1, angle)
    t.forward(10)
    _hilbert(level - 1, angle)
    t.left(angle)
    t.forward(10)
    _hilbert(level - 1, -angle)
    t.right(angle)


def shell(ratio):
    for i in range(1, 27):
        a = 10 * i
        b = 10 * i * ratio
        c = math.sqrt(a ** 2 + b ** 2)
        angle = degrees(math.asin(b / c))
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(angle + 90)
        t.forward(c)
        t.right(180)
    t.draw("images3\\shell")


# drawRegularPolygon(6)
# drawStar(13)
# drawPentagramRelative()
# drawsTheSquares(150,10,t,75)
# drawNestedSquares(50, 89, 200)
# drawMeshedCircle(10, 200)
# drawTriangles(10)
# drawDiamond(15, 45)
# drawDiamond(15, 46)
# tree(20)
# snowflake(4)
# hilbert(5)
shell(1 / 1.618034)  # zlaty rez

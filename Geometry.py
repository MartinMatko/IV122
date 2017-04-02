from PIL import Image, ImageDraw
import math

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)
middle = size // 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getMovedPoint(self, angle, step, direction=1):
        xDifference = math.sin(angle) * step * direction
        yDifference = math.cos(angle) * step * direction
        return Point(self.x + xDifference, self.y + yDifference)


class Line:
    def __init__(self, p1, p2, isPenDown=True):
        self.p1 = p1
        self.p2 = p2
        self.isPenDown = isPenDown

    def is_point_on_line(self, point):
        if (min(self.p1.x, self.p2.x) <= point.x <= max(self.p1.x, self.p2.x)
            and min(self.p1.y, self.p2.y) <= point.y <= max(self.p1.y, self.p2.y)):
            return True
        else:
            return False

    def intersect(self, l):
        def line(p1, p2):
            A = (p1.y - p2.y)
            B = (p2.x - p1.x)
            C = (p1.x * p2.y - p2.x * p1.y)
            return A, B, -C

        L1 = line(self.p1, self.p2)
        L2 = line(l.p1, l.p2)

        D = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]

        if D != 0:
            x = Dx / D
            y = Dy / D
            p = Point(x, y)
            return self.is_point_on_line(p) and l.is_point_on_line(
                p)  # musim overit, lebo ma zaujimaju usecky a nie priamky

        return False

    def drawLine(self, image, size):
        draw = ImageDraw.Draw(image)
        draw.line((size // 2 + self.p1.x, size // 2 - self.p1.y, size // 2 + self.p2.x, size // 2 - self.p2.y), fill=10)
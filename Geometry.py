import math
from PIL import ImageDraw


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

    def isPointOnLine(self, point):
        if (min(self.p1.x, self.p2.x) < point.x < max(self.p1.x, self.p2.x)
            and min(self.p1.y, self.p2.y) < point.y < max(self.p1.y, self.p2.y)):
            return True
        else:
            return False

    def length(self):
        a = self.p2.x - self.p1.x
        b = self.p2.y - self.p1.y
        return math.sqrt(a ** 2 + b ** 2)

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
            # musim overit, lebo ma zaujimaju usecky a nie priamky
            if self.isPointOnLine(p) and l.isPointOnLine(p):
                return p
        return None

    def drawLine(self, image, size):
        draw = ImageDraw.Draw(image)
        draw.line((size // 2 + self.p1.x, size // 2 - self.p1.y, size // 2 + self.p2.x, size // 2 - self.p2.y), fill=10)

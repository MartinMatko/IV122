import sys
from math import cos, sin, radians

from PIL import Image
from PIL import ImageDraw

from Geometry import *

class Turtle:
    def __init__(self):
        self.path = []
        self.stack = []
        self.previousPosition = Point(0, 0)
        self.position = Point(0, 0)
        self.angle = 0
        self.isPenDown = True

    def forward(self, step):
        self.goto(step, -1)

    def back(self, step):
        self.goto(step, 1)

    def goto(self, step, direction):
        self.previousPosition = self.position
        self.position = self.previousPosition.getMovedPoint(self.angle, step, direction)
        line = Line(self.previousPosition, self.position, self.isPenDown)
        self.path.append(line)

    def right(self, angle):
        self.angle += radians(360 - angle)

    def left(self, angle):
        self.angle += radians(angle)

    def penup(self):
        self.isPenDown = False

    def pendown(self):
        self.isPenDown = True

    def draw(self, nameOfFile, color=(0, 0, 0), width=1):
        size = 500
        image = Image.new("RGB", (size, size), color="white")
        draw = ImageDraw.Draw(image)
        for line in self.path:
            if line.isPenDown:
                draw.line((line.p1.x + size//2, size//2 - line.p1.y, line.p2.x + size//2, size//2 - line.p2.y), color, width)
        image.show()
        image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\" + nameOfFile + ".png")

    def push(self):
        self.stack.append((self.position, self.angle, self.pendown))

    def pop(self):
        self.position, self.angle, self.isPenDown = self.stack.pop()

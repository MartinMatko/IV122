from PIL import Image, ImageDraw
import math
from Geometry import *

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)
middle = size // 2

def spiral():
    t = 0
    r = 1
    while r < middle:
        x = int(middle + r * math.cos(t % (2 * math.pi)))
        y = int(middle + r * math.sin(t % (2 * math.pi)))
        if r < middle / 2:
            image.putpixel((x, y), (int(r) * 2, int(r) * 4, 255 - int(r) * 2))
        else:
            image.putpixel((x, y), (int(r) * 2, 255 + int(middle / 2) - int(r) * 2, 255 - int(r) * 2))
        t += 0.001
        r += 0.002
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\spiral.png")


def circle_full(r):
    for x in range(size):
        for y in range(size):
            if (x - size / 2) ** 2 + (y - size / 2) ** 2 < r ** 2:
                image.putpixel((x, y), (255 % abs(x), 255 % abs(x + y), 255 % abs(y)))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\circle_full.png")


def circle_with_width(r):
    for x in range(size):
        for y in range(size):
            epsilon = size / 100
            if (((x - size / 2) ** 2 + (y - size / 2) ** 2) / (r - epsilon) ** 2) > 1 > (
                        ((x - size / 2) ** 2 + (y - size / 2) ** 2) / (r + epsilon) ** 2):
                image.putpixel((x, y), (x, x + y, y))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\circle_with_width.png")


def triangle(a):
    for x in range(size):
        for y in range(size):
            cartesianx = x - middle;
            cartesiany = -y + middle + a // 2;

            # y > 0 and y < -sqrt(3)*x + (sqrt(3)/2)*10 and y < sqrt(3)*x + (sqrt(3)/2)*10
            if 0 < cartesiany < -math.sqrt(3) * cartesianx + a * math.sqrt(3) / 2 and cartesiany < math.sqrt(
                    3) * cartesianx + a * math.sqrt(3) / 2:
                r = 255 // a * (a - x)
                g = 255 // a * (a - y)
                b = abs(255 - r - g)
                image.putpixel((x, y), (r, g, b))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\triangle.png")


def ellipse(a, b, angle):
    for x in range(size):
        for y in range(size):
            x_new = (x - middle) * math.cos(angle) - (y - middle) * math.sin(angle)
            y_new = (x - middle) * math.sin(angle) + (y - middle) * math.cos(angle)
            x_eq = x_new ** 2 / a ** 2
            y_eq = y_new ** 2 / b ** 2
            if x_eq + y_eq < 1:
                color = int(abs(x_eq + y_eq) * 255)
                image.putpixel((x, y), (color, color, color))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\elipse.png")


def polygon(points):
    lines = []
    points.append(points[0])
    for i in range(0, len(points) - 1):
        start = Point(points[i][0], points[i][1])
        end = Point(points[i + 1][0], points[i + 1][1])
        lines.append(Line(start, end))

    for x in range(size):
        for y in range(size):
            control_line = Line(Point(0, y), Point(x, y))
            counter = 0
            for line in lines:
                if control_line.intersect(line):
                    counter += 1
            if counter % 2 != 0:
                image.putpixel((x, y), (0, 0, 0))
    im = image.rotate(180)
    im.show()
    im.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\polygon.png")


def circle_ilusion():
    for x in range(size):
        for y in range(size):
            for z in range(1, size, int(size / 30)):
                epsilon = 0.5
                if (((x - size / 2) ** 2 + (y - size / 2) ** 2) / (z - epsilon) ** 2) > 1 \
                        and (((x - size / 2) ** 2 + (y - size / 2) ** 2) / (z + epsilon) ** 2) < 1:
                    image.putpixel((x, y), (0, 0, 0))
    margin = 20
    draw.line((middle, margin, size - margin, middle), fill=(0, 0, 0), width=3)
    draw.line((size - margin, middle, middle, size - margin), fill=(0, 0, 0), width=3)
    draw.line((middle, size - margin, margin, middle), fill=(0, 0, 0), width=3)
    draw.line((margin, middle, middle, margin), fill=(0, 0, 0), width=3)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\circle_ilusion.png")


def chessboard(circles, squares):
    white = (255, 255, 255)
    black = (0, 0, 0)
    r = (math.sqrt(2 * size ** 2) / 2) / circles
    a = size // squares
    for x in range(size):
        for y in range(size):
            # circles
            if math.sqrt((x - middle) ** 2 + (y - middle) ** 2) // r % 2 == 0:
                col = black
                opposite = white
            else:
                col = white
                opposite = black
            # squares
            if (x // a + y // a) % 2 == 0:
                image.putpixel((x, y), col)
            else:
                image.putpixel((x, y), opposite)
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\chessboard.png")


def lines():
    x = 0
    y = 0
    im = Image.new("RGB", (size, size), color="grey")
    rows = 10
    size_of_square = 22
    for line in range(rows):
        x = (line % 2) * size_of_square // 2;
        draw_row(x, y, rows // 2, size_of_square, im)
        y = y + size_of_square + 2
    im.show()
    im.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images4\\lines.png")


def draw_row(x, y, pairs, size_of_square, image):
    white = (255, 255, 255)
    black = (0, 0, 0)
    for i in range(pairs):
        draw_square(x, y, size_of_square, black, image)
        draw_square(x + size_of_square, y, size_of_square, white, image)
        x += size_of_square * 2


def draw_square(x, y, size, color, image):
    for i in range(size):
        for j in range(size):
            image.putpixel((x + i, y + j), color)


# spiral()
# circle_full(80)
# circle_with_width(80)
# ellipse(100, 50, math.pi/4)
# polygon([[10, 10], [180, 20], [160, 150], [100, 50], [20, 180]])
# circle_ilusion()
# lines()
chessboard(6, 10)
image.show()

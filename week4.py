from PIL import Image, ImageDraw
import math

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)
middle = int(size / 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def point_on_line(self, point):
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
            return self.point_on_line(p) and l.point_on_line(p) #musim overit, lebo ma zaujimaju usecky a nie priamky

        return False


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
            if 0.9 < ((x - size / 2) ** 2 + (y - size / 2) ** 2) / r ** 2 < 1.1:
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


def elipse(a, b, angle):
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


# spiral()
# circle_full(80)
# circle_with_width(80)
# elipse(100, 50, math.pi/4)
polygon([[10, 10], [180, 20], [160, 150], [100, 50], [20, 180]])

# image.show()

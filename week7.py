import colorsys

from PIL import Image

from Geometry import *

size = 255
image = Image.new("RGB", (size, size), color="white")
draw = ImageDraw.Draw(image)
middle = size // 2


def mandelbrot(zoom=((-2, 1), (-1.5, 1))):
    for i in range(size):
        for j in range(size):
            zoomX = zoom[0][1] - zoom[0][0]
            zoomY = zoom[1][1] - zoom[1][0]
            realPart = zoom[0][0] + i * max(zoomX, zoomY) / size
            imaginaryPart = zoom[1][0] + j * max(zoomX, zoomY) / size
            c = complex(realPart, imaginaryPart)
            z = complex(0, 0)
            steps = 0
            while abs(z) <= 2 and steps < 30:
                zPrevious = z
                # z = z*z + c
                z = z * z + c * c * c * c
                steps += 1
            if abs(z) <= 2:
                image.putpixel((i, j), (int(255 * abs(z) + 1), 0, 0))
                # image.putpixel((i, j), (int(255 * abs(c) + 1), 0, 0))
            else:
                # smooth = steps + 1 - (math.log(abs(zPrevious) + 1))/math.log(2)
                # smooth = steps + 1 - math.log(abs(z) - abs(zPrevious) + 1)/math.log(2)
                smooth = steps + 1 - math.log(math.log(abs(z) + 1)) / math.log(2)
                image.putpixel((i, j), hsv2rgb(smooth / 30, 1, 1))
                # image.putpixel((i, j), ((255 // 30 * steps), (255 // 30 * steps), (255 // 30 * steps)))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images7\\mandelbrotColouredZZCCCC.png")


def hsv2rgb(h, s, v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def julia(a, b, zoom=((-2, 1), (-1.5, 1))):
    for i in range(size):
        for j in range(size):
            zoomX = zoom[0][1] - zoom[0][0]
            zoomY = zoom[1][1] - zoom[1][0]
            realPart = zoom[0][0] + i * max(zoomX, zoomY) / size
            imaginaryPart = zoom[1][0] + j * max(zoomX, zoomY) / size
            z = complex(realPart, imaginaryPart)
            c = complex(a, b)
            steps = 1
            while abs(z) <= 2 and steps < 30:
                z = z * z + c
                steps += 1
            if abs(z) <= 2:
                image.putpixel((i, j), (int(255 * abs(z) + 1), 0, 0))
            else:
                smooth = steps + 1 - math.log(math.log(abs(z) + 1)) / math.log(2)
                image.putpixel((i, j), hsv2rgb(smooth / 30, 1, 1))
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images7\\julia" + str(a) + "b=" + str(b) + ".png")


def newton(zoom=((-2, 2), (-2, 2))):
    roots = []
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    for i in range(size):
        for j in range(size):
            zoomX = zoom[0][1] - zoom[0][0]
            zoomY = zoom[1][1] - zoom[1][0]
            realPart = zoom[0][0] + i * max(zoomX, zoomY) / size
            imaginaryPart = zoom[1][0] + j * max(zoomX, zoomY) / size
            z = complex(realPart, imaginaryPart)
            z, steps = newtonMethod(z)
            if z:
                correspondingRootFound = False
                for root in roots:
                    if abs(root - z) < 0.1:
                        z = root
                        correspondingRootFound = True
                        break
                if not correspondingRootFound:
                    roots.append(z)
                image.putpixel((i, j), (steps, steps, steps))
                #image.putpixel((i, j), colors[roots.index(z)])
    image.save("C:\\Users\\Martin\\Dropbox\\Skola\\IV122\\images7\\newtonStepsPower3.png")


def newtonMethod(z):
    steps = 1
    while steps < 60:
        if z == 0: #mozne delenie nulou
            return None, None
        zNew = z - (z ** 3 - 1) / (3 * z ** 2)
        if abs(zNew - z) < 0.01:
            return z, steps
        z = zNew
        steps += 1
    return None, None

# mandelbrot()
# mandelbrot(((-1.9, -1.6),(-0.3, 0.3)))
# julia(0.3, 0.01)
newton()
#newton(((0.3, 0.6), (0.3, 0.6)))
image.show()

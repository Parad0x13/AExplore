# https://int10h.org/oldschool-pc-fonts/fontlist/

from PIL import Image

class FontManager:
    def __init__(self, filename, fileW, fileH, fontW, fontH):
            self.filename = filename
            self.fileW = fileW
            self.fileH = fileH
            self.fontW = fontW
            self.fontH = fontH

            im = Image.open(self.filename)
            self.px = im.load()
            self.computePatterns()

    def render(self, pixels):
        for line in pixels:
            for pixel in line:
                if pixel == 0: print(".", end = "")
                else: print("X", end = "")
            print()
        print()

    def grab(self, x, y):
        pixels = []
        X = x * 8
        Y = y * 16
        for y in range(16):
            line = []
            for x in range(8):
                val = 1
                pixel = self.px[X + x, Y + y]
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0: val = 0
                line.append(val)
            pixels.append(line)
        return pixels

    def computePatterns(self):
        self.patterns = []
        for y in range(self.fileH):
            for x in range(self.fileW):
                pattern = self.grab(x, y)
                self.patterns.append(pattern)

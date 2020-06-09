# !/usr/bin/python3
from tkinter import *
from FontManager import FontManager

top = Tk()
canvas = Canvas(top, bg = "black", width = 10 * 80, height = 20 * 16, borderwidth = 0, highlightthickness = 0)
canvas.pack()

fm = FontManager("BM437.png", 64, 4, 8, 16)
globalScale = 5.0

class Entity:
    def __init__(self, canvas, fm, x, y, iconIndex, color = "limegreen", tags = ""):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.tags = tags

        pixels = fm.patterns[iconIndex]
        for Y in range(len(pixels)):
            for X in range(len(pixels[Y])):
                pixel = pixels[Y][X]
                if pixel == 1:
                    x1 = self.x * 8 + X
                    y1 = self.y * 16 + Y
                    x2 = x1 + 1
                    y2 = y1 + 1
                    canvas.create_rectangle(canvas.canvasx(x1), canvas.canvasy(y1), canvas.canvasx(x2), canvas.canvasy(y2), fill = self.color, width = 0, tags = self.tags)

class Player(Entity):
    def __init__(self, canvas, fm, x, y):
        super().__init__(canvas = canvas, fm = fm, x = x, y = y, iconIndex = 1, color = "limegreen", tags = "player")
        self.canvas.bind_all("<Key>", self.keyPressed)

    def keyPressed(self, e):
        key = e.keysym

        # [TODO] These pixel measurements should not be hardcoded
        deltaX = 8 * globalScale
        deltaY = 16 * globalScale

        # [TODO] Make this move to an absolute position, or calculate it dynamically. Don't do it this way
        if key == "w":
            self.y -= 1
            self.canvas.move(self.tags, 0, -deltaY)

        if key == "s":
            self.y += 1
            self.canvas.move(self.tags, 0, deltaY)

        if key == "a":
            self.x -= 1
            self.canvas.move(self.tags, -deltaX, 0)

        if key == "d":
            self.x += 1
            self.canvas.move(self.tags, deltaX, 0)

        self.canvas.update()

player = Player(canvas = canvas, fm = fm, x = 0, y = 0)
b = Entity(canvas, fm, 1, 1, 2, color = "blue", tags = "enemy")
canvas.scale("all", 0, 0, globalScale, globalScale)    # [TODO] There has got to be a better way to do this...

top.mainloop()

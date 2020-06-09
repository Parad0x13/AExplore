# !/usr/bin/python3
from tkinter import *
from FontManager import FontManager

top = Tk()
canvas = Canvas(top, bg = "black", width = 10 * 80, height = 20 * 16, borderwidth = 0, highlightthickness = 0)
#canvas.scale("all", 0, 0, 4, 4)
canvas.pack()

"""
def renderFont(fontManager, index, x, y, color = "limegreen", tags = ""):
    x *= fontManager.fontW * scale
    y *= fontManager.fontH * scale

    pixels = fontManager.patterns[index]
    for Y in range(len(pixels)):
        for X in range(len(pixels[Y])):
            pixel = pixels[Y][X]
            if pixel == 1:
                x1 = x + (X * scale)
                y1 = y + (Y * scale)
                x2 = x1 + scale
                y2 = y1 + scale
                canvas.create_rectangle(canvas.canvasx(x1), canvas.canvasy(y1), canvas.canvasx(x2), canvas.canvasy(y2), fill = color, width = 0, tags = tags)
"""

fm = FontManager("BM437.png", 64, 4, 8, 16)

#renderFont(fm, 1, 10, 1, "blue", tags = "player")

"""
def onKeyPressed(e):
    key = e.keysym

    deltaX = 8 * scale
    deltaY = 16 * scale

    if key == "w": canvas.move("player", 0, -deltaY)
    if key == "s": canvas.move("player", 0, deltaY)
    if key == "a": canvas.move("player", -deltaX, 0)
    if key == "d": canvas.move("player", deltaX, 0)

    canvas.update()

canvas.bind_all("<Key>", onKeyPressed)

def tick(): top.after(16, tick)
top.after(16, tick)
"""

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

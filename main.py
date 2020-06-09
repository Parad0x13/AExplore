# !/usr/bin/python3
from tkinter import *
from FontManager import FontManager

root = Tk()
canvas = Canvas(root, bg = "black", width = 10 * 80, height = 20 * 16, borderwidth = 0, highlightthickness = 0)
canvas.pack()

fm = FontManager("BM437.png", 64, 4, 8, 16)
globalScale = 5.0

# [TODO] Create frames instead of drawing directly onto the canvas so it can be manipulated better later on
def generateFrame(canvas, fm, x, y, iconIndex, color, tags):
    pass

class Sprite:
    def __init__(self, x, y, iconIndex, color = "limegreen", tags = "", state = "normal"):
        self.x = x
        self.y = y
        self.color = color
        self.tags = tags
        self.state = state

        self.IDs = []
        pixels = fm.patterns[iconIndex]
        for Y in range(len(pixels)):
            for X in range(len(pixels[Y])):
                pixel = pixels[Y][X]
                if pixel == 1:
                    x1 = self.x * 8 + X
                    y1 = self.y * 16 + Y
                    x2 = x1 + 1
                    y2 = y1 + 1
                    newID = canvas.create_rectangle(canvas.canvasx(x1), canvas.canvasy(y1), canvas.canvasx(x2), canvas.canvasy(y2), fill = self.color, width = 0, tags = self.tags, state = self.state)
                    self.IDs.append(newID)

    def toggleHidden(self):
        if self.state == "normal": self.state = "hidden"
        else: self.state = "normal"

        for ID in self.IDs:
            canvas.itemconfigure(ID, state = self.state)

"""
class Player(Sprite):
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
"""

class Entity:
    def __init__(self, sprites):
        self.sprites = sprites
        self.currentTick = 0

    def tick(self, delta):
        self.currentTick += delta

class Player(Entity):
    def __init__(self, x, y):
        a = Sprite(x, y, 1, color = "limegreen", tags = "player", state = "normal")
        b = Sprite(x, -1.0 / 16.0, 1, color = "limegreen", tags = "player", state = "hidden")
        super().__init__([a, b])

    def tick(self, delta):
        super().tick(delta)

        if self.currentTick > 1000:
            self.currentTick = 0
            for sprite in self.sprites:
                sprite.toggleHidden()

class Water(Entity):
    def __init__(self, x, y):
        a = Sprite(x, y, 177, color = "lightblue", tags = "water", state = "normal")
        b = Sprite(x, y, 178, color = "lightblue", tags = "water", state = "hidden")
        super().__init__([a, b])

    def tick(self, delta):
        super().tick(delta)

        if self.currentTick > 500:
            self.currentTick = 0
            for sprite in self.sprites:
                sprite.toggleHidden()

class Fire(Entity):
    def __init__(self, x, y):
        a = Sprite(x, y, 189, color = "red", tags = "fire", state = "normal")
        b = Sprite(x, y, 190, color = "red", tags = "fire", state = "hidden")
        super().__init__([a, b])

    def tick(self, delta):
        super().tick(delta)

        if self.currentTick > 200:
            self.currentTick = 0
            for sprite in self.sprites:
                sprite.toggleHidden()

player = Player(x = 0, y = 0)
water = Water(x = 3, y = 2)
fire = Fire(x = 1, y = 1)
entities = [player, water, fire]

tickPeriod = int((1.0 / 30.0) * 1000)
def tick():
    for entity in entities:
        entity.tick(tickPeriod)

    root.after(tickPeriod, tick)
root.after(0, tick)

canvas.scale("all", 0, 0, globalScale, globalScale)    # [TODO] There has got to be a better way to do this...
root.mainloop()

# !/usr/bin/python3
from tkinter import *
from FontManager import FontManager

top = Tk()
C = Canvas(top, bg = "black", width = 320, height = 200, borderwidth = 0, highlightthickness = 0)
C.pack()

scale = 5.0    # Global to canvas
def renderFont(fontManager, index, x, y, color = "limegreen"):
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
                C.create_rectangle(C.canvasx(x1), C.canvasy(y1), C.canvasx(x2), C.canvasy(y2), fill = color, width = 0)

fm = FontManager("BM437.png", 64, 4, 8, 16)
renderFont(fm, 1, 0, 0, "blue")
renderFont(fm, 2, 1, 1, "yellow")

top.mainloop()

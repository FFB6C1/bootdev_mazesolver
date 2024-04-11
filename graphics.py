import checks
from tkinter import Tk, BOTH, Canvas

colours = {"background": "AntiqueWhite3",
           "cellBg": "AntiqueWhite1",
           "cellWall": "RosyBrown4",
           "pathActive": "OliveDrab",
           "pathInactive": "AntiqueWhite3",
           }

class Window():
    def __init__(self, width, height):
        checks.typeCheck("Window", "width", width, type(1))
        checks.typeCheck("Window", "height", height, type(1))

        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._width = width
        self._height = height
        self._active = False
        self.canvas = Canvas(self._root, 
                             width=800, 
                             height=600, 
                             background=colours["background"]
                             )
        self.canvas.pack()

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def waitForClose(self):
        self._active = True
        while self._active:
            self.redraw()

    def close(self):
        self._active = False

    def drawLine(self, line, colour):
        newLine = line.draw(self.canvas, colour)
        return newLine

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        checks.typeCheck("line", "point1", point1, type(Point(0, 0)))
        checks.typeCheck("line", "point2", point2, type(Point(0, 0)))

        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, colour):
        line = canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill = colour,
            width = 2,
        )
        canvas.pack()
        return line
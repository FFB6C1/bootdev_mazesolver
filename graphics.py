import checks
from tkinter import Tk, BOTH, Canvas

colours = {"background": "AntiqueWhite3"}

class Window():
    def __init__(self, dimensions):
        checks.typeCheck("Window", "dimensions", dimensions, type([]))
        checks.lenCheck("Window", "dimensions", dimensions, 2, 2)

        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._width = dimensions[0]
        self._height = dimensions[1]
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
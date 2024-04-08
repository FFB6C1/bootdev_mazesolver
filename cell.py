from graphics import (
    colours,
    Window,
    Point,
    Line,
)
import checks

class Cell():
    def __init__(self, position, width, height, win):
        checks.typeCheck("Cell", "position", position, type(Point(0,0)))
        checks.typeCheck("Cell", "width", width, type(1))
        checks.typeCheck("Cell", "height", height, type(1))

        self.walls = 0b1111
        self._x1 = position.x
        self._x2 = position.x + width
        self._y1 = position.y
        self._y2 = position.y + height
        self.centre = Point(position.x + width/2, position.y + height/2)
        self._win = win

    def draw(self):
        self._win.canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, fill=colours["cellBg"], outline = "")
        
        topLeft = Point(self._x1, self._y1)
        topRight = Point(self._x2, self._y1)
        bottomRight = Point(self._x2, self._y2)
        bottomLeft = Point(self._x1, self._y2)

        wallColour = colours["cellWall"]

        wallLines = [
            Line(topLeft, topRight),
            Line(topRight, bottomRight),
            Line(bottomRight, bottomLeft),
            Line(bottomLeft, topLeft)
        ]

        if self.walls & 0b0001 == 0b0001:
            self._win.drawLine(wallLines[0], wallColour)
        if self.walls & 0b0010 == 0b0010:
            self._win.drawLine(wallLines[1], wallColour)
        if self.walls & 0b0100 == 0b0100:
            self._win.drawLine(wallLines[2], wallColour)
        if self.walls & 0b1000 == 0b1000:
            self._win.drawLine(wallLines[3], wallColour)

    def drawMove(self, destination, undo = False):
        checks.typeCheck("drawMove", "destination", destination, Cell)
        path = Line(self.centre, destination.centre)
        if undo:
            colour = colours["pathInactive"]
        else:
            colour = colours["pathActive"]
        self._win.drawLine(path, colour)

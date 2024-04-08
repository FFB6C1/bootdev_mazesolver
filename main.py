from graphics import (
    Window,
    Point,
    Line
)

from cell import (
    Cell,
)

def main():
    newWin = Window(800, 600)

    newCell = Cell(Point(10, 10), 50, 50, newWin)
    newCell2 = Cell(Point(200, 200), 40, 80, newWin)
    newCell.draw()
    newCell2.draw()
    newCell.drawMove(newCell2)

    newWin.waitForClose()


main()
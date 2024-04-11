from graphics import (
    Window,
    Point,
    Line
)
from maze import Maze

from cell import (
    Cell,
)

def main():
    newWin = Window(800, 600)

    newMaze = Maze(Point(50, 50), 24, 20, 20, 20, newWin)

    newWin.waitForClose()


main()
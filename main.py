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
    window_height = 800
    window_width = 600
    cell_width = 20
    cell_height = 20
    border = 50
    row_size = (window_height - (border*2))//cell_height
    col_size = (window_width - (border*2))//cell_width

    newWin = Window(window_height, window_width)
    newMaze = Maze(Point(border, border), row_size, col_size, cell_width, cell_height, newWin)
    newMaze.solve()

    newWin.waitForClose()


main()
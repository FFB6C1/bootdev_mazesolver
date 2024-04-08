from graphics import Window, Point, Line, Cell
from maze import Maze

#Cell wall notes: the walls of the cells are represented by a 4bit binary
#starting with the top, the walls go clockwise.
#examples: 
#0b1000 is top wall, no other walls
#0b1011 is top, bottom and left walls with a gap to the right

def main():
    new_win = Window(800, 600)
    new_maze = Maze(Point(100, 100), Point(12, 10), Point(40, 40), new_win)

    new_win.wait_for_close()

main()
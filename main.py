from graphics import Window, Point, Line, Cell

def main():
    new_win = Window(800, 600)
    new_cell = Cell(new_win, 0b1011, Point(200, 200))
    new_cell2 = Cell(new_win, 0b1110, Point(240, 200))

    new_cell.draw()
    new_cell2.draw()
    new_cell.draw_move(new_cell2, True)

    new_win.wait_for_close()

main()
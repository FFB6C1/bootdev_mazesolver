from graphics import Point, Cell
import random
import time

class Maze():
    def __init__(self, position, dimensions, cell_dimensions, win):
        #value tests
        if not isinstance(position, Point):
            raise ValueError("Maze(): position argument expects a Point (Point(x,y)) input")
        if not isinstance(dimensions, Point):
            raise ValueError("Maze(): dimensions argument expects a Point (Point(x,y)) input")
        if not isinstance(cell_dimensions, Point):
            raise ValueError("Maze(): cell_dimensions argument expects a Point (Point(x,y)) input")
        
        self.x = position.x
        self.y = position.y
        self.rows = dimensions.x
        self.cols = dimensions.y
        self.cell_x = cell_dimensions.x
        self.cell_y = cell_dimensions.y
        self.win = win

        #create cells
        self.cells = self._create_cells()
        self._draw_cells()

    def _create_cells(self):
        cells = []
        for i in range(0, self.cols):
            new_row = []
            for j in range(0, self.rows):
                walls = int(bin(random.randrange(1,16)), 2)
                x_pos = self.x + (j * self.cell_x)
                y_pos = self.y + (i * self.cell_y)
                new_row.append(Cell(self.win, walls, Point(x_pos, y_pos), [self.cell_x, self.cell_y]))
            cells.append(new_row)
        return cells
    
    def _draw_cells(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
                self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


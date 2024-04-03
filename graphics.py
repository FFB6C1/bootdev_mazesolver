from tkinter import Tk, BOTH, Canvas

wall_color = "dark green"
fill_color = "white"
line_color = "orange"
undo_color = "lightgrey"

class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Root Widget"
        self.canvas = Canvas(self.root_widget, {"width": width, "height": height, "bg": "grey"})
        self.canvas.pack(fill=BOTH, expand=1)
        self.active = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.active = True
        while self.active == True:
            self.redraw()

    def close(self):
        self.active = False

    def draw_line(self, line, fill):
        line.draw(self.canvas, fill)
        self.canvas.pack(fill=BOTH, expand=1)

    def draw_fill(self, point1, point2, fill):
        self.canvas.create_rectangle([point1.x, point1.y, point2.x, point2.y], fill = fill, outline = "")
        self.canvas.pack(fill=BOTH, expand=1)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill, width = 2
        )

class Cell():
    size = 40
    def __init__(self, win, walls = 0b0000, pos = Point(0, 0)):
        self.walls = walls
        self._x1 = pos.x
        self._x2 = pos.x + self.size
        self._y1 = pos.y
        self._y2 = pos.y + self.size
        self._win = win

    def draw(self):
        self._win.draw_fill(Point(self._x1, self._y1), Point(self._x2, self._y2), fill_color)
        if 0b1000 & self.walls == 0b1000:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, wall_color)
        if 0b0100 & self.walls == 0b0100:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, wall_color)
        if 0b0010 & self.walls == 0b0010:
            bottom_wall = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(bottom_wall, wall_color)
        if 0b0001 & self.walls == 0b0001:
            left_wall = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
            self._win.draw_line(left_wall, wall_color)
    
    def draw_move(self, to_cell, undo = False):
        move_line = Line(
            Point(self._x1 + self.size/2, self._y1 + self.size/2), Point(to_cell._x1 + to_cell.size/2, to_cell._y1 + to_cell.size/2))
        if undo:
            fill = undo_color
        else:
            fill = line_color
        self._win.draw_line(move_line, fill)
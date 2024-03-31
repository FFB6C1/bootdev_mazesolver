from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = "Window."
        self.canvas = Canvas(self.root_widget, {"width": self.width, "height": self.height, "bg": "grey"})
        self.canvas.pack()
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

def main():
    new_win = Window(800, 600)
    new_win.wait_for_close()

main()
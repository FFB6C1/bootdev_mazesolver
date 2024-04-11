from cell import Cell
from graphics import Point
from time import sleep
import random

class Maze():
    def __init__(self, position, rows, cols, cellWidth, cellHeight, win = None, seed = None):
        self.x = position.x
        self.y = position.y
        self.rows = rows
        self.cols = cols
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self._win = win
        self.createCells()
        if self._win != None:
            self.drawCells()
            self.makeExits()
            self.pathCells = []
            self.makePaths(self.maze[0][0])
            self.resetVisited()

    def createCells(self):
        self.maze = []
        for i in range(self.rows):
            new_col = []
            for j in range(self.cols):
                posX = self.x + i*self.cellWidth
                posY = self.y + j*self.cellHeight
                new_col.append(Cell(Point(posX, posY), self.cellWidth, self.cellHeight, self._win, [i, j]))
            self.maze.append(new_col)
        
    def drawCells(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.maze[j][i].draw()
                self.animate()

    def animate(self):
        self._win.redraw()
        sleep(0.005)

    def makeExits(self):
        self.maze[0][0].breakWall("left")
        self.maze[self.rows-1][self.cols-1].breakWall("right")

    def makePaths(self, cell):
        cell.visit()
        if cell not in self.pathCells:
            self.pathCells.append(cell)
        directions = []
        row = cell.coords[0]
        col = cell.coords[1]

        if row > 0 and self.maze[row-1][col].visited == False:
            directions.append(["left", self.maze[row-1][col], "right"])
        if row < self.rows-1 and self.maze[row+1][col].visited == False:
            directions.append(["right", self.maze[row+1][col], "left"])
        if col > 0 and self.maze[row][col-1].visited == False:
            directions.append(["up", self.maze[row][col-1], "down"])
        if col < self.cols-1 and self.maze[row][col+1].visited == False:
            directions.append(["down", self.maze[row][col+1], "up"])

        if directions == []:
            if len(self.pathCells) < self.rows * self.cols:
                self.makePaths(self.pathCells[random.randrange(0, len(self.pathCells))])
            return
            

        destination = directions[random.randrange(0, len(directions))]
        cell.breakWall(destination[0])
        destination[1].breakWall(destination[2])

        self.animate()
        self.makePaths(destination[1])
        return

    def resetVisited(self):
        for col in self.maze:
            for cell in col:
                cell.unvisit()
                

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
        self.solved = False
        self.cellsUnvisited = set()
        self.createCells()
        self.cellsPathed = []
        if self._win != None:
            self.drawCells()
            self.goalCell = self.maze[self.rows-1][self.cols-1]
            self.makeExits()
            self.makePaths()
            self.resetVisited()

    def createCells(self):
        self.maze = []
        for i in range(self.rows):
            new_col = []
            for j in range(self.cols):
                posX = self.x + i*self.cellWidth
                posY = self.y + j*self.cellHeight
                new_col.append(Cell(Point(posX, posY), self.cellWidth, self.cellHeight, self._win, [i, j]))
                self.cellsUnvisited.add(f"{i},{j}")
            self.maze.append(new_col)
        
    def drawCells(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.maze[j][i].draw()

    def animate(self):
        self._win.redraw()
        sleep(0.005)

    def makeExits(self):
        self.maze[0][0].breakWall("left")
        self.maze[self.rows-1][self.cols-1].breakWall("right")

    def checkVisited(self):
        if len(self.cellsUnvisited) != 0:
            self.makePaths(self.cellsPathed[random.randrange(0, len(self.cellsPathed))])

    def makePaths(self):
        self.makePathsR(self.maze[0][0])
        while len(self.cellsUnvisited) > 0:
            self.makePathsR(self.cellsPathed[random.randrange(0,len(self.cellsPathed))])

    def makePathsR(self, cell):
        if cell not in self.cellsPathed:
            cell.visit()
            self.cellsPathed.append(cell)
            self.cellsUnvisited.remove(f"{cell.coords[0]},{cell.coords[1]}")
        to_visit = []
        if cell.coords[0] > 0 and self.maze[cell.coords[0] - 1][cell.coords[1]].visited == False:
            to_visit.append([self.maze[cell.coords[0] - 1][cell.coords[1]], "left", "right"])
        if cell.coords[0] < self.rows-1 and self.maze[cell.coords[0] + 1][cell.coords[1]].visited == False:
            to_visit.append([self.maze[cell.coords[0] + 1][cell.coords[1]], "right", "left"])
        if cell.coords[1] > 0 and self.maze[cell.coords[0]][cell.coords[1] - 1].visited == False:
            to_visit.append([self.maze[cell.coords[0]][cell.coords[1] - 1], "up", "down"])
        if cell.coords[1] < self.cols-1 and self.maze[cell.coords[0]][cell.coords[1] + 1].visited == False:
            to_visit.append([self.maze[cell.coords[0]][cell.coords[1] + 1], "down", "up"])
        if len(to_visit) == 0:
            return
        number = random.randrange(0, len(to_visit))
        destinationCell = to_visit[number]
        cell.breakWall(destinationCell[1])
        destinationCell[0].breakWall(destinationCell[2])
        self.animate()
        self.makePathsR(destinationCell[0])
        return

    def resetVisited(self):
        for row in self.maze:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self.solveR(self.maze[0][0])
    
    def solveR(self, cell):
        self.animate()
        cell.visit()
        if cell == self.goalCell:
            return True
        next_cells = self.checkDir(cell)
        if next_cells == []:
            return False
        for c in next_cells:
            cell.drawMove(c)
            if self.solveR(c) == True:
                return True
            else:
                cell.drawMove(c, True)
        
    def checkDir(self, cell):
        directions = []
        if ( cell.coords[0] > 0 and 
            cell.checkWall("left") == False and 
            self.maze[cell.coords[0] - 1][cell.coords[1]].visited == False ):
            directions.append(self.maze[cell.coords[0] - 1][cell.coords[1]])
        if ( cell.coords[0] < self.rows - 1 and
            cell.checkWall("right") == False and
            self.maze[cell.coords[0] + 1][cell.coords[1]].visited == False):
            directions.append(self.maze[cell.coords[0] + 1][cell.coords[1]])
        if ( cell.coords[1] > 0 and
            cell.checkWall("up") == False and
            self.maze[cell.coords[0]][cell.coords[1] - 1].visited == False):
            directions.append(self.maze[cell.coords[0]][cell.coords[1] - 1])
        if ( cell.coords[1] < self.cols - 1 and
            cell.checkWall("down") == False and
            self.maze[cell.coords[0]][cell.coords[1] + 1].visited == False):
            directions.append(self.maze[cell.coords[0]][cell.coords[1] + 1])
        return directions
        


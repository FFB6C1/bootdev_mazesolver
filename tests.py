import unittest
from maze import Maze
from graphics import Point

class Tests(unittest.TestCase):
    def testMazeCreation(self):
        rows = 10
        cols = 12
        height = 50
        width = 60
        maze = Maze(Point(0,0), rows, cols, height, width)

        self.assertEqual(rows, len(maze.maze))
        self.assertEqual(cols, len(maze.maze[0]))

if __name__ == "__main__":
    unittest.main()
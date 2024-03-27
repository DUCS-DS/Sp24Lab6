from queue_ import Queue

class Maze:
    """Traverse and print a solved maze.

    Upon instantiation of this class, a grid with entries -1
    and 1 similar to below is created.

         -1  0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
         -1  0  0  0 -1  0 -1 -1 -1  0  0  0  0  0  0  0 -1
         -1  0 -1 -1 -1  0 -1  0  0  0 -1 -1 -1  0 -1  0 -1
         -1  0  0  0  0  0 -1  0 -1  0 -1  0 -1 -1 -1  0 -1
         -1 -1 -1 -1 -1  0  0  0 -1  0 -1  0 -1  0 -1  0 -1
         -1  0  0  0 -1  0  0  0 -1  0 -1  0  0  0 -1  0 -1
         -1  0 -1  0 -1 -1 -1 -1 -1  0 -1 -1 -1  0 -1  0 -1
         -1  0 -1  0  0  0  0  0  0  0  0  0  0  0 -1  0 -1
         -1  0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  0 -1
         -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 -1
         -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  0 -1

    The grid represents a maze as follows:

           -1 indicates a wall.
            0 indicates a valid next position during traversal.

    The starting position for a traversal of the maze is (0,1)
    near the upper left corner.  The maze is solved when a tra-
    versal reaches the exit position near the lower right corn-
    er.  A valid traversal cannot go through walls, of course.

    The shortestPath method below finds a shortest path through
    the maze and modifies the entries in self.grid so as to ill-
    ustrate a shortest path via this class's __str__ method.
    """

    def __init__(self):
        """Set up the grid for the maze and set some constants."""

        self.WALL = -1
        self.UNVISITED = 0

        self.grid = \
        [[-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
         [-1, 0,-1,-1,-1, 0,-1, 0, 0, 0,-1,-1,-1, 0,-1, 0,-1,-1,-1],
         [-1, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1, 0, 0, 0,-1],
         [-1,-1,-1,-1,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1],
         [-1, 0, 0, 0,-1, 0, 0, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
         [-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1,-1,-1, 0,-1, 0,-1, 0,-1],
         [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1],
         [-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1],
         [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
         [-1, 0,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1, 0,-1,-1],
         [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1]]

        self.ENTRY = (0, 1)
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])
        self.EXIT = (self.ROWS - 1, self.COLS - 2)

    def shortestPath(self):
        """Return the number of steps in a shortest traversal.

        If no complete traversal exists, return None.  This method
        also modifies self.grid in such a way that a shortest path
        is evident in the string representation of the maze.
        """
        q = Queue()
        q.enqueue((self.ENTRY, 0))
        while q.length() > 0:
            break  # remove this line

            #
            #  your code goes here
            #

        return None

    def isMoveValid(self, nextPos):
        """Return True if nextPos is a valid move; otherwise, return False.

        The argument to nextPos is a valid move if it is not a wall, has not
        been visited previously, and is within the maze.
        """
        valid = 1 <= nextPos[0]
        if valid:
            value = self.grid[nextPos[0]][nextPos[1]]
        return valid and value != self.WALL and value == self.UNVISITED

    def nextMoves(self, curPos):
        """Return a list containing the valid next moves."""

        nextMoves = []
        x = curPos[0]
        y = curPos[1]
        for pos in  [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if self.isMoveValid(pos):
                nextMoves.append(pos)
        return nextMoves

    def __str__(self):
        """Return a string representation."""

        mazeStr = "\n"
        for row in self.grid:
            for colVal in row:
                if row == self.grid[0] and colVal == 0:
                    mazeStr += str(colVal) + " " * (2 - len(str(colVal)))
                elif colVal == -1:
                    mazeStr += '.' + " "
                elif colVal == 0:
                    mazeStr += ' ' + " "
                elif colVal > 0:
                    mazeStr += str(colVal) + " " * (2 - len(str(colVal)))
                elif colVal < -1:
                    mazeStr += '*' + " "
            mazeStr += "\n"
        return mazeStr

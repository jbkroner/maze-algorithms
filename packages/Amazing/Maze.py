from Amazing.Nodes.MazeNode import MazeNode

class Maze():
    def __init__(self, cols:int = 20, rows: int = 20) -> None:

        self.cols = cols
        self.rows = rows

        # define and populate with new maznodes
        self.grid = [[MazeNode()]*cols]*rows

        # associate neighbors
        for col in range(self.grid):
            for row in range(self.grid[col]):
                # current node
                node = self.grid[col][row]

                # north neighbor
                if row - 1 >= 0:
                    node.northNeighbor = self.grid[col][row - 1]

                # east neighbor
                if col + 1 < len(self.cols):
                    node.eastNeighbor = self.grid[col + 1][row]

                # south neighbor
                if row + 1 < len(self.rows):
                    node.southNeighbor = self.grid[col][row + 1]

                # west neighbor
                if col - 1 >= 0:
                    node.westNeighbor = self.grid[col - 1][row]


    def _wellFormed(self):
        assert self.cols >= 2
        assert self.rows >= 2
from packages.Amazing.Maze import Maze
from __future__ import annotations

class MazeNode():
    """
    Track the state of one node in a Maze.

    MazeNodes have neighors in the cardinal directions.  

    MazeNodes keep track of their own wall state.
    """
    def __init__(
        self,

        # neighbor nodes
        northNeighbor: MazeNode = None,
        eastNeighbor: MazeNode = None,
        southNeighbor: MazeNode = None,
        westNeighbor: MazeNode = None,

        # walls - default to walls True
        northWall: bool = True,
        eastWall: bool = True,
        southWall: bool = True,
        westWall: bool = True
    ) -> None:

        # neighbor nodes
        self.northNeighbor = northNeighbor
        self.eastNeighbor = eastNeighbor
        self.southNeighbor = southNeighbor
        self.westNeighbor = westNeighbor

        # walls
        self.northWall = northWall
        self.eastWall = eastWall
        self.southWall = southWall
        self.westWall = westWall

        # put neighbors in a list
        self.neighbors = [
            self.northNeighbor, 
            self.eastNeighbor, 
            self.southNeighbor, 
            self.westNeighbor
        ]

        # health check
        self._wellFormed()

    def _wellFormed(self):
        """
        Maintain the MazeNode invarient
        - neighbors must share wall states
        
        ex: MazeNode A is MazeNode B's northern neighbor.  If MazeNode A's southern wall is closed, then MazeNode B's northern wall must be closed.
        """
        if self.northNeighbor:
            assert self.northNeighbor.southWall and self.northWall
        if self.eastNeighbor:
            assert self.eastNeighbor.westNeighbor and self.eastWall
        if self.southNeighbor:
            assert self.southNeighbor.northWall and self.southNeighbor
        if self.westNeighbor:
            assert self.westNeighbor.eastWall and self.westWall

    def setNorthWall(self, closed:bool):
        self.northWall = closed
        if self.northNeighbor:
            self.northNeighbor.southWall = closed
        self._wellFormed()

    def setEastWall(self, closed:bool):
        self.eastWall = closed
        if self.eastNeighbor:
            self.eastNeighbor.westWall = closed
        self._wellFormed()

    def setSouthWall(self, closed:bool):
        self.southWall = closed
        if self.southNeighbor:
            self.southNeighbor.northWall = closed
        self._wellFormed()

    def setWestWall(self, closed:bool):
        self.westWall = closed
        if self.southNeighbor:
            self.southNeighbor.northWall = closed
        self._wellFormed()


from Amazing.Nodes.MazeNode import MazeNode

"""Maze
A Maze is an n * m 
"""
class Maze():
    def __init__(self, width:int = 20, height: int = 20) -> None:
        self.width = width
        self.height = height

        self.grid = [[MazeNode()]]

        pass
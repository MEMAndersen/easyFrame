"""
Node class

"""
import numpy as np


class Node:
    def __init__(self, x, y):
        self.coords = np.array([x, y])
        self.dim = np.size(self.coords)
        # self.x = self.coords[0]
        # self.y = self.coords[1]
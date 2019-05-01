"""
Node class

"""
import numpy as np


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dim = 2
        print('creating new node ({},{})'.format(self.x, self.y))

    def get_coord(self):
        return np.array([self.x, self.y])

    def plot(self, ax):
        ax.plot(self.x, self.y, 'bo')

"""
Node class

"""
import numpy as np


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dim = 2
        self.support = None
        self.dofs = np.array([])

        print('creating new node ({},{})'.format(self.x, self.y))

    def get_coord(self):
        return np.array([self.x, self.y])

    def get_supported_dofs(self):
        if self.support is not None:
            return self.dofs[self.support]
        else:
            return np.array([], dtype=int)

    def is_within_tol(self, x, y, tol):
        if abs(self.x - x) < tol and abs(self.y - y) < tol:
            return True
        else:
            return False

    def plot(self, ax):
        if self.support is None or np.all(self.support == False):
            ax.plot(self.x, self.y, 'b.')
        else:
            if np.all(self.support[0] == True):
                ax.plot(self.x, self.y, 'r>')
            if np.all(self.support[1] == True):
                ax.plot(self.x, self.y, 'r^')
            if np.all(self.support[0] == True):
                ax.plot(self.x, self.y, 'r|')

    def add_support(self, directions):
        self.support = directions

    def update_dofs(self, dof_counter):
        n = dof_counter
        self.dofs = np.array([n, n + 1, n + 2], dtype=int)

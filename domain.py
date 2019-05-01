"""
domain class

"""
import numpy as np
import matplotlib.pyplot as plt
from node import *


class Domain:
    def __init__(self, tol=0.05):
        self.geom_objects = np.array([])
        self.nodes = np.array([])
        self.tol = tol

    def add_node(self, x1, y1):
        self.nodes = np.append(self.nodes, Node(x1, y1))

    def add_line(self, x1, y1, x2, y2):
        self.geom_objects = np.append(self.geom_objects, Line(x1, y1, x2, y2, self.nodes, self.tol))

    def change_tol(self, tol):
        self.tol = tol

    def geom_plot(self): # Does not work yet!
        for geom_object in self.geom_objects:
            geom_object.plot()
        plt.axis('equal')
        plt.show()


class Line:
    def __init__(self, x1, y1, x2, y2, nodes, tol):

        if nodes.size != 0:
            for node in nodes:
                if abs(node.x - x1) < tol and abs(node.y - y1) < tol:
                    node1 = node
                else:
                    node1 = Node(x1, y1)
                if abs(node.x - x2) < tol and abs(node.y - y2) < tol:
                    node2 = node
                else:
                    node2 = Node(x2, y2)
        else:
            node1 = Node(x1, y1)
            node2 = Node(x2, y2)

        self.node1 = node1
        self.node2 = node2

    def plot(self):
        xx = np.array([self.node1.x, self.node2.x])
        yy = np.array([self.node1.y, self.node2.y])
        plt.plot(xx, yy)


if __name__ == '__main__':
    domain = Domain()

    domain.add_node(0.5, 0.5)

    domain.add_line(0.5, 0.5, 1.0, 1.0)
    domain.add_line(0.5, 0.5, 2.0, 2.0)
    print(domain.geom_objects)

    domain.geom_plot()

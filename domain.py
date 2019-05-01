"""
domain class

"""
import numpy as np
import matplotlib.pyplot as plt
from node import *


class Domain:
    def __init__(self, tol=0.01):
        self.geom_objects = np.array([])
        self.nodes = np.array([])
        self.tol = tol

    def add_node(self, x, y):
        self.nodes = np.append(self.nodes, Node(x, y))

    def add_line(self, x1, y1, x2, y2):
        line = Line(x1, y1, x2, y2, self.nodes, self.tol)
        self.geom_objects = np.append(self.geom_objects, line)
        if not np.any(line.node1 == self.nodes):
            self.nodes = np.append(self.nodes, line.node1)

        if not np.any(line.node2 == self.nodes):
            self.nodes = np.append(self.nodes, line.node2)

    def change_tol(self, tol):
        self.tol = tol

    def geom_plot(self, line_style='b-'):  # Does not work yet!
        fig = plt.figure()
        ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])
        for geom_object in self.geom_objects:
            geom_object.plot(ax, line_style)
        for node in self.nodes:
            node.plot(ax)
        plt.axis('equal')
        plt.show()


class Line:
    def __init__(self, x1, y1, x2, y2, nodes=np.array([]), tol=0.01):

        if nodes.size != 0:
            for node in nodes:
                if abs(node.x - x1) < tol and abs(node.y - y1) < tol:
                    node1 = node
                    break
            else:
                node1 = Node(x1, y1)

            for node in nodes:
                if abs(node.x - x2) < tol and abs(node.y - y2) < tol:
                    node2 = node
                    break
            else:
                node2 = Node(x2, y2)

        self.node1 = node1
        self.node2 = node2

    def plot(self, ax, line_style):
        xx = np.array([self.node1.x, self.node2.x])
        yy = np.array([self.node1.y, self.node2.y])
        ax.plot(xx, yy, line_style)


if __name__ == '__main__':
    domain = Domain()

    domain.add_node(0.5, 0.5)
    domain.add_node(4, 5)

    domain.add_line(0.5, 0.5, 1.0, 1.0)
    domain.add_line(0.5, 0.5, 1.0, 2.0)
    domain.add_line(1.0, 1.0, 1.0, 2.0)
    domain.add_line(1.0, 1.0, 4, 5)
    domain.add_line(2, 5, 4, 6)
    domain.add_line(1, 1, 4, 6)

    print(domain.geom_objects)

    print(domain.nodes)

    for node in domain.nodes:
        print(node.x, node.y)

    domain.geom_plot()

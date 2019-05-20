"""
domain class

"""
import numpy as np
import matplotlib.pyplot as plt
import math
from node import *


class Domain:
    def __init__(self, tol=0.01):
        self.geom_objects = np.array([])
        self.nodes = np.array([])
        self.tol = tol

    def add_node(self, x, y):
        for node in self.nodes:
            if abs(node.x - x) < self.tol and abs(node.y - y) < self.tol:
                print('Node already present at ({},{})'.format(x, y))
                return node
        else:
            node = Node(x, y)
            self.nodes = np.append(self.nodes, node)
            return node

    def add_support(self, x, y, directions=np.array([True, True, True])):
        """
            method: add_support(self, x, y, directions)

            Adds support conditions to domain shape.

            Parameters
            ----------
            x, y = coordinates
            directions = vector of length 3 with true false values for support [x,y,z]
            Returns
            -------
            transformation matrix
        """
        node = self.add_node(x, y)
        node.add_support(directions)

    def add_line(self, x1, y1, x2, y2):
        line = Line(x1, y1, x2, y2, self.nodes, self.tol)
        self.geom_objects = np.append(self.geom_objects, line)
        if not np.any(line.node1 == self.nodes):
            self.nodes = np.append(self.nodes, line.node1)

        if not np.any(line.node2 == self.nodes):
            self.nodes = np.append(self.nodes, line.node2)

    def change_tol(self, tol):
        self.tol = tol

    def create_mesh(self, h):
        mesh = Mesh(self.tol)
        for geom_object in self.geom_objects:
            print(geom_object)
            mesh.nodes, mesh.lines = geom_object.create_mesh(mesh, h)
        return mesh

    def geom_plot(self, line_style='b-'):
        fig = plt.figure()
        ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])
        for geom_object in self.geom_objects:
            geom_object.plot(ax, line_style)
        for node in self.nodes:
            node.plot(ax)
        plt.axis('equal')
        plt.show()

    def get_node_coords(self):
        nno = np.size(self.nodes)
        coords = np.zeros([nno, 2])

        for i in range(nno):
            coords[i,:] = self.nodes[i].get_coord()
        return coords


class Line:
    def __init__(self, x1, y1, x2, y2, nodes=np.array([]), tol=0.01):

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
        print('creating new line ({}), ({})'.format(node1.get_coord(),node2.get_coord()))

    def get_length(self):
        return np.linalg.norm(self.node2.get_coord() - self.node1.get_coord())

    def plot(self, ax, line_style):
        xx = np.array([self.node1.x, self.node2.x])
        yy = np.array([self.node1.y, self.node2.y])
        ax.plot(xx, yy, line_style)

    def create_mesh(self, mesh, h):
        le = self.get_length()
        n = math.ceil(le / h)

        mesh.add_node(self.node1)
        mesh.add_node(self.node2)

        if n == 1:
            mesh.lines = self
            return
        else:
            x0 = self.node1.x
            y0 = self.node1.y
            x_step = (self.node2.x - self.node1.x) / n
            y_step = (self.node2.y - self.node1.y) / n

        for i in range(n):
            x1 = x0 + x_step
            y1 = y0 + y_step
            mesh.add_line(x0, y0, x1, y1)
            x0 = x1
            y0 = y1


class Mesh:
    def __init__(self, tol=0.01):
        self.nodes = np.array([])
        self.lines = np.array([])
        self.tol = tol

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes = np.append(self.nodes, node)

    def add_line(self, x1, y1, x2, y2):
        line = Line(x1, y1, x2, y2, self.nodes, self.tol)
        self.lines = np.append(self.lines, line)
        if not np.any(line.node1 == self.nodes):
            self.nodes = np.append(self.nodes, line.node1)

        if not np.any(line.node2 == self.nodes):
            self.nodes = np.append(self.nodes, line.node2)


if __name__ == '__main__':
    domain = Domain()

    domain.add_line(0.0, 0.0, 0.0, 1.0)
    domain.add_line(0.0, 1.0, 1.0, 1.0)
    domain.add_line(1.0, 1.0, 1.0, 0.0)

    domain.add_support(0.0, 0.0, np.array([True, True, False]))
    domain.add_support(1.0, 0.0, np.array([True, True, False]))

    mesh_h01 = domain.create_mesh(0.1)

    print(domain.get_node_coords())

    domain.geom_plot()

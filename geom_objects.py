import numpy as np
import matplotlib.pyplot as plt
from copy import copy
from node import *
from beam import *
import math


class Line:
    def __init__(self, x1, y1, x2, y2, nodes=np.array([]), tol=0.01, el_type="beam", cross_section=None):
        self.el_type = el_type
        self.cross_section = cross_section

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
        print('creating new line ({}), ({})'.format(node1.get_coord(), node2.get_coord()))

    def get_length(self):
        return np.linalg.norm(self.node2.get_coord() - self.node1.get_coord())

    def plot(self, ax, line_style):
        xx = np.array([self.node1.x, self.node2.x])
        yy = np.array([self.node1.y, self.node2.y])
        ax.plot(xx, yy, line_style)

    def create_mesh(self, mesh, h):
        le = self.get_length()
        n = math.ceil(le / h)

        mesh.add_node(copy(self.node1))
        mesh.add_node(copy(self.node2))

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
            mesh.add_line(x0, y0, x1, y1, self.cross_section, self.el_type)
            x0 = x1
            y0 = y1

        return mesh

    def get_element(self):
        if self.el_type == 'beam':
            return Beam(self)

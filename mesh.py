"""
Mesh class

"""
import numpy as np
import matplotlib.pyplot as plt
from node import *

from geom_objects import *


class Mesh:
    def __init__(self, tol=0.01):
        self.nodes = np.array([])
        self.lines = np.array([])
        self.elements = np.array([])
        self.nel = 0
        self.ndof = 0
        self.nno = 0
        self.k = np.array([])
        self.tol = tol
        self.global_k = np.array([])

    def get_supported_dofs(self):
        supported_dofs = np.array([])
        for node in self.nodes:
            supported_dofs = np.append(supported_dofs, node.get_supported_dofs())
        return supported_dofs

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes = np.append(self.nodes, node)

    def add_line(self, x1, y1, x2, y2, cross_section, el_type='beam'):
        line = Line(x1, y1, x2, y2, self.nodes, self.tol, el_type, cross_section)
        self.lines = np.append(self.lines, line)
        if not np.any(line.node1 == self.nodes):
            self.nodes = np.append(self.nodes, line.node1)

        if not np.any(line.node2 == self.nodes):
            self.nodes = np.append(self.nodes, line.node2)

    def plot(self, line_style='b-', ax=None):

        if ax is None:
            fig = plt.figure()
            ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])

        for line in self.lines:
            line.plot(ax, line_style)
        for node in self.nodes:
            node.plot(ax)

        plt.axis('equal')

    def generate_dofs(self):
        dof_counter = 0
        for node in self.nodes:
            node.update_dofs(dof_counter)
            dof_counter += 3
        self.ndof = dof_counter

    def generate_elements(self):
        for line in self.lines:
            element = line.get_element()
            self.elements = np.append(self.elements, element)
        self.nel = len(self.elements)

    def generate_global_k(self):
        self.k = np.zeros([self.ndof, self.ndof])
        for element in self.elements:
            element_k = element.global_k_matrix()
            element_dofs = element.get_dofs()
            self.k[np.ix_(element_dofs, element_dofs)] = element_k

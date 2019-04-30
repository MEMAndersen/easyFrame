"""
domain class

"""
import numpy as np

class Domain:
    def __init__(self):
        self.geom_objects = np.array([])

    def line(self, node1, node2):
        self.geom_objects.__add__(Line(node1, node2)

class Line:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
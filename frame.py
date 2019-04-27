"""
Frame class

Class variables:
nodes: Geometry nodes as a (x*2 or x*3 numpy array)
connectivity:
"""
import numpy as np
from mesh import Mesh


class Frame:
    def __init__(self):
        # Geometry definitions
        self.nodes = np.array()
        self.connectivity = np.array()
        self.elTypes = ()
        self.elements = ()

    def create_mesh(self):
        mesh = Mesh(self.nodes, self.connectivity, self.el_types)

    def stiffness_matrix(self):
        # number of elements
        nel = np.size(self.mesh.T)

    def beam(self, L, E, I):
        return Beam(, x2, E, I)

class Beam:
    def __init__(self):
        # Geometry definitions
        self.nodes = np.array()
        self.connectivity = np.array()
        self.elTypes = ()
        self.elements = ()



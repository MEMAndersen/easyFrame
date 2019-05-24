"""
Frame class

Class variables:
nodes: Geometry nodes as a (x*2 or x*3 numpy array)
connectivity:
"""
import numpy as np
from easyFrame.mesh import Mesh


class Frame:
    def __init__(self):
        # Geometry definitions
        self.nodes = np.array()
        self.connectivity = np.array()
        self.elTypes = ()
        self.elements = ()

    def create_mesh(self):
        mesh = Mesh(self.nodes, self.connectivity, self.el_types)





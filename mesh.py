"""
Mesh class

"""
import numpy as np


class Mesh:

    def __init__(self):
        # Geometry definitions
        self.X = np.array()
        self.T = np.array()
        self.elTypes = ()
        self.n = 10; # default dizcretization

        #updateMesh(self)

    #def updateMesh(self):

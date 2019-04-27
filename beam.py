"""
beam class

"""
import numpy as np
from line_int import *
import matplotlib.pyplot as plt


class Beam:
    def __init__(self, node1, node2, e_module, area, moment_inertia):
        self.node1 = node1
        self.node2 = node2
        self.e_module = e_module
        self.area = area
        self.moment_inertia = moment_inertia

        self.length = self.get_length()

        # Determine if 2D or 3D beam
        if node1.dim == 2:
            self.dof = 6
        elif node1.dim == 3:
            self.dof = 9

    def get_length(self):
        return np.linalg.norm(self.node2.coords - self.node1.coords)

    def d_matrix(self):
        return np.array([[self.e_module * self.area, 0], [0, self.e_module * self.moment_inertia]])

    def b_matrix(self, xl):
        L = self.length

        b1 = -1 / L
        b2 = 1 / L ** 2 * (- 6 + 12 * xl / L)
        b3 = 1 / L ** 2 * (- 4 + 6 * xl / L)
        b4 = 1 / L
        b5 = 1 / L ** 2 * (6 - 12 * xl / L)
        b6 = 1 / L ** 2 * (-2 + 6 * xl / L)

        return np.array([[b1, 0, 0, b4, 0, 0], [0, b2, b3, 0, b5, b6]])

    def k_matrix(self):
        xp, wp, n = line_int(3, 0, self.length)
        k = np.zeros([self.dof, self.dof])
        d = self.d_matrix()

        for i in range(n):
            b = self.b_matrix(xp[i])
            b_t = np.transpose(b)
            k += wp[i] * b_t.dot(d).dot(b)

        return k


"""
    def calc_strains(self, v, coords):
        coords = np.zeros([100, 2])
        xl = np.linspace(0, 1, coords)
        for i in range(coords):
            b = self.b_matrix(xl[i])
            coords[i, :] = np.dot(b, v)

    def calc_stresses(self):
"""

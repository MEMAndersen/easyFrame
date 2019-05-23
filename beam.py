"""
beam class

"""
import numpy as np
from line_int import *
import matplotlib.pyplot as plt
import unittest


class Beam:
    def __init__(self, line):
        self.el_type = 'beam'
        self.node1 = line.node1
        self.node2 = line.node2
        self.cross_section = line.cross_section
        self.length = self.get_length()
        self.line = line

        # Determine if 2D or 3D beam
        if self.node1.dim == 2:
            self.dim = 2
            self.dof = 6
        elif self.node1.dim == 3:
            self.dim = 3
            self.dof = 9

    def get_length(self):
        return np.linalg.norm(self.node2.get_coord() - self.node1.get_coord())

    def get_dofs(self):
        return np.concatenate([self.node1.dofs, self.node2.dofs])

    def d_matrix(self):
        ea = self.cross_section.get_ea()
        ei = self.cross_section.get_ei()
        return np.array([[ea, 0], [0, ei]])

    def n_matrix(self, xl):
        le = self.length
        xl_le = xl / le

        n1 = 1 - xl_le
        n2 = 1 - 3 * xl_le ** 2 + 2 * xl_le ** 3
        n3 = le * (xl_le - 2 * xl_le ** 2 + xl_le ** 3)
        n4 = xl_le
        n5 = 3 * xl_le ** 2 - 2 * xl_le ** 3
        n6 = le * (-xl_le ** 2 + xl_le ** 3)

        return np.array([[n1, 0, 0, n4, 0, 0], [0, n2, n3, 0, n5, n6]])

    def b_matrix(self, xl):
        le = self.length

        b1 = -1 / le
        b2 = 1 / le ** 2 * (- 6 + 12 * xl / le)
        b3 = 1 / le ** 2 * (- 4 + 6 * xl / le)
        b4 = 1 / le
        b5 = 1 / le ** 2 * (6 - 12 * xl / le)
        b6 = 1 / le ** 2 * (-2 + 6 * xl / le)

        return np.array([[b1, 0, 0, b4, 0, 0], [0, b2, b3, 0, b5, b6]])

    def local_k_matrix(self):
        xp, wp, n = line_int(3, 0, self.length)
        k = np.zeros([self.dof, self.dof])
        d = self.d_matrix()

        for i in range(n):
            b = self.b_matrix(xp[i])
            b_t = np.transpose(b)
            k += wp[i] * b_t.dot(d).dot(b)

        return k

    def global_k_matrix(self):
        k = self.local_k_matrix()
        t = self.t_matrix(typ='full')
        t_t = np.transpose(t)

        return t_t.dot(k).dot(t)

    def t_matrix(self, typ='full'):
        """
            method: t_matrix(self, full=True)

            Transformation matrix.

            Parameters
            ----------
            typ='full':
                Determines what kind of transformation matrix are provided.
                'full' : Full transformation matrix for element
                'single' : transformation for only one node

            Returns
            -------
            transformation matrix
        """
        n = 1 / self.length * (self.node2.get_coord() - self.node1.get_coord())
        nx = n[0]
        ny = n[1]

        if typ == 'full':
            return np.array([[nx, ny, 0, 0, 0, 0],
                             [-ny, nx, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0, 0],
                             [0, 0, 0, nx, ny, 0],
                             [0, 0, 0, -ny, nx, 0],
                             [0, 0, 0, 0, 0, 1]])
        elif typ == 'single':
            return np.array([[nx, ny, 0],
                             [-ny, nx, 0],
                             [0, 0, 1]])
        elif typ == 'node':
            return np.array([[nx, ny],
                             [-ny, nx]])

    def plot(self, ax, v, div=1, local=False):

        if ax is None:
            fig = plt.figure()
            ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])

        # interpolate between nodes
        x = np.linspace(self.node1.x, self.node2.x, div+1)
        y = np.linspace(self.node1.y, self.node2.y, div+1)
        xyz = np.transpose(np.array([x, y]))
        xyz_v = np.zeros([div+1, self.dim])

        # local length variable
        xl = np.linspace(0, self.length, div+1)

        # convert to local deformations
        t_full = self.t_matrix()
        if not local:
            v = v.dot(t_full)

        # compute points in local coordinates and transform back to global
        t_node = self.t_matrix('node')
        for i in range(div+1):
            xyz_v[i, :] = self.n_matrix(xl[i]).dot(v).dot(t_node)

        ax.plot(xyz[:, 0] + xyz_v[:, 0], xyz[:, 1] + xyz_v[:, 1], 'b-')
        ax.axis('equal')

if __name__ == '__main__':
    pass

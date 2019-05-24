"""
test script for Beam class
"""

import unittest
from easyFrame.cross_section import *
from easyFrame.material import *
from easyFrame.geom_objects import *
import math
import random


class TestBeamRandom(unittest.TestCase):

    def setUp(self):
        mat = Material()
        mat.set_random()
        cs = CrossSection(1, 1, mat)
        cs.set_random()
        self.tol = 1e-8
        self.x1 = random.uniform(0, 10)
        self.y1 = random.uniform(0, 10)
        self.x2 = random.uniform(0, 10)
        self.y2 = random.uniform(0, 10)
        line = Line(self.x1, self.y1, self.x2, self.y2, cross_section=cs)

        self.beam = Beam(line)

    def test_beam_get_length(self):
        length1 = self.beam.get_length()
        length2 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.assertAlmostEqual(length1, length2, delta=1e-9)

    def test_b_matrix_translation(self):
        xl = random.random()
        dx = random.random()
        dy = random.random()

        # Get translation vector
        v = np.array([dx, dy, 0, dx, dy, 0])

        # Get B-matrix
        b = self.beam.b_matrix(xl)

        # computed
        dv = b.dot(v)
        # expected
        dv_e = [0, 0]
        # test results
        res = np.abs(dv - dv_e)

        self.assertTrue(np.all(res < self.tol))

    def test_b_matrix_rotation(self):
        xl = random.random()
        d_alpha = random.random() * math.pi / 2

        # Get translation vector
        le = self.beam.get_length()

        dy = d_alpha * le / 2
        dx = math.sin(d_alpha) * le / 2
        v = np.array([0, dy / 2, -d_alpha, 0, -dy / 2, -d_alpha])

        # Get B-matrix
        b = self.beam.b_matrix(xl)

        # computed
        dv = b.dot(v)
        # expected
        dv_e = [0, 0]
        # test results
        res = np.abs(dv - dv_e)

        print(dv)

        self.beam.plot(None, v, div=100, local=True)
        self.beam.line.plot(None, line_style='r--')
        plt.show()

        self.assertTrue(np.all(res < self.tol))

    def test_b_matrix_pure_axial_strain(self):
        xl = random.random()
        dx = random.random()

        # Get translation vector
        le = self.beam.get_length()
        v = np.array([-dx / 2, 0, 0, dx / 2, 0, 0])

        # Get B-matrix
        b = self.beam.b_matrix(xl)

        # computed
        dv = b.dot(v)
        # expected
        dv_e = [dx / le, 0]
        # test results
        res = np.abs(dv - dv_e)

        print(dv)
        print([dx / le, 0])

        self.assertTrue(np.all(res < self.tol))

    def test_b_matrix_pure_curvature(self):
        xl = random.random()
        d_alpha = random.random() * math.pi / 2

        # Get translation vector
        le = self.beam.get_length()
        v = np.array([0, 0, -d_alpha, 0, 0, d_alpha])

        # Get B-matrix
        b = self.beam.b_matrix(xl)

        # computed
        dv = b.dot(v)
        # expected
        dv_e = [0, 2 / le * d_alpha]
        # test results
        res = np.abs(dv - dv_e)

        print(res)

        self.assertTrue(np.all(res < self.tol))


if __name__ == '__main__':
    unittest.main()

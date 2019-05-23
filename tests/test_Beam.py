"""
test script for Beam class
"""

import unittest
from cross_section import *
from material import *
from geom_objects import *
import math
import random


class TestBeam(unittest.TestCase):

    def setUp(self):
        mat = Material()
        mat.set_random()
        cs = CrossSection(1, 1, mat)
        cs.set_random()
        self.x1 = random.uniform(1, 10)
        self.y1 = random.uniform(1, 10)
        self.x2 = random.uniform(1, 10)
        self.y2 = random.uniform(1, 10)
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

        dv = b.dot(v)

        self.assertTrue(np.any(dv == [0, 0]))

    def test_b_matrix_rotation(self):
        xl = random.random()
        d_alpha = random.random() * math.pi / 2

        # Get translation vector
        le = self.beam.get_length()
        dy = math.cos(d_alpha) * le / 2
        v = np.array([0, dy / 2, d_alpha, 0, -dy / 2, d_alpha])

        # Get B-matrix
        b = self.beam.b_matrix(xl)

        dv = b.dot(v)

        self.assertTrue(np.any(dv == [0, 0]))


if __name__ == '__main__':
    unittest.main()

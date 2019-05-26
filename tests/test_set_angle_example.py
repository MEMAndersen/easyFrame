"""
Example "vinkelramme" from book "bærende konstruktioner 4" s. 40
"""

import unittest
import numpy as np
import numpy.testing as npt

# Import the easeFrame package
from easyFrame import material
from easyFrame import cross_section
from easyFrame import domain
from easyFrame import load
from easyFrame import analysis


class TestSetAngleExample(unittest.TestCase):
    def setUp(self):
        # Material and constants
        a = 2  # m
        area = 3e-3  # m^2
        moment_inertia = 2e-5  # m^4
        e_modulus = 2e11  # N/m^2
        P = 1000  # N

        # Create material and cross section
        mat = material.Material(e_modulus=e_modulus)
        cs = cross_section.CrossSection(area=area, moment_inertia=moment_inertia, material=mat)

        # Initialise domain and create lines and supports
        self.frame = domain.Domain()

        self.frame.add_line(0, 2 * a, a, 2 * a, cs, el_type='beam')
        self.frame.add_line(a, 2 * a, 2 * a, 2 * a, cs, el_type='beam')
        self.frame.add_line(2 * a, 2 * a, 2 * a, 0, cs, el_type='beam')

        self.frame.add_support(0, 2 * a, directions=[True, True, False])
        self.frame.add_support(2 * a, 0, directions=[True, True, False])

        # mesh the structure
        self.mesh_1 = self.frame.create_mesh(2 * a)
        self.mesh_1.generate_dofs()
        self.mesh_1.generate_elements()
        self.mesh_1.plot()

        # create the load case
        self.load_case_1 = load.LoadCase(self.mesh_1)
        self.load_case_1.add_point_load(a, 2 * a, [0, -P, 0])
        self.load_case_1.generate_load_vector()

        self.LE = analysis.LinearElastic(self.mesh_1, self.load_case_1)

        self.LE.run_analysis()

    def test_deformation_results(self):
        # Values differs from book example by a factor 10, the mistake is with the book
        res = 1e-4 * np.array([0, 0, -1.8877, -0.0031, -2.4199, 0.1456, -0.0062, -0.0396, 1.2458, 0, 0, - 0.6206])
        npt.assert_almost_equal(self.LE.v, res, decimal=8)

    def test_reaction_results(self):
        # Values differs from book example by a factor 10, the mistake is with the book
        res = 1e3 * np.array([0.09332, 0.40668, -0.09362, 0.59362])
        npt.assert_allclose(self.LE.r, res,rtol=1e-2)

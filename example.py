"""
Example file for calling the easyFrame routines
"""

import numpy as np

from line_int import *

from node import Node
from beam import Beam

e_module = 210e6
area = 0.343
moment_inertia = 0.104 * 1e-6

n1 = Node(0, 0)
n2 = Node(5, 0)
n3 = Node(10, 0)

beam1 = Beam(n1, n2, e_module, area, moment_inertia)
beam2 = Beam(n2, n3, e_module, area, moment_inertia)

print(beam1.k_matrix())

beam1.plot(np.array([0, 0, 0, 0, 0, 3.14]), div=100)

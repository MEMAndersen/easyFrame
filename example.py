"""
Example file for calling the easyFrame routines
"""

import numpy as np

from line_int import *


from node import Node
from beam import Beam

n1 = Node(0, 0)
n2 = Node(1, 1)

beam1 = Beam(n1, n2, 1, 1, 1)

v = np.transpose(np.array([0, 1, 0, 0, 0, 0]))

print(beam1.k_matrix())




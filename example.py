"""
Example file for calling the easyFrame routines
"""

import numpy as np

from line_int import *


from node import Node
from beam import Beam

n1 = Node(0, 0)
n2 = Node(5, 0)

beam1 = Beam(n1, n2, 1, 1, 1)

v = np.transpose(np.array([0, 1, 1, 0, 0, 0]))

k = beam1.k_matrix()

f = k.dot(v)

print(k,v, f)

n = beam1.n_matrix(beam1.length)

print(n)

beam1.plot(v, local=True, div=100)

t = beam1.t_matrix()
print(t)

print(v.dot(t))


"""
Example file for calling the easyFrame routines
"""

import numpy as np
from line_int import *
from node import Node
from geom_objects import *
from beam import *
from cross_section import *
from material import *
from domain import *

area = 0.343
moment_inertia = 0.104 * 1e-6

cs = CrossSection(area, moment_inertia, Steel())

domain = Domain()

domain.add_line(0.0, 0.0, 0.0, 1.0, el_type='beam', cross_section=cs)
domain.add_line(0.0, 1.0, 1.0, 1.0, el_type='beam', cross_section=cs)
domain.add_line(1.0, 1.0, 1.0, 0.0, el_type='beam', cross_section=cs)

domain.add_support(0.0, 0.0, np.array([True, True, False]))
domain.add_support(1.0, 0.0, np.array([True, True, False]))
domain.plot()

mesh_h0_1 = domain.create_mesh(0.1)
mesh_h0_1.generate_dofs()
mesh_h0_1.plot()
mesh_h0_1.generate_elements()
mesh_h0_1.generate_global_k()

print(mesh_h0_1.elements)
print(mesh_h0_1.k)
plt.show()

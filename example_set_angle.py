"""
Example "vinkelramme" from book "bærende konstruktioner 4" s. 40
"""

# Import the easeFrame package
from easyFrame import material
from easyFrame import cross_section
from easyFrame import domain
from easyFrame import load
from easyFrame import analysis

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
frame = domain.Domain()

frame.add_line(0, 2 * a, a, 2 * a, cs, el_type='beam')
frame.add_line(a, 2 * a, 2 * a, 2 * a, cs, el_type='beam')
frame.add_line(2 * a, 2 * a, 2 * a, 0, cs, el_type='beam')

frame.add_support(0, 2 * a, directions=[True, True, False])
frame.add_support(2 * a, 0, directions=[True, True, False])

frame.plot()

# mesh the structure
mesh_1 = frame.create_mesh(2*a)
mesh_1.generate_dofs()
mesh_1.generate_elements()
mesh_1.plot()

# create the load case
load_case_1 = load.LoadCase(mesh_1)
load_case_1.add_point_load(a, 2*a, [0, -P, 0])
load_case_1.generate_load_vector()


LE = analysis.LinearElastic(mesh_1, load_case_1)

LE.run_analysis()
LE.plot_deformed(div=100, scale=2000, show=True)
print(LE.v)
print(LE.r)

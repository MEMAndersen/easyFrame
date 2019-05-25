"""
Analysis class

"""
from easyFrame.mesh import *


class LinearElastic:
    def __init__(self, mesh, load_case):
        self.mesh = mesh
        self.load_case = load_case
        self.v = np.array([])
        self.f = np.array([])
        self.r = np.array([])

    def run_analysis(self):

        # generate stiffness and loads
        self.mesh.generate_global_k()
        self.load_case.generate_load_vector()

        # dof control
        dof_a = np.arange(self.mesh.ndof)  # all dofs
        dof_u = self.mesh.get_supported_dofs()  # Supported dofs
        dof_f = np.setdiff1d(dof_a, dof_u)  # Free dofs

        # seperate k into parts
        k_ff = self.mesh.k[np.ix_(dof_f, dof_f)]
        #k_fu = self.mesh.k[np.ix_(dof_f, dof_u)]
        k_uf = self.mesh.k[np.ix_(dof_u, dof_f)]
        #k_uu = self.mesh.k[np.ix_(dof_u, dof_u)]

        # seperate loads into parts
        r_f = self.load_case.load_vector[dof_f]

        # solve system
        v_f = np.linalg.solve(k_ff, r_f)

        # solve the free deformations
        self.v = np.zeros(self.mesh.ndof)
        self.v[dof_f] = v_f

        # solve for reactions
        self.r = k_uf.dot(v_f)  #+ k_uu.dot(v)

    def plot_deformed(self, div=1, scale=100, show=False):
        fig = plt.figure()
        ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])

        self.mesh.plot(ax=ax)

        for element in self.mesh.elements:
            v_element = self.v[element.get_dofs()] * scale
            element.plot(ax, v_element, div=div)
        plt.axis('equal')

        if show:
            plt.show()

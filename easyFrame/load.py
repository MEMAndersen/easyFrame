"""
Mesh class

"""

from easyFrame.geom_objects import *


class LoadCase:
    def __init__(self, mesh):
        self.mesh = mesh
        self.load_vector = np.zeros(mesh.ndof)
        self.loads = []

    def add_load(self, load):
        self.loads.append(load)

    def add_point_load(self, x, y, force, local=False):
        load = PointLoad(x, y, force, local)
        self.loads.append(load)

    def generate_load_vector(self):
        self.load_vector = np.zeros(self.mesh.ndof)
        for load in self.loads:
            self.load_vector = load.apply_load(self.load_vector, self.mesh)

    # def total_load(self, direction):
    #     if direction == 'x' or direction == 1:
    #         tl = np.sum(self.load_vector[::3])
    #     elif direction == 'y' or direction == 2:
    #         tl = np.sum(self.load_vector[1::3])
    #     return tl



class PointLoad:
    def __init__(self, x, y, force, local=False):
        self.x = x
        self.y = y
        self.force = force
        self.local = local

        if local:
            print("WARNING, local not defined for Point Load.")

    def apply_load(self, load_vector, mesh):
        nodes = mesh.nodes
        tol = mesh.tol
        for node in nodes:
            if node.is_within_tol(self.x, self.y, tol):
                load_vector[node.dofs] += self.force
        return load_vector


class LineLoad:
    def __init__(self, x1, y1, x2, y2, force, local=False):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.force = force
        self.local = local

if __name__ == '__main__':
    pass
"""
domain class

"""
from easyFrame.mesh import *
from easyFrame.geom_objects import *


class Domain:
    def __init__(self, tol=0.01):
        self.geom_objects = np.array([])
        self.nodes = np.array([])
        self.tol = tol

    def add_node(self, x, y):
        for node in self.nodes:
            if abs(node.x - x) < self.tol and abs(node.y - y) < self.tol:
                print('Node already present at ({},{})'.format(x, y))
                return node
        else:
            node = Node(x, y)
            self.nodes = np.append(self.nodes, node)
            return node

    def add_support(self, x, y, directions=np.array([True, True, True])):
        """
            method: add_support(self, x, y, directions)

            Adds support conditions to domain shape.

            Parameters
            ----------
            x, y = coordinates
            directions = vector of length 3 with true false values for support [x,y,z]
            Returns
            -------
            transformation matrix
        """
        node = self.add_node(x, y)
        node.add_support(directions)

    def add_line(self, x1, y1, x2, y2, cross_section, el_type='beam'):
        line = Line(x1, y1, x2, y2, self.nodes, self.tol, el_type, cross_section)
        self.geom_objects = np.append(self.geom_objects, line)
        if not np.any(line.node1 == self.nodes):
            self.nodes = np.append(self.nodes, line.node1)

        if not np.any(line.node2 == self.nodes):
            self.nodes = np.append(self.nodes, line.node2)

    def change_tol(self, tol):
        self.tol = tol

    def create_mesh(self, h):
        mesh = Mesh(self.tol)
        for geom_object in self.geom_objects:
            print(geom_object)
            mesh = geom_object.create_mesh(mesh, h)
        return mesh

    def plot(self, line_style='b-', show=False):
        fig = plt.figure()
        ax = fig.add_axes([0.10, 0.10, 0.8, 0.8])
        for geom_object in self.geom_objects:
            geom_object.plot(ax, line_style)
        for node in self.nodes:
            node.plot(ax)
        plt.axis('equal')

        if show:
            plt.show()

    def get_node_coords(self):
        nno = np.size(self.nodes)
        coords = np.zeros([nno, 2])

        for i in range(nno):
            coords[i, :] = self.nodes[i].get_coord()
        return coords


if __name__ == '__main__':
    pass

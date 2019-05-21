"""
material class

"""


class Material:
    def __init__(self):
        self.e_modulus = None
        self.g_modulus = None


class Steel(Material):
    def __init__(self):
        Material.__init__(self)
        self.e_modulus = 210e9  # MPa

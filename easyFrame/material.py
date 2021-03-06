"""
material class

"""
import random


class Material:
    def __init__(self, e_modulus=None, g_modulus=None):
        self.e_modulus = e_modulus
        self.g_modulus = g_modulus

    def set_random(self, lower=1, upper=10):
        self.e_modulus = random.uniform(lower, upper)
        self.g_modulus = random.uniform(lower, upper)


class Steel(Material):
    def __init__(self):
        Material.__init__(self)
        self.e_modulus = 210e9  # MPa

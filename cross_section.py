"""
cross section class

"""
import random


class CrossSection:
    def __init__(self, area, moment_inertia, material):
        self.area = area
        self.moment_inertia = moment_inertia
        self.material = material

    def set_random(self, lower=1, upper=10):
        self.area = random.uniform(lower, upper)
        self.moment_inertia = random.uniform(lower, upper)

    def get_ea(self):
        return self.material.e_modulus * self.area

    def get_ei(self):
        return self.material.e_modulus * self.moment_inertia

import math

class Circle:
    """Circle v6 (special methods)"""
    def __init__(self, radius = 0.0):
        self.__set_radius(radius)

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def __set_radius(self, radius):
        if radius >= 0.0:
            self.__radius = radius
        else:
            print('radius cannot be less than 0.0')
            self.__radius = 0.0

    def __get_radius(self):
        return self.__radius

    def __str__(self):
        return 'Circle with radius %.2f' % self.__get_radius()

    def __gt__(self, other):
        return self.radius > other.radius

    radius = property(__get_radius, __set_radius)

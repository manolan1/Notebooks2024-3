import math
from Shape_3 import Shape

class Circle(Shape):
    """Circle v9 (kwds init)"""
    def __init__(self, radius = 0.0, **kwds):
        super().__init__(**kwds)
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

    radius = property(__get_radius, __set_radius)

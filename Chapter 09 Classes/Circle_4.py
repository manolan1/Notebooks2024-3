import math

class Circle:
    """Circle v4 (getter & setter)"""
    def __init__(self, radius = 0.0):
        self.set_radius(radius)

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def set_radius(self, radius):
        if radius >= 0.0:
            self.__radius = radius
        else:
            print('radius cannot be less than 0.0')
            self.__radius = 0.0

    def get_radius(self):
        return self.__radius

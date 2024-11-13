import math

class Circle:
    """Circle v3 (attribute & method)"""
    def __init__(self, radius = 0.0):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
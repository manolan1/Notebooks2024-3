class Shape:
    """Shape v1 (The superclass)"""
    def calculate_area(self):
        return 0

    def __str__(self):
        return 'We should not get here, this is a Shape with area %.2f' % self.calculate_area()

    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()

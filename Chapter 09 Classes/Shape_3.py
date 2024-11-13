class Shape:
    """Shape v3 (class attribute fixed)"""

    __count = 0

    def __init__(self, name = ''):
        Shape.__count += 1
        self.__set_name(name)

    def __del__(self):
        Shape.__count -= 1

    def calculate_area(self):
        return 0

    def __str__(self):
        return 'We should not get here, this is a Shape with area %.2f' % self.calculate_area()

    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()

    def __set_name(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    name = property(__get_name, __set_name)

    def __get_count(self):
        return Shape.__count

    count = property(__get_count)

# or
# from Shape_3 import Shape
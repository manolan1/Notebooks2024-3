from Shape_1 import Shape

class Square(Shape):
    """Square v1 (subclass)"""
    def __init__(self, length = 0.0):
        super().__init__()
        self.__set_length(length)

    def calculate_area(self):
        return self.__length * self.__length

    def __set_length(self, length):
        if length >= 0.0:
            self.__length = length
        else:
            print('length cannot be less than 0.0')
            self.__length = 0.0

    def __get_length(self):
        return self.__length

    def __str__(self):
        return 'Square with side length %.2f' % self.__get_length()

    length = property(__get_length, __set_length)

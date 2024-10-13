import math

from shape import Shape


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def calc_circumference(self):
        return self.__radius * math.pi * 2

    def calc_area(self):
        # can be done return math.pi * (self.__radius ** 2)
        return float(self.__radius) * float(self.__radius) * math.pi

    def display_shape_parameters(self):
        print(f"Circle: color {self.get_color}, radius: {self.radius}")

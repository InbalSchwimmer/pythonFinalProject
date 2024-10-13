import math
from math import sqrt

from shape import Shape


class RightTriangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def calc_area(self):
        return (float(self.__height) * float(self.__width))/2

    def calc_circumference(self):
        hypotenuse = math.sqrt(self.__width ** 2 + self.__height ** 2)  # Calculate hypotenuse
        return float(self.__width) + float(self.__height) + hypotenuse

    def display_shape_parameters(self):
        print(f"Right triangle: color {self.get_color}, width: {self.width}, height: {self.height}")
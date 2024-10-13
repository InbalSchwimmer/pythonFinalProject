from shape import Shape


class Square(Shape):

    def __init__(self, color, width):
        super().__init__(color)
        self.__width = width

    @property
    def width(self):
        return self.__width

    def calc_area(self):
        return float(self.__width) * 2

    def calc_circumference(self):
        return float(self.__width) * 4

    def display_shape_parameters(self):
        print(f"Square: color {self.get_color}, width: {self.width}")












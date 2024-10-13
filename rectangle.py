from square import Square


class Rectangle(Square):
    def __init__(self, color, width, height):
        super().__init__(color, width)
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def calc_circumference(self):
        return (self.__width * 2) + (self.__height * 2)

    def calc_area(self):
        return self.__width * self.__height

    def display_shape_parameters(self):
        print(f"Rectangle: color {self.get_color}, width: {self.width}, height: {self.height}")

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.__color = color

    @property
    def get_color(self):
        return self.__color

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_circumference(self):
        pass

    @abstractmethod
    def display_shape_parameters(self):
        pass

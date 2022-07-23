import abc
from abc import ABC, abstractproperty


class Figure(ABC):

    @property
    def name(self):
        return type(self).__name__

    @property
    @abc.abstractmethod
    def perimeter(self):
        pass

    @property
    @abc.abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        return self.area + figure.area

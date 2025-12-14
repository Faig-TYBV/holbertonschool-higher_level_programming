#!/usr/bin/python3
""" a class """


class BaseGeometry:
    """ geoclass """
    def area(self):
        """ it is not implemented yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate integers here """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class BaseGeometry:
    """
    A class with Public instance method: def area(self)
    """
    def area(self):
        """
        A public instance method that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

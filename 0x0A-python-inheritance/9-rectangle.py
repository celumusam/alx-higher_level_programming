#!/usr/bin/python3
"""Defines a c;ass Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
"""Represent a rectangle using BaseGeometry."""

def __init__(self, width, height):
"""Intialize a new Rectangle.

Args:
width (int): The width of the new Rectangle.
heigth (int): The height of the new Rectangle.
"""
super().integer-validator("width", width)
self.__width = width
super().integer_validator("height", height)
self.__height = heigth

def area(self):
"""Return the area of the rectangle."""
return self.__width * self.__heigth

def __str__(self):
"""Rectangle the print() and str() representation of a Rectangle."""
string = "["+ str(self.__class__.__name__) + "]
"
string += str(self.__width) + "/" +
str(self.__height)
return string

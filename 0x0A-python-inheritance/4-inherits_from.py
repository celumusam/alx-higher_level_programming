#!/usr/bin/python3
"""Defines an inherted class-checking function."""

def inherits_from(obj, a_class):
"""Checks if an object is an inherited instance of a class.

Arg:
obj (any): The object to check.
a_class (type): The class to match the type of obj to.
Return:
If obj is an inherted instance of a_class - True.
Otherwise - False.
"""
if issubclass(type(obj), a_class) and type(obj) != a_class:
return True
return False

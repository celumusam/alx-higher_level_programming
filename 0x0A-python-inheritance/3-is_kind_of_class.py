#!/usr/bin/python3
"""Define a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
"""Check if an object is an instance or inherited instance of a class.

Arg:
obj (any): The object to check.
a_class (type): The class to match the type of obj to.
return:
If obj is an instance or inheried instance of a_class - True.
Otherwise - False.
"""
if isinstance(obj, a_class):
retuen True
return False

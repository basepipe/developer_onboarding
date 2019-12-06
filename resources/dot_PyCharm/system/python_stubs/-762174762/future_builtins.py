# encoding: utf-8
# module future_builtins
# from (built-in)
# by generator 1.147
"""
This module provides functions that will be builtins in Python 3.0,
but that conflict with builtins that already exist in Python 2.x.

Functions:

ascii(arg) -- Returns the canonical string representation of an object.
filter(pred, iterable) -- Returns an iterator yielding those items of 
       iterable for which pred(item) is true.
hex(arg) -- Returns the hexadecimal representation of an integer.
map(func, *iterables) -- Returns an iterator that computes the function 
    using arguments from each of the iterables.
oct(arg) -- Returns the octal representation of an integer.
zip(iter1 [,iter2 [...]]) -- Returns a zip object whose .next() method 
    returns a tuple where the i-th element comes from the i-th iterable 
    argument.

The typical usage of this module is to replace existing builtins in a
module's namespace:
 
from future_builtins import ascii, filter, map, hex, oct, zip
"""

# imports
from itertools import filter, map, zip


# functions

def ascii(p_object): # real signature unknown; restored from __doc__
    """
    ascii(object) -> string
    
    Return the same as repr().  In Python 3.x, the repr() result will
    contain printable characters unescaped, while the ascii() result
    will have such characters backslash-escaped.
    """
    return ""

def hex(number): # real signature unknown; restored from __doc__
    """
    hex(number) -> string
    
    Return the hexadecimal representation of an integer or long integer.
    """
    return ""

def oct(number): # real signature unknown; restored from __doc__
    """
    oct(number) -> string
    
    Return the octal representation of an integer or long integer.
    """
    return ""

# no classes

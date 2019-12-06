# encoding: utf-8
# module _bisect
# from (built-in)
# by generator 1.147
"""
Bisection algorithms.

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over the more
common approach.
"""
# no imports

# functions

def bisect(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    bisect(a, x[, lo[, hi]]) -> index
    bisect_right(a, x[, lo[, hi]]) -> index
    
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, i points just
    beyond the rightmost x already there
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def bisect_left(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    bisect_left(a, x[, lo[, hi]]) -> index
    
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, i points just
    before the leftmost x already there.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def bisect_right(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    bisect(a, x[, lo[, hi]]) -> index
    bisect_right(a, x[, lo[, hi]]) -> index
    
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, i points just
    beyond the rightmost x already there
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    insort(a, x[, lo[, hi]])
    insort_right(a, x[, lo[, hi]])
    
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the right of the rightmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_left(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    insort_left(a, x[, lo[, hi]])
    
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the left of the leftmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_right(a, x, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    insort(a, x[, lo[, hi]])
    insort_right(a, x[, lo[, hi]])
    
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the right of the rightmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

# no classes

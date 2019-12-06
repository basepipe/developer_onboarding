# encoding: utf-8
# module pandas._libs.interval
# from C:\Python27\lib\site-packages\pandas\_libs\interval.pyd
# by generator 1.147
# no doc

# imports
import numbers as numbers # C:\Python27\lib\numbers.pyc
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
from operator import le, lt

from pandas._libs.tslibs.timestamps import Timestamp


# functions

def intervals_to_interval_bounds(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        intervals : ndarray
            object array of Intervals / nulls
    
        validate_closed: boolean, default True
            boolean indicating if all intervals must be closed on the same side.
            Mismatching closed will raise if True, else return None for closed.
    
        Returns
        -------
        tuples (left: ndarray object array,
                right: ndarray object array,
                closed: str)
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalMixin(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalTree(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

# classes

class Float32ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBB40>'


class Float32ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBAE0>'


class Float32ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBB70>'


class Float32ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBB10>'


class Float64ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBC00>'


class Float64ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBBA0>'


class Float64ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBC30>'


class Float64ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBBD0>'


class Int32ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBCC0>'


class Int32ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBC60>'


class Int32ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBCF0>'


class Int32ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBC90>'


class Int64ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBD80>'


class Int64ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBD20>'


class Int64ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBDB0>'


class Int64ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBD50>'


class IntervalMixin(object):
    # no doc
    def _check_closed_matches(self, *args, **kwargs): # real signature unknown
        """
        Check if the closed attribute of `other` matches.
        
                Note that 'left' and 'right' are considered different from 'both'.
        
                Parameters
                ----------
                other : Interval, IntervalIndex, IntervalArray
                name : str
                    Name to use for 'other' in the error message.
        
                Raises
                ------
                ValueError
                    When `other` is not closed exactly the same as self.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is closed on the left side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            ``True`` if the Interval is closed on the left-side, else
            ``False``.
        """

    closed_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is closed on the right side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            ``True`` if the Interval is closed on the left-side, else
            ``False``.
        """

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the length of the Interval"""

    mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the midpoint of the Interval
        """

    open_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is open on the left side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            ``True`` if the Interval is closed on the left-side, else
            ``False``.
        """

    open_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is open on the right side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            ``True`` if the Interval is closed on the left-side, else
            ``False``.
        """



class Interval(IntervalMixin):
    """
    Immutable object implementing an Interval, a bounded slice-like interval.
    
        .. versionadded:: 0.20.0
    
        Parameters
        ----------
        left : orderable scalar
            Left bound for the interval.
        right : orderable scalar
            Right bound for the interval.
        closed : {'left', 'right', 'both', 'neither'}, default 'right'
            Whether the interval is closed on the left-side, right-side, both or
            neither.
        closed : {'right', 'left', 'both', 'neither'}, default 'right'
            Whether the interval is closed on the left-side, right-side, both or
            neither. See the Notes for more detailed explanation.
    
        See Also
        --------
        IntervalIndex : An Index of Interval objects that are all closed on the
            same side.
        cut : Convert continuous data into discrete bins (Categorical
            of Interval objects).
        qcut : Convert continuous data into bins (Categorical of Interval objects)
            based on quantiles.
        Period : Represents a period of time.
    
        Notes
        -----
        The parameters `left` and `right` must be from the same type, you must be
        able to compare them and they must satisfy ``left <= right``.
    
        A closed interval (in mathematics denoted by square brackets) contains
        its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the
        conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.
        An open interval (in mathematics denoted by parentheses) does not contain
        its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the
        conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.
        Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is
        described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is
        described by ``0 < x <= 5`` (``closed='right'``).
    
        Examples
        --------
        It is possible to build Intervals of different types, like numeric ones:
    
        >>> iv = pd.Interval(left=0, right=5)
        >>> iv
        Interval(0, 5, closed='right')
    
        You can check if an element belongs to it
    
        >>> 2.5 in iv
        True
    
        You can test the bounds (``closed='right'``, so ``0 < x <= 5``):
    
        >>> 0 in iv
        False
        >>> 5 in iv
        True
        >>> 0.0001 in iv
        True
    
        Calculate its length
    
        >>> iv.length
        5
    
        You can operate with `+` and `*` over an Interval and the operation
        is applied to each of its bounds, so the result depends on the type
        of the bound elements
    
        >>> shifted_iv = iv + 3
        >>> shifted_iv
        Interval(3, 8, closed='right')
        >>> extended_iv = iv * 10.0
        >>> extended_iv
        Interval(0.0, 50.0, closed='right')
    
        To create a time interval you can use Timestamps as the bounds
    
        >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),
        ...                         pd.Timestamp('2018-01-01 00:00:00'),
        ...                         closed='left')
        >>> pd.Timestamp('2017-01-01 00:00') in year_2017
        True
        >>> year_2017.length
        Timedelta('365 days 00:00:00')
    
        And also you can create string intervals
    
        >>> volume_1 = pd.Interval('Ant', 'Dog', closed='both')
        >>> 'Bee' in volume_1
        True
    """
    def overlaps(self, i2): # real signature unknown; restored from __doc__
        """
        Check whether two Interval objects overlap.
        
                Two intervals overlap if they share a common point, including closed
                endpoints. Intervals that only have an open endpoint in common do not
                overlap.
        
                .. versionadded:: 0.24.0
        
                Parameters
                ----------
                other : Interval
                    The interval to check against for an overlap.
        
                Returns
                -------
                bool
                    ``True`` if the two intervals overlap, else ``False``.
        
                See Also
                --------
                IntervalArray.overlaps : The corresponding method for IntervalArray.
                IntervalIndex.overlaps : The corresponding method for IntervalIndex.
        
                Examples
                --------
                >>> i1 = pd.Interval(0, 2)
                >>> i2 = pd.Interval(1, 3)
                >>> i1.overlaps(i2)
                True
                >>> i3 = pd.Interval(4, 5)
                >>> i1.overlaps(i3)
                False
        
                Intervals that share closed endpoints overlap:
        
                >>> i4 = pd.Interval(0, 1, closed='both')
                >>> i5 = pd.Interval(1, 2, closed='both')
                >>> i4.overlaps(i5)
                True
        
                Intervals that only have an open endpoint in common do not overlap:
        
                >>> i6 = pd.Interval(1, 2, closed='neither')
                >>> i4.overlaps(i6)
                False
        """
        pass

    def _repr_base(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __floordiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, left=0, right=5): # real signature unknown; restored from __doc__
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rfloordiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rfloordiv__(y) <==> y//x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__truediv__(y) <==> x/y """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Whether the interval is closed on the left-side, right-side, both or
    neither
    """

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Left bound for the interval"""

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Right bound for the interval"""


    _typ = 'interval'


class IntervalTree(IntervalMixin):
    """
    A centered interval tree
    
        Based off the algorithm described on Wikipedia:
        http://en.wikipedia.org/wiki/Interval_tree
    
        we are emulating the IndexEngine interface
    """
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def get_loc_interval(self, *args, **kwargs): # real signature unknown
        """
        Lookup the intervals enclosed in the given interval bounds
        
                The given interval is presumed to have closed bounds.
        """
        pass

    def _get_partial_overlap(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals with the given side
                falling between the left and right bounds of an interval query
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                left, right : np.ndarray[ndim=1]
                    Left and right bounds for each interval. Assumed to contain no
                    NaNs.
                closed : {'left', 'right', 'both', 'neither'}, optional
                    Whether the intervals are closed on the left-side, right-side, both
                    or neither. Defaults to 'right'.
                leaf_size : int, optional
                    Parameter that controls when the tree switches from creating nodes
                    to brute-force search. Tune this parameter to optimize query
                    performance.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __pyx_fuse_0get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_0get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_0get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_1get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_1get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_1get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_2get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_2get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_2get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_3get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_3get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_3get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_4get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_4get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_4get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_overlapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Determine if the IntervalTree contains overlapping intervals.
        Cached as self._is_overlapping.
        """

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the left labels; this is used for binary search
        """

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the right labels
        """

    root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Uint64ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBE40>'


class Uint64ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBDE0>'


class Uint64ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBE70>'


class Uint64ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003DCBE10>'


# variables with complex values

NODE_CLASSES = {
    (
        'float32',
        'both',
    ): 
        Float32ClosedBothIntervalNode
    ,
    (
        'float32',
        'left',
    ): 
        Float32ClosedLeftIntervalNode
    ,
    (
        'float32',
        'neither',
    ): 
        Float32ClosedNeitherIntervalNode
    ,
    (
        'float32',
        'right',
    ): 
        Float32ClosedRightIntervalNode
    ,
    (
        'float64',
        'both',
    ): 
        Float64ClosedBothIntervalNode
    ,
    (
        'float64',
        'left',
    ): 
        Float64ClosedLeftIntervalNode
    ,
    (
        'float64',
        'neither',
    ): 
        Float64ClosedNeitherIntervalNode
    ,
    (
        'float64',
        'right',
    ): 
        Float64ClosedRightIntervalNode
    ,
    (
        'int32',
        'both',
    ): 
        Int32ClosedBothIntervalNode
    ,
    (
        'int32',
        'left',
    ): 
        Int32ClosedLeftIntervalNode
    ,
    (
        'int32',
        'neither',
    ): 
        Int32ClosedNeitherIntervalNode
    ,
    (
        'int32',
        'right',
    ): 
        Int32ClosedRightIntervalNode
    ,
    (
        'int64',
        'both',
    ): 
        Int64ClosedBothIntervalNode
    ,
    (
        'int64',
        'left',
    ): 
        Int64ClosedLeftIntervalNode
    ,
    (
        'int64',
        'neither',
    ): 
        Int64ClosedNeitherIntervalNode
    ,
    (
        'int64',
        'right',
    ): 
        Int64ClosedRightIntervalNode
    ,
    (
        'uint64',
        'both',
    ): 
        Uint64ClosedBothIntervalNode
    ,
    (
        'uint64',
        'left',
    ): 
        Uint64ClosedLeftIntervalNode
    ,
    (
        'uint64',
        'neither',
    ): 
        Uint64ClosedNeitherIntervalNode
    ,
    (
        'uint64',
        'right',
    ): 
        Uint64ClosedRightIntervalNode
    ,
}

_VALID_CLOSED = None # (!) real value is "frozenset(['both', 'neither', 'right', 'left'])"

__test__ = {
    u'Interval.overlaps (line 370)': u"\n        Check whether two Interval objects overlap.\n\n        Two intervals overlap if they share a common point, including closed\n        endpoints. Intervals that only have an open endpoint in common do not\n        overlap.\n\n        .. versionadded:: 0.24.0\n\n        Parameters\n        ----------\n        other : Interval\n            The interval to check against for an overlap.\n\n        Returns\n        -------\n        bool\n            ``True`` if the two intervals overlap, else ``False``.\n\n        See Also\n        --------\n        IntervalArray.overlaps : The corresponding method for IntervalArray.\n        IntervalIndex.overlaps : The corresponding method for IntervalIndex.\n\n        Examples\n        --------\n        >>> i1 = pd.Interval(0, 2)\n        >>> i2 = pd.Interval(1, 3)\n        >>> i1.overlaps(i2)\n        True\n        >>> i3 = pd.Interval(4, 5)\n        >>> i1.overlaps(i3)\n        False\n\n        Intervals that share closed endpoints overlap:\n\n        >>> i4 = pd.Interval(0, 1, closed='both')\n        >>> i5 = pd.Interval(1, 2, closed='both')\n        >>> i4.overlaps(i5)\n        True\n\n        Intervals that only have an open endpoint in common do not overlap:\n\n        >>> i6 = pd.Interval(1, 2, closed='neither')\n        >>> i4.overlaps(i6)\n        False\n        ",
}


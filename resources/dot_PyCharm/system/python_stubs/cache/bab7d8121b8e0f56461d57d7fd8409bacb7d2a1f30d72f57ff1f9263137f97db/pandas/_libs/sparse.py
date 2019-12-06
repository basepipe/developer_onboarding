# encoding: utf-8
# module pandas._libs.sparse
# from C:\Python27\lib\site-packages\pandas\_libs\sparse.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# functions

def get_blocks(*args, **kwargs): # real signature unknown
    pass

def make_mask_object_ndarray(*args, **kwargs): # real signature unknown
    pass

def sparse_add_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_add_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_and_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_and_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_div_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_div_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_eq_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_eq_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_add_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_add_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_and_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_and_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_div_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_div_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_eq_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_eq_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_floordiv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_floordiv_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_ge_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_ge_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_gt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_gt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_le_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_le_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_lt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_lt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_mod_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_mod_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_mul_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_mul_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_ne_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_ne_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_or_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_or_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_pow_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_pow_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_sub_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_sub_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_truediv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_fill_truediv_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_floordiv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_floordiv_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_ge_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_ge_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_gt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_gt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_le_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_le_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_lt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_lt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_mod_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_mod_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_mul_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_mul_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_ne_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_ne_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_or_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_or_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_pow_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_pow_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_sub_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_sub_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_truediv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_truediv_int64(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockMerge(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockUnion(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SparseIndex(*args, **kwargs): # real signature unknown
    pass

# classes

class SparseIndex(object):
    """ Abstract superclass for sparse index types. """
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


class BlockIndex(SparseIndex):
    """
    Object for holding block-based sparse indexing information
    
        Parameters
        ----------
    """
    def check_integrity(self, *args, **kwargs): # real signature unknown
        """
        Check:
                - Locations are in ascending order
                - No overlapping blocks
                - Blocks to not start after end of index, nor extend beyond end
        """
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        """
        Intersect two BlockIndex objects
        
                Parameters
                ----------
        
                Returns
                -------
                intersection : BlockIndex
        """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """
        Return the internal location if value exists on given index.
                Return -1 otherwise.
        """
        pass

    def lookup_array(self, *args, **kwargs): # real signature unknown
        """ Vectorized lookup, returns ndarray[int32_t] """
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        """
        Combine together two BlockIndex objects, accepting indices if contained
                in one or the other
        
                Parameters
                ----------
                other : SparseIndex
        
                Notes
                -----
                union is a protected keyword in Cython, hence make_union
        
                Returns
                -------
                union : BlockIndex
        """
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def reindex(self, *args, **kwargs): # real signature unknown
        pass

    def take(self, *args, **kwargs): # real signature unknown
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
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

    blengths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nblocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000068DBAB0>'


class BlockMerge(object):
    """
    Object-oriented approach makes sharing state between recursive functions a
        lot easier and reduces code duplication
    """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000068DBAE0>'


class BlockUnion(BlockMerge):
    """
    Object-oriented approach makes sharing state between recursive functions a
        lot easier and reduces code duplication
    """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000068DBB10>'


class IntIndex(SparseIndex):
    """
    Object for holding exact integer sparse indexing information
    
        Parameters
        ----------
        length : integer
        indices : array-like
            Contains integers corresponding to the indices.
    """
    def check_integrity(self, *args, **kwargs): # real signature unknown
        """
        Checks the following:
        
                - Indices are strictly ascending
                - Number of indices is at most self.length
                - Indices are at least 0 and at most the total length less one
        
                A ValueError is raised if any of these conditions is violated.
        """
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """
        Return the internal location if value exists on given index.
                Return -1 otherwise.
        """
        pass

    def lookup_array(self, *args, **kwargs): # real signature unknown
        """ Vectorized lookup, returns ndarray[int32_t] """
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def reindex(self, *args, **kwargs): # real signature unknown
        pass

    def take(self, *args, **kwargs): # real signature unknown
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
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

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000068DBA50>'


# variables with complex values

__test__ = {}


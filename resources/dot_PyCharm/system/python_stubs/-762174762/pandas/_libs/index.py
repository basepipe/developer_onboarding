# encoding: utf-8
# module pandas._libs.index
# from C:\Python27\lib\site-packages\pandas\_libs\index.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import pandas._libs.tslibs.period as periodlib # C:\Python27\lib\site-packages\pandas\_libs\tslibs\period.pyd
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pandas._libs.algos as algos # C:\Python27\lib\site-packages\pandas\_libs\algos.pyd
import pandas._libs.hashtable as _hash # C:\Python27\lib\site-packages\pandas\_libs\hashtable.pyd
from datetime import date, datetime, timedelta

from pandas._libs.missing import checknull

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


# Variables with simple values

_SIZE_CUTOFF = 1000000

# functions

def convert_scalar(*args, **kwargs): # real signature unknown
    pass

def get_value_at(*args, **kwargs): # real signature unknown
    pass

def get_value_box(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BaseMultiIndexCodesEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_DatetimeEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IndexEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int16Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int8Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ObjectEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PeriodEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_TimedeltaEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt16Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt8Engine(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseMultiIndexCodesEngine(object):
    """
    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which
        represent each label in a MultiIndex as an integer, by juxtaposing the bits
        encoding each level, with appropriate offsets.
    
        For instance: if 3 levels have respectively 3, 6 and 1 possible values,
        then their labels can be represented using respectively 2, 3 and 1 bits,
        as follows:
         _ _ _ _____ _ __ __ __
        |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾
        and the resulting unsigned integer representation will be:
         _ _ _ _____ _ __ __ __ __ __ __
        |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾
    
        Offsets are calculated at initialization, labels are transformed by method
        _codes_to_ints.
    
        Keys are located by first locating each component against the respective
        level, then locating (the integer representation of) codes.
    """
    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def _extract_level_codes(self, *args, **kwargs): # real signature unknown
        """
        Map the requested list of (tuple) keys to their integer representations
                for searching in the underlying integer index.
        
                Parameters
                ----------
                target : list-like of keys
                    Each key is a tuple, with a label for each level of the index.
        
                Returns
                ------
                int_keys : 1-dimensional array of dtype uint64 or object
                    Integers representing one combination each
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                levels : list-like of numpy arrays
                    Levels of the MultiIndex
                labels : list-like of numpy arrays of integer dtype
                    Labels of the MultiIndex
                offsets : numpy array of uint64 dtype
                    Pre-calculated offsets, one for each level of the index
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class IndexEngine(object):
    # no doc
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        return an indexer suitable for takng from a non unique index
                    return the labels in the same order ast the target
                    and a missing indexer into the targets (which correspond
                    to the -1 indices in the results
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the sizeof our mapping """
        pass

    def _call_map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
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

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    is_mapping_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    over_size_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vgetter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006753F00>'


class Int64Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006753F60>'


class DatetimeEngine(Int64Engine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006753F90>'


class Float32Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761090>'


class Float64Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761060>'


class Int16Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000067610F0>'


class Int32Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000067610C0>'


class Int8Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761120>'


class ObjectEngine(IndexEngine):
    """ Index Engine for use with object-dtype Index, namely the base class Index """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006753F30>'


class PeriodEngine(Int64Engine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761030>'


class TimedeltaEngine(DatetimeEngine):
    # no doc
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006753FC0>'


class UInt16Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000067611B0>'


class UInt32Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761180>'


class UInt64Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000006761150>'


class UInt8Engine(IndexEngine):
    # no doc
    def _call_map_locations(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000067611E0>'


# variables with complex values

__test__ = {}


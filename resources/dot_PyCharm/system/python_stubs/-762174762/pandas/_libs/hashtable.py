# encoding: utf-8
# module pandas._libs.hashtable
# from C:\Python27\lib\site-packages\pandas\_libs\hashtable.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# Variables with simple values

_SIZE_HINT_LIMIT = 1048583

# functions

def duplicated_float64(*args, **kwargs): # real signature unknown
    pass

def duplicated_int64(*args, **kwargs): # real signature unknown
    pass

def duplicated_object(*args, **kwargs): # real signature unknown
    pass

def duplicated_uint64(*args, **kwargs): # real signature unknown
    pass

def ismember_float64(*args, **kwargs): # real signature unknown
    """
    Return boolean of values in arr on an
        element by-element basis
    
        Parameters
        ----------
        arr : float64 ndarray
        values : float64 ndarray
    
        Returns
        -------
        boolean ndarry len of (arr)
    """
    pass

def ismember_int64(*args, **kwargs): # real signature unknown
    """
    Return boolean of values in arr on an
        element by-element basis
    
        Parameters
        ----------
        arr : int64 ndarray
        values : int64 ndarray
    
        Returns
        -------
        boolean ndarry len of (arr)
    """
    pass

def ismember_object(*args, **kwargs): # real signature unknown
    """
    Return boolean of values in arr on an
        element by-element basis
    
        Parameters
        ----------
        arr : object ndarray
        values : object ndarray
    
        Returns
        -------
        boolean ndarry len of (arr)
    """
    pass

def ismember_uint64(*args, **kwargs): # real signature unknown
    """
    Return boolean of values in arr on an
        element by-element basis
    
        Parameters
        ----------
        arr : uint64 ndarray
        values : uint64 ndarray
    
        Returns
        -------
        boolean ndarry len of (arr)
    """
    pass

def mode_float64(*args, **kwargs): # real signature unknown
    pass

def mode_int64(*args, **kwargs): # real signature unknown
    pass

def mode_object(*args, **kwargs): # real signature unknown
    pass

def mode_uint64(*args, **kwargs): # real signature unknown
    pass

def unique_label_indices(*args, **kwargs): # real signature unknown
    """
    indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def value_count_float64(*args, **kwargs): # real signature unknown
    pass

def value_count_int64(*args, **kwargs): # real signature unknown
    pass

def value_count_object(*args, **kwargs): # real signature unknown
    pass

def value_count_uint64(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Factorizer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_HashTable(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64Factorizer(*args, **kwargs): # real signature unknown
    pass

# classes

class Factorizer(object):
    # no doc
    def factorize(self, np_array, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Factorize values with nans replaced by na_sentinel
                >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)
                array([ 0,  1, 20])
        """
        pass

    def get_count(self, *args, **kwargs): # real signature unknown
        pass

    def unique(self, *args, **kwargs): # real signature unknown
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

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uniques = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HashTable(object):
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


class Float64HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[float64]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
        
                Returns
                -------
                uniques : ndarray[float64]
                    Unique values of input, not sorted
                labels : ndarray[int64]
                    The labels from values to uniques
        """
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels_groupby(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[float64]
                    Array of values of which unique will be calculated
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[float64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[float64]
                    Array of values of which unique will be calculated
                uniques : Float64Vector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                ignore_na : boolean, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[float64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse=True)
                    The labels from values to uniques
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D210C0>'


class Float64Vector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D211B0>'


class Int64Factorizer(object):
    # no doc
    def factorize(self, np_array, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Factorize values with nans replaced by na_sentinel
                >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)
                array([ 0,  1, 20])
        """
        pass

    def get_count(self, *args, **kwargs): # real signature unknown
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

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uniques = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Int64HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[int64]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
        
                Returns
                -------
                uniques : ndarray[int64]
                    Unique values of input, not sorted
                labels : ndarray[int64]
                    The labels from values to uniques
        """
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels_groupby(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[int64]
                    Array of values of which unique will be calculated
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[int64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[int64]
                    Array of values of which unique will be calculated
                uniques : Int64Vector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                ignore_na : boolean, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[int64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse=True)
                    The labels from values to uniques
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21090>'


class Int64Vector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21180>'


class ObjectVector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21240>'


class PyObjectHashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then None _plus_
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64]
                    The labels from values to uniques
        """
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                uniques : ObjectVector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then None _plus_
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                ignore_na : boolean, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse=True)
                    The labels from values to uniques
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D210F0>'


class StringHashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then any value
                    that is not a string is considered missing. If na_value is
                    not None, then _additionally_ any value "val" satisfying
                    val == na_value is considered missing.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64]
                    The labels from values to uniques
        """
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[object]
                    Array of values of which unique will be calculated
                uniques : ObjectVector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then any value
                    that is not a string is considered missing. If na_value is
                    not None, then _additionally_ any value "val" satisfying
                    val == na_value is considered missing.
                ignore_na : boolean, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[object]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse=True)
                    The labels from values to uniques
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

    na_string_sentinel = '__nan__'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21150>'


class StringVector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21210>'


class UInt64HashTable(HashTable):
    # no doc
    def factorize(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Missing values are not included in the "uniques" for this method.
                The labels for any missing values will be set to "na_sentinel"
        
                Parameters
                ----------
                values : ndarray[uint64]
                    Array of values of which unique will be calculated
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
        
                Returns
                -------
                uniques : ndarray[uint64]
                    Unique values of input, not sorted
                labels : ndarray[int64]
                    The labels from values to uniques
        """
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_labels_groupby(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def map_locations(self, *args, **kwargs): # real signature unknown
        pass

    def set_item(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the size of my table in bytes """
        pass

    def unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[uint64]
                    Array of values of which unique will be calculated
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[uint64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse)
                    The labels from values to uniques
        """
        pass

    def _unique(self, *args, **kwargs): # real signature unknown
        """
        Calculate unique values and labels (no sorting!)
        
                Parameters
                ----------
                values : ndarray[uint64]
                    Array of values of which unique will be calculated
                uniques : UInt64Vector
                    Vector into which uniques will be written
                count_prior : Py_ssize_t, default 0
                    Number of existing entries in uniques
                na_sentinel : Py_ssize_t, default -1
                    Sentinel value used for all NA-values in inverse
                na_value : object, default None
                    Value to identify as missing. If na_value is None, then
                    any value "val" satisfying val != val is considered missing.
                    If na_value is not None, then _additionally_, any value "val"
                    satisfying val == na_value is considered missing.
                ignore_na : boolean, default False
                    Whether NA-values should be ignored for calculating the uniques. If
                    True, the labels corresponding to missing values will be set to
                    na_sentinel.
                return_inverse : boolean, default False
                    Whether the mapping of the original array values to their location
                    in the vector of uniques should be returned.
        
                Returns
                -------
                uniques : ndarray[uint64]
                    Unique values of input, not sorted
                labels : ndarray[int64] (if return_inverse=True)
                    The labels from values to uniques
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D21060>'


class UInt64Vector(object):
    # no doc
    def to_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000003D211E0>'


# variables with complex values

__test__ = {
    u'Factorizer.factorize (line 67)': u"\n        Factorize values with nans replaced by na_sentinel\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        ",
    u'Int64Factorizer.factorize (line 111)': u"\n        Factorize values with nans replaced by na_sentinel\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        ",
}


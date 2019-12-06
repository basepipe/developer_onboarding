# encoding: utf-8
# module pandas._libs.lib
# from C:\Python27\lib\site-packages\pandas\_libs\lib.pyd
# by generator 1.147
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import warnings as warnings # C:\Python27\lib\warnings.pyc
import sys as sys # <module 'sys' (built-in)>
from pandas._libs.tslib import array_to_datetime

from pandas._libs.tslibs.nattype import NaT

import numbers as __numbers


# functions

def array_equivalent_object(*args, **kwargs): # real signature unknown
    """
    perform an element by element comparion on 1-d object arrays
            taking into account nan positions
    """
    pass

def astype_intsafe(*args, **kwargs): # real signature unknown
    pass

def astype_str(*args, **kwargs): # real signature unknown
    """
    Convert all elements in an array to string.
    
        Parameters
        ----------
        arr : ndarray
            The array whose elements we are casting.
        skipna : bool, default False
            Whether or not to coerce nulls to their stringified form
            (e.g. NaN becomes 'nan').
    
        Returns
        -------
        casted_arr : ndarray
            A new array with the input array's elements casted.
    """
    pass

def astype_unicode(*args, **kwargs): # real signature unknown
    """
    Convert all elements in an array to unicode.
    
        Parameters
        ----------
        arr : ndarray
            The array whose elements we are casting.
        skipna : bool, default False
            Whether or not to coerce nulls to their stringified form
            (e.g. NaN becomes 'nan').
    
        Returns
        -------
        casted_arr : ndarray
            A new array with the input array's elements casted.
    """
    pass

def clean_index_list(*args, **kwargs): # real signature unknown
    """ Utility used in pandas.core.index.ensure_index """
    pass

def count_level_2d(*args, **kwargs): # real signature unknown
    pass

def dicts_to_array(*args, **kwargs): # real signature unknown
    pass

def fast_multiget(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple(*args, **kwargs): # real signature unknown
    """
    Generate a list of unique values from a list of arrays.
    
        Parameters
        ----------
        list : array-like
            A list of array-like objects
        sort : boolean
            Whether or not to sort the resulting unique list
    
        Returns
        -------
        unique_list : list of unique values
    """
    pass

def fast_unique_multiple_list(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list_gen(*args, **kwargs): # real signature unknown
    """
    Generate a list of unique values from a generator of lists.
    
        Parameters
        ----------
        gen : generator object
            A generator of lists from which the unique list is created
        sort : boolean
            Whether or not to sort the resulting unique list
    
        Returns
        -------
        unique_list : list of unique values
    """
    pass

def fast_zip(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def generate_bins_dt64(*args, **kwargs): # real signature unknown
    """ Int64 (datetime64) version of generic python version in groupby.py """
    pass

def generate_slices(*args, **kwargs): # real signature unknown
    pass

def get_level_sorter(*args, **kwargs): # real signature unknown
    """
    argsort for a single level of a multi-index, keeping the order of higher
        levels unchanged. `starts` points to starts of same-key indices w.r.t
        to leading levels; equivalent to:
            np.hstack([label[starts[i]:starts[i+1]].argsort(kind='mergesort')
                + starts[i] for i in range(len(starts) - 1)])
    """
    pass

def get_reverse_indexer(*args, **kwargs): # real signature unknown
    """
    Reverse indexing operation.
    
        Given `indexer`, make `indexer_inv` of it, such that::
    
            indexer_inv[indexer[x]] = x
    
        .. note:: If indexer is not unique, only first occurrence is accounted.
    """
    pass

def has_infs_f4(*args, **kwargs): # real signature unknown
    pass

def has_infs_f8(*args, **kwargs): # real signature unknown
    pass

def indices_fast(*args, **kwargs): # real signature unknown
    pass

def infer_datetimelike_array(*args, **kwargs): # real signature unknown
    """
    infer if we have a datetime or timedelta array
        - date: we have *only* date and maybe strings, nulls
        - datetime: we have *only* datetimes and maybe strings, nulls
        - timedelta: we have *only* timedeltas and maybe strings, nulls
        - nat: we do not have *any* date, datetimes or timedeltas, but do have
          at least a NaT
        - mixed: other objects (strings, a mix of tz-aware and tz-naive, or
                                actual objects)
    
        Parameters
        ----------
        arr : object array
    
        Returns
        -------
        string: {datetime, timedelta, date, nat, mixed}
    """
    pass

def infer_dtype(foo=None, bar=None): # real signature unknown; restored from __doc__
    """
    Efficiently infer the type of a passed val, or list-like
        array of values. Return a string describing the type.
    
        Parameters
        ----------
        value : scalar, list, ndarray, or pandas type
        skipna : bool, default False
            Ignore NaN values when inferring the type.
    
            .. versionadded:: 0.21.0
    
        Returns
        -------
        string describing the common type of the input data.
        Results can include:
    
        - string
        - unicode
        - bytes
        - floating
        - integer
        - mixed-integer
        - mixed-integer-float
        - decimal
        - complex
        - categorical
        - boolean
        - datetime64
        - datetime
        - date
        - timedelta64
        - timedelta
        - time
        - period
        - mixed
    
        Raises
        ------
        TypeError if ndarray-like but cannot infer the dtype
    
        Notes
        -----
        - 'mixed' is the catchall for anything that is not otherwise
          specialized
        - 'mixed-integer-float' are floats and integers
        - 'mixed-integer' are integers mixed with non-integers
    
        Examples
        --------
        >>> infer_dtype(['foo', 'bar'])
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=True)
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=False)
        'mixed'
    
        >>> infer_dtype([b'foo', b'bar'])
        'bytes'
    
        >>> infer_dtype([1, 2, 3])
        'integer'
    
        >>> infer_dtype([1, 2, 3.5])
        'mixed-integer-float'
    
        >>> infer_dtype([1.0, 2.0, 3.5])
        'floating'
    
        >>> infer_dtype(['a', 1])
        'mixed-integer'
    
        >>> infer_dtype([Decimal(1), Decimal(2.0)])
        'decimal'
    
        >>> infer_dtype([True, False])
        'boolean'
    
        >>> infer_dtype([True, False, np.nan])
        'mixed'
    
        >>> infer_dtype([pd.Timestamp('20130101')])
        'datetime'
    
        >>> infer_dtype([datetime.date(2013, 1, 1)])
        'date'
    
        >>> infer_dtype([np.datetime64('2013-01-01')])
        'datetime64'
    
        >>> infer_dtype([datetime.timedelta(0, 1, 1)])
        'timedelta'
    
        >>> infer_dtype(pd.Series(list('aabc')).astype('category'))
        'categorical'
    """
    pass

def is_bool(*args, **kwargs): # real signature unknown
    pass

def is_bool_array(*args, **kwargs): # real signature unknown
    pass

def is_complex(*args, **kwargs): # real signature unknown
    pass

def is_datetime64_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_with_singletz_array(*args, **kwargs): # real signature unknown
    """
    Check values have the same tzinfo attribute.
        Doesn't check values are datetime-like types.
    """
    pass

def is_date_array(*args, **kwargs): # real signature unknown
    pass

def is_decimal(*args, **kwargs): # real signature unknown
    pass

def is_float(*args, **kwargs): # real signature unknown
    pass

def is_float_array(*args, **kwargs): # real signature unknown
    pass

def is_integer(*args, **kwargs): # real signature unknown
    pass

def is_integer_array(*args, **kwargs): # real signature unknown
    pass

def is_interval(*args, **kwargs): # real signature unknown
    pass

def is_interval_array(*args, **kwargs): # real signature unknown
    pass

def is_period(*args, **kwargs): # real signature unknown
    """ Return a boolean if this is a Period object """
    pass

def is_period_array(*args, **kwargs): # real signature unknown
    pass

def is_scalar(dt): # real signature unknown; restored from __doc__
    """
    Return True if given value is scalar.
    
        Parameters
        ----------
        val : object
            This includes:
    
            - numpy array scalar (e.g. np.int64)
            - Python builtin numerics
            - Python builtin byte arrays and strings
            - None
            - datetime.datetime
            - datetime.timedelta
            - Period
            - decimal.Decimal
            - Interval
            - DateOffset
            - Fraction
            - Number
    
        Returns
        -------
        bool
            Return True if given object is scalar, False otherwise
    
        Examples
        --------
        >>> dt = pd.datetime.datetime(2018, 10, 3)
        >>> pd.is_scalar(dt)
        True
    
        >>> pd.api.types.is_scalar([2, 3])
        False
    
        >>> pd.api.types.is_scalar({0: 1, 2: 3})
        False
    
        >>> pd.api.types.is_scalar((0, 2))
        False
    
        pandas supports PEP 3141 numbers:
    
        >>> from fractions import Fraction
        >>> pd.api.types.is_scalar(Fraction(3, 5))
        True
    """
    pass

def is_string_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_or_timedelta64_array(*args, **kwargs): # real signature unknown
    """ infer with timedeltas and/or nat/none """
    pass

def is_time_array(*args, **kwargs): # real signature unknown
    pass

def item_from_zerodim(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    If the value is a zerodim array, return the item it contains.
    
        Parameters
        ----------
        val : object
    
        Returns
        -------
        result : object
    
        Examples
        --------
        >>> item_from_zerodim(1)
        1
        >>> item_from_zerodim('foobar')
        'foobar'
        >>> item_from_zerodim(np.array(1))
        1
        >>> item_from_zerodim(np.array([1]))
        array([1])
    """
    pass

def map_infer(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def map_infer_mask(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def maybe_booleans_to_slice(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_numeric(*args, **kwargs): # real signature unknown
    """
    Convert object array to a numeric array if possible.
    
        Parameters
        ----------
        values : ndarray
            Array of object elements to convert.
        na_values : set
            Set of values that should be interpreted as NaN.
        convert_empty : bool, default True
            If an empty array-like object is encountered, whether to interpret
            that element as NaN or not. If set to False, a ValueError will be
            raised if such an element is encountered and 'coerce_numeric' is False.
        coerce_numeric : bool, default False
            If initial attempts to convert to numeric have failed, whether to
            force conversion to numeric via alternative methods or by setting the
            element to NaN. Otherwise, an Exception will be raised when such an
            element is encountered.
    
            This boolean also has an impact on how conversion behaves when a
            numeric array has no suitable numerical dtype to return (i.e. uint64,
            int32, uint8). If set to False, the original object array will be
            returned. Otherwise, a ValueError will be raised.
    
        Returns
        -------
        numeric_array : array of converted object values to numerical ones
    """
    pass

def maybe_convert_objects(*args, **kwargs): # real signature unknown
    """ Type inference function-- convert object array to proper dtype """
    pass

def maybe_indices_to_slice(*args, **kwargs): # real signature unknown
    pass

def memory_usage_of_objects(*args, **kwargs): # real signature unknown
    """
    return the memory usage of an object array in bytes,
        does not include the actual bytes of the pointers
    """
    pass

def row_bool_subset(*args, **kwargs): # real signature unknown
    pass

def row_bool_subset_object(*args, **kwargs): # real signature unknown
    pass

def to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert a list of lists into an object array.
    
        Parameters
        ----------
        rows : 2-d array (N, K)
            A list of lists to be converted into an array
        min_width : int
            The minimum width of the object array. If a list
            in `rows` contains fewer than `width` elements,
            the remaining elements in the corresponding row
            will all be `NaN`.
    
        Returns
        -------
        obj_array : numpy array of the object dtype
    """
    pass

def to_object_array_tuples(*args, **kwargs): # real signature unknown
    pass

def tuples_to_object_array(*args, **kwargs): # real signature unknown
    pass

def values_from_object(*args, **kwargs): # real signature unknown
    """ return my values or the object if we are say an ndarray """
    pass

# classes

class Validator(object):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E61B0>'


class TemporalValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6330>'


class TimedeltaValidator(TemporalValidator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E63C0>'


class AnyTimedeltaValidator(TimedeltaValidator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E63F0>'


class BoolValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E61E0>'


class BytesValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6300>'


class DatetimeValidator(TemporalValidator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6360>'


class Datetime64Validator(DatetimeValidator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6390>'


class DateValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6420>'


class Decimal(object):
    """ Floating point class for decimal arithmetic. """
    def adjusted(self, *args, **kwargs): # real signature unknown
        """ Return the adjusted exponent of self """
        pass

    def as_tuple(self, *args, **kwargs): # real signature unknown
        """
        Represents the number as a triple tuple.
        
                To show the internals exactly as they are.
        """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """
        Returns the same Decimal object.
        
                As we do not have different encodings for the same number, the
                received object already is in its canonical form.
        """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """
        Compares one to another.
        
                -1 => a < b
                0  => a = b
                1  => a > b
                NaN => one is NaN
                Like __cmp__, but returns Decimal instances.
        """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """
        Compares self to the other operand numerically.
        
                It's pretty much like compare(), but all NaNs signal, with signaling
                NaNs taking precedence over quiet NaNs.
        """
        pass

    def compare_total(self, *args, **kwargs): # real signature unknown
        """
        Compares self to other using the abstract representations.
        
                This is not like the standard compare, which use their numerical
                value. Note that a total ordering is defined for all possible abstract
                representations.
        """
        pass

    def compare_total_mag(self, *args, **kwargs): # real signature unknown
        """
        Compares self to other using abstract repr., ignoring sign.
        
                Like compare_total, but with operand's sign ignored and assumed to be 0.
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """ Returns a copy with the sign set to 0. """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """ Returns a copy with the sign inverted. """
        pass

    def copy_sign(self, *args, **kwargs): # real signature unknown
        """ Returns self with the sign of other. """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """ Returns e ** self. """
        pass

    def fma(self, *args, **kwargs): # real signature unknown
        """
        Fused multiply-add.
        
                Returns self*other+third with no rounding of the intermediate
                product self*other.
        
                self and other are multiplied together, with no rounding of
                the result.  The third operand is then added to the result,
                and a single final rounding is performed.
        """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Converts a float to a decimal number, exactly.
        
                Note that Decimal.from_float(0.1) is not the same as Decimal('0.1').
                Since 0.1 is not exactly representable in binary floating point, the
                value is stored as the nearest representable value which is
                0x1.999999999999ap-4.  The exact equivalent of the value in decimal
                is 0.1000000000000000055511151231257827021181583404541015625.
        
                >>> Decimal.from_float(0.1)
                Decimal('0.1000000000000000055511151231257827021181583404541015625')
                >>> Decimal.from_float(float('nan'))
                Decimal('NaN')
                >>> Decimal.from_float(float('inf'))
                Decimal('Infinity')
                >>> Decimal.from_float(-float('inf'))
                Decimal('-Infinity')
                >>> Decimal.from_float(-0.0)
                Decimal('-0')
        """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """
        Return True if self is canonical; otherwise return False.
        
                Currently, the encoding of a Decimal instance is always
                canonical, so this method returns True for any Decimal.
        """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """
        Return True if self is finite; otherwise return False.
        
                A Decimal instance is considered finite if it is neither
                infinite nor a NaN.
        """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """ Return True if self is infinite; otherwise return False. """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """ Return True if self is a qNaN or sNaN; otherwise return False. """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """ Return True if self is a normal number; otherwise return False. """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if self is a quiet NaN; otherwise return False. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """ Return True if self is negative; otherwise return False. """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if self is a signaling NaN; otherwise return False. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """ Return True if self is subnormal; otherwise return False. """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """ Return True if self is a zero; otherwise return False. """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """ Returns the natural (base e) logarithm of self. """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """ Returns the base 10 logarithm of self. """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """
        Returns the exponent of the magnitude of self's MSD.
        
                The result is the integer which is the exponent of the magnitude
                of the most significant digit of self (as though it were truncated
                to a single digit while maintaining the value of that digit and
                without limiting the resulting exponent).
        """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Applies an 'and' operation between self and other's digits. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Invert all its digits. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Applies an 'or' operation between self and other's digits. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Applies an 'xor' operation between self and other's digits. """
        pass

    def max(self, other): # real signature unknown; restored from __doc__
        """
        Returns the larger value.
        
                Like max(self, other) except if one is not a number, returns
                NaN (and signals if one is sNaN).  Also rounds.
        """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """ Compares the values numerically with their sign ignored. """
        pass

    def min(self, other): # real signature unknown; restored from __doc__
        """
        Returns the smaller value.
        
                Like min(self, other) except if one is not a number, returns
                NaN (and signals if one is sNaN).  Also rounds.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """ Compares the values numerically with their sign ignored. """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """ Returns the largest representable number smaller than itself. """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """ Returns the smallest representable number larger than itself. """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """
        Returns the number closest to self, in the direction towards other.
        
                The result is the closest representable number to self
                (excluding self) that is in the direction towards other,
                unless both have the same value.  If the two operands are
                numerically equal, then the result is a copy of self with the
                sign set to be the same as the sign of other.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """ Normalize- strip trailing 0s, change anything equal to 0 to 0e0 """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """
        Returns an indication of the class of self.
        
                The class is one of the following strings:
                  sNaN
                  NaN
                  -Infinity
                  -Normal
                  -Subnormal
                  -Zero
                  +Zero
                  +Subnormal
                  +Normal
                  +Infinity
        """
        pass

    def quantize(self, *args, **kwargs): # real signature unknown
        """
        Quantize self so its exponent is the same as that of exp.
        
                Similar to self._rescale(exp._exp) but with error checking.
        """
        pass

    def radix(self, *args, **kwargs): # real signature unknown
        """ Just returns 10, as this is Decimal, :) """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """ Remainder nearest to 0-  abs(remainder-near) <= other/2 """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """ Returns a rotated copy of self, value-of-other times. """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """
        Return True if self and other have the same exponent; otherwise
                return False.
        
                If either operand is a special value, the following rules are used:
                   * return True if both operands are infinities
                   * return True if both operands are NaNs
                   * otherwise, return False.
        """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """ Returns self operand after adding the second value to its exp. """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """ Returns a shifted copy of self, value-of-other times. """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """ Return the square root of self. """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """
        Convert to a string, using engineering notation if an exponent is needed.
        
                Engineering notation has an exponent which is a multiple of 3.  This
                can leave up to 3 digits to the left of the decimal place and may
                require the addition of either one or two trailing zeros.
        """
        pass

    def to_integral(self, *args, **kwargs): # real signature unknown
        """ Rounds to the nearest integer, without raising inexact, rounded. """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """
        Rounds to a nearby integer.
        
                If no rounding mode is specified, take the rounding mode from
                the context.  This method raises the Rounded and Inexact flags
                when appropriate.
        
                See also: to_integral_value, which does exactly the same as
                this method except that it doesn't raise Inexact or Rounded.
        """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """ Rounds to the nearest integer, without raising inexact, rounded. """
        pass

    def _check_nans(self, *args, **kwargs): # real signature unknown
        """
        Returns whether the number is not actually one.
        
                if self, other are sNaN, signal
                if self, other are NaN return nan
                return 0
        
                Done before operations.
        """
        pass

    def _cmp(self, *args, **kwargs): # real signature unknown
        """
        Compare the two non-NaN decimal instances self and other.
        
                Returns -1 if self < other, 0 if self == other and 1
                if self > other.  This routine is for internal use only.
        """
        pass

    def _compare_check_nans(self, *args, **kwargs): # real signature unknown
        """
        Version of _check_nans used for the signaling comparisons
                compare_signal, __le__, __lt__, __ge__, __gt__.
        
                Signal InvalidOperation if either self or other is a (quiet
                or signaling) NaN.  Signaling NaNs take precedence over quiet
                NaNs.
        
                Return 0 if neither operand is a NaN.
        """
        pass

    def _divide(self, *args, **kwargs): # real signature unknown
        """
        Return (self // other, self % other), to context.prec precision.
        
                Assumes that neither self nor other is a NaN, that self is not
                infinite and that other is nonzero.
        """
        pass

    def _fill_logical(self, *args, **kwargs): # real signature unknown
        pass

    def _fix(self, *args, **kwargs): # real signature unknown
        """
        Round if it is necessary to keep self within prec precision.
        
                Rounds and fixes the exponent.  Does not raise on a sNaN.
        
                Arguments:
                self - Decimal instance
                context - context used.
        """
        pass

    def _fix_nan(self, *args, **kwargs): # real signature unknown
        """ Decapitate the payload of a NaN to fit the context """
        pass

    def _iseven(self, *args, **kwargs): # real signature unknown
        """ Returns True if self is even.  Assumes self is an integer. """
        pass

    def _isinfinity(self, *args, **kwargs): # real signature unknown
        """
        Returns whether the number is infinite
        
                0 if finite or not a number
                1 if +INF
                -1 if -INF
        """
        pass

    def _isinteger(self, *args, **kwargs): # real signature unknown
        """ Returns whether self is an integer """
        pass

    def _islogical(self, *args, **kwargs): # real signature unknown
        """
        Return True if self is a logical operand.
        
                For being logical, it must be a finite number with a sign of 0,
                an exponent of 0, and a coefficient whose digits must all be
                either 0 or 1.
        """
        pass

    def _isnan(self, *args, **kwargs): # real signature unknown
        """
        Returns whether the number is not actually one.
        
                0 if a number
                1 if NaN
                2 if sNaN
        """
        pass

    def _ln_exp_bound(self, *args, **kwargs): # real signature unknown
        """
        Compute a lower bound for the adjusted exponent of self.ln().
                In other words, compute r such that self.ln() >= 10**r.  Assumes
                that self is finite and positive and that self != 1.
        """
        pass

    def _log10_exp_bound(self, *args, **kwargs): # real signature unknown
        """
        Compute a lower bound for the adjusted exponent of self.log10().
                In other words, find r such that self.log10() >= 10**r.
                Assumes that self is finite and positive and that self != 1.
        """
        pass

    def _power_exact(self, *args, **kwargs): # real signature unknown
        """
        Attempt to compute self**other exactly.
        
                Given Decimals self and other and an integer p, attempt to
                compute an exact result for the power self**other, with p
                digits of precision.  Return None if self**other is not
                exactly representable in p digits.
        
                Assumes that elimination of special cases has already been
                performed: self and other must both be nonspecial; self must
                be positive and not numerically equal to 1; other must be
                nonzero.  For efficiency, other._exp should not be too large,
                so that 10**abs(other._exp) is a feasible calculation.
        """
        pass

    def _power_modulo(self, *args, **kwargs): # real signature unknown
        """ Three argument version of __pow__ """
        pass

    def _rescale(self, *args, **kwargs): # real signature unknown
        """
        Rescale self so that the exponent is exp, either by padding with zeros
                or by truncating digits, using the given rounding mode.
        
                Specials are returned without change.  This operation is
                quiet: it raises no flags, and uses no information from the
                context.
        
                exp = exp to scale to (an integer)
                rounding = rounding mode
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        """
        Round a nonzero, nonspecial Decimal to a fixed number of
                significant figures, using the given rounding mode.
        
                Infinities, NaNs and zeros are returned unaltered.
        
                This operation is quiet: it raises no flags, and uses no
                information from the context.
        """
        pass

    def _round_05up(self, *args, **kwargs): # real signature unknown
        """ Round down unless digit prec-1 is 0 or 5. """
        pass

    def _round_ceiling(self, *args, **kwargs): # real signature unknown
        """ Rounds up (not away from 0 if negative.) """
        pass

    def _round_down(self, *args, **kwargs): # real signature unknown
        """ Also known as round-towards-0, truncate. """
        pass

    def _round_floor(self, *args, **kwargs): # real signature unknown
        """ Rounds down (not towards 0 if negative) """
        pass

    def _round_half_down(self, *args, **kwargs): # real signature unknown
        """ Round 5 down """
        pass

    def _round_half_even(self, *args, **kwargs): # real signature unknown
        """ Round 5 to even, rest to nearest. """
        pass

    def _round_half_up(self, *args, **kwargs): # real signature unknown
        """ Rounds 5 up (away from 0) """
        pass

    def _round_up(self, *args, **kwargs): # real signature unknown
        """ Rounds away from 0. """
        pass

    def __abs__(self, round=False): # real signature unknown; restored from __doc__
        """
        Returns the absolute value of self.
        
                If the keyword argument 'round' is false, do not round.  The
                expression self.__abs__(round=False) is equivalent to
                self.copy_abs().
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """
        Returns self + other.
        
                -INF + INF (or the reverse) cause InvalidOperation errors.
        """
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return (self // other, self % other) """
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        """ Return self / other. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ Float representation. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ self // other """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Format a Decimal instance according to the given specifier.
        
                The specifier should be a standard format specifier, with the
                form described in PEP 3101.  Formatting types 'e', 'E', 'f',
                'F', 'g', 'G', 'n' and '%' are supported.  If the formatting
                type is omitted it defaults to 'g' or 'G', depending on the
                value of context.capitals.
        """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ Converts self to an int, truncating if necessary. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __long__(self, *args, **kwargs): # real signature unknown
        """
        Converts to a long.
        
                Equivalent to long(int(self))
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ self % other """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """
        Return self * other.
        
                (+-) INF * 0 (or its reverse) raise InvalidOperation.
        """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """
        Returns a copy with the sign switched.
        
                Rounds, if it has reason.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value=0, context=None): # reliably restored by inspect
        """
        Create a decimal point instance.
        
                >>> Decimal('3.14')              # string input
                Decimal('3.14')
                >>> Decimal((0, (3, 1, 4), -2))  # tuple (sign, digit_tuple, exponent)
                Decimal('3.14')
                >>> Decimal(314)                 # int or long
                Decimal('314')
                >>> Decimal(Decimal(314))        # another decimal instance
                Decimal('314')
                >>> Decimal('  3.14  \n')        # leading and trailing whitespace okay
                Decimal('3.14')
        """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        """
        Return True if self is nonzero; otherwise return False.
        
                NaNs and infinities are considered nonzero.
        """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """
        Returns a copy, unless it is a sNaN.
        
                Rounds the number (if more than precision digits)
        """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """
        Return self ** other [ % modulo].
        
                With two arguments, compute self**other.
        
                With three arguments, compute (self**other) % modulo.  For the
                three argument form, the following restrictions on the
                arguments hold:
        
                 - all three arguments must be integral
                 - other must be nonnegative
                 - either self or other (or both) must be nonzero
                 - modulo must be nonzero and must have at most p digits,
                   where p is the context precision.
        
                If any of these restrictions is violated the InvalidOperation
                flag is raised.
        
                The result of pow(self, other, modulo) is identical to the
                result that would be obtained by computing (self**other) %
                modulo with unbounded precision, but is computed more
                efficiently.  It is always exact.
        """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """
        Returns self + other.
        
                -INF + INF (or the reverse) cause InvalidOperation errors.
        """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __divmod__. """
        pass

    def __rdiv__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __truediv__. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Represents the number as an instance of Decimal. """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __floordiv__. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __mod__. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """
        Return self * other.
        
                (+-) INF * 0 (or its reverse) raise InvalidOperation.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __pow__. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return other - self """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Swaps self/other and returns __truediv__. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """
        Return string representation of the number in scientific notation.
        
                Captures all of the information in the underlying representation.
        """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self - other """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self / other. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Converts self to an int, truncating if necessary. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _exp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_special = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _pick_rounding_function = {
        'ROUND_05UP': None, # (!) real value is '<function _round_05up at 0x0000000005FC6048>'
        'ROUND_CEILING': None, # (!) real value is '<function _round_ceiling at 0x0000000005FD4F28>'
        'ROUND_DOWN': None, # (!) real value is '<function _round_down at 0x0000000005FD4CF8>'
        'ROUND_FLOOR': None, # (!) real value is '<function _round_floor at 0x0000000005FD4F98>'
        'ROUND_HALF_DOWN': None, # (!) real value is '<function _round_half_down at 0x0000000005FD4E48>'
        'ROUND_HALF_EVEN': None, # (!) real value is '<function _round_half_even at 0x0000000005FD4EB8>'
        'ROUND_HALF_UP': None, # (!) real value is '<function _round_half_up at 0x0000000005FD4DD8>'
        'ROUND_UP': None, # (!) real value is '<function _round_up at 0x0000000005FD4D68>'
    }
    __slots__ = (
        '_exp',
        '_int',
        '_sign',
        '_is_special',
    )


class FloatValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6270>'


class Number(object):
    """
    All numbers inherit from this class.
    
        If you just want to check if an argument x is a number, without
        caring what kind, use isinstance(x, Number).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x00000000030696C8>'
    _abc_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x0000000005FDFA48>'
    _abc_negative_cache_version = 29
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x0000000003069908>'
    __abstractmethods__ = frozenset([])
    __hash__ = None
    __metaclass__ = None # (!) real value is "<class 'abc.ABCMeta'>"
    __slots__ = ()


class Fraction(__numbers.Rational):
    """
    This class implements rational numbers.
    
        In the two-argument form of the constructor, Fraction(8, 6) will
        produce a rational number equivalent to 4/3. Both arguments must
        be Rational. The numerator defaults to 0 and the denominator
        defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.
    
        Fractions can also be constructed from:
    
          - numeric strings similar to those accepted by the
            float constructor (for example, '-2.3' or '1e10')
    
          - strings of the form '123/456'
    
          - float and Decimal instances
    
          - other Rational instances (including integers)
    """
    @classmethod
    def from_decimal(cls, *args, **kwargs): # real signature unknown
        """ Converts a finite Decimal instance to a rational number, exactly. """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Converts a finite float to a rational number, exactly.
        
                Beware that Fraction.from_float(0.3) != Fraction(3, 10).
        """
        pass

    def limit_denominator(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Closest Fraction to self with denominator at most max_denominator.
        
                >>> Fraction('3.141592653589793').limit_denominator(10)
                Fraction(22, 7)
                >>> Fraction('3.141592653589793').limit_denominator(100)
                Fraction(311, 99)
                >>> Fraction(4321, 8765).limit_denominator(10000)
                Fraction(4321, 8765)
        """
        pass

    def _add(self, *args, **kwargs): # real signature unknown
        """ a + b """
        pass

    def _div(self, *args, **kwargs): # real signature unknown
        """ a / b """
        pass

    def _mul(self, *args, **kwargs): # real signature unknown
        """ a * b """
        pass

    def _operator_fallbacks(self, just_rational_op, operator_op): # real signature unknown; restored from __doc__
        """
        Generates forward and reverse operators given a purely-rational
                operator and a function from the operator module.
        
                Use this like:
                __op__, __rop__ = _operator_fallbacks(just_rational_op, operator.op)
        
                In general, we want to implement the arithmetic operations so
                that mixed-mode operations either call an implementation whose
                author knew about the types of both arguments, or convert both
                to the nearest built in type and do the operation there. In
                Fraction, that means that we define __add__ and __radd__ as:
        
                    def __add__(self, other):
                        # Both types have numerators/denominator attributes,
                        # so do the operation directly
                        if isinstance(other, (int, long, Fraction)):
                            return Fraction(self.numerator * other.denominator +
                                            other.numerator * self.denominator,
                                            self.denominator * other.denominator)
                        # float and complex don't have those operations, but we
                        # know about those types, so special case them.
                        elif isinstance(other, float):
                            return float(self) + other
                        elif isinstance(other, complex):
                            return complex(self) + other
                        # Let the other type take over.
                        return NotImplemented
        
                    def __radd__(self, other):
                        # radd handles more types than add because there's
                        # nothing left to fall back to.
                        if isinstance(other, Rational):
                            return Fraction(self.numerator * other.denominator +
                                            other.numerator * self.denominator,
                                            self.denominator * other.denominator)
                        elif isinstance(other, Real):
                            return float(other) + float(self)
                        elif isinstance(other, Complex):
                            return complex(other) + complex(self)
                        return NotImplemented
        
        
                There are 5 different cases for a mixed-type addition on
                Fraction. I'll refer to all of the above code that doesn't
                refer to Fraction, float, or complex as "boilerplate". 'r'
                will be an instance of Fraction, which is a subtype of
                Rational (r : Fraction <: Rational), and b : B <:
                Complex. The first three involve 'r + b':
        
                    1. If B <: Fraction, int, float, or complex, we handle
                       that specially, and all is well.
                    2. If Fraction falls back to the boilerplate code, and it
                       were to return a value from __add__, we'd miss the
                       possibility that B defines a more intelligent __radd__,
                       so the boilerplate should return NotImplemented from
                       __add__. In particular, we don't handle Rational
                       here, even though we could get an exact answer, in case
                       the other type wants to do something special.
                    3. If B <: Fraction, Python tries B.__radd__ before
                       Fraction.__add__. This is ok, because it was
                       implemented with knowledge of Fraction, so it can
                       handle those instances before delegating to Real or
                       Complex.
        
                The next two situations describe 'b + r'. We assume that b
                didn't know about Fraction in its implementation, and that it
                uses similar boilerplate code:
        
                    4. If B <: Rational, then __radd_ converts both to the
                       builtin rational type (hey look, that's us) and
                       proceeds.
                    5. Otherwise, __radd__ tries to find the nearest common
                       base ABC, and fall back to its builtin type. Since this
                       class doesn't subclass a concrete type, there's no
                       implementation to fall back to, so we need to try as
                       hard as possible to return an actual value, or the user
                       will get a TypeError.
        """
        pass

    def _richcmp(self, *args, **kwargs): # real signature unknown
        """
        Helper for comparison operators, for internal use only.
        
                Implement comparison between a Rational instance `self`, and
                either another Rational instance or a float `other`.  If
                `other` is not a Rational instance or a float, return
                NotImplemented. `op` should be one of the six standard
                comparison operators.
        """
        pass

    def _sub(self, *args, **kwargs): # real signature unknown
        """ a - b """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(a) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ a + b """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        """ a / b """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ a == b """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ a // b """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ a >= b """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ a > b """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """
        hash(self)
        
                Tricky because values that are exactly representable as a
                float must have the same hash as that float.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ a <= b """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ a < b """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ a % b """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ a * b """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -a """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, numerator=0, denominator=None): # reliably restored by inspect
        """
        Constructs a Fraction.
        
                Takes a string like '3/2' or '1.5', another Rational instance, a
                numerator/denominator pair, or a float.
        
                Examples
                --------
        
                >>> Fraction(10, -8)
                Fraction(-5, 4)
                >>> Fraction(Fraction(1, 7), 5)
                Fraction(1, 35)
                >>> Fraction(Fraction(1, 7), Fraction(2, 3))
                Fraction(3, 14)
                >>> Fraction('314')
                Fraction(314, 1)
                >>> Fraction('-35/4')
                Fraction(-35, 4)
                >>> Fraction('3.1415') # conversion from numeric string
                Fraction(6283, 2000)
                >>> Fraction('-47e-2') # string may include a decimal exponent
                Fraction(-47, 100)
                >>> Fraction(1.47)  # direct construction from float (exact conversion)
                Fraction(6620291452234629, 4503599627370496)
                >>> Fraction(2.25)
                Fraction(9, 4)
                >>> Fraction(Decimal('1.47'))
                Fraction(147, 100)
        """
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        """ a != 0 """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +a: Coerces a subclass instance to Fraction """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """
        a ** b
        
                If b is not an integer, the result will be a float or complex
                since roots are generally irrational. If b is an integer, the
                result will be rational.
        """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ a + b """
        pass

    def __rdiv__(self, *args, **kwargs): # real signature unknown
        """ a / b """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ repr(self) """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ a // b """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ a % b """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ a * b """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ a ** b """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ a - b """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ a / b """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ str(self) """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ a - b """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ a / b """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ trunc(a) """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x00000000038FAA08>'
    _abc_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x00000000038FAA48>'
    _abc_negative_cache_version = 30
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x00000000038FA948>'
    __abstractmethods__ = frozenset([])
    __slots__ = (
        '_numerator',
        '_denominator',
    )


class IntegerFloatValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6240>'


class IntegerValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6210>'


class IntervalValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E64B0>'


class PeriodValidator(TemporalValidator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6480>'


class Seen(object):
    """
    Class for keeping track of the types of elements
        encountered when trying to perform type conversions.
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

    is_bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_float_or_complex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numeric_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6180>'


class StringValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E62A0>'


class TimeValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E6450>'


class UnicodeValidator(Validator):
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000000038E62D0>'


# variables with complex values

_TYPE_MAP = {
    'M': 'datetime64',
    'S': 'string',
    'U': 'unicode',
    'b': 'boolean',
    'bool': 'boolean',
    'c': 'complex',
    'categorical': 'categorical',
    'category': 'categorical',
    'complex128': 'complex',
    'datetime64[ns]': 'datetime64',
    'f': 'floating',
    'float16': 'floating',
    'float32': 'floating',
    'float64': 'floating',
    'i': 'integer',
    'int16': 'integer',
    'int32': 'integer',
    'int64': 'integer',
    'int8': 'integer',
    'm': 'timedelta64',
    'string': 'string',
    'timedelta64[ns]': 'timedelta64',
    'u': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'uint8': 'integer',
    'unicode': 'unicode',
}

__test__ = {
    u'infer_dtype (line 1099)': u"\n    Efficiently infer the type of a passed val, or list-like\n    array of values. Return a string describing the type.\n\n    Parameters\n    ----------\n    value : scalar, list, ndarray, or pandas type\n    skipna : bool, default False\n        Ignore NaN values when inferring the type.\n\n        .. versionadded:: 0.21.0\n\n    Returns\n    -------\n    string describing the common type of the input data.\n    Results can include:\n\n    - string\n    - unicode\n    - bytes\n    - floating\n    - integer\n    - mixed-integer\n    - mixed-integer-float\n    - decimal\n    - complex\n    - categorical\n    - boolean\n    - datetime64\n    - datetime\n    - date\n    - timedelta64\n    - timedelta\n    - time\n    - period\n    - mixed\n\n    Raises\n    ------\n    TypeError if ndarray-like but cannot infer the dtype\n\n    Notes\n    -----\n    - 'mixed' is the catchall for anything that is not otherwise\n      specialized\n    - 'mixed-integer-float' are floats and integers\n    - 'mixed-integer' are integers mixed with non-integers\n\n    Examples\n    --------\n    >>> infer_dtype(['foo', 'bar'])\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=True)\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=False)\n    'mixed'\n\n    >>> infer_dtype([b'foo', b'bar'])\n    'bytes'\n\n    >>> infer_dtype([1, 2, 3])\n    'integer'\n\n    >>> infer_dtype([1, 2, 3.5])\n    'mixed-integer-float'\n\n    >>> infer_dtype([1.0, 2.0, 3.5])\n    'floating'\n\n    >>> infer_dtype(['a', 1])\n    'mixed-integer'\n\n    >>> infer_dtype([Decimal(1), Decimal(2.0)])\n    'decimal'\n\n    >>> infer_dtype([True, False])\n    'boolean'\n\n    >>> infer_dtype([True, False, np.nan])\n    'mixed'\n\n    >>> infer_dtype([pd.Timestamp('20130101')])\n    'datetime'\n\n    >>> infer_dtype([datetime.date(2013, 1, 1)])\n    'date'\n\n    >>> infer_dtype([np.datetime64('2013-01-01')])\n    'datetime64'\n\n    >>> infer_dtype([datetime.timedelta(0, 1, 1)])\n    'timedelta'\n\n    >>> infer_dtype(pd.Series(list('aabc')).astype('category'))\n    'categorical'\n    ",
    u'is_scalar (line 108)': u'\n    Return True if given value is scalar.\n\n    Parameters\n    ----------\n    val : object\n        This includes:\n\n        - numpy array scalar (e.g. np.int64)\n        - Python builtin numerics\n        - Python builtin byte arrays and strings\n        - None\n        - datetime.datetime\n        - datetime.timedelta\n        - Period\n        - decimal.Decimal\n        - Interval\n        - DateOffset\n        - Fraction\n        - Number\n\n    Returns\n    -------\n    bool\n        Return True if given object is scalar, False otherwise\n\n    Examples\n    --------\n    >>> dt = pd.datetime.datetime(2018, 10, 3)\n    >>> pd.is_scalar(dt)\n    True\n\n    >>> pd.api.types.is_scalar([2, 3])\n    False\n\n    >>> pd.api.types.is_scalar({0: 1, 2: 3})\n    False\n\n    >>> pd.api.types.is_scalar((0, 2))\n    False\n\n    pandas supports PEP 3141 numbers:\n\n    >>> from fractions import Fraction\n    >>> pd.api.types.is_scalar(Fraction(3, 5))\n    True\n    ',
    u'item_from_zerodim (line 172)': u"\n    If the value is a zerodim array, return the item it contains.\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : object\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n\n    ",
}


# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\conversion.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # C:\Python27\lib\site-packages\pytz\__init__.pyc
from datetime import datetime_time

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string

import datetime as __datetime


# Variables with simple values

DAY_SECONDS = 86400

HOUR_SECONDS = 3600

# functions

def datetime_to_datetime64(*args, **kwargs): # real signature unknown
    """
    Convert ndarray of datetime-like objects to int64 array representing
        nanosecond timestamps.
    
        Parameters
        ----------
        values : ndarray[object]
    
        Returns
        -------
        result : ndarray[int64_t]
        inferred_tz : tzinfo or None
    """
    pass

def ensure_datetime64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype datetime64[ns]
    """
    pass

def ensure_timedelta64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype timedelta64[ns]
    """
    pass

def is_date_array_normalized(*args, **kwargs): # real signature unknown
    """
    Check if all of the given (nanosecond) timestamps are normalized to
        midnight, i.e. hour == minute == second == 0.  If the optional timezone
        `tz` is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        is_normalized : bool True if all stamps are normalized
    """
    pass

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo, "UTC", or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def normalize_date(*args, **kwargs): # real signature unknown
    """
    Normalize datetime.datetime value to midnight. Returns datetime.date as a
        datetime.datetime at midnight
    
        Parameters
        ----------
        dt : date, datetime, or Timestamp
    
        Returns
        -------
        normalized : datetime.datetime or Timestamp
    
        Raises
        ------
        TypeError : if input is not datetime.date, datetime.datetime, or Timestamp
    """
    pass

def normalize_i8_timestamps(*args, **kwargs): # real signature unknown
    """
    Normalize each of the (nanosecond) timezone aware timestamps in the given
        array by rounding down to the beginning of the day (i.e. midnight).
        This is midnight for timezone, `tz`.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        result : int64 ndarray of converted of normalized nanosecond timestamps
    """
    pass

def pydt_to_i8(*args, **kwargs): # real signature unknown
    """
    Convert to int64 representation compatible with numpy datetime64; converts
        to UTC
    
        Parameters
        ----------
        pydt : object
    
        Returns
        -------
        i8value : np.int64
    """
    pass

def tz_convert(*args, **kwargs): # real signature unknown
    """
    Convert the values (in i8) from timezone1 to timezone2
    
        Parameters
        ----------
        vals : int64 ndarray
        tz1 : string / timezone object
        tz2 : string / timezone object
    
        Returns
        -------
        int64 ndarray of converted
    """
    pass

def tz_convert_single(*args, **kwargs): # real signature unknown
    """
    Convert the val (in i8) from timezone1 to timezone2
    
        This is a single timezone version of tz_convert
    
        Parameters
        ----------
        val : int64
        tz1 : string / timezone object
        tz2 : string / timezone object
    
        Returns
        -------
        converted: int64
    """
    pass

def tz_localize_to_utc(*args, **kwargs): # real signature unknown
    """
    Localize tzinfo-naive i8 to given time zone (using pytz). If
        there are ambiguities in the values, raise AmbiguousTimeError.
    
        Parameters
        ----------
        vals : ndarray[int64_t]
        tz : tzinfo or None
        ambiguous : str, bool, or arraylike
            When clocks moved backward due to DST, ambiguous times may arise.
            For example in Central European Time (UTC+01), when going from 03:00
            DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC
            and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter
            dictates how ambiguous times should be handled.
    
            - 'infer' will attempt to infer fall dst-transition hours based on
              order
            - bool-ndarray where True signifies a DST time, False signifies a
              non-DST time (note that this flag is only applicable for ambiguous
              times, but the array must have the same length as vals)
            - bool if True, treat all vals as DST. If False, treat them as non-DST
            - 'NaT' will return NaT where there are ambiguous times
    
        nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise",
                       timedelta-like}
            How to handle non-existent times when converting wall times to UTC
    
            .. versionadded:: 0.24.0
    
        Returns
        -------
        localized : ndarray[int64_t]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class tzutc(__datetime.tzinfo):
    """
    This is a tzinfo object that represents the UTC time zone.
    
        **Examples:**
    
        .. doctest::
    
            >>> from datetime import *
            >>> from dateutil.tz import *
    
            >>> datetime.now()
            datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)
    
            >>> datetime.now(tzutc())
            datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())
    
            >>> datetime.now(tzutc()).tzname()
            'UTC'
    
        .. versionchanged:: 2.7.0
            ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will
            always return the same object.
    
            .. doctest::
    
                >>> from dateutil.tz import tzutc, UTC
                >>> tzutc() is tzutc()
                True
                >>> tzutc() is UTC
                True
    """
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def fromutc(self): # real signature unknown; restored from __doc__
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, *args, **kwargs): # real signature unknown
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _TzSingleton__instance = tzutc()
    __dict__ = None # (!) real value is 'dict_proxy({\'__ne__\': <function __ne__ at 0x00000000037AD438>, \'__module__\': \'dateutil.tz.tz\', \'_TzSingleton__instance\': tzutc(), \'fromutc\': <function fromutc at 0x00000000037AD358>, \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'dst\': <function dst at 0x00000000037AD128>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'is_ambiguous\': <function is_ambiguous at 0x00000000037AD278>, \'utcoffset\': <function utcoffset at 0x00000000037AD0B8>, \'tzname\': <function tzname at 0x00000000037AD208>, \'__hash__\': None, \'__eq__\': <function __eq__ at 0x00000000037AD3C8>, \'__doc__\': "\\n    This is a tzinfo object that represents the UTC time zone.\\n\\n    **Examples:**\\n\\n    .. doctest::\\n\\n        >>> from datetime import *\\n        >>> from dateutil.tz import *\\n\\n        >>> datetime.now()\\n        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n        >>> datetime.now(tzutc())\\n        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n        >>> datetime.now(tzutc()).tzname()\\n        \'UTC\'\\n\\n    .. versionchanged:: 2.7.0\\n        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n        always return the same object.\\n\\n        .. doctest::\\n\\n            >>> from dateutil.tz import tzutc, UTC\\n            >>> tzutc() is tzutc()\\n            True\\n            >>> tzutc() is UTC\\n            True\\n    ", \'__repr__\': <function __repr__ at 0x00000000037AD4A8>})'
    __hash__ = None


class _TSObject(object):
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

nat_strings = None # (!) real value is "set(['nat', 'NaT', 'NAN', 'nan', 'NaN', 'NAT'])"

NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

UTC = pytz.UTC

__pyx_capi__ = {
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyObject *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x00000000037D03C0>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x00000000037D0390>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *)" at 0x00000000037D0420>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyObject *, int __pyx_skip_dispatch)" at 0x00000000037D04E0>'
    'maybe_datetimelike_to_i8': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x00000000037D0480>'
    'pydt_to_i8': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, int __pyx_skip_dispatch)" at 0x00000000037D0450>'
    'tz_convert_single': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000000037D03F0>'
    'tz_convert_utc_to_tzlocal': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *)" at 0x00000000037D04B0>'
}

__test__ = {}


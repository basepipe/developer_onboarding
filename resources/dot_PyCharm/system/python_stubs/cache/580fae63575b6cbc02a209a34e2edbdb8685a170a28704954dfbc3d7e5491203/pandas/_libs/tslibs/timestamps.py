# encoding: utf-8
# module pandas._libs.tslibs.timestamps
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\timestamps.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import warnings as warnings # C:\Python27\lib\warnings.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
from datetime import datetime_time, timedelta

from pandas._libs.tslibs.conversion import (normalize_i8_timestamps, 
    tz_localize_to_utc)

from pandas._libs.tslibs.fields import (get_date_name_field, 
    get_start_end_field)

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.timedeltas import Timedelta

import datetime as __datetime


# Variables with simple values

DAY_SECONDS = 86400

# functions

def maybe_integer_op_deprecated(*args, **kwargs): # real signature unknown
    pass

def npdivmod(*args, **kwargs): # real signature unknown
    """
    divmod(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return element-wise quotient and remainder simultaneously.
    
    .. versionadded:: 1.13.0
    
    ``np.divmod(x, y)`` is equivalent to ``(x // y, x % y)``, but faster
    because it avoids redundant work. It is used to implement the Python
    built-in function ``divmod`` on NumPy arrays.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or `None`,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        Values of True indicate to calculate the ufunc at that position, values
        of False indicate to leave the value in the output alone.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.
    
    Returns
    -------
    out1 : ndarray
        Element-wise quotient resulting from floor division.
        This is a scalar if both `x1` and `x2` are scalars.
    out2 : ndarray
        Element-wise remainder from floor division.
        This is a scalar if both `x1` and `x2` are scalars.
    
    See Also
    --------
    floor_divide : Equivalent to Python's ``//`` operator.
    remainder : Equivalent to Python's ``%`` operator.
    modf : Equivalent to ``divmod(x, 1)`` for positive ``x`` with the return
           values switched.
    
    Examples
    --------
    >>> np.divmod(np.arange(5), 3)
    (array([0, 0, 0, 1, 1]), array([0, 1, 2, 0, 1]))
    """
    pass

def round_nsint64(*args, **kwargs): # real signature unknown
    """
    Applies rounding mode at given frequency
    
        Parameters
        ----------
        values : :obj:`ndarray`
        mode : instance of `RoundTo` enumeration
        freq : str, obj
    
        Returns
        -------
        :obj:`ndarray`
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class RoundTo(object):
    """
    enumeration defining the available rounding modes
    
        Attributes
        ----------
        MINUS_INFTY
            round towards -∞, or floor [2]_
        PLUS_INFTY
            round towards +∞, or ceil [3]_
        NEAREST_HALF_EVEN
            round to nearest, tie-break half to even [6]_
        NEAREST_HALF_MINUS_INFTY
            round to nearest, tie-break half to -∞ [5]_
        NEAREST_HALF_PLUS_INFTY
            round to nearest, tie-break half to +∞ [4]_
    
    
        References
        ----------
        .. [1] "Rounding - Wikipedia"
               https://en.wikipedia.org/wiki/Rounding
        .. [2] "Rounding down"
               https://en.wikipedia.org/wiki/Rounding#Rounding_down
        .. [3] "Rounding up"
               https://en.wikipedia.org/wiki/Rounding#Rounding_up
        .. [4] "Round half up"
               https://en.wikipedia.org/wiki/Rounding#Round_half_up
        .. [5] "Round half down"
               https://en.wikipedia.org/wiki/Rounding#Round_half_down
        .. [6] "Round half to even"
               https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_EVEN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'dict_proxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'MINUS_INFTY\': <property object at 0x0000000003537AE8>, \'NEAREST_HALF_EVEN\': <property object at 0x0000000003537B88>, \'NEAREST_HALF_MINUS_INFTY\': <property object at 0x0000000003537C28>, \'PLUS_INFTY\': <property object at 0x0000000003537B38>, \'__qualname__\': \'RoundTo\', \'NEAREST_HALF_PLUS_INFTY\': <property object at 0x0000000003537BD8>, \'__dict__\': <attribute \'__dict__\' of \'RoundTo\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'RoundTo\' objects>, \'__doc__\': \'\\n    enumeration defining the available rounding modes\\n\\n    Attributes\\n    ----------\\n    MINUS_INFTY\\n        round towards -\\xe2\\x88\\x9e, or floor [2]_\\n    PLUS_INFTY\\n        round towards +\\xe2\\x88\\x9e, or ceil [3]_\\n    NEAREST_HALF_EVEN\\n        round to nearest, tie-break half to even [6]_\\n    NEAREST_HALF_MINUS_INFTY\\n        round to nearest, tie-break half to -\\xe2\\x88\\x9e [5]_\\n    NEAREST_HALF_PLUS_INFTY\\n        round to nearest, tie-break half to +\\xe2\\x88\\x9e [4]_\\n\\n\\n    References\\n    ----------\\n    .. [1] "Rounding - Wikipedia"\\n           https://en.wikipedia.org/wiki/Rounding\\n    .. [2] "Rounding down"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\\n    .. [3] "Rounding up"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\\n    .. [4] "Round half up"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\\n    .. [5] "Round half down"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\\n    .. [6] "Round half to even"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\\n    \'})'
    __qualname__ = 'RoundTo'


class _Timestamp(__datetime.datetime):
    # no doc
    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.datetime64 object with 'ns' precision """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        """
        pass

    def _get_date_name_field(self, *args, **kwargs): # real signature unknown
        pass

    def _get_start_end_field(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
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

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return resolution describing the smallest difference between two
        times that can be represented by Timestamp object_state
        """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _short_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000000005D03E10>'


class Timestamp(_Timestamp):
    """
    Pandas replacement for datetime.datetime
    
        Timestamp is the pandas equivalent of python's Datetime
        and is interchangeable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp
        freq : str, DateOffset
            Offset which Timestamp will have
        tz : str, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : str
            Unit used for conversion if ts_input is of type int or float. The
            valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For
            example, 's' means seconds and 'ms' means milliseconds.
        year, month, day : int
            .. versionadded:: 0.19.0
        hour, minute, second, microsecond : int, optional, default 0
            .. versionadded:: 0.19.0
        nanosecond : int, optional, default 0
            .. versionadded:: 0.23.0
        tzinfo : datetime.tzinfo, optional, default None
            .. versionadded:: 0.19.0
    
        Notes
        -----
        There are essentially three calling conventions for the constructor. The
        primary form accepts four parameters. They can be passed by position or
        keyword.
    
        The other two forms mimic the parameters from ``datetime.datetime``. They
        can be passed by either position or keyword, but not both mixed together.
    
        Examples
        --------
        Using the primary calling convention:
    
        This converts a datetime-like string
        >>> pd.Timestamp('2017-01-01T12')
        Timestamp('2017-01-01 12:00:00')
    
        This converts a float representing a Unix epoch in units of seconds
        >>> pd.Timestamp(1513393355.5, unit='s')
        Timestamp('2017-12-16 03:02:35.500000')
    
        This converts an int representing a Unix-epoch in units of seconds
        and for a particular timezone
        >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
        Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
    
        Using the other two forms that mimic the API for ``datetime.datetime``:
    
        >>> pd.Timestamp(2017, 1, 1, 12)
        Timestamp('2017-01-01 12:00:00')
    
        >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)
        Timestamp('2017-01-01 12:00:00')
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def ceil(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp ceiled to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the ceiling resolution
                ambiguous : bool, 'NaT', default 'raise'
                    - bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                    .. versionadded:: 0.24.0
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,
                              default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    - 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time
                    - 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time
                    - 'NaT' will return NaT where there are nonexistent times
                    - timedelta objects will shift nonexistent times by the timedelta
                    - 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times
        
                    .. versionadded:: 0.24.0
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    @classmethod
    def combine(cls, date, time): # real signature unknown; restored from __doc__
        """
        Timsetamp.combine(date, time)
        
                date, time -> datetime with same date and time fields
        """
        pass

    def day_name(self, *args, **kwargs): # real signature unknown
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    locale determining the language in which to return the day name
        
                Returns
                -------
                day_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp floored to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the flooring resolution
                ambiguous : bool, 'NaT', default 'raise'
                    - bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                    .. versionadded:: 0.24.0
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,
                              default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    - 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time
                    - 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time
                    - 'NaT' will return NaT where there are nonexistent times
                    - timedelta objects will shift nonexistent times by the timedelta
                    - 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times
        
                    .. versionadded:: 0.24.0
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    @classmethod
    def fromordinal(cls, ordinal, freq=None, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.fromordinal(ordinal, freq=None, tz=None)
        
                passed an ordinal, translate and convert to a ts
                note: by definition there cannot be any tz info on the ordinal itself
        
                Parameters
                ----------
                ordinal : int
                    date corresponding to a proleptic Gregorian ordinal
                freq : str, DateOffset
                    Offset which Timestamp will have
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will have.
        """
        pass

    @classmethod
    def fromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                timestamp[, tz] -> tz's local time from POSIX timestamp.
        """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def month_name(self, *args, **kwargs): # real signature unknown
        """
        Return the month name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    locale determining the language in which to return the month name
        
                Returns
                -------
                month_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize Timestamp to midnight, preserving
                tz information.
        """
        pass

    @classmethod
    def now(cls, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.now(tz=None)
        
                Returns new Timestamp object representing current time local to
                tz.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        implements datetime.replace, handles nanoseconds
        
                Parameters
                ----------
                year : int, optional
                month : int, optional
                day : int, optional
                hour : int, optional
                minute : int, optional
                second : int, optional
                microsecond : int, optional
                nanosecond : int, optional
                tzinfo : tz-convertible, optional
                fold : int, optional, default is 0
                    added in 3.6, NotImplemented
        
                Returns
                -------
                Timestamp with fields replaced
        """
        pass

    def round(self, *args, **kwargs): # real signature unknown
        """
        Round the Timestamp to the specified resolution
        
                Parameters
                ----------
                freq : a freq string indicating the rounding resolution
                ambiguous : bool, 'NaT', default 'raise'
                    - bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                    .. versionadded:: 0.24.0
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,
                              default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    - 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time
                    - 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time
                    - 'NaT' will return NaT where there are nonexistent times
                    - timedelta objects will shift nonexistent times by the timedelta
                    - 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times
        
                    .. versionadded:: 0.24.0
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    @classmethod
    def today(cls, cls_1, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.today(cls, tz=None)
        
                Return the current time in the local timezone.  This differs
                from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to
        """
        pass

    def to_julian_date(self, *args, **kwargs): # real signature unknown
        """
        Convert TimeStamp to a Julian Date.
                0 Julian date is noon January 1, 4713 BC.
        """
        pass

    def to_period(self, *args, **kwargs): # real signature unknown
        """ Return an period of which this timestamp is an observation. """
        pass

    def tz_convert(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def tz_localize(self, *args, **kwargs): # real signature unknown
        """
        Convert naive Timestamp to local time zone, or remove
                timezone from tz-aware Timestamp.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    When clocks moved backward due to DST, ambiguous times may arise.
                    For example in Central European Time (UTC+01), when going from
                    03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
                    00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
                    `ambiguous` parameter dictates how ambiguous times should be
                    handled.
        
                    - bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,
                              default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    - 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time
                    - 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time
                    - 'NaT' will return NaT where there are nonexistent times
                    - timedelta objects will shift nonexistent times by the timedelta
                    - 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times
        
                    .. versionadded:: 0.24.0
        
                errors : 'raise', 'coerce', default None
                    - 'raise' will raise a NonExistentTimeError if a timestamp is not
                       valid in the specified timezone (e.g. due to a transition from
                       or to DST time). Use ``nonexistent='raise'`` instead.
                    - 'coerce' will return NaT if the timestamp can not be converted
                      into the specified timezone. Use ``nonexistent='NaT'`` instead.
        
                      .. deprecated:: 0.24.0
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        """
        pass

    @classmethod
    def utcnow(cls): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        """
        pass

    def _has_time_component(self, *args, **kwargs): # real signature unknown
        """
        Returns if the Timestamp has a time component
                in addition to the date part
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        .. deprecated:: 0.23.0
            Use ``Timestamp.day_name()`` instead
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = Timestamp('2262-04-11 23:47:16.854775807')
    min = Timestamp('1677-09-21 00:12:43.145225')
    __dict__ = None # (!) real value is 'dict_proxy({\'dayofweek\': <property object at 0x0000000003537CC8>, \'__module__\': \'pandas._libs.tslibs.timestamps\', \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x000000000353AF48>, \'is_year_start\': <property object at 0x000000000353C138>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'weekday_name\': <property object at 0x0000000003537DB8>, \'__reduce__\': <cyfunction Timestamp.__reduce__ at 0x000000000353A1C8>, \'replace\': <cyfunction Timestamp.replace at 0x000000000353D108>, \'to_period\': <cyfunction Timestamp.to_period at 0x000000000353A288>, \'utcnow\': <classmethod object at 0x000000000353B708>, \'is_month_end\': <property object at 0x000000000353C048>, \'freqstr\': <property object at 0x0000000003537F48>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'normalize\': <cyfunction Timestamp.normalize at 0x000000000353D408>, \'tz\': <property object at 0x0000000003537D68>, \'__new__\': <cyfunction Timestamp.__new__ at 0x0000000005CFAB88>, \'floor\': <cyfunction Timestamp.floor at 0x0000000005CFADC8>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x000000000353D048>, \'is_quarter_start\': <property object at 0x000000000353C098>, \'utcfromtimestamp\': <classmethod object at 0x000000000353B738>, \'month_name\': <cyfunction Timestamp.month_name at 0x000000000353A4C8>, \'dayofyear\': <property object at 0x0000000003537E08>, \'combine\': <classmethod object at 0x000000000353B798>, \'day_name\': <cyfunction Timestamp.day_name at 0x000000000353A408>, \'__doc__\': "Pandas replacement for datetime.datetime\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp\\n    freq : str, DateOffset\\n        Offset which Timestamp will have\\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n    year, month, day : int\\n        .. versionadded:: 0.19.0\\n    hour, minute, second, microsecond : int, optional, default 0\\n        .. versionadded:: 0.19.0\\n    nanosecond : int, optional, default 0\\n        .. versionadded:: 0.23.0\\n    tzinfo : datetime.tzinfo, optional, default None\\n        .. versionadded:: 0.19.0\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'today\': <classmethod object at 0x000000000353B6D8>, \'week\': <property object at 0x0000000003537E58>, \'_has_time_component\': <cyfunction Timestamp._has_time_component at 0x000000000353D288>, \'weekofyear\': <property object at 0x0000000003537E58>, \'__setstate__\': <cyfunction Timestamp.__setstate__ at 0x000000000353A108>, \'max\': Timestamp(\'2262-04-11 23:47:16.854775807\'), \'ceil\': <cyfunction Timestamp.ceil at 0x0000000005CFAE88>, \'daysinmonth\': <property object at 0x0000000003537EF8>, \'now\': <classmethod object at 0x000000000353B6A8>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x000000000353D048>, \'quarter\': <property object at 0x0000000003537EA8>, \'__radd__\': <cyfunction Timestamp.__radd__ at 0x000000000353D4C8>, \'is_year_end\': <property object at 0x000000000353C188>, \'_round\': <cyfunction Timestamp._round at 0x0000000005CFAC48>, \'fromordinal\': <classmethod object at 0x000000000353B678>, \'fromtimestamp\': <classmethod object at 0x000000000353B768>, \'__qualname__\': \'Timestamp\', \'is_quarter_end\': <property object at 0x000000000353C0E8>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x000000000353D348>, \'days_in_month\': <property object at 0x0000000003537EF8>, \'isoformat\': <cyfunction Timestamp.isoformat at 0x000000000353D1C8>, \'min\': Timestamp(\'1677-09-21 00:12:43.145225\'), \'is_month_start\': <property object at 0x0000000003537F98>, \'is_leap_year\': <property object at 0x000000000353C1D8>, \'round\': <cyfunction Timestamp.round at 0x0000000005CFAD08>})'
    __qualname__ = 'Timestamp'


# variables with complex values

UTC = None # (!) real value is '<UTC>'

_no_input = None # (!) real value is '<object object at 0x0000000002414EF0>'

_zero_time = None # (!) real value is 'datetime.time(0, 0)'

__pyx_capi__ = {
    'create_timestamp_from_ts': None, # (!) real value is '<capsule object "PyObject *(__pyx_t_5numpy_int64_t, npy_datetimestruct, PyObject *, PyObject *)" at 0x0000000005D03DB0>'
}

__test__ = {}


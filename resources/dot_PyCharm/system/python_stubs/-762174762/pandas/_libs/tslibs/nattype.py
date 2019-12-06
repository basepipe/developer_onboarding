# encoding: utf-8
# module pandas._libs.tslibs.nattype
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\nattype.pyd
# by generator 1.147
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import datetime as __datetime


# Variables with simple values

iNaT = -9223372036854775808L

# functions

def is_null_datetimelike(*args, **kwargs): # real signature unknown
    """
    Determine if we have a null for a timedelta/datetime (or integer versions)
    
        Parameters
        ----------
        val : object
        inat_is_null : bool, default True
            Whether to treat integer iNaT value as null
    
        Returns
        -------
        null_datetimelike : bool
    """
    pass

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def __nat_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__NaT(*args, **kwargs): # real signature unknown
    pass

# classes

class _NaT(__datetime.datetime):
    # no doc
    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total duration of timedelta in seconds (to ns precision) """
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.datetime64 object with 'ns' precision """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
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

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
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

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NaTType(_NaT):
    """ (N)ot-(A)-(T)ime, the time equivalent of NaN """
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

    def combine(self, date, time): # real signature unknown; restored from __doc__
        """
        Timsetamp.combine(date, time)
        
                date, time -> datetime with same date and time fields
        """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
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

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
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

    def fromordinal(self, ordinal, freq=None, tz=None): # real signature unknown; restored from __doc__
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

    def fromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                timestamp[, tz] -> tz's local time from POSIX timestamp.
        """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
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

    def now(self, tz=None): # real signature unknown; restored from __doc__
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

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def strptime(self): # real signature unknown; restored from __doc__
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def today(self, cls, tz=None): # real signature unknown; restored from __doc__
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

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
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

    def utcfromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        """
        pass

    def utcnow(self): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __rdiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "dict_proxy({'__dict__': <attribute '__dict__' of 'NaTType' objects>, 'strptime': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91708>, 'nanoseconds': <property object at 0x0000000005E8CD18>, 'month': <property object at 0x0000000005E8C778>, 'utcnow': <cyfunction _make_error_func.<locals>.f at 0x0000000003714048>, 'to_pydatetime': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714348>, '__rdiv__': <cyfunction NaTType.__rdiv__ at 0x0000000005D09D08>, '__rmul__': <cyfunction NaTType.__rmul__ at 0x0000000005D09F48>, '__weakref__': <attribute '__weakref__' of 'NaTType' objects>, 'millisecond': <property object at 0x0000000005E8C908>, 'now': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714408>, 'weekday_name': <property object at 0x0000000005E8CBD8>, 'utcfromtimestamp': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91DC8>, 'month_name': <cyfunction _make_nan_func.<locals>.f at 0x0000000005E91288>, 'dayofyear': <property object at 0x0000000005E8CA48>, '__rfloordiv__': <cyfunction NaTType.__rfloordiv__ at 0x0000000005D09E88>, 'combine': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91F48>, '__doc__': '(N)ot-(A)-(T)ime, the time equivalent of NaN', 'today': <cyfunction _make_nat_func.<locals>.f at 0x00000000037144C8>, 'weekofyear': <property object at 0x0000000005E8CA98>, 'timestamp': <cyfunction _make_error_func.<locals>.f at 0x0000000003714108>, 'isoweekday': <cyfunction _make_nan_func.<locals>.f at 0x0000000005E911C8>, 'ceil': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714708>, 'utcoffset': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91D08>, 'replace': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714948>, 'tz_convert': <cyfunction _make_nat_func.<locals>.f at 0x00000000037147C8>, 'day': <property object at 0x0000000005E8C7C8>, 'minute': <property object at 0x0000000005E8C868>, 'ctime': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91A08>, 'hour': <property object at 0x0000000005E8C818>, 'day_name': <cyfunction _make_nan_func.<locals>.f at 0x0000000005E91348>, '__qualname__': 'NaTType', 'tzname': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91C48>, 'timetz': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91588>, 'round': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714588>, 'dayofweek': <property object at 0x0000000005E8CB88>, '__module__': 'pandas._libs.tslibs.nattype', '__rtruediv__': <cyfunction NaTType.__rtruediv__ at 0x0000000005D09DC8>, '__reduce__': <cyfunction NaTType.__reduce__ at 0x0000000005D09C48>, 'days': <property object at 0x0000000005E8CC28>, 'utctimetuple': <cyfunction _make_error_func.<locals>.f at 0x0000000005E914C8>, 'second': <property object at 0x0000000005E8C8B8>, 'toordinal': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91B88>, 'year': <property object at 0x0000000005E8C6D8>, 'isocalendar': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91888>, '__reduce_ex__': <cyfunction NaTType.__reduce_ex__ at 0x0000000005D09B88>, '__new__': <cyfunction NaTType.__new__ at 0x0000000005D09AC8>, 'floor': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714648>, 'dst': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91948>, 'astimezone': <cyfunction _make_error_func.<locals>.f at 0x00000000037141C8>, 'nanosecond': <property object at 0x0000000005E8C9A8>, 'timetuple': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91648>, 'week': <property object at 0x0000000005E8C9F8>, 'seconds': <property object at 0x0000000005E8CC78>, 'microseconds': <property object at 0x0000000005E8CCC8>, 'microsecond': <property object at 0x0000000005E8C958>, 'date': <cyfunction _make_nat_func.<locals>.f at 0x0000000005E91408>, 'daysinmonth': <property object at 0x0000000005E8CB38>, 'quarter': <property object at 0x0000000005E8C728>, 'qyear': <property object at 0x0000000005E8CD68>, 'tz_localize': <cyfunction _make_nat_func.<locals>.f at 0x0000000003714888>, 'fromordinal': <cyfunction _make_error_func.<locals>.f at 0x0000000003714288>, 'fromtimestamp': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91E88>, 'days_in_month': <property object at 0x0000000005E8CAE8>, 'weekday': <cyfunction _make_nan_func.<locals>.f at 0x0000000005E91108>, 'time': <cyfunction _make_error_func.<locals>.f at 0x0000000005E91AC8>, 'strftime': <cyfunction _make_error_func.<locals>.f at 0x0000000005E917C8>})"
    __qualname__ = 'NaTType'


# variables with complex values

NaT = None # (!) real value is 'NaT'

nat_strings = None # (!) real value is "set(['nat', 'NaT', 'NAN', 'nan', 'NaN', 'NAT'])"

__pyx_capi__ = {
    'NPY_NAT': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t" at 0x0000000005E88C00>'
    '_nat_scalar_rules': None, # (!) real value is '<capsule object "int [6]" at 0x0000000005E88C30>'
    'c_NaT': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_7nattype__NaT *" at 0x0000000005E88C60>'
    'checknull_with_nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000000005E88C90>'
    'is_null_datetimelike': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_7nattype_is_null_datetimelike *__pyx_optional_args)" at 0x0000000005E88CC0>'
}

__test__ = {}


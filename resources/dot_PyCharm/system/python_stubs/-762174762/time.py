# encoding: utf-8
# module time
# from (built-in)
# by generator 1.147
"""
This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (four digits, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.

Variables:

timezone -- difference in seconds between UTC and local standard time
altzone -- difference in  seconds between UTC and local DST time
daylight -- whether local time should reflect DST
tzname -- tuple of (standard time zone name, DST time zone name)

Functions:

time() -- return current time in seconds since the Epoch as a float
clock() -- return CPU time since process start as a float
sleep() -- delay for a number of seconds given as a float
gmtime() -- convert seconds since Epoch to UTC tuple
localtime() -- convert seconds since Epoch to local time tuple
asctime() -- convert time tuple to string
ctime() -- convert time in seconds to string
mktime() -- convert local time tuple to seconds since Epoch
strftime() -- convert time tuple to string according to format specification
strptime() -- parse string to time tuple according to format specification
tzset() -- change the local timezone
"""
# no imports

# Variables with simple values

accept2dyear = 1

altzone = -14400

daylight = 0

timezone = -10800

# functions

def asctime(p_tuple=None): # real signature unknown; restored from __doc__
    """
    asctime([tuple]) -> string
    
    Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
    When the time tuple is not present, current time as returned by localtime()
    is used.
    """
    return ""

def clock(): # real signature unknown; restored from __doc__
    """
    clock() -> floating point number
    
    Return the CPU time or real time since the start of the process or since
    the first call to clock().  This has as much precision as the system
    records.
    """
    return 0.0

def ctime(seconds=None): # known case of time.ctime
    """
    ctime(seconds) -> string
    
    Convert a time in seconds since the Epoch to a string in local time.
    This is equivalent to asctime(localtime(seconds)). When the time tuple is
    not present, current time as returned by localtime() is used.
    """
    return ""

def gmtime(seconds=None): # real signature unknown; restored from __doc__
    """
    gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                           tm_sec, tm_wday, tm_yday, tm_isdst)
    
    Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
    GMT).  When 'seconds' is not passed in, convert the current time instead.
    """
    pass

def localtime(seconds=None): # real signature unknown; restored from __doc__
    """
    localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)
    
    Convert seconds since the Epoch to a time tuple expressing local time.
    When 'seconds' is not passed in, convert the current time instead.
    """
    pass

def mktime(p_tuple): # real signature unknown; restored from __doc__
    """
    mktime(tuple) -> floating point number
    
    Convert a time tuple in local time to seconds since the Epoch.
    """
    return 0.0

def sleep(seconds): # real signature unknown; restored from __doc__
    """
    sleep(seconds)
    
    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
    """
    pass

def strftime(format, p_tuple=None): # real signature unknown; restored from __doc__
    """
    strftime(format[, tuple]) -> string
    
    Convert a time tuple to a string according to a format specification.
    See the library reference manual for formatting codes. When the time tuple
    is not present, current time as returned by localtime() is used.
    """
    return ""

def strptime(string, format): # real signature unknown; restored from __doc__
    """
    strptime(string, format) -> struct_time
    
    Parse a string to a time tuple according to a format specification.
    See the library reference manual for formatting codes (same as strftime()).
    """
    return struct_time

def time(): # real signature unknown; restored from __doc__
    """
    time() -> floating point number
    
    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.
    """
    return 0.0

# classes

class struct_time(object):
    """
    The time value as returned by gmtime(), localtime(), and strptime(), and
     accepted by asctime(), mktime() and strftime().  May be considered as a
     sequence of 9 integers.
    
     Note that several fields' values are not the same as those defined by
     the C language standard for struct tm.  For example, the value of the
     field tm_year is the actual year, not year - 1900.  See individual
     fields' descriptions for details.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
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

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    tm_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hours, range [0, 23]"""

    tm_isdst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """1 if summer time is in effect, 0 if not, and -1 if unknown"""

    tm_mday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of month, range [1, 31]"""

    tm_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """minutes, range [0, 59]"""

    tm_mon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """month of year, range [1, 12]"""

    tm_sec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """seconds, range [0, 61])"""

    tm_wday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of week, range [0, 6], Monday is 0"""

    tm_yday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of year, range [1, 366]"""

    tm_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """year, for example, 1993"""


    n_fields = 9
    n_sequence_fields = 9
    n_unnamed_fields = 0


# variables with complex values

tzname = (
    'Russia TZ 2 Standard Time',
    'Russia TZ 2 Daylight Time',
)


# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\offsets.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import time as time # <module 'time' (built-in)>

# Variables with simple values

key = 'BAS-DEC'

PY2 = True

_alias = 'Q-DEC'

_d = 'SUN'

_m = 'DEC'

__prefix = 'Q'

# functions

def apply_index_wraps(*args, **kwargs): # real signature unknown
    pass

def as_datetime(*args, **kwargs): # real signature unknown
    pass

def get_day_of_month(other, start): # real signature unknown; restored from __doc__
    """
    Find the day in `other`'s month that satisfies a DateOffset's onOffset
        policy, as described by the `day_opt` argument.
    
        Parameters
        ----------
        other : datetime or Timestamp
        day_opt : 'start', 'end', 'business_start', 'business_end', or int
            'start': returns 1
            'end': returns last day of the month
            'business_start': returns the first business day of the month
            'business_end': returns the last business day of the month
            int: returns the day in the month indicated by `other`, or the last of
                day the month if the value exceeds in that month's number of days.
    
        Returns
        -------
        day_of_month : int
    
        Examples
        -------
        >>> other = datetime(2017, 11, 14)
        >>> get_day_of_month(other, 'start')
        1
        >>> get_day_of_month(other, 'end')
        30
    """
    pass

def get_firstbday(*args, **kwargs): # real signature unknown
    """
    Find the first day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        first_bday : int
    """
    pass

def get_lastbday(*args, **kwargs): # real signature unknown
    """
    Find the last day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        last_bday : int
    """
    pass

def roll_convention(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : int, generally the day component of a datetime
        n : number of periods to increment, before adjusting for rolling
        compare : int, generally the day component of a datetime, in the same
                  month as the datetime form which `other` was taken.
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_qtrday(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : int reference month giving the first month of the year
        day_opt : 'start', 'end', 'business_start', 'business_end', or int
            The convention to use in finding the day in a given month against
            which to compare for rollforward/rollbackward decisions.
        modby : int 3 for quarters, 12 for years
    
        Returns
        -------
        n : int number of periods to increment
    
        See Also
        --------
        get_day_of_month : Find the day in a month provided an offset.
    """
    pass

def roll_yearday(other, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : reference month giving the first month of the year
        day_opt : 'start', 'end', 'business_start', 'business_end', or int
            The day of the month to compare against that of `other` when
            incrementing or decrementing the number of periods:
    
            'start': 1
            'end': last day of the month
            'business_start': first business day of the month
            'business_end': last business day of the month
            int: day in the month indicated by `other`, or the last of day
                the month if the value exceeds in that month's number of days.
    
        Returns
        -------
        n : int number of periods to increment
    
        Notes
        -----
        * Mirrors `roll_check` in shift_months
    
        Examples
        -------
        >>> month = 3
        >>> day_opt = 'start'              # `other` will be compared to March 1
        >>> other = datetime(2017, 2, 10)  # before March 1
        >>> roll_yearday(other, 2, month, day_opt)
        1
        >>> roll_yearday(other, -7, month, day_opt)
        -7
        >>>
        >>> other = Timestamp('2014-03-15', tz='US/Eastern')  # after March 1
        >>> roll_yearday(other, 2, month, day_opt)
        2
        >>> roll_yearday(other, -7, month, day_opt)
        -6
    
        >>> month = 6
        >>> day_opt = 'end'                # `other` will be compared to June 30
        >>> other = datetime(1999, 6, 29)  # before June 30
        >>> roll_yearday(other, 5, month, day_opt)
        4
        >>> roll_yearday(other, -7, month, day_opt)
        -7
        >>>
        >>> other = Timestamp(2072, 8, 24, 6, 17, 18)  # after June 30
        >>> roll_yearday(other, 5, month, day_opt)
        5
        >>> roll_yearday(other, -7, month, day_opt)
        -6
    """
    pass

def shift_day(*args, **kwargs): # real signature unknown
    """
    Increment the datetime `other` by the given number of days, retaining
        the time-portion of the datetime.  For tz-naive datetimes this is
        equivalent to adding a timedelta.  For tz-aware datetimes it is similar to
        dateutil's relativedelta.__add__, but handles pytz tzinfo objects.
    
        Parameters
        ----------
        other : datetime or Timestamp
        days : int
    
        Returns
        -------
        shifted: datetime or Timestamp
    """
    pass

def shift_month(*args, **kwargs): # real signature unknown
    """
    Given a datetime (or Timestamp) `stamp`, an integer `months` and an
        option `day_opt`, return a new datetimelike that many months later,
        with day determined by `day_opt` using relativedelta semantics.
    
        Scalar analogue of shift_months
    
        Parameters
        ----------
        stamp : datetime or Timestamp
        months : int
        day_opt : None, 'start', 'end', 'business_start', 'business_end', or int
            None: returned datetimelike has the same day as the input, or the
                  last day of the month if the new month is too short
            'start': returned datetimelike has day=1
            'end': returned datetimelike has day on the last day of the month
            'business_start': returned datetimelike has day on the first
                business day of the month
            'business_end': returned datetimelike has day on the last
                business day of the month
            int: returned datetimelike has day equal to day_opt
    
        Returns
        -------
        shifted : datetime or Timestamp (same as input `stamp`)
    """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day: {None, 'start', 'end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def shift_quarters(*args, **kwargs): # real signature unknown
    """
    Given an int64 array representing nanosecond timestamps, shift all elements
        by the specified number of quarters using DateOffset semantics.
    
        Parameters
        ----------
        dtindex : int64_t[:] timestamps for input dates
        quarters : int number of quarters to shift
        q1start_month : int month in which Q1 begins by convention
        day : {'start', 'end', 'business_start', 'business_end'}
        modby : int (3 for quarters, 12 for years)
    
        Returns
        -------
        out : ndarray[int64_t]
    """
    pass

def _determine_offset(*args, **kwargs): # real signature unknown
    pass

def _get_calendar(*args, **kwargs): # real signature unknown
    """ Generate busdaycalendar """
    pass

def _is_normalized(*args, **kwargs): # real signature unknown
    pass

def _to_dt64(*args, **kwargs): # real signature unknown
    pass

def _validate_business_time(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class ApplyTypeError(TypeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'ApplyTypeError'


class _BaseOffset(object):
    """
    Base class for DateOffset methods that are not overridden by subclasses
        and will (after pickle errors are resolved) go into a cdef class.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_n(self, *args, **kwargs): # real signature unknown
        """
        Require that `n` be a nonzero integer.
        
                Parameters
                ----------
                n : int
        
                Returns
                -------
                nint : int
        
                Raises
                ------
                TypeError if `int(n)` raises
                ValueError if n != int(n)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Return a pickleable state """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Reconstruct an instance from a pickled state """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns a copy of the calling offset object with n=1 and all other
        attributes equal.
        """

    kwds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns a tuple containing all of the attributes needed to evaluate
        equality between two DateOffset objects.
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = frozenset(['normalize', 'n'])
    _day_opt = None
    _typ = 'dateoffset'
    __dict__ = None # (!) real value is "dict_proxy({'__ne__': <cyfunction _BaseOffset.__ne__ at 0x000000000376B888>, '__module__': 'pandas._libs.tslibs.offsets', '__repr__': <cyfunction _BaseOffset.__repr__ at 0x000000000377A108>, '__setstate__': <cyfunction _BaseOffset.__setstate__ at 0x000000000377A348>, '_attributes': frozenset(['normalize', 'n']), '_params': <property object at 0x0000000003776688>, '__hash__': <cyfunction _BaseOffset.__hash__ at 0x000000000376B948>, 'base': <property object at 0x0000000003776728>, '_get_offset_day': <cyfunction _BaseOffset._get_offset_day at 0x000000000377A1C8>, '__add__': <cyfunction _BaseOffset.__add__ at 0x000000000376BC48>, '__dict__': <attribute '__dict__' of '_BaseOffset' objects>, 'copy': <cyfunction _BaseOffset.copy at 0x000000000377A048>, '__eq__': <cyfunction _BaseOffset.__eq__ at 0x000000000376B7C8>, '__init__': <cyfunction _BaseOffset.__init__ at 0x000000000376B588>, '__setattr__': <cyfunction _BaseOffset.__setattr__ at 0x000000000376B708>, 'kwds': <property object at 0x00000000037766D8>, '__weakref__': <attribute '__weakref__' of '_BaseOffset' objects>, '__qualname__': '_BaseOffset', '_validate_n': <cyfunction _BaseOffset._validate_n at 0x000000000377A288>, '_typ': 'dateoffset', '__mul__': <cyfunction _BaseOffset.__mul__ at 0x000000000376BE88>, '_day_opt': None, '__call__': <cyfunction _BaseOffset.__call__ at 0x000000000376BDC8>, '__sub__': <cyfunction _BaseOffset.__sub__ at 0x000000000376BD08>, '__getstate__': <cyfunction _BaseOffset.__getstate__ at 0x000000000377A408>, '__doc__': '\\n    Base class for DateOffset methods that are not overridden by subclasses\\n    and will (after pickle errors are resolved) go into a cdef class.\\n    ', '__neg__': <cyfunction _BaseOffset.__neg__ at 0x000000000376BF48>})"
    __qualname__ = '_BaseOffset'


class BaseOffset(_BaseOffset):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    __qualname__ = 'BaseOffset'


class relativedelta(object):
    """
    The relativedelta type is designed to be applied to an existing datetime and
        can replace specific components of that datetime, or represents an interval
        of time.
    
        It is based on the specification of the excellent work done by M.-A. Lemburg
        in his
        `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.
        However, notice that this type does *NOT* implement the same algorithm as
        his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
    
        There are two different ways to build a relativedelta instance. The
        first one is passing it two date/datetime classes::
    
            relativedelta(datetime1, datetime2)
    
        The second one is passing it any number of the following keyword arguments::
    
            relativedelta(arg1=x,arg2=y,arg3=z...)
    
            year, month, day, hour, minute, second, microsecond:
                Absolute information (argument is singular); adding or subtracting a
                relativedelta with absolute information does not perform an arithmetic
                operation, but rather REPLACES the corresponding value in the
                original datetime with the value(s) in relativedelta.
    
            years, months, weeks, days, hours, minutes, seconds, microseconds:
                Relative information, may be negative (argument is plural); adding
                or subtracting a relativedelta with relative information performs
                the corresponding arithmetic operation on the original datetime value
                with the information in the relativedelta.
    
            weekday: 
                One of the weekday instances (MO, TU, etc) available in the
                relativedelta module. These instances may receive a parameter N,
                specifying the Nth weekday, which could be positive or negative
                (like MO(+1) or MO(-2)). Not specifying it is the same as specifying
                +1. You can also use an integer, where 0=MO. This argument is always
                relative e.g. if the calculated date is already Monday, using MO(1)
                or MO(-1) won't change the day. To effectively make it absolute, use
                it in combination with the day argument (e.g. day=1, MO(1) for first
                Monday of the month).
    
            leapdays:
                Will add given days to the date found, if year is a leap
                year, and the date found is post 28 of february.
    
            yearday, nlyearday:
                Set the yearday or the non-leap year day (jump leap days).
                These are converted to day/month/leapdays information.
    
        There are relative and absolute forms of the keyword
        arguments. The plural is relative, and the singular is
        absolute. For each argument in the order below, the absolute form
        is applied first (by setting each attribute to that value) and
        then the relative form (by adding the value to the attribute).
    
        The order of attributes considered when this relativedelta is
        added to a datetime is:
    
        1. Year
        2. Month
        3. Day
        4. Hours
        5. Minutes
        6. Seconds
        7. Microseconds
    
        Finally, weekday is applied, using the rule described above.
    
        For example
    
        >>> from datetime import datetime
        >>> from dateutil.relativedelta import relativedelta, MO
        >>> dt = datetime(2018, 4, 9, 13, 37, 0)
        >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))
        >>> dt + delta
        datetime.datetime(2018, 4, 2, 14, 37)
    
        First, the day is set to 1 (the first of the month), then 25 hours
        are added, to get to the 2nd day and 14th hour, finally the
        weekday is applied, but since the 2nd is already a Monday there is
        no effect.
    """
    def normalized(self): # real signature unknown; restored from __doc__
        """
        Return a version of this object represented entirely using integer
                values for the relative attributes.
        
                >>> relativedelta(days=1.5, hours=2).normalized()
                relativedelta(days=+1, hours=+14)
        
                :return:
                    Returns a :class:`dateutil.relativedelta.relativedelta` object.
        """
        pass

    def _fix(self, *args, **kwargs): # real signature unknown
        pass

    def _set_months(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    weeks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'dict_proxy({\'__ne__\': <function __ne__ at 0x0000000005D486D8>, \'__module__\': \'dateutil.relativedelta\', \'__dict__\': <attribute \'__dict__\' of \'relativedelta\' objects>, \'__radd__\': <function __radd__ at 0x0000000005EABCF8>, \'__bool__\': <function __bool__ at 0x0000000005D48358>, \'__truediv__\': <function __div__ at 0x0000000005D48748>, \'__rsub__\': <function __rsub__ at 0x0000000005D48048>, \'normalized\': <function normalized at 0x0000000005EABDD8>, \'__add__\': <function __add__ at 0x0000000005EABF98>, \'__rmul__\': <function __mul__ at 0x0000000005D483C8>, \'__eq__\': <function __eq__ at 0x0000000005D48438>, \'__init__\': <function __init__ at 0x0000000005D3E5F8>, \'__nonzero__\': <function __bool__ at 0x0000000005D48358>, \'__weakref__\': <attribute \'__weakref__\' of \'relativedelta\' objects>, \'_set_months\': <function _set_months at 0x0000000005D3EF98>, \'__abs__\': <function __abs__ at 0x0000000005D48278>, \'__div__\': <function __div__ at 0x0000000005D48748>, \'__mul__\': <function __mul__ at 0x0000000005D483C8>, \'_fix\': <function _fix at 0x0000000005D3EC88>, \'__repr__\': <function __repr__ at 0x0000000005D48B38>, \'__hash__\': <function __hash__ at 0x0000000005D48668>, \'__sub__\': <function __sub__ at 0x0000000005D480B8>, \'weeks\': <property object at 0x0000000005D582C8>, \'__doc__\': "\\n    The relativedelta type is designed to be applied to an existing datetime and\\n    can replace specific components of that datetime, or represents an interval\\n    of time.\\n\\n    It is based on the specification of the excellent work done by M.-A. Lemburg\\n    in his\\n    `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.\\n    However, notice that this type does *NOT* implement the same algorithm as\\n    his work. Do *NOT* expect it to behave like mx.DateTime\'s counterpart.\\n\\n    There are two different ways to build a relativedelta instance. The\\n    first one is passing it two date/datetime classes::\\n\\n        relativedelta(datetime1, datetime2)\\n\\n    The second one is passing it any number of the following keyword arguments::\\n\\n        relativedelta(arg1=x,arg2=y,arg3=z...)\\n\\n        year, month, day, hour, minute, second, microsecond:\\n            Absolute information (argument is singular); adding or subtracting a\\n            relativedelta with absolute information does not perform an arithmetic\\n            operation, but rather REPLACES the corresponding value in the\\n            original datetime with the value(s) in relativedelta.\\n\\n        years, months, weeks, days, hours, minutes, seconds, microseconds:\\n            Relative information, may be negative (argument is plural); adding\\n            or subtracting a relativedelta with relative information performs\\n            the corresponding arithmetic operation on the original datetime value\\n            with the information in the relativedelta.\\n\\n        weekday: \\n            One of the weekday instances (MO, TU, etc) available in the\\n            relativedelta module. These instances may receive a parameter N,\\n            specifying the Nth weekday, which could be positive or negative\\n            (like MO(+1) or MO(-2)). Not specifying it is the same as specifying\\n            +1. You can also use an integer, where 0=MO. This argument is always\\n            relative e.g. if the calculated date is already Monday, using MO(1)\\n            or MO(-1) won\'t change the day. To effectively make it absolute, use\\n            it in combination with the day argument (e.g. day=1, MO(1) for first\\n            Monday of the month).\\n\\n        leapdays:\\n            Will add given days to the date found, if year is a leap\\n            year, and the date found is post 28 of february.\\n\\n        yearday, nlyearday:\\n            Set the yearday or the non-leap year day (jump leap days).\\n            These are converted to day/month/leapdays information.\\n\\n    There are relative and absolute forms of the keyword\\n    arguments. The plural is relative, and the singular is\\n    absolute. For each argument in the order below, the absolute form\\n    is applied first (by setting each attribute to that value) and\\n    then the relative form (by adding the value to the attribute).\\n\\n    The order of attributes considered when this relativedelta is\\n    added to a datetime is:\\n\\n    1. Year\\n    2. Month\\n    3. Day\\n    4. Hours\\n    5. Minutes\\n    6. Seconds\\n    7. Microseconds\\n\\n    Finally, weekday is applied, using the rule described above.\\n\\n    For example\\n\\n    >>> from datetime import datetime\\n    >>> from dateutil.relativedelta import relativedelta, MO\\n    >>> dt = datetime(2018, 4, 9, 13, 37, 0)\\n    >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))\\n    >>> dt + delta\\n    datetime.datetime(2018, 4, 2, 14, 37)\\n\\n    First, the day is set to 1 (the first of the month), then 25 hours\\n    are added, to get to the 2nd day and 14th hour, finally the\\n    weekday is applied, but since the 2nd is already a Monday there is\\n    no effect.\\n\\n    ", \'__neg__\': <function __neg__ at 0x0000000005D482E8>})'


class _Tick(object):
    """
    dummy class to mix into tseries.offsets.Tick so that in tslibs.period we
        can do isinstance checks on _Tick and avoid importing tseries.offsets
    """
    def __div__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "dict_proxy({'__module__': 'pandas._libs.tslibs.offsets', '__truediv__': <cyfunction _Tick.__truediv__ at 0x000000000377A708>, '__qualname__': '_Tick', '__div__': <cyfunction _Tick.__truediv__ at 0x000000000377A708>, '__dict__': <attribute '__dict__' of '_Tick' objects>, '__weakref__': <attribute '__weakref__' of '_Tick' objects>, '__doc__': '\\n    dummy class to mix into tseries.offsets.Tick so that in tslibs.period we\\n    can do isinstance checks on _Tick and avoid importing tseries.offsets\\n    '})"
    __qualname__ = '_Tick'


# variables with complex values

DAYS = [
    'MON',
    'TUE',
    'WED',
    'THU',
    'FRI',
    'SAT',
    'SUN',
]

MONTHS = [
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUL',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
]

need_suffix = [
    'QS',
    'BQ',
    'BQS',
    'YS',
    'AS',
    'BY',
    'BA',
    'BYS',
    'BAS',
]

relativedelta_kwds = None # (!) real value is "set(['hour', 'microseconds', 'seconds', 'nanoseconds', 'months', 'nanosecond', 'days', 'month', 'hours', 'second', 'microsecond', 'weekday', 'year', 'weeks', 'years', 'minutes', 'day', 'minute'])"

UTC = None # (!) real value is '<UTC>'

_offset_to_period_map = {
    'A': 'A',
    'A-APR': 'A-APR',
    'A-AUG': 'A-AUG',
    'A-DEC': 'A-DEC',
    'A-FEB': 'A-FEB',
    'A-JAN': 'A-JAN',
    'A-JUL': 'A-JUL',
    'A-JUN': 'A-JUN',
    'A-MAR': 'A-MAR',
    'A-MAY': 'A-MAY',
    'A-NOV': 'A-NOV',
    'A-OCT': 'A-OCT',
    'A-SEP': 'A-SEP',
    'AS': 'A',
    'AS-APR': 'A',
    'AS-AUG': 'A',
    'AS-DEC': 'A',
    'AS-FEB': 'A',
    'AS-JAN': 'A',
    'AS-JUL': 'A',
    'AS-JUN': 'A',
    'AS-MAR': 'A',
    'AS-MAY': 'A',
    'AS-NOV': 'A',
    'AS-OCT': 'A',
    'AS-SEP': 'A',
    'B': 'B',
    'BA': 'A',
    'BA-APR': 'A',
    'BA-AUG': 'A',
    'BA-DEC': 'A',
    'BA-FEB': 'A',
    'BA-JAN': 'A',
    'BA-JUL': 'A',
    'BA-JUN': 'A',
    'BA-MAR': 'A',
    'BA-MAY': 'A',
    'BA-NOV': 'A',
    'BA-OCT': 'A',
    'BA-SEP': 'A',
    'BAS': 'A',
    'BAS-APR': 'A',
    'BAS-AUG': 'A',
    'BAS-DEC': 'A',
    'BAS-FEB': 'A',
    'BAS-JAN': 'A',
    'BAS-JUL': 'A',
    'BAS-JUN': 'A',
    'BAS-MAR': 'A',
    'BAS-MAY': 'A',
    'BAS-NOV': 'A',
    'BAS-OCT': 'A',
    'BAS-SEP': 'A',
    'BM': 'M',
    'BQ': 'Q',
    'BQ-APR': 'Q',
    'BQ-AUG': 'Q',
    'BQ-DEC': 'Q',
    'BQ-FEB': 'Q',
    'BQ-JAN': 'Q',
    'BQ-JUL': 'Q',
    'BQ-JUN': 'Q',
    'BQ-MAR': 'Q',
    'BQ-MAY': 'Q',
    'BQ-NOV': 'Q',
    'BQ-OCT': 'Q',
    'BQ-SEP': 'Q',
    'BQS': 'Q',
    'BQS-APR': 'Q',
    'BQS-AUG': 'Q',
    'BQS-DEC': 'Q',
    'BQS-FEB': 'Q',
    'BQS-JAN': 'Q',
    'BQS-JUL': 'Q',
    'BQS-JUN': 'Q',
    'BQS-MAR': 'Q',
    'BQS-MAY': 'Q',
    'BQS-NOV': 'Q',
    'BQS-OCT': 'Q',
    'BQS-SEP': 'Q',
    'BY': 'A',
    'BY-APR': 'A',
    'BY-AUG': 'A',
    'BY-DEC': 'A',
    'BY-FEB': 'A',
    'BY-JAN': 'A',
    'BY-JUL': 'A',
    'BY-JUN': 'A',
    'BY-MAR': 'A',
    'BY-MAY': 'A',
    'BY-NOV': 'A',
    'BY-OCT': 'A',
    'BY-SEP': 'A',
    'BYS': 'A',
    'BYS-APR': 'A',
    'BYS-AUG': 'A',
    'BYS-DEC': 'A',
    'BYS-FEB': 'A',
    'BYS-JAN': 'A',
    'BYS-JUL': 'A',
    'BYS-JUN': 'A',
    'BYS-MAR': 'A',
    'BYS-MAY': 'A',
    'BYS-NOV': 'A',
    'BYS-OCT': 'A',
    'BYS-SEP': 'A',
    'C': 'C',
    'D': 'D',
    'EOM': 'M',
    'H': 'H',
    'L': 'L',
    'M': 'M',
    'MS': 'M',
    'N': 'N',
    'Q': 'Q',
    'Q-APR': 'Q-APR',
    'Q-AUG': 'Q-AUG',
    'Q-DEC': 'Q-DEC',
    'Q-FEB': 'Q-FEB',
    'Q-JAN': 'Q-JAN',
    'Q-JUL': 'Q-JUL',
    'Q-JUN': 'Q-JUN',
    'Q-MAR': 'Q-MAR',
    'Q-MAY': 'Q-MAY',
    'Q-NOV': 'Q-NOV',
    'Q-OCT': 'Q-OCT',
    'Q-SEP': 'Q-SEP',
    'QS': 'Q',
    'QS-APR': 'Q',
    'QS-AUG': 'Q',
    'QS-DEC': 'Q',
    'QS-FEB': 'Q',
    'QS-JAN': 'Q',
    'QS-JUL': 'Q',
    'QS-JUN': 'Q',
    'QS-MAR': 'Q',
    'QS-MAY': 'Q',
    'QS-NOV': 'Q',
    'QS-OCT': 'Q',
    'QS-SEP': 'Q',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'W': 'W',
    'W-FRI': 'W-FRI',
    'W-MON': 'W-MON',
    'W-SAT': 'W-SAT',
    'W-SUN': 'W-SUN',
    'W-THU': 'W-THU',
    'W-TUE': 'W-TUE',
    'W-WED': 'W-WED',
    'WEEKDAY': 'D',
    'Y': 'A',
    'YS': 'A',
    'YS-APR': 'A',
    'YS-AUG': 'A',
    'YS-DEC': 'A',
    'YS-FEB': 'A',
    'YS-JAN': 'A',
    'YS-JUL': 'A',
    'YS-JUN': 'A',
    'YS-MAR': 'A',
    'YS-MAY': 'A',
    'YS-NOV': 'A',
    'YS-OCT': 'A',
    'YS-SEP': 'A',
}

__pyx_capi__ = {
    'to_offset': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000000000375CDB0>'
}

__test__ = {
    u'get_day_of_month (line 928)': u"\n    Find the day in `other`'s month that satisfies a DateOffset's onOffset\n    policy, as described by the `day_opt` argument.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    day_opt : 'start', 'end', 'business_start', 'business_end', or int\n        'start': returns 1\n        'end': returns last day of the month\n        'business_start': returns the first business day of the month\n        'business_end': returns the last business day of the month\n        int: returns the day in the month indicated by `other`, or the last of\n            day the month if the value exceeds in that month's number of days.\n\n    Returns\n    -------\n    day_of_month : int\n\n    Examples\n    -------\n    >>> other = datetime(2017, 11, 14)\n    >>> get_day_of_month(other, 'start')\n    1\n    >>> get_day_of_month(other, 'end')\n    30\n\n    ",
    u'roll_yearday (line 1053)': u"\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : reference month giving the first month of the year\n    day_opt : 'start', 'end', 'business_start', 'business_end', or int\n        The day of the month to compare against that of `other` when\n        incrementing or decrementing the number of periods:\n\n        'start': 1\n        'end': last day of the month\n        'business_start': first business day of the month\n        'business_end': last business day of the month\n        int: day in the month indicated by `other`, or the last of day\n            the month if the value exceeds in that month's number of days.\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    Notes\n    -----\n    * Mirrors `roll_check` in shift_months\n\n    Examples\n    -------\n    >>> month = 3\n    >>> day_opt = 'start'              # `other` will be compared to March 1\n    >>> other = datetime(2017, 2, 10)  # before March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    1\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp('2014-03-15', tz='US/Eastern')  # after March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    2\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    >>> month = 6\n    >>> day_opt = 'end'                # `other` will be compared to June 30\n    >>> other = datetime(1999, 6, 29)  # before June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    4\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp(2072, 8, 24, 6, 17, 18)  # after June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    5\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    ",
}


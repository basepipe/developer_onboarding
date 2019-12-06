# encoding: utf-8
# module pandas._libs.tslibs.timezones
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\timezones.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # C:\Python27\lib\site-packages\pytz\__init__.pyc
import datetime as __datetime
import dateutil.tz._common as __dateutil_tz__common


# functions

def dateutil_gettz(*args, **kwargs): # real signature unknown
    """
    Retrieve a time zone object from a string representation
    
            This function is intended to retrieve the :py:class:`tzinfo` subclass
            that best represents the time zone that would be used if a POSIX
            `TZ variable`_ were set to the same value.
    
            If no argument or an empty string is passed to ``gettz``, local time
            is returned:
    
            .. code-block:: python3
    
                >>> gettz()
                tzfile('/etc/localtime')
    
            This function is also the preferred way to map IANA tz database keys
            to :class:`tzfile` objects:
    
            .. code-block:: python3
    
                >>> gettz('Pacific/Kiritimati')
                tzfile('/usr/share/zoneinfo/Pacific/Kiritimati')
    
            On Windows, the standard is extended to include the Windows-specific
            zone names provided by the operating system:
    
            .. code-block:: python3
    
                >>> gettz('Egypt Standard Time')
                tzwin('Egypt Standard Time')
    
            Passing a GNU ``TZ`` style string time zone specification returns a
            :class:`tzstr` object:
    
            .. code-block:: python3
    
                >>> gettz('AEST-10AEDT-11,M10.1.0/2,M4.1.0/3')
                tzstr('AEST-10AEDT-11,M10.1.0/2,M4.1.0/3')
    
            :param name:
                A time zone name (IANA, or, on Windows, Windows keys), location of
                a ``tzfile(5)`` zoneinfo file or ``TZ`` variable style time zone
                specifier. An empty string, no argument or ``None`` is interpreted
                as local time.
    
            :return:
                Returns an instance of one of ``dateutil``'s :py:class:`tzinfo`
                subclasses.
    
            .. versionchanged:: 2.7.0
    
                After version 2.7.0, any two calls to ``gettz`` using the same
                input strings will return the same object:
    
                .. code-block:: python3
    
                    >>> tz.gettz('America/Chicago') is tz.gettz('America/Chicago')
                    True
    
                In addition to improving performance, this ensures that
                `"same zone" semantics`_ are used for datetimes in the same zone.
    
    
            .. _`TZ variable`:
                https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html
    
            .. _`"same zone" semantics`:
                https://blog.ganssle.io/articles/2018/02/aware-datetime-arithmetic.html
    """
    pass

def get_timezone(*args, **kwargs): # real signature unknown
    """
    We need to do several things here:
        1) Distinguish between pytz and dateutil timezones
        2) Not be over-specific (e.g. US/Eastern with/without DST is same *zone*
           but a different tz object)
        3) Provide something to serialize when we're storing a datetime object
           in pytables.
    
        We return a string prefaced with dateutil if it's a dateutil tz, else just
        the tz name. It needs to be a string so that we can serialize it with
        UJSON/pytables. maybe_get_tz (below) is the inverse of this process.
    """
    pass

def infer_tzinfo(*args, **kwargs): # real signature unknown
    pass

def is_utc(*args, **kwargs): # real signature unknown
    pass

def maybe_get_tz(*args, **kwargs): # real signature unknown
    """
    (Maybe) Construct a timezone object from a string. If tz is a string, use
        it to construct a timezone object. Otherwise, just return tz.
    """
    pass

def tz_compare(*args, **kwargs): # real signature unknown
    """
    Compare string representations of timezones
    
        The same timezone can be represented as different instances of
        timezones. For example
        `<DstTzInfo 'Europe/Paris' LMT+0:09:00 STD>` and
        `<DstTzInfo 'Europe/Paris' CET+1:00:00 STD>` are essentially same
        timezones but aren't evaluated such, but the string representation
        for both of these is `'Europe/Paris'`.
    
        This exists only to add a notion of equality to pytz-style zones
        that is compatible with the notion of equality expected of tzinfo
        subclasses.
    
        Parameters
        ----------
        start : tzinfo
        end : tzinfo
    
        Returns:
        -------
        compare : bint
    """
    pass

def tz_standardize(tz): # real signature unknown; restored from __doc__
    """
    If the passed tz is a pytz timezone object, "normalize" it to the a
        consistent version
    
        Parameters
        ----------
        tz : tz object
    
        Returns:
        -------
        tz object
    
        Examples:
        --------
        >>> tz
        <DstTzInfo 'US/Pacific' PST-1 day, 16:00:00 STD>
    
        >>> tz_standardize(tz)
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    
        >>> tz
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    
        >>> tz_standardize(tz)
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    
        >>> tz
        dateutil.tz.tz.tzutc
    
        >>> tz_standardize(tz)
        dateutil.tz.tz.tzutc
    """
    pass

def _p_tz_cache_key(*args, **kwargs): # real signature unknown
    """ Python interface for cache function to facilitate testing. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class _dateutil_tzfile(__dateutil_tz__common._tzinfo):
    """
    This is a ``tzinfo`` subclass that allows one to use the ``tzfile(5)``
        format timezone files to extract current and historical zone information.
    
        :param fileobj:
            This can be an opened file stream or a file name that the time zone
            information can be read from.
    
        :param filename:
            This is an optional parameter specifying the source of the time zone
            information in the event that ``fileobj`` is a file object. If omitted
            and ``fileobj`` is a file stream, this parameter will be set either to
            ``fileobj``'s ``name`` attribute or to ``repr(fileobj)``.
    
        See `Sources for Time Zone and Daylight Saving Time Data
        <https://data.iana.org/time-zones/tz-link.html>`_ for more information.
        Time zone files can be compiled from the `IANA Time Zone database files
        <https://www.iana.org/time-zones>`_ with the `zic time zone compiler
        <https://www.freebsd.org/cgi/man.cgi?query=zic&sektion=8>`_
    
        .. note::
    
            Only construct a ``tzfile`` directly if you have a specific timezone
            file on disk that you want to read into a Python ``tzinfo`` object.
            If you want to get a ``tzfile`` representing a specific IANA zone,
            (e.g. ``'America/New_York'``), you should call
            :func:`dateutil.tz.gettz` with the zone identifier.
    
    
        **Examples:**
    
        Using the US Eastern time zone as an example, we can see that a ``tzfile``
        provides time zone information for the standard Daylight Saving offsets:
    
        .. testsetup:: tzfile
    
            from dateutil.tz import gettz
            from datetime import datetime
    
        .. doctest:: tzfile
    
            >>> NYC = gettz('America/New_York')
            >>> NYC
            tzfile('/usr/share/zoneinfo/America/New_York')
    
            >>> print(datetime(2016, 1, 3, tzinfo=NYC))     # EST
            2016-01-03 00:00:00-05:00
    
            >>> print(datetime(2016, 7, 7, tzinfo=NYC))     # EDT
            2016-07-07 00:00:00-04:00
    
    
        The ``tzfile`` structure contains a fully history of the time zone,
        so historical dates will also have the right offsets. For example, before
        the adoption of the UTC standards, New York used local solar  mean time:
    
        .. doctest:: tzfile
    
           >>> print(datetime(1901, 4, 12, tzinfo=NYC))    # LMT
           1901-04-12 00:00:00-04:56
    
        And during World War II, New York was on "Eastern War Time", which was a
        state of permanent daylight saving time:
    
        .. doctest:: tzfile
    
            >>> print(datetime(1944, 2, 7, tzinfo=NYC))    # EWT
            1944-02-07 00:00:00-04:00
    """
    def dst(self, *args, **kwargs): # real signature unknown
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """
        The ``tzfile`` implementation of :py:func:`datetime.tzinfo.fromutc`.
        
                :param dt:
                    A :py:class:`datetime.datetime` object.
        
                :raises TypeError:
                    Raised if ``dt`` is not a :py:class:`datetime.datetime` object.
        
                :raises ValueError:
                    Raised if this is called with a ``dt`` which does not have this
                    ``tzinfo`` attached.
        
                :return:
                    Returns a :py:class:`datetime.datetime` object representing the
                    wall time in ``self``'s time zone.
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

    def _find_last_transition(self, *args, **kwargs): # real signature unknown
        pass

    def _find_ttinfo(self, *args, **kwargs): # real signature unknown
        pass

    def _get_ttinfo(self, *args, **kwargs): # real signature unknown
        pass

    def _read_tzfile(self, *args, **kwargs): # real signature unknown
        pass

    def _resolve_ambiguous_time(self, *args, **kwargs): # real signature unknown
        pass

    def _set_tzdata(self, *args, **kwargs): # real signature unknown
        """ Set the time zone data of this object from a _tzfile object """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __hash__ = None


class _dateutil_tzlocal(__dateutil_tz__common._tzinfo):
    """ A :class:`tzinfo` subclass built around the ``time`` timezone functions. """
    def dst(self, *args, **kwargs): # real signature unknown
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

    def _isdst(self, *args, **kwargs): # real signature unknown
        pass

    def _naive_is_dst(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __hash__ = None


class _dateutil_tzutc(__datetime.tzinfo):
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

    def __init__(self, *args, **kwargs): # real signature unknown
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
    __dict__ = None # (!) real value is 'dict_proxy({\'__ne__\': <function __ne__ at 0x0000000005B953C8>, \'__module__\': \'dateutil.tz.tz\', \'_TzSingleton__instance\': tzutc(), \'fromutc\': <function fromutc at 0x0000000005B952E8>, \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'dst\': <function dst at 0x0000000005B950B8>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'is_ambiguous\': <function is_ambiguous at 0x0000000005B95208>, \'utcoffset\': <function utcoffset at 0x0000000005B95048>, \'tzname\': <function tzname at 0x0000000005B95198>, \'__hash__\': None, \'__eq__\': <function __eq__ at 0x0000000005B95358>, \'__doc__\': "\\n    This is a tzinfo object that represents the UTC time zone.\\n\\n    **Examples:**\\n\\n    .. doctest::\\n\\n        >>> from datetime import *\\n        >>> from dateutil.tz import *\\n\\n        >>> datetime.now()\\n        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n        >>> datetime.now(tzutc())\\n        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n        >>> datetime.now(tzutc()).tzname()\\n        \'UTC\'\\n\\n    .. versionchanged:: 2.7.0\\n        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n        always return the same object.\\n\\n        .. doctest::\\n\\n            >>> from dateutil.tz import tzutc, UTC\\n            >>> tzutc() is tzutc()\\n            True\\n            >>> tzutc() is UTC\\n            True\\n    ", \'__repr__\': <function __repr__ at 0x0000000005B95438>})'
    __hash__ = None


class _pytz_BaseTzInfo(__datetime.tzinfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    zone = None
    _tzname = None
    _utcoffset = None
    __dict__ = None # (!) real value is "dict_proxy({'__module__': 'pytz.tzinfo', '_utcoffset': None, 'zone': None, '__str__': <function __str__ at 0x00000000031DA438>, '__dict__': <attribute '__dict__' of 'BaseTzInfo' objects>, '__weakref__': <attribute '__weakref__' of 'BaseTzInfo' objects>, '__doc__': None, '_tzname': None})"


# variables with complex values

dst_cache = {}

UTC = pytz.UTC

__pyx_capi__ = {
    'get_dst_info': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000000000344FA20>'
    'get_timezone': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000000003216210>'
    'get_utcoffset': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x000000000344F930>'
    'is_fixed_offset': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000000000344F9C0>'
    'is_tzlocal': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000000003216510>'
    'is_utc': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x00000000032164E0>'
    'maybe_get_tz': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x00000000032161B0>'
    'treat_tz_as_dateutil': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000000003216390>'
    'treat_tz_as_pytz': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000000003216450>'
    'tz_compare': None, # (!) real value is '<capsule object "int (PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x0000000003216240>'
}

__test__ = {
    u'tz_standardize (line 324)': u'\n    If the passed tz is a pytz timezone object, "normalize" it to the a\n    consistent version\n\n    Parameters\n    ----------\n    tz : tz object\n\n    Returns:\n    -------\n    tz object\n\n    Examples:\n    --------\n    >>> tz\n    <DstTzInfo \'US/Pacific\' PST-1 day, 16:00:00 STD>\n\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz\n    dateutil.tz.tz.tzutc\n\n    >>> tz_standardize(tz)\n    dateutil.tz.tz.tzutc\n    ',
}


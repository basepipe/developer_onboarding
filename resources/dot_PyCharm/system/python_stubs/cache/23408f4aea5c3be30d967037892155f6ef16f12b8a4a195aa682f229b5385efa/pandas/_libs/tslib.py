# encoding: utf-8
# module pandas._libs.tslib
# from C:\Python27\lib\site-packages\pandas\_libs\tslib.pyd
# by generator 1.147
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # C:\Python27\lib\site-packages\pytz\__init__.pyc
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string

from pandas._libs.tslibs.timestamps import Timestamp


# Variables with simple values

iNaT = -9223372036854775808L

# functions

def array_to_datetime(*args, **kwargs): # real signature unknown
    """
    Converts a 1D array of date-like values to a numpy array of either:
            1) datetime64[ns] data
            2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError
               is encountered
    
        Also returns a pytz.FixedOffset if an array of strings with the same
        timezone offset is passed and utc=True is not passed. Otherwise, None
        is returned
    
        Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,
        strings
    
        Parameters
        ----------
        values : ndarray of object
             date-like objects to convert
        errors : str, default 'raise'
             error behavior when parsing
        dayfirst : bool, default False
             dayfirst parsing behavior when encountering datetime strings
        yearfirst : bool, default False
             yearfirst parsing behavior when encountering datetime strings
        utc : bool, default None
             indicator whether the dates should be UTC
        require_iso8601 : bool, default False
             indicator whether the datetime string should be iso8601
    
        Returns
        -------
        tuple (ndarray, tzoffset)
    """
    pass

def array_with_unit_to_datetime(*args, **kwargs): # real signature unknown
    """
    convert the ndarray according to the unit
        if errors:
          - raise: return converted values or raise OutOfBoundsDatetime
              if out of range on the conversion or
              ValueError for other conversions (e.g. a string)
          - ignore: return non-convertible values as the same unit
          - coerce: NaT for non-convertibles
    """
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return a np object array of the string formatted values
    
        Parameters
        ----------
        values : a 1-d i8 array
        tz : the timezone (or None)
        format : optional, default is None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
    """
    pass

def ints_to_pydatetime(*args, **kwargs): # real signature unknown
    """
    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp
    
        Parameters
        ----------
        arr  : array of i8
        tz   : str, default None
             convert to this timezone
        freq : str/Offset, default None
             freq to convert
        box  : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'
             If datetime, convert to datetime.datetime
             If date, convert to datetime.date
             If time, convert to datetime.time
             If Timestamp, convert to pandas.Timestamp
    
        Returns
        -------
        result : array of dtype specified by box
    """
    pass

def _test_parse_iso8601(*args, **kwargs): # real signature unknown
    """
    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used
        only for testing, actual construction uses `convert_str_to_tsobject`
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

nat_strings = None # (!) real value is "set(['nat', 'NaT', 'NAN', 'nan', 'NaN', 'NAT'])"

UTC = pytz.UTC

__test__ = {}


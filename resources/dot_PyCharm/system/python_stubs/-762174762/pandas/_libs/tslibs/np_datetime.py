# encoding: utf-8
# module pandas._libs.tslibs.np_datetime
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\np_datetime.pyd
# by generator 1.147
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# no functions
# classes

class OutOfBoundsDatetime(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'OutOfBoundsDatetime'


# variables with complex values

__pyx_capi__ = {
    '_string_to_dts': None, # (!) real value is '<capsule object "int (PyObject *, npy_datetimestruct *, int *, int *)" at 0x0000000005B001E0>'
    'check_dts_bounds': None, # (!) real value is '<capsule object "PyObject *(npy_datetimestruct *)" at 0x0000000005AFAFC0>'
    'cmp_scalar': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_int64_t, __pyx_t_5numpy_int64_t, int)" at 0x0000000005AFAF60>'
    'dt64_to_dtstruct': None, # (!) real value is '<capsule object "void (__pyx_t_5numpy_int64_t, npy_datetimestruct *)" at 0x0000000005B00030>'
    'dtstruct_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (npy_datetimestruct *)" at 0x0000000005AFAE70>'
    'get_datetime64_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyObject *)" at 0x0000000005B00180>'
    'get_datetime64_value': None, # (!) real value is '<capsule object "npy_datetime (PyObject *)" at 0x0000000005B00120>'
    'get_timedelta64_value': None, # (!) real value is '<capsule object "npy_timedelta (PyObject *)" at 0x0000000005B00150>'
    'pydate_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_Date *, npy_datetimestruct *)" at 0x0000000005B000C0>'
    'pydatetime_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *)" at 0x0000000005B00090>'
    'reverse_ops': None, # (!) real value is '<capsule object "int [6]" at 0x0000000005AFAF30>'
    'td64_to_tdstruct': None, # (!) real value is '<capsule object "void (__pyx_t_5numpy_int64_t, pandas_timedeltastruct *)" at 0x0000000005B00060>'
}

__test__ = {}


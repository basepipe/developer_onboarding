# encoding: utf-8
# module _ctypes
# from (pre-generated)
# by generator 1.147
""" Create and manipulate C compatible data types in Python. """
# no imports

# Variables with simple values

FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0

FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16

RTLD_GLOBAL = 0
RTLD_LOCAL = 0

_cast_addr = 1887211824L

_memmove_addr = 1918165552L

_memset_addr = 1887248546L

_string_at_addr = 1887211584L

_wstring_at_addr = 1887212144L

__version__ = '1.1.0'

# functions

def addressof(C_instance): # real signature unknown; restored from __doc__
    """
    addressof(C instance) -> integer
    Return the address of the C instance internal buffer
    """
    return 0

def alignment(C_type): # real signature unknown; restored from __doc__
    """
    alignment(C type) -> integer
    alignment(C instance) -> integer
    Return the alignment requirements of a C instance
    """
    return 0

def byref(C_instance, offset=0): # real signature unknown; restored from __doc__
    """
    byref(C instance[, offset=0]) -> byref-object
    Return a pointer lookalike to a C instance, only usable
    as function argument
    """
    pass

def call_cdeclfunction(*args, **kwargs): # real signature unknown
    pass

def call_commethod(*args, **kwargs): # real signature unknown
    pass

def call_function(*args, **kwargs): # real signature unknown
    pass

def CopyComPointer(src, dst): # real signature unknown; restored from __doc__
    """ CopyComPointer(src, dst) -> HRESULT value """
    pass

def FormatError(integer=None): # real signature unknown; restored from __doc__
    """
    FormatError([integer]) -> string
    
    Convert a win32 error code into a string. If the error code is not
    given, the return value of a call to GetLastError() is used.
    """
    return ""

def FreeLibrary(handle): # real signature unknown; restored from __doc__
    """
    FreeLibrary(handle) -> void
    
    Free the handle of an executable previously loaded by LoadLibrary.
    """
    pass

def get_errno(*args, **kwargs): # real signature unknown
    pass

def get_last_error(*args, **kwargs): # real signature unknown
    pass

def LoadLibrary(name): # real signature unknown; restored from __doc__
    """
    LoadLibrary(name) -> handle
    
    Load an executable (usually a DLL), and return a handle to it.
    The handle may be used to locate exported functions in this
    module.
    """
    pass

def pointer(*args, **kwargs): # real signature unknown
    pass

def POINTER(*args, **kwargs): # real signature unknown
    pass

def PyObj_FromPtr(*args, **kwargs): # real signature unknown
    pass

def Py_DECREF(*args, **kwargs): # real signature unknown
    pass

def Py_INCREF(*args, **kwargs): # real signature unknown
    pass

def resize(*args, **kwargs): # real signature unknown
    """ Resize the memory buffer of a ctypes instance """
    pass

def set_conversion_mode(encoding, errors): # real signature unknown; restored from __doc__
    """
    set_conversion_mode(encoding, errors) -> (previous-encoding, previous-errors)
    
    Set the encoding and error handling ctypes uses when converting
    between unicode and strings.  Returns the previous values.
    """
    pass

def set_errno(*args, **kwargs): # real signature unknown
    pass

def set_last_error(*args, **kwargs): # real signature unknown
    pass

def sizeof(C_type): # real signature unknown; restored from __doc__
    """
    sizeof(C type) -> integer
    sizeof(C instance) -> integer
    Return the size in bytes of a C instance
    """
    return 0

def _buffer_info(*args, **kwargs): # real signature unknown
    """ Return buffer interface information (for testing only) """
    pass

def _check_HRESULT(*args, **kwargs): # real signature unknown
    pass

def _unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgumentError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Array(_CData):
    """ XXX to be provided """
    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass


class CFuncPtr(_CData):
    """ Function Pointer """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    argtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the argument types"""

    errcheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a function to check for errors"""

    restype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the result type"""



class COMError(Exception):
    """ Raised when a COM method call failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Structure(_CData):
    """ Structure base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Union(_CData):
    """ Union base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class _Pointer(_CData):
    """ XXX to be provided """
    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the object this pointer points to (read-write)"""



class _SimpleCData(_CData):
    """ XXX to be provided """
    def __ctypes_from_outparam__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current value"""



# variables with complex values

_pointer_type_cache = {
    None: None, # (!) real value is "<class 'ctypes.c_void_p'>"
    None:  # (!) real value is "<class 'ctypes.c_char'>"
        None # (!) real value is "<class 'ctypes.LP_c_char'>"
    ,
    None:  # (!) real value is "<class 'ctypes.c_wchar'>"
        None # (!) real value is "<class 'ctypes.LP_c_wchar'>"
    ,
}


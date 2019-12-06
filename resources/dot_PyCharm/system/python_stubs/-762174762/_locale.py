# encoding: utf-8
# module _locale
# from (built-in)
# by generator 1.147
""" Support for POSIX locales. """
# no imports

# Variables with simple values

CHAR_MAX = 127

LC_ALL = 0
LC_COLLATE = 1
LC_CTYPE = 2
LC_MONETARY = 3
LC_NUMERIC = 4
LC_TIME = 5

# functions

def localeconv(*args, **kwargs): # real signature unknown
    """ () -> dict. Returns numeric and monetary locale-specific parameters. """
    pass

def setlocale(*args, **kwargs): # real signature unknown
    """ (integer,string=None) -> string. Activates/queries locale processing. """
    pass

def strcoll(*args, **kwargs): # real signature unknown
    """ string,string -> int. Compares two strings according to the locale. """
    pass

def strxfrm(*args, **kwargs): # real signature unknown
    """ string -> string. Returns a string that behaves for cmp locale-aware. """
    pass

def _getdefaultlocale(*args, **kwargs): # real signature unknown
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




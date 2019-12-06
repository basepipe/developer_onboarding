# encoding: utf-8
# module _struct
# from (built-in)
# by generator 1.147
"""
Functions to convert between Python values and C structs represented
as Python strings. It uses format strings (explained below) as compact
descriptions of the lay-out of the C structs and the intended conversion
to/from Python values.

The optional first format char indicates byte order, size and alignment:
  @: native order, size & alignment (default)
  =: native order, std. size & alignment
  <: little-endian, std. size & alignment
  >: big-endian, std. size & alignment
  !: same as >

The remaining chars indicate types of args and must match exactly;
these can be preceded by a decimal repeat count:
  x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
  ?: _Bool (requires C99; if not available, char is used instead)
  h:short; H:unsigned short; i:int; I:unsigned int;
  l:long; L:unsigned long; f:float; d:double.
Special cases (preceding decimal count indicates length):
  s:string (array of char); p: pascal string (with count byte).
Special case (only available in native format):
  P:an integer type that is wide enough to hold a pointer.
Special case (not in native mode unless 'long long' in platform C):
  q:long long; Q:unsigned long long
Whitespace between formats is ignored.

The variable struct.error is an exception raised on errors.
"""
# no imports

# Variables with simple values

_PY_STRUCT_FLOAT_COERCE = 1

_PY_STRUCT_RANGE_CHECKING = 1

__version__ = '0.2'

# functions

def calcsize(fmt): # known case of _struct.calcsize
    """ Return size of C struct described by format string fmt. """
    return 0

def pack(fmt, *args): # known case of _struct.pack
    """ Return string containing values v1, v2, ... packed according to fmt. """
    return ""

def pack_into(fmt, buffer, offset, *args): # known case of _struct.pack_into
    """
    Pack the values v1, v2, ... according to fmt.
    Write the packed bytes into the writable buffer buf starting at offset.
    """
    pass

def unpack(fmt, string): # known case of _struct.unpack
    """
    Unpack the string containing packed C structure data, according to fmt.
    Requires len(string) == calcsize(fmt).
    """
    pass

def unpack_from(fmt, buffer, offset=0): # known case of _struct.unpack_from
    """
    Unpack the buffer, containing packed C structure data, according to
    fmt, starting at offset. Requires len(buffer[offset:]) >= calcsize(fmt).
    """
    pass

def _clearcache(*args, **kwargs): # real signature unknown
    """ Clear the internal cache. """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Struct(object):
    """ Compiled struct object """
    def pack(self, *args): # known case of _struct.Struct.pack
        """
        S.pack(v1, v2, ...) -> string
        
        Return a string containing values v1, v2, ... packed according to this
        Struct's format. See struct.__doc__ for more on format strings.
        """
        return ""

    def pack_into(self, buffer, offset, *args): # known case of _struct.Struct.pack_into
        """
        S.pack_into(buffer, offset, v1, v2, ...)
        
        Pack the values v1, v2, ... according to this Struct's format, write 
        the packed bytes into the writable buffer buf starting at offset.  Note
        that the offset is not an optional argument.  See struct.__doc__ for 
        more on format strings.
        """
        pass

    def unpack(self, string): # known case of _struct.Struct.unpack
        """
        S.unpack(str) -> (v1, v2, ...)
        
        Return tuple containing values unpacked according to this Struct's format.
        Requires len(str) == self.size. See struct.__doc__ for more on format
        strings.
        """
        pass

    def unpack_from(self, buffer, offset=0): # known case of _struct.Struct.unpack_from
        """
        S.unpack_from(buffer[, offset]) -> (v1, v2, ...)
        
        Return tuple containing values unpacked according to this Struct's format.
        Unlike unpack, unpack_from can unpack values from any object supporting
        the buffer API, not just str. Requires len(buffer[offset:]) >= self.size.
        See struct.__doc__ for more on format strings.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, fmt): # known case of _struct.Struct.__init__
        """
        Compiled struct object
        # (copied from class doc)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    format = property(lambda self: '')
    """struct format string

    :type: string
    """

    size = property(lambda self: 0)
    """struct size in bytes

    :type: int
    """




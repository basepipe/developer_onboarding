# encoding: utf-8
# module marshal
# from (built-in)
# by generator 1.147
"""
This module contains functions that can read and write Python values in
a binary format. The format is specific to Python, but independent of
machine architecture issues.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can be
written and read by this module. The following types are supported:
None, integers, long integers, floating point numbers, strings, Unicode
objects, tuples, lists, sets, dictionaries, and code objects, where it
should be understood that tuples, lists and dictionaries are only
supported as long as the values contained therein are themselves
supported; and recursive lists and dictionaries should not be written
(they will cause infinite loops).

Variables:

version -- indicates the format that the module uses. Version 0 is the
    historical format, version 1 (added in Python 2.4) shares interned
    strings and version 2 (added in Python 2.5) uses a binary format for
    floating point numbers. (New in version 2.4)

Functions:

dump() -- write value to a file
load() -- read value from a file
dumps() -- write value to a string
loads() -- read value from a string
"""
# no imports

# Variables with simple values

version = 2

# functions

def dump(value, file, version=None): # real signature unknown; restored from __doc__
    """
    dump(value, file[, version])
    
    Write the value on the open file. The value must be a supported type.
    The file must be an open file object such as sys.stdout or returned by
    open() or os.popen(). It must be opened in binary mode ('wb' or 'w+b').
    
    If the value has (or contains an object that has) an unsupported type, a
    ValueError exception is raised — but garbage data will also be written
    to the file. The object will not be properly read back by load()
    
    New in version 2.4: The version argument indicates the data format that
    dump should use.
    """
    pass

def dumps(value, version=None): # real signature unknown; restored from __doc__
    """
    dumps(value[, version])
    
    Return the string that would be written to a file by dump(value, file).
    The value must be a supported type. Raise a ValueError exception if
    value has (or contains an object that has) an unsupported type.
    
    New in version 2.4: The version argument indicates the data format that
    dumps should use.
    """
    pass

def load(file): # real signature unknown; restored from __doc__
    """
    load(file)
    
    Read one value from the open file and return it. If no valid value is
    read (e.g. because the data has a different Python version’s
    incompatible marshal format), raise EOFError, ValueError or TypeError.
    The file must be an open file object opened in binary mode ('rb' or
    'r+b').
    
    Note: If an object containing an unsupported type was marshalled with
    dump(), load() will substitute None for the unmarshallable type.
    """
    pass

def loads(string): # real signature unknown; restored from __doc__
    """
    loads(string)
    
    Convert the string to a value. If no valid value is found, raise
    EOFError, ValueError or TypeError. Extra characters in the string are
    ignored.
    """
    pass

# no classes

# encoding: utf-8
# module cStringIO
# from (built-in)
# by generator 1.147
"""
A simple fast partial StringIO replacement.

This module provides a simple useful replacement for
the StringIO module that is written in C.  It does not provide the
full generality of StringIO, but it provides enough for most
applications and is especially useful in conjunction with the
pickle module.

Usage:

  from cStringIO import StringIO

  an_output_stream=StringIO()
  an_output_stream.write(some_stuff)
  ...
  value=an_output_stream.getvalue()

  an_input_stream=StringIO(a_string)
  spam=an_input_stream.readline()
  spam=an_input_stream.read(5)
  an_input_stream.seek(0)           # OK, start over
  spam=an_input_stream.read()       # and read it all
  
If someone else wants to provide a more complete implementation,
go for it. :-)  

cStringIO.c,v 1.29 1999/06/15 14:10:27 jim Exp
"""
# no imports

# functions

def StringIO(s=None): # real signature unknown; restored from __doc__
    """ StringIO([s]) -- Return a StringIO-like stream for reading or writing """
    pass

# classes

class InputType(object):
    """ Simple type for treating strings as input file streams """
    def close(self): # real signature unknown; restored from __doc__
        """ close(): explicitly release resources held. """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(): does nothing. """
        pass

    def getvalue(self, use_pos=None): # real signature unknown; restored from __doc__
        """
        getvalue([use_pos]) -- Get the string value.
        If use_pos is specified and is a true value, then the string returned
        will include only the text up to the current file position.
        """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """ isatty(): always returns 0 """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, s=None): # real signature unknown; restored from __doc__
        """ read([s]) -- Read s characters, or the rest of the string """
        pass

    def readline(self): # real signature unknown; restored from __doc__
        """ readline() -- Read one line """
        pass

    def readlines(self): # real signature unknown; restored from __doc__
        """ readlines() -- Read all lines """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset() -- Reset the file position to the beginning """
        pass

    def seek(self, position, mode=0): # known case of cStringIO.InputType.seek
        """
        seek(position)       -- set the current position
        seek(position, mode) -- mode 0: absolute; 1: relative; 2: relative to EOF
        """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """ tell() -- get the current position. """
        pass

    def truncate(self): # real signature unknown; restored from __doc__
        """ truncate(): truncate the file at the current position. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed"""



class OutputType(object):
    """ Simple type for output to strings. """
    def close(self): # real signature unknown; restored from __doc__
        """ close(): explicitly release resources held. """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(): does nothing. """
        pass

    def getvalue(self, use_pos=None): # real signature unknown; restored from __doc__
        """
        getvalue([use_pos]) -- Get the string value.
        If use_pos is specified and is a true value, then the string returned
        will include only the text up to the current file position.
        """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """ isatty(): always returns 0 """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, s=None): # real signature unknown; restored from __doc__
        """ read([s]) -- Read s characters, or the rest of the string """
        pass

    def readline(self): # real signature unknown; restored from __doc__
        """ readline() -- Read one line """
        pass

    def readlines(self): # real signature unknown; restored from __doc__
        """ readlines() -- Read all lines """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset() -- Reset the file position to the beginning """
        pass

    def seek(self, position, mode=0): # known case of cStringIO.OutputType.seek
        """
        seek(position)       -- set the current position
        seek(position, mode) -- mode 0: absolute; 1: relative; 2: relative to EOF
        """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """ tell() -- get the current position. """
        pass

    def truncate(self): # real signature unknown; restored from __doc__
        """ truncate(): truncate the file at the current position. """
        pass

    def write(self, s): # real signature unknown; restored from __doc__
        """
        write(s) -- Write a string to the file
        
        Note (hack:) writing None resets the buffer
        """
        pass

    def writelines(self, sequence_of_strings): # real signature unknown; restored from __doc__
        """
        writelines(sequence_of_strings) -> None.  Write the strings to the file.
        
        Note that newlines are not added.  The sequence can be any iterable object
        producing strings. This is equivalent to calling write() for each string.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed"""

    softspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """flag indicating that a space needs to be printed; used by print"""



# variables with complex values

cStringIO_CAPI = None # (!) real value is '<capsule object "cStringIO.cStringIO_CAPI" at 0x00000000018C4090>'


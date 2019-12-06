# encoding: utf-8
# module pandas.util._move
# from C:\Python27\lib\site-packages\pandas\util\_move.pyd
# by generator 1.147
# no doc
# no imports

# functions

def move_into_mutable_buffer(*args, **kwargs): # real signature unknown
    """
    Moves a bytes object that is about to be destroyed into a mutable buffer
    without copying the data.
    
    Parameters
    ----------
    bytes_rvalue : bytes with 1 refcount.
        The bytes object that you want to move into a mutable buffer. This
        cannot be a named object. It must only have a single reference.
    
    Returns
    -------
    buf : stolenbuf
        An object that supports the buffer protocol which can give a mutable
        view of the data that was previously owned by ``bytes_rvalue``.
    
    Raises
    ------
    BadMove
        Raised when a move is attempted on an object with more than one
        reference.
    
    Notes
    -----
    If you want to use this function you are probably wrong.
    
    Warning: Do not call this function through *unpacking. This can
    potentially trick the reference checks which may allow you to get a
    mutable reference to a shared string!
    """
    pass

# classes

class BadMove(Exception):
    """
    Exception used to indicate that a move was attempted on a value with
    more than a single reference.
    
    Parameters
    ----------
    data : any
        The data which was passed to ``move_into_mutable_buffer``.
    
    See Also
    --------
    pandas.util._move.move_into_mutable_buffer
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class stolenbuf(object):
    """ A buffer that is wrapping a stolen bytes object's buffer. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass



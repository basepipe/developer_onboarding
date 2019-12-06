# encoding: utf-8
# module _tkinter
# from (pre-generated)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ALL_EVENTS = -3

DONT_WAIT = 2

EXCEPTION = 8

FILE_EVENTS = 8

IDLE_EVENTS = 32

READABLE = 2

TCL_VERSION = '8.5'

TIMER_EVENTS = 16

TK_VERSION = '8.5'

WINDOW_EVENTS = 4

WRITABLE = 4

# functions

def create(*args, **kwargs): # real signature unknown
    pass

def createtimerhandler(*args, **kwargs): # real signature unknown
    pass

def dooneevent(*args, **kwargs): # real signature unknown
    pass

def getbusywaitinterval(): # real signature unknown; restored from __doc__
    """
    getbusywaitinterval() -> int
    
    Return the current busy-wait interval between successive
    calls to Tcl_DoOneEvent in a threaded Python interpreter.
    """
    return 0

def mainloop(*args, **kwargs): # real signature unknown
    pass

def quit(*args, **kwargs): # real signature unknown
    pass

def setbusywaitinterval(n): # real signature unknown; restored from __doc__
    """
    setbusywaitinterval(n) -> None
    
    Set the busy-wait interval in milliseconds between successive
    calls to Tcl_DoOneEvent in a threaded Python interpreter.
    It should be set to a divisor of the maximum time between
    frames in an animation.
    """
    pass

def _flatten(*args, **kwargs): # real signature unknown
    pass

# classes

class TclError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Tcl_Obj(object):
    # no doc
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __unicode__(self, *args, **kwargs): # real signature unknown
        """ convert argument to unicode """
        pass

    string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the string representation of this object, either as string or Unicode"""

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of the Tcl type"""



class TkappType(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class TkttType(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass



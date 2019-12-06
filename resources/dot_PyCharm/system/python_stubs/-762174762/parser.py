# encoding: utf-8
# module parser
# from (built-in)
# by generator 1.147
""" This is an interface to Python's internal parser. """
# no imports

# Variables with simple values

__copyright__ = 'Copyright 1995-1996 by Virginia Polytechnic Institute & State\nUniversity, Blacksburg, Virginia, USA, and Fred L. Drake, Jr., Reston,\nVirginia, USA.  Portions copyright 1991-1995 by Stichting Mathematisch\nCentrum, Amsterdam, The Netherlands.'

__version__ = '0.5'

# functions

def ast2list(*args, **kwargs): # real signature unknown
    """ Creates a list-tree representation of an ST. """
    pass

def ast2tuple(*args, **kwargs): # real signature unknown
    """ Creates a tuple-tree representation of an ST. """
    pass

def compileast(*args, **kwargs): # real signature unknown
    """ Compiles an ST object into a code object. """
    pass

def compilest(*args, **kwargs): # real signature unknown
    """ Compiles an ST object into a code object. """
    pass

def expr(*args, **kwargs): # real signature unknown
    """ Creates an ST object from an expression. """
    pass

def isexpr(*args, **kwargs): # real signature unknown
    """ Determines if an ST object was created from an expression. """
    pass

def issuite(*args, **kwargs): # real signature unknown
    """ Determines if an ST object was created from a suite. """
    pass

def sequence2ast(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def sequence2st(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def st2list(*args, **kwargs): # real signature unknown
    """ Creates a list-tree representation of an ST. """
    pass

def st2tuple(*args, **kwargs): # real signature unknown
    """ Creates a tuple-tree representation of an ST. """
    pass

def suite(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a suite. """
    pass

def tuple2ast(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def tuple2st(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def _pickler(*args, **kwargs): # real signature unknown
    """ Returns the pickle magic to allow ST objects to be pickled. """
    pass

# classes

class STType(object):
    """ Intermediate representation of a Python parse tree. """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Compile this ST object into a code object. """
        pass

    def isexpr(self, *args, **kwargs): # real signature unknown
        """ Determines if this ST object was created from an expression. """
        pass

    def issuite(self, *args, **kwargs): # real signature unknown
        """ Determines if this ST object was created from a suite. """
        pass

    def tolist(self, *args, **kwargs): # real signature unknown
        """ Creates a list-tree representation of this ST. """
        pass

    def totuple(self, *args, **kwargs): # real signature unknown
        """ Creates a tuple-tree representation of this ST. """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass


ASTType = STType


class ParserError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




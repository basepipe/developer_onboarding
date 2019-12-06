# encoding: utf-8
# module _elementtree
# from (pre-generated)
# by generator 1.147
# no doc

# imports
import xml.etree.ElementPath as ElementPath # C:\BuildAgent\system\.persistent_cache\pythons\python27\lib\xml\etree\ElementPath.pyc
import xml.etree.ElementTree as __xml_etree_ElementTree


# Variables with simple values

VERSION = '1.0.6'

__version__ = '1.0.6'

# functions

def Comment(*args, **kwargs): # real signature unknown
    pass

def dump(elem): # reliably restored by inspect
    # no doc
    pass

def Element(*args, **kwargs): # real signature unknown
    pass

def fromstring(text): # reliably restored by inspect
    # no doc
    pass

def fromstringlist(sequence, parser=None): # reliably restored by inspect
    # no doc
    pass

def iselement(element): # reliably restored by inspect
    # no doc
    pass

def parse(source, parser=None): # reliably restored by inspect
    # no doc
    pass

def PI(*args, **kwargs): # real signature unknown
    pass

def ProcessingInstruction(*args, **kwargs): # real signature unknown
    pass

def register_namespace(prefix, uri): # reliably restored by inspect
    # no doc
    pass

def SubElement(*args, **kwargs): # real signature unknown
    pass

def tostring(element, encoding=None, method=None): # reliably restored by inspect
    # no doc
    pass

def tostringlist(element, encoding=None, method=None): # reliably restored by inspect
    # no doc
    pass

def TreeBuilder(*args, **kwargs): # real signature unknown
    pass

def XML(text): # reliably restored by inspect
    # no doc
    pass

def XMLID(text): # reliably restored by inspect
    # no doc
    pass

def XMLParser(*args, **kwargs): # real signature unknown
    pass

def XMLTreeBuilder(*args, **kwargs): # real signature unknown
    pass

# classes

class ElementTree(__xml_etree_ElementTree.ElementTree):
    # no doc
    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class iterparse(object):
    # no doc
    def next(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    root = None
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '__builtin__', '__weakref__': <attribute '__weakref__' of 'iterparse' objects>, 'next': <function next at 0x00000000016ADF28>, '__iter__': <function __iter__ at 0x00000000016ADF98>, '__dict__': <attribute '__dict__' of 'iterparse' objects>, 'root': None, '__doc__': None, '__init__': <function __init__ at 0x00000000016ADEB8>})"


class ParseError(SyntaxError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QName(object):
    # no doc
    def __cmp__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "dict_proxy({'__module__': 'xml.etree.ElementTree', '__str__': <function __str__ at 0x00000000016AB2E8>, '__cmp__': <function __cmp__ at 0x00000000016AB3C8>, '__dict__': <attribute '__dict__' of 'QName' objects>, '__hash__': <function __hash__ at 0x00000000016AB358>, '__weakref__': <attribute '__weakref__' of 'QName' objects>, '__doc__': None, '__init__': <function __init__ at 0x00000000016AB278>})"



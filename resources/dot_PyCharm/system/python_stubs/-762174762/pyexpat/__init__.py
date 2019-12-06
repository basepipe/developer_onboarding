# encoding: utf-8
# module pyexpat
# from (pre-generated)
# by generator 1.147
""" Python wrapper for Expat parser. """

# imports
import pyexpat.errors as errors # <module 'pyexpat.errors' (built-in)>
import pyexpat.model as model # <module 'pyexpat.model' (built-in)>

# Variables with simple values

EXPAT_VERSION = 'expat_2.2.6'

native_encoding = 'UTF-8'

XML_PARAM_ENTITY_PARSING_ALWAYS = 2
XML_PARAM_ENTITY_PARSING_NEVER = 0

XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE = 1

__version__ = '2.7.16'

# functions

def ErrorString(errno): # real signature unknown; restored from __doc__
    """
    ErrorString(errno) -> string
    Returns string error for given number.
    """
    return ""

def ParserCreate(encoding=None, namespace_separator=None): # real signature unknown; restored from __doc__
    """
    ParserCreate([encoding[, namespace_separator]]) -> parser
    Return a new XML parser object.
    """
    pass

# classes

class ExpatError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



error = ExpatError


class XMLParserType(object):
    """ XML parser """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

expat_CAPI = None # (!) real value is '<capsule object "pyexpat.expat_CAPI" at 0x00000000020753C0>'

features = [
    (
        'sizeof(XML_Char)',
        1,
    ),
    (
        'sizeof(XML_LChar)',
        1,
    ),
    (
        'XML_DTD',
        0,
    ),
    (
        'XML_CONTEXT_BYTES',
        1024,
    ),
    (
        'XML_NS',
        0,
    ),
]

version_info = (
    2,
    2,
    6,
)


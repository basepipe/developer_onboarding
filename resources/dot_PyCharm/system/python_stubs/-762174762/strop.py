# encoding: utf-8
# module strop
# from (built-in)
# by generator 1.147
"""
Common string manipulations, optimized for speed.

Always use "import string" rather than referencing
this module directly.
"""
# no imports

# Variables with simple values

lowercase = 'abcdefghijklmnopqrstuvwxyz'

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

whitespace = '\t\n\x0b\x0c\r '

# functions

def atof(s): # real signature unknown; restored from __doc__
    """
    atof(s) -> float
    
    Return the floating point number represented by the string s.
    """
    return 0.0

def atoi(s, base=None): # real signature unknown; restored from __doc__
    """
    atoi(s [,base]) -> int
    
    Return the integer represented by the string s in the given
    base, which defaults to 10.  The string s must consist of one
    or more digits, possibly preceded by a sign.  If base is 0, it
    is chosen from the leading characters of s, 0 for octal, 0x or
    0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
    accepted.
    """
    return 0

def atol(s, base=None): # real signature unknown; restored from __doc__
    """
    atol(s [,base]) -> long
    
    Return the long integer represented by the string s in the
    given base, which defaults to 10.  The string s must consist
    of one or more digits, possibly preceded by a sign.  If base
    is 0, it is chosen from the leading characters of s, 0 for
    octal, 0x or 0X for hexadecimal.  If base is 16, a preceding
    0x or 0X is accepted.  A trailing L or l is not accepted,
    unless base is 0.
    """
    return 0

def capitalize(s): # real signature unknown; restored from __doc__
    """
    capitalize(s) -> string
    
    Return a copy of the string s with only its first character
    capitalized.
    """
    return ""

def count(s, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    count(s, sub[, start[, end]]) -> int
    
    Return the number of occurrences of substring sub in string
    s[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
    """
    return 0

def expandtabs(string, tabsize=None): # real signature unknown; restored from __doc__
    """
    expandtabs(string, [tabsize]) -> string
    
    Expand tabs in a string, i.e. replace them by one or more spaces,
    depending on the current column and the given tab size (default 8).
    The column number is reset to zero after each newline occurring in the
    string.  This doesn't understand other non-printing characters.
    """
    return ""

def find(s, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    find(s, sub [,start [,end]]) -> in
    
    Return the lowest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.
    """
    pass

def join(p_list, sep=None): # real signature unknown; restored from __doc__
    """
    join(list [,sep]) -> string
    joinfields(list [,sep]) -> string
    
    Return a string composed of the words in list, with
    intervening occurrences of sep.  Sep defaults to a single
    space.
    
    (join and joinfields are synonymous)
    """
    return ""

def joinfields(p_list, sep=None): # real signature unknown; restored from __doc__
    """
    join(list [,sep]) -> string
    joinfields(list [,sep]) -> string
    
    Return a string composed of the words in list, with
    intervening occurrences of sep.  Sep defaults to a single
    space.
    
    (join and joinfields are synonymous)
    """
    return ""

def lower(s): # real signature unknown; restored from __doc__
    """
    lower(s) -> string
    
    Return a copy of the string s converted to lowercase.
    """
    return ""

def lstrip(s): # real signature unknown; restored from __doc__
    """
    lstrip(s) -> string
    
    Return a copy of the string s with leading whitespace removed.
    """
    return ""

def maketrans(frm, to): # real signature unknown; restored from __doc__
    """
    maketrans(frm, to) -> string
    
    Return a translation table (a string of 256 bytes long)
    suitable for use in string.translate.  The strings frm and to
    must be of the same length.
    """
    return ""

def replace(p_str, old, new, maxsplit=None): # real signature unknown; restored from __doc__
    """
    replace (str, old, new[, maxsplit]) -> string
    
    Return a copy of string str with all occurrences of substring
    old replaced by new. If the optional argument maxsplit is
    given, only the first maxsplit occurrences are replaced.
    """
    return ""

def rfind(s, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    rfind(s, sub [,start [,end]]) -> int
    
    Return the highest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.
    """
    return 0

def rstrip(s): # real signature unknown; restored from __doc__
    """
    rstrip(s) -> string
    
    Return a copy of the string s with trailing whitespace removed.
    """
    return ""

def split(s, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
    """
    split(s [,sep [,maxsplit]]) -> list of strings
    splitfields(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is nonzero, splits into at most
    maxsplit words.  If sep is not specified, any whitespace string
    is a separator.  Maxsplit defaults to 0.
    
    (split and splitfields are synonymous)
    """
    return []

def splitfields(s, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
    """
    split(s [,sep [,maxsplit]]) -> list of strings
    splitfields(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is nonzero, splits into at most
    maxsplit words.  If sep is not specified, any whitespace string
    is a separator.  Maxsplit defaults to 0.
    
    (split and splitfields are synonymous)
    """
    return []

def strip(s): # real signature unknown; restored from __doc__
    """
    strip(s) -> string
    
    Return a copy of the string s with leading and trailing
    whitespace removed.
    """
    return ""

def swapcase(s): # real signature unknown; restored from __doc__
    """
    swapcase(s) -> string
    
    Return a copy of the string s with upper case characters
    converted to lowercase and vice versa.
    """
    return ""

def translate(s, table, deletechars=None): # real signature unknown; restored from __doc__
    """
    translate(s,table [,deletechars]) -> string
    
    Return a copy of the string s, where all characters occurring
    in the optional argument deletechars are removed, and the
    remaining characters have been mapped through the given
    translation table, which must be a string of length 256.
    """
    return ""

def upper(s): # real signature unknown; restored from __doc__
    """
    upper(s) -> string
    
    Return a copy of the string s converted to uppercase.
    """
    return ""

# no classes

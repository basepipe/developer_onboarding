# encoding: utf-8
# module unicodedata
# from (pre-generated)
# by generator 1.147
"""
This module provides access to the Unicode Character Database which
defines character properties for all Unicode characters. The data in
this database is based on the UnicodeData.txt file version
5.2.0 which is publically available from ftp://ftp.unicode.org/.

The module uses the same names and symbols as defined by the
UnicodeData File Format 5.2.0 (see
http://www.unicode.org/reports/tr44/tr44-4.html).
"""
# no imports

# Variables with simple values

unidata_version = '5.2.0'

# functions

def bidirectional(unichr): # real signature unknown; restored from __doc__
    """
    bidirectional(unichr)
    
    Returns the bidirectional class assigned to the Unicode character
    unichr as string. If no such value is defined, an empty string is
    returned.
    """
    pass

def category(unichr): # real signature unknown; restored from __doc__
    """
    category(unichr)
    
    Returns the general category assigned to the Unicode character
    unichr as string.
    """
    pass

def combining(unichr): # real signature unknown; restored from __doc__
    """
    combining(unichr)
    
    Returns the canonical combining class assigned to the Unicode
    character unichr as integer. Returns 0 if no combining class is
    defined.
    """
    pass

def decimal(unichr, default=None): # real signature unknown; restored from __doc__
    """
    decimal(unichr[, default])
    
    Returns the decimal value assigned to the Unicode character unichr
    as integer. If no such value is defined, default is returned, or, if
    not given, ValueError is raised.
    """
    pass

def decomposition(unichr): # real signature unknown; restored from __doc__
    """
    decomposition(unichr)
    
    Returns the character decomposition mapping assigned to the Unicode
    character unichr as string. An empty string is returned in case no
    such mapping is defined.
    """
    pass

def digit(unichr, default=None): # real signature unknown; restored from __doc__
    """
    digit(unichr[, default])
    
    Returns the digit value assigned to the Unicode character unichr as
    integer. If no such value is defined, default is returned, or, if
    not given, ValueError is raised.
    """
    pass

def east_asian_width(unichr): # real signature unknown; restored from __doc__
    """
    east_asian_width(unichr)
    
    Returns the east asian width assigned to the Unicode character
    unichr as string.
    """
    pass

def lookup(name): # real signature unknown; restored from __doc__
    """
    lookup(name)
    
    Look up character by name.  If a character with the
    given name is found, return the corresponding Unicode
    character.  If not found, KeyError is raised.
    """
    pass

def mirrored(unichr): # real signature unknown; restored from __doc__
    """
    mirrored(unichr)
    
    Returns the mirrored property assigned to the Unicode character
    unichr as integer. Returns 1 if the character has been identified as
    a "mirrored" character in bidirectional text, 0 otherwise.
    """
    pass

def name(unichr, default=None): # real signature unknown; restored from __doc__
    """
    name(unichr[, default])
    Returns the name assigned to the Unicode character unichr as a
    string. If no name is defined, default is returned, or, if not
    given, ValueError is raised.
    """
    pass

def normalize(form, unistr): # real signature unknown; restored from __doc__
    """
    normalize(form, unistr)
    
    Return the normal form 'form' for the Unicode string unistr.  Valid
    values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
    """
    pass

def numeric(unichr, default=None): # real signature unknown; restored from __doc__
    """
    numeric(unichr[, default])
    
    Returns the numeric value assigned to the Unicode character unichr
    as float. If no such value is defined, default is returned, or, if
    not given, ValueError is raised.
    """
    pass

# classes

class UCD(object):
    # no doc
    def bidirectional(self, unichr): # real signature unknown; restored from __doc__
        """
        bidirectional(unichr)
        
        Returns the bidirectional class assigned to the Unicode character
        unichr as string. If no such value is defined, an empty string is
        returned.
        """
        pass

    def category(self, unichr): # real signature unknown; restored from __doc__
        """
        category(unichr)
        
        Returns the general category assigned to the Unicode character
        unichr as string.
        """
        pass

    def combining(self, unichr): # real signature unknown; restored from __doc__
        """
        combining(unichr)
        
        Returns the canonical combining class assigned to the Unicode
        character unichr as integer. Returns 0 if no combining class is
        defined.
        """
        pass

    def decimal(self, unichr, default=None): # real signature unknown; restored from __doc__
        """
        decimal(unichr[, default])
        
        Returns the decimal value assigned to the Unicode character unichr
        as integer. If no such value is defined, default is returned, or, if
        not given, ValueError is raised.
        """
        pass

    def decomposition(self, unichr): # real signature unknown; restored from __doc__
        """
        decomposition(unichr)
        
        Returns the character decomposition mapping assigned to the Unicode
        character unichr as string. An empty string is returned in case no
        such mapping is defined.
        """
        pass

    def digit(self, unichr, default=None): # real signature unknown; restored from __doc__
        """
        digit(unichr[, default])
        
        Returns the digit value assigned to the Unicode character unichr as
        integer. If no such value is defined, default is returned, or, if
        not given, ValueError is raised.
        """
        pass

    def east_asian_width(self, unichr): # real signature unknown; restored from __doc__
        """
        east_asian_width(unichr)
        
        Returns the east asian width assigned to the Unicode character
        unichr as string.
        """
        pass

    def lookup(self, name): # real signature unknown; restored from __doc__
        """
        lookup(name)
        
        Look up character by name.  If a character with the
        given name is found, return the corresponding Unicode
        character.  If not found, KeyError is raised.
        """
        pass

    def mirrored(self, unichr): # real signature unknown; restored from __doc__
        """
        mirrored(unichr)
        
        Returns the mirrored property assigned to the Unicode character
        unichr as integer. Returns 1 if the character has been identified as
        a "mirrored" character in bidirectional text, 0 otherwise.
        """
        pass

    def name(self, unichr, default=None): # real signature unknown; restored from __doc__
        """
        name(unichr[, default])
        Returns the name assigned to the Unicode character unichr as a
        string. If no name is defined, default is returned, or, if not
        given, ValueError is raised.
        """
        pass

    def normalize(self, form, unistr): # real signature unknown; restored from __doc__
        """
        normalize(form, unistr)
        
        Return the normal form 'form' for the Unicode string unistr.  Valid
        values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
        """
        pass

    def numeric(self, unichr, default=None): # real signature unknown; restored from __doc__
        """
        numeric(unichr[, default])
        
        Returns the numeric value assigned to the Unicode character unichr
        as float. If no such value is defined, default is returned, or, if
        not given, ValueError is raised.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    unidata_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

ucd_3_2_0 = None # (!) real value is '<unicodedata.UCD object at 0x0000000001CF1580>'

ucnhash_CAPI = None # (!) real value is '<capsule object "unicodedata.ucnhash_CAPI" at 0x0000000001CFADE0>'


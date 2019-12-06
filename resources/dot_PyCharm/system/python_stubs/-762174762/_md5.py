# encoding: utf-8
# module _md5
# from (built-in)
# by generator 1.147
"""
This module implements the interface to RSA's MD5 message digest
algorithm (see also Internet RFC 1321). Its use is quite
straightforward: use the new() to create an md5 object. You can now
feed this object with arbitrary strings using the update() method, and
at any point you can ask it for the digest (a strong kind of 128-bit
checksum, a.k.a. ``fingerprint'') of the concatenation of the strings
fed to it so far using the digest() method.

Functions:

new([arg]) -- return a new md5 object, initialized with arg if provided
md5([arg]) -- DEPRECATED, same as new, but for compatibility

Special Objects:

MD5Type -- type object for md5 objects
"""
# no imports

# Variables with simple values

digest_size = 16

# functions

def new(arg=None): # real signature unknown; restored from __doc__
    """
    new([arg]) -> md5 object
    
    Return a new md5 object. If arg is present, the method call update(arg)
    is made.
    """
    pass

# classes

class MD5Type(object):
    """
    An md5 represents the object used to calculate the MD5 checksum of a
    string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current md5 object
    """
    def copy(self): # real signature unknown; restored from __doc__
        """
        copy() -> md5 object
        
        Return a copy (``clone'') of the md5 object.
        """
        pass

    def digest(self): # real signature unknown; restored from __doc__
        """
        digest() -> string
        
        Return the digest of the strings passed to the update() method so
        far. This is a 16-byte string which may contain non-ASCII characters,
        including null bytes.
        """
        return ""

    def hexdigest(self): # real signature unknown; restored from __doc__
        """
        hexdigest() -> string
        
        Like digest(), but returns the digest as a string of hexadecimal digits.
        """
        return ""

    def update(self, arg): # real signature unknown; restored from __doc__
        """
        update (arg)
        
        Update the md5 object with the string arg. Repeated calls are
        equivalent to a single call with the concatenation of all the
        arguments.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digestsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




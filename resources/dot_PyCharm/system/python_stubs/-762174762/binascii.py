# encoding: utf-8
# module binascii
# from (built-in)
# by generator 1.147
""" Conversion between binary data and ASCII """
# no imports

# functions

def a2b_base64(*args, **kwargs): # real signature unknown
    """ (ascii) -> bin. Decode a line of base64 data """
    pass

def a2b_hex(hexstr): # real signature unknown; restored from __doc__
    """
    a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    This function is also available as "unhexlify()"
    """
    pass

def a2b_hqx(*args, **kwargs): # real signature unknown
    """ ascii -> bin, done. Decode .hqx coding """
    pass

def a2b_qp(*args, **kwargs): # real signature unknown
    """ Decode a string of qp-encoded data """
    pass

def a2b_uu(*args, **kwargs): # real signature unknown
    """ (ascii) -> bin. Decode a line of uuencoded data """
    pass

def b2a_base64(*args, **kwargs): # real signature unknown
    """ (bin) -> ascii. Base64-code line of data """
    pass

def b2a_hex(data): # real signature unknown; restored from __doc__
    """
    b2a_hex(data) -> s; Hexadecimal representation of binary data.
    
    This function is also available as "hexlify()".
    """
    pass

def b2a_hqx(*args, **kwargs): # real signature unknown
    """ Encode .hqx data """
    pass

def b2a_qp(data, quotetabs=0, istext=1, header=0): # real signature unknown; restored from __doc__
    """
    b2a_qp(data, quotetabs=0, istext=1, header=0) -> s; 
     Encode a string using quoted-printable encoding. 
    
    On encoding, when istext is set, newlines are not encoded, and white 
    space at end of lines is.  When istext is not set, \r and \n (CR/LF) are 
    both encoded.  When quotetabs is set, space and tabs are encoded.
    """
    pass

def b2a_uu(*args, **kwargs): # real signature unknown
    """ (bin) -> ascii. Uuencode line of data """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """ (data, oldcrc = 0) -> newcrc. Compute CRC-32 incrementally """
    pass

def crc_hqx(*args, **kwargs): # real signature unknown
    """ (data, oldcrc) -> newcrc. Compute CRC-CCITT incrementally """
    pass

def hexlify(data): # known case of binascii.hexlify
    """
    b2a_hex(data) -> s; Hexadecimal representation of binary data.
    
    This function is also available as "hexlify()".
    """
    return ""

def rlecode_hqx(*args, **kwargs): # real signature unknown
    """ Binhex RLE-code binary data """
    pass

def rledecode_hqx(*args, **kwargs): # real signature unknown
    """ Decode hexbin RLE-coded string """
    pass

def unhexlify(hexstr): # known case of binascii.unhexlify
    """
    a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    This function is also available as "unhexlify()"
    """
    return ""

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Incomplete(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




# encoding: utf-8
# module _codecs
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def ascii_decode(*args, **kwargs): # real signature unknown
    pass

def ascii_encode(*args, **kwargs): # real signature unknown
    pass

def charbuffer_encode(*args, **kwargs): # real signature unknown
    pass

def charmap_build(*args, **kwargs): # real signature unknown
    pass

def charmap_decode(*args, **kwargs): # real signature unknown
    pass

def charmap_encode(*args, **kwargs): # real signature unknown
    pass

def decode(obj, encoding=None, errors=None): # real signature unknown; restored from __doc__
    """
    decode(obj, [encoding[,errors]]) -> object
    
    Decodes obj using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a ValueError. Other possible values are 'ignore' and 'replace'
    as well as any other name registered with codecs.register_error that is
    able to handle ValueErrors.
    """
    return object()

def encode(obj, encoding=None, errors=None): # real signature unknown; restored from __doc__
    """
    encode(obj, [encoding[,errors]]) -> object
    
    Encodes obj using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a ValueError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle ValueErrors.
    """
    return object()

def escape_decode(*args, **kwargs): # real signature unknown
    pass

def escape_encode(*args, **kwargs): # real signature unknown
    pass

def latin_1_decode(*args, **kwargs): # real signature unknown
    pass

def latin_1_encode(*args, **kwargs): # real signature unknown
    pass

def lookup(encoding): # real signature unknown; restored from __doc__
    """
    lookup(encoding) -> CodecInfo
    
    Looks up a codec tuple in the Python codec registry and returns
    a CodecInfo object.
    """
    pass

def lookup_error(errors): # real signature unknown; restored from __doc__
    """
    lookup_error(errors) -> handler
    
    Return the error handler for the specified error handling name
    or raise a LookupError, if no handler exists under this name.
    """
    pass

def mbcs_decode(*args, **kwargs): # real signature unknown
    pass

def mbcs_encode(*args, **kwargs): # real signature unknown
    pass

def raw_unicode_escape_decode(*args, **kwargs): # real signature unknown
    pass

def raw_unicode_escape_encode(*args, **kwargs): # real signature unknown
    pass

def readbuffer_encode(*args, **kwargs): # real signature unknown
    pass

def register(search_function): # real signature unknown; restored from __doc__
    """
    register(search_function)
    
    Register a codec search function. Search functions are expected to take
    one argument, the encoding name in all lower case letters, and return
    a tuple of functions (encoder, decoder, stream_reader, stream_writer)
    (or a CodecInfo object).
    """
    pass

def register_error(errors, handler): # real signature unknown; restored from __doc__
    """
    register_error(errors, handler)
    
    Register the specified error handler under the name
    errors. handler must be a callable object, that
    will be called with an exception instance containing
    information about the location of the encoding/decoding
    error and must return a (replacement, new position) tuple.
    """
    pass

def unicode_escape_decode(*args, **kwargs): # real signature unknown
    pass

def unicode_escape_encode(*args, **kwargs): # real signature unknown
    pass

def unicode_internal_decode(*args, **kwargs): # real signature unknown
    pass

def unicode_internal_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_be_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_be_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_ex_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_le_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_le_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_be_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_be_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_ex_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_le_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_le_encode(*args, **kwargs): # real signature unknown
    pass

def utf_7_decode(*args, **kwargs): # real signature unknown
    pass

def utf_7_encode(*args, **kwargs): # real signature unknown
    pass

def utf_8_decode(*args, **kwargs): # real signature unknown
    pass

def utf_8_encode(*args, **kwargs): # real signature unknown
    pass

# no classes

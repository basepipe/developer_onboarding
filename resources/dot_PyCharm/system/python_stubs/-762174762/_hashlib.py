# encoding: utf-8
# module _hashlib
# from (pre-generated)
# by generator 1.147
# no doc
# no imports

# functions

def new(*args, **kwargs): # real signature unknown
    """
    Return a new hash object using the named algorithm.
    An optional string argument may be provided and will be
    automatically hashed.
    
    The MD5 and SHA1 algorithms are always supported.
    """
    pass

def openssl_md5(*args, **kwargs): # real signature unknown
    """ Returns a md5 hash object; optionally initialized with a string """
    pass

def openssl_sha1(*args, **kwargs): # real signature unknown
    """ Returns a sha1 hash object; optionally initialized with a string """
    pass

def openssl_sha224(*args, **kwargs): # real signature unknown
    """ Returns a sha224 hash object; optionally initialized with a string """
    pass

def openssl_sha256(*args, **kwargs): # real signature unknown
    """ Returns a sha256 hash object; optionally initialized with a string """
    pass

def openssl_sha384(*args, **kwargs): # real signature unknown
    """ Returns a sha384 hash object; optionally initialized with a string """
    pass

def openssl_sha512(*args, **kwargs): # real signature unknown
    """ Returns a sha512 hash object; optionally initialized with a string """
    pass

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None): # real signature unknown; restored from __doc__
    """
    pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key
    
    Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as
    pseudorandom function.
    """
    pass

# no classes
# variables with complex values

openssl_md_meth_names = None # (!) real value is "frozenset(['SHA256', 'SHA512', 'dsaWithSHA', 'md4', 'sha256', 'sha512', 'ripemd160', 'md5', 'whirlpool', 'SHA1', 'SHA224', 'SHA', 'SHA384', 'ecdsa-with-SHA1', 'MD4', 'DSA', 'sha1', 'DSA-SHA', 'sha224', 'dsaEncryption', 'RIPEMD160', 'sha', 'MD5', 'sha384'])"


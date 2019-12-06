# encoding: utf-8
# module _ssl
# from (pre-generated)
# by generator 1.147
"""
Implementation module for SSL socket operations.  See the socket module
for documentation.
"""

# imports
import socket as __socket
import ssl as __ssl


# Variables with simple values

ALERT_DESCRIPTION_ACCESS_DENIED = 49

ALERT_DESCRIPTION_BAD_CERTIFICATE = 42

ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE = 114

ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE = 113

ALERT_DESCRIPTION_BAD_RECORD_MAC = 20

ALERT_DESCRIPTION_CERTIFICATE_EXPIRED = 45
ALERT_DESCRIPTION_CERTIFICATE_REVOKED = 44
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN = 46
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE = 111

ALERT_DESCRIPTION_CLOSE_NOTIFY = 0

ALERT_DESCRIPTION_DECODE_ERROR = 50

ALERT_DESCRIPTION_DECOMPRESSION_FAILURE = 30

ALERT_DESCRIPTION_DECRYPT_ERROR = 51

ALERT_DESCRIPTION_HANDSHAKE_FAILURE = 40

ALERT_DESCRIPTION_ILLEGAL_PARAMETER = 47

ALERT_DESCRIPTION_INSUFFICIENT_SECURITY = 71

ALERT_DESCRIPTION_INTERNAL_ERROR = 80

ALERT_DESCRIPTION_NO_RENEGOTIATION = 100

ALERT_DESCRIPTION_PROTOCOL_VERSION = 70

ALERT_DESCRIPTION_RECORD_OVERFLOW = 22

ALERT_DESCRIPTION_UNEXPECTED_MESSAGE = 10

ALERT_DESCRIPTION_UNKNOWN_CA = 48

ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY = 115

ALERT_DESCRIPTION_UNRECOGNIZED_NAME = 112

ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE = 43
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION = 110

ALERT_DESCRIPTION_USER_CANCELLED = 90

CERT_NONE = 0
CERT_OPTIONAL = 1
CERT_REQUIRED = 2

HAS_ALPN = True
HAS_ECDH = True
HAS_NPN = True
HAS_SNI = True

HAS_TLSv1_3 = False

HAS_TLS_UNIQUE = True

OPENSSL_VERSION = 'OpenSSL 1.0.2q  20 Nov 2018'

OPENSSL_VERSION_NUMBER = 268443935L

OP_ALL = -2147482625

OP_CIPHER_SERVER_PREFERENCE = 4194304

OP_NO_COMPRESSION = 131072
OP_NO_SSLv2 = 16777216
OP_NO_SSLv3 = 33554432
OP_NO_TLSv1 = 67108864

OP_NO_TLSv1_1 = 268435456
OP_NO_TLSv1_2 = 134217728
OP_NO_TLSv1_3 = 0

OP_SINGLE_DH_USE = 1048576

OP_SINGLE_ECDH_USE = 524288

PROTOCOL_SSLv23 = 2
PROTOCOL_SSLv3 = 1
PROTOCOL_TLS = 2
PROTOCOL_TLSv1 = 3

PROTOCOL_TLSv1_1 = 4
PROTOCOL_TLSv1_2 = 5

SSL_ERROR_EOF = 8

SSL_ERROR_INVALID_ERROR_CODE = 10

SSL_ERROR_SSL = 1
SSL_ERROR_SYSCALL = 5

SSL_ERROR_WANT_CONNECT = 7
SSL_ERROR_WANT_READ = 2
SSL_ERROR_WANT_WRITE = 3

SSL_ERROR_WANT_X509_LOOKUP = 4

SSL_ERROR_ZERO_RETURN = 6

VERIFY_CRL_CHECK_CHAIN = 12
VERIFY_CRL_CHECK_LEAF = 4

VERIFY_DEFAULT = 0

VERIFY_X509_STRICT = 32

VERIFY_X509_TRUSTED_FIRST = 32768

# functions

def enum_certificates(store_name): # real signature unknown; restored from __doc__
    """
    enum_certificates(store_name) -> []
    
    Retrieve certificates from Windows' cert store. store_name may be one of
    'CA', 'ROOT' or 'MY'. The system may provide more cert storages, too.
    The function returns a list of (bytes, encoding_type, trust) tuples. The
    encoding_type flag can be interpreted with X509_ASN_ENCODING or
    PKCS_7_ASN_ENCODING. The trust setting is either a set of OIDs or the
    boolean True.
    """
    pass

def enum_crls(store_name): # real signature unknown; restored from __doc__
    """
    enum_crls(store_name) -> []
    
    Retrieve CRLs from Windows' cert store. store_name may be one of
    'CA', 'ROOT' or 'MY'. The system may provide more cert storages, too.
    The function returns a list of (bytes, encoding_type) tuples. The
    encoding_type flag can be interpreted with X509_ASN_ENCODING or
    PKCS_7_ASN_ENCODING.
    """
    pass

def get_default_verify_paths(): # real signature unknown; restored from __doc__
    """
    get_default_verify_paths() -> tuple
    
    Return search paths and environment vars that are used by SSLContext's
    set_default_verify_paths() to load default CAs. The values are
    'cert_file_env', 'cert_file', 'cert_dir_env', 'cert_dir'.
    """
    return ()

def nid2obj(nid): # real signature unknown; restored from __doc__
    """
    nid2obj(nid) -> (nid, shortname, longname, oid)
    
    Lookup NID, short name, long name and OID of an ASN1_OBJECT by NID.
    """
    pass

def RAND_add(string, entropy): # real signature unknown; restored from __doc__
    """
    RAND_add(string, entropy)
    
    Mix string into the OpenSSL PRNG state.  entropy (a float) is a lower
    bound on the entropy contained in string.  See RFC 1750.
    """
    pass

def RAND_egd(path): # real signature unknown; restored from __doc__
    """
    RAND_egd(path) -> bytes
    
    Queries the entropy gather daemon (EGD) on the socket named by 'path'.
    Returns number of bytes read.  Raises SSLError if connection to EGD
    fails or if it does not provide enough data to seed PRNG.
    """
    return ""

def RAND_status(): # real signature unknown; restored from __doc__
    """
    RAND_status() -> 0 or 1
    
    Returns 1 if the OpenSSL PRNG has been seeded with enough data and 0 if not.
    It is necessary to seed the PRNG with RAND_add() on some platforms before
    using the ssl() function.
    """
    pass

def txt2obj(txt, name=False): # real signature unknown; restored from __doc__
    """
    txt2obj(txt, name=False) -> (nid, shortname, longname, oid)
    
    Lookup NID, short name, long name and OID of an ASN1_OBJECT. By default
    objects are looked up by OID. With name=True short and long name are also
    matched.
    """
    pass

def _test_decode_cert(*args, **kwargs): # real signature unknown
    pass

# classes

class SSLError(__socket.error):
    """ An error occurred in the SSL implementation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SSLEOFError(__ssl.SSLError):
    """ SSL/TLS connection terminated abruptly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SSLSyscallError(__ssl.SSLError):
    """ System error when attempting SSL operation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SSLWantReadError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to read more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SSLWantWriteError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to write more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SSLZeroReturnError(__ssl.SSLError):
    """ SSL/TLS session closed cleanly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class _SSLContext(object):
    # no doc
    def cert_store_stats(self): # real signature unknown; restored from __doc__
        """
        cert_store_stats() -> {'crl': int, 'x509_ca': int, 'x509': int}
        
        Returns quantities of loaded X.509 certificates. X.509 certificates with a
        CA extension and certificate revocation lists inside the context's cert
        store.
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        pass

    def get_ca_certs(self, binary_form=False): # real signature unknown; restored from __doc__
        """
        get_ca_certs(binary_form=False) -> list of loaded certificate
        
        Returns a list of dicts with information of loaded CA certs. If the
        optional argument is True, returns a DER-encoded copy of the CA certificate.
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        return []

    def load_cert_chain(self, *args, **kwargs): # real signature unknown
        pass

    def load_dh_params(self, *args, **kwargs): # real signature unknown
        pass

    def load_verify_locations(self, *args, **kwargs): # real signature unknown
        pass

    def session_stats(self, *args, **kwargs): # real signature unknown
        pass

    def set_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_verify_paths(self, *args, **kwargs): # real signature unknown
        pass

    def set_ecdh_curve(self, *args, **kwargs): # real signature unknown
        pass

    def set_servername_callback(self, method): # real signature unknown; restored from __doc__
        """
        set_servername_callback(method)
        
        This sets a callback that will be called when a server name is provided by
        the SSL/TLS client in the SNI extension.
        
        If the argument is None then the callback is disabled. The method is called
        with the SSLSocket, the server name as a string, and the SSLContext object.
        See RFC 6066 for details of the SNI extension.
        """
        pass

    def _set_alpn_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def _set_npn_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def _wrap_socket(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    check_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _SSLSocket(object):
    # no doc
    def cipher(self, *args, **kwargs): # real signature unknown
        pass

    def compression(self, *args, **kwargs): # real signature unknown
        pass

    def do_handshake(self, *args, **kwargs): # real signature unknown
        pass

    def peer_certificate(self, der=False): # real signature unknown; restored from __doc__
        """
        peer_certificate([der=False]) -> certificate
        
        Returns the certificate for the peer.  If no certificate was provided,
        returns None.  If a certificate was provided, but not validated, returns
        an empty dictionary.  Otherwise returns a dict containing information
        about the peer certificate.
        
        If the optional argument is True, returns a DER-encoded copy of the
        peer certificate, or None if no certificate was provided.  This will
        return the certificate even if it wasn't validated.
        """
        pass

    def pending(self): # real signature unknown; restored from __doc__
        """
        pending() -> count
        
        Returns the number of already decrypted bytes available for read,
        pending on the connection.
        """
        pass

    def read(self, len=None): # real signature unknown; restored from __doc__
        """
        read([len]) -> string
        
        Read up to len bytes from the SSL socket.
        """
        return ""

    def selected_alpn_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def selected_npn_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def shutdown(self, s): # real signature unknown; restored from __doc__
        """
        shutdown(s) -> socket
        
        Does the SSL shutdown handshake with the remote end, and returns
        the underlying socket object.
        """
        pass

    def tls_unique_cb(self): # real signature unknown; restored from __doc__
        """
        tls_unique_cb() -> bytes
        
        Returns the 'tls-unique' channel binding data, as defined by RFC 5929.
        
        If the TLS handshake is not yet complete, None is returned
        """
        return ""

    def version(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, s): # real signature unknown; restored from __doc__
        """
        write(s) -> len
        
        Writes the string s into the SSL object.  Returns the number
        of bytes written.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_setter_context(ctx)
This changes the context associated with the SSLSocket. This is typically
used from within a callback function set by the set_servername_callback
on the SSLContext to change the certificate information associated with the
SSLSocket before the cryptographic exchange handshake messages
"""



# variables with complex values

err_codes_to_names = {
    (
        9,
        100,
    ): 
        u'BAD_BASE64_DECODE'
    ,
    (
        9,
        101,
    ): 
        u'BAD_DECRYPT'
    ,
    (
        9,
        102,
    ): 
        u'BAD_END_LINE'
    ,
    (
        9,
        103,
    ): 
        u'BAD_IV_CHARS'
    ,
    (
        9,
        104,
    ): 
        u'BAD_PASSWORD_READ'
    ,
    (
        9,
        105,
    ): 
        u'NOT_DEK_INFO'
    ,
    (
        9,
        106,
    ): 
        u'NOT_ENCRYPTED'
    ,
    (
        9,
        107,
    ): 
        u'NOT_PROC_TYPE'
    ,
    (
        9,
        108,
    ): 
        u'NO_START_LINE'
    ,
    (
        9,
        109,
    ): 
        u'PROBLEMS_GETTING_PASSWORD'
    ,
    (
        9,
        110,
    ): 
        u'PUBLIC_KEY_NO_RSA'
    ,
    (
        9,
        111,
    ): 
        u'READ_KEY'
    ,
    (
        9,
        112,
    ): 
        u'SHORT_HEADER'
    ,
    (
        9,
        113,
    ): 
        u'UNSUPPORTED_CIPHER'
    ,
    (
        9,
        114,
    ): 
        u'UNSUPPORTED_ENCRYPTION'
    ,
    (
        9,
        115,
    ): 
        u'ERROR_CONVERTING_PRIVATE_KEY'
    ,
    (
        9,
        116,
    ): 
        u'BAD_MAGIC_NUMBER'
    ,
    (
        9,
        117,
    ): 
        u'BAD_VERSION_NUMBER'
    ,
    (
        9,
        118,
    ): 
        u'BIO_WRITE_FAILURE'
    ,
    (
        9,
        119,
    ): 
        u'EXPECTING_PRIVATE_KEY_BLOB'
    ,
    (
        9,
        120,
    ): 
        u'EXPECTING_PUBLIC_KEY_BLOB'
    ,
    (
        9,
        121,
    ): 
        u'INCONSISTENT_HEADER'
    ,
    (
        9,
        122,
    ): 
        u'KEYBLOB_HEADER_PARSE_ERROR'
    ,
    (
        9,
        123,
    ): 
        u'KEYBLOB_TOO_SHORT'
    ,
    (
        9,
        124,
    ): 
        u'PVK_DATA_TOO_SHORT'
    ,
    (
        9,
        125,
    ): 
        u'PVK_TOO_SHORT'
    ,
    (
        9,
        126,
    ): 
        u'UNSUPPORTED_KEY_COMPONENTS'
    ,
    (
        9,
        127,
    ): 
        u'CIPHER_IS_NULL'
    ,
    (
        11,
        100,
    ): 
        u'BAD_X509_FILETYPE'
    ,
    (
        11,
        101,
    ): 
        u'CERT_ALREADY_IN_HASH_TABLE'
    ,
    (
        11,
        102,
    ): 
        u'ERR_ASN1_LIB'
    ,
    (
        11,
        103,
    ): 
        u'LOADING_CERT_DIR'
    ,
    (
        11,
        104,
    ): 
        u'LOADING_DEFAULTS'
    ,
    (
        11,
        105,
    ): 
        u'NO_CERT_SET_FOR_US_TO_VERIFY'
    ,
    (
        11,
        106,
    ): 
        u'SHOULD_RETRY'
    ,
    (
        11,
        107,
    ): 
        u'UNABLE_TO_FIND_PARAMETERS_IN_CHAIN'
    ,
    (
        11,
        108,
    ): 
        u'UNABLE_TO_GET_CERTS_PUBLIC_KEY'
    ,
    (
        11,
        109,
    ): 
        u'UNKNOWN_NID'
    ,
    (
        11,
        110,
    ): 
        u'AKID_MISMATCH'
    ,
    (
        11,
        111,
    ): 
        u'UNSUPPORTED_ALGORITHM'
    ,
    (
        11,
        112,
    ): 
        u'WRONG_LOOKUP_TYPE'
    ,
    (
        11,
        113,
    ): 
        u'INVALID_DIRECTORY'
    ,
    (
        11,
        114,
    ): 
        u'CANT_CHECK_DH_KEY'
    ,
    (
        11,
        115,
    ): 
        u'KEY_TYPE_MISMATCH'
    ,
    (
        11,
        116,
    ): 
        u'KEY_VALUES_MISMATCH'
    ,
    (
        11,
        117,
    ): 
        u'UNKNOWN_KEY_TYPE'
    ,
    (
        11,
        118,
    ): 
        u'BASE64_DECODE_ERROR'
    ,
    (
        11,
        119,
    ): 
        u'INVALID_FIELD_NAME'
    ,
    (
        11,
        120,
    ): 
        u'UNKNOWN_TRUST_ID'
    ,
    (
        11,
        121,
    ): 
        u'UNKNOWN_PURPOSE_ID'
    ,
    (
        11,
        122,
    ): 
        u'WRONG_TYPE'
    ,
    (
        11,
        123,
    ): 
        u'INVALID_TRUST'
    ,
    (
        11,
        124,
    ): 
        u'METHOD_NOT_SUPPORTED'
    ,
    (
        11,
        125,
    ): 
        u'PUBLIC_KEY_DECODE_ERROR'
    ,
    (
        11,
        126,
    ): 
        u'PUBLIC_KEY_ENCODE_ERROR'
    ,
    (
        11,
        127,
    ): 
        u'CRL_ALREADY_DELTA'
    ,
    (
        11,
        128,
    ): 
        u'IDP_MISMATCH'
    ,
    (
        11,
        129,
    ): 
        u'ISSUER_MISMATCH'
    ,
    (
        11,
        130,
    ): 
        u'NO_CRL_NUMBER'
    ,
    (
        11,
        131,
    ): 
        u'CRL_VERIFY_FAILURE'
    ,
    (
        11,
        132,
    ): 
        u'NEWER_CRL_NOT_NEWER'
    ,
    (
        20,
        100,
    ): 
        u'APP_DATA_IN_HANDSHAKE'
    ,
    (
        20,
        101,
    ): 
        u'BAD_ALERT_RECORD'
    ,
    (
        20,
        102,
    ): 
        u'BAD_AUTHENTICATION_TYPE'
    ,
    (
        20,
        103,
    ): 
        u'BAD_CHANGE_CIPHER_SPEC'
    ,
    (
        20,
        104,
    ): 
        u'BAD_CHECKSUM'
    ,
    (
        20,
        105,
    ): 
        u'BAD_HELLO_REQUEST'
    ,
    (
        20,
        106,
    ): 
        u'BAD_DATA_RETURNED_BY_CALLBACK'
    ,
    (
        20,
        107,
    ): 
        u'BAD_DECOMPRESSION'
    ,
    (
        20,
        108,
    ): 
        u'BAD_DH_G_LENGTH'
    ,
    (
        20,
        109,
    ): 
        u'BAD_DH_PUB_KEY_LENGTH'
    ,
    (
        20,
        110,
    ): 
        u'BAD_DH_P_LENGTH'
    ,
    (
        20,
        111,
    ): 
        u'BAD_DIGEST_LENGTH'
    ,
    (
        20,
        112,
    ): 
        u'BAD_DSA_SIGNATURE'
    ,
    (
        20,
        113,
    ): 
        u'BAD_MAC_DECODE'
    ,
    (
        20,
        114,
    ): 
        u'BAD_MESSAGE_TYPE'
    ,
    (
        20,
        115,
    ): 
        u'BAD_PACKET_LENGTH'
    ,
    (
        20,
        116,
    ): 
        u'BAD_PROTOCOL_VERSION_NUMBER'
    ,
    (
        20,
        117,
    ): 
        u'BAD_RESPONSE_ARGUMENT'
    ,
    (
        20,
        118,
    ): 
        u'BAD_RSA_DECRYPT'
    ,
    (
        20,
        119,
    ): 
        u'BAD_RSA_ENCRYPT'
    ,
    (
        20,
        120,
    ): 
        u'BAD_RSA_E_LENGTH'
    ,
    (
        20,
        121,
    ): 
        u'BAD_RSA_MODULUS_LENGTH'
    ,
    (
        20,
        122,
    ): 
        u'BAD_RSA_SIGNATURE'
    ,
    (
        20,
        123,
    ): 
        u'BAD_SIGNATURE'
    ,
    (
        20,
        124,
    ): 
        u'BAD_SSL_FILETYPE'
    ,
    (
        20,
        125,
    ): 
        u'BAD_SSL_SESSION_ID_LENGTH'
    ,
    (
        20,
        126,
    ): 
        u'BAD_STATE'
    ,
    (
        20,
        127,
    ): 
        u'BAD_WRITE_RETRY'
    ,
    (
        20,
        128,
    ): 
        u'BIO_NOT_SET'
    ,
    (
        20,
        129,
    ): 
        u'BLOCK_CIPHER_PAD_IS_WRONG'
    ,
    (
        20,
        130,
    ): 
        u'BN_LIB'
    ,
    (
        20,
        131,
    ): 
        u'CA_DN_LENGTH_MISMATCH'
    ,
    (
        20,
        132,
    ): 
        u'CA_DN_TOO_LONG'
    ,
    (
        20,
        133,
    ): 
        u'CCS_RECEIVED_EARLY'
    ,
    (
        20,
        134,
    ): 
        u'CERTIFICATE_VERIFY_FAILED'
    ,
    (
        20,
        135,
    ): 
        u'CERT_LENGTH_MISMATCH'
    ,
    (
        20,
        136,
    ): 
        u'CHALLENGE_IS_DIFFERENT'
    ,
    (
        20,
        137,
    ): 
        u'CIPHER_CODE_WRONG_LENGTH'
    ,
    (
        20,
        138,
    ): 
        u'CIPHER_OR_HASH_UNAVAILABLE'
    ,
    (
        20,
        139,
    ): 
        u'CIPHER_TABLE_SRC_ERROR'
    ,
    (
        20,
        140,
    ): 
        u'COMPRESSED_LENGTH_TOO_LONG'
    ,
    (
        20,
        141,
    ): 
        u'COMPRESSION_FAILURE'
    ,
    (
        20,
        142,
    ): 
        u'COMPRESSION_LIBRARY_ERROR'
    ,
    (
        20,
        143,
    ): 
        u'CONNECTION_ID_IS_DIFFERENT'
    ,
    (
        20,
        144,
    ): 
        u'CONNECTION_TYPE_NOT_SET'
    ,
    (
        20,
        145,
    ): 
        u'DATA_BETWEEN_CCS_AND_FINISHED'
    ,
    (
        20,
        146,
    ): 
        u'DATA_LENGTH_TOO_LONG'
    ,
    (
        20,
        147,
    ): 
        u'DECRYPTION_FAILED'
    ,
    (
        20,
        148,
    ): 
        u'DH_PUBLIC_VALUE_LENGTH_IS_WRONG'
    ,
    (
        20,
        149,
    ): 
        u'DIGEST_CHECK_FAILED'
    ,
    (
        20,
        150,
    ): 
        u'ENCRYPTED_LENGTH_TOO_LONG'
    ,
    (
        20,
        151,
    ): 
        u'ERROR_IN_RECEIVED_CIPHER_LIST'
    ,
    (
        20,
        152,
    ): 
        u'EXCESSIVE_MESSAGE_SIZE'
    ,
    (
        20,
        153,
    ): 
        u'EXTRA_DATA_IN_MESSAGE'
    ,
    (
        20,
        154,
    ): 
        u'GOT_A_FIN_BEFORE_A_CCS'
    ,
    (
        20,
        155,
    ): 
        u'HTTPS_PROXY_REQUEST'
    ,
    (
        20,
        156,
    ): 
        u'HTTP_REQUEST'
    ,
    (
        20,
        157,
    ): 
        u'TLS_INVALID_ECPOINTFORMAT_LIST'
    ,
    (
        20,
        158,
    ): 
        u'INVALID_CHALLENGE_LENGTH'
    ,
    (
        20,
        159,
    ): 
        u'LENGTH_MISMATCH'
    ,
    (
        20,
        160,
    ): 
        u'LENGTH_TOO_SHORT'
    ,
    (
        20,
        161,
    ): 
        u'LIBRARY_HAS_NO_CIPHERS'
    ,
    (
        20,
        162,
    ): 
        u'MISSING_DH_DSA_CERT'
    ,
    (
        20,
        163,
    ): 
        u'MISSING_DH_KEY'
    ,
    (
        20,
        164,
    ): 
        u'MISSING_DH_RSA_CERT'
    ,
    (
        20,
        165,
    ): 
        u'MISSING_DSA_SIGNING_CERT'
    ,
    (
        20,
        166,
    ): 
        u'MISSING_EXPORT_TMP_DH_KEY'
    ,
    (
        20,
        167,
    ): 
        u'MISSING_EXPORT_TMP_RSA_KEY'
    ,
    (
        20,
        168,
    ): 
        u'MISSING_RSA_CERTIFICATE'
    ,
    (
        20,
        169,
    ): 
        u'MISSING_RSA_ENCRYPTING_CERT'
    ,
    (
        20,
        170,
    ): 
        u'MISSING_RSA_SIGNING_CERT'
    ,
    (
        20,
        171,
    ): 
        u'MISSING_TMP_DH_KEY'
    ,
    (
        20,
        172,
    ): 
        u'MISSING_TMP_RSA_KEY'
    ,
    (
        20,
        173,
    ): 
        u'MISSING_TMP_RSA_PKEY'
    ,
    (
        20,
        174,
    ): 
        u'MISSING_VERIFY_MESSAGE'
    ,
    (
        20,
        175,
    ): 
        u'NON_SSLV2_INITIAL_PACKET'
    ,
    (
        20,
        176,
    ): 
        u'NO_CERTIFICATES_RETURNED'
    ,
    (
        20,
        177,
    ): 
        u'NO_CERTIFICATE_ASSIGNED'
    ,
    (
        20,
        178,
    ): 
        u'NO_CERTIFICATE_RETURNED'
    ,
    (
        20,
        179,
    ): 
        u'NO_CERTIFICATE_SET'
    ,
    (
        20,
        180,
    ): 
        u'NO_CERTIFICATE_SPECIFIED'
    ,
    (
        20,
        181,
    ): 
        u'NO_CIPHERS_AVAILABLE'
    ,
    (
        20,
        182,
    ): 
        u'NO_CIPHERS_PASSED'
    ,
    (
        20,
        183,
    ): 
        u'NO_CIPHERS_SPECIFIED'
    ,
    (
        20,
        184,
    ): 
        u'NO_CIPHER_LIST'
    ,
    (
        20,
        185,
    ): 
        u'NO_CIPHER_MATCH'
    ,
    (
        20,
        186,
    ): 
        u'NO_CLIENT_CERT_RECEIVED'
    ,
    (
        20,
        187,
    ): 
        u'NO_COMPRESSION_SPECIFIED'
    ,
    (
        20,
        188,
    ): 
        u'NO_METHOD_SPECIFIED'
    ,
    (
        20,
        189,
    ): 
        u'NO_PRIVATEKEY'
    ,
    (
        20,
        190,
    ): 
        u'NO_PRIVATE_KEY_ASSIGNED'
    ,
    (
        20,
        191,
    ): 
        u'NO_PROTOCOLS_AVAILABLE'
    ,
    (
        20,
        192,
    ): 
        u'NO_PUBLICKEY'
    ,
    (
        20,
        193,
    ): 
        u'NO_SHARED_CIPHER'
    ,
    (
        20,
        194,
    ): 
        u'NO_VERIFY_CALLBACK'
    ,
    (
        20,
        195,
    ): 
        u'NULL_SSL_CTX'
    ,
    (
        20,
        196,
    ): 
        u'NULL_SSL_METHOD_PASSED'
    ,
    (
        20,
        197,
    ): 
        u'OLD_SESSION_CIPHER_NOT_RETURNED'
    ,
    (
        20,
        198,
    ): 
        u'PACKET_LENGTH_TOO_LONG'
    ,
    (
        20,
        199,
    ): 
        u'PEER_DID_NOT_RETURN_A_CERTIFICATE'
    ,
    (
        20,
        200,
    ): 
        u'PEER_ERROR'
    ,
    (
        20,
        201,
    ): 
        u'PEER_ERROR_CERTIFICATE'
    ,
    (
        20,
        202,
    ): 
        u'PEER_ERROR_NO_CERTIFICATE'
    ,
    (
        20,
        203,
    ): 
        u'PEER_ERROR_NO_CIPHER'
    ,
    (
        20,
        204,
    ): 
        u'PEER_ERROR_UNSUPPORTED_CERTIFICATE_TYPE'
    ,
    (
        20,
        205,
    ): 
        u'PRE_MAC_LENGTH_TOO_LONG'
    ,
    (
        20,
        206,
    ): 
        u'PROBLEMS_MAPPING_CIPHER_FUNCTIONS'
    ,
    (
        20,
        207,
    ): 
        u'PROTOCOL_IS_SHUTDOWN'
    ,
    (
        20,
        208,
    ): 
        u'PUBLIC_KEY_ENCRYPT_ERROR'
    ,
    (
        20,
        209,
    ): 
        u'PUBLIC_KEY_IS_NOT_RSA'
    ,
    (
        20,
        210,
    ): 
        u'PUBLIC_KEY_NOT_RSA'
    ,
    (
        20,
        211,
    ): 
        u'READ_BIO_NOT_SET'
    ,
    (
        20,
        212,
    ): 
        u'READ_WRONG_PACKET_TYPE'
    ,
    (
        20,
        213,
    ): 
        u'RECORD_LENGTH_MISMATCH'
    ,
    (
        20,
        214,
    ): 
        u'RECORD_TOO_LARGE'
    ,
    (
        20,
        215,
    ): 
        u'REQUIRED_CIPHER_MISSING'
    ,
    (
        20,
        216,
    ): 
        u'REUSE_CERT_LENGTH_NOT_ZERO'
    ,
    (
        20,
        217,
    ): 
        u'REUSE_CERT_TYPE_NOT_ZERO'
    ,
    (
        20,
        218,
    ): 
        u'REUSE_CIPHER_LIST_NOT_ZERO'
    ,
    (
        20,
        219,
    ): 
        u'SHORT_READ'
    ,
    (
        20,
        220,
    ): 
        u'SIGNATURE_FOR_NON_SIGNING_CERTIFICATE'
    ,
    (
        20,
        221,
    ): 
        u'SSL23_DOING_SESSION_ID_REUSE'
    ,
    (
        20,
        222,
    ): 
        u'SSL3_SESSION_ID_TOO_SHORT'
    ,
    (
        20,
        223,
    ): 
        u'PSK_IDENTITY_NOT_FOUND'
    ,
    (
        20,
        224,
    ): 
        u'PSK_NO_CLIENT_CB'
    ,
    (
        20,
        225,
    ): 
        u'PSK_NO_SERVER_CB'
    ,
    (
        20,
        226,
    ): 
        u'CLIENTHELLO_TLSEXT'
    ,
    (
        20,
        227,
    ): 
        u'PARSE_TLSEXT'
    ,
    (
        20,
        228,
    ): 
        u'SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION'
    ,
    (
        20,
        229,
    ): 
        u'SSL_HANDSHAKE_FAILURE'
    ,
    (
        20,
        230,
    ): 
        u'SSL_LIBRARY_HAS_NO_CIPHERS'
    ,
    (
        20,
        231,
    ): 
        u'SSL_SESSION_ID_IS_DIFFERENT'
    ,
    (
        20,
        232,
    ): 
        u'TLS_CLIENT_CERT_REQ_WITH_ANON_CIPHER'
    ,
    (
        20,
        233,
    ): 
        u'TLS_PEER_DID_NOT_RESPOND_WITH_CERTIFICATE_LIST'
    ,
    (
        20,
        234,
    ): 
        u'TLS_RSA_ENCRYPTED_VALUE_LENGTH_IS_WRONG'
    ,
    (
        20,
        235,
    ): 
        u'TRIED_TO_USE_UNSUPPORTED_CIPHER'
    ,
    (
        20,
        236,
    ): 
        u'UNABLE_TO_DECODE_DH_CERTS'
    ,
    (
        20,
        237,
    ): 
        u'UNABLE_TO_EXTRACT_PUBLIC_KEY'
    ,
    (
        20,
        238,
    ): 
        u'UNABLE_TO_FIND_DH_PARAMETERS'
    ,
    (
        20,
        239,
    ): 
        u'UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS'
    ,
    (
        20,
        240,
    ): 
        u'UNABLE_TO_FIND_SSL_METHOD'
    ,
    (
        20,
        241,
    ): 
        u'UNABLE_TO_LOAD_SSL2_MD5_ROUTINES'
    ,
    (
        20,
        242,
    ): 
        u'UNABLE_TO_LOAD_SSL3_MD5_ROUTINES'
    ,
    (
        20,
        243,
    ): 
        u'UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES'
    ,
    (
        20,
        244,
    ): 
        u'UNEXPECTED_MESSAGE'
    ,
    (
        20,
        245,
    ): 
        u'UNEXPECTED_RECORD'
    ,
    (
        20,
        246,
    ): 
        u'UNKNOWN_ALERT_TYPE'
    ,
    (
        20,
        247,
    ): 
        u'UNKNOWN_CERTIFICATE_TYPE'
    ,
    (
        20,
        248,
    ): 
        u'UNKNOWN_CIPHER_RETURNED'
    ,
    (
        20,
        249,
    ): 
        u'UNKNOWN_CIPHER_TYPE'
    ,
    (
        20,
        250,
    ): 
        u'UNKNOWN_KEY_EXCHANGE_TYPE'
    ,
    (
        20,
        251,
    ): 
        u'UNKNOWN_PKEY_TYPE'
    ,
    (
        20,
        252,
    ): 
        u'UNKNOWN_PROTOCOL'
    ,
    (
        20,
        253,
    ): 
        u'UNKNOWN_REMOTE_ERROR_TYPE'
    ,
    (
        20,
        254,
    ): 
        u'UNKNOWN_SSL_VERSION'
    ,
    (
        20,
        255,
    ): 
        u'UNKNOWN_STATE'
    ,
    (
        20,
        256,
    ): 
        u'UNSUPPORTED_CIPHER'
    ,
    (
        20,
        257,
    ): 
        u'UNSUPPORTED_COMPRESSION_ALGORITHM'
    ,
    (
        20,
        258,
    ): 
        u'UNSUPPORTED_PROTOCOL'
    ,
    (
        20,
        259,
    ): 
        u'UNSUPPORTED_SSL_VERSION'
    ,
    (
        20,
        260,
    ): 
        u'WRITE_BIO_NOT_SET'
    ,
    (
        20,
        261,
    ): 
        u'WRONG_CIPHER_RETURNED'
    ,
    (
        20,
        262,
    ): 
        u'WRONG_MESSAGE_TYPE'
    ,
    (
        20,
        263,
    ): 
        u'WRONG_NUMBER_OF_KEY_BITS'
    ,
    (
        20,
        264,
    ): 
        u'WRONG_SIGNATURE_LENGTH'
    ,
    (
        20,
        265,
    ): 
        u'WRONG_SIGNATURE_SIZE'
    ,
    (
        20,
        266,
    ): 
        u'WRONG_SSL_VERSION'
    ,
    (
        20,
        267,
    ): 
        u'WRONG_VERSION_NUMBER'
    ,
    (
        20,
        268,
    ): 
        u'X509_LIB'
    ,
    (
        20,
        269,
    ): 
        u'X509_VERIFICATION_SETUP_PROBLEMS'
    ,
    (
        20,
        270,
    ): 
        u'PATH_TOO_LONG'
    ,
    (
        20,
        271,
    ): 
        u'BAD_LENGTH'
    ,
    (
        20,
        272,
    ): 
        u'ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT'
    ,
    (
        20,
        273,
    ): 
        u'SSL_SESSION_ID_CONTEXT_TOO_LONG'
    ,
    (
        20,
        274,
    ): 
        u'LIBRARY_BUG'
    ,
    (
        20,
        275,
    ): 
        u'SERVERHELLO_TLSEXT'
    ,
    (
        20,
        276,
    ): 
        u'UNINITIALIZED'
    ,
    (
        20,
        277,
    ): 
        u'SESSION_ID_CONTEXT_UNINITIALIZED'
    ,
    (
        20,
        278,
    ): 
        u'INVALID_PURPOSE'
    ,
    (
        20,
        279,
    ): 
        u'INVALID_TRUST'
    ,
    (
        20,
        280,
    ): 
        u'INVALID_COMMAND'
    ,
    (
        20,
        281,
    ): 
        u'DECRYPTION_FAILED_OR_BAD_RECORD_MAC'
    ,
    (
        20,
        282,
    ): 
        u'ERROR_GENERATING_TMP_RSA_KEY'
    ,
    (
        20,
        283,
    ): 
        u'ILLEGAL_PADDING'
    ,
    (
        20,
        284,
    ): 
        u'KEY_ARG_TOO_LONG'
    ,
    (
        20,
        285,
    ): 
        u'KRB5'
    ,
    (
        20,
        286,
    ): 
        u'KRB5_C_CC_PRINC'
    ,
    (
        20,
        287,
    ): 
        u'KRB5_C_GET_CRED'
    ,
    (
        20,
        288,
    ): 
        u'KRB5_C_INIT'
    ,
    (
        20,
        289,
    ): 
        u'KRB5_C_MK_REQ'
    ,
    (
        20,
        290,
    ): 
        u'KRB5_S_BAD_TICKET'
    ,
    (
        20,
        291,
    ): 
        u'KRB5_S_INIT'
    ,
    (
        20,
        292,
    ): 
        u'KRB5_S_RD_REQ'
    ,
    (
        20,
        293,
    ): 
        u'KRB5_S_TKT_EXPIRED'
    ,
    (
        20,
        294,
    ): 
        u'KRB5_S_TKT_NYV'
    ,
    (
        20,
        295,
    ): 
        u'KRB5_S_TKT_SKEW'
    ,
    (
        20,
        296,
    ): 
        u'MESSAGE_TOO_LONG'
    ,
    (
        20,
        297,
    ): 
        u'ONLY_TLS_ALLOWED_IN_FIPS_MODE'
    ,
    (
        20,
        298,
    ): 
        u'RECORD_TOO_SMALL'
    ,
    (
        20,
        299,
    ): 
        u'SSL2_CONNECTION_ID_TOO_LONG'
    ,
    (
        20,
        300,
    ): 
        u'SSL3_SESSION_ID_TOO_LONG'
    ,
    (
        20,
        301,
    ): 
        u'SSL_SESSION_ID_CALLBACK_FAILED'
    ,
    (
        20,
        302,
    ): 
        u'SSL_SESSION_ID_CONFLICT'
    ,
    (
        20,
        303,
    ): 
        u'SSL_SESSION_ID_HAS_BAD_LENGTH'
    ,
    (
        20,
        304,
    ): 
        u'BAD_ECC_CERT'
    ,
    (
        20,
        305,
    ): 
        u'BAD_ECDSA_SIGNATURE'
    ,
    (
        20,
        306,
    ): 
        u'BAD_ECPOINT'
    ,
    (
        20,
        307,
    ): 
        u'COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE'
    ,
    (
        20,
        308,
    ): 
        u'COOKIE_MISMATCH'
    ,
    (
        20,
        309,
    ): 
        u'DUPLICATE_COMPRESSION_ID'
    ,
    (
        20,
        310,
    ): 
        u'ECGROUP_TOO_LARGE_FOR_CIPHER'
    ,
    (
        20,
        311,
    ): 
        u'MISSING_TMP_ECDH_KEY'
    ,
    (
        20,
        312,
    ): 
        u'READ_TIMEOUT_EXPIRED'
    ,
    (
        20,
        313,
    ): 
        u'UNABLE_TO_DECODE_ECDH_CERTS'
    ,
    (
        20,
        314,
    ): 
        u'UNABLE_TO_FIND_ECDH_PARAMETERS'
    ,
    (
        20,
        315,
    ): 
        u'UNSUPPORTED_ELLIPTIC_CURVE'
    ,
    (
        20,
        316,
    ): 
        u'BAD_PSK_IDENTITY_HINT_LENGTH'
    ,
    (
        20,
        317,
    ): 
        u'ECC_CERT_NOT_FOR_KEY_AGREEMENT'
    ,
    (
        20,
        318,
    ): 
        u'ECC_CERT_NOT_FOR_SIGNING'
    ,
    (
        20,
        319,
    ): 
        u'SSL3_EXT_INVALID_SERVERNAME'
    ,
    (
        20,
        320,
    ): 
        u'SSL3_EXT_INVALID_SERVERNAME_TYPE'
    ,
    (
        20,
        321,
    ): 
        u'SSL3_EXT_INVALID_ECPOINTFORMAT'
    ,
    (
        20,
        322,
    ): 
        u'ECC_CERT_SHOULD_HAVE_RSA_SIGNATURE'
    ,
    (
        20,
        323,
    ): 
        u'ECC_CERT_SHOULD_HAVE_SHA1_SIGNATURE'
    ,
    (
        20,
        324,
    ): 
        u'NO_REQUIRED_DIGEST'
    ,
    (
        20,
        325,
    ): 
        u'INVALID_TICKET_KEYS_LENGTH'
    ,
    (
        20,
        326,
    ): 
        u'UNSUPPORTED_DIGEST_TYPE'
    ,
    (
        20,
        327,
    ): 
        u'OPAQUE_PRF_INPUT_TOO_LONG'
    ,
    (
        20,
        328,
    ): 
        u'INVALID_STATUS_RESPONSE'
    ,
    (
        20,
        329,
    ): 
        u'UNSUPPORTED_STATUS_TYPE'
    ,
    (
        20,
        330,
    ): 
        u'NO_GOST_CERTIFICATE_SENT_BY_PEER'
    ,
    (
        20,
        331,
    ): 
        u'NO_CLIENT_CERT_METHOD'
    ,
    (
        20,
        332,
    ): 
        u'BAD_HANDSHAKE_LENGTH'
    ,
    (
        20,
        333,
    ): 
        u'BAD_MAC_LENGTH'
    ,
    (
        20,
        334,
    ): 
        u'DTLS_MESSAGE_TOO_BIG'
    ,
    (
        20,
        335,
    ): 
        u'RENEGOTIATE_EXT_TOO_LONG'
    ,
    (
        20,
        336,
    ): 
        u'RENEGOTIATION_ENCODING_ERR'
    ,
    (
        20,
        337,
    ): 
        u'RENEGOTIATION_MISMATCH'
    ,
    (
        20,
        338,
    ): 
        u'UNSAFE_LEGACY_RENEGOTIATION_DISABLED'
    ,
    (
        20,
        339,
    ): 
        u'NO_RENEGOTIATION'
    ,
    (
        20,
        340,
    ): 
        u'INCONSISTENT_COMPRESSION'
    ,
    (
        20,
        341,
    ): 
        u'INVALID_COMPRESSION_ALGORITHM'
    ,
    (
        20,
        342,
    ): 
        u'REQUIRED_COMPRESSSION_ALGORITHM_MISSING'
    ,
    (
        20,
        343,
    ): 
        u'COMPRESSION_DISABLED'
    ,
    (
        20,
        344,
    ): 
        u'OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED'
    ,
    (
        20,
        345,
    ): 
        u'SCSV_RECEIVED_WHEN_RENEGOTIATING'
    ,
    (
        20,
        346,
    ): 
        u'MULTIPLE_SGC_RESTARTS'
    ,
    (
        20,
        347,
    ): 
        u'BAD_SRP_A_LENGTH'
    ,
    (
        20,
        348,
    ): 
        u'BAD_SRP_B_LENGTH'
    ,
    (
        20,
        349,
    ): 
        u'BAD_SRP_G_LENGTH'
    ,
    (
        20,
        350,
    ): 
        u'BAD_SRP_N_LENGTH'
    ,
    (
        20,
        351,
    ): 
        u'BAD_SRP_S_LENGTH'
    ,
    (
        20,
        352,
    ): 
        u'BAD_SRTP_MKI_VALUE'
    ,
    (
        20,
        353,
    ): 
        u'BAD_SRTP_PROTECTION_PROFILE_LIST'
    ,
    (
        20,
        354,
    ): 
        u'EMPTY_SRTP_PROTECTION_PROFILE_LIST'
    ,
    (
        20,
        355,
    ): 
        u'GOT_NEXT_PROTO_BEFORE_A_CCS'
    ,
    (
        20,
        356,
    ): 
        u'GOT_NEXT_PROTO_WITHOUT_EXTENSION'
    ,
    (
        20,
        357,
    ): 
        u'INVALID_SRP_USERNAME'
    ,
    (
        20,
        358,
    ): 
        u'MISSING_SRP_PARAM'
    ,
    (
        20,
        359,
    ): 
        u'NO_SRTP_PROFILES'
    ,
    (
        20,
        360,
    ): 
        u'SIGNATURE_ALGORITHMS_ERROR'
    ,
    (
        20,
        361,
    ): 
        u'SRP_A_CALC'
    ,
    (
        20,
        362,
    ): 
        u'SRTP_COULD_NOT_ALLOCATE_PROFILES'
    ,
    (
        20,
        363,
    ): 
        u'SRTP_PROTECTION_PROFILE_LIST_TOO_LONG'
    ,
    (
        20,
        364,
    ): 
        u'SRTP_UNKNOWN_PROTECTION_PROFILE'
    ,
    (
        20,
        365,
    ): 
        u'TLS_HEARTBEAT_PEER_DOESNT_ACCEPT'
    ,
    (
        20,
        366,
    ): 
        u'TLS_HEARTBEAT_PENDING'
    ,
    (
        20,
        367,
    ): 
        u'TLS_ILLEGAL_EXPORTER_LABEL'
    ,
    (
        20,
        368,
    ): 
        u'UNKNOWN_DIGEST'
    ,
    (
        20,
        369,
    ): 
        u'USE_SRTP_NOT_NEGOTIATED'
    ,
    (
        20,
        370,
    ): 
        u'WRONG_SIGNATURE_TYPE'
    ,
    (
        20,
        371,
    ): 
        u'BAD_SRP_PARAMETERS'
    ,
    (
        20,
        372,
    ): 
        u'SSL_NEGATIVE_LENGTH'
    ,
    (
        20,
        373,
    ): 
        u'INAPPROPRIATE_FALLBACK'
    ,
    (
        20,
        374,
    ): 
        u'ECDH_REQUIRED_FOR_SUITEB_MODE'
    ,
    (
        20,
        376,
    ): 
        u'NO_SHARED_SIGATURE_ALGORITHMS'
    ,
    (
        20,
        377,
    ): 
        u'CERT_CB_ERROR'
    ,
    (
        20,
        378,
    ): 
        u'WRONG_CURVE'
    ,
    (
        20,
        379,
    ): 
        u'ONLY_TLS_1_2_ALLOWED_IN_SUITEB_MODE'
    ,
    (
        20,
        380,
    ): 
        u'ILLEGAL_SUITEB_DIGEST'
    ,
    (
        20,
        381,
    ): 
        u'MISSING_ECDSA_SIGNING_CERT'
    ,
    (
        20,
        382,
    ): 
        u'MISSING_ECDH_CERT'
    ,
    (
        20,
        383,
    ): 
        u'WRONG_CERTIFICATE_TYPE'
    ,
    (
        20,
        384,
    ): 
        u'BAD_VALUE'
    ,
    (
        20,
        385,
    ): 
        u'INVALID_NULL_CMD_NAME'
    ,
    (
        20,
        386,
    ): 
        u'UNKNOWN_CMD_NAME'
    ,
    (
        20,
        387,
    ): 
        u'ONLY_DTLS_1_2_ALLOWED_IN_SUITEB_MODE'
    ,
    (
        20,
        388,
    ): 
        u'INVALID_SERVERINFO_DATA'
    ,
    (
        20,
        389,
    ): 
        u'NO_PEM_EXTENSIONS'
    ,
    (
        20,
        390,
    ): 
        u'BAD_DATA'
    ,
    (
        20,
        391,
    ): 
        u'PEM_NAME_BAD_PREFIX'
    ,
    (
        20,
        392,
    ): 
        u'PEM_NAME_TOO_SHORT'
    ,
    (
        20,
        396,
    ): 
        u'VERSION_TOO_LOW'
    ,
    (
        20,
        397,
    ): 
        u'CA_KEY_TOO_SMALL'
    ,
    (
        20,
        398,
    ): 
        u'CA_MD_TOO_WEAK'
    ,
    (
        20,
        399,
    ): 
        u'EE_KEY_TOO_SMALL'
    ,
    (
        20,
        1010,
    ): 
        u'SSLV3_ALERT_UNEXPECTED_MESSAGE'
    ,
    (
        20,
        1020,
    ): 
        u'SSLV3_ALERT_BAD_RECORD_MAC'
    ,
    (
        20,
        1021,
    ): 
        u'TLSV1_ALERT_DECRYPTION_FAILED'
    ,
    (
        20,
        1022,
    ): 
        u'TLSV1_ALERT_RECORD_OVERFLOW'
    ,
    (
        20,
        1030,
    ): 
        u'SSLV3_ALERT_DECOMPRESSION_FAILURE'
    ,
    (
        20,
        1040,
    ): 
        u'SSLV3_ALERT_HANDSHAKE_FAILURE'
    ,
    (
        20,
        1041,
    ): 
        u'SSLV3_ALERT_NO_CERTIFICATE'
    ,
    (
        20,
        1042,
    ): 
        u'SSLV3_ALERT_BAD_CERTIFICATE'
    ,
    (
        20,
        1043,
    ): 
        u'SSLV3_ALERT_UNSUPPORTED_CERTIFICATE'
    ,
    (
        20,
        1044,
    ): 
        u'SSLV3_ALERT_CERTIFICATE_REVOKED'
    ,
    (
        20,
        1045,
    ): 
        u'SSLV3_ALERT_CERTIFICATE_EXPIRED'
    ,
    (
        20,
        1046,
    ): 
        u'SSLV3_ALERT_CERTIFICATE_UNKNOWN'
    ,
    (
        20,
        1047,
    ): 
        u'SSLV3_ALERT_ILLEGAL_PARAMETER'
    ,
    (
        20,
        1048,
    ): 
        u'TLSV1_ALERT_UNKNOWN_CA'
    ,
    (
        20,
        1049,
    ): 
        u'TLSV1_ALERT_ACCESS_DENIED'
    ,
    (
        20,
        1050,
    ): 
        u'TLSV1_ALERT_DECODE_ERROR'
    ,
    (
        20,
        1051,
    ): 
        u'TLSV1_ALERT_DECRYPT_ERROR'
    ,
    (
        20,
        1060,
    ): 
        u'TLSV1_ALERT_EXPORT_RESTRICTION'
    ,
    (
        20,
        1070,
    ): 
        u'TLSV1_ALERT_PROTOCOL_VERSION'
    ,
    (
        20,
        1071,
    ): 
        u'TLSV1_ALERT_INSUFFICIENT_SECURITY'
    ,
    (
        20,
        1080,
    ): 
        u'TLSV1_ALERT_INTERNAL_ERROR'
    ,
    (
        20,
        1086,
    ): 
        u'TLSV1_ALERT_INAPPROPRIATE_FALLBACK'
    ,
    (
        20,
        1090,
    ): 
        u'TLSV1_ALERT_USER_CANCELLED'
    ,
    (
        20,
        1100,
    ): 
        u'TLSV1_ALERT_NO_RENEGOTIATION'
    ,
    (
        20,
        1110,
    ): 
        u'TLSV1_UNSUPPORTED_EXTENSION'
    ,
    (
        20,
        1111,
    ): 
        u'TLSV1_CERTIFICATE_UNOBTAINABLE'
    ,
    (
        20,
        1112,
    ): 
        u'TLSV1_UNRECOGNIZED_NAME'
    ,
    (
        20,
        1113,
    ): 
        u'TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE'
    ,
    (
        20,
        1114,
    ): 
        u'TLSV1_BAD_CERTIFICATE_HASH_VALUE'
    ,
}

err_names_to_codes = {
    u'AKID_MISMATCH': (
        11,
        110,
    ),
    u'APP_DATA_IN_HANDSHAKE': (
        20,
        100,
    ),
    u'ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT': (
        20,
        272,
    ),
    u'BAD_ALERT_RECORD': (
        20,
        101,
    ),
    u'BAD_AUTHENTICATION_TYPE': (
        20,
        102,
    ),
    u'BAD_BASE64_DECODE': (
        9,
        100,
    ),
    u'BAD_CHANGE_CIPHER_SPEC': (
        20,
        103,
    ),
    u'BAD_CHECKSUM': (
        20,
        104,
    ),
    u'BAD_DATA': (
        20,
        390,
    ),
    u'BAD_DATA_RETURNED_BY_CALLBACK': (
        20,
        106,
    ),
    u'BAD_DECOMPRESSION': (
        20,
        107,
    ),
    u'BAD_DECRYPT': (
        9,
        101,
    ),
    u'BAD_DH_G_LENGTH': (
        20,
        108,
    ),
    u'BAD_DH_PUB_KEY_LENGTH': (
        20,
        109,
    ),
    u'BAD_DH_P_LENGTH': (
        20,
        110,
    ),
    u'BAD_DIGEST_LENGTH': (
        20,
        111,
    ),
    u'BAD_DSA_SIGNATURE': (
        20,
        112,
    ),
    u'BAD_ECC_CERT': (
        20,
        304,
    ),
    u'BAD_ECDSA_SIGNATURE': (
        20,
        305,
    ),
    u'BAD_ECPOINT': (
        20,
        306,
    ),
    u'BAD_END_LINE': (
        9,
        102,
    ),
    u'BAD_HANDSHAKE_LENGTH': (
        20,
        332,
    ),
    u'BAD_HELLO_REQUEST': (
        20,
        105,
    ),
    u'BAD_IV_CHARS': (
        9,
        103,
    ),
    u'BAD_LENGTH': (
        20,
        271,
    ),
    u'BAD_MAC_DECODE': (
        20,
        113,
    ),
    u'BAD_MAC_LENGTH': (
        20,
        333,
    ),
    u'BAD_MAGIC_NUMBER': (
        9,
        116,
    ),
    u'BAD_MESSAGE_TYPE': (
        20,
        114,
    ),
    u'BAD_PACKET_LENGTH': (
        20,
        115,
    ),
    u'BAD_PASSWORD_READ': (
        9,
        104,
    ),
    u'BAD_PROTOCOL_VERSION_NUMBER': (
        20,
        116,
    ),
    u'BAD_PSK_IDENTITY_HINT_LENGTH': (
        20,
        316,
    ),
    u'BAD_RESPONSE_ARGUMENT': (
        20,
        117,
    ),
    u'BAD_RSA_DECRYPT': (
        20,
        118,
    ),
    u'BAD_RSA_ENCRYPT': (
        20,
        119,
    ),
    u'BAD_RSA_E_LENGTH': (
        20,
        120,
    ),
    u'BAD_RSA_MODULUS_LENGTH': (
        20,
        121,
    ),
    u'BAD_RSA_SIGNATURE': (
        20,
        122,
    ),
    u'BAD_SIGNATURE': (
        20,
        123,
    ),
    u'BAD_SRP_A_LENGTH': (
        20,
        347,
    ),
    u'BAD_SRP_B_LENGTH': (
        20,
        348,
    ),
    u'BAD_SRP_G_LENGTH': (
        20,
        349,
    ),
    u'BAD_SRP_N_LENGTH': (
        20,
        350,
    ),
    u'BAD_SRP_PARAMETERS': (
        20,
        371,
    ),
    u'BAD_SRP_S_LENGTH': (
        20,
        351,
    ),
    u'BAD_SRTP_MKI_VALUE': (
        20,
        352,
    ),
    u'BAD_SRTP_PROTECTION_PROFILE_LIST': (
        20,
        353,
    ),
    u'BAD_SSL_FILETYPE': (
        20,
        124,
    ),
    u'BAD_SSL_SESSION_ID_LENGTH': (
        20,
        125,
    ),
    u'BAD_STATE': (
        20,
        126,
    ),
    u'BAD_VALUE': (
        20,
        384,
    ),
    u'BAD_VERSION_NUMBER': (
        9,
        117,
    ),
    u'BAD_WRITE_RETRY': (
        20,
        127,
    ),
    u'BAD_X509_FILETYPE': (
        11,
        100,
    ),
    u'BASE64_DECODE_ERROR': (
        11,
        118,
    ),
    u'BIO_NOT_SET': (
        20,
        128,
    ),
    u'BIO_WRITE_FAILURE': (
        9,
        118,
    ),
    u'BLOCK_CIPHER_PAD_IS_WRONG': (
        20,
        129,
    ),
    u'BN_LIB': (
        20,
        130,
    ),
    u'CANT_CHECK_DH_KEY': (
        11,
        114,
    ),
    u'CA_DN_LENGTH_MISMATCH': (
        20,
        131,
    ),
    u'CA_DN_TOO_LONG': (
        20,
        132,
    ),
    u'CA_KEY_TOO_SMALL': (
        20,
        397,
    ),
    u'CA_MD_TOO_WEAK': (
        20,
        398,
    ),
    u'CCS_RECEIVED_EARLY': (
        20,
        133,
    ),
    u'CERTIFICATE_VERIFY_FAILED': (
        20,
        134,
    ),
    u'CERT_ALREADY_IN_HASH_TABLE': (
        11,
        101,
    ),
    u'CERT_CB_ERROR': (
        20,
        377,
    ),
    u'CERT_LENGTH_MISMATCH': (
        20,
        135,
    ),
    u'CHALLENGE_IS_DIFFERENT': (
        20,
        136,
    ),
    u'CIPHER_CODE_WRONG_LENGTH': (
        20,
        137,
    ),
    u'CIPHER_IS_NULL': (
        9,
        127,
    ),
    u'CIPHER_OR_HASH_UNAVAILABLE': (
        20,
        138,
    ),
    u'CIPHER_TABLE_SRC_ERROR': (
        20,
        139,
    ),
    u'CLIENTHELLO_TLSEXT': (
        20,
        226,
    ),
    u'COMPRESSED_LENGTH_TOO_LONG': (
        20,
        140,
    ),
    u'COMPRESSION_DISABLED': (
        20,
        343,
    ),
    u'COMPRESSION_FAILURE': (
        20,
        141,
    ),
    u'COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE': (
        20,
        307,
    ),
    u'COMPRESSION_LIBRARY_ERROR': (
        20,
        142,
    ),
    u'CONNECTION_ID_IS_DIFFERENT': (
        20,
        143,
    ),
    u'CONNECTION_TYPE_NOT_SET': (
        20,
        144,
    ),
    u'COOKIE_MISMATCH': (
        20,
        308,
    ),
    u'CRL_ALREADY_DELTA': (
        11,
        127,
    ),
    u'CRL_VERIFY_FAILURE': (
        11,
        131,
    ),
    u'DATA_BETWEEN_CCS_AND_FINISHED': (
        20,
        145,
    ),
    u'DATA_LENGTH_TOO_LONG': (
        20,
        146,
    ),
    u'DECRYPTION_FAILED': (
        20,
        147,
    ),
    u'DECRYPTION_FAILED_OR_BAD_RECORD_MAC': (
        20,
        281,
    ),
    u'DH_KEY_TOO_SMALL': (
        20,
        372,
    ),
    u'DH_PUBLIC_VALUE_LENGTH_IS_WRONG': (
        20,
        148,
    ),
    u'DIGEST_CHECK_FAILED': (
        20,
        149,
    ),
    u'DTLS_MESSAGE_TOO_BIG': (
        20,
        334,
    ),
    u'DUPLICATE_COMPRESSION_ID': (
        20,
        309,
    ),
    u'ECC_CERT_NOT_FOR_KEY_AGREEMENT': (
        20,
        317,
    ),
    u'ECC_CERT_NOT_FOR_SIGNING': (
        20,
        318,
    ),
    u'ECC_CERT_SHOULD_HAVE_RSA_SIGNATURE': (
        20,
        322,
    ),
    u'ECC_CERT_SHOULD_HAVE_SHA1_SIGNATURE': (
        20,
        323,
    ),
    u'ECDH_REQUIRED_FOR_SUITEB_MODE': (
        20,
        374,
    ),
    u'ECGROUP_TOO_LARGE_FOR_CIPHER': (
        20,
        310,
    ),
    u'EE_KEY_TOO_SMALL': (
        20,
        399,
    ),
    u'EMPTY_SRTP_PROTECTION_PROFILE_LIST': (
        20,
        354,
    ),
    u'ENCRYPTED_LENGTH_TOO_LONG': (
        20,
        150,
    ),
    u'ERROR_CONVERTING_PRIVATE_KEY': (
        9,
        115,
    ),
    u'ERROR_GENERATING_TMP_RSA_KEY': (
        20,
        282,
    ),
    u'ERROR_IN_RECEIVED_CIPHER_LIST': (
        20,
        151,
    ),
    u'ERR_ASN1_LIB': (
        11,
        102,
    ),
    u'EXCESSIVE_MESSAGE_SIZE': (
        20,
        152,
    ),
    u'EXPECTING_PRIVATE_KEY_BLOB': (
        9,
        119,
    ),
    u'EXPECTING_PUBLIC_KEY_BLOB': (
        9,
        120,
    ),
    u'EXTRA_DATA_IN_MESSAGE': (
        20,
        153,
    ),
    u'GOT_A_FIN_BEFORE_A_CCS': (
        20,
        154,
    ),
    u'GOT_NEXT_PROTO_BEFORE_A_CCS': (
        20,
        355,
    ),
    u'GOT_NEXT_PROTO_WITHOUT_EXTENSION': (
        20,
        356,
    ),
    u'HTTPS_PROXY_REQUEST': (
        20,
        155,
    ),
    u'HTTP_REQUEST': (
        20,
        156,
    ),
    u'IDP_MISMATCH': (
        11,
        128,
    ),
    u'ILLEGAL_PADDING': (
        20,
        283,
    ),
    u'ILLEGAL_SUITEB_DIGEST': (
        20,
        380,
    ),
    u'INAPPROPRIATE_FALLBACK': (
        20,
        373,
    ),
    u'INCONSISTENT_COMPRESSION': (
        20,
        340,
    ),
    u'INCONSISTENT_HEADER': (
        9,
        121,
    ),
    u'INVALID_CHALLENGE_LENGTH': (
        20,
        158,
    ),
    u'INVALID_COMMAND': (
        20,
        280,
    ),
    u'INVALID_COMPRESSION_ALGORITHM': (
        20,
        341,
    ),
    u'INVALID_DIRECTORY': (
        11,
        113,
    ),
    u'INVALID_FIELD_NAME': (
        11,
        119,
    ),
    u'INVALID_NULL_CMD_NAME': (
        20,
        385,
    ),
    u'INVALID_PURPOSE': (
        20,
        278,
    ),
    u'INVALID_SERVERINFO_DATA': (
        20,
        388,
    ),
    u'INVALID_SRP_USERNAME': (
        20,
        357,
    ),
    u'INVALID_STATUS_RESPONSE': (
        20,
        328,
    ),
    u'INVALID_TICKET_KEYS_LENGTH': (
        20,
        325,
    ),
    u'INVALID_TRUST': (
        11,
        123,
    ),
    u'ISSUER_MISMATCH': (
        11,
        129,
    ),
    u'KEYBLOB_HEADER_PARSE_ERROR': (
        9,
        122,
    ),
    u'KEYBLOB_TOO_SHORT': (
        9,
        123,
    ),
    u'KEY_ARG_TOO_LONG': (
        20,
        284,
    ),
    u'KEY_TYPE_MISMATCH': (
        11,
        115,
    ),
    u'KEY_VALUES_MISMATCH': (
        11,
        116,
    ),
    u'KRB5': (
        20,
        285,
    ),
    u'KRB5_C_CC_PRINC': (
        20,
        286,
    ),
    u'KRB5_C_GET_CRED': (
        20,
        287,
    ),
    u'KRB5_C_INIT': (
        20,
        288,
    ),
    u'KRB5_C_MK_REQ': (
        20,
        289,
    ),
    u'KRB5_S_BAD_TICKET': (
        20,
        290,
    ),
    u'KRB5_S_INIT': (
        20,
        291,
    ),
    u'KRB5_S_RD_REQ': (
        20,
        292,
    ),
    u'KRB5_S_TKT_EXPIRED': (
        20,
        293,
    ),
    u'KRB5_S_TKT_NYV': (
        20,
        294,
    ),
    u'KRB5_S_TKT_SKEW': (
        20,
        295,
    ),
    u'LENGTH_MISMATCH': (
        20,
        159,
    ),
    u'LENGTH_TOO_SHORT': (
        20,
        160,
    ),
    u'LIBRARY_BUG': (
        20,
        274,
    ),
    u'LIBRARY_HAS_NO_CIPHERS': (
        20,
        161,
    ),
    u'LOADING_CERT_DIR': (
        11,
        103,
    ),
    u'LOADING_DEFAULTS': (
        11,
        104,
    ),
    u'MESSAGE_TOO_LONG': (
        20,
        296,
    ),
    u'METHOD_NOT_SUPPORTED': (
        11,
        124,
    ),
    u'MISSING_DH_DSA_CERT': (
        20,
        162,
    ),
    u'MISSING_DH_KEY': (
        20,
        163,
    ),
    u'MISSING_DH_RSA_CERT': (
        20,
        164,
    ),
    u'MISSING_DSA_SIGNING_CERT': (
        20,
        165,
    ),
    u'MISSING_ECDH_CERT': (
        20,
        382,
    ),
    u'MISSING_ECDSA_SIGNING_CERT': (
        20,
        381,
    ),
    u'MISSING_EXPORT_TMP_DH_KEY': (
        20,
        166,
    ),
    u'MISSING_EXPORT_TMP_RSA_KEY': (
        20,
        167,
    ),
    u'MISSING_RSA_CERTIFICATE': (
        20,
        168,
    ),
    u'MISSING_RSA_ENCRYPTING_CERT': (
        20,
        169,
    ),
    u'MISSING_RSA_SIGNING_CERT': (
        20,
        170,
    ),
    u'MISSING_SRP_PARAM': (
        20,
        358,
    ),
    u'MISSING_TMP_DH_KEY': (
        20,
        171,
    ),
    u'MISSING_TMP_ECDH_KEY': (
        20,
        311,
    ),
    u'MISSING_TMP_RSA_KEY': (
        20,
        172,
    ),
    u'MISSING_TMP_RSA_PKEY': (
        20,
        173,
    ),
    u'MISSING_VERIFY_MESSAGE': (
        20,
        174,
    ),
    u'MULTIPLE_SGC_RESTARTS': (
        20,
        346,
    ),
    u'NEWER_CRL_NOT_NEWER': (
        11,
        132,
    ),
    u'NON_SSLV2_INITIAL_PACKET': (
        20,
        175,
    ),
    u'NOT_DEK_INFO': (
        9,
        105,
    ),
    u'NOT_ENCRYPTED': (
        9,
        106,
    ),
    u'NOT_PROC_TYPE': (
        9,
        107,
    ),
    u'NO_CERTIFICATES_RETURNED': (
        20,
        176,
    ),
    u'NO_CERTIFICATE_ASSIGNED': (
        20,
        177,
    ),
    u'NO_CERTIFICATE_RETURNED': (
        20,
        178,
    ),
    u'NO_CERTIFICATE_SET': (
        20,
        179,
    ),
    u'NO_CERTIFICATE_SPECIFIED': (
        20,
        180,
    ),
    u'NO_CERT_SET_FOR_US_TO_VERIFY': (
        11,
        105,
    ),
    u'NO_CIPHERS_AVAILABLE': (
        20,
        181,
    ),
    u'NO_CIPHERS_PASSED': (
        20,
        182,
    ),
    u'NO_CIPHERS_SPECIFIED': (
        20,
        183,
    ),
    u'NO_CIPHER_LIST': (
        20,
        184,
    ),
    u'NO_CIPHER_MATCH': (
        20,
        185,
    ),
    u'NO_CLIENT_CERT_METHOD': (
        20,
        331,
    ),
    u'NO_CLIENT_CERT_RECEIVED': (
        20,
        186,
    ),
    u'NO_COMPRESSION_SPECIFIED': (
        20,
        187,
    ),
    u'NO_CRL_NUMBER': (
        11,
        130,
    ),
    u'NO_GOST_CERTIFICATE_SENT_BY_PEER': (
        20,
        330,
    ),
    u'NO_METHOD_SPECIFIED': (
        20,
        188,
    ),
    u'NO_PEM_EXTENSIONS': (
        20,
        389,
    ),
    u'NO_PRIVATEKEY': (
        20,
        189,
    ),
    u'NO_PRIVATE_KEY_ASSIGNED': (
        20,
        190,
    ),
    u'NO_PROTOCOLS_AVAILABLE': (
        20,
        191,
    ),
    u'NO_PUBLICKEY': (
        20,
        192,
    ),
    u'NO_RENEGOTIATION': (
        20,
        339,
    ),
    u'NO_REQUIRED_DIGEST': (
        20,
        324,
    ),
    u'NO_SHARED_CIPHER': (
        20,
        193,
    ),
    u'NO_SHARED_SIGATURE_ALGORITHMS': (
        20,
        376,
    ),
    u'NO_SRTP_PROFILES': (
        20,
        359,
    ),
    u'NO_START_LINE': (
        9,
        108,
    ),
    u'NO_VERIFY_CALLBACK': (
        20,
        194,
    ),
    u'NULL_SSL_CTX': (
        20,
        195,
    ),
    u'NULL_SSL_METHOD_PASSED': (
        20,
        196,
    ),
    u'OLD_SESSION_CIPHER_NOT_RETURNED': (
        20,
        197,
    ),
    u'OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED': (
        20,
        344,
    ),
    u'ONLY_DTLS_1_2_ALLOWED_IN_SUITEB_MODE': (
        20,
        387,
    ),
    u'ONLY_TLS_1_2_ALLOWED_IN_SUITEB_MODE': (
        20,
        379,
    ),
    u'ONLY_TLS_ALLOWED_IN_FIPS_MODE': (
        20,
        297,
    ),
    u'OPAQUE_PRF_INPUT_TOO_LONG': (
        20,
        327,
    ),
    u'PACKET_LENGTH_TOO_LONG': (
        20,
        198,
    ),
    u'PARSE_TLSEXT': (
        20,
        227,
    ),
    u'PATH_TOO_LONG': (
        20,
        270,
    ),
    u'PEER_DID_NOT_RETURN_A_CERTIFICATE': (
        20,
        199,
    ),
    u'PEER_ERROR': (
        20,
        200,
    ),
    u'PEER_ERROR_CERTIFICATE': (
        20,
        201,
    ),
    u'PEER_ERROR_NO_CERTIFICATE': (
        20,
        202,
    ),
    u'PEER_ERROR_NO_CIPHER': (
        20,
        203,
    ),
    u'PEER_ERROR_UNSUPPORTED_CERTIFICATE_TYPE': (
        20,
        204,
    ),
    u'PEM_NAME_BAD_PREFIX': (
        20,
        391,
    ),
    u'PEM_NAME_TOO_SHORT': (
        20,
        392,
    ),
    u'PRE_MAC_LENGTH_TOO_LONG': (
        20,
        205,
    ),
    u'PROBLEMS_GETTING_PASSWORD': (
        9,
        109,
    ),
    u'PROBLEMS_MAPPING_CIPHER_FUNCTIONS': (
        20,
        206,
    ),
    u'PROTOCOL_IS_SHUTDOWN': (
        20,
        207,
    ),
    u'PSK_IDENTITY_NOT_FOUND': (
        20,
        223,
    ),
    u'PSK_NO_CLIENT_CB': (
        20,
        224,
    ),
    u'PSK_NO_SERVER_CB': (
        20,
        225,
    ),
    u'PUBLIC_KEY_DECODE_ERROR': (
        11,
        125,
    ),
    u'PUBLIC_KEY_ENCODE_ERROR': (
        11,
        126,
    ),
    u'PUBLIC_KEY_ENCRYPT_ERROR': (
        20,
        208,
    ),
    u'PUBLIC_KEY_IS_NOT_RSA': (
        20,
        209,
    ),
    u'PUBLIC_KEY_NOT_RSA': (
        20,
        210,
    ),
    u'PUBLIC_KEY_NO_RSA': (
        9,
        110,
    ),
    u'PVK_DATA_TOO_SHORT': (
        9,
        124,
    ),
    u'PVK_TOO_SHORT': (
        9,
        125,
    ),
    u'READ_BIO_NOT_SET': (
        20,
        211,
    ),
    u'READ_KEY': (
        9,
        111,
    ),
    u'READ_TIMEOUT_EXPIRED': (
        20,
        312,
    ),
    u'READ_WRONG_PACKET_TYPE': (
        20,
        212,
    ),
    u'RECORD_LENGTH_MISMATCH': (
        20,
        213,
    ),
    u'RECORD_TOO_LARGE': (
        20,
        214,
    ),
    u'RECORD_TOO_SMALL': (
        20,
        298,
    ),
    u'RENEGOTIATE_EXT_TOO_LONG': (
        20,
        335,
    ),
    u'RENEGOTIATION_ENCODING_ERR': (
        20,
        336,
    ),
    u'RENEGOTIATION_MISMATCH': (
        20,
        337,
    ),
    u'REQUIRED_CIPHER_MISSING': (
        20,
        215,
    ),
    u'REQUIRED_COMPRESSSION_ALGORITHM_MISSING': (
        20,
        342,
    ),
    u'REUSE_CERT_LENGTH_NOT_ZERO': (
        20,
        216,
    ),
    u'REUSE_CERT_TYPE_NOT_ZERO': (
        20,
        217,
    ),
    u'REUSE_CIPHER_LIST_NOT_ZERO': (
        20,
        218,
    ),
    u'SCSV_RECEIVED_WHEN_RENEGOTIATING': (
        20,
        345,
    ),
    u'SERVERHELLO_TLSEXT': (
        20,
        275,
    ),
    u'SESSION_ID_CONTEXT_UNINITIALIZED': (
        20,
        277,
    ),
    u'SHORT_HEADER': (
        9,
        112,
    ),
    u'SHORT_READ': (
        20,
        219,
    ),
    u'SHOULD_RETRY': (
        11,
        106,
    ),
    u'SIGNATURE_ALGORITHMS_ERROR': (
        20,
        360,
    ),
    u'SIGNATURE_FOR_NON_SIGNING_CERTIFICATE': (
        20,
        220,
    ),
    u'SRP_A_CALC': (
        20,
        361,
    ),
    u'SRTP_COULD_NOT_ALLOCATE_PROFILES': (
        20,
        362,
    ),
    u'SRTP_PROTECTION_PROFILE_LIST_TOO_LONG': (
        20,
        363,
    ),
    u'SRTP_UNKNOWN_PROTECTION_PROFILE': (
        20,
        364,
    ),
    u'SSL23_DOING_SESSION_ID_REUSE': (
        20,
        221,
    ),
    u'SSL2_CONNECTION_ID_TOO_LONG': (
        20,
        299,
    ),
    u'SSL3_EXT_INVALID_ECPOINTFORMAT': (
        20,
        321,
    ),
    u'SSL3_EXT_INVALID_SERVERNAME': (
        20,
        319,
    ),
    u'SSL3_EXT_INVALID_SERVERNAME_TYPE': (
        20,
        320,
    ),
    u'SSL3_SESSION_ID_TOO_LONG': (
        20,
        300,
    ),
    u'SSL3_SESSION_ID_TOO_SHORT': (
        20,
        222,
    ),
    u'SSLV3_ALERT_BAD_CERTIFICATE': (
        20,
        1042,
    ),
    u'SSLV3_ALERT_BAD_RECORD_MAC': (
        20,
        1020,
    ),
    u'SSLV3_ALERT_CERTIFICATE_EXPIRED': (
        20,
        1045,
    ),
    u'SSLV3_ALERT_CERTIFICATE_REVOKED': (
        20,
        1044,
    ),
    u'SSLV3_ALERT_CERTIFICATE_UNKNOWN': (
        20,
        1046,
    ),
    u'SSLV3_ALERT_DECOMPRESSION_FAILURE': (
        20,
        1030,
    ),
    u'SSLV3_ALERT_HANDSHAKE_FAILURE': (
        20,
        1040,
    ),
    u'SSLV3_ALERT_ILLEGAL_PARAMETER': (
        20,
        1047,
    ),
    u'SSLV3_ALERT_NO_CERTIFICATE': (
        20,
        1041,
    ),
    u'SSLV3_ALERT_UNEXPECTED_MESSAGE': (
        20,
        1010,
    ),
    u'SSLV3_ALERT_UNSUPPORTED_CERTIFICATE': (
        20,
        1043,
    ),
    u'SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION': (
        20,
        228,
    ),
    u'SSL_HANDSHAKE_FAILURE': (
        20,
        229,
    ),
    u'SSL_LIBRARY_HAS_NO_CIPHERS': (
        20,
        230,
    ),
    u'SSL_NEGATIVE_LENGTH': '<value is a self-reference, replaced by this string>',
    u'SSL_SESSION_ID_CALLBACK_FAILED': (
        20,
        301,
    ),
    u'SSL_SESSION_ID_CONFLICT': (
        20,
        302,
    ),
    u'SSL_SESSION_ID_CONTEXT_TOO_LONG': (
        20,
        273,
    ),
    u'SSL_SESSION_ID_HAS_BAD_LENGTH': (
        20,
        303,
    ),
    u'SSL_SESSION_ID_IS_DIFFERENT': (
        20,
        231,
    ),
    u'TLSV1_ALERT_ACCESS_DENIED': (
        20,
        1049,
    ),
    u'TLSV1_ALERT_DECODE_ERROR': (
        20,
        1050,
    ),
    u'TLSV1_ALERT_DECRYPTION_FAILED': (
        20,
        1021,
    ),
    u'TLSV1_ALERT_DECRYPT_ERROR': (
        20,
        1051,
    ),
    u'TLSV1_ALERT_EXPORT_RESTRICTION': (
        20,
        1060,
    ),
    u'TLSV1_ALERT_INAPPROPRIATE_FALLBACK': (
        20,
        1086,
    ),
    u'TLSV1_ALERT_INSUFFICIENT_SECURITY': (
        20,
        1071,
    ),
    u'TLSV1_ALERT_INTERNAL_ERROR': (
        20,
        1080,
    ),
    u'TLSV1_ALERT_NO_RENEGOTIATION': (
        20,
        1100,
    ),
    u'TLSV1_ALERT_PROTOCOL_VERSION': (
        20,
        1070,
    ),
    u'TLSV1_ALERT_RECORD_OVERFLOW': (
        20,
        1022,
    ),
    u'TLSV1_ALERT_UNKNOWN_CA': (
        20,
        1048,
    ),
    u'TLSV1_ALERT_USER_CANCELLED': (
        20,
        1090,
    ),
    u'TLSV1_BAD_CERTIFICATE_HASH_VALUE': (
        20,
        1114,
    ),
    u'TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE': (
        20,
        1113,
    ),
    u'TLSV1_CERTIFICATE_UNOBTAINABLE': (
        20,
        1111,
    ),
    u'TLSV1_UNRECOGNIZED_NAME': (
        20,
        1112,
    ),
    u'TLSV1_UNSUPPORTED_EXTENSION': (
        20,
        1110,
    ),
    u'TLS_CLIENT_CERT_REQ_WITH_ANON_CIPHER': (
        20,
        232,
    ),
    u'TLS_HEARTBEAT_PEER_DOESNT_ACCEPT': (
        20,
        365,
    ),
    u'TLS_HEARTBEAT_PENDING': (
        20,
        366,
    ),
    u'TLS_ILLEGAL_EXPORTER_LABEL': (
        20,
        367,
    ),
    u'TLS_INVALID_ECPOINTFORMAT_LIST': (
        20,
        157,
    ),
    u'TLS_PEER_DID_NOT_RESPOND_WITH_CERTIFICATE_LIST': (
        20,
        233,
    ),
    u'TLS_RSA_ENCRYPTED_VALUE_LENGTH_IS_WRONG': (
        20,
        234,
    ),
    u'TRIED_TO_USE_UNSUPPORTED_CIPHER': (
        20,
        235,
    ),
    u'UNABLE_TO_DECODE_DH_CERTS': (
        20,
        236,
    ),
    u'UNABLE_TO_DECODE_ECDH_CERTS': (
        20,
        313,
    ),
    u'UNABLE_TO_EXTRACT_PUBLIC_KEY': (
        20,
        237,
    ),
    u'UNABLE_TO_FIND_DH_PARAMETERS': (
        20,
        238,
    ),
    u'UNABLE_TO_FIND_ECDH_PARAMETERS': (
        20,
        314,
    ),
    u'UNABLE_TO_FIND_PARAMETERS_IN_CHAIN': (
        11,
        107,
    ),
    u'UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS': (
        20,
        239,
    ),
    u'UNABLE_TO_FIND_SSL_METHOD': (
        20,
        240,
    ),
    u'UNABLE_TO_GET_CERTS_PUBLIC_KEY': (
        11,
        108,
    ),
    u'UNABLE_TO_LOAD_SSL2_MD5_ROUTINES': (
        20,
        241,
    ),
    u'UNABLE_TO_LOAD_SSL3_MD5_ROUTINES': (
        20,
        242,
    ),
    u'UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES': (
        20,
        243,
    ),
    u'UNEXPECTED_MESSAGE': (
        20,
        244,
    ),
    u'UNEXPECTED_RECORD': (
        20,
        245,
    ),
    u'UNINITIALIZED': (
        20,
        276,
    ),
    u'UNKNOWN_ALERT_TYPE': (
        20,
        246,
    ),
    u'UNKNOWN_CERTIFICATE_TYPE': (
        20,
        247,
    ),
    u'UNKNOWN_CIPHER_RETURNED': (
        20,
        248,
    ),
    u'UNKNOWN_CIPHER_TYPE': (
        20,
        249,
    ),
    u'UNKNOWN_CMD_NAME': (
        20,
        386,
    ),
    u'UNKNOWN_DIGEST': (
        20,
        368,
    ),
    u'UNKNOWN_KEY_EXCHANGE_TYPE': (
        20,
        250,
    ),
    u'UNKNOWN_KEY_TYPE': (
        11,
        117,
    ),
    u'UNKNOWN_NID': (
        11,
        109,
    ),
    u'UNKNOWN_PKEY_TYPE': (
        20,
        251,
    ),
    u'UNKNOWN_PROTOCOL': (
        20,
        252,
    ),
    u'UNKNOWN_PURPOSE_ID': (
        11,
        121,
    ),
    u'UNKNOWN_REMOTE_ERROR_TYPE': (
        20,
        253,
    ),
    u'UNKNOWN_SSL_VERSION': (
        20,
        254,
    ),
    u'UNKNOWN_STATE': (
        20,
        255,
    ),
    u'UNKNOWN_TRUST_ID': (
        11,
        120,
    ),
    u'UNSAFE_LEGACY_RENEGOTIATION_DISABLED': (
        20,
        338,
    ),
    u'UNSUPPORTED_ALGORITHM': (
        11,
        111,
    ),
    u'UNSUPPORTED_CIPHER': (
        20,
        256,
    ),
    u'UNSUPPORTED_COMPRESSION_ALGORITHM': (
        20,
        257,
    ),
    u'UNSUPPORTED_DIGEST_TYPE': (
        20,
        326,
    ),
    u'UNSUPPORTED_ELLIPTIC_CURVE': (
        20,
        315,
    ),
    u'UNSUPPORTED_ENCRYPTION': (
        9,
        114,
    ),
    u'UNSUPPORTED_KEY_COMPONENTS': (
        9,
        126,
    ),
    u'UNSUPPORTED_PROTOCOL': (
        20,
        258,
    ),
    u'UNSUPPORTED_SSL_VERSION': (
        20,
        259,
    ),
    u'UNSUPPORTED_STATUS_TYPE': (
        20,
        329,
    ),
    u'USE_SRTP_NOT_NEGOTIATED': (
        20,
        369,
    ),
    u'VERSION_TOO_LOW': (
        20,
        396,
    ),
    u'WRITE_BIO_NOT_SET': (
        20,
        260,
    ),
    u'WRONG_CERTIFICATE_TYPE': (
        20,
        383,
    ),
    u'WRONG_CIPHER_RETURNED': (
        20,
        261,
    ),
    u'WRONG_CURVE': (
        20,
        378,
    ),
    u'WRONG_LOOKUP_TYPE': (
        11,
        112,
    ),
    u'WRONG_MESSAGE_TYPE': (
        20,
        262,
    ),
    u'WRONG_NUMBER_OF_KEY_BITS': (
        20,
        263,
    ),
    u'WRONG_SIGNATURE_LENGTH': (
        20,
        264,
    ),
    u'WRONG_SIGNATURE_SIZE': (
        20,
        265,
    ),
    u'WRONG_SIGNATURE_TYPE': (
        20,
        370,
    ),
    u'WRONG_SSL_VERSION': (
        20,
        266,
    ),
    u'WRONG_TYPE': (
        11,
        122,
    ),
    u'WRONG_VERSION_NUMBER': (
        20,
        267,
    ),
    u'X509_LIB': (
        20,
        268,
    ),
    u'X509_VERIFICATION_SETUP_PROBLEMS': (
        20,
        269,
    ),
}

lib_codes_to_names = {
    9L: u'PEM',
    11L: u'X509',
    20L: u'SSL',
}

OPENSSL_VERSION_INFO = (
    1,
    0,
    2,
    17,
    15,
)

_OPENSSL_API_VERSION = (
    1,
    0,
    2,
    17,
    15,
)


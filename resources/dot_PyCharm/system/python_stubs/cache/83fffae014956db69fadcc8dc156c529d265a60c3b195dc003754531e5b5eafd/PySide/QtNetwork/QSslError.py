# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QSslError(__Shiboken.Object):
    # no doc
    def certificate(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    AuthorityIssuerSerialNumberMismatch = PySide.QtNetwork.QSslError.SslError.AuthorityIssuerSerialNumberMismatch
    CertificateBlacklisted = PySide.QtNetwork.QSslError.SslError.CertificateBlacklisted
    CertificateExpired = PySide.QtNetwork.QSslError.SslError.CertificateExpired
    CertificateNotYetValid = PySide.QtNetwork.QSslError.SslError.CertificateNotYetValid
    CertificateRejected = PySide.QtNetwork.QSslError.SslError.CertificateRejected
    CertificateRevoked = PySide.QtNetwork.QSslError.SslError.CertificateRevoked
    CertificateSignatureFailed = PySide.QtNetwork.QSslError.SslError.CertificateSignatureFailed
    CertificateUntrusted = PySide.QtNetwork.QSslError.SslError.CertificateUntrusted
    HostNameMismatch = PySide.QtNetwork.QSslError.SslError.HostNameMismatch
    InvalidCaCertificate = PySide.QtNetwork.QSslError.SslError.InvalidCaCertificate
    InvalidNotAfterField = PySide.QtNetwork.QSslError.SslError.InvalidNotAfterField
    InvalidNotBeforeField = PySide.QtNetwork.QSslError.SslError.InvalidNotBeforeField
    InvalidPurpose = PySide.QtNetwork.QSslError.SslError.InvalidPurpose
    NoError = PySide.QtNetwork.QSslError.SslError.NoError
    NoPeerCertificate = PySide.QtNetwork.QSslError.SslError.NoPeerCertificate
    NoSslSupport = PySide.QtNetwork.QSslError.SslError.NoSslSupport
    PathLengthExceeded = PySide.QtNetwork.QSslError.SslError.PathLengthExceeded
    SelfSignedCertificate = PySide.QtNetwork.QSslError.SslError.SelfSignedCertificate
    SelfSignedCertificateInChain = PySide.QtNetwork.QSslError.SslError.SelfSignedCertificateInChain
    SslError = None # (!) real value is "<type 'PySide.QtNetwork.QSslError.SslError'>"
    SubjectIssuerMismatch = PySide.QtNetwork.QSslError.SslError.SubjectIssuerMismatch
    UnableToDecodeIssuerPublicKey = PySide.QtNetwork.QSslError.SslError.UnableToDecodeIssuerPublicKey
    UnableToDecryptCertificateSignature = PySide.QtNetwork.QSslError.SslError.UnableToDecryptCertificateSignature
    UnableToGetIssuerCertificate = PySide.QtNetwork.QSslError.SslError.UnableToGetIssuerCertificate
    UnableToGetLocalIssuerCertificate = PySide.QtNetwork.QSslError.SslError.UnableToGetLocalIssuerCertificate
    UnableToVerifyFirstCertificate = PySide.QtNetwork.QSslError.SslError.UnableToVerifyFirstCertificate
    UnspecifiedError = PySide.QtNetwork.QSslError.SslError.UnspecifiedError



# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkReply(__PySide_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def downloadProgress(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def hasRawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def header(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self, *args, **kwargs): # real signature unknown
        pass

    def isRunning(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self, *args, **kwargs): # real signature unknown
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def operation(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeaderList(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeaderPairs(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def request(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setHeader(self, *args, **kwargs): # real signature unknown
        pass

    def setOperation(self, *args, **kwargs): # real signature unknown
        pass

    def setRawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setRequest(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def sslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def uploadProgress(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AuthenticationRequiredError = PySide.QtNetwork.QNetworkReply.NetworkError.AuthenticationRequiredError
    ConnectionRefusedError = PySide.QtNetwork.QNetworkReply.NetworkError.ConnectionRefusedError
    ContentAccessDenied = PySide.QtNetwork.QNetworkReply.NetworkError.ContentAccessDenied
    ContentNotFoundError = PySide.QtNetwork.QNetworkReply.NetworkError.ContentNotFoundError
    ContentOperationNotPermittedError = PySide.QtNetwork.QNetworkReply.NetworkError.ContentOperationNotPermittedError
    ContentReSendError = PySide.QtNetwork.QNetworkReply.NetworkError.ContentReSendError
    HostNotFoundError = PySide.QtNetwork.QNetworkReply.NetworkError.HostNotFoundError
    NetworkError = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkReply.NetworkError'>"
    NoError = PySide.QtNetwork.QNetworkReply.NetworkError.NoError
    OperationCanceledError = PySide.QtNetwork.QNetworkReply.NetworkError.OperationCanceledError
    ProtocolFailure = PySide.QtNetwork.QNetworkReply.NetworkError.ProtocolFailure
    ProtocolInvalidOperationError = PySide.QtNetwork.QNetworkReply.NetworkError.ProtocolInvalidOperationError
    ProtocolUnknownError = PySide.QtNetwork.QNetworkReply.NetworkError.ProtocolUnknownError
    ProxyAuthenticationRequiredError = PySide.QtNetwork.QNetworkReply.NetworkError.ProxyAuthenticationRequiredError
    ProxyConnectionClosedError = PySide.QtNetwork.QNetworkReply.NetworkError.ProxyConnectionClosedError
    ProxyConnectionRefusedError = PySide.QtNetwork.QNetworkReply.NetworkError.ProxyConnectionRefusedError
    ProxyNotFoundError = PySide.QtNetwork.QNetworkReply.NetworkError.ProxyNotFoundError
    ProxyTimeoutError = PySide.QtNetwork.QNetworkReply.NetworkError.ProxyTimeoutError
    RemoteHostClosedError = PySide.QtNetwork.QNetworkReply.NetworkError.RemoteHostClosedError
    SslHandshakeFailedError = PySide.QtNetwork.QNetworkReply.NetworkError.SslHandshakeFailedError
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038B1C08>'
    TemporaryNetworkFailureError = PySide.QtNetwork.QNetworkReply.NetworkError.TemporaryNetworkFailureError
    TimeoutError = PySide.QtNetwork.QNetworkReply.NetworkError.TimeoutError
    UnknownContentError = PySide.QtNetwork.QNetworkReply.NetworkError.UnknownContentError
    UnknownNetworkError = PySide.QtNetwork.QNetworkReply.NetworkError.UnknownNetworkError
    UnknownProxyError = PySide.QtNetwork.QNetworkReply.NetworkError.UnknownProxyError



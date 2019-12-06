# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QHttp(__PySide_QtCore.QObject):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def clearPendingRequests(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def currentDestinationDevice(self, *args, **kwargs): # real signature unknown
        pass

    def currentId(self, *args, **kwargs): # real signature unknown
        pass

    def currentRequest(self, *args, **kwargs): # real signature unknown
        pass

    def currentSourceDevice(self, *args, **kwargs): # real signature unknown
        pass

    def dataReadProgress(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def dataSendProgress(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingRequests(self, *args, **kwargs): # real signature unknown
        pass

    def head(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def lastResponse(self, *args, **kwargs): # real signature unknown
        pass

    def post(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readAll(self, *args, **kwargs): # real signature unknown
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def request(self, *args, **kwargs): # real signature unknown
        pass

    def requestFinished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def requestStarted(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def responseHeaderReceived(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setHost(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setSocket(self, *args, **kwargs): # real signature unknown
        pass

    def setUser(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Aborted = PySide.QtNetwork.QHttp.Error.Aborted
    AuthenticationRequiredError = PySide.QtNetwork.QHttp.Error.AuthenticationRequiredError
    Closing = PySide.QtNetwork.QHttp.State.Closing
    Connected = PySide.QtNetwork.QHttp.State.Connected
    Connecting = PySide.QtNetwork.QHttp.State.Connecting
    ConnectionMode = None # (!) real value is "<type 'PySide.QtNetwork.QHttp.ConnectionMode'>"
    ConnectionModeHttp = PySide.QtNetwork.QHttp.ConnectionMode.ConnectionModeHttp
    ConnectionModeHttps = PySide.QtNetwork.QHttp.ConnectionMode.ConnectionModeHttps
    ConnectionRefused = PySide.QtNetwork.QHttp.Error.ConnectionRefused
    Error = None # (!) real value is "<type 'PySide.QtNetwork.QHttp.Error'>"
    HostLookup = PySide.QtNetwork.QHttp.State.HostLookup
    HostNotFound = PySide.QtNetwork.QHttp.Error.HostNotFound
    InvalidResponseHeader = PySide.QtNetwork.QHttp.Error.InvalidResponseHeader
    NoError = PySide.QtNetwork.QHttp.Error.NoError
    ProxyAuthenticationRequiredError = PySide.QtNetwork.QHttp.Error.ProxyAuthenticationRequiredError
    Reading = PySide.QtNetwork.QHttp.State.Reading
    Sending = PySide.QtNetwork.QHttp.State.Sending
    State = None # (!) real value is "<type 'PySide.QtNetwork.QHttp.State'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038A6048>'
    Unconnected = PySide.QtNetwork.QHttp.State.Unconnected
    UnexpectedClose = PySide.QtNetwork.QHttp.Error.UnexpectedClose
    UnknownError = PySide.QtNetwork.QHttp.Error.UnknownError
    WrongContentLength = PySide.QtNetwork.QHttp.Error.WrongContentLength



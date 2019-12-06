# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkSession(__PySide_QtCore.QObject):
    # no doc
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def activeTime(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReceived(self, *args, **kwargs): # real signature unknown
        pass

    def bytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def closed(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def configuration(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def ignore(self, *args, **kwargs): # real signature unknown
        pass

    def interface(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def migrate(self, *args, **kwargs): # real signature unknown
        pass

    def newConfigurationActivated(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def opened(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def preferredConfigurationChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def reject(self, *args, **kwargs): # real signature unknown
        pass

    def sessionProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setSessionProperty(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def waitForOpened(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Closing = PySide.QtNetwork.QNetworkSession.State.Closing
    Connected = PySide.QtNetwork.QNetworkSession.State.Connected
    Connecting = PySide.QtNetwork.QNetworkSession.State.Connecting
    Disconnected = PySide.QtNetwork.QNetworkSession.State.Disconnected
    Invalid = PySide.QtNetwork.QNetworkSession.State.Invalid
    InvalidConfigurationError = PySide.QtNetwork.QNetworkSession.SessionError.InvalidConfigurationError
    NotAvailable = PySide.QtNetwork.QNetworkSession.State.NotAvailable
    OperationNotSupportedError = PySide.QtNetwork.QNetworkSession.SessionError.OperationNotSupportedError
    Roaming = PySide.QtNetwork.QNetworkSession.State.Roaming
    RoamingError = PySide.QtNetwork.QNetworkSession.SessionError.RoamingError
    SessionAbortedError = PySide.QtNetwork.QNetworkSession.SessionError.SessionAbortedError
    SessionError = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkSession.SessionError'>"
    State = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkSession.State'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000037D39C8>'
    UnknownSessionError = PySide.QtNetwork.QNetworkSession.SessionError.UnknownSessionError



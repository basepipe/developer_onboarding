# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QLocalSocket(__PySide_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def connectToServer(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def disconnectFromServer(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def fullServerName(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def serverName(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ClosingState = PySide.QtNetwork.QLocalSocket.LocalSocketState.ClosingState
    ConnectedState = PySide.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState
    ConnectingState = PySide.QtNetwork.QLocalSocket.LocalSocketState.ConnectingState
    ConnectionError = PySide.QtNetwork.QLocalSocket.LocalSocketError.ConnectionError
    ConnectionRefusedError = PySide.QtNetwork.QLocalSocket.LocalSocketError.ConnectionRefusedError
    DatagramTooLargeError = PySide.QtNetwork.QLocalSocket.LocalSocketError.DatagramTooLargeError
    LocalSocketError = None # (!) real value is "<type 'PySide.QtNetwork.QLocalSocket.LocalSocketError'>"
    LocalSocketState = None # (!) real value is "<type 'PySide.QtNetwork.QLocalSocket.LocalSocketState'>"
    PeerClosedError = PySide.QtNetwork.QLocalSocket.LocalSocketError.PeerClosedError
    ServerNotFoundError = PySide.QtNetwork.QLocalSocket.LocalSocketError.ServerNotFoundError
    SocketAccessError = PySide.QtNetwork.QLocalSocket.LocalSocketError.SocketAccessError
    SocketResourceError = PySide.QtNetwork.QLocalSocket.LocalSocketError.SocketResourceError
    SocketTimeoutError = PySide.QtNetwork.QLocalSocket.LocalSocketError.SocketTimeoutError
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038AD808>'
    UnconnectedState = PySide.QtNetwork.QLocalSocket.LocalSocketState.UnconnectedState
    UnknownSocketError = PySide.QtNetwork.QLocalSocket.LocalSocketError.UnknownSocketError
    UnsupportedSocketOperationError = PySide.QtNetwork.QLocalSocket.LocalSocketError.UnsupportedSocketOperationError



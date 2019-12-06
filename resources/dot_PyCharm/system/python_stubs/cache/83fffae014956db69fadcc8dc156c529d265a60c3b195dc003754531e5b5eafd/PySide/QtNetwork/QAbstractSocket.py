# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QAbstractSocket(__PySide_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
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

    def connectionClosed(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def connectToHost(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def delayedCloseFinished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def disconnectFromHost(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def hostFound(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self, *args, **kwargs): # real signature unknown
        pass

    def localPort(self, *args, **kwargs): # real signature unknown
        pass

    def peerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def peerName(self, *args, **kwargs): # real signature unknown
        pass

    def peerPort(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def socketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def socketOption(self, *args, **kwargs): # real signature unknown
        pass

    def socketType(self, *args, **kwargs): # real signature unknown
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

    AddressInUseError = PySide.QtNetwork.QAbstractSocket.SocketError.AddressInUseError
    BoundState = PySide.QtNetwork.QAbstractSocket.SocketState.BoundState
    ClosingState = PySide.QtNetwork.QAbstractSocket.SocketState.ClosingState
    ConnectedState = PySide.QtNetwork.QAbstractSocket.SocketState.ConnectedState
    ConnectingState = PySide.QtNetwork.QAbstractSocket.SocketState.ConnectingState
    ConnectionRefusedError = PySide.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError
    DatagramTooLargeError = PySide.QtNetwork.QAbstractSocket.SocketError.DatagramTooLargeError
    HostLookupState = PySide.QtNetwork.QAbstractSocket.SocketState.HostLookupState
    HostNotFoundError = PySide.QtNetwork.QAbstractSocket.SocketError.HostNotFoundError
    IPv4Protocol = PySide.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv4Protocol
    IPv6Protocol = PySide.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv6Protocol
    KeepAliveOption = PySide.QtNetwork.QAbstractSocket.SocketOption.KeepAliveOption
    ListeningState = PySide.QtNetwork.QAbstractSocket.SocketState.ListeningState
    LowDelayOption = PySide.QtNetwork.QAbstractSocket.SocketOption.LowDelayOption
    MulticastLoopbackOption = PySide.QtNetwork.QAbstractSocket.SocketOption.MulticastLoopbackOption
    MulticastTtlOption = PySide.QtNetwork.QAbstractSocket.SocketOption.MulticastTtlOption
    NetworkError = PySide.QtNetwork.QAbstractSocket.SocketError.NetworkError
    NetworkLayerProtocol = None # (!) real value is "<type 'PySide.QtNetwork.QAbstractSocket.NetworkLayerProtocol'>"
    ProxyAuthenticationRequiredError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyAuthenticationRequiredError
    ProxyConnectionClosedError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionClosedError
    ProxyConnectionRefusedError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionRefusedError
    ProxyConnectionTimeoutError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionTimeoutError
    ProxyNotFoundError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyNotFoundError
    ProxyProtocolError = PySide.QtNetwork.QAbstractSocket.SocketError.ProxyProtocolError
    RemoteHostClosedError = PySide.QtNetwork.QAbstractSocket.SocketError.RemoteHostClosedError
    SocketAccessError = PySide.QtNetwork.QAbstractSocket.SocketError.SocketAccessError
    SocketAddressNotAvailableError = PySide.QtNetwork.QAbstractSocket.SocketError.SocketAddressNotAvailableError
    SocketError = None # (!) real value is "<type 'PySide.QtNetwork.QAbstractSocket.SocketError'>"
    SocketOption = None # (!) real value is "<type 'PySide.QtNetwork.QAbstractSocket.SocketOption'>"
    SocketResourceError = PySide.QtNetwork.QAbstractSocket.SocketError.SocketResourceError
    SocketState = None # (!) real value is "<type 'PySide.QtNetwork.QAbstractSocket.SocketState'>"
    SocketTimeoutError = PySide.QtNetwork.QAbstractSocket.SocketError.SocketTimeoutError
    SocketType = None # (!) real value is "<type 'PySide.QtNetwork.QAbstractSocket.SocketType'>"
    SslHandshakeFailedError = PySide.QtNetwork.QAbstractSocket.SocketError.SslHandshakeFailedError
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038B6708>'
    TcpSocket = PySide.QtNetwork.QAbstractSocket.SocketType.TcpSocket
    UdpSocket = PySide.QtNetwork.QAbstractSocket.SocketType.UdpSocket
    UnconnectedState = PySide.QtNetwork.QAbstractSocket.SocketState.UnconnectedState
    UnfinishedSocketOperationError = PySide.QtNetwork.QAbstractSocket.SocketError.UnfinishedSocketOperationError
    UnknownNetworkLayerProtocol = PySide.QtNetwork.QAbstractSocket.NetworkLayerProtocol.UnknownNetworkLayerProtocol
    UnknownSocketError = PySide.QtNetwork.QAbstractSocket.SocketError.UnknownSocketError
    UnknownSocketType = PySide.QtNetwork.QAbstractSocket.SocketType.UnknownSocketType
    UnsupportedSocketOperationError = PySide.QtNetwork.QAbstractSocket.SocketError.UnsupportedSocketOperationError



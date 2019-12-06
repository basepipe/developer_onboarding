# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def addDefaultCaCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def addDefaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def caCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def encryptedBytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def isEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def localCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def mode(self, *args, **kwargs): # real signature unknown
        pass

    def modeChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def peerCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def peerCertificateChain(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyDepth(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def peerVerifyMode(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyName(self, *args, **kwargs): # real signature unknown
        pass

    def privateKey(self, *args, **kwargs): # real signature unknown
        pass

    def protocol(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def sessionCipher(self, *args, **kwargs): # real signature unknown
        pass

    def setCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def setCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyDepth(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyName(self, *args, **kwargs): # real signature unknown
        pass

    def setPrivateKey(self, *args, **kwargs): # real signature unknown
        pass

    def setProtocol(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def socketOption(self, *args, **kwargs): # real signature unknown
        pass

    def sslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def startClientEncryption(self, *args, **kwargs): # real signature unknown
        pass

    def startServerEncryption(self, *args, **kwargs): # real signature unknown
        pass

    def supportedCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def supportsSsl(self, *args, **kwargs): # real signature unknown
        pass

    def systemCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForEncrypted(self, *args, **kwargs): # real signature unknown
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

    AutoVerifyPeer = PySide.QtNetwork.QSslSocket.PeerVerifyMode.AutoVerifyPeer
    PeerVerifyMode = None # (!) real value is "<type 'PySide.QtNetwork.QSslSocket.PeerVerifyMode'>"
    QueryPeer = PySide.QtNetwork.QSslSocket.PeerVerifyMode.QueryPeer
    SslClientMode = PySide.QtNetwork.QSslSocket.SslMode.SslClientMode
    SslMode = None # (!) real value is "<type 'PySide.QtNetwork.QSslSocket.SslMode'>"
    SslServerMode = PySide.QtNetwork.QSslSocket.SslMode.SslServerMode
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038C0F08>'
    UnencryptedMode = PySide.QtNetwork.QSslSocket.SslMode.UnencryptedMode
    VerifyNone = PySide.QtNetwork.QSslSocket.PeerVerifyMode.VerifyNone
    VerifyPeer = PySide.QtNetwork.QSslSocket.PeerVerifyMode.VerifyPeer



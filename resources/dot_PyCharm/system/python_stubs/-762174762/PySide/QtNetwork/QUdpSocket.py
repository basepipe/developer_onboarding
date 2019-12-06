# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    # no doc
    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingDatagrams(self, *args, **kwargs): # real signature unknown
        pass

    def joinMulticastGroup(self, *args, **kwargs): # real signature unknown
        pass

    def leaveMulticastGroup(self, *args, **kwargs): # real signature unknown
        pass

    def multicastInterface(self, *args, **kwargs): # real signature unknown
        pass

    def pendingDatagramSize(self, *args, **kwargs): # real signature unknown
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        pass

    def setMulticastInterface(self, *args, **kwargs): # real signature unknown
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BindFlag = None # (!) real value is "<type 'PySide.QtNetwork.QUdpSocket.BindFlag'>"
    BindMode = None # (!) real value is "<type 'BindMode'>"
    DefaultForPlatform = PySide.QtNetwork.QUdpSocket.BindFlag.DefaultForPlatform
    DontShareAddress = PySide.QtNetwork.QUdpSocket.BindFlag.DontShareAddress
    ReuseAddressHint = PySide.QtNetwork.QUdpSocket.BindFlag.ReuseAddressHint
    ShareAddress = PySide.QtNetwork.QUdpSocket.BindFlag.ShareAddress
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038B6F08>'



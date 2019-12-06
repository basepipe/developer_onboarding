# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkInterface(__Shiboken.Object):
    # no doc
    def addressEntries(self, *args, **kwargs): # real signature unknown
        pass

    def allAddresses(self, *args, **kwargs): # real signature unknown
        pass

    def allInterfaces(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def hardwareAddress(self, *args, **kwargs): # real signature unknown
        pass

    def humanReadableName(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def interfaceFromIndex(self, *args, **kwargs): # real signature unknown
        pass

    def interfaceFromName(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    CanBroadcast = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.CanBroadcast
    CanMulticast = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.CanMulticast
    InterfaceFlag = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkInterface.InterfaceFlag'>"
    InterfaceFlags = None # (!) real value is "<type 'InterfaceFlags'>"
    IsLoopBack = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.IsLoopBack
    IsPointToPoint = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.IsPointToPoint
    IsRunning = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.IsRunning
    IsUp = PySide.QtNetwork.QNetworkInterface.InterfaceFlag.IsUp



# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkConfigurationManager(__PySide_QtCore.QObject):
    # no doc
    def allConfigurations(self, *args, **kwargs): # real signature unknown
        pass

    def capabilities(self, *args, **kwargs): # real signature unknown
        pass

    def configurationAdded(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def configurationChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def configurationFromIdentifier(self, *args, **kwargs): # real signature unknown
        pass

    def configurationRemoved(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def defaultConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def isOnline(self, *args, **kwargs): # real signature unknown
        pass

    def onlineStateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def updateCompleted(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def updateConfigurations(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ApplicationLevelRoaming = PySide.QtNetwork.QNetworkConfigurationManager.Capability.ApplicationLevelRoaming
    CanStartAndStopInterfaces = PySide.QtNetwork.QNetworkConfigurationManager.Capability.CanStartAndStopInterfaces
    Capabilities = None # (!) real value is "<type 'Capabilities'>"
    Capability = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkConfigurationManager.Capability'>"
    DataStatistics = PySide.QtNetwork.QNetworkConfigurationManager.Capability.DataStatistics
    DirectConnectionRouting = PySide.QtNetwork.QNetworkConfigurationManager.Capability.DirectConnectionRouting
    ForcedRoaming = PySide.QtNetwork.QNetworkConfigurationManager.Capability.ForcedRoaming
    NetworkSessionRequired = PySide.QtNetwork.QNetworkConfigurationManager.Capability.NetworkSessionRequired
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038A0F48>'
    SystemSessionSupport = PySide.QtNetwork.QNetworkConfigurationManager.Capability.SystemSessionSupport



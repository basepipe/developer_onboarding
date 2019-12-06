# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkAccessManager(__PySide_QtCore.QObject):
    # no doc
    def activeConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def cache(self, *args, **kwargs): # real signature unknown
        pass

    def configuration(self, *args, **kwargs): # real signature unknown
        pass

    def cookieJar(self, *args, **kwargs): # real signature unknown
        pass

    def createRequest(self, *args, **kwargs): # real signature unknown
        pass

    def deleteResource(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def head(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessible(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessibleChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def networkSessionConnected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def post(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def proxyFactory(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def sendCustomRequest(self, *args, **kwargs): # real signature unknown
        pass

    def setCache(self, *args, **kwargs): # real signature unknown
        pass

    def setConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def setCookieJar(self, *args, **kwargs): # real signature unknown
        pass

    def setNetworkAccessible(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setProxyFactory(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Accessible = PySide.QtNetwork.QNetworkAccessManager.NetworkAccessibility.Accessible
    CustomOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.CustomOperation
    DeleteOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.DeleteOperation
    GetOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.GetOperation
    HeadOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.HeadOperation
    NetworkAccessibility = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkAccessManager.NetworkAccessibility'>"
    NotAccessible = PySide.QtNetwork.QNetworkAccessManager.NetworkAccessibility.NotAccessible
    Operation = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkAccessManager.Operation'>"
    PostOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.PostOperation
    PutOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.PutOperation
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000037D0DC8>'
    UnknownAccessibility = PySide.QtNetwork.QNetworkAccessManager.NetworkAccessibility.UnknownAccessibility
    UnknownOperation = PySide.QtNetwork.QNetworkAccessManager.Operation.UnknownOperation



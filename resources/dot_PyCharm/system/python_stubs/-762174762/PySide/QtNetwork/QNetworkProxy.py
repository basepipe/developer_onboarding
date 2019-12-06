# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QNetworkProxy(__Shiboken.Object):
    # no doc
    def applicationProxy(self, *args, **kwargs): # real signature unknown
        pass

    def capabilities(self, *args, **kwargs): # real signature unknown
        pass

    def hostName(self, *args, **kwargs): # real signature unknown
        pass

    def isCachingProxy(self, *args, **kwargs): # real signature unknown
        pass

    def isTransparentProxy(self, *args, **kwargs): # real signature unknown
        pass

    def password(self, *args, **kwargs): # real signature unknown
        pass

    def port(self, *args, **kwargs): # real signature unknown
        pass

    def setApplicationProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setCapabilities(self, *args, **kwargs): # real signature unknown
        pass

    def setHostName(self, *args, **kwargs): # real signature unknown
        pass

    def setPassword(self, *args, **kwargs): # real signature unknown
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def setUser(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def user(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    CachingCapability = PySide.QtNetwork.QNetworkProxy.Capability.CachingCapability
    Capabilities = None # (!) real value is "<type 'Capabilities'>"
    Capability = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkProxy.Capability'>"
    DefaultProxy = PySide.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy
    FtpCachingProxy = PySide.QtNetwork.QNetworkProxy.ProxyType.FtpCachingProxy
    HostNameLookupCapability = PySide.QtNetwork.QNetworkProxy.Capability.HostNameLookupCapability
    HttpCachingProxy = PySide.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy
    HttpProxy = PySide.QtNetwork.QNetworkProxy.ProxyType.HttpProxy
    ListeningCapability = PySide.QtNetwork.QNetworkProxy.Capability.ListeningCapability
    NoProxy = PySide.QtNetwork.QNetworkProxy.ProxyType.NoProxy
    ProxyType = None # (!) real value is "<type 'PySide.QtNetwork.QNetworkProxy.ProxyType'>"
    Socks5Proxy = PySide.QtNetwork.QNetworkProxy.ProxyType.Socks5Proxy
    TunnelingCapability = PySide.QtNetwork.QNetworkProxy.Capability.TunnelingCapability
    UdpTunnelingCapability = PySide.QtNetwork.QNetworkProxy.Capability.UdpTunnelingCapability



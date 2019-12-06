# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QHostAddress(__Shiboken.Object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def isInSubnet(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def parseSubnet(self, *args, **kwargs): # real signature unknown
        pass

    def protocol(self, *args, **kwargs): # real signature unknown
        pass

    def scopeId(self, *args, **kwargs): # real signature unknown
        pass

    def setAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setScopeId(self, *args, **kwargs): # real signature unknown
        pass

    def toIPv4Address(self, *args, **kwargs): # real signature unknown
        pass

    def toIPv6Address(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
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

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    Any = PySide.QtNetwork.QHostAddress.SpecialAddress.Any
    AnyIPv6 = PySide.QtNetwork.QHostAddress.SpecialAddress.AnyIPv6
    Broadcast = PySide.QtNetwork.QHostAddress.SpecialAddress.Broadcast
    LocalHost = PySide.QtNetwork.QHostAddress.SpecialAddress.LocalHost
    LocalHostIPv6 = PySide.QtNetwork.QHostAddress.SpecialAddress.LocalHostIPv6
    Null = PySide.QtNetwork.QHostAddress.SpecialAddress.Null
    SpecialAddress = None # (!) real value is "<type 'PySide.QtNetwork.QHostAddress.SpecialAddress'>"



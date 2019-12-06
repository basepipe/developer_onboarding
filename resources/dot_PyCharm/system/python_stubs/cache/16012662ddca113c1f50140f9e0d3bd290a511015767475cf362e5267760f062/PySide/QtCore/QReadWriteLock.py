# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QReadWriteLock(__Shiboken.Object):
    # no doc
    def lockForRead(self, *args, **kwargs): # real signature unknown
        pass

    def lockForWrite(self, *args, **kwargs): # real signature unknown
        pass

    def tryLockForRead(self, *args, **kwargs): # real signature unknown
        pass

    def tryLockForWrite(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    NonRecursive = PySide.QtCore.QReadWriteLock.RecursionMode.NonRecursive
    RecursionMode = None # (!) real value is "<type 'PySide.QtCore.QReadWriteLock.RecursionMode'>"
    Recursive = PySide.QtCore.QReadWriteLock.RecursionMode.Recursive



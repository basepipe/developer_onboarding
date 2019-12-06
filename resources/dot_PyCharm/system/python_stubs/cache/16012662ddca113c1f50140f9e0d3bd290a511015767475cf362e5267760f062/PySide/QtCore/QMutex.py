# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QMutex(__Shiboken.Object):
    # no doc
    def lock(self, *args, **kwargs): # real signature unknown
        pass

    def lockInline(self, *args, **kwargs): # real signature unknown
        pass

    def tryLock(self, *args, **kwargs): # real signature unknown
        pass

    def tryLockInline(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, *args, **kwargs): # real signature unknown
        pass

    def unlockInline(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    NonRecursive = PySide.QtCore.QMutex.RecursionMode.NonRecursive
    RecursionMode = None # (!) real value is "<type 'PySide.QtCore.QMutex.RecursionMode'>"
    Recursive = PySide.QtCore.QMutex.RecursionMode.Recursive



# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QSystemSemaphore(__Shiboken.Object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def key(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def setKey(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AccessMode = None # (!) real value is "<type 'PySide.QtCore.QSystemSemaphore.AccessMode'>"
    AlreadyExists = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.AlreadyExists
    Create = PySide.QtCore.QSystemSemaphore.AccessMode.Create
    KeyError = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.KeyError
    NoError = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.NoError
    NotFound = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.NotFound
    Open = PySide.QtCore.QSystemSemaphore.AccessMode.Open
    OutOfResources = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.OutOfResources
    PermissionDenied = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.PermissionDenied
    SystemSemaphoreError = None # (!) real value is "<type 'PySide.QtCore.QSystemSemaphore.SystemSemaphoreError'>"
    UnknownError = PySide.QtCore.QSystemSemaphore.SystemSemaphoreError.UnknownError



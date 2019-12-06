# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QSessionManager(__PySide_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self, *args, **kwargs): # real signature unknown
        pass

    def allowsInteraction(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def discardCommand(self, *args, **kwargs): # real signature unknown
        pass

    def isPhase2(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def requestPhase2(self, *args, **kwargs): # real signature unknown
        pass

    def restartCommand(self, *args, **kwargs): # real signature unknown
        pass

    def restartHint(self, *args, **kwargs): # real signature unknown
        pass

    def sessionId(self, *args, **kwargs): # real signature unknown
        pass

    def sessionKey(self, *args, **kwargs): # real signature unknown
        pass

    def setDiscardCommand(self, *args, **kwargs): # real signature unknown
        pass

    def setManagerProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setRestartCommand(self, *args, **kwargs): # real signature unknown
        pass

    def setRestartHint(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RestartAnyway = PySide.QtGui.QSessionManager.RestartHint.RestartAnyway
    RestartHint = None # (!) real value is "<type 'PySide.QtGui.QSessionManager.RestartHint'>"
    RestartIfRunning = PySide.QtGui.QSessionManager.RestartHint.RestartIfRunning
    RestartImmediately = PySide.QtGui.QSessionManager.RestartHint.RestartImmediately
    RestartNever = PySide.QtGui.QSessionManager.RestartHint.RestartNever
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F41688>'



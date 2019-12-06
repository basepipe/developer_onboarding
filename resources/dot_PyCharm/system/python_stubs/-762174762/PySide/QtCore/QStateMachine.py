# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QState import QState

class QStateMachine(QState):
    # no doc
    def addDefaultAnimation(self, *args, **kwargs): # real signature unknown
        pass

    def addState(self, *args, **kwargs): # real signature unknown
        pass

    def beginMicrostep(self, *args, **kwargs): # real signature unknown
        pass

    def beginSelectTransitions(self, *args, **kwargs): # real signature unknown
        pass

    def cancelDelayedEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearError(self, *args, **kwargs): # real signature unknown
        pass

    def configuration(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAnimations(self, *args, **kwargs): # real signature unknown
        pass

    def endMicrostep(self, *args, **kwargs): # real signature unknown
        pass

    def endSelectTransitions(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def globalRestorePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def isAnimated(self, *args, **kwargs): # real signature unknown
        pass

    def isRunning(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, *args, **kwargs): # real signature unknown
        pass

    def onExit(self, *args, **kwargs): # real signature unknown
        pass

    def postDelayedEvent(self, *args, **kwargs): # real signature unknown
        pass

    def postEvent(self, *args, **kwargs): # real signature unknown
        pass

    def removeDefaultAnimation(self, *args, **kwargs): # real signature unknown
        pass

    def removeState(self, *args, **kwargs): # real signature unknown
        pass

    def setAnimated(self, *args, **kwargs): # real signature unknown
        pass

    def setGlobalRestorePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def stopped(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    DontRestoreProperties = PySide.QtCore.QStateMachine.RestorePolicy.DontRestoreProperties
    Error = None # (!) real value is "<type 'PySide.QtCore.QStateMachine.Error'>"
    EventPriority = None # (!) real value is "<type 'PySide.QtCore.QStateMachine.EventPriority'>"
    HighPriority = PySide.QtCore.QStateMachine.EventPriority.HighPriority
    NoCommonAncestorForTransitionError = PySide.QtCore.QStateMachine.Error.NoCommonAncestorForTransitionError
    NoDefaultStateInHistoryStateError = PySide.QtCore.QStateMachine.Error.NoDefaultStateInHistoryStateError
    NoError = PySide.QtCore.QStateMachine.Error.NoError
    NoInitialStateError = PySide.QtCore.QStateMachine.Error.NoInitialStateError
    NormalPriority = PySide.QtCore.QStateMachine.EventPriority.NormalPriority
    RestorePolicy = None # (!) real value is "<type 'PySide.QtCore.QStateMachine.RestorePolicy'>"
    RestoreProperties = PySide.QtCore.QStateMachine.RestorePolicy.RestoreProperties
    SignalEvent = None # (!) real value is "<type 'PySide.QtCore.QStateMachine.SignalEvent'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F01708>'
    WrappedEvent = None # (!) real value is "<type 'PySide.QtCore.QStateMachine.WrappedEvent'>"



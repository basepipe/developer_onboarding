# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QObject import QObject

class QAbstractAnimation(QObject):
    # no doc
    def currentLoop(self, *args, **kwargs): # real signature unknown
        pass

    def currentLoopChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def currentLoopTime(self, *args, **kwargs): # real signature unknown
        pass

    def currentTime(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self, *args, **kwargs): # real signature unknown
        pass

    def directionChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def duration(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def group(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def setDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setLoopCount(self, *args, **kwargs): # real signature unknown
        pass

    def setPaused(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def totalDuration(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Backward = PySide.QtCore.QAbstractAnimation.Direction.Backward
    DeleteWhenStopped = PySide.QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped
    DeletionPolicy = None # (!) real value is "<type 'PySide.QtCore.QAbstractAnimation.DeletionPolicy'>"
    Direction = None # (!) real value is "<type 'PySide.QtCore.QAbstractAnimation.Direction'>"
    Forward = PySide.QtCore.QAbstractAnimation.Direction.Forward
    KeepWhenStopped = PySide.QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped
    Paused = PySide.QtCore.QAbstractAnimation.State.Paused
    Running = PySide.QtCore.QAbstractAnimation.State.Running
    State = None # (!) real value is "<type 'PySide.QtCore.QAbstractAnimation.State'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E675C8>'
    Stopped = PySide.QtCore.QAbstractAnimation.State.Stopped



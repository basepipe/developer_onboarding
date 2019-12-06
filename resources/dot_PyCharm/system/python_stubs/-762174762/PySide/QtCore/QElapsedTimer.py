# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QElapsedTimer(__Shiboken.Object):
    # no doc
    def clockType(self, *args, **kwargs): # real signature unknown
        pass

    def elapsed(self, *args, **kwargs): # real signature unknown
        pass

    def hasExpired(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate(self, *args, **kwargs): # real signature unknown
        pass

    def isMonotonic(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def msecsSinceReference(self, *args, **kwargs): # real signature unknown
        pass

    def msecsTo(self, *args, **kwargs): # real signature unknown
        pass

    def nsecsElapsed(self, *args, **kwargs): # real signature unknown
        pass

    def restart(self, *args, **kwargs): # real signature unknown
        pass

    def secsTo(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
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

    ClockType = None # (!) real value is "<type 'PySide.QtCore.QElapsedTimer.ClockType'>"
    MachAbsoluteTime = PySide.QtCore.QElapsedTimer.ClockType.MachAbsoluteTime
    MonotonicClock = PySide.QtCore.QElapsedTimer.ClockType.MonotonicClock
    PerformanceCounter = PySide.QtCore.QElapsedTimer.ClockType.PerformanceCounter
    SystemTime = PySide.QtCore.QElapsedTimer.ClockType.SystemTime
    TickCounter = PySide.QtCore.QElapsedTimer.ClockType.TickCounter



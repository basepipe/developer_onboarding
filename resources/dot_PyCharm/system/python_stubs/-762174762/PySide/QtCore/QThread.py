# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QObject import QObject

class QThread(QObject):
    # no doc
    def currentThread(self, *args, **kwargs): # real signature unknown
        pass

    def currentThreadId(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def exit(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def idealThreadCount(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self, *args, **kwargs): # real signature unknown
        pass

    def isRunning(self, *args, **kwargs): # real signature unknown
        pass

    def msleep(self, *args, **kwargs): # real signature unknown
        pass

    def priority(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        pass

    def setStackSize(self, *args, **kwargs): # real signature unknown
        pass

    def setTerminationEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def sleep(self, *args, **kwargs): # real signature unknown
        pass

    def stackSize(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def terminate(self, *args, **kwargs): # real signature unknown
        pass

    def terminated(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def usleep(self, *args, **kwargs): # real signature unknown
        pass

    def wait(self, *args, **kwargs): # real signature unknown
        pass

    def yieldCurrentThread(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    HighestPriority = PySide.QtCore.QThread.Priority.HighestPriority
    HighPriority = PySide.QtCore.QThread.Priority.HighPriority
    IdlePriority = PySide.QtCore.QThread.Priority.IdlePriority
    InheritPriority = PySide.QtCore.QThread.Priority.InheritPriority
    LowestPriority = PySide.QtCore.QThread.Priority.LowestPriority
    LowPriority = PySide.QtCore.QThread.Priority.LowPriority
    NormalPriority = PySide.QtCore.QThread.Priority.NormalPriority
    Priority = None # (!) real value is "<type 'PySide.QtCore.QThread.Priority'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003EF6E88>'
    TimeCriticalPriority = PySide.QtCore.QThread.Priority.TimeCriticalPriority



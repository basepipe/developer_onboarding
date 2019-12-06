# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QObject import QObject

class QEventLoop(QObject):
    # no doc
    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def exit(self, *args, **kwargs): # real signature unknown
        pass

    def isRunning(self, *args, **kwargs): # real signature unknown
        pass

    def processEvents(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def wakeUp(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AllEvents = PySide.QtCore.QEventLoop.ProcessEventsFlag.AllEvents
    DeferredDeletion = PySide.QtCore.QEventLoop.ProcessEventsFlag.DeferredDeletion
    DialogExec = PySide.QtCore.QEventLoop.ProcessEventsFlag.DialogExec
    EventLoopExec = PySide.QtCore.QEventLoop.ProcessEventsFlag.EventLoopExec
    ExcludeSocketNotifiers = PySide.QtCore.QEventLoop.ProcessEventsFlag.ExcludeSocketNotifiers
    ExcludeUserInputEvents = PySide.QtCore.QEventLoop.ProcessEventsFlag.ExcludeUserInputEvents
    ProcessEventsFlag = None # (!) real value is "<type 'PySide.QtCore.QEventLoop.ProcessEventsFlag'>"
    ProcessEventsFlags = None # (!) real value is "<type 'ProcessEventsFlags'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E806C8>'
    WaitForMoreEvents = PySide.QtCore.QEventLoop.ProcessEventsFlag.WaitForMoreEvents
    X11ExcludeTimers = PySide.QtCore.QEventLoop.ProcessEventsFlag.X11ExcludeTimers



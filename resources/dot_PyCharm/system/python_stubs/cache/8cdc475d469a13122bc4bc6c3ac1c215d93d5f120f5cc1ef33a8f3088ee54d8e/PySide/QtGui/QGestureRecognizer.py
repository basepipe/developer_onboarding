# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QGestureRecognizer(__Shiboken.Object):
    # no doc
    def create(self, *args, **kwargs): # real signature unknown
        pass

    def recognize(self, *args, **kwargs): # real signature unknown
        pass

    def registerRecognizer(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterRecognizer(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    CancelGesture = PySide.QtGui.QGestureRecognizer.ResultFlag.CancelGesture
    ConsumeEventHint = PySide.QtGui.QGestureRecognizer.ResultFlag.ConsumeEventHint
    FinishGesture = PySide.QtGui.QGestureRecognizer.ResultFlag.FinishGesture
    Ignore = PySide.QtGui.QGestureRecognizer.ResultFlag.Ignore
    MayBeGesture = PySide.QtGui.QGestureRecognizer.ResultFlag.MayBeGesture
    Result = None # (!) real value is "<type 'Result'>"
    ResultFlag = None # (!) real value is "<type 'PySide.QtGui.QGestureRecognizer.ResultFlag'>"
    ResultHint_Mask = PySide.QtGui.QGestureRecognizer.ResultFlag.ResultHint_Mask
    ResultState_Mask = PySide.QtGui.QGestureRecognizer.ResultFlag.ResultState_Mask
    TriggerGesture = PySide.QtGui.QGestureRecognizer.ResultFlag.TriggerGesture



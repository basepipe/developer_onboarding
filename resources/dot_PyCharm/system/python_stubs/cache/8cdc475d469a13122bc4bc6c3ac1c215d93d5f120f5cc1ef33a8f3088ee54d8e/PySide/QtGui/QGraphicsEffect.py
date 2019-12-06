# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QGraphicsEffect(__PySide_QtCore.QObject):
    # no doc
    def boundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def boundingRectFor(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, *args, **kwargs): # real signature unknown
        pass

    def drawSource(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def sourceBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sourceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def sourcePixmap(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def updateBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ChangeFlag = None # (!) real value is "<type 'PySide.QtGui.QGraphicsEffect.ChangeFlag'>"
    ChangeFlags = None # (!) real value is "<type 'ChangeFlags'>"
    NoPad = PySide.QtGui.QGraphicsEffect.PixmapPadMode.NoPad
    PadToEffectiveBoundingRect = PySide.QtGui.QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect
    PadToTransparentBorder = PySide.QtGui.QGraphicsEffect.PixmapPadMode.PadToTransparentBorder
    PixmapPadMode = None # (!) real value is "<type 'PySide.QtGui.QGraphicsEffect.PixmapPadMode'>"
    SourceAttached = PySide.QtGui.QGraphicsEffect.ChangeFlag.SourceAttached
    SourceBoundingRectChanged = PySide.QtGui.QGraphicsEffect.ChangeFlag.SourceBoundingRectChanged
    SourceDetached = PySide.QtGui.QGraphicsEffect.ChangeFlag.SourceDetached
    SourceInvalidated = PySide.QtGui.QGraphicsEffect.ChangeFlag.SourceInvalidated
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F56588>'



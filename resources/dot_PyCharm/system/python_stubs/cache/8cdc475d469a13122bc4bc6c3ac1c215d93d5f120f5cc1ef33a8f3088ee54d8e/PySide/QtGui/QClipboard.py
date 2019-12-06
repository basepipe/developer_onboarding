# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QClipboard(__PySide_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def findBufferChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def image(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, *args, **kwargs): # real signature unknown
        pass

    def ownsClipboard(self, *args, **kwargs): # real signature unknown
        pass

    def ownsFindBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def ownsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setImage(self, *args, **kwargs): # real signature unknown
        pass

    def setMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def setPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        pass

    def supportsFindBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def supportsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clipboard = PySide.QtGui.QClipboard.Mode.Clipboard
    FindBuffer = PySide.QtGui.QClipboard.Mode.FindBuffer
    LastMode = PySide.QtGui.QClipboard.Mode.LastMode
    Mode = None # (!) real value is "<type 'PySide.QtGui.QClipboard.Mode'>"
    Selection = PySide.QtGui.QClipboard.Mode.Selection
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F19348>'



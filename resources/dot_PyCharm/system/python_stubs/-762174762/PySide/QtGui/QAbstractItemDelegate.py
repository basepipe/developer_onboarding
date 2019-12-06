# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QAbstractItemDelegate(__PySide_QtCore.QObject):
    # no doc
    def closeEditor(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def createEditor(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def helpEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def setModelData(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def updateEditorGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    EditNextItem = PySide.QtGui.QAbstractItemDelegate.EndEditHint.EditNextItem
    EditPreviousItem = PySide.QtGui.QAbstractItemDelegate.EndEditHint.EditPreviousItem
    EndEditHint = None # (!) real value is "<type 'PySide.QtGui.QAbstractItemDelegate.EndEditHint'>"
    NoHint = PySide.QtGui.QAbstractItemDelegate.EndEditHint.NoHint
    RevertModelCache = PySide.QtGui.QAbstractItemDelegate.EndEditHint.RevertModelCache
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F630C8>'
    SubmitModelCache = PySide.QtGui.QAbstractItemDelegate.EndEditHint.SubmitModelCache



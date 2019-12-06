# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QItemSelectionModel(__PySide_QtCore.QObject):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearSelection(self, *args, **kwargs): # real signature unknown
        pass

    def columnIntersectsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def currentColumnChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def currentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def emitSelectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self, *args, **kwargs): # real signature unknown
        pass

    def isColumnSelected(self, *args, **kwargs): # real signature unknown
        pass

    def isRowSelected(self, *args, **kwargs): # real signature unknown
        pass

    def isSelected(self, *args, **kwargs): # real signature unknown
        pass

    def model(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def rowIntersectsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectedColumns(self, *args, **kwargs): # real signature unknown
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedRows(self, *args, **kwargs): # real signature unknown
        pass

    def selection(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setCurrentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Clear = PySide.QtGui.QItemSelectionModel.SelectionFlag.Clear
    ClearAndSelect = PySide.QtGui.QItemSelectionModel.SelectionFlag.ClearAndSelect
    Columns = PySide.QtGui.QItemSelectionModel.SelectionFlag.Columns
    Current = PySide.QtGui.QItemSelectionModel.SelectionFlag.Current
    Deselect = PySide.QtGui.QItemSelectionModel.SelectionFlag.Deselect
    NoUpdate = PySide.QtGui.QItemSelectionModel.SelectionFlag.NoUpdate
    Rows = PySide.QtGui.QItemSelectionModel.SelectionFlag.Rows
    Select = PySide.QtGui.QItemSelectionModel.SelectionFlag.Select
    SelectCurrent = PySide.QtGui.QItemSelectionModel.SelectionFlag.SelectCurrent
    SelectionFlag = None # (!) real value is "<type 'PySide.QtGui.QItemSelectionModel.SelectionFlag'>"
    SelectionFlags = None # (!) real value is "<type 'SelectionFlags'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F50388>'
    Toggle = PySide.QtGui.QItemSelectionModel.SelectionFlag.Toggle
    ToggleCurrent = PySide.QtGui.QItemSelectionModel.SelectionFlag.ToggleCurrent



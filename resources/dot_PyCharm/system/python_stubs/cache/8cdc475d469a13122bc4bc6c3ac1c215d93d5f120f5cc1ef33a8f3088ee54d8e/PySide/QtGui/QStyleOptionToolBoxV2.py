# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QStyleOptionToolBox import QStyleOptionToolBox

class QStyleOptionToolBoxV2(QStyleOptionToolBox):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectedPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Beginning = PySide.QtGui.QStyleOptionToolBoxV2.TabPosition.Beginning
    End = PySide.QtGui.QStyleOptionToolBoxV2.TabPosition.End
    Middle = PySide.QtGui.QStyleOptionToolBoxV2.TabPosition.Middle
    NextIsSelected = PySide.QtGui.QStyleOptionToolBoxV2.SelectedPosition.NextIsSelected
    NotAdjacent = PySide.QtGui.QStyleOptionToolBoxV2.SelectedPosition.NotAdjacent
    OnlyOneTab = PySide.QtGui.QStyleOptionToolBoxV2.TabPosition.OnlyOneTab
    PreviousIsSelected = PySide.QtGui.QStyleOptionToolBoxV2.SelectedPosition.PreviousIsSelected
    SelectedPosition = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionToolBoxV2.SelectedPosition'>"
    StyleOptionVersion = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionToolBoxV2.StyleOptionVersion'>"
    TabPosition = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionToolBoxV2.TabPosition'>"
    Version = PySide.QtGui.QStyleOptionToolBoxV2.StyleOptionVersion.Version



# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QStyleOption import QStyleOption

class QStyleOptionTab(QStyleOption):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    cornerWidgets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectedPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Beginning = PySide.QtGui.QStyleOptionTab.TabPosition.Beginning
    CornerWidget = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionTab.CornerWidget'>"
    CornerWidgets = None # (!) real value is "<type 'CornerWidgets'>"
    End = PySide.QtGui.QStyleOptionTab.TabPosition.End
    LeftCornerWidget = PySide.QtGui.QStyleOptionTab.CornerWidget.LeftCornerWidget
    Middle = PySide.QtGui.QStyleOptionTab.TabPosition.Middle
    NextIsSelected = PySide.QtGui.QStyleOptionTab.SelectedPosition.NextIsSelected
    NoCornerWidgets = PySide.QtGui.QStyleOptionTab.CornerWidget.NoCornerWidgets
    NotAdjacent = PySide.QtGui.QStyleOptionTab.SelectedPosition.NotAdjacent
    OnlyOneTab = PySide.QtGui.QStyleOptionTab.TabPosition.OnlyOneTab
    PreviousIsSelected = PySide.QtGui.QStyleOptionTab.SelectedPosition.PreviousIsSelected
    RightCornerWidget = PySide.QtGui.QStyleOptionTab.CornerWidget.RightCornerWidget
    SelectedPosition = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionTab.SelectedPosition'>"
    StyleOptionType = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionTab.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionTab.StyleOptionVersion'>"
    TabPosition = None # (!) real value is "<type 'PySide.QtGui.QStyleOptionTab.TabPosition'>"
    Type = PySide.QtGui.QStyleOptionTab.StyleOptionType.Type
    Version = PySide.QtGui.QStyleOptionTab.StyleOptionVersion.Version



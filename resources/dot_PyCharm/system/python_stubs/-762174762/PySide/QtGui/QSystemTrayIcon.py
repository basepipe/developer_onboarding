# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QSystemTrayIcon(__PySide_QtCore.QObject):
    # no doc
    def activated(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def contextMenu(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def geometry(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def isSystemTrayAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def messageClicked(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setContextMenu(self, *args, **kwargs): # real signature unknown
        pass

    def setIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setToolTip(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def showMessage(self, *args, **kwargs): # real signature unknown
        pass

    def supportsMessages(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    ActivationReason = None # (!) real value is "<type 'PySide.QtGui.QSystemTrayIcon.ActivationReason'>"
    Context = PySide.QtGui.QSystemTrayIcon.ActivationReason.Context
    Critical = PySide.QtGui.QSystemTrayIcon.MessageIcon.Critical
    DoubleClick = PySide.QtGui.QSystemTrayIcon.ActivationReason.DoubleClick
    Information = PySide.QtGui.QSystemTrayIcon.MessageIcon.Information
    MessageIcon = None # (!) real value is "<type 'PySide.QtGui.QSystemTrayIcon.MessageIcon'>"
    MiddleClick = PySide.QtGui.QSystemTrayIcon.ActivationReason.MiddleClick
    NoIcon = PySide.QtGui.QSystemTrayIcon.MessageIcon.NoIcon
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003F604C8>'
    Trigger = PySide.QtGui.QSystemTrayIcon.ActivationReason.Trigger
    Unknown = PySide.QtGui.QSystemTrayIcon.ActivationReason.Unknown
    Warning = PySide.QtGui.QSystemTrayIcon.MessageIcon.Warning


